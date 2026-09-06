

# Safety event detection
<a name="safety-event-detection"></a>

The SafetyProcessor consumes from the `cms-telemetry-safety` Kafka topic and evaluates each telemetry message against a set of safety rules to detect dangerous driving behaviors.

## Catalog-driven architecture
<a name="safety-catalog-driven"></a>

The SafetyProcessor uses a **catalog-driven** approach rather than hardcoded thresholds. Safety event rules are loaded from the `cms-{stage}-event-catalog` DynamoDB table on startup and refreshed every 5 minutes. This allows operators to modify detection thresholds without redeploying the Flink application.

Each rule in the event catalog defines:
+  **Event type** — The safety event name (for example, `SPEEDING`, `HARD_BRAKING`)
+  **Trigger signal** — The telemetry signal to evaluate (for example, `speed`, `harsh_brk`)
+  **Operator** — Comparison operator (`>`, `<`, `=`, `!=`)
+  **Threshold** — The trigger value
+  **Severity** — `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` 
+  **Cooldown** — Minimum time between repeated events of the same type for the same vehicle

## Event types and thresholds
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

## Processing flow
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

## Safety event DynamoDB record
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

## Deduplication
<a name="safety-deduplication"></a>

The SafetyProcessor prevents alert fatigue through two mechanisms:
+  **Cooldown per vehicle per event type** — After a safety event fires for a vehicle, the same event type will not fire again for that vehicle for 5 minutes (configurable). This prevents a vehicle driving at 70 mph from generating a SPEEDING event every second.
+  **Message deduplication** — Each telemetry message is hashed and checked against a processed set to prevent duplicate processing from Kafka redelivery.