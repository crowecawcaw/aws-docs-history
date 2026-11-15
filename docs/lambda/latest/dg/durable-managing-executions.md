

# Managing durable executions
<a name="durable-managing-executions"></a>

After a durable execution starts, you can change what happens to it without changing your function code. Each operation acts on one execution, identified by its execution ARN. New invocations of your function and other executions aren't affected.
+ **Stop** – End an execution permanently. Stopping an execution doesn't undo work that completed steps already did. For more information, see [Stopping an execution](#durable-managing-executions-stop).
+ **Delete** – Permanently remove a finished execution and its data. For more information, see [Deleting durable executions](durable-delete.md).

To find the executions to act on, use [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html). You can filter the list by status and by start time.

## Stopping an execution
<a name="durable-managing-executions-stop"></a>

To end a running execution permanently, call [StopDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_StopDurableExecution.html). The execution status changes to `STOPPED`, and Lambda doesn't invoke your function for that execution again. You can't resume a stopped execution.

```
aws lambda stop-durable-execution \
  --durable-execution-arn {{arn:aws:lambda:us-east-1:123456789012:function:myDurableFunction:my-function-version/durable-execution/my-execution-name/my-execution-id}}
```