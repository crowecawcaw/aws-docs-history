# Starting workflows in Amazon SWF

You can start a workflow execution of a registered workflow type from any application using
the `StartWorkflowExecution` action. When you start the execution you
associate an identifier, called the `workflowId`, with it. The
`workflowId` can be any string that is appropriate for your application, such as
the order number in an order processing application. You can't use the same
`workflowId` for multiple open workflow executions within the same domain. For
example, if you start two workflow executions with the `workflowId`
`Customer Order 01`, the second workflow execution will not start and the request
will fail. You can, however, reuse the `workflowId` of a closed execution. Amazon SWF also
associates a unique system generated identifier, called the `runId`, with each
workflow execution.

After the workflow and activity types are registered, start the workflow by calling the
`StartWorkflowExecution` action. The value of the `input`
parameter can be any string specified by the application that is starting the workflow. The
`executionStartToCloseTimeout` is the length of time in seconds that the workflow
execution can consume from start to close. Exceeding this limit causes the workflow execution to
time out. Unlike some of the other timeout parameters in Amazon SWF, you can't specify a value of
`NONE` for this timeout; there is a one-year maximum limit on the time that a
workflow execution can run. Similarly, the _taskStartToCloseTimeout_ is the
length of time in seconds that a decision task associated with this workflow execution can take
before timing out.

```
https://swf.us-east-1.amazonaws.com
StartWorkflowExecution
{
  "domain" : "867530901",
  "workflowId" : "20110927-T-1",
  "workflowType" : {
    "name" : "customerOrderWorkflow", "version" : "1.1"
  },
  "taskList" : { "name" : "specialTaskList" },
  "input" : "arbitrary-string-that-is-meaningful-to-the-workflow",
  "executionStartToCloseTimeout" : "1800",
  "tagList" : [ "music purchase", "digital", "ricoh-the-dog" ],
  "taskStartToCloseTimeout" : "1800",
  "childPolicy" : "TERMINATE"
}
```

If the `StartWorkflowExecution` action is successful, Amazon SWF returns
the `runId` for the workflow execution. The `runId` for a workflow
execution is unique within a specific region. Save the `runId` in case you later need
to specify this workflow execution in a call to Amazon SWF. For example, you would use the
`runId` if you later needed to send a signal to the workflow execution.

```
{"runId": "9ba33198-4b18-4792-9c15-7181fb3a8852"}
```
