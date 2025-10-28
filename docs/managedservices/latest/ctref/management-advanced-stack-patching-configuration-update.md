# Stack Patching Configuration | Update

Use to update patch configuration.

**Full classification:** Management | Advanced stack components | Stack patching configuration | Update

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Change type ID              | ct-34alumbtv2b9p |
| Current version             | 1.0              |
| Expected execution duration | 15 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        | ## Additional Information ###### Important This change type has been deprecated and cannot be used. ## Execution Input Parameters For detailed information about the execution input parameters, see [Schema for Change Type ct-34alumbtv2b9p](schemas.md#ct-34alumbtv2b9p-schema-section "schemas.md#ct-34alumbtv2b9p-schema-section"). ## Example: Required Parameters `{ "StackId": "stack-12345678901234567" }` ## Example: All Parameters `{ "StackId": "stack-12345678901234567", "MaintenanceWindow": { "DayOfWeek": 4, "DurationInMinutes": 240, "Hour": 18, "Minute": 0, "WeekOfMonth": 2 }, "HealthyHostThreshold": 0.8 }` |
