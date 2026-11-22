

# Deleting durable executions

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

If you log Lambda data events in AWS CloudTrail, CloudTrail records each [DeleteDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteDurableExecution.html) call. Use these records to audit deletions. For more information, see [Audit execution deletions](#durable-cloudtrail-audit-deletions).

## Delete an execution
<a name="durable-delete-execution"></a>

To delete a running or paused execution, stop it first with [StopDurableExecution](https://docs.aws.amazon.com/lambda/latest/api/API_StopDurableExecution.html). For more information, see [Stopping an execution](durable-managing-executions.md#durable-managing-executions-stop) and [Pausing and resuming durable executions](durable-pause-resume.md).

**To delete an execution**

1. Run the following AWS CLI command:

   ```bash
   aws lambda delete-durable-execution \
     --durable-execution-arn {{arn:aws:lambda:us-east-1:111122223333:function:my-durable-function:my-function-version/durable-execution/my-execution-name/my-execution-id}}
   ```

   Replace the value of `--durable-execution-arn` with the ARN of the execution to delete.

   The response includes the time at which Lambda accepted the deletion request:

   ```json
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

## Audit execution deletions
<a name="durable-cloudtrail-audit-deletions"></a>

To find out who deleted an execution, turn on data event logging before the deletion happens. CloudTrail doesn't record calls made while logging is off.

To log only deletions, and not every invoke and checkpoint, use an advanced event selector that filters on the event name. The following AWS CLI command logs only `DeleteDurableExecution` calls. Replace {{my-trail}} with the name of your trail.

```bash
aws cloudtrail put-event-selectors \
   --trail-name {{my-trail}} \
   --advanced-event-selectors '[{
     "Name": "Log durable execution deletions",
     "FieldSelectors": [
       { "Field": "eventCategory", "Equals": ["Data"] },
       { "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },
       { "Field": "eventName", "Equals": ["DeleteDurableExecution"] }
     ]
   }]'
```

The selector has the following fields:
+ `eventCategory` – `Data` selects data events. Lambda logs durable execution operations as data events.
+ `resources.type` – `AWS::Lambda::Function`. CloudTrail lists the function that owns the execution as the resource.
+ `eventName` – The operations to log.

For more information about advanced event selectors, see [Log data events for trails by using advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced) in the CloudTrail User Guide.

The following example shows a CloudTrail log entry for a `DeleteDurableExecution` call. `userIdentity` shows who made the call, and `requestParameters` contains the ARN of the deleted execution.

```json
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "A1B2C3D4E5F6G7EXAMPLE:mySessionName",
    "arn": "arn:aws:sts::111122223333:assumed-role/MyRole/mySessionName",
    "accountId": "111122223333"
  },
  "eventTime": "2026-11-18T17:41:16Z",
  "eventSource": "lambda.amazonaws.com",
  "eventName": "DeleteDurableExecution",
  "awsRegion": "{{us-east-1}}",
  "sourceIPAddress": "192.0.2.1",
  "requestParameters": {
    "durableExecutionArn": "arn:aws:lambda:{{us-east-1}}:111122223333:function:my-function:$LATEST/durable-execution/my-execution/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  },
  "responseElements": {
    "deletionRequestTimestamp": 1795023676.71
  },
  "additionalEventData": {
    "functionVersion": "arn:aws:lambda:{{us-east-1}}:111122223333:function:my-function:$LATEST"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
  "readOnly": false,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::Lambda::Function",
      "ARN": "arn:aws:lambda:{{us-east-1}}:111122223333:function:my-function"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data"
}
```

To get notified when someone deletes an execution, create an Amazon EventBridge rule on the default event bus. When your trail logs `DeleteDurableExecution` data events, CloudTrail also sends each logged `DeleteDurableExecution` call to EventBridge as an `AWS API Call via CloudTrail` event. Without that trail, EventBridge receives no event for a deletion. The following event pattern matches these calls. For how to create the rule and send matched events to a target such as an Amazon SNS topic, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the EventBridge User Guide.

```json
{
  "source": ["aws.lambda"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventName": ["DeleteDurableExecution"]
  }
}
```