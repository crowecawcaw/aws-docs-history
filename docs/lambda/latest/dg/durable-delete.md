

# Deleting durable executions
<a name="durable-delete"></a>

You can delete a durable execution after it reaches a terminal state: `SUCCEEDED`, `FAILED`, `STOPPED`, or `TIMED_OUT`. When you delete an execution, Lambda removes all of its data, including its history, checkpoint data, and input and output payloads.

Lambda deletes execution data automatically when the [retention period](durable-basic-concepts.md#durable-retention-period) ends. You can delete an execution to remove its data sooner, for example to meet your compliance requirements.

Deleting an execution doesn't remove data that Lambda or your function stored elsewhere. The following data stays until you delete it or it expires under its own retention settings:
+ Your function's logs in Amazon CloudWatch Logs.
+ AWS CloudTrail records of calls to the execution, which you keep as an audit trail.
+ CloudWatch metrics.
+ Data that your function wrote to other services.
+ Child executions that the execution started through chained invokes.

**Important**  
Deletion is permanent. After Lambda deletes an execution, you can't retrieve its details, history, or result.

**Note**  
Deleting an execution doesn't reduce its storage charges. Lambda charges for an execution's retained data for its full retention period, even if you delete the execution before that period ends. To reduce storage charges, set a shorter retention period. The new retention period applies to executions that start after you change it. For more information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

## Prerequisites
<a name="durable-delete-prerequisites"></a>

To delete an execution, you need the `lambda:DeleteDurableExecution` permission on the durable execution ARN. Grant this permission only to principals that are allowed to permanently remove execution data. For more information, see [Permissions for managing durable executions](durable-security.md#durable-manage-permissions).

If your durable function uses an AWS Key Management Service (AWS KMS) customer managed key, deleting an execution doesn't require permissions on the key. For more information, see [Encrypting AWS Lambda durable execution data](durable-encryption.md).

If you log Lambda data events in AWS CloudTrail, CloudTrail records each [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) call. Use these records to audit deletions. For more information, see [CloudTrail logging](durable-security.md#durable-cloudtrail-logging).

## Delete an execution
<a name="durable-delete-execution"></a>

To delete a running or paused execution, stop it first with [StopDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_StopDurableExecution.html). For more information, see [Stopping an execution](durable-managing-executions.md#durable-managing-executions-stop).

**To delete an execution**

1. Run the following AWS CLI command:

   ```
   aws lambda delete-durable-execution \
     --durable-execution-arn {{arn:aws:lambda:us-east-1:111122223333:function:my-durable-function:my-function-version/durable-execution/my-execution-name/my-execution-id}}
   ```

   Replace the value of `--durable-execution-arn` with the ARN of the execution to delete.

   The response includes the time at which Lambda accepted the deletion request:

   ```
   {
       "DeletionRequestTimestamp": "2026-06-14T10:20:00Z"
   }
   ```

1. To confirm that the deletion finished, call [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) with the same ARN. After Lambda deletes the execution, the call returns a `ResourceNotFoundException`.

After Lambda deletes an execution, you can use the same execution name again. An invocation with that name starts a new execution, which has the same execution ARN.

### Deleting an execution that just finished
<a name="durable-delete-recently-finished"></a>

Execution status is eventually consistent. [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) can return a `ResourceConflictException` for an execution that recently reached a terminal state. Try the request again later.

### Delete multiple executions
<a name="durable-delete-multiple"></a>

[DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) deletes one execution. To delete many executions, for example every execution that started before a date, list them with [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) and call [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) for each one.

## What happens during deletion
<a name="durable-delete-how-it-works"></a>

Lambda deletes an execution asynchronously:
+ The execution status changes to `DELETING`. [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html) and [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) report this status until the deletion finishes. To find executions that are being deleted, call [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) with a status filter of `DELETING`.
+ Calling [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) again while the execution is `DELETING` succeeds and doesn't start a second deletion.
+ When the deletion finishes, [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecution.html), [GetDurableExecutionHistory](https://docs.aws.amazon.com/lambda/latest/api/API_GetDurableExecutionHistory.html), and [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) return a `ResourceNotFoundException` for the execution ARN, and the execution no longer appears in [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html) results.
+ Deleting a parent execution doesn't delete its child executions. Delete each child separately, or let it expire at the end of its retention period.
+ Lambda doesn't publish an EventBridge status change event for a deletion. To audit deletions, use CloudTrail data events, as described in [Prerequisites](#durable-delete-prerequisites).