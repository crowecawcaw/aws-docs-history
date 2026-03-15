# Remote commands

The remote commands system enables fleet managers to send actuator commands to vehicles (lock doors, flash lights, start engine) and track whether the vehicle executed the command successfully.

## End-to-end flow

1. **Fleet Manager UI** — The operator selects a vehicle, chooses a command from the catalog (for example, "Lock Doors"), and clicks send.
2. **API Gateway → Commands Lambda** — The request hits POST `/api/commands/{vehicleId}`. The Lambda validates the command name against the signal catalog (only signals with an `actuator` attribute are valid commands).
3. **MQTT publish** — The Lambda publishes the command payload to `cms/commands/{vehicleId}/request` via IoT Core MQTT with QoS 1:

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

4. **DynamoDB write** — The Lambda stores the command with status `SENT` and a 7-day TTL.
5. **Vehicle receives command** — The vehicle (or simulator) is subscribed to `cms/commands/{vehicleId}/request`. It parses the command, executes the action, and publishes a response to `cms/commands/{vehicleId}/response`:

```
{
  "commandId": "a1b2c3d4e5f6",
  "vehicleId": "VEH-0049",
  "status": "SUCCEEDED",
  "reason": "",
  "resultValue": "true"
}
```

6. **IoT Rule → Response Handler Lambda** — The IoT Rule on `cms/commands/+/response` triggers the Command Response Handler Lambda.
7. **Status update** — The Response Handler updates the command in DynamoDB: sets the status, records the response timestamp, and calculates the round-trip latency in milliseconds by comparing `issuedAtMs` with the current time.
8. **UI update** — The Fleet Manager UI polls the command history endpoint and displays the updated status and latency.

## Command catalog

The command catalog is not hardcoded — it is dynamically derived from the signal catalog. Any signal in the `cms-{stage}-signal-catalog` DynamoDB table that has an `actuator` attribute is exposed as an available command.

Each actuator definition includes:

- `commandName` — Identifier used in the MQTT payload (for example, `lock_doors`)
- `label` — Human-readable name for the UI (for example, "Lock Doors")
- `category` — Grouping for the UI (doors, lights, climate, windows, trunk, horn, engine)
- `valueType` — Data type: `boolean`, `number`, or `enum`
- `min` / `max` — Valid range for numeric commands (for example, temperature 60-85°F)
- `options` — Valid values for enum commands (for example, headlight modes: off, low, high)
- `responseTimeout` — Expected response time in milliseconds
- `unit` — Unit of measurement (if applicable)

This design means new commands can be added by inserting a signal with an `actuator` attribute into the signal catalog — no code changes required.
