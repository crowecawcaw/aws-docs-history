# Delete batch evaluation

Delete a batch evaluation job and its associated metadata. The job must be in a terminal state (`COMPLETED`, `FAILED`, or `STOPPED`) before it can be deleted.

Deleting a batch evaluation removes the job record from `ListBatchEvaluations`. It does not delete per-session evaluation results that were written to CloudWatch Logs.

## Code samples

###### Example

AWS SDK (boto3)

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.delete_batch_evaluation(batchEvaluationId=batch_eval_id)
print(f"Deleted: {response['batchEvaluationId']}")
print(f"Status: {response['status']}")
```

## Request parameters

| Parameter           | Type   | Required | Description                                                    |
| ------------------- | ------ | -------- | -------------------------------------------------------------- |
| `batchEvaluationId` | String | Yes      | The batch evaluation ID to delete. Passed as a path parameter. |

## Response

| Field                | Type   | Description                      |
| -------------------- | ------ | -------------------------------- |
| `batchEvaluationId`  | String | The batch evaluation ID.         |
| `batchEvaluationArn` | String | ARN of the batch evaluation.     |
| `status`             | String | Final status of the deleted job. |

## Errors

| Error                       | HTTP status | Description                                                        |
| --------------------------- | ----------- | ------------------------------------------------------------------ |
| `ResourceNotFoundException` | 404         | No batch evaluation found with the specified ID.                   |
| `ConflictException`         | 409         | The batch evaluation is still running. Stop it first, then delete. |
| `ValidationException`       | 400         | Invalid batch evaluation ID format.                                |
| `AccessDeniedException`     | 403         | Insufficient permissions.                                          |
| `ThrottlingException`       | 429         | Request rate exceeded.                                             |
| `InternalServerException`   | 500         | Service-side error.                                                |
