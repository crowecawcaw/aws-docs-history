

# Delete batch evaluation
<a name="batch-evaluations-delete"></a>

Delete a batch evaluation job and its associated metadata. The job must be in a terminal state (`COMPLETED`, `FAILED`, or `STOPPED`) before it can be deleted.

Deleting a batch evaluation removes the job record from `ListBatchEvaluations`. It does not delete per-session evaluation results that were written to CloudWatch Logs.

## Code samples
<a name="delete-batch-eval-examples"></a>

**Example**  

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.delete_batch_evaluation(batchEvaluationId=batch_eval_id)
print(f"Deleted: {response['batchEvaluationId']}")
print(f"Status: {response['status']}")
```
To delete your batch evaluation job record from the service and clear local history, use `agentcore archive batch-evaluation`.  

```
# Archive (delete) a batch evaluation job record on the service and clear local history
agentcore archive batch-evaluation -i <batch-evaluation-id>
```
For a still-running job, you must first stop it before archiving:  

```
agentcore stop batch-evaluation -i <batch-evaluation-id>
```
Both subcommands accept `-i, --id <id>`, plus `--region` and `--json`.

## Request parameters
<a name="delete-batch-eval-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `batchEvaluationId`  | String | Yes | The batch evaluation ID to delete. Passed as a path parameter. | 

## Response
<a name="delete-batch-eval-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `batchEvaluationId`  | String | The batch evaluation ID. | 
|  `batchEvaluationArn`  | String | ARN of the batch evaluation. | 
|  `status`  | String | Final status of the deleted job. | 

## Errors
<a name="delete-batch-eval-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ResourceNotFoundException`  | 404 | No batch evaluation found with the specified ID. | 
|  `ConflictException`  | 409 | The batch evaluation is still running. Stop it first, then delete. With the AgentCore CLI, stop the running job using `agentcore stop batch-evaluation -i <batch-evaluation-id>` (flag is `-i, --id`; optional `--region` and `--json`) before archiving it. | 
|  `ValidationException`  | 400 | Invalid batch evaluation ID format. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. | 
|  `InternalServerException`  | 500 | Service-side error. | 