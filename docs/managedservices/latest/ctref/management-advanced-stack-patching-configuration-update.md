

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Stack Patching Configuration \| Update
<a name="management-advanced-stack-patching-configuration-update"></a>

Use to update patch configuration.

**Full classification:** Management \| Advanced stack components \| Stack patching configuration \| Update

## Change Type Details
<a name="ct-34alumbtv2b9p-MASu-table"></a>



|  |  | 
| --- |--- |
| Change type ID | ct-34alumbtv2b9p | 
| Current version | 1.0 | 
| Expected execution duration | 15 minutes | 
| AWS approval | Required | 
| Customer approval | Not required | 
| Execution mode | Automated | 

## Additional Information
<a name="management-advanced-stack-patching-configuration-update-info"></a>

**Important**  
This change type has been deprecated and cannot be used.

## Execution Input Parameters
<a name="management-advanced-stack-patching-configuration-update-input"></a>

For detailed information about the execution input parameters, see [Schema for Change Type ct-34alumbtv2b9p](schemas.md#ct-34alumbtv2b9p-schema-section).

## Example: Required Parameters
<a name="management-advanced-stack-patching-configuration-update-ex-min"></a>

```
{
  "StackId": "stack-12345678901234567"
}
```

## Example: All Parameters
<a name="management-advanced-stack-patching-configuration-update-ex-max"></a>

```
{
  "StackId": "stack-12345678901234567",
  "MaintenanceWindow": {
    "DayOfWeek": 4,
    "DurationInMinutes": 240,
    "Hour": 18,
    "Minute": 0,
    "WeekOfMonth": 2
  },
  "HealthyHostThreshold": 0.8
}
```