

# Understanding results and output
<a name="batch-evaluations-results"></a>

Batch evaluation results come in two layers: aggregate summaries in the API response, and per-session detail in CloudWatch Logs.

## Aggregate results
<a name="batch-eval-aggregate-results"></a>

When a batch evaluation completes, the `GetBatchEvaluation` response includes an `evaluationResults` object with aggregate summaries.

### Session counts
<a name="batch-eval-session-counts"></a>


| Field | Description | 
| --- | --- | 
|  `numberOfSessionsCompleted`  | Number of sessions successfully evaluated by all evaluators. | 
|  `numberOfSessionsFailed`  | Number of sessions where at least one evaluator failed. | 
|  `numberOfSessionsInProgress`  | Number of sessions still being evaluated (0 when the job is complete). | 
|  `totalNumberOfSessions`  | Total number of sessions discovered from the session source. | 
|  `numberOfSessionsIgnored`  | Number of sessions ignored for evaluation. The service evaluates up to 500 sessions per job. If more than 500 sessions are discovered, the service selects the 500 most recent sessions and ignores the rest. | 

### Per-evaluator summaries
<a name="batch-eval-evaluator-summaries"></a>

Each entry in `evaluatorSummaries` provides aggregate metrics for one evaluator, or for one dimension of a multi-dimension evaluator:


| Field | Description | 
| --- | --- | 
|  `evaluatorId`  | Short ID (for example, `Builtin.GoalSuccessRate`). | 
|  `evaluationDimensionName`  | For a [multi-dimension evaluator](multi-dimension-evaluators.md), the dimension this entry covers. Absent for single-scale evaluators. | 
|  `statistics.averageScore`  | Mean score across all evaluated sessions. Range depends on the evaluator (typically 0–1). Absent for categorical evaluators and categorical dimensions. | 
|  `totalEvaluated`  | Number of sessions this evaluator successfully scored. | 
|  `totalFailed`  | Number of sessions where this evaluator returned an error. | 

A multi-dimension evaluator has one entry per dimension. A separate entry for the evaluator, without `evaluationDimensionName`, counts the sessions that fail before the judge model runs.

### Example response
<a name="batch-eval-example-response"></a>

```
{
    "batchEvaluationId": "acme_baseline-a1b2c3d4e5",
    "status": "COMPLETED",
    "evaluationResults": {
        "numberOfSessionsCompleted": 47,
        "numberOfSessionsFailed": 3,
        "numberOfSessionsIgnored": 0,
        "totalNumberOfSessions": 50,
        "evaluatorSummaries": [
            {
                "evaluatorId": "Builtin.GoalSuccessRate",
                "statistics": {
                    "averageScore": 0.72
                },
                "totalEvaluated": 47,
                "totalFailed": 0
            },
            {
                "evaluatorId": "Builtin.Helpfulness",
                "statistics": {
                    "averageScore": 0.81
                },
                "totalEvaluated": 47,
                "totalFailed": 0
            }
        ]
    }
}
```

## Per-session detail in CloudWatch Logs
<a name="batch-eval-per-session-detail"></a>

The `outputConfig` field in the `GetBatchEvaluation` response specifies a CloudWatch Logs location where per-session, per-evaluator results are written as OpenTelemetry events.

```
{
    "outputConfig": {
        "cloudWatchConfig": {
            "logGroupName": "/aws/bedrock-agentcore/evaluations/batch",
            "logStreamName": "acme_baseline-a1b2c3d4e5"
        }
    }
}
```

**Note**  
The `logGroupName` returned here reflects the destination you chose for the job. For the available `outputConfig` options, see [Start batch evaluation](batch-evaluations-start.md).

Each event in the log stream contains per-turn, per-evaluator detail:


| Field | Description | 
| --- | --- | 
|  `gen_ai.evaluation.score.value`  | Numeric score for this turn. | 
|  `gen_ai.evaluation.score.label`  | Categorical label (for example, `PASS`, `Very Helpful`). | 
|  `gen_ai.evaluation.explanation`  | LLM-generated reasoning for the score. | 

To read these events with the AWS SDK, use the CloudWatch Logs API. `agentcore eval batch-evaluation get` reads them for you, as described in [Viewing results from the CLI](#batch-eval-viewing-from-cli).

```
import boto3

logs_client = boto3.client("logs", region_name="us-west-2")

response = logs_client.get_log_events(
    logGroupName="/aws/bedrock-agentcore/evaluations/batch",
    logStreamName="acme_baseline-a1b2c3d4e5",
)

for event in response["events"]:
    print(event["message"])
```

## Interpreting scores
<a name="batch-eval-interpreting-scores"></a>

Batch evaluation scores follow the same conventions as on-demand evaluation:
+  **Numeric scores** (`value`): Range depends on the evaluator. Most built-in evaluators score from 0 to 1, where higher is better.
+  **Labels** (`label`): Categorical descriptions of the score. For example, `Builtin.Helpfulness` returns labels like `Very Helpful`, `Somewhat Helpful`, `Not Helpful`.

## Error handling
<a name="batch-eval-error-handling"></a>

### Job-level errors
<a name="batch-eval-job-errors"></a>

If the batch evaluation job fails entirely, the `status` is `FAILED` and `errorDetails` contains one or more error messages describing what went wrong. Common causes:
+ No sessions found in the specified source.
+ Invalid CloudWatch log group or service name.

### Session-level errors
<a name="batch-eval-session-errors"></a>

Individual sessions can fail while the overall job succeeds. The `numberOfSessionsFailed` count in `evaluationResults` indicates how many sessions had errors. Per-session errors are recorded in the CloudWatch Logs output.

### Evaluator-level errors
<a name="batch-eval-evaluator-errors"></a>

Within a successfully evaluated session, individual evaluators can fail. The `totalFailed` count on each evaluator summary indicates how many sessions that evaluator could not score. Common causes include malformed spans or missing required attributes.

## Comparing results across runs
<a name="batch-eval-comparing-runs"></a>

A common workflow is to run batch evaluation before and after a change (prompt update, model swap, tool modification) and compare the aggregate scores:

```
# After running two batch evaluations
baseline = client.get_batch_evaluation(batchEvaluationId=baseline_id)
treatment = client.get_batch_evaluation(batchEvaluationId=treatment_id)

def average_scores(job):
    # Key on the dimension too: a multi-dimension evaluator has one summary per dimension.
    return {
        (s["evaluatorId"], s.get("evaluationDimensionName")): s["statistics"]["averageScore"]
        for s in job["evaluationResults"]["evaluatorSummaries"]
        if "averageScore" in s.get("statistics", {})
    }

baseline_summaries = average_scores(baseline)
treatment_summaries = average_scores(treatment)

print(f"{'Evaluator':<45} {'Baseline':>10} {'Treatment':>10} {'Delta':>10}")
print("=" * 77)
for (eid, dim), b in baseline_summaries.items():
    t = treatment_summaries.get((eid, dim), 0)
    name = f"{eid}/{dim}" if dim else eid
    print(f"{name:<45} {b:>10.4f} {t:>10.4f} {t - b:>+10.4f}")
```

## Viewing results from the CLI
<a name="batch-eval-viewing-from-cli"></a>

The AgentCore CLI provides the following commands:
+  `agentcore eval batch-evaluation get --id <batch-evaluation-id>`: Returns the `GetBatchEvaluation` response. For a finished job, the command also reads the result log stream and adds a `results` array with one entry per score. Each entry has fields such as `evaluatorId`, `level`, `sessionId`, `traceId`, `score`, `label`, `explanation`, and `error`. Pass `--disable-cw-results` to skip the CloudWatch read and return only the job metadata.
+  `agentcore eval batch-evaluation list`: Lists batch evaluation jobs.
+  `agentcore eval batch-evaluation evaluate`: Starts a job and prints its metadata as JSON.

```
# View a single batch evaluation job and its results
agentcore eval batch-evaluation get \
  --id acme_baseline-a1b2c3d4e5 \
  --json

# List batch evaluation jobs
agentcore eval batch-evaluation list --json
```