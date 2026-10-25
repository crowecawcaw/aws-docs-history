

# Start batch evaluation
<a name="batch-evaluations-start"></a>

Start a batch evaluation to run evaluators against multiple agent sessions. The service discovers sessions from CloudWatch Logs, runs each evaluator against each session, and produces aggregate results.

## Code samples
<a name="start-batch-eval-examples"></a>

**Example**  
Pass the ID of the deployed Runtime or harness with `--agent`. The CLI reads the Runtime or harness to find its log group and service name, so your credentials need the `ResolveAgentForCli` permissions in [Required IAM permissions](batch-evaluations-prereqs.md#batch-eval-iam-permissions). To skip this lookup, pass the log group and service name with `--data-source-config` instead of `--agent`.  

```
agentcore eval batch-evaluation evaluate \
  --agent <AGENT_ID> \
  --evaluators Builtin.GoalSuccessRate Builtin.Helpfulness Builtin.Faithfulness \
  --name my_baseline_eval
```
With optional flags:  

```
# Time window
agentcore eval batch-evaluation evaluate \
  --agent <AGENT_ID> \
  --evaluators Builtin.GoalSuccessRate \
  --name my_baseline_eval \
  --start-time 2026-09-15T00:00:00Z \
  --end-time 2026-09-16T00:00:00Z

# Specific sessions
agentcore eval batch-evaluation evaluate \
  --agent <AGENT_ID> \
  --evaluators Builtin.GoalSuccessRate \
  --name my_session_eval \
  --session-ids session-abc123 session-def456

# With ground truth
agentcore eval batch-evaluation evaluate \
  --agent <AGENT_ID> \
  --evaluators Builtin.GoalSuccessRate Builtin.Correctness \
  --name my_ground_truth_eval \
  --ground-truth file://ground-truth.json

# Sessions that an online evaluation configuration sampled
agentcore eval batch-evaluation evaluate \
  --online-eval <ONLINE_EVAL_ID> \
  --evaluators Builtin.GoalSuccessRate \
  --name my_online_eval_sessions

# Log groups matched by prefix, with results in a custom log group
agentcore eval batch-evaluation evaluate \
  --data-source-config '{"cloudWatchLogs":{"logGroupNamePrefixes":["/aws/bedrock-agentcore/runtimes/MyAgent-"],"serviceNames":["MyAgent.DEFAULT"]}}' \
  --evaluators Builtin.GoalSuccessRate \
  --name my_prefix_eval \
  --output-config '{"cloudWatchConfig":{"resultDestination":"DEDICATED_LOG_GROUP","logGroupName":"/my/team/batch-evaluation-results"}}'
```
Pass exactly one session source: `--agent`, `--online-eval`, or `--data-source-config`. The `--data-source-config` value is the `dataSourceConfig` object described in [Session source](#start-batch-eval-session-source), and it can’t be combined with `--start-time`, `--end-time`, `--session-ids`, or `--endpoint`. Put those filters in its `filterConfig` instead. The `--output-config` value is the `outputConfig` object described in [Result output](#start-batch-eval-output). Use `--endpoint` with `--agent` to read sessions from a Runtime endpoint other than `DEFAULT`. Use `--description` and `--kms-key-arn` to set the job description and the KMS key that encrypts evaluation data.  
The `--ground-truth` file holds a JSON array with one entry per session:  

```
[
  {
    "sessionId": "session-abc123",
    "groundTruth": {
      "inline": {
        "turns": [
          {
            "input": {"prompt": "Where is my order?"},
            "expectedResponse": {"text": "It shipped on Tuesday."}
          }
        ],
        "assertions": [
          {"text": "The agent gives the ship date"}
        ]
      }
    }
  }
]
```
The command starts the asynchronous job and returns its ID. Use `agentcore eval batch-evaluation get --id <id>` to retrieve status and results. To replay a dataset against a Runtime before evaluation, use `agentcore eval batch-evaluation simulate`. It replays only predefined scenarios that have scripted `turns`. For simulated scenarios that contain `actor_profile`, use the AgentCore SDK as described in [User simulation](user-simulation.md).

```
import boto3
import uuid
import time
import json

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

# All sessions in the log group
response = client.start_batch_evaluation(
    batchEvaluationName=f"baseline_eval_{uuid.uuid4().hex[:8]}",
    evaluators=[
        {"evaluatorId": "Builtin.GoalSuccessRate"},
        {"evaluatorId": "Builtin.Helpfulness"},
        {"evaluatorId": "Builtin.Faithfulness"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": ["MyAgent.DEFAULT"],
            "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
        }
    },
    clientToken=str(uuid.uuid4()),
)

batch_eval_id = response["batchEvaluationId"]
print(f"Started: {batch_eval_id}")

# Poll until complete
while True:
    result = client.get_batch_evaluation(batchEvaluationId=batch_eval_id)
    status = result["status"]
    print(f"Status: {status}")

    if status in ("COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPED"):
        break
    time.sleep(30)

print(json.dumps(result, indent=4, default=str))
```
With session ID filtering:  

```
response = client.start_batch_evaluation(
    batchEvaluationName=f"targeted_eval_{uuid.uuid4().hex[:8]}",
    evaluators=[
        {"evaluatorId": "Builtin.GoalSuccessRate"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": ["MyAgent.DEFAULT"],
            "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
            "filterConfig": {
                "sessionIds": ["session-001", "session-002", "session-003"]
            },
        }
    },
    clientToken=str(uuid.uuid4()),
)
```
With time range filtering:  

```
from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)
response = client.start_batch_evaluation(
    batchEvaluationName=f"weekly_eval_{uuid.uuid4().hex[:8]}",
    evaluators=[
        {"evaluatorId": "Builtin.GoalSuccessRate"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": ["MyAgent.DEFAULT"],
            "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123-DEFAULT"],
            "filterConfig": {
                "timeRange": {
                    "startTime": (now - timedelta(days=7)).isoformat(),
                    "endTime": now.isoformat(),
                }
            },
        }
    },
    clientToken=str(uuid.uuid4()),
)
```

## Request parameters
<a name="start-batch-eval-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `batchEvaluationName`  | String | Yes | A name for the batch evaluation job. Pattern: starts with a letter, alphanumeric and underscores, max 48 characters. | 
|  `dataSourceConfig`  | Object | Yes | Where to find agent sessions. Specify a `cloudWatchLogs` source with your agent’s service name and either exact log group names or log group name prefixes. See [Session source](#start-batch-eval-session-source) below. | 
|  `evaluators`  | List | Yes | List of evaluators. Each entry has an `evaluatorId` field (for example, `Builtin.GoalSuccessRate`). Maximum 10 evaluators. | 
|  `evaluationMetadata`  | Object | No | Contains `sessionMetadata`, a list of per-session ground truth and metadata. Maximum 500 entries. | 
|  `outputConfig`  | Object | No | Optional CloudWatch destination for per-session results and score metrics. Specify a `cloudWatchConfig` to choose the result log group and metrics namespace. See [Result output](#start-batch-eval-output) below. | 
|  `clientToken`  | String | No | Idempotency token. If you retry a request with the same client token, the service returns the existing job instead of creating a new one. | 

## Session source
<a name="start-batch-eval-session-source"></a>

The `dataSourceConfig` parameter specifies the CloudWatch Logs location where the service discovers agent sessions.

### Required fields
<a name="start-batch-eval-session-source-required"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `cloudWatchLogs.serviceNames`  | List of strings (exactly 1) | The service name that identifies your agent’s traces in CloudWatch. Convention: `{RuntimeName}.DEFAULT`. | 
|  `cloudWatchLogs.logGroupNames`  | List of strings (1–10) | One way to select input log groups. Specify the exact CloudWatch log group names where agent telemetry is stored. Mutually exclusive with `logGroupNamePrefixes`. | 
|  `cloudWatchLogs.logGroupNamePrefixes`  | List of strings (1–5) | One way to select input log groups. The service discovers sessions from every log group whose name starts with one of these prefixes, so newly created matching log groups are picked up automatically. Mutually exclusive with `logGroupNames`. | 

Specify exactly one of `logGroupNames` or `logGroupNamePrefixes`. In both cases, `serviceNames` is required to identify your agent’s traces within the selected log groups.

If you use `logGroupNamePrefixes` to match Amazon Bedrock AgentCore Runtime log groups, make sure your runtime sends spans to the agent’s own log group. For agents that still use the shared `aws/spans` log group, set `UNIFIED_TRACES_DESTINATION_ENABLED=true` on the runtime. For more information, see [Span destination for agents hosted in Amazon Bedrock AgentCore runtime](observability-configure.md#observability-configure-unified-traces).

```
# Match input log groups by prefix instead of exact names
dataSourceConfig={
    "cloudWatchLogs": {
        "logGroupNamePrefixes": ["/aws/bedrock-agentcore/runtimes/MyAgent-"],
        "serviceNames": ["MyAgent.DEFAULT"]
    }
}
```

### Optional fields
<a name="start-batch-eval-session-source-optional"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `cloudWatchLogs.filterConfig.sessionIds`  | List of strings | Evaluate only these specific session IDs. When omitted, the service discovers all sessions in the log group. | 
|  `cloudWatchLogs.filterConfig.timeRange.startTime`  | ISO 8601 datetime | Filter sessions created after this time. | 
|  `cloudWatchLogs.filterConfig.timeRange.endTime`  | ISO 8601 datetime | Filter sessions created before this time. | 

## Result output
<a name="start-batch-eval-output"></a>

By default, batch evaluation results go to a dedicated, service-managed log group. Use `outputConfig.cloudWatchConfig` to control where per-session results are written and which CloudWatch metrics namespace receives evaluation scores.

### Choose where results are written
<a name="start-batch-eval-output-destination"></a>
+  `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group. If you don’t set `logGroupName`, the service manages the group for you. To use your own group, set `logGroupName` (see [Use a custom output log group](#start-batch-eval-custom-output-log-group)).
+  `SOURCE_LOG_GROUP` – Writes results back to the same log group the agent traces were read from. When you use this value, don’t set `logGroupName`.

### Use a custom output log group
<a name="start-batch-eval-custom-output-log-group"></a>

For `DEDICATED_LOG_GROUP`, set `logGroupName` to write results to a log group you choose. If the log group exists, the service writes to it. If it doesn’t exist, the service creates it. The caller’s credentials must allow `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` on that log group. The name can’t be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from the service-managed default group.

```
# Write results back to the trace source log group
outputConfig={
    "cloudWatchConfig": {
        "resultDestination": "SOURCE_LOG_GROUP"
    }
}

# Write results to a custom dedicated log group
outputConfig={
    "cloudWatchConfig": {
        "resultDestination": "DEDICATED_LOG_GROUP",
        "logGroupName": "/my/team/batch-evaluation-results"
    }
}
```

### Publish metrics to a custom namespace
<a name="start-batch-eval-custom-metrics-namespace"></a>

Set `metricsNamespace` to publish score metrics under your own CloudWatch namespace instead of `Bedrock-AgentCore/Evaluations`. The value can’t begin with `AWS/`.

```
outputConfig={
    "cloudWatchConfig": {
        "metricsNamespace": "MyTeam/Evaluations"
    }
}
```

## Response
<a name="start-batch-eval-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `batchEvaluationId`  | String | Unique identifier for the batch evaluation. | 
|  `batchEvaluationArn`  | String | ARN of the batch evaluation. | 
|  `batchEvaluationName`  | String | The name you specified. | 
|  `status`  | String | Initial status. One of: `PENDING`, `IN_PROGRESS`. | 
|  `evaluators`  | List | The evaluators used. | 
|  `createdAt`  | Timestamp | When the job was created. | 
|  `outputConfig`  | Object | CloudWatch destination for per-session results and score metrics. | 

## Errors
<a name="start-batch-eval-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ValidationException`  | 400 | Invalid request parameters. Check field constraints and required fields. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. Verify IAM policies. | 
|  `ConflictException`  | 409 | A batch evaluation with the same client token already exists with different parameters. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. Retry with exponential backoff. | 
|  `InternalServerException`  | 500 | Service-side error. Retry the request. | 