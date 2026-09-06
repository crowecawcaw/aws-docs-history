

# Maintenance alert detection
<a name="maintenance-alert-detection"></a>

The MaintenanceProcessor consumes from the `cms-telemetry-maintenance` Kafka topic and analyzes vehicle health signals to detect conditions that require maintenance attention.

## Vehicle type detection
<a name="maintenance-vehicle-type-detection"></a>

The processor automatically detects whether a vehicle is ICE (Internal Combustion Engine) or EV (Electric Vehicle) based on the telemetry signals present:
+  **EV detected** — If `soc` (state of charge) > 0, or `volt` (HV battery voltage) > 0, or `regen_pwr` (regenerative braking power) ≠ 0
+  **ICE detected** — If `fuel_rate` > 0 or `oil_life` > 0

A vehicle can be both (hybrid). The processor applies the appropriate maintenance rules based on the detected type.

## ICE vehicle alerts
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

## EV vehicle alerts
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

## Common alerts (ICE and EV)
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

## Processing flow
<a name="maintenance-processing-flow"></a>

For each telemetry message:

1. Parse the JSON and extract all maintenance-critical signal values.

1. Detect vehicle type (ICE, EV, or hybrid) from the signals present.

1. Apply the appropriate maintenance rules based on vehicle type.

1. For each triggered alert, check deduplication: has this alert type already been generated for this message hash?

1. Write each new alert to the `cms-{stage}-storage-maintenance-alerts` DynamoDB table.

## Maintenance alert DynamoDB record
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