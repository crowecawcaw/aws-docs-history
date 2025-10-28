# Additional interface examples

Here are additional examples of how interfaces can be used in different industrial
scenarios:

## Energy generation equipment

A power generation company can use interfaces to standardize metrics across different
types of generation equipment:

```
{
  "assetModelName": "GENERATOR-INTERFACE",
  "assetModelDescription": "Standard interface for power generators",
  "assetModelType": "INTERFACE",
  "assetModelProperties": [
    {
      "name": "ActivePower",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "MW"
    },
    {
      "name": "ReactivePower",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "MVAR"
    },
    {
      "name": "Frequency",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "Hz"
    },
    {
      "name": "PowerFactor",
      "dataType": "DOUBLE",
      "type": {
        "metric": {
          "expression": "cos(atan(ReactivePower / ActivePower))",
          "variables": [
            {
              "name": "ActivePower",
              "value": { "propertyId": "${ActivePower}" }
            },
            {
              "name": "ReactivePower",
              "value": { "propertyId": "${ReactivePower}" }
            }
          ],
          "window": { "tumbling": { "interval": "5m" } }
        }
      },
      "unit": "None"
    }
  ]
}
```

This interface can be applied to various generator asset models (gas turbines, steam
turbines, wind turbines) to ensure consistent power metrics across the fleet.

## Water treatment facilities

A water utility can use interfaces to standardize monitoring across treatment
plants:

```
{
  "assetModelName": "WATER-QUALITY-INTERFACE",
  "assetModelDescription": "Standard interface for water quality monitoring",
  "assetModelType": "INTERFACE",
  "assetModelProperties": [
    {
      "name": "pH",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "pH"
    },
    {
      "name": "Turbidity",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "NTU"
    },
    {
      "name": "DissolvedOxygen",
      "dataType": "DOUBLE",
      "type": { "measurement": {} },
      "unit": "mg/L"
    },
    {
      "name": "QualityIndex",
      "dataType": "DOUBLE",
      "type": {
        "metric": {
          "expression": "(pH >= 6.5 && pH <= 8.5 ? 100 : 50) * (Turbidity < 1 ? 1 : 0.8) * (DissolvedOxygen > 5 ? 1 : 0.7)",
          "variables": [
            {
              "name": "pH",
              "value": { "propertyId": "${pH}" }
            },
            {
              "name": "Turbidity",
              "value": { "propertyId": "${Turbidity}" }
            },
            {
              "name": "DissolvedOxygen",
              "value": { "propertyId": "${DissolvedOxygen}" }
            }
          ],
          "window": { "tumbling": { "interval": "1h" } }
        }
      },
      "unit": "Score"
    }
  ]
}
```

This interface ensures that water quality is measured consistently across all treatment
facilities, regardless of their specific equipment configurations.

## Hierarchical interfaces

Interfaces can be organized hierarchically to support aggregate metrics at different
levels of your operation:

1. **Equipment-level interface** (for example,
   `PUMP-INTERFACE`)
   - Properties: Flow rate, pressure, power consumption, vibration
   - Metrics: Efficiency, health score

2. **Process-level interface** (for example,
   `PUMPING-STATION-INTERFACE`)
   - Properties: Total flow, average pressure, total power
   - Metrics: Station efficiency, operational cost per volume
   - Hierarchy: Contains `PUMP-INTERFACE` equipment

3. **Facility-level interface** (for example,
   `WATER-FACILITY-INTERFACE`)
   - Properties: Facility throughput, energy usage, chemical usage
   - Metrics: Facility efficiency, cost per unit volume, carbon footprint
   - Hierarchy: Contains `PUMPING-STATION-INTERFACE` processes

This hierarchical approach allows metrics to be calculated at each level while
maintaining consistency across your entire operation.
