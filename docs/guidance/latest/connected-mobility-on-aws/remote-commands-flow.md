

# Remote commands
<a name="remote-commands-flow"></a>

The remote commands system enables fleet managers to send actuator commands to vehicles (lock doors, flash lights, start engine) and track whether the vehicle executed the command successfully. The system supports two wire formats — JSON for MQTT Direct simulators and protobuf for FleetWise Edge (FWE) vehicles — using a single API endpoint.

## End-to-end flow
<a name="command-flow-detail"></a>

1.  **Fleet Manager UI** — The operator selects a vehicle, chooses a command from the catalog (for example, "Lock Doors"), and clicks send.

1.  **API Gateway → Commands Lambda** — The request hits POST `/api/commands/{vehicleId}`. The Lambda validates the command name against the signal catalog (only signals with an `actuator` attribute are valid commands). It looks up the vehicle’s VIN from the vehicles table for FWE topic addressing.

1.  **Dual MQTT publish** — The Lambda publishes the command to both wire formats simultaneously via IoT Core MQTT with QoS 1:

    **FWE protobuf path** (for FleetWise Edge vehicles):

   Topic: `cms/commands/things/{vin}/executions/{commandId}/request/protobuf` 

   The Lambda builds a `CommandRequest` protobuf message containing the command ID, timeout, signal ID (resolved from the signal catalog), decoder manifest sync ID, and the typed value (boolean, double, or string). The FWE agent on the vehicle subscribes to this topic pattern via its `commandsTopicPrefix` configuration.

    **JSON path** (for MQTT Direct simulators):

   Topic: `cms/commands/{vehicleId}/request` 

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

1.  **DynamoDB write** — The Lambda stores the command with status `SENT` and a 7-day TTL.

1.  **Vehicle receives and responds** — The vehicle executes the command and publishes a response:

    **FWE protobuf response:** 

   Topic: `cms/commands/things/{vin}/executions/{commandId}/response/protobuf` 

   The FWE agent publishes a `CommandResponse` protobuf containing the command ID, status enum (SUCCEEDED=1, TIMEOUT=2, FAILED=4, IN\_PROGRESS=10), and an optional reason description.

    **JSON response** (simulators):

   Topic: `cms/commands/{vehicleId}/response` 

   ```
   {
     "commandId": "a1b2c3d4e5f6",
     "vehicleId": "VEH-0049",
     "status": "SUCCEEDED",
     "reason": "",
     "resultValue": "true"
   }
   ```

1.  **IoT Rules → Response Handler Lambda** — Two IoT Rules route responses to the Command Response Handler Lambda:
   +  `cms_prod_fwe_command_response_rule` — Matches `cms/commands/things/+/executions/+/response/protobuf`. The SQL uses `encode(*, 'base64')` to pass the binary payload as a base64 string, along with the VIN extracted from the topic via `topic(3)`.
   +  `cms_prod_command_response_rule` — Matches `cms/commands/+/response` for JSON responses.

   The Response Handler detects the format (base64-encoded protobuf vs. JSON), decodes accordingly, and maps the FWE status enum to a string status.

1.  **Status update** — The Response Handler updates the command in DynamoDB: sets the status, records the response timestamp, and calculates the round-trip latency in milliseconds.

1.  **UI update** — The Fleet Manager UI polls the command history endpoint and displays the updated status and latency.

## Why dual-path publishing
<a name="command-dual-path"></a>

The Commands Lambda publishes to both topics on every command because the Lambda does not know which protocol the target vehicle uses. MQTT Direct simulators subscribe to `cms/commands/{vehicleId}/request` (JSON), while FWE agents subscribe to `cms/commands/things/{vin}/executions/+/request/protobuf` (protobuf). Only the vehicle that matches the topic pattern receives the message — the other publish is a no-op (no subscriber, message is discarded by the broker).

This approach avoids the need to track which protocol each vehicle uses and ensures commands work regardless of the vehicle’s telemetry source.

## Protobuf encoding
<a name="command-protobuf-detail"></a>

The FWE command protocol uses two protobuf message types:

 **CommandRequest** (Lambda → vehicle):
+  `command_id` (string) — Unique identifier for tracking
+  `timeout_ms` (uint32) — How long the vehicle should attempt execution
+  `issued_timestamp_ms` (uint64) — When the command was issued
+  `actuator_command.signal_id` (uint32) — Numeric signal ID from the signal catalog
+  `actuator_command.decoder_manifest_sync_id` (string) — Decoder manifest version
+  `actuator_command.boolean_value` / `double_value` / `string_value` — Typed value (one of)

 **CommandResponse** (vehicle → Lambda):
+  `command_id` (string) — Matches the request
+  `status` (enum) — 0=UNKNOWN, 1=SUCCEEDED, 2=TIMEOUT, 4=FAILED, 10=IN\_PROGRESS
+  `reason_code` (uint32) — OEM-specific error code
+  `reason_description` (string) — Human-readable failure reason

The protobuf definitions are compiled into `command_request_pb2.py` and `command_response_pb2.py` in the commands Lambda package.

## Command catalog
<a name="command-catalog-detail"></a>

The command catalog is not hardcoded — it is dynamically derived from the signal catalog. Any signal in the `cms-{stage}-signal-catalog` DynamoDB table that has an `actuator` attribute is exposed as an available command.

Each actuator definition includes:
+  `commandName` — Identifier used in the MQTT payload (for example, `lock_doors`)
+  `label` — Human-readable name for the UI (for example, "Lock Doors")
+  `category` — Grouping for the UI (doors, lights, climate, windows, trunk, horn, engine)
+  `valueType` — Data type: `boolean`, `number`, or `enum` 
+  `min` / `max` — Valid range for numeric commands (for example, temperature 60-85°F)
+  `options` — Valid values for enum commands (for example, headlight modes: off, low, high)
+  `responseTimeout` — Expected response time in milliseconds
+  `unit` — Unit of measurement (if applicable)

This design means new commands can be added by inserting a signal with an `actuator` attribute into the signal catalog — no code changes required.