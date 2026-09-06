

# Data flow details
<a name="data-flow-details"></a>

## Telemetry ingestion flow
<a name="telemetry-ingestion-flow"></a>

1. Vehicle publishes telemetry to `cms/telemetry/{vin}` MQTT topic

1. IoT Core receives message and triggers IoT Rule

1. IoT Rule sends message to MSK via VPC Destination

1. Message written to `cms-telemetry` Kafka topic

1. Flink applications consume from topic

1. Processed data written to DynamoDB and ElastiCache

1. Fleet Manager UI queries data via API Gateway

 **Latency:** 
+ Vehicle to IoT Core: <100ms
+ IoT Core to MSK: <100ms
+ MSK to Flink: <500ms
+ Flink to DynamoDB: <200ms
+ Total: <1 second

## Trip detection flow
<a name="trip-detection-flow"></a>

1. Flink reads telemetry from `cms-telemetry` topic

1. Groups messages by VIN

1. Detects ignition state change (off → on)

1. Generates trip start event

1. Writes to `cms-trips` topic and DynamoDB

1. Continues monitoring until ignition off

1. Generates trip end event with metrics

1. Updates trip record in DynamoDB

## Alert generation flow
<a name="alert-generation-flow"></a>

1. Flink reads telemetry from `cms-telemetry` topic

1. Evaluates safety and maintenance rules

1. Detects threshold violations

1. Generates alert event

1. Writes to `cms-alerts` topic and DynamoDB

1. SNS notification sent (if configured)

1. Fleet Manager UI displays alert

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

1. IoT Rule routes telemetry to MSK `fw-telemetry-raw` topic (and S3 backup)

1. FWTelemetryProcessor decodes protobuf, maps CAN signals to standard format using decoder manifest

1. Mapped telemetry written to `cms-telemetry-preprocessed` Kafka topic

1. Downstream processors (TripProcessor, SafetyProcessor, MaintenanceProcessor) consume and process as standard telemetry

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

1. Lambda publishes command payload to `cms/commands/{vehicleId}/request` via IoT Core MQTT (QoS 1)

1. Lambda stores the command in DynamoDB with status `SENT` 

1. Vehicle receives the MQTT message and executes the command

1. Vehicle publishes response to `cms/commands/{vehicleId}/response` 

1. IoT Rule triggers the Command Response Handler Lambda

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

1. Geofence stored in DynamoDB `cms-dev-storage-geofences` table

1. GeofenceProcessor Flink application reads telemetry from `cms-telemetry-preprocessed` 

1. Processor extracts vehicle position (latitude, longitude) from each message

1. Processor queries DynamoDB for active geofences (vehicle-specific and global with `vehicleId=ALL`)

1. Processor calculates Haversine distance from vehicle to each geofence center

1. On boundary crossing (enter or exit), processor writes a safety event to DynamoDB

1. Deduplication prevents repeated alerts while vehicle remains inside or outside the geofence

1. Fleet Manager UI displays geofence violations in the safety events view