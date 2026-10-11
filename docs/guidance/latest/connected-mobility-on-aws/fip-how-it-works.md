

# How it works
<a name="fip-how-it-works"></a>

Each screen in the portal reads the output of a stream-processing flow or a command path. The subsections below describe each flow end to end, from vehicle telemetry to the record the portal renders.

## Trip lifecycle
<a name="trip-lifecycle"></a>

How trips are detected, tracked, and completed using ignition state transitions and stateful stream processing.

The TripProcessor detects trip boundaries from ignition signal transitions. It does not rely on simulator-provided trip IDs or engine event strings, making it compatible with both MQTT Direct and FleetWise Edge telemetry.

### Detection flow
<a name="trip-detection-flow-platform"></a>

The TripProcessor consumes from the `cms-telemetry-trips` Kafka topic (routed by the EventDrivenTelemetryProcessor) and uses the `ignitionOn` signal to detect trip boundaries:


| Previous Ignition | Current Ignition | Action | 
| --- | --- | --- | 
| OFF (or null) | ON |  **Start trip**: Generate trip ID, create ACTIVE trip in DynamoDB, set active trip in Redis | 
| ON | ON |  **Continue trip**: Accumulate route points and metrics, flush to DynamoDB periodically | 
| ON | OFF |  **End trip**: Update trip status to COMPLETED, calculate final metrics, clear active trip from Redis | 
| OFF | OFF | Ignore (no active trip) | 

### Trip ID generation
<a name="trip-id-generation"></a>

When a new trip starts, the processor generates a trip ID using the pattern:

```
{vehicleId}-{timestamp}-{randomHex}
```

For example: `VEH-0049-1709751600000-fc9567` 

If the incoming telemetry message already contains a `tripId` (from the simulator), the processor uses that value instead. This ensures trip IDs are consistent between the simulator’s intent and the processor’s detection.

### State management
<a name="trip-state-management"></a>

The TripProcessor maintains trip state in three locations:

1.  **In-memory ConcurrentHashMap** — Maps `vehicleId` → `tripId` for the currently active trip. This is the primary lookup, avoiding DynamoDB reads on every message. Uses `putIfAbsent` to prevent race conditions when multiple messages arrive simultaneously for the same vehicle.

1.  **Redis** — The active trip ID is written to `vehicle:{vehicleId}:activeTrip` on trip start and deleted on trip end. This allows the TelemetryProcessor (a separate Flink application) to tag telemetry records with the correct `tripId` without querying DynamoDB. The FWTelemetryProcessor also reads this cache to tag FleetWise telemetry with trip IDs.

1.  **DynamoDB** — The authoritative trip record. Written on trip start (PutItem), updated periodically during the trip (UpdateItem every 5 messages to append route points and update metrics), and finalized on trip end (UpdateItem with COMPLETED status and final metrics).

### Closing trips that never close
<a name="trip-stuck-sweeper"></a>

The TripProcessor closes a trip when it sees an ignition-off frame, or when a 30-minute inactivity timeout fires. Both paths depend on the processor continuing to see telemetry for that vehicle, and in practice three situations defeat them:
+ The simulator or the Edge Agent stops without emitting an ignition-off frame.
+ The Flink application restarts mid-trip — a deploy, a failure, a scaling event — and loses the in-memory vehicle-to-trip map that gates the timeout path.
+ Telemetry simply stops arriving for a vehicle, with no indicator either way.

In all three the trip stays `ACTIVE` indefinitely. That is more than cosmetic: the vehicle appears to be permanently driving, and aggregate mileage, duration and driver scoring are computed from trip records, so every downstream figure derived from them is wrong.

A scheduled Lambda closes them as a third layer. It runs hourly on the EventBridge rule `cms-trip-sweeper-hourly`, scans the trips table for `status=ACTIVE`, and for any row whose `lastUpdated` is older than a threshold — two hours by default, configurable through `STUCK_THRESHOLD_MS` — updates the row to `COMPLETED` with an end time, a duration and audit fields recording that the sweep closed it rather than a telemetry frame. A `DRY_RUN` setting logs what would be closed without writing.

The sweeper is deliberately conservative: it keys on `lastUpdated` rather than on trip start, so a long but genuinely active trip is not closed while telemetry is still arriving. Its permissions are limited to scanning and updating that one table.

**Note**  
The sweeper publishes a `TripsClosed` metric under the `CMS/TripSweeper` namespace, and that metric is the signal worth watching rather than the sweep itself. An occasional closure is the mechanism working as intended. A **sustained** nonzero rate means the primary closure paths are failing upstream — most often a processor that is running but idle — and the sweeper is masking it. No alarm ships on this metric; see [What no alarm covers](mon-build-a-dashboard.md).

### Trip DynamoDB record
<a name="trip-dynamodb-record"></a>

A trip record progresses through these states:

 **On trip start (ignition ON):** 

```
{
  "tripId": "VEH-0049-1709751600000-fc9567",
  "vehicleId": "VEH-0049",
  "driverId": "DRV-001",
  "status": "ACTIVE",
  "startTime": 1709751600000,
  "startLocation": {"lat": 40.7128, "lng": -74.0060},
  "route": [{"lat": 40.7128, "lng": -74.0060, "ts": 1709751600000}],
  "maxSpeed": 0,
  "totalDistance": 0,
  "telemetryCount": 1,
  "source": "mqtt_direct"
}
```

 **During trip (periodic flush every 5 messages):** 

The processor uses `UpdateItem` (not `PutItem`) to append route points and update running metrics without overwriting the full record. This eliminates race conditions from concurrent writes.

 **On trip end (ignition OFF):** 

```
{
  "tripId": "VEH-0049-1709751600000-fc9567",
  "vehicleId": "VEH-0049",
  "driverId": "DRV-001",
  "status": "COMPLETED",
  "startTime": 1709751600000,
  "endTime": 1709755200000,
  "startLocation": {"lat": 40.7128, "lng": -74.0060},
  "endLocation": {"lat": 40.7589, "lng": -73.9851},
  "route": [{"lat": 40.7128, "lng": -74.0060, "ts": 1709751600000}, "..."],
  "maxSpeed": 65.5,
  "totalDistance": 12.3,
  "duration": 3600,
  "telemetryCount": 120,
  "source": "mqtt_direct"
}
```

### DynamoDB write optimization
<a name="trip-write-optimization"></a>

The stateful design reduces DynamoDB operations compared to a stateless approach:


| Operation | Stateless (per message) | Stateful (current) | 
| --- | --- | --- | 
| DynamoDB reads | 2-3 (GetItem \+ GSI query) | 0 (in-memory \+ Redis) | 
| DynamoDB writes | 1 PutItem (full record) | 1 UpdateItem every 5 messages | 
| 20-message trip total | \~60 reads \+ 20 writes | 0 reads \+ 5 writes | 

Only the TripProcessor writes to the trips table. The TelemetryProcessor tags telemetry records with `tripId` for querying but does not write to the trips table. This single-writer pattern prevents data clobbering between processors.

## Safety event detection
<a name="safety-event-detection"></a>

How the SafetyProcessor identifies unsafe driving behaviors from telemetry signals using a catalog-driven rule engine.

The SafetyProcessor consumes from the `cms-telemetry-safety` Kafka topic and evaluates each telemetry message against a set of safety rules to detect dangerous driving behaviors.

### Catalog-driven architecture
<a name="safety-catalog-driven"></a>

The SafetyProcessor uses a **catalog-driven** approach rather than hardcoded thresholds. Safety event rules are loaded from the `cms-{stage}-event-catalog` DynamoDB table on startup and refreshed every 5 minutes. This allows operators to modify detection thresholds without redeploying the Flink application.

Each rule in the event catalog defines:
+  **Event type** — The safety event name (for example, `SPEEDING`, `HARD_BRAKING`)
+  **Trigger signal** — The telemetry signal to evaluate (for example, `speed`, `harsh_brk`)
+  **Operator** — Comparison operator (`>`, `<`, `=`, `!=`)
+  **Threshold** — The trigger value
+  **Severity** — `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` 
+  **Cooldown** — Minimum time between repeated events of the same type for the same vehicle

### Event types and thresholds
<a name="safety-event-types"></a>


| Event Type | Trigger Signal | Operator | Threshold | Description | 
| --- | --- | --- | --- | --- | 
| SPEEDING | speed | > | 65 mph | Vehicle exceeding speed limit | 
| HARD\_BRAKING | harsh\_brk | > | 0.3g | Sudden deceleration | 
| RAPID\_ACCELERATION | harsh\_acc | > | 0.3g | Sudden acceleration | 
| HARSH\_CORNERING | harsh\_turn | > | 40 deg/s | Sharp turn | 
| SEATBELT\_VIOLATION | seatbelt | = | 0 | Seatbelt unfastened while driving | 
| PHONE\_USAGE | phone\_use | = | 1 | Phone in use while driving | 
| LANE\_DEPARTURE | lateralG | > | 0.5g | Excessive lateral acceleration | 
| TAILGATING | followingDistance | < | 2.0m | Following too closely | 
| AEB\_ACTIVATION | aeb\_act | = | 1 | Automatic emergency braking triggered | 
| ESC\_ACTIVATION | esc\_act | = | 1 | Electronic stability control triggered | 

### Processing flow
<a name="safety-processing-flow"></a>

For each telemetry message:

1. Parse the JSON and extract all signal values.

1. Load the signal catalog to resolve JSON field names to signal metadata (if not already cached).

1. Iterate over each safety rule from the event catalog.

1. For each rule, extract the trigger signal value from the telemetry message.

1. Evaluate the signal value against the rule’s operator and threshold.

1. If the rule triggers, check the cooldown map: has this event type fired for this vehicle within the cooldown period (default 5 minutes)?

1. If not in cooldown, generate a safety event and write it to the `cms-{stage}-storage-safety-events` DynamoDB table.

1. Update the cooldown map with the current timestamp.

### Safety event DynamoDB record
<a name="safety-event-record"></a>

```
{
  "eventId": "SE-a1b2c3d4",
  "vehicleId": "VEH-0049",
  "tripId": "VEH-0049-1709751600000-fc9567",
  "driverId": "DRV-001",
  "eventType": "HARD_BRAKING",
  "severity": "HIGH",
  "timestamp": 1709752800000,
  "location": {"lat": 40.7350, "lng": -73.9900},
  "speed": 45.2,
  "triggerSignal": "harsh_brk",
  "triggerValue": 0.45,
  "threshold": 0.3,
  "message": "Hard braking detected: 0.45g (threshold: 0.3g)"
}
```

### Deduplication
<a name="safety-deduplication"></a>

The SafetyProcessor prevents alert fatigue through two mechanisms:
+  **Cooldown per vehicle per event type** — After a safety event fires for a vehicle, the same event type will not fire again for that vehicle for 5 minutes (configurable). This prevents a vehicle driving at 70 mph from generating a SPEEDING event every second.
+  **Message deduplication** — Each telemetry message is hashed and checked against a processed set to prevent duplicate processing from Kafka redelivery.

## Maintenance alert detection
<a name="maintenance-alert-detection"></a>

How the MaintenanceProcessor generates predictive maintenance alerts from vehicle health signals, with separate logic for ICE and EV vehicles.

The MaintenanceProcessor consumes from the `cms-telemetry-maintenance` Kafka topic and analyzes vehicle health signals to detect conditions that require maintenance attention.

### Vehicle type detection
<a name="maintenance-vehicle-type-detection"></a>

The processor automatically detects whether a vehicle is ICE (Internal Combustion Engine) or EV (Electric Vehicle) based on the telemetry signals present:
+  **EV detected** — If `soc` (state of charge) > 0, or `volt` (HV battery voltage) > 0, or `regen_pwr` (regenerative braking power) ≠ 0
+  **ICE detected** — If `fuel_rate` > 0 or `oil_life` > 0

A vehicle can be both (hybrid). The processor applies the appropriate maintenance rules based on the detected type.

### ICE vehicle alerts
<a name="maintenance-ice-alerts"></a>


| Alert Type | Severity | Condition | DTC Code | 
| --- | --- | --- | --- | 
| OIL\_CHANGE\_OVERDUE | CRITICAL | oil\_life < 10% | P0524 | 
| OIL\_CHANGE\_DUE | HIGH | oil\_life < 25% | P0524 | 
| OIL\_PRESSURE\_LOW | CRITICAL | oilPressure < 15 PSI | P0520 | 
| OIL\_PRESSURE\_WARNING | HIGH | oilPressure < 25 PSI | P0520 | 
| ENGINE\_OVERHEATING | CRITICAL | engineTemp > 230°F | P0217 | 
| ENGINE\_RUNNING\_HOT | HIGH | engineTemp > 210°F | P0217 | 
| COOLANT\_OVERHEATING | CRITICAL | coolant\_temp > 220°F | P0217 | 

### EV vehicle alerts
<a name="maintenance-ev-alerts"></a>


| Alert Type | Severity | Condition | 
| --- | --- | --- | 
| HV\_BATTERY\_VOLTAGE\_LOW | CRITICAL | volt < 300V (battery pack failure risk) | 
| HV\_BATTERY\_DEGRADATION | HIGH | volt < 320V (capacity loss) | 
| HV\_BATTERY\_OVERVOLTAGE | CRITICAL | volt > 450V (charger malfunction) | 
| BATTERY\_CRITICALLY\_LOW | CRITICAL | soc < 5% | 
| BATTERY\_LOW\_WARNING | HIGH | soc < 15% | 
| BATTERY\_CAPACITY\_DEGRADATION | MEDIUM | soc > 95% AND volt < 380V (full charge voltage low) | 
| REGEN\_BRAKING\_EXCESSIVE | MEDIUM | regen\_pwr < -50 kW | 
| BATTERY\_COOLING\_OVERTEMP | HIGH | coolant\_temp > 60°F (thermal management failure) | 
| MOTOR\_OVERHEATING | CRITICAL | engineTemp > 150°F (motor protection required) | 
| MOTOR\_RUNNING\_HOT | HIGH | engineTemp > 130°F | 
| CHARGING\_SYSTEM\_OVERVOLTAGE | HIGH | batteryVoltage > 15V (12V system) | 

### Common alerts (ICE and EV)
<a name="maintenance-common-alerts"></a>


| Alert Type | Severity | Condition | 
| --- | --- | --- | 
| BRAKE\_REPLACEMENT\_CRITICAL | CRITICAL | brake\_wear < 20% (ICE) or < 15% (EV) | 
| BRAKE\_REPLACEMENT\_DUE | HIGH | brake\_wear < 35% (ICE) or < 30% (EV) | 
| TIRE\_REPLACEMENT\_CRITICAL | CRITICAL | any tire tread < 2.0mm | 
| TIRE\_REPLACEMENT\_DUE | HIGH | any tire tread < 4.0mm | 
| FILTER\_REPLACEMENT | HIGH | filter\_life < 15% | 
| LOW\_BATTERY\_12V | CRITICAL | batteryVoltage < 11.5V | 
| DTC\_ACTIVE | HIGH | dtc\_codes\_active = 1 | 

Note: EV vehicles have higher brake wear thresholds because regenerative braking reduces mechanical brake usage.

### Processing flow
<a name="maintenance-processing-flow"></a>

For each telemetry message:

1. Parse the JSON and extract all maintenance-critical signal values.

1. Detect vehicle type (ICE, EV, or hybrid) from the signals present.

1. Apply the appropriate maintenance rules based on vehicle type.

1. For each triggered alert, check deduplication: has this alert type already been generated for this message hash?

1. Write each new alert to the `cms-{stage}-storage-maintenance-alerts` DynamoDB table.

### Maintenance alert DynamoDB record
<a name="maintenance-alert-record"></a>

```
{
  "alertId": "MA-e5f6g7h8",
  "vehicleId": "VEH-0049",
  "tripId": "VEH-0049-1709751600000-fc9567",
  "alertType": "ENGINE_OVERHEATING",
  "severity": "CRITICAL",
  "timestamp": 1709753400000,
  "message": "Engine overheating: 235°F - cooling system failure",
  "triggerSignal": "engineTemp",
  "triggerValue": 235.0,
  "threshold": 230.0,
  "dtcCode": "P0217",
  "vehicleType": "ICE",
  "rule": "engineTemp > 230°F"
}
```

## Remote commands
<a name="remote-commands-flow"></a>

How the bidirectional command system sends instructions to vehicles and tracks execution status across both MQTT Direct and FleetWise Edge vehicles.

The remote commands system enables fleet managers to send actuator commands to vehicles (lock doors, flash lights, start engine) and track whether the vehicle executed the command successfully. Commands are sent through a single API endpoint and published in two wire formats — JSON on `cms/commands/{vehicleId}/request` and protobuf on the FleetWise Edge command topic.

**Important**  
 **Actuation happens on the JSON path for both vehicle classes.** The protobuf path carries transport and response handling: the FWE agent subscribes to it, parses the `CommandRequest`, and returns a `CommandResponse`. The agent answers actuator commands with `reason_code` 3 (`NO_DECODING_RULES_FOUND`).  
For FleetWise Edge vehicles, the component that actually executes a command is the **simulator** task, not the agent: it applies the command to its vehicle state and writes the resulting CAN frame, which the FWE agent then decodes and reports as telemetry. This means the mutated state is observable through the genuine FleetWise decode path. See [FleetWise Edge native actuation](#command-fwe-actuation-limits).

### End-to-end flow
<a name="command-flow-detail"></a>

1.  **Fleet Intelligence portal** — The operator selects a vehicle, chooses a command from the catalog (for example, "Lock Doors"), and clicks send.

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

1.  **Vehicle receives and responds** — The receiving component publishes a response. On the FleetWise Edge path the agent answers on the protobuf topic (a rejection with `reason_code` 3 — see [FleetWise Edge native actuation](#command-fwe-actuation-limits)), while the simulator performs the actuation and answers on the JSON topic:

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

1.  **UI update** — The Fleet Intelligence portal polls the command history endpoint and displays the updated status and latency.

### Why dual-path publishing
<a name="command-dual-path"></a>

The Commands Lambda publishes to both topics on every command because the Lambda does not know which protocol the target vehicle uses. MQTT Direct simulators subscribe to `cms/commands/{vehicleId}/request` (JSON), while FWE agents subscribe to `cms/commands/things/{vin}/executions/+/request/protobuf` (protobuf).

For an MQTT Direct vehicle only the JSON publish has a subscriber; the protobuf publish is discarded by the broker. For a FleetWise Edge vehicle **both** publishes have subscribers, so two responses arrive and they disagree — the simulator returns `SUCCEEDED` (it performed the actuation) and the agent returns `FAILED` with `reason_code` 3 (it cannot). Because the agent is usually slower, the Response Handler applies a precedence rule: **a non-success response may not move a command out of `SUCCEEDED` **. Without that rule, last-write-wins would report a failure for a command that succeeded.

This approach avoids the need to track which protocol each vehicle uses and ensures commands work regardless of the vehicle’s telemetry source.

### FleetWise Edge native actuation
<a name="command-fwe-actuation-limits"></a>

The FWE agent receives and answers protobuf command requests, and the simulator’s CAN write-back performs the actuation. To actuate natively in the FWE agent, add four pieces:

1.  **The actuator signal must be declared as a custom-decoding signal.** The agent resolves an incoming command’s signal ID against a map built exclusively from the decoder manifest’s `custom_decoding_signals`. The solution emits actuator signals as `can_signals`, so the lookup misses and the command is rejected with `NO_DECODING_RULES_FOUND`.

1.  **A command dispatcher must be registered.** This requires a `canCommandInterface` entry in the agent’s network-interface configuration; the generated configuration declares `canInterface`, `obdInterface`, and the UDS-DTC example interface only. Without it the agent reports `NO_COMMAND_DISPATCHER_FOUND`.

1.  **The CAN actuator map must include the solution’s actuators.** AWS IoT FleetWise Edge v1.3.2 hardcodes its CAN command actuator map to two example entries and exposes no runtime configuration for it, so a source patch is required — the same pattern the image build already uses for the DTC signal list and extended CAN IDs.

1.  **A CAN command responder must exist.** The agent’s CAN command dispatcher sends a request frame on a configured CAN ID and waits for a matching response frame carrying the command ID, a status code, and a reason. With nothing answering on the bus, commands end in `EXECUTION_TIMEOUT`.

Without these pieces, the protobuf path is the transport and acknowledgement mechanism, and the simulator’s CAN write-back is the actuation seam.

**Note**  
On the FleetWise Edge path, command handling does **not** depend on a trip being in progress. The long-lived per-vehicle task runs two containers: the FleetWise Edge agent, and a `vehicle-ecu` sidecar that owns the command subscription and the vehicle’s state, and puts that state on the vcan device on an idle cadence. A parked vehicle is therefore commandable, and the resulting state change is observable in telemetry within one idle tick.  
Trips remain a separate, ephemeral `fwe-simulator` task; it signals the sidecar through a DynamoDB `tripIntent` attribute rather than owning vehicle state itself. Trip completion no longer tears down the command channel.  
If a command is not acknowledged, check `connectionStatus` on the vehicle record: it is written only after a confirmed MQTT session, so a value other than `connected` means the command channel is not live.

### Protobuf encoding
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

### Command catalog
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

## Last Known State pattern
<a name="last-known-state-pattern"></a>

How Redis maintains a real-time snapshot of every vehicle’s state for sub-millisecond lookups.

Connected vehicle platforms face a fundamental read/write asymmetry: telemetry arrives at high frequency (every 1-3 seconds per vehicle), but the Fleet Intelligence portal only needs the *current* value of each signal. Querying DynamoDB for the latest telemetry record on every page load would be expensive and slow at scale.

The Last Known State (LKS) pattern solves this by maintaining a continuously updated snapshot of each vehicle’s state in Redis.

### Write path
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

### Read path
<a name="lks-read-path-detail"></a>

The Fleet Intelligence portal API Lambda reads LKS data through two mechanisms:

 **Vehicle detail view:** The Lambda calls `HGETALL` on three hashes (`signals`, `timestamps`, `meta`) and overlays the live state onto the DynamoDB vehicle record. Signal IDs are resolved to human-readable names using the `signal_catalog:reverse` hash. This provides the UI with current speed, location, engine state, and all other signals without querying the telemetry table.

 **Map view:** The Lambda calls `GEOSEARCH vehicle:locations FROMLONLAT {lng} {lat} BYRADIUS {km} km` to find all vehicles within a geographic area. This returns vehicle IDs with coordinates, which the UI plots on the map. No DynamoDB scan is needed.

 **Sparkline charts:** The Lambda calls `XRANGE vehicle:{id}:stream` to retrieve the last 100 signal snapshots for rendering mini time-series charts in the vehicle detail view.

### TTL and lifecycle
<a name="lks-ttl-lifecycle"></a>
+ All per-vehicle keys expire after 5 minutes of inactivity (configurable via `REDIS_TTL`).
+ Each telemetry message resets the TTL, so active vehicles never expire.
+ When a vehicle stops sending telemetry, its state expires automatically — the map view clears, and the vehicle detail page falls back to DynamoDB-only data.
+ The geo index entry is explicitly removed on ignition OFF, so the map shows only vehicles with active trips.
+ The signal catalog keys (`signal_catalog:map`, `signal_catalog:reverse`) do not expire — they are refreshed on Flink startup or when the version key changes.

### Graceful fallback
<a name="lks-fallback"></a>

The Fleet Intelligence portal API Lambda uses a minimal raw-socket RESP client that caches Redis availability for 60 seconds. If Redis is unreachable (ElastiCache maintenance, network issue), the Lambda falls back gracefully to DynamoDB-only responses. The UI still works — it just shows slightly stale data from the last DynamoDB write instead of real-time Redis state.

## Driver scoring
<a name="driver-scoring"></a>

How the guidance calculates per-trip driver safety scores from telemetry and safety events.

The TripProcessor calculates a driver safety score for each trip on a 0–100 scale. The score starts at 100 (perfect) and is reduced by deductions for safety events and unsafe driving behavior detected during the trip.

### Scoring formula
<a name="scoring-formula"></a>

The score is calculated from two sources:

 **1. Safety event deductions (primary):** 

The TripProcessor queries the safety events table for all events associated with the current trip and applies deductions based on severity and event type. Each unique event type is counted only once to avoid double-penalizing repeated events of the same kind.


| Severity | Example Events | Deduction | 
| --- | --- | --- | 
| CRITICAL | Collision avoidance, rollover risk | -15 points | 
| CRITICAL | Engine overheat, coolant overheat | -10 points | 
| CRITICAL | Other critical events | -12 points | 
| HIGH | Tire pressure critical, airbag malfunction, seatbelt violation | -8 points | 
| HIGH | Oil pressure low | -6 points | 
| HIGH | Other high-severity events | -5 points | 
| MEDIUM | Speeding, harsh braking, harsh acceleration | -3 points | 
| LOW | Minor infractions | -1 point | 

 **2. Real-time telemetry deductions (secondary):** 

On each telemetry message during the trip, the processor applies small deductions for:
+ Speed > 80 mph: -1 point
+ Harsh braking signal (`harsh_brk`) > 0.3g: -0.5 points
+ Harsh acceleration signal (`harsh_acc`) > 0.3g: -0.5 points
+ Harsh turn signal (`harsh_turn`) > 40 deg/s: -0.5 points

The score is clamped to the range 0–100.

### Score lifecycle
<a name="scoring-lifecycle"></a>

1.  **Trip start** — Score initialized at 100.

1.  **During trip** — Score updated on each telemetry message with real-time deductions. Safety event deductions are applied as events are detected by the SafetyProcessor.

1.  **Trip end** — Final score recalculated with all safety events for the trip.

1.  **Delayed rescore** — 30 seconds after trip completion, the TripProcessor re-queries the safety events table and recalculates the score. This accounts for safety events that were still being processed when the trip ended.

The final `driverScore` is stored on the trip record in DynamoDB and displayed in the Fleet Intelligence portal on the trip detail page and driver profile.

### Score display
<a name="scoring-display"></a>

The Fleet Intelligence portal displays driver scores in several places:
+  **Driver detail page** — Per-driver score history across trips
+  **Trip detail page** — Individual trip score with breakdown of safety events that caused deductions
+  **Map view** — Vehicle cards show the current trip’s running score

## Campaign management
<a name="campaign-management-ui"></a>

How fleet operators create and manage FleetWise data collection campaigns through the web application.

The Fleet Intelligence portal includes a Data Collection section where operators create, monitor, and manage FleetWise campaigns without writing code or using the AWS CLI.

### Create Campaign wizard
<a name="create-campaign-wizard"></a>

The wizard walks operators through campaign creation in four steps:

 **Step 1 — Campaign details:** 
+ Campaign name and description
+ Scheme type: **Condition-based** (collect when a signal crosses a threshold) or **Time-based** (collect at fixed intervals)
+ For condition-based: select the trigger signal, operator (>, <, =), threshold value, and trigger mode (rising edge or always)
+ Minimum collection interval (milliseconds between samples)
+ Optional: link to a safety event definition from the event catalog

 **Step 2 — Signal selection:** 
+ Browse all 260\+ signals from the signal catalog, grouped by category
+ Multi-select signals to include in the campaign
+ Each signal shows its name, VSS path, unit, and signal group
+ Select a decoder manifest (the default `cms-fleet-v1` is pre-selected if only one exists)

 **Step 3 — Vehicle targeting:** 
+ Browse registered vehicles from DynamoDB
+ Multi-select vehicles to target with this campaign
+ If launched from a vehicle detail page, the vehicle is pre-selected and locked
+ Assign to an entire fleet — all vehicles in the fleet receive the campaign with `sourceFleetId` set. Fleet-assigned campaigns cannot be modified at the vehicle level.

 **Step 4 — Review and create:** 
+ Review all settings before submission
+ On submit, the campaign is written to DynamoDB with status `RUNNING` 
+ The CampaignSyncProcessor picks up the new campaign on the next agent checkin and pushes the collection scheme to targeted vehicles

### Managing campaigns
<a name="campaign-lifecycle-ui"></a>

From the campaigns list view, operators can:
+  **View status** — See which campaigns are RUNNING, SUSPENDED, or COMPLETED
+  **Suspend** — Pause a campaign. The CampaignSyncProcessor pushes an empty collection scheme on the next checkin, stopping signal collection.
+  **Resume** — Reactivate a suspended campaign
+  **Delete** — Remove a campaign permanently

## FleetWise Edge agent controls
<a name="fwe-agent-controls"></a>

How to manage FleetWise Edge agent containers from the Fleet Intelligence portal and simulation service.

When running in FleetWise Edge mode, the simulation service manages per-vehicle FWE agent Docker containers. The Fleet Intelligence portal provides controls to start, stop, and monitor these agents.

### Starting and stopping agents
<a name="agent-start-stop"></a>

From the simulation panel in the Fleet Intelligence portal, operators can:
+  **Select telemetry mode** — Choose between "MQTT Direct" (JSON telemetry published directly to IoT Core) and "FleetWise Edge" (CAN signals collected by FWE agent, encoded as protobuf). The FWE mode description notes that Docker is required.
+  **Start an agent** — The simulation service calls the `/api/agent/start` endpoint with the vehicle ID. The service:

  1. Resolves the vehicle’s VIN from DynamoDB

  1. Retrieves the vehicle’s IoT certificate

  1. Generates FWE persistency files (static config, decoder manifest, collection schemes)

  1. Starts a Docker container named `fwe-{vin}` with the FWE agent image

  1. Configures a virtual CAN bus interface (`vcan0`) inside the container

  1. The agent connects to IoT Core, publishes a checkin, receives campaigns, and begins collecting
+  **Stop an agent** — Stops and removes the Docker container for the specified vehicle
+  **View agent status** — The `/api/agent/status` endpoint returns all running FWE containers with their VINs, uptime, and campaign sync state
+  **Stream agent logs** — The `/api/agent/logs/{vin}` endpoint streams the FWE container’s stdout, showing checkin messages, scheme receipts, and signal collection activity

### Cloud simulation with FWE
<a name="agent-cloud-mode"></a>

In cloud simulation mode, the FWE agent and simulator run as separate EC2-backed ECS tasks on the same host:
+ The `fwe-simulator` task generates CAN frames and writes them to the assigned virtual CAN interface (e.g., `vcan0`)
+ The `fwe-agent` task reads from the same vcan interface, collects signals per campaign, and uploads protobuf to IoT Core
+ Each vehicle gets a unique vcan interface to prevent cross-contamination between simultaneous simulations
+ The simulation Lambda assigns vcan interfaces using `_next_vcan_index()` and passes the interface name to both tasks
+ The FWE agent health check uses `pgrep aws-iot-fleetwise-edge` — once healthy, the simulator task starts