# Canonical Message Format

Every normalized message uses the same schema regardless of source:

```
{
  "vehicleId": "VEH-001",
  "fleetId": "FLEET-001",
  "timestamp": 1710764400000,
  "source": "simulator | fleetwise | oem",
  "speed": 65.2,
  "odometer": 45230.1,
  "lat": 47.6062,
  "lng": -122.3321,
  "heading": 180.5,
  "ignitionOn": true,
  "engineRPM": 2100,
  "fuelLevel": 72.3,
  "tire_fl": 35.2,
  "tire_fr": 34.8
}
```

Field names are `json_field` values from the signal catalog. Units are canonical: mph, miles, °F, PSI. Not all fields are present in every message — availability depends on the vehicle’s telemetry source.
