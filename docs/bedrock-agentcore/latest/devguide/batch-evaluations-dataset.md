

# Run a dataset evaluation with AgentCore Evaluations

**Note**  
AgentCore-run dataset evaluation is part of dataset evaluation, which is in public preview. Features and APIs may change before general availability.

An AgentCore-run dataset evaluation creates sessions from a dataset instead of evaluating sessions that already exist in CloudWatch Logs. You provide a published dataset version and an Amazon Bedrock AgentCore Runtime endpoint in a single `StartBatchEvaluation` request. The service then invokes your agent for each scenario, waits for the telemetry to arrive in CloudWatch Logs, and evaluates the resulting sessions. Because the service invokes your AgentCore Runtime agent, you don’t need to write code that invokes it.

**Note**  
The AgentCore-run option supports AgentCore Runtime endpoints that use the HTTP protocol and IAM inbound authorization. If your Runtime uses JWT inbound authorization or another protocol such as MCP or A2A, use an SDK dataset runner. Also use an SDK dataset runner if you host your agent outside AgentCore Runtime. With an SDK dataset runner, either the [on-demand runner](dataset-evaluations-on-demand.md) or the [batch runner](dataset-evaluations-batch.md), your code invokes the agent. See [Choose how to run a dataset evaluation](dataset-evaluations.md#dataset-evaluations-choose).

Use an AgentCore-run dataset evaluation when you need to:
+  **Run a regression suite** against a new agent version before you route traffic to it.
+  **Compare configurations** by running the same dataset version against two Runtime endpoints.
+  **Measure a baseline** on a fixed set of scenarios, without depending on production traffic.

Each scenario is one of two types, and one dataset can contain both:
+  **Fixed:** the scenario lists its user turns. The service sends them to the agent in order.
+  **Dynamic:** you describe a user’s context and goal in the scenario. A model that AgentCore Evaluations manages plays that user. You don’t specify the model, unlike with the SDK dataset runners, where you choose it in `SimulationConfig`. The model writes each user turn based on the conversation so far.

To create a dataset, see [Manage datasets](datasets-manage.md). For the fields that each scenario type uses, see [Dataset schema](dataset-evaluations-schema.md).

## How it works
<a name="batch-dataset-how-it-works"></a>

1.  **You start a job.** You call `StartBatchEvaluation` with the evaluators to run and two configurations. The `datasetExecutionConfig` names the dataset and the Runtime endpoint. The `dataSourceConfig` names the endpoint’s CloudWatch Logs location.

1.  **The service validates the request.** It resolves the dataset version and checks the endpoint and the dataset before the job starts. If a check fails, the call returns an error and the service doesn’t create a job. See [Troubleshooting](#batch-dataset-errors).

1.  **The service runs the scenarios.** Each scenario runs in a new Runtime session, with one `InvokeAgentRuntime` call for each turn. Turns in a scenario run in order; scenarios run in parallel.

1.  **The service evaluates each session.** After a scenario finishes, the service reads its spans from CloudWatch Logs and runs every evaluator on the session. The service passes ground truth from the scenario, such as `expected_response`, `expected_trajectory`, and `assertions`, to the evaluators that use it.

1.  **You get the results.** When the service finishes running and evaluating every scenario, the job reaches a terminal status. The results have the same format as any other batch evaluation, plus the dataset and Runtime version that the job used.

## Requirements
<a name="batch-dataset-requirements"></a>

In addition to the [batch evaluation prerequisites](batch-evaluations-prereqs.md), an AgentCore-run dataset evaluation requires the following.

 **AgentCore Runtime endpoint** 
+ The endpoint and its Runtime are in the same AWS account and Region as the batch evaluation.
+ The endpoint and the Runtime version it serves are both `READY`.
+ The Runtime uses the HTTP server protocol. For an MCP, A2A, or other non-HTTP Runtime, use an [SDK dataset runner](dataset-evaluations.md#dataset-evaluations-choose).
+ The Runtime uses IAM (SigV4) inbound authorization. For a Runtime configured with a JWT authorizer, use an [SDK dataset runner](dataset-evaluations.md#dataset-evaluations-choose).
+ CloudWatch Transaction Search is turned on for the account and Region, and the Runtime sends telemetry to its CloudWatch Logs log group through [AgentCore Observability](observability.md). After you turn on Transaction Search, it can take up to 10 minutes for spans to become available, so turn it on before you start the job. See [Enable transaction search on CloudWatch](observability-get-started.md#enabling-transaction-search).

 **Dataset** 
+ The dataset has at least one published version. You can’t evaluate draft content. To publish a version, see [Manage dataset versions](datasets-versions.md).
+ The version contains between 1 and 1,000 scenarios.
+ If you use a trajectory evaluator (`Builtin.TrajectoryExactOrderMatch`, `Builtin.TrajectoryInOrderMatch`, or `Builtin.TrajectoryAnyOrderMatch`), every fixed and dynamic scenario has an `expected_trajectory`: the list of tool names that you expect the agent to call. For how each trajectory evaluator compares this list with the agent’s tool calls, see [Trajectory matching with expected trajectory](ground-truth-evaluations.md#gt-trajectory-matching).

 **Permissions** 

The service calls your Runtime with your credentials, so the identity that calls `StartBatchEvaluation` needs permission to read and invoke the endpoint. If the dataset is encrypted with a customer managed key, the identity also needs `kms:Decrypt` on that key. See [Permissions](#batch-dataset-permissions).

## Prepare the dataset
<a name="batch-dataset-prepare"></a>

For the JSON format, field requirements, the 2 KB `metadata` limit, and ground truth mapping, see [Dataset schema](dataset-evaluations-schema.md). To create the dataset and publish a version, see [Getting started](datasets-getting-started.md) with datasets.

### How dynamic scenarios run
<a name="batch-dataset-simulated"></a>

In a dynamic scenario, a managed model plays your user. You don’t choose this model or grant it any permissions. For each turn, the model reads `actor_profile`, `scenario_description`, and the conversation so far, and then writes the next user message. The conversation ends when one of the following happens:
+ The simulated user’s goal is met.
+ Your agent hands off the conversation to another agent or a person.
+ The scenario doesn’t give the simulated user enough information to continue.
+ The conversation reaches `max_turns`.

The results don’t record which of these conditions ended a conversation.

Very long agent responses or long scenarios can make a simulated conversation fail. When a scenario fails, the job counts its session in `numberOfSessionsFailed` and continues with the other scenarios. Keep agent responses, `scenario_description`, and `actor_profile` concise.

## Format the request to your agent
<a name="batch-dataset-request-template"></a>

The service sends each user turn to your agent as the `InvokeAgentRuntime` payload. The `requestTemplate` controls the payload’s shape. The service replaces `{{turn.input}}` with the turn’s input.

In a fixed scenario, each entry in `turns` is one user turn. For example, the following scenario has two turns:

```json
{
  "scenario_id": "order-status",
  "turns": [
    {"input": "Where is my order?"},
    {"input": "The order number is 12345."}
  ]
}
```

With the default template, the service sends `{"prompt": "Where is my order?"}` and then `{"prompt": "The order number is 12345."}` in the same Runtime session. In a dynamic scenario, each user turn is a message that the simulated user writes.

By default, if you omit `requestTemplate`, the service sends the turn’s input in a `prompt` field. This matches the example request format in the [AgentCore Runtime HTTP protocol contract](runtime-http-protocol-contract.md):

```json
{"prompt": "{{turn.input}}"}
```

If your agent reads a different field, or needs fixed values in every request, pass your own template. For example:

```json
{"message": "{{turn.input}}", "channel": "evaluation", "locale": "en-US"}
```

A request template must follow these rules:
+ It is a JSON object, up to 10,240 characters.
+ It contains `{{turn.input}}` exactly once.
+  `{{turn.input}}` is the complete value of a JSON string, such as `"{{turn.input}}"`. It can’t be part of a longer string or a field name.

Turns in a scenario share one Runtime session ID, so your agent can keep conversation context across turns the same way it does in production.

## Start the job
<a name="batch-dataset-start"></a>

**Example**  

```python
import json
import time
import uuid

import boto3

REGION = "us-west-2"
ACCOUNT_ID = "111122223333"
AGENT_ID = "MyAgent-abc123XYZ0"   # The Runtime ID
AGENT_NAME = "MyAgent"            # The Runtime name
ENDPOINT = "DEFAULT"

client = boto3.client("bedrock-agentcore", region_name=REGION)

response = client.start_batch_evaluation(
    batchEvaluationName=f"regression_{uuid.uuid4().hex[:8]}",
    evaluators=[
        {"evaluatorId": "Builtin.GoalSuccessRate"},
        {"evaluatorId": "Builtin.Correctness"},
        {"evaluatorId": "Builtin.Helpfulness"},
    ],
    dataSourceConfig={
        "cloudWatchLogs": {
            "serviceNames": [f"{AGENT_NAME}.{ENDPOINT}"],
            "logGroupNames": [f"/aws/bedrock-agentcore/runtimes/{AGENT_ID}-{ENDPOINT}"],
        }
    },
    datasetExecutionConfig={
        "dataset": {
            "datasetId": "my-dataset-id",
            "datasetVersion": "3",   # Omit to use the latest published version
        },
        "agentInvocation": {
            "agentCoreRuntime": {
                "agentRuntimeEndpointArn": (
                    f"arn:aws:bedrock-agentcore:{REGION}:{ACCOUNT_ID}:"
                    f"runtime/{AGENT_ID}/runtime-endpoint/{ENDPOINT}"
                ),
                "requestTemplate": json.dumps({"prompt": "{{turn.input}}"}),
            }
        },
    },
    clientToken=str(uuid.uuid4()),
)

batch_evaluation_id = response["batchEvaluationId"]
print(f"Started: {batch_evaluation_id}")

while True:
    result = client.get_batch_evaluation(batchEvaluationId=batch_evaluation_id)
    print(f"Status: {result['status']}")
    if result["status"] in ("COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "STOPPED"):
        break
    time.sleep(60)

print(json.dumps(result, indent=4, default=str))
```

```bash
aws bedrock-agentcore start-batch-evaluation \
  --region us-west-2 \
  --batch-evaluation-name regression_run_1 \
  --evaluators '[{"evaluatorId":"Builtin.GoalSuccessRate"},{"evaluatorId":"Builtin.Helpfulness"}]' \
  --data-source-config '{
    "cloudWatchLogs": {
      "serviceNames": ["MyAgent.DEFAULT"],
      "logGroupNames": ["/aws/bedrock-agentcore/runtimes/MyAgent-abc123XYZ0-DEFAULT"]
    }
  }' \
  --dataset-execution-config '{
    "dataset": {"datasetId": "my-dataset-id", "datasetVersion": "3"},
    "agentInvocation": {
      "agentCoreRuntime": {
        "agentRuntimeEndpointArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/MyAgent-abc123XYZ0/runtime-endpoint/DEFAULT",
        "requestTemplate": "{\"prompt\":\"{{turn.input}}\"}"
      }
    }
  }'
```
To check the job’s status and results:  

```bash
aws bedrock-agentcore get-batch-evaluation \
  --region us-west-2 \
  --batch-evaluation-id <batch-evaluation-id>
```

A job can take from a few minutes to several hours. The duration depends on the number of scenarios and turns, the number of evaluators, and how long your agent takes to respond. To end a job before it finishes, see [Stop a job](#batch-dataset-stop).

### Request parameters
<a name="batch-dataset-params"></a>

An AgentCore-run dataset evaluation uses the same request as any other batch evaluation, with the following differences.


| Parameter | Required | Description | 
| --- | --- | --- | 
|  `datasetExecutionConfig.dataset.datasetId`  | Yes | The ID of the dataset. | 
|  `datasetExecutionConfig.dataset.datasetVersion`  | No | The number of a published version, such as `"3"`. If you omit it, the service uses the latest published version when the job starts. `DRAFT` isn’t accepted. | 
|  `datasetExecutionConfig.agentInvocation.agentCoreRuntime.agentRuntimeEndpointArn`  | Yes | The ARN of the Runtime endpoint to invoke, in the format `arn:aws:bedrock-agentcore:<region>:<account-id>:runtime/<runtime-id>/runtime-endpoint/<endpoint-name>`. | 
|  `datasetExecutionConfig.agentInvocation.agentCoreRuntime.requestTemplate`  | No | The payload template for each turn. The default is `{"prompt":"{{turn.input}}"}`. See [Format the request to your agent](#batch-dataset-request-template). | 
|  `dataSourceConfig`  | Yes | A `cloudWatchLogs` source with the service name and log group of the same Runtime endpoint. The service reads the sessions it creates from this location. For a Runtime endpoint, the service name is `<runtime-name>.<endpoint-name>` and the log group is `/aws/bedrock-agentcore/runtimes/<runtime-id>-<endpoint-name>`. Don’t set `maxSessions` or `filterConfig`, because the job always runs every scenario in the dataset version. If you set `maxSessions`, `StartBatchEvaluation` returns an error and doesn’t create the job. | 
|  `evaluators`  | Yes | Up to 10 evaluators. An AgentCore-run dataset evaluation requires at least one evaluator. | 
|  `insights`  | — | Not supported with `datasetExecutionConfig`. | 
|  `evaluationMetadata`  | — | Not used. Ground truth comes from the dataset’s scenarios. | 

The `outputConfig`, `kmsKeyArn`, `description`, `tags`, and `clientToken` parameters work the same way as for other batch evaluations. See [Start batch evaluation](batch-evaluations-start.md).

## Read the results
<a name="batch-dataset-results"></a>

 `GetBatchEvaluation` returns the aggregate results described in [Understanding results and output](batch-evaluations-results.md). An AgentCore-run dataset evaluation also returns `datasetExecutionDetails`, which records what the job ran. It includes the dataset version and the Runtime version that the endpoint was serving when the job started.

```json
{
    "batchEvaluationId": "regression_1a2b3c4d-a1b2c3d4e5",
    "batchEvaluationName": "regression_1a2b3c4d",
    "status": "COMPLETED",
    "datasetExecutionDetails": {
        "dataset": {
            "datasetId": "my-dataset-id",
            "datasetVersion": "3"
        },
        "agentInvocation": {
            "agentCoreRuntime": {
                "agentRuntimeEndpointArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/MyAgent-abc123XYZ0/runtime-endpoint/DEFAULT",
                "agentRuntimeVersion": "7",
                "requestTemplate": "{\"prompt\":\"{{turn.input}}\"}"
            }
        }
    },
    "evaluationResults": {
        "numberOfSessionsCompleted": 50,
        "numberOfSessionsFailed": 0,
        "numberOfSessionsInProgress": 0,
        "numberOfSessionsIgnored": 0,
        "totalNumberOfSessions": 50,
        "evaluatorSummaries": [
            {
                "evaluatorId": "Builtin.GoalSuccessRate",
                "statistics": {"averageScore": 0.83},
                "totalEvaluated": 50,
                "totalFailed": 0
            }
        ]
    }
}
```
+  `datasetVersion` is always a version number, including when you omitted it from the request.
+  `agentRuntimeVersion` is the version that the endpoint was serving when the job started. If you move the endpoint to a new version while the job runs, later turns go to the new version. Don’t update the endpoint during a job.
+  `totalNumberOfSessions` is the number of scenarios in the dataset version. A scenario that fails to run counts in `numberOfSessionsFailed`.
+ When some scenarios fail and others succeed, the status is `COMPLETED_WITH_ERRORS`, and `errorDetails` summarizes the most common causes. See [Scenarios that fail during a job](#batch-dataset-errors-run).

### Per-session results
<a name="batch-dataset-per-session"></a>

Each scenario runs in its own Runtime session. As with any batch evaluation, the service writes per-session, per-evaluator results to CloudWatch Logs. See [Per-session detail in CloudWatch Logs](batch-evaluations-results.md#batch-eval-per-session-detail). Results from an AgentCore-run dataset evaluation also carry the following attributes, so you can match each score to a scenario:


| Attribute | Description | 
| --- | --- | 
|  `aws.bedrock_agentcore.dataset.arn`  | The ARN of the dataset. | 
|  `aws.bedrock_agentcore.dataset.version`  | The dataset version. | 
|  `aws.bedrock_agentcore.dataset.scenario.id`  | The scenario’s `scenario_id`. | 
|  `aws.bedrock_agentcore.dataset.scenario.turn.index`  | On trace-level results, the zero-based index of the turn. | 

## Stop a job
<a name="batch-dataset-stop"></a>

To stop a running job, call `StopBatchEvaluation`. The job moves to `STOPPING`, the service stops scenarios that haven’t finished, and the final job status is `STOPPED`. See [Manage batch evaluations](batch-evaluations-manage.md).

## Permissions
<a name="batch-dataset-permissions"></a>

An AgentCore-run dataset evaluation runs under the credentials of the identity that calls `StartBatchEvaluation`. The service uses those credentials to invoke your Runtime endpoint, so the `InvokeAgentRuntime` calls appear in CloudTrail under your identity. You don’t need a separate execution role.

In addition to the policy in [Required IAM permissions](batch-evaluations-prereqs.md#batch-eval-iam-permissions), grant the following. The example limits the identity to one dataset and one Runtime endpoint. Replace {{111122223333}}, {{my-dataset-id}}, {{MyAgent-abc123XYZ0}}, and {{DEFAULT}} with your values. To allow every dataset or Runtime in the account, use ` ` in place of the ID, for example `dataset/` or `runtime/*`.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "StartDatasetBatchEvaluation",
            "Effect": "Allow",
            "Action": "bedrock-agentcore:StartBatchEvaluation",
            "Resource": "arn:aws:bedrock-agentcore:us-west-2:111122223333:dataset/my-dataset-id"
        },
        {
            "Sid": "ReadAndInvokeRuntimeEndpoint",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:GetAgentRuntime",
                "bedrock-agentcore:GetAgentRuntimeEndpoint",
                "bedrock-agentcore:InvokeAgentRuntime"
            ],
            "Resource": [
                "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/MyAgent-abc123XYZ0",
                "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/MyAgent-abc123XYZ0/runtime-endpoint/DEFAULT"
            ]
        }
    ]
}
```
+ AgentCore authorizes `StartBatchEvaluation` against both the batch evaluation and the dataset. Without the `StartDatasetBatchEvaluation` statement, the request fails with `AccessDeniedException`.
+ When the job starts, the service checks `GetAgentRuntimeEndpoint` and `GetAgentRuntime`. It then calls `InvokeAgentRuntime` for each turn. Grant all three actions on both the Runtime ARN and the endpoint ARN. If you grant them on only one of the two ARNs, the job either doesn’t start or fails every scenario.
+ If the dataset is encrypted with a customer managed key, the calling identity also needs `kms:Decrypt` on that key, and the key policy must allow the AgentCore service principal to decrypt the dataset. See [Dataset encryption](datasets-encryption.md).

If you set `kmsKeyArn` on the job, the service also uses that key to encrypt the conversation turns and agent responses that it stores while the job runs. Make sure that you enable the key. Its key policy must allow `kms:GenerateDataKey` and `kms:Decrypt`. See [Encryption](batch-evaluations-encryption.md). If you encrypted the dataset with a customer managed key, make sure that you enable that key too. Its key policy must allow its use. See [dataset encryption](datasets-encryption.md).

## Limits
<a name="batch-dataset-limits"></a>

Your agent must respond to each turn within 15 minutes. A turn that takes longer fails the scenario. For the number of scenarios and turns that a dataset version can contain, see [Dataset schema](dataset-evaluations-schema.md). AgentCore-run dataset evaluations count toward the active batch evaluations quota for your account. See [Quotas for Amazon Bedrock AgentCore](bedrock-agentcore-limits.md).

## Troubleshooting
<a name="batch-dataset-errors"></a>

### Errors when you start a job
<a name="batch-dataset-errors-start"></a>

 `StartBatchEvaluation` returns these errors, and the service doesn’t create a job. The table uses text from the service exceptions; values such as counts and evaluator IDs vary by request.


| Error message (excerpt) | What to do | 
| --- | --- | 
|  `datasetVersion doesn’t identify a published Dataset version`  | Pass the number of a published version, or omit `datasetVersion`. `DRAFT` isn’t accepted. | 
|  `the specified Dataset has no published version available`  | Publish a version with `CreateDatasetVersion`, and then retry. | 
|  `the specified Dataset version contains more than 1000 scenarios`  | Split the dataset, or use a version with 1,000 scenarios or fewer. | 
|  `scenarios in the specified Dataset version are missing expected_trajectory, which these evaluators require in every scenario`  | Add a non-empty `expected_trajectory` to every fixed and dynamic scenario, and publish a new version, or remove the trajectory evaluators. If an older dataset version is missing `expected_trajectory`, the affected scenarios can fail during the run instead. To have the service check this when the job starts, publish a new version. | 
|  `the specified AgentCore Runtime endpoint isn’t available`  | Use an endpoint that your account owns in the Region where you start the job. | 
|  `the specified AgentCore Runtime endpoint isn’t READY`  | Wait until the endpoint and its Runtime version finish updating, and then retry. | 
|  `the specified AgentCore Runtime doesn’t use the HTTP server protocol`  | Use a Runtime that uses the HTTP protocol, or have your code invoke the agent with the [SDK batch dataset runner](dataset-evaluations-batch.md). | 
|  `the specified AgentCore Runtime requires inbound authorization that this operation can’t supply`  | Use a Runtime that uses IAM authorization, or have your code invoke the agent with the [SDK batch dataset runner](dataset-evaluations-batch.md). | 
|  `you don’t have permission to read the specified AgentCore Runtime endpoint`  | Grant `bedrock-agentcore:GetAgentRuntimeEndpoint` and `bedrock-agentcore:GetAgentRuntime`. See [Permissions](#batch-dataset-permissions). | 
|  `requestTemplate must contain exactly one '{{turn.input}}' JSON value`, or another `requestTemplate` error | Fix the template. See [Format the request to your agent](#batch-dataset-request-template). | 
|  `insights can’t be used with datasetExecutionConfig`  | Remove `insights`. Insights aren’t supported for AgentCore-run dataset evaluations. | 
|  `evaluators are required when datasetExecutionConfig is provided`  | Add at least one evaluator. | 
|  `datasetExecutionConfig can’t be used with dataSourceConfig.cloudWatchLogs.maxSessions`  | Remove `maxSessions`. The job always runs every scenario in the version. | 

### Scenarios that fail during a job
<a name="batch-dataset-errors-run"></a>

When scenarios fail after the job starts, the job finishes as `COMPLETED_WITH_ERRORS`, or as `FAILED` if no scenario succeeds. `errorDetails` lists the most frequent causes, with the number of sessions that each cause affected. The following table describes the causes.


| Cause | What to do | 
| --- | --- | 
| The agent returned an error. | Check the AgentCore Runtime application logs. | 
| The agent didn’t finish a turn within 15 minutes. | Make the agent respond faster, and check the AgentCore Runtime application logs. | 
| The identity that started the job isn’t allowed to call `bedrock-agentcore:InvokeAgentRuntime` on the Runtime endpoint. | Grant `InvokeAgentRuntime` on both the Runtime ARN and the endpoint ARN. See [Permissions](#batch-dataset-permissions). | 
| The scenario isn’t valid. A turn of a fixed scenario has no `input`, or a dynamic scenario has neither `input` nor `actor_profile`, or its `max_turns` isn’t from 1 to 30. | Fix the scenario, and publish a new dataset version. | 
| The simulated conversation grew too large for the simulated user. | Shorten the scenario’s `scenario_description`, `actor_profile`, or `input`, or lower `max_turns`. | 
| An AgentCore Runtime or service issue, or the job reached its time limit. | Check the AgentCore Runtime application logs. If they show no errors, try again. If the failure continues, contact AWS Support with the batch evaluation ID. | 

If you don’t see spans for a session in CloudWatch Logs, make sure that your Runtime sends telemetry to the log group in `dataSourceConfig`. Also make sure that you turned on Transaction Search.