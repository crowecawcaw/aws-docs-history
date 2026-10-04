

# Remote commands
<a name="remote-commands-flow"></a>

The remote commands system enables fleet managers to send actuator commands to vehicles (lock doors, flash lights, start engine) and track whether the vehicle executed the command successfully. Commands are sent through a single API endpoint and published in two wire formats — JSON on `cms/commands/{vehicleId}/request` and protobuf on the FleetWise Edge command topic.

**Important**  
 **Actuation happens on the JSON path for both vehicle classes.** The protobuf path is fully wired for transport and response handling — the FWE agent subscribes to it, parses the `CommandRequest`, and returns a `CommandResponse` — but FWE-native actuation is not implemented in this release, so the agent rejects actuator commands with `reason_code` 3 (`NO_DECODING_RULES_FOUND`).  
For FleetWise Edge vehicles, the component that actually executes a command is the **simulator** task, not the agent: it applies the command to its vehicle state and writes the resulting CAN frame, which the FWE agent then decodes and reports as telemetry. This means the mutated state is observable through the genuine FleetWise decode path. See [FleetWise Edge actuation limits](#command-fwe-actuation-limits).

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

1.  **Vehicle receives and responds** — The receiving component publishes a response. On the FleetWise Edge path the agent answers on the protobuf topic (currently always a rejection — see [FleetWise Edge actuation limits](#command-fwe-actuation-limits)), while the simulator performs the actuation and answers on the JSON topic:

    **FWE protobuf response:** 

   Topic: `cms/commands/things/{vin}/executions/{commandId}/response/protobuf` 

   The FWE agent publishes a `CommandResponse` protobuf containing the command ID, status enum (SUCCEEDED=1, TIMEOUT=2, FAILED=4, IN\_PROGRESS=10), a numeric `reason_code`, and an optional reason description. Note that FWE commonly sets `reason_code` with an **empty** description, so the numeric code is the diagnostic value worth persisting.

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
   +  `cms_prod_fwe_command_response_rule` — Matches `cms/commands/things/+/executions/+/response/protobuf`. The SQL uses `encode(*, 'base64')` to pass the binary payload as a base64 string, along with the VIN extracted from the topic via `topic(4)`. (`topic(n)` is 1-indexed, so for `cms/commands/things/{vin}/…` the segments are `cms`=1, `commands`=2, `things`=3, `{vin}`=4.)
   +  `cms_prod_command_response_rule` — Matches `cms/commands/+/response` for JSON responses.

   The Response Handler detects the format (base64-encoded protobuf vs. JSON), decodes accordingly, and maps the FWE status enum to a string status.

1.  **Status update** — The Response Handler updates the command in DynamoDB: sets the status, records the response timestamp, persists the FWE `reason_code` when present, and calculates the round-trip latency in milliseconds. A non-success response is rejected if the command has already reached `SUCCEEDED` (see [Why dual-path publishing](#command-dual-path)).

1.  **UI update** — The Fleet Manager UI polls the command history endpoint and displays the updated status and latency.

## Why dual-path publishing
<a name="command-dual-path"></a>

The Commands Lambda publishes to both topics on every command because the Lambda does not know which protocol the target vehicle uses. MQTT Direct simulators subscribe to `cms/commands/{vehicleId}/request` (JSON), while FWE agents subscribe to `cms/commands/things/{vin}/executions/+/request/protobuf` (protobuf).

For an MQTT Direct vehicle only the JSON publish has a subscriber; the protobuf publish is discarded by the broker. For a FleetWise Edge vehicle **both** publishes have subscribers, so two responses arrive and they disagree — the simulator returns `SUCCEEDED` (it performed the actuation) and the agent returns `FAILED` with `reason_code` 3 (it cannot). Because the agent is usually slower, the Response Handler applies a precedence rule: **a non-success response may not move a command out of `SUCCEEDED` **. Without that rule, last-write-wins would report a failure for a command that succeeded.

This approach avoids the need to track which protocol each vehicle uses and ensures commands work regardless of the vehicle’s telemetry source.

## FleetWise Edge actuation limits
<a name="command-fwe-actuation-limits"></a>

The FWE agent receives and answers protobuf command requests, but does not actuate them in this release. Enabling FWE-native actuation requires four additional pieces, listed here so the boundary is explicit:

1.  **The actuator signal must be declared as a custom-decoding signal.** The agent resolves an incoming command’s signal ID against a map built exclusively from the decoder manifest’s `custom_decoding_signals`. Actuator signals are currently emitted as `can_signals`, so the lookup misses and the command is rejected with `NO_DECODING_RULES_FOUND`.

1.  **A command dispatcher must be registered.** This requires a `canCommandInterface` entry in the agent’s network-interface configuration; the generated configuration declares `canInterface`, `obdInterface`, and the UDS-DTC example interface only. Without it the agent reports `NO_COMMAND_DISPATCHER_FOUND`.

1.  **The CAN actuator map must include the solution’s actuators.** AWS IoT FleetWise Edge v1.3.2 hardcodes its CAN command actuator map to two example entries and exposes no runtime configuration for it, so a source patch is required — the same pattern the image build already uses for the DTC signal list and extended CAN IDs.

1.  **A CAN command responder must exist.** The agent’s CAN command dispatcher sends a request frame on a configured CAN ID and waits for a matching response frame carrying the command ID, a status code, and a reason. With nothing answering on the bus, commands end in `EXECUTION_TIMEOUT`.

Until these are in place, treat the protobuf path as the transport and acknowledgement mechanism, and the simulator’s CAN write-back as the actuation seam.

**Note**  
On the FleetWise Edge path, command handling does **not** depend on a trip being in progress. The long-lived per-vehicle task runs two containers: the FleetWise Edge agent, and a `vehicle-ecu` sidecar that owns the command subscription and the vehicle’s state, and puts that state on the vcan device on an idle cadence. A parked vehicle is therefore commandable, and the resulting state change is observable in telemetry within one idle tick.  
Trips remain a separate, ephemeral `fwe-simulator` task; it signals the sidecar through a DynamoDB `tripIntent` attribute rather than owning vehicle state itself. Trip completion no longer tears down the command channel.  
If a command is not acknowledged, check `connectionStatus` on the vehicle record: it is written only after a confirmed MQTT session, so a value other than `connected` means the command channel is not live.

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