

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
+  `bedrock-agentcore`: To start, get, list, stop, and delete batch evaluations
+  `logs` (CloudWatch Logs): To read session spans and write evaluation results

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
            "Sid": "ResolveAgentForCli",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:GetAgentRuntime",
                "bedrock-agentcore:GetHarness"
            ],
            "Resource": [
                "arn:aws:bedrock-agentcore:*:*:runtime/*",
                "arn:aws:bedrock-agentcore:*:*:harness/*"
            ]
        },
        {
            "Sid": "ResolveOnlineEvalForCli",
            "Effect": "Allow",
            "Action": "bedrock-agentcore:GetOnlineEvaluationConfig",
            "Resource": "arn:aws:bedrock-agentcore:*:*:online-evaluation-config/*"
        },
        {
            "Sid": "SimulateForCli",
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:InvokeAgentRuntime",
                "bedrock-agentcore:GetDataset"
            ],
            "Resource": [
                "arn:aws:bedrock-agentcore:*:*:runtime/*",
                "arn:aws:bedrock-agentcore:*:*:dataset/*"
            ]
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
            "Sid": "DescribeLogGroups",
            "Effect": "Allow",
            "Action": "logs:DescribeLogGroups",
            "Resource": "*"
        },
        {
            "Sid": "WriteEvaluationLogs",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:PutRetentionPolicy"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/evaluations/*",
                "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/evaluations/*:*"
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

**Note**  
The `ResolveAgentForCli` statement is required only when you pass `--agent` to `agentcore eval batch-evaluation evaluate`, or when you run `agentcore eval batch-evaluation simulate`. The CLI calls `GetAgentRuntime` to find the log group and service name. For a harness ID, that call returns not found and the CLI then calls `GetHarness`.

**Note**  
The `ResolveOnlineEvalForCli` statement is required only when you pass an online evaluation configuration ID to `--online-eval`. The CLI calls `GetOnlineEvaluationConfig` to look up the configuration ARN. If you pass the ARN, the CLI makes no call.

**Note**  
The `SimulateForCli` statement is required only for `agentcore eval batch-evaluation simulate`. The command invokes the Runtime, which needs `bedrock-agentcore:InvokeAgentRuntime`. If you pass `--bearer-token` for a Runtime that uses JWT authorization, the CLI authenticates with the token and doesn’t need `bedrock-agentcore:InvokeAgentRuntime`. When `--dataset` is a dataset ID, the command also needs `bedrock-agentcore:GetDataset`.

**Note**  
The `WriteEvaluationLogs` statement lets the service create the evaluation-results log group and log streams and write results under your credentials. You must grant `logs:DescribeLogGroups` on `Resource` `*` because this action doesn’t support resource-level permissions.

## SDK and CLI requirements
<a name="batch-eval-sdk-cli"></a>
+  ** AWS SDK (boto3):** Python 3.10 or later.
+  **AgentCore CLI:** Run `agentcore --version` to check your version.

**Note**  
The batch-evaluation CLI surface consists of the following commands:  
 `agentcore eval batch-evaluation evaluate`: Evaluates existing sessions.
 `agentcore eval batch-evaluation simulate`: Replays a dataset and evaluates the generated sessions.
 `agentcore eval batch-evaluation get --id <id>`: Gets a job.
 `agentcore eval batch-evaluation list`: Lists jobs.
 `agentcore eval batch-evaluation stop --id <id>`: Stops a running job.
To delete a batch evaluation, use the AWS SDK.