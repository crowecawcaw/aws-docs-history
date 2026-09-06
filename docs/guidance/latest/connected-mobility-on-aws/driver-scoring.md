

# Driver scoring
<a name="driver-scoring"></a>

The TripProcessor calculates a driver safety score for each trip on a 0–100 scale. The score starts at 100 (perfect) and is reduced by deductions for safety events and unsafe driving behavior detected during the trip.

## Scoring formula
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

## Score lifecycle
<a name="scoring-lifecycle"></a>

1.  **Trip start** — Score initialized at 100.

1.  **During trip** — Score updated on each telemetry message with real-time deductions. Safety event deductions are applied as events are detected by the SafetyProcessor.

1.  **Trip end** — Final score recalculated with all safety events for the trip.

1.  **Delayed rescore** — 30 seconds after trip completion, the TripProcessor re-queries the safety events table and recalculates the score. This accounts for safety events that were still being processed when the trip ended.

The final `driverScore` is stored on the trip record in DynamoDB and displayed in the Fleet Manager UI on the trip detail page and driver profile.

## Score display
<a name="scoring-display"></a>

The Fleet Manager UI displays driver scores in several places:
+  **Dashboard** — Fleet-wide driver score distribution widget
+  **Driver detail page** — Per-driver score history across trips
+  **Trip detail page** — Individual trip score with breakdown of safety events that caused deductions
+  **Map view** — Vehicle cards show the current trip’s running score