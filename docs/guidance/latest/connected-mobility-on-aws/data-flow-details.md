

# Data flow details
<a name="data-flow-details"></a>

## Telemetry ingestion flow
<a name="telemetry-ingestion-flow"></a>

1. Vehicle publishes telemetry to `cms/{stage}/telemetry/{clientId}` MQTT topic

1. IoT Core receives message and triggers IoT Rule

1. IoT Rule sends message to MSK via VPC Destination (and to S3 for raw backup)

1. Message written to `cms-telemetry-raw` Kafka topic

1. SimulatorPreprocessor Flink application normalizes the message and writes to `cms-telemetry-preprocessed` 

1. EventDrivenTelemetryProcessor reads `cms-telemetry-preprocessed`, writes real-time vehicle state to ElastiCache (Redis), and routes events to domain topics (`cms-telemetry-trips`, `cms-telemetry-safety`, `cms-telemetry-maintenance`)

1. Fleet Manager UI queries data via API Gateway

 **Latency:** 
+ Vehicle to IoT Core: <100ms
+ IoT Core to MSK: <100ms
+ MSK to Flink: <500ms
+ Flink to DynamoDB: <200ms
+ Total: <1 second

## Trip detection flow
<a name="trip-detection-flow"></a>

1. TripProcessor reads routed trip events from the `cms-telemetry-trips` Kafka topic (populated by EventDrivenTelemetryProcessor — see [Telemetry ingestion flow](#telemetry-ingestion-flow))

1. Groups messages by VIN

1. Detects ignition state change (off → on)

1. Generates trip start event

1. Writes trip start event to DynamoDB and emits a CloudWatch metric

1. Continues monitoring until ignition off

1. Generates trip end event with metrics

1. Updates trip record in DynamoDB

## Alert generation flow
<a name="alert-generation-flow"></a>

1. SafetyProcessor reads routed safety events from `cms-telemetry-safety`, and MaintenanceProcessor reads routed maintenance events from `cms-telemetry-maintenance` (both populated by EventDrivenTelemetryProcessor — see [Telemetry ingestion flow](#telemetry-ingestion-flow))

1. Evaluates safety and maintenance rules

1. Detects threshold violations

1. Generates alert event

1. Writes alert to DynamoDB

1. Fleet Manager UI displays alert

**Note**  
This guidance does not send alert notifications to fleet operators via SNS or any other out-of-band channel by default — alerts are written to DynamoDB and surfaced when the Fleet Manager UI queries them. Amazon SNS is used elsewhere in this guidance for CloudWatch alarm actions on Flink application health and simulation monitoring, not for fleet-facing alert delivery.

## UI query flow
<a name="ui-query-flow"></a>

1. User opens Fleet Manager UI

1. CloudFront serves React application

1. User authenticates with Cognito

1. UI requests vehicle list from API Gateway

1. Lambda queries ElastiCache for real-time state

1. Lambda queries DynamoDB for vehicle details

1. Response returned to UI

1. UI displays vehicles on map with Location Service

## FleetWise Edge telemetry flow
<a name="fleetwise-telemetry-flow"></a>

1. FWE agent starts and publishes a checkin protobuf to `cms/fleetwise/vehicles/{vin}/checkins` 

1. IoT Rule routes checkin to MSK `fw-checkin` topic

1. CampaignSyncProcessor consumes checkin, queries DynamoDB for active campaigns

1. CampaignSyncProcessor pushes decoder manifest and collection schemes to agent via IoT Core MQTT

1. Agent receives schemes and begins collecting specified CAN signals

1. Agent encodes collected signals as protobuf and publishes to `cms/fleetwise/vehicles/{vin}/signals` 

1. IoT Rule routes telemetry to MSK `fw-telemetry-raw` topic

1. FWTelemetryProcessor decodes protobuf, maps CAN signals to standard format using decoder manifest

1. Mapped telemetry written to `cms-telemetry-preprocessed` Kafka topic

1. EventDrivenTelemetryProcessor reads `cms-telemetry-preprocessed`, writes real-time vehicle state to ElastiCache, and routes events to `cms-telemetry-trips`, `cms-telemetry-safety`, and `cms-telemetry-maintenance` 

1. Downstream processors (TripProcessor, SafetyProcessor, MaintenanceProcessor) consume their respective routed topic and process as standard telemetry — see [Telemetry ingestion flow](#telemetry-ingestion-flow) 

1. Processed data written to DynamoDB and ElastiCache

 **Latency:** 
+ FWE agent to IoT Core: <200ms
+ IoT Core to MSK: <100ms
+ FWTelemetryProcessor decode: <500ms
+ Downstream processing: <500ms
+ Total: <1.5 seconds

## Remote command flow
<a name="remote-command-flow"></a>

1. Fleet Manager UI sends POST request to `/api/commands/{vehicleId}` with command name and value

1. Commands Lambda validates the request and generates a unique command ID

1. Lambda publishes the command to both vehicle telemetry paths via IoT Core MQTT (QoS 1) on every command: a protobuf payload to `cms/commands/things/{vin}/executions/{executionId}/request/protobuf` for FWE agents, and a JSON payload to the legacy `cms/commands/{vehicleId}/request` topic for MQTT Direct simulators

1. Lambda stores the command in DynamoDB with status `SENT` 

1. Vehicle executes the command and publishes a response on the matching topic: an FWE agent publishes a `CommandResponse` protobuf to `cms/commands/things/{vin}/executions/{executionId}/response/protobuf`; an MQTT Direct simulator publishes JSON to the legacy `cms/commands/{vehicleId}/response` topic

1. A single IoT Rule per response topic triggers the Command Response Handler Lambda, which decodes either payload shape — base64-encoded protobuf (mapping the FWE status enum to SUCCEEDED/FAILED/TIMEOUT/IN\_PROGRESS) or legacy JSON

1. Response Handler updates command status in DynamoDB and calculates round-trip latency

1. Fleet Manager UI polls command history to display updated status

 **Latency:** 
+ API to IoT Core publish: <100ms
+ IoT Core to vehicle: <200ms
+ Vehicle execution: varies by command type
+ Vehicle response to IoT Core: <200ms
+ Response Handler processing: <100ms
+ Total (excluding execution): <600ms

## Geofence evaluation flow
<a name="geofence-evaluation-flow"></a>

1. Fleet Manager UI creates a geofence via POST `/api/geofences` 

1. Geofence stored in DynamoDB `cms-{stage}-storage-geofences` table

1. GeofenceProcessor Flink application reads telemetry from `cms-telemetry-preprocessed` 

1. Processor extracts vehicle position (latitude, longitude) from each message

1. Processor queries DynamoDB for active geofences (vehicle-specific and global with `vehicleId=ALL`)

1. Processor calculates Haversine distance from vehicle to each geofence center

1. On boundary crossing (enter or exit), processor writes a safety event to DynamoDB

1. Deduplication prevents repeated alerts while vehicle remains inside or outside the geofence

1. Fleet Manager UI displays geofence violations in the safety events view