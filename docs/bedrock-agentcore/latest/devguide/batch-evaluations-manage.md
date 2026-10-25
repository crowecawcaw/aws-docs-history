

# Manage batch evaluations
<a name="batch-evaluations-manage"></a>

After you start a batch evaluation, you can check its status and results, list your batch evaluations, stop a running job, and delete a job that you no longer need.

## Get status and results
<a name="batch-evaluations-get"></a>

Poll the batch evaluation until it reaches a terminal state, then read the results. For the fields in the response, see [Understanding results and output](batch-evaluations-results.md). For the API, see [GetBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBatchEvaluation.html) in the * AWS API Reference*.

The status of a batch evaluation is one of the following:
+  `PENDING`: The job is accepted and queued.
+  `IN_PROGRESS`: The service is discovering sessions and running the evaluators.
+  `COMPLETED`: All sessions are evaluated.
+  `COMPLETED_WITH_ERRORS`: The job finished, but some sessions had errors. Partial results are available.
+  `FAILED`: The job failed. The `errorDetails` field in the response describes the error.
+  `STOPPING` and `STOPPED`: The job is stopping, or it stopped before completion. Partial results might be available.
+  `DELETING`: The job is being deleted.

Terminal states are `COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, and `STOPPED`.

**Example**  
The following AgentCore CLI command starts a job and waits for it to reach a terminal state:  

```
agentcore run batch-evaluation -r MyAgent -e Builtin.Correctness --wait
```
Without `--wait`, the command starts the job and returns immediately. To check a job later, run the following command. Replace `<batch-evaluation-id>` with the ID that the previous command prints:  

```
agentcore view batch-evaluation <batch-evaluation-id>
```
Add `--json` for machine-readable output.
The following Python code polls a batch evaluation until it reaches a terminal state and then prints the results. Replace `batch_eval_id` with your batch evaluation ID.  

```
import time
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
batch_eval_id = "my-batch-evaluation-1a2b3c4d5e"

# Poll until the job reaches a terminal state.
while True:
    result = client.get_batch_evaluation(batchEvaluationId=batch_eval_id)
    status = result["status"]
    print(f"Status: {status}")

    if status in ("COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPED"):
        break
    time.sleep(30)

# Display the results.
if result.get("evaluationResults"):
    er = result["evaluationResults"]
    print(f"Sessions completed: {er.get('numberOfSessionsCompleted', 0)}")
    print(f"Sessions failed:    {er.get('numberOfSessionsFailed', 0)}")
    print(f"Total sessions:     {er.get('totalNumberOfSessions', 0)}")

    for summary in er.get("evaluatorSummaries", []):
        avg = summary.get("statistics", {}).get("averageScore")
        print(f"  {summary['evaluatorId']}: {avg}")
```

## List batch evaluations
<a name="batch-evaluations-list"></a>

List the batch evaluations in your account. The results are paginated. For the API, see [ListBatchEvaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBatchEvaluations.html) in the * AWS API Reference*.

**Example**  
The following AgentCore CLI command lists your batch evaluations. The CLI refreshes running jobs from the service.  

```
agentcore batch-evaluations history --json
```
The following Python code lists all of your batch evaluations. It uses the `nextToken` value from each response to retrieve the next page.  

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

evaluations = []
params = {"maxResults": 50}

while True:
    response = client.list_batch_evaluations(**params)
    evaluations.extend(response["batchEvaluations"])

    if not response.get("nextToken"):
        break
    params["nextToken"] = response["nextToken"]

for evaluation in evaluations:
    print(
        f"{evaluation['batchEvaluationId']}  "
        f"{evaluation['batchEvaluationName']}  "
        f"{evaluation['status']}  "
        f"{evaluation['createdAt']}"
    )
```

## Stop a batch evaluation
<a name="batch-evaluations-stop"></a>

Stop a running batch evaluation. The job moves to `STOPPING` and then `STOPPED`. The response might include partial results from the sessions that the service already evaluated. Stopping is useful when you started a job with incorrect parameters or no longer need the results.

If the job is not in a state that can be stopped, such as a job that already completed, the service returns a `ConflictException`. For the API, see [StopBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBatchEvaluation.html) in the * AWS API Reference*.

**Example**  
The following AgentCore CLI command stops a batch evaluation. Replace `<batch-evaluation-id>` with your batch evaluation ID.  

```
agentcore stop batch-evaluation -i <batch-evaluation-id>
```
The following Python code stops a batch evaluation. Replace `batch_eval_id` with your batch evaluation ID.  

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
batch_eval_id = "my-batch-evaluation-1a2b3c4d5e"

response = client.stop_batch_evaluation(batchEvaluationId=batch_eval_id)
print(f"Status: {response['status']}")  # STOPPING or STOPPED
```

## Delete a batch evaluation
<a name="batch-evaluations-delete"></a>

Delete a batch evaluation and its metadata. The job must be in a terminal state (`COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, or `STOPPED`). To delete a running job, stop it first. Deleting a job removes it from the list of batch evaluations. The per-session results that the job wrote to your CloudWatch Logs log group remain. For the API, see [DeleteBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteBatchEvaluation.html) in the * AWS API Reference*.

**Example**  
The following AgentCore CLI command archives a batch evaluation, which deletes its record from the service and clears the local history. Replace `<batch-evaluation-id>` with your batch evaluation ID.  

```
agentcore archive batch-evaluation -i <batch-evaluation-id>
```
The following Python code deletes a batch evaluation. Replace `batch_eval_id` with your batch evaluation ID.  

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
batch_eval_id = "my-batch-evaluation-1a2b3c4d5e"

response = client.delete_batch_evaluation(batchEvaluationId=batch_eval_id)
print(f"Deleted: {response['batchEvaluationId']}")
print(f"Status: {response['status']}")
```