

# Prerequisites
<a name="batch-evaluations-prereqs"></a>

Before you can run batch evaluations, make sure the following are in place.

## Setup
<a name="batch-eval-agent-requirements"></a>

Set up the following before you run batch evaluations:
+ An agent built with a supported framework and instrumentation library. For more information about supported frameworks and instrumentation libraries, see [Supported agent frameworks](supported-frameworks.md).
+ An agent deployed on AgentCore Runtime with observability enabled, or an agent built with a supported framework configured with [AgentCore Observability](observability.md), including Transaction Search. For more information about telemetry setup, see [Telemetry setup and delivery](supported-frameworks-telemetry.md).
+ An agent invoked with telemetry data in CloudWatch Logs. Wait 2–5 minutes for CloudWatch to ingest the telemetry before starting a batch evaluation.

## AWS credentials and permissions
<a name="batch-eval-credentials"></a>

Batch evaluation runs under the caller’s credentials. Unlike online evaluation, batch evaluation does not require a separate service execution role. The service uses your IAM identity to access CloudWatch Logs for session discovery and to write evaluation results.

 AWS credentials configured with permissions for the following services:
+  `bedrock-agentcore` — to start, get, list, stop, and delete batch evaluations
+  `logs` (CloudWatch Logs) — to read session spans and write evaluation results

### Required IAM permissions
<a name="batch-eval-iam-permissions"></a>

The following IAM policy grants the minimum permissions needed to run batch evaluations:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:StartBatchEvaluation",
                "bedrock-agentcore:GetBatchEvaluation",
                "bedrock-agentcore:ListBatchEvaluations",
                "bedrock-agentcore:StopBatchEvaluation",
                "bedrock-agentcore:DeleteBatchEvaluation"
            ],
            "Resource": "arn:aws:bedrock-agentcore:*:*:batch-evaluate/*"
        },
        {
            "Sid": "ReadAgentLogs",
            "Effect": "Allow",
            "Action": [
                "logs:GetLogEvents",
                "logs:FilterLogEvents",
                "logs:StartQuery",
                "logs:GetQueryResults"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/runtimes/*",
                "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/evaluations/*"
            ]
        },
        {
            "Sid": "BedrockInvokeForCustomEvaluators",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/*",
                "arn:aws:bedrock:*:*:inference-profile/*"
            ]
        }
    ]
}
```

**Note**  
The `BedrockInvokeForCustomEvaluators` statement is required only if you use a custom evaluator that invokes Amazon Bedrock models. You can omit it when using only built-in evaluators.

## SDK and CLI requirements
<a name="batch-eval-sdk-cli"></a>
+  ** AWS SDK (boto3):** Python 3.10 or later.
+  **AgentCore CLI:** Run `agentcore --version` to check your version.

**Note**  
The batch-evaluation CLI surface consists of the following commands:  
 `agentcore run batch-evaluation` — start a batch evaluation
 `agentcore stop batch-evaluation -i <id>` — stop a running batch evaluation
 `agentcore view batch-evaluation [id]` and `agentcore batch-evaluations history` — view a job or list jobs
 `agentcore archive batch-evaluation -i <id>` — archive a batch evaluation job record on the service and clear local history
The `bedrock-agentcore:DeleteBatchEvaluation` IAM action is backed by the CLI’s `archive batch-evaluation` command; there is no literal `delete` CLI verb.