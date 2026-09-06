

# Stream processing
<a name="flink-stack"></a>

The stream processing layer deploys ten independent Flink applications on Amazon Managed Service for Apache Flink for real-time telemetry processing, plus two additional applications for FleetWise Edge integration. Each application consumes from a dedicated Kafka topic and writes to its own DynamoDB table, ensuring separation of concerns and independent scaling.

## Flink applications
<a name="flink-applications"></a>

Ten applications process different aspects of telemetry data. All share a single JAR artifact with a `UniversalProcessor` entry point that routes to the correct processor class based on application configuration.


| Application | Kafka Topic | DynamoDB Table | Purpose | 
| --- | --- | --- | --- | 
| SimulatorPreprocessor |  `cms-telemetry-raw`  | — | Decodes gzip\+base64 telemetry from the simulator, outputs clean JSON to `cms-telemetry-preprocessed`  | 
| EventDrivenTelemetryProcessor |  `cms-telemetry-preprocessed`  | — | Routes messages to domain-specific topics and writes Last Known State to Redis | 
| TelemetryProcessor |  `cms-telemetry-preprocessed`  |  `cms-dev-storage-telemetry`  | Writes telemetry records, tags with tripId | 
| TripProcessor |  `cms-telemetry-trips`  |  `cms-dev-storage-trips`  | Trip lifecycle (create/update/complete) | 
| SafetyProcessor |  `cms-telemetry-safety`  |  `cms-dev-storage-safety-events`  | Safety event detection | 
| MaintenanceProcessor |  `cms-telemetry-maintenance`  |  `cms-dev-storage-maintenance-alerts`  | Maintenance alert generation | 
| FWTelemetryProcessor |  `fw-telemetry-raw`  | — | Decodes FWE protobuf, maps CAN signals to standard format, outputs to `cms-telemetry-preprocessed`  | 
| CampaignSyncProcessor |  `fw-checkin`  |  `cms-dev-campaigns`  | Resolves campaigns, pushes decoder manifests and collection schemes to FWE agents via IoT Core MQTT | 
| GeofenceProcessor |  `cms-telemetry-preprocessed`  |  `cms-dev-storage-geofences` / `cms-dev-storage-safety-events`  | Evaluates vehicle positions against active geofences, generates boundary crossing events | 
| OEMTelemetryProcessor |  `cms-telemetry-oem`  | — | Transforms OEM-specific telemetry to standard format using S3-hosted transform manifests, outputs to `cms-telemetry-raw`  | 

### FleetWise telemetry processor
<a name="fleetwise-telemetry-processor"></a>

The FWTelemetryProcessor decodes protobuf-encoded telemetry uploaded by FleetWise Edge agents. It reads the decoder manifest from DynamoDB to map CAN signal IDs to human-readable signal names (for example, signal ID 1 maps to `Vehicle.Speed`), converts units to the standard format, and outputs JSON records to the `cms-telemetry-preprocessed` Kafka topic. This enables the same downstream processors (TripProcessor, SafetyProcessor, MaintenanceProcessor) to process FleetWise telemetry without modification.

The processor maps all 66 signals defined in the decoder manifest, including speed, engine temperature, tire pressure (all four wheels), battery voltage, GPS coordinates, and ignition status.

### Campaign sync processor
<a name="campaign-sync-processor"></a>

The CampaignSyncProcessor manages the FleetWise Edge agent lifecycle:

1. Agent publishes a checkin protobuf to `cms/fleetwise/vehicles/{vin}/checkins` 

1. IoT Rule routes the checkin to the `fw-checkin` Kafka topic

1. CampaignSyncProcessor consumes the checkin and extracts the vehicle VIN

1. Processor queries the `cms-dev-campaigns` DynamoDB table for active campaigns targeting the vehicle

1. Processor generates protobuf decoder manifest and collection scheme messages

1. Processor publishes the schemes to `cms/fleetwise/vehicles/{vin}/collection_schemes_and_decoder_manifests` via IoT Core MQTT

1. Agent receives the schemes and begins collecting the specified signals

Campaign sync status is tracked per vehicle:
+  **PENDING** — Campaign has been pushed to the agent but the agent has not yet confirmed receipt
+  **HEALTHY** — Agent confirmed receipt of the collection scheme in its checkin `document_sync_ids` 

When all campaigns for a vehicle are suspended, the processor pushes an empty `CollectionSchemes` protobuf to clear the agent’s active collection.

### Simulator preprocessor
<a name="simulator-preprocessor"></a>

The SimulatorPreprocessor decodes gzip-compressed, base64-encoded telemetry messages published by the MQTT Direct simulator. The simulator compresses telemetry payloads to reduce IoT Core message costs and bandwidth. This processor reads from the `cms-telemetry-raw` Kafka topic, base64-decodes and gunzips each message, validates the resulting JSON, and writes clean JSON records to the `cms-telemetry-preprocessed` topic.

 **Pipeline:** 

1. Simulator publishes gzip\+base64 telemetry to IoT Core

1. IoT Rule routes to MSK `cms-telemetry-raw` topic

1. SimulatorPreprocessor decodes and decompresses

1. Clean JSON written to `cms-telemetry-preprocessed` 

1. Downstream processors (EventDrivenTelemetryProcessor, TripProcessor, SafetyProcessor, MaintenanceProcessor) consume from `cms-telemetry-preprocessed` 

This design means both MQTT Direct and FleetWise Edge telemetry converge on the same `cms-telemetry-preprocessed` topic, enabling a single set of downstream processors for both modes.

### Geofence processor
<a name="geofence-processor"></a>

The GeofenceProcessor evaluates vehicle positions against active geofences stored in DynamoDB. It reads telemetry from the `cms-telemetry-preprocessed` Kafka topic, extracts latitude and longitude from each message, and checks whether the vehicle is inside or outside each active geofence.

 **How it works:** 

1. Reads telemetry messages from `cms-telemetry-preprocessed` 

1. Extracts vehicle ID, latitude, and longitude

1. Queries the `cms-dev-storage-geofences` DynamoDB table for active geofences (vehicle-specific and global)

1. Calculates distance from vehicle position to geofence center using the Haversine formula

1. Compares distance against the geofence radius

1. On boundary crossing (enter or exit), generates a safety event and writes to the `cms-dev-storage-safety-events` DynamoDB table

1. Deduplicates events: only fires once per boundary crossing direction (enter or exit), preventing repeated alerts while a vehicle remains inside or outside a geofence

 **Geofence types:** 
+  **CIRCLE** — Defined by center coordinates (latitude, longitude) and radius in kilometers
+  **Vehicle-specific** — Geofences assigned to a specific vehicle ID
+  **Global** — Geofences with `vehicleId=ALL` that apply to every vehicle

### OEM telemetry processor
<a name="oem-telemetry-processor"></a>

The OEMTelemetryProcessor transforms telemetry from third-party OEM APIs into the standard signal catalog format. This enables the guidance to ingest data from any OEM without modifying the core processing pipeline.

 **How it works:** 

1. Reads raw OEM telemetry from the `cms-telemetry-oem` Kafka topic

1. Extracts the `oem_source` field to identify which OEM sent the data

1. Loads the corresponding transform manifest from S3 (cached in memory per OEM)

1. Applies field mappings, unit conversions, and data type transformations defined in the manifest

1. Outputs standard CMS-format JSON to the `cms-telemetry-raw` topic

 **Transform manifest capabilities:** 
+  **Field mapping** — Maps OEM field paths to signal catalog names (for example, `vehicle_data.speed_kmh` → `speed`)
+  **Unit conversion** — Multiplier, formula, or lookup table conversions (for example, km/h to mph, Celsius to Fahrenheit)
+  **Conditional mapping** — Apply mappings only when conditions are met (for example, EV-only signals)
+  **Validation** — Required signal checks and range validation

Transform manifests are stored in S3 with versioning enabled. Customers create their own manifests by copying the provided template and customizing field mappings for their OEM data format.

### Trip detection application
<a name="trip-detection-application"></a>

The TripProcessor uses Flink’s `KeyedProcessFunction` with per-vehicle keyed state to detect trip boundaries through ignition signal transitions. This stateful approach eliminates DynamoDB reads during normal operation.

 **Transition-based detection:** 


| Previous Ignition | Current Ignition | Action | 
| --- | --- | --- | 
| OFF (or null) | ON |  **Start trip**: Generate tripId, PutItem to DynamoDB | 
| ON | ON |  **Update**: Accumulate route/metrics in Flink state, flush every 5 messages | 
| ON | OFF |  **End trip**: UpdateItem with COMPLETED status | 
| OFF | OFF | Ignore | 

 **State per vehicle (Flink ValueState):** 
+  `tripId` — generated from `vehicleId + timestamp` at trip start
+  `vehicleId`, `driverId` — from telemetry payload
+  `ignitionOn` — previous ignition state for transition detection
+  `routeBuffer` — GPS points accumulated in memory
+  `maxSpeed`, `totalDistance`, `telemetryCount` — running metrics

 **DynamoDB write optimization:** 

The stateful design reduces DynamoDB operations significantly compared to a stateless approach:


| Operation | Stateless (per message) | Stateful (v2) | 
| --- | --- | --- | 
| DynamoDB reads | 2-3 (GetItem \+ GSI query) | 0 | 
| DynamoDB writes | 1 PutItem (full record) | 1 UpdateItem every 5 messages | 
| 20-message trip total | \~60 reads \+ 20 writes | 0 reads \+ 5 writes | 

Mid-trip updates use `UpdateItem` (not `PutItem`) to append route points and update metrics without overwriting the full record. This eliminates race conditions from concurrent writes.

 **Single trip ownership:** 

Only the TripProcessor writes to the trips table. The TelemetryProcessor tags telemetry records with `tripId` for querying but does not write to the trips table. This prevents data clobbering between processors.

 **No simulator dependencies:** 

The TripProcessor does not require `engineEvent` strings or simulator-provided `tripId`. It generates trip identifiers from `vehicleId + timestamp` when not provided, making it compatible with both the MQTT simulator and CAN bus data from FleetWise Edge Agent. In FWE mode, the TripProcessor detects trip boundaries from the ignition signal (`ignitionOn: true/false`) decoded by the FWTelemetryProcessor from CAN signal ID 4.

### Safety event application
<a name="safety-event-application"></a>

Identifies unsafe driving behaviors from telemetry signals.

 **Detection rules:** 
+ Hard braking: deceleration > 0.4g
+ Rapid acceleration: acceleration > 0.35g
+ Harsh cornering: lateral acceleration > 0.4g
+ Speed violation: speed > threshold
+ AEB/ABS/ESC activation events
+ Seatbelt violations, phone usage detection

 **Output:** 
+ Write to DynamoDB safety events table
+ Update driver safety score (integrated with trip metrics)

### Maintenance alert application
<a name="maintenance-alert-application"></a>

Generates predictive maintenance alerts from vehicle health signals.

 **Monitoring:** 
+ Engine temperature > 240°F (critical)
+ Tire pressure < 28 PSI or > 35 PSI
+ Battery voltage < 12.0V
+ Oil pressure < 20 PSI
+ Brake wear, filter life, oil life thresholds
+ DTC (Diagnostic Trouble Code) detection

 **Output:** 
+ Write to DynamoDB maintenance alerts table
+ Deduplicated per trip (one alert per type per trip)

## Flink configuration
<a name="flink-configuration"></a>

 **Runtime:** 
+ Flink version: 1.18.1
+ Parallelism: 1 (development) or 2-4 (production)
+ Checkpointing: Every 60 seconds, exactly-once semantics
+ State backend: Managed by Amazon Managed Service for Apache Flink

 **Resources:** 
+ KPUs: 1 per application (development)
+ Memory: 4 GB per KPU
+ vCPUs: 1 per KPU

 **Deployment:** 

All ten applications share a single JAR (`cms-telemetry-processor-1.0.0.zip`) stored in S3. The `UniversalProcessor` entry point routes to the correct processor class based on the Flink application’s runtime properties.

 **Kafka resilience:** 

All processors use a shared `KafkaConfig.withReconnect()` utility that applies reconnect backoff, connection keepalive, and session timeout settings to prevent stale SSL connections to MSK. Key properties include `reconnect.backoff.ms=1000`, `reconnect.backoff.max.ms=10000`, `connections.max.idle.ms=540000`, and `metadata.max.age.ms=300000`.

 **CloudWatch alarms:** 

The FlinkStack creates CloudWatch alarms for processor health monitoring:
+  **Downtime alarms** — Fire when a processor has more than 1 minute of downtime in a 5-minute window. Applied to all critical processors.
+  **Idle processing alarms** — Fire when the FWTelemetryProcessor or TripProcessor processes 0 records in a 10-minute window, indicating a pipeline stall.