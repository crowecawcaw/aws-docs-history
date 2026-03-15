# Data flow details

## Telemetry ingestion flow

1. Vehicle publishes telemetry to `cms/telemetry/{vin}` MQTT topic
2. IoT Core receives message and triggers IoT Rule
3. IoT Rule sends message to MSK via VPC Destination
4. Message written to `cms-telemetry` Kafka topic
5. Flink applications consume from topic
6. Processed data written to DynamoDB and ElastiCache
7. Fleet Manager UI queries data via API Gateway

**Latency:**

- Vehicle to IoT Core: <100ms
- IoT Core to MSK: <100ms
- MSK to Flink: <500ms
- Flink to DynamoDB: <200ms
- Total: <1 second

## Trip detection flow

1. Flink reads telemetry from `cms-telemetry` topic
2. Groups messages by VIN
3. Detects ignition state change (off → on)
4. Generates trip start event
5. Writes to `cms-trips` topic and DynamoDB
6. Continues monitoring until ignition off
7. Generates trip end event with metrics
8. Updates trip record in DynamoDB

## Alert generation flow

1. Flink reads telemetry from `cms-telemetry` topic
2. Evaluates safety and maintenance rules
3. Detects threshold violations
4. Generates alert event
5. Writes to `cms-alerts` topic and DynamoDB
6. SNS notification sent (if configured)
7. Fleet Manager UI displays alert

## UI query flow

1. User opens Fleet Manager UI
2. CloudFront serves React application
3. User authenticates with Cognito
4. UI requests vehicle list from API Gateway
5. Lambda queries ElastiCache for real-time state
6. Lambda queries DynamoDB for vehicle details
7. Response returned to UI
8. UI displays vehicles on map with Location Service

## FleetWise Edge telemetry flow

1. FWE agent starts and publishes a checkin protobuf to `cms/fleetwise/vehicles/{vin}/checkins`
2. IoT Rule routes checkin to MSK `fw-checkin` topic
3. CampaignSyncProcessor consumes checkin, queries DynamoDB for active campaigns
4. CampaignSyncProcessor pushes decoder manifest and collection schemes to agent via IoT Core MQTT
5. Agent receives schemes and begins collecting specified CAN signals
6. Agent encodes collected signals as protobuf and publishes to `cms/fleetwise/vehicles/{vin}/signals`
7. IoT Rule routes telemetry to MSK `fw-telemetry-raw` topic (and S3 backup)
8. FWTelemetryProcessor decodes protobuf, maps CAN signals to standard format using decoder manifest
9. Mapped telemetry written to `cms-telemetry-preprocessed` Kafka topic
10. Downstream processors (TripProcessor, SafetyProcessor, MaintenanceProcessor) consume and process as standard telemetry
11. Processed data written to DynamoDB and ElastiCache

**Latency:**

- FWE agent to IoT Core: <200ms
- IoT Core to MSK: <100ms
- FWTelemetryProcessor decode: <500ms
- Downstream processing: <500ms
- Total: <1.5 seconds

## Remote command flow

1. Fleet Manager UI sends POST request to `/api/commands/{vehicleId}` with command name and value
2. Commands Lambda validates the request and generates a unique command ID
3. Lambda publishes command payload to `cms/commands/{vehicleId}/request` via IoT Core MQTT (QoS 1)
4. Lambda stores the command in DynamoDB with status `SENT`
5. Vehicle receives the MQTT message and executes the command
6. Vehicle publishes response to `cms/commands/{vehicleId}/response`
7. IoT Rule triggers the Command Response Handler Lambda
8. Response Handler updates command status in DynamoDB and calculates round-trip latency
9. Fleet Manager UI polls command history to display updated status

**Latency:**

- API to IoT Core publish: <100ms
- IoT Core to vehicle: <200ms
- Vehicle execution: varies by command type
- Vehicle response to IoT Core: <200ms
- Response Handler processing: <100ms
- Total (excluding execution): <600ms

## Geofence evaluation flow

1. Fleet Manager UI creates a geofence via POST `/api/geofences`
2. Geofence stored in DynamoDB `cms-dev-storage-geofences` table
3. GeofenceProcessor Flink application reads telemetry from `cms-telemetry-preprocessed`
4. Processor extracts vehicle position (latitude, longitude) from each message
5. Processor queries DynamoDB for active geofences (vehicle-specific and global with `vehicleId=ALL`)
6. Processor calculates Haversine distance from vehicle to each geofence center
7. On boundary crossing (enter or exit), processor writes a safety event to DynamoDB
8. Deduplication prevents repeated alerts while vehicle remains inside or outside the geofence
9. Fleet Manager UI displays geofence violations in the safety events view
