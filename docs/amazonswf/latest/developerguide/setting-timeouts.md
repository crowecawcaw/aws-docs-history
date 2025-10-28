# Setting timeout values in Amazon SWF

###### Topics

- [Quotas on Timeout Values](#setting-timeouts-limits "#setting-timeouts-limits")
- [Workflow Execution and Decision Task Timeouts](#setting-timeouts-execution "#setting-timeouts-execution")
- [Activity Task Timeouts](#setting-timeouts-activity "#setting-timeouts-activity")
- [See Also](#timeout-types-see-also "#timeout-types-see-also")

## Quotas on Timeout Values

Timeout values are always declared in seconds, and can be set to any number of seconds up to a year
(31536000 seconds)—the maximum execution limit for any workflow or activity. The special value `NONE` is
used to set a timeout parameter to "no timeout", or infinite, but the maximum limit of a year still
applies.

## Workflow Execution and Decision Task Timeouts

You can set timeout values for your Workflow and Decision tasks when registering the workflow type. For
example:

```
https://swf.us-east-1.amazonaws.com
RegisterWorkflowType
{
  "domain": "867530901",
  "name": "customerOrderWorkflow",
  "version": "1.0",
  "description": "Handle customer orders",
  "defaultTaskStartToCloseTimeout": "600",
  "defaultExecutionStartToCloseTimeout": "3600",
  "defaultTaskList": { "name": "mainTaskList" },
  "defaultChildPolicy": "TERMINATE"
}
```

This workflow type registration sets the `defaultTaskStartToCloseTimeout` to 600 seconds (10 minutes), and
`defaultExecutionStartToCloseTimeout` to 3600 seconds (1 hour).

For more information about workflow type registration, see [Registering a Workflow Type with Amazon SWF](swf-dg-register-workflow.md "swf-dg-register-workflow.md"), and
`RegisterWorkflowType` in the
_Amazon Simple Workflow Service API Reference_.

You can override the value set for `defaultExecutionStartToCloseTimeout` by
specifying `executionStartToCloseTimeout`i.

## Activity Task Timeouts

You can set timeout values for your activity tasks when registering the activity type. For example:

```
https://swf.us-east-1.amazonaws.com
RegisterActivityType
{
  "domain": "867530901",
  "name": "activityVerify",
  "version": "1.0",
  "description": "Verify the customer credit",
  "defaultTaskStartToCloseTimeout": "600",
  "defaultTaskHeartbeatTimeout": "120",
  "defaultTaskList": { "name": "mainTaskList" },
  "defaultTaskScheduleToStartTimeout": "1800",
  "defaultTaskScheduleToCloseTimeout": "5400"
}
```

This activity type registration sets the `defaultTaskStartToCloseTimeout` to 600 seconds (10 minutes), the
`defaultTaskHeartbeatTimeout` to 120 seconds (2 minutes), the
`defaultTaskScheduleToStartTimeout` to 1800 seconds (30 minutes) and
`defaultTaskScheduleToCloseTimeout` to 5400 seconds (1.5 hours).

For more information about activity type registration, see [Registering an Activity Type with Amazon SWF](swf-dg-register-activity.md "swf-dg-register-activity.md"), and
`RegisterActivityType` in the _Amazon Simple Workflow Service API Reference_.

You can override the value set for `defaultTaskStartToCloseTimeout` by
specifying `taskStartToCloseTimeout` when scheduling the activity task.

## See Also

[Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md")
