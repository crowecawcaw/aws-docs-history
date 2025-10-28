# Registering a Workflow Type with Amazon SWF

The example discussed in this section registers a workflow type using the Amazon SWF API. The
name and version that you specify during registration form a unique identifier for the
workflow type. The specified domain must have already been registered using the `RegisterDomain` API
action.

The timeout parameters in the following example are duration values specified in seconds.
For the `defaultTaskStartToCloseTimeout` parameter, you can use the duration
specifier `NONE` to indicate no timeout. However, you can't specify a value of
`NONE` for `defaultExecutionStartToCloseTimeout`; there is a one-year
maximum limit on the time that a workflow execution can run. Exceeding this limit always
causes the workflow execution to time out. If you specify a value for
`defaultExecutionStartToCloseTimeout` that is greater than one year, the
registration will fail.

```
https://swf.us-east-1.amazonaws.com
RegisterWorkflowType
{
  "domain" : "867530901",
  "name" : "customerOrderWorkflow",
  "version" : "1.0",
  "description" : "Handle customer orders",
  "defaultTaskStartToCloseTimeout" : "600",
  "defaultExecutionStartToCloseTimeout" : "3600",
  "defaultTaskList" : { "name": "mainTaskList" },
  "defaultChildPolicy" : "TERMINATE"
}
```

## See Also

[RegisterWorkflowType](../apireference/API_RegisterWorkflowType.md "../apireference/API_RegisterWorkflowType.md") in the
_Amazon Simple Workflow Service API Reference_
