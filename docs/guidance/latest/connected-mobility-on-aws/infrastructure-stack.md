

# Networking and caching
<a name="infrastructure-stack"></a>

The networking and caching layer provides the foundational infrastructure required by other components in the guidance.

## VPC configuration
<a name="vpc-configuration"></a>

The stack creates an Amazon VPC with the following configuration:

 **Network topology:** 
+ CIDR block: 10.0.0.0/16 (customizable)
+ Availability Zones: 2
+ Public subnets: 2 (one per AZ)
+ Private subnets: 2 (one per AZ)
+ NAT Gateways: 2 (one per AZ for high availability)
+ Internet Gateway: 1

 **Subnet allocation:** 
+ Public subnets (10.0.0.0/24, 10.0.1.0/24): Host NAT Gateways and internet-facing resources
+ Private subnets (10.0.128.0/24, 10.0.129.0/24): Host MSK cluster, ElastiCache, and other internal resources

 **Security:** 
+ Security groups restrict traffic between components
+ Network ACLs provide subnet-level protection
+ VPC Flow Logs capture network traffic for analysis

## ElastiCache configuration — Last Known State (LKS)
<a name="elasticache-configuration"></a>

Amazon ElastiCache for Redis serves as the Last Known State (LKS) store for the guidance. LKS is a core pattern in connected vehicle platforms: it maintains the most recent value of every signal for every vehicle, enabling sub-second lookups without querying the telemetry database.

### Why Redis for Last Known State
<a name="why-redis-for-lks"></a>

Connected vehicle platforms face a fundamental read/write asymmetry: telemetry arrives at high frequency (every 1-5 seconds per vehicle), but the Fleet Manager UI and APIs only need the *current* value of each signal. Querying DynamoDB for the latest telemetry record on every page load would be expensive and slow at scale.

Redis solves this by maintaining a single, continuously updated snapshot of each vehicle’s state:
+  **Sub-millisecond reads** — Hash lookups return in <1ms, enabling real-time dashboards
+  **High write throughput** — Flink processors pipeline multiple HSET commands per telemetry message
+  **Built-in TTL** — Stale vehicle state expires automatically when a vehicle goes offline
+  **Geospatial indexing** — GEOADD/GEOSEARCH enables map-based vehicle proximity queries without a separate spatial database
+  **Stream data type** — XADD provides a capped time-series per vehicle for sparkline charts without a separate time-series store

The alternative — querying DynamoDB with `LIMIT 1` sorted by timestamp — would require a GSI per vehicle and would not support geospatial queries or streaming history.

### Cluster configuration
<a name="lks-cluster-configuration"></a>
+ Engine: Redis 7.0
+ Node type: cache.t3.micro (development) or cache.r6g.large (production)
+ Deployment: Multi-AZ replication group with automatic failover (primary \+ replica across 2 AZs)
+ Subnet group: Private subnets only (same subnet group as MSK)
+ Encryption: At rest enabled, in transit disabled (Flink Jedis client compatibility)
+ Failover: Automatic — if the primary node fails, the replica is promoted within seconds. The primary endpoint DNS record updates transparently, so no client configuration changes are needed.

### Data model
<a name="lks-data-model"></a>

The LKS store uses five Redis data structures per vehicle, plus a shared signal catalog and geospatial index.

 **Per-vehicle keys:** 


| Redis Key | Type | Content | 
| --- | --- | --- | 
|  `vehicle:{vehicleId}:signals`  | HASH | All signal values keyed by signal ID (e.g., `1` → `65.5`, `2` → `2400`) | 
|  `vehicle:{vehicleId}:timestamps`  | HASH | Per-signal last-update timestamp in epoch milliseconds | 
|  `vehicle:{vehicleId}:meta`  | HASH | Connection state (`connectionStatus`, `lastSeenAt`, `tripId`, `driverId`, `source`) | 
|  `vehicle:{vehicleId}:stream`  | STREAM | Time-series of signal snapshots, capped at 100 entries (for UI sparkline charts) | 
|  `vehicle:locations`  | GEO (sorted set) | Geospatial index of all active vehicles by longitude/latitude | 

 **Signal catalog keys:** 


| Redis Key | Type | Content | 
| --- | --- | --- | 
|  `signal_catalog:map`  | HASH | JSON field name → signal ID mapping (e.g., `speed` → `1`) | 
|  `signal_catalog:reverse`  | HASH | Signal ID → metadata string: `name\|vssPath\|unit\|dataType` (e.g., `1` → `speed\|Vehicle.Speed\|mph\|float`) | 

 **Example — vehicle state in Redis:** 

```
# Signal values (HGETALL vehicle:VEH-0049:signals)
1  → "65.5"       # speed (mph)
2  → "2400"       # engineRPM
3  → "195.2"      # engineTemp (°F)
4  → "true"       # ignitionOn
23 → "32.1"       # tirePressureFrontLeft (PSI)
33 → "40.7128"    # lat
34 → "-74.0060"   # lng

# Metadata (HGETALL vehicle:VEH-0049:meta)
connectionStatus → "connected"
lastSeenAt       → "1709751600000"
tripId           → "VEH-0049-1709751600000-fc9567"
driverId         → "DRV-001"
source           → "fleetwise"
```

### Write path — Flink to Redis
<a name="lks-write-path"></a>

The `EventDrivenTelemetryProcessor` Flink application writes to Redis on every telemetry message using a Jedis pipeline (single round-trip for all commands):

1. Parse incoming telemetry JSON and resolve field names to signal IDs using the signal catalog

1.  `HSET vehicle:{id}:signals` — update all signal values

1.  `HSET vehicle:{id}:timestamps` — update per-signal timestamps

1.  `HSET vehicle:{id}:meta` — update connection status, trip ID, driver ID, source

1.  `XADD vehicle:{id}:stream` — append to capped stream (MAXLEN \~100)

1.  `GEOADD vehicle:locations` — update geospatial position (if lat/lng present)

1.  `EXPIRE` on all keys — reset TTL on each write

1. On ignition off or ENGINE\_STOP: `ZREM vehicle:locations` — remove from geo index

The `SignalCatalogLoader` loads the signal catalog from DynamoDB on Flink startup and writes it to `signal_catalog:map` and `signal_catalog:reverse` in Redis. It checks a version key for hot-reload without restarting the Flink application.

### Read path — API to Redis
<a name="lks-read-path"></a>

The Fleet Manager API Lambda reads LKS data through two mechanisms:

 **Vehicle detail view:** When the UI requests a vehicle’s details, the Lambda calls `_build_live_vehicle_state()` which reads three hashes (`signals`, `timestamps`, `meta`) via HGETALL and overlays the live state onto the DynamoDB vehicle record. Signal IDs are resolved to human-readable names using the `signal_catalog:reverse` hash. This provides the UI with current speed, location, engine state, and all other signals without querying the telemetry table.

 **Map view:** The Fleet Manager map uses `GEOSEARCH vehicle:locations FROMLONLAT {lng} {lat} BYRADIUS {km} km` to find all vehicles within a geographic area. This returns vehicle IDs with coordinates, which the UI plots on the map. No DynamoDB scan is needed.

 **Redis client:** The Lambda uses a minimal raw-socket RESP client (`_RedisClient`) that requires no external dependencies. It supports HGETALL, XRANGE, and GEOSEARCH commands. The client caches Redis availability for 60 seconds to avoid repeated connection timeouts if Redis is unreachable, and falls back gracefully to DynamoDB-only responses.

### TTL and lifecycle
<a name="lks-ttl-policy"></a>
+ All per-vehicle keys expire after 5 minutes of inactivity (configurable via `REDIS_TTL` in the Flink application)
+ Each telemetry message resets the TTL, so active vehicles never expire
+ When a vehicle stops sending telemetry, its state expires automatically
+ The geo index entry is explicitly removed on ignition off, so the map view only shows active vehicles
+ The signal catalog keys do not expire (they are refreshed on Flink startup or version change)

## VPC endpoints
<a name="vpc-endpoints"></a>

The stack creates VPC endpoints for private connectivity to AWS services:
+ DynamoDB: Gateway endpoint (no cost)
+ S3: Gateway endpoint (no cost)
+ IoT Core: Interface endpoint
+ Kinesis Data Analytics: Interface endpoint
+ CloudWatch Logs: Interface endpoint