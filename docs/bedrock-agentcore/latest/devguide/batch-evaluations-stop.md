

# Stop batch evaluation
<a name="batch-evaluations-stop"></a>

Stop a running batch evaluation job. The job transitions to `STOPPING` and then `STOPPED`. Partial results from sessions that were already evaluated may be available in the response.

Stopping a batch evaluation is useful when you realize the job was started with incorrect parameters, or when you no longer need the results.

## Code samples
<a name="stop-batch-eval-examples"></a>

**Example**  

```
agentcore stop batch-evaluation --id <batch-evaluation-id> [--region <region>] [--json]
```
You can use `-i` as the short alias for `--id`. The `--region` flag specifies the AWS Region (auto-detected if omitted), and `--json` outputs the response as JSON.

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.stop_batch_evaluation(batchEvaluationId=batch_eval_id)
print(f"Status: {response['status']}")  # STOPPING or STOPPED
```

## Request parameters
<a name="stop-batch-eval-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `batchEvaluationId`  | String | Yes | The batch evaluation ID to stop. Passed as a path parameter. | 

## Response
<a name="stop-batch-eval-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `batchEvaluationId`  | String | The batch evaluation ID. | 
|  `batchEvaluationArn`  | String | ARN of the batch evaluation. | 
|  `status`  | String | Updated status: `STOPPING` or `STOPPED`. | 

## Errors
<a name="stop-batch-eval-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ResourceNotFoundException`  | 404 | No batch evaluation found with the specified ID. | 
|  `ConflictException`  | 409 | The batch evaluation is not in a state that can be stopped (for example, already completed or stopped). | 
|  `ValidationException`  | 400 | Invalid batch evaluation ID format. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. | 
|  `InternalServerException`  | 500 | Service-side error. | 