

# Data plane — Message streaming
<a name="data-plane"></a>

The data plane handles the real-time flow of vehicle telemetry from edge devices through the processing pipeline to storage and consumption. Every message follows the same path regardless of source: ingestion → normalization → routing → storage \+ real-time state.

![Cloud-Native Data Plane for Dynamic Vehicle Data Collection](http://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/cloud-native-data-plane-dynamic-data-collection.png)


## Ingestion layer
<a name="ingestion-layer"></a>

Telemetry enters the platform through AWS IoT Core and lands on source-specific Amazon MSK (Kafka) topics. The solution uses [IoT Core Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html) to reduce messaging costs by bypassing the IoT message broker and routing telemetry directly to IoT Rule actions.

### Basic Ingest
<a name="basic-ingest"></a>

Standard IoT Core messaging charges per message when data passes through the message broker (publish \+ rule evaluation). Basic Ingest eliminates the broker hop — vehicles publish directly to a rule topic (`$aws/rules/{rule_name}/{vin}`), and the message is delivered straight to the rule action (in this case, the MSK Kafka topic) without incurring message broker charges. For high-volume telemetry workloads (thousands of vehicles publishing every 1-3 seconds), this significantly reduces IoT Core costs.

The simulator publishes to `$aws/rules/cms_{stage}_iot_msk_rule/{vin}` instead of `cms/telemetry/{vin}`. The IoT Rule still evaluates the SQL statement and routes to MSK, but the message never touches the broker. Vehicles that need to publish to multiple subscribers (for example, device shadow updates or command responses) still use standard MQTT topics.

For more details, see [Reducing messaging costs with Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html) in the AWS IoT Core Developer Guide.

### MQTT Direct path
<a name="mqtt-direct-path"></a>

 **MQTT Direct path:** 

### MQTT Direct path
<a name="mqtt-direct-path-2"></a>

1. Vehicle (or simulator) publishes gzip\+base64-encoded JSON to the Basic Ingest topic `$aws/rules/cms_{stage}_iot_msk_rule/{vin}`, bypassing the IoT message broker.

1. IoT Rule `cms_{stage}_iot_msk_rule` evaluates the SQL statement and routes the raw payload to MSK topic `cms-telemetry-raw` via a VPC destination. The VPC destination connects IoT Core to the MSK cluster in the private subnet using the MSK security group.

1. IoT Core authenticates to MSK using SCRAM-SHA-512 credentials stored in AWS Secrets Manager. This is the only component that uses SCRAM — all other consumers use IAM authentication.

### FleetWise Edge path
<a name="fleetwise-edge-path"></a>

1. The [FWE agent](https://github.com/aws/aws-iot-fleetwise-edge) (open source) on the vehicle collects CAN bus signals based on the active collection scheme, encodes them as protobuf (snappy-compressed), and publishes to IoT Core topic `cms/fleetwise/vehicles/{vin}/signals`.

1. IoT Rule `fw_{stage}_iot_msk_rule` matches `cms/fleetwise/vehicles/+/signals`, base64-encodes the binary payload (preserving the protobuf), extracts the VIN from `topic(4)`, and routes to MSK topic `fw-telemetry-raw`.

1. A separate IoT Rule routes FWE agent checkins from `cms/fleetwise/vehicles/+/checkins` to MSK topic `fw-checkin` for the CampaignSyncProcessor.

## Normalization layer (Apache Flink)
<a name="normalization-layer-apache-flink"></a>

Three Flink preprocessors read from the source-specific topics and output canonical JSON to a single shared topic (`cms-telemetry-preprocessed`). All Flink applications authenticate to MSK using IAM (no secrets required — the Flink execution role has `kafka-cluster:*` permissions).

 **SimulatorPreprocessor:** 
+ Reads from `cms-telemetry-raw` 
+ Base64-decodes and gunzip-decompresses each message
+ Validates the resulting JSON
+ Writes clean JSON to `cms-telemetry-preprocessed` 
+ No field mapping needed — the simulator already uses canonical field names from the signal catalog

 **FWTelemetryProcessor:** 
+ Reads from `fw-telemetry-raw` 
+ Decodes the protobuf payload using the `VehicleData.proto` schema (snappy decompression first)
+ Resolves integer signal IDs to VSS-path fully qualified names using the decoder manifest (cached from DynamoDB)
+ Maps VSS paths to canonical `json_field` names using the signal catalog (cached in Redis)
+ Resolves VIN to `vehicleId` using the vehicles DynamoDB table
+ Writes canonical JSON to `cms-telemetry-preprocessed` 

 **OEMTelemetryProcessor:** 
+ Reads from `cms-telemetry-oem` 
+ Extracts the `oem_source` field to select the correct transform manifest from S3 (cached)
+ Applies JSONPath-based field extraction, unit conversions (m/s→mph, °C→°F, kPa→PSI), and value mappings
+ Writes canonical JSON to `cms-telemetry-preprocessed` 

## Routing layer (EventDrivenTelemetryProcessor)
<a name="routing-layer-eventdriventelemetryprocessor"></a>

The `EventDrivenTelemetryProcessor` reads every message from `cms-telemetry-preprocessed` and fans out to multiple destinations in a single pass:

 **Redis writes** (pipelined, single round-trip per message):
+  `HSET vehicle:{id}:signals` — All signal values keyed by numeric signal ID
+  `HSET vehicle:{id}:timestamps` — Per-signal last-update timestamp in epoch milliseconds
+  `HSET vehicle:{id}:meta` — Connection status, current trip ID, driver ID, telemetry source
+  `XADD vehicle:{id}:stream MAXLEN ~100` — Append to capped stream for sparkline charts
+  `GEOADD vehicle:locations` — Update GPS position in the geospatial index (if lat/lng present)
+  `EXPIRE` on all keys — 7-day TTL for last known state persistence
+ On ignition OFF: `ZREM vehicle:locations` — Remove from geo index so the map shows only active vehicles

 **Kafka topic routing:** 
+  `cms-telemetry-processed` — Persistence topic for all processed telemetry
+  `cms-telemetry-trips` — Consumed by TripProcessor for trip detection and completion
+  `cms-telemetry-safety` — Consumed by SafetyProcessor for hard braking, speeding, seatbelt events
+  `cms-telemetry-maintenance` — Consumed by MaintenanceProcessor for engine temp, tire pressure, battery alerts
+  `cms-fleet-{fleetId}-telemetry` — Per-fleet topic for real-time distribution to fleet operators via WebSocket

 **Fleet routing:** 

For each message, the processor looks up `vehicleId → fleetId` from the fleet enrollment table. The lookup uses a two-tier cache: Redis first (5-minute TTL), then DynamoDB GSI (`vehicleId-index`) as fallback. The `fleetId` is injected into the message payload before writing to the per-fleet topic. Vehicles not enrolled in any fleet are routed to `cms-telemetry-unassigned`.

## Storage layer
<a name="storage-layer"></a>

 **Amazon DynamoDB** — Trip records, safety events, maintenance alerts, and vehicle metadata are written by the domain-specific Flink processors (TripProcessor, SafetyProcessor, MaintenanceProcessor). DynamoDB is accessed via VPC Gateway Endpoint — no NAT gateway traffic.

 **Amazon ElastiCache (Redis)** — Latest vehicle state for sub-millisecond REST API lookups. The Fleet Manager API Lambda reads from Redis using `HGETALL` (signals, timestamps, meta), `GEOSEARCH` (vehicle locations for map view), and `XRANGE` (sparkline history). Redis runs as a multi-AZ replication group (primary \+ replica across 2 AZs) with automatic failover.

 **Amazon S3** — Iceberg sink for historical analytics, partitioned by `fleetId` and day. Queryable via Amazon Athena with Lake Formation row-level security.