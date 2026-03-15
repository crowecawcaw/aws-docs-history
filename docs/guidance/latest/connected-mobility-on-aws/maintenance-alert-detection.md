# Maintenance alert detection

The MaintenanceProcessor consumes from the `cms-telemetry-maintenance` Kafka topic and analyzes vehicle health signals to detect conditions that require maintenance attention.

## Vehicle type detection

The processor automatically detects whether a vehicle is ICE (Internal Combustion Engine) or EV (Electric Vehicle) based on the telemetry signals present:

- **EV detected** — If `soc` (state of charge) > 0, or `volt` (HV battery voltage) > 0, or `regen_pwr` (regenerative braking power) ≠ 0
- **ICE detected** — If `fuel_rate` > 0 or `oil_life` > 0

A vehicle can be both (hybrid). The processor applies the appropriate maintenance rules based on the detected type.

## ICE vehicle alerts

| Alert Type           | Severity | Condition            | DTC Code |
| -------------------- | -------- | -------------------- | -------- |
| OIL_CHANGE_OVERDUE   | CRITICAL | oil_life < 10%       | P0524    |
| OIL_CHANGE_DUE       | HIGH     | oil_life < 25%       | P0524    |
| OIL_PRESSURE_LOW     | CRITICAL | oilPressure < 15 PSI | P0520    |
| OIL_PRESSURE_WARNING | HIGH     | oilPressure < 25 PSI | P0520    |
| ENGINE_OVERHEATING   | CRITICAL | engineTemp > 230°F   | P0217    |
| ENGINE_RUNNING_HOT   | HIGH     | engineTemp > 210°F   | P0217    |
| COOLANT_OVERHEATING  | CRITICAL | coolant_temp > 220°F | P0217    |

## EV vehicle alerts

| Alert Type                   | Severity | Condition                                           |
| ---------------------------- | -------- | --------------------------------------------------- |
| HV_BATTERY_VOLTAGE_LOW       | CRITICAL | volt < 300V (battery pack failure risk)             |
| HV_BATTERY_DEGRADATION       | HIGH     | volt < 320V (capacity loss)                         |
| HV_BATTERY_OVERVOLTAGE       | CRITICAL | volt > 450V (charger malfunction)                   |
| BATTERY_CRITICALLY_LOW       | CRITICAL | soc < 5%                                            |
| BATTERY_LOW_WARNING          | HIGH     | soc < 15%                                           |
| BATTERY_CAPACITY_DEGRADATION | MEDIUM   | soc > 95% AND volt < 380V (full charge voltage low) |
| REGEN_BRAKING_EXCESSIVE      | MEDIUM   | regen_pwr < -50 kW                                  |
| BATTERY_COOLING_OVERTEMP     | HIGH     | coolant_temp > 60°F (thermal management failure)    |
| MOTOR_OVERHEATING            | CRITICAL | engineTemp > 150°F (motor protection required)      |
| MOTOR_RUNNING_HOT            | HIGH     | engineTemp > 130°F                                  |
| CHARGING_SYSTEM_OVERVOLTAGE  | HIGH     | batteryVoltage > 15V (12V system)                   |

## Common alerts (ICE and EV)

| Alert Type                 | Severity | Condition                            |
| -------------------------- | -------- | ------------------------------------ |
| BRAKE_REPLACEMENT_CRITICAL | CRITICAL | brake_wear < 20% (ICE) or < 15% (EV) |
| BRAKE_REPLACEMENT_DUE      | HIGH     | brake_wear < 35% (ICE) or < 30% (EV) |
| TIRE_REPLACEMENT_CRITICAL  | CRITICAL | any tire tread < 2.0mm               |
| TIRE_REPLACEMENT_DUE       | HIGH     | any tire tread < 4.0mm               |
| FILTER_REPLACEMENT         | HIGH     | filter_life < 15%                    |
| LOW_BATTERY_12V            | CRITICAL | batteryVoltage < 11.5V               |
| DTC_ACTIVE                 | HIGH     | dtc_codes_active = 1                 |

Note: EV vehicles have higher brake wear thresholds because regenerative braking reduces mechanical brake usage.

## Processing flow

For each telemetry message:

1. Parse the JSON and extract all maintenance-critical signal values.
2. Detect vehicle type (ICE, EV, or hybrid) from the signals present.
3. Apply the appropriate maintenance rules based on vehicle type.
4. For each triggered alert, check deduplication: has this alert type already been generated for this message hash?
5. Write each new alert to the `cms-{stage}-storage-maintenance-alerts` DynamoDB table.

## Maintenance alert DynamoDB record

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
