

# Last Known State pattern
<a name="last-known-state-pattern"></a>

Connected vehicle platforms face a fundamental read/write asymmetry: telemetry arrives at high frequency (every 1-3 seconds per vehicle), but the Fleet Manager UI only needs the *current* value of each signal. Querying DynamoDB for the latest telemetry record on every page load would be expensive and slow at scale.

The Last Known State (LKS) pattern solves this by maintaining a continuously updated snapshot of each vehicle’s state in Redis.

## Write path
<a name="lks-write-path-detail"></a>

The EventDrivenTelemetryProcessor writes to Redis on every telemetry message using a Jedis pipeline (single network round-trip for all commands):

1. Parse the incoming telemetry JSON.

1. Resolve field names to numeric signal IDs using the signal catalog (cached from `signal_catalog:map`).

1.  `HSET vehicle:{id}:signals` — Update all signal values.

1.  `HSET vehicle:{id}:timestamps` — Update per-signal timestamps in epoch milliseconds.

1.  `HSET vehicle:{id}:meta` — Update connection status, trip ID, driver ID, and telemetry source (`mqtt_direct` or `fleetwise`).

1.  `XADD vehicle:{id}:stream MAXLEN ~100` — Append a snapshot to the capped stream (used for UI sparkline charts).

1.  `GEOADD vehicle:locations` — Update the vehicle’s position in the geospatial index (if lat/lng present).

1.  `EXPIRE` on all keys — Reset TTL to 5 minutes on each write.

1. On ignition OFF: `ZREM vehicle:locations` — Remove from the geo index so the map only shows active vehicles.

## Read path
<a name="lks-read-path-detail"></a>

The Fleet Manager API Lambda reads LKS data through two mechanisms:

 **Vehicle detail view:** The Lambda calls `HGETALL` on three hashes (`signals`, `timestamps`, `meta`) and overlays the live state onto the DynamoDB vehicle record. Signal IDs are resolved to human-readable names using the `signal_catalog:reverse` hash. This provides the UI with current speed, location, engine state, and all other signals without querying the telemetry table.

 **Map view:** The Lambda calls `GEOSEARCH vehicle:locations FROMLONLAT {lng} {lat} BYRADIUS {km} km` to find all vehicles within a geographic area. This returns vehicle IDs with coordinates, which the UI plots on the map. No DynamoDB scan is needed.

 **Sparkline charts:** The Lambda calls `XRANGE vehicle:{id}:stream` to retrieve the last 100 signal snapshots for rendering mini time-series charts in the vehicle detail view.

## TTL and lifecycle
<a name="lks-ttl-lifecycle"></a>
+ All per-vehicle keys expire after 5 minutes of inactivity (configurable via `REDIS_TTL`).
+ Each telemetry message resets the TTL, so active vehicles never expire.
+ When a vehicle stops sending telemetry, its state expires automatically — the map view clears, and the vehicle detail page falls back to DynamoDB-only data.
+ The geo index entry is explicitly removed on ignition OFF, so the map shows only vehicles with active trips.
+ The signal catalog keys (`signal_catalog:map`, `signal_catalog:reverse`) do not expire — they are refreshed on Flink startup or when the version key changes.

## Graceful fallback
<a name="lks-fallback"></a>

The Fleet Manager API Lambda uses a minimal raw-socket RESP client that caches Redis availability for 60 seconds. If Redis is unreachable (ElastiCache maintenance, network issue), the Lambda falls back gracefully to DynamoDB-only responses. The UI still works — it just shows slightly stale data from the last DynamoDB write instead of real-time Redis state.