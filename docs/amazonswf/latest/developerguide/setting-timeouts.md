

# Setting timeout values in Amazon SWF
<a name="setting-timeouts"></a>

**Topics**
+ [Quotas on Timeout Values](#setting-timeouts-limits)
+ [Workflow Execution and Decision Task Timeouts](#setting-timeouts-execution)
+ [Activity Task Timeouts](#setting-timeouts-activity)
+ [See Also](#timeout-types-see-also)

## Quotas on Timeout Values
<a name="setting-timeouts-limits"></a>

Timeout values are always declared in seconds, and can be set to any number of seconds up to a year (31536000 seconds)—the maximum execution limit for any workflow or activity. The special value `NONE` is used to set a timeout parameter to "no timeout", or infinite, but the maximum limit of a year still applies.

## Workflow Execution and Decision Task Timeouts
<a name="setting-timeouts-execution"></a>

You can set timeout values for your Workflow and Decision tasks when registering the workflow type. For example:

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

This workflow type registration sets the `[defaultTaskStartToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultTaskStartToCloseTimeout)` to 600 seconds (10 minutes), and `[defaultExecutionStartToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html#SWF-RegisterWorkflowType-request-defaultExecutionStartToCloseTimeout)` to 3600 seconds (1 hour).

For more information about workflow type registration, see [Registering a Workflow Type with Amazon SWF](swf-dg-register-workflow.md), and `[RegisterWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html)` in the *Amazon Simple Workflow Service API Reference*.

You can override the value set for `defaultExecutionStartToCloseTimeout` by specifying `[executionStartToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-executionStartToCloseTimeout) `i.

## Activity Task Timeouts
<a name="setting-timeouts-activity"></a>

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

This activity type registration sets the `[defaultTaskStartToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskStartToCloseTimeout)` to 600 seconds (10 minutes), the `[defaultTaskHeartbeatTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskHeartbeatTimeout)` to 120 seconds (2 minutes), the `[defaultTaskScheduleToStartTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskScheduleToStartTimeout)` to 1800 seconds (30 minutes) and `[defaultTaskScheduleToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html#SWF-RegisterActivityType-request-defaultTaskScheduleToCloseTimeout)` to 5400 seconds (1.5 hours). 

For more information about activity type registration, see [Registering an Activity Type with Amazon SWF](swf-dg-register-activity.md), and `[RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html)` in the *Amazon Simple Workflow Service API Reference*. 

You can override the value set for `defaultTaskStartToCloseTimeout` by specifying `[taskStartToCloseTimeout](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html#SWF-StartWorkflowExecution-request-taskStartToCloseTimeout)` when scheduling the activity task.

## See Also
<a name="timeout-types-see-also"></a>

[Amazon SWF Timeout Types](swf-timeout-types.md)