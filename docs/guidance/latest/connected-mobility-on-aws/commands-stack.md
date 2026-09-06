

# Remote commands and geofences
<a name="commands-stack"></a>

The remote commands and geofences layer enables bidirectional communication with vehicles by sending commands from the cloud to vehicles through IoT Core MQTT and tracking command execution status.

## Remote commands architecture
<a name="remote-commands-architecture"></a>

The remote commands system uses a request/response pattern over MQTT:

1. Fleet Manager UI or API sends a command request

1. Commands Lambda publishes the command payload to `cms/commands/{vehicleId}/request` via IoT Core MQTT

1. Command is stored in DynamoDB with status `SENT` 

1. Vehicle (or simulator) receives the command, executes it, and publishes a response to `cms/commands/{vehicleId}/response` 

1. IoT Rule triggers the Command Response Handler Lambda

1. Response Handler updates the command status in DynamoDB (SUCCEEDED, FAILED, TIMEOUT, IN\_PROGRESS)

1. Response Handler calculates round-trip latency in milliseconds

## Command API endpoints
<a name="command-api-endpoints"></a>


| Method | Path | Description | 
| --- | --- | --- | 
| POST | /api/commands/{vehicleId} | Send a command to a vehicle | 
| GET | /api/commands/{vehicleId} | List command history for a vehicle | 
| GET | /api/commands/catalog | List available actuatable commands from the signal catalog | 
| POST | /api/geofences | Create a geofence | 
| GET | /api/geofences/{vehicleId} | List geofences for a vehicle (includes global geofences) | 
| DELETE | /api/geofences/{geofenceId} | Deactivate a geofence | 

## Command request payload
<a name="command-request-payload"></a>

When sending a command, the Lambda publishes the following JSON to the MQTT topic `cms/commands/{vehicleId}/request`:

```
{
  "commandId": "a1b2c3d4e5f6",
  "commandName": "lock_doors",
  "vehicleId": "VEH-0049",
  "value": true,
  "issuedAt": "2025-03-08T15:30:00+00:00",
  "issuedAtMs": 1741448200000,
  "timeout": 10000
}
```

## Command response payload
<a name="command-response-payload"></a>

The vehicle publishes a response to `cms/commands/{vehicleId}/response`:

```
{
  "commandId": "a1b2c3d4e5f6",
  "vehicleId": "VEH-0049",
  "status": "SUCCEEDED",
  "reason": "",
  "resultValue": "true"
}
```

 **Status values:** 
+  `SENT` — Command published to MQTT, awaiting vehicle response
+  `IN_PROGRESS` — Vehicle acknowledged receipt, execution in progress
+  `SUCCEEDED` — Command executed successfully
+  `FAILED` — Command execution failed (reason field contains details)
+  `TIMEOUT` — Vehicle did not respond within the timeout period

## Command catalog
<a name="command-catalog"></a>

The command catalog is derived from the signal catalog. Signals with an `actuator` attribute are exposed as available commands. The catalog endpoint returns actuatable signals grouped by category:

 **Categories:** 
+  **doors** — Lock/unlock doors
+  **lights** — Headlights, hazard lights, turn signals
+  **climate** — HVAC on/off, target temperature, seat heating
+  **windows** — Window open/close
+  **trunk** — Trunk lock/unlock
+  **horn** — Horn activation
+  **engine** — Remote start/stop

Each actuator definition includes:
+  `commandName` — The command identifier (for example, `lock_doors`)
+  `valueType` — Data type: boolean, number, enum
+  `min` / `max` — Valid range for numeric values
+  `options` — Valid values for enum types
+  `responseTimeout` — Expected response time in milliseconds
+  `unit` — Unit of measurement (if applicable)

## Commands table schema
<a name="command-dynamodb-schema"></a>


| Attribute | Type | Description | 
| --- | --- | --- | 
| commandId | String (PK) | Unique command identifier (UUID prefix) | 
| vehicleId | String | Target vehicle ID (GSI: vehicleId-index) | 
| commandName | String | Command name from catalog | 
| value | String | Command value | 
| status | String | SENT, IN\_PROGRESS, SUCCEEDED, FAILED, TIMEOUT | 
| issuedAt | String | ISO 8601 timestamp when command was sent | 
| respondedAt | String | ISO 8601 timestamp when response was received | 
| latencyMs | Number | Round-trip latency in milliseconds | 
| reason | String | Failure reason (if status is FAILED) | 
| resultValue | String | Value returned by the vehicle | 
| ttl | Number | DynamoDB TTL (7 days after creation) | 

## Geofence management
<a name="geofence-management"></a>

Geofences are managed through the Commands API and evaluated by the GeofenceProcessor Flink application.

 **Geofence schema:** 


| Attribute | Type | Description | 
| --- | --- | --- | 
| geofenceId | String (PK) | Unique geofence identifier | 
| vehicleId | String | Target vehicle ID or `ALL` for global geofences | 
| name | String | Human-readable geofence name | 
| centerLat | Number | Center latitude | 
| centerLng | Number | Center longitude | 
| radiusKm | Number | Radius in kilometers | 
| type | String | Geofence shape (CIRCLE) | 
| action | String | Action on violation (ALERT) | 
| active | Boolean | Whether the geofence is active | 
| createdAt | String | ISO 8601 creation timestamp | 
| ttl | Number | DynamoDB TTL (90 days after creation) | 