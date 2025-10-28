# Registering an Activity Type with Amazon SWF

The following example registers an activity type by using the Amazon SWF API. The name and version that you specify
during registration form a unique identifier for the activity type within the domain. The specified domain must have
already been registered using the `RegisterDomain` action.

The timeout parameters in this example are duration values specified in seconds. You can
use the duration specifier `NONE` to indicate no timeout.

```
https://swf.us-east-1.amazonaws.com
RegisterActivityType
{
  "domain" : "867530901",
  "name" : "activityVerify",
  "version" : "1.0",
  "description" : "Verify the customer credit",
  "defaultTaskStartToCloseTimeout" : "600",
  "defaultTaskHeartbeatTimeout" : "120",
  "defaultTaskList" : { "name" : "mainTaskList" },
  "defaultTaskScheduleToStartTimeout" : "1800",
  "defaultTaskScheduleToCloseTimeout" : "5400"
}
```

## See Also

[RegisterActivityType](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md")
in the _Amazon Simple Workflow Service API Reference_
