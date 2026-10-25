

# Insights in batch evaluation
<a name="batch-evaluations-insights"></a>

Some evaluators go beyond scoring and provide *insights*. When you include one of these evaluators in a batch evaluation, the service analyzes your agent sessions, groups related problems across sessions, and returns the groups in the `insightResults` field of the `GetBatchEvaluation` response. Each insight describes a pattern, the root causes behind it, and suggested fixes, so that you can see why your agent behaves as it does and what to change.

The following evaluators provide insights. For details about each evaluator, see [Insight evaluators](insight-evaluators.md).


| Evaluator | Insights it provides | 
| --- | --- | 
|  `Builtin.FailureAnalysis`  | The evaluator finds failure patterns across sessions, each with root causes, suggested fixes, and the spans where the failures occurred. See [Failure analysis evaluator](builtin-failure-analysis.md). | 

## How it works
<a name="batch-evaluations-insights-how-it-works"></a>

1.  **Start:** You start a batch evaluation with an insight-providing evaluator, alone or together with other evaluators such as `Builtin.GoalSuccessRate`.

1.  **Evaluate:** The service evaluates each session and records whether the session had failures.

1.  **Group:** The service groups the failures from all sessions into insights and determines the root causes of each insight.

1.  **Read:** You call `GetBatchEvaluation` to get the evaluator summaries and the `insightResults`, and you find the per-session results in CloudWatch Logs.

For example, a batch evaluation of about 14 sessions typically finishes in about 3 minutes. Run time grows with the number of sessions and the number of failure patterns found.

## Start a batch evaluation with insights
<a name="batch-evaluations-insights-start"></a>

Add `Builtin.FailureAnalysis` to the `evaluators` list when you call `StartBatchEvaluation`. The data source, time range, and output options work as described in [Start a batch evaluation](batch-evaluations-start.md).

**Example**  
The following AgentCore CLI command starts a batch evaluation with the failure analysis and goal success rate evaluators.  

```
agentcore eval batch-evaluation evaluate \
  --name "MyFailureAnalysis" \
  --evaluators Builtin.FailureAnalysis Builtin.GoalSuccessRate \
  --data-source-config '{
    "cloudWatchLogs": {
      "serviceNames": ["MyAgent.DEFAULT"],
      "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
      "filterConfig": {
        "timeRange": {
          "startTime": "2026-10-12T17:00:00Z",
          "endTime": "2026-10-12T17:30:00Z"
        }
      }
    }
  }' \
  --region us-west-2 --json
```
The response contains the `batchEvaluationId`. To read the sessions of a deployed agent without writing a data source configuration, pass `--agent` with the agent’s runtime ID instead of `--data-source-config`.
The AgentCore SDK evaluates the sessions that it creates. `BatchEvaluationRunner` invokes your agent once for each scenario in a dataset, then starts a batch evaluation over those sessions, so you add `Builtin.FailureAnalysis` to `evaluator_ids` rather than selecting sessions by time range. To evaluate sessions that already exist, use the AgentCore CLI or `StartBatchEvaluation` instead. For the dataset format and the `agent_invoker` contract, see [Batch dataset evaluations](dataset-evaluations-batch.md).  

```
from bedrock_agentcore.evaluation import (
    BatchEvaluationRunner,
    BatchEvaluationRunConfig,
    BatchEvaluatorConfig,
    CloudWatchDataSourceConfig,
    FileDatasetProvider,
)

dataset = FileDatasetProvider("dataset.json").get_dataset()

config = BatchEvaluationRunConfig(
    batch_evaluation_name="MyFailureAnalysis",
    evaluator_config=BatchEvaluatorConfig(
        evaluator_ids=[
            "Builtin.FailureAnalysis",
            "Builtin.GoalSuccessRate",
        ],
    ),
    data_source=CloudWatchDataSourceConfig(
        service_names=["MyAgent.DEFAULT"],
        log_group_names=["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
        ingestion_delay_seconds=180,
    ),
    polling_timeout_seconds=1800,
    polling_interval_seconds=30,
)

runner = BatchEvaluationRunner(region="us-west-2")
result = runner.run_dataset_evaluation(
    agent_invoker=agent_invoker,
    dataset=dataset,
    config=config,
)

print(f"Batch evaluation ID: {result.batch_evaluation_id}")
```
The following AWS CLI command starts a batch evaluation with the failure analysis and goal success rate evaluators.  

```
aws bedrock-agentcore start-batch-evaluation \
  --batch-evaluation-name "MyFailureAnalysis" \
  --evaluators '[
    {"evaluatorId": "Builtin.FailureAnalysis"},
    {"evaluatorId": "Builtin.GoalSuccessRate"}
  ]' \
  --data-source-config '{
    "cloudWatchLogs": {
      "serviceNames": ["MyAgent.DEFAULT"],
      "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
      "filterConfig": {
        "timeRange": {
          "startTime": "2026-10-12T17:00:00Z",
          "endTime": "2026-10-12T17:30:00Z"
        }
      }
    }
  }'
```
The response contains the `batchEvaluationId`. To select sessions by ID instead of by time range, use `"filterConfig": {"sessionIds": ["<session-id>"]}`.
The following Python code starts a batch evaluation with the failure analysis and goal success rate evaluators.  

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.start_batch_evaluation(
    batchEvaluationName="MyFailureAnalysis",
    evaluators=[
        {"evaluatorId": "Builtin.FailureAnalysis"},
        {"evaluatorId": "Builtin.GoalSuccessRate"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": ["MyAgent.DEFAULT"],
            "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
            "filterConfig": {
                "timeRange": {
                    "startTime": "2026-10-12T17:00:00Z",
                    "endTime": "2026-10-12T17:30:00Z",
                }
            },
        }
    },
)

batch_eval_id = response["batchEvaluationId"]
print(f"Batch evaluation ID: {batch_eval_id}")
```

You can also encrypt the results with a customer managed key by specifying `kmsKeyArn`. The insight results are encrypted with that key. If the key policy does not grant the service the `kms:GenerateDataKey` permission, `StartBatchEvaluation` returns a `ValidationException` and the service does not create a batch evaluation. For the key policy that you need, see [Batch evaluation encryption](batch-evaluations-encryption.md).

## Read the insights
<a name="batch-evaluations-insights-read"></a>

Poll `GetBatchEvaluation` until the status is `COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, or `STOPPED`. Then read `insightResults` from the response. For the full list of status values and response fields, see [Get batch evaluation results](batch-evaluations-manage.md#batch-evaluations-get).

**Example**  
The following AgentCore CLI command gets a batch evaluation, including its `insightResults`. Replace `<batch-evaluation-id>` with your batch evaluation ID.  

```
agentcore eval batch-evaluation get \
  --id <batch-evaluation-id> \
  --region us-west-2 --json
```
The command also reads the per-session results from CloudWatch Logs and returns them alongside the job. Pass `--disable-cw-results` to return only the job itself.
 `run_dataset_evaluation` polls until the job reaches a terminal state, so the insights are on the result that it returns. An empty `insight_results` list means that the analysis ran and found no failures, while `None` means that no insight-providing evaluator ran or that the service could not read its results, in which case `error_details` names the evaluator.  

```
print("Status:", result.status)
print("Errors:", result.error_details)

if result.insight_results is None:
    print("No insights were returned.")
else:
    for insight in result.insight_results:
        print(f"{insight.name} ({insight.affected_session_count} sessions)")
        for cause in insight.root_causes or []:
            print(f"  Root cause: {cause.name}")
            print(f"  Suggested fix: {cause.suggested_fix}")
```
Call `fetch_evaluation_events` on the runner to read the per-session results from CloudWatch Logs.
The following AWS CLI command gets a batch evaluation. Replace `<batch-evaluation-id>` with your batch evaluation ID.  

```
aws bedrock-agentcore get-batch-evaluation \
  --batch-evaluation-id <batch-evaluation-id> \
  --output json
```
The following Python code polls a batch evaluation until it reaches a terminal state and then prints the insights. Replace `batch_eval_id` with your batch evaluation ID.  

```
import time
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
batch_eval_id = "my-batch-evaluation-1a2b3c4d5e"

terminal = {"COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPED"}
while True:
    job = client.get_batch_evaluation(batchEvaluationId=batch_eval_id)
    if job["status"] in terminal:
        break
    time.sleep(30)

print("Status:", job["status"])
print("Errors:", job.get("errorDetails"))

for insight in job.get("insightResults", []):
    print(f"{insight['name']} ({insight['affectedSessionCount']} sessions)")
    for cause in insight.get("rootCauses", []):
        print(f"  Root cause: {cause['name']}")
        print(f"  Suggested fix: {cause['suggestedFix']}")
```

### insightResults fields
<a name="batch-evaluations-insights-fields"></a>

 `insightResults` is a list of up to 50 insights. When no session has failures, the list is empty.

The following table describes the fields of each insight.


| Field | Type | Description | 
| --- | --- | --- | 
|  `type`  | String | The kind of insight. For `Builtin.FailureAnalysis`, the value is `FAILURE`. | 
|  `name`  | String | A short name for the insight. Up to 200 characters. | 
|  `description`  | String | A description of the pattern that the insight represents. Up to 4,000 characters. | 
|  `createdAt`  | Timestamp | When the service generated the insight. | 
|  `affectedSessionCount`  | Integer | The number of sessions that the insight affects. A session can appear in more than one insight, so the counts across insights can add up to more than the number of sessions with failures. | 
|  `rootCauses`  | List | The root causes behind the insight. Up to 50 per insight. This field is not present when the insight has no root causes. | 
|  `sampleSessions`  | List | Example sessions for the insight. Present at this level only when the insight has no root causes. Otherwise, the sample sessions are on each root cause. Up to 10 per insight. | 

Each root cause has a name, an explanation, a suggested fix, and up to 10 sample sessions. Each sample session has up to 10 failure findings, which locate the failures at spans. For a readable description of an insight, see [Failure insights](builtin-failure-analysis.md#builtin-failure-analysis-results) in the failure analysis evaluator documentation.

### Example response
<a name="batch-evaluations-insights-example"></a>

The following example shows part of a `GetBatchEvaluation` response for a batch evaluation that ran `Builtin.FailureAnalysis` and `Builtin.GoalSuccessRate`. The `insightResults` field is trimmed to one insight with one root cause.

```
{
    "batchEvaluationId": "MyFailureAnalysis-1a2b3c4d5e",
    "batchEvaluationName": "MyFailureAnalysis",
    "status": "COMPLETED",
    "evaluationResults": {
        "numberOfSessionsCompleted": 20,
        "numberOfSessionsFailed": 0,
        "totalNumberOfSessions": 20,
        "evaluatorSummaries": [
            {
                "evaluatorId": "Builtin.GoalSuccessRate",
                "statistics": {"averageScore": 0.95},
                "totalEvaluated": 20,
                "totalFailed": 0
            },
            {
                "evaluatorId": "Builtin.FailureAnalysis",
                "statistics": {"averageScore": 0.2},
                "totalEvaluated": 20,
                "totalFailed": 0
            }
        ]
    },
    "insightResults": [
        {
            "type": "FAILURE",
            "name": "Tool calls fail because of permission and quota errors",
            "description": "Tool calls that change the state of a service fail because the caller lacks permissions or because a quota is exceeded.",
            "createdAt": "2026-10-12T17:18:26+00:00",
            "affectedSessionCount": 3,
            "rootCauses": [
                {
                    "name": "Constraints are not visible to the agent before it acts",
                    "explanation": "The agent calls tools without checking quotas or permissions first, so the call fails and the request is not completed.",
                    "suggestedFix": "Update the tools to return current limits and permissions, and update the system prompt to check them before it changes a resource.",
                    "affectedSessionCount": 2,
                    "sampleSessions": [
                        {
                            "sessionId": "session-0001",
                            "lastSeenAt": "2026-10-12T17:10:37+00:00",
                            "findings": [
                                {
                                    "targetId": "1a2b3c4d5e6f7a8b",
                                    "targetType": "SPAN_ID",
                                    "description": "The scale_service tool call returned an error because the requested replica count exceeded the quota.",
                                    "category": "execution-error-rate-limiting",
                                    "confidence": 0.9
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

In this example, the average score for `Builtin.FailureAnalysis` is `0.2`, which means that failures were found in 20 percent of the sessions. For this evaluator, a higher score is worse.

## Per-session results
<a name="batch-evaluations-insights-session-results"></a>

In addition to the insights, `Builtin.FailureAnalysis` writes one result for each session to CloudWatch Logs, like any session-level evaluator. By default, the results go to the log group `/aws/bedrock-agentcore/evaluations/batch-evaluations/results/default`, in the log stream `run-<batchEvaluationId>`. If you set `outputConfig`, the results go to the log group that you specify.

Each result has the following values:
+  **Score:** `1.0` when failures were found, and `0.0` when none were found. A higher score is worse.
+  **Label:** `Failures Found` or `No Failures Found`.
+  **Explanation:** A summary of the failures in the session, or `No failures detected in this session.` 

The service also publishes the score as the `Builtin.FailureAnalysis` metric in the `Bedrock-AgentCore/Evaluations` CloudWatch namespace.

## Job status and errors
<a name="batch-evaluations-insights-outcomes"></a>

The status of the batch evaluation and the `insightResults` field depend on how the run went:


| Case | Status | insightResults | 
| --- | --- | --- | 
| Failures were found. |  `COMPLETED`  | A list of insights. | 
| No session had failures. |  `COMPLETED`  | An empty list. | 
| Some sessions could not be evaluated. |  `COMPLETED_WITH_ERRORS`  | Insights for the sessions that were evaluated. The `errorDetails` field names the sessions that failed. | 
| The service could not generate the insights. |  `COMPLETED_WITH_ERRORS`  | Not present. The `errorDetails` field describes the problem. The results of the other evaluators are not affected. | 
| No session could be evaluated. |  `FAILED`  | Not present. | 

A session that has no agent spans in the selected time range fails with the message `No spans were found for the session`, and the batch evaluation can then end with the status `COMPLETED_WITH_ERRORS`. If every selected session fails this way, check the service name, log groups, and time range in your data source configuration.

When insight generation fails, the `errorDetails` field contains the message `Insight generation failed for the Builtin.FailureAnalysis evaluator.` 