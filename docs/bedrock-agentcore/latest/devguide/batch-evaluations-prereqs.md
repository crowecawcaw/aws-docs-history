# Prerequisites

Before you can run batch evaluations, make sure the following are in place.

## Agent requirements

- An agent deployed on AgentCore Runtime with observability enabled, or an agent built with a supported framework configured with [AgentCore Observability](observability.md "observability.md"). Supported frameworks:
  - Strands Agents
  - LangGraph with `opentelemetry-instrumentation-langchain` or `openinference-instrumentation-langchain`

- [Transaction Search](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-getting-started.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-getting-started.md") enabled in CloudWatch (required when using CloudWatch as the session source).
- Agent sessions with telemetry data in CloudWatch Logs. Invoke your agent and wait 2–5 minutes for CloudWatch to ingest the telemetry before starting a batch evaluation.

## AWS credentials and permissions

Batch evaluation runs under the caller’s credentials. Unlike online evaluation, batch evaluation does not require a separate service execution role. The service uses your IAM identity to access CloudWatch Logs for session discovery and to write evaluation results.

AWS credentials configured with permissions for the following services:

- `bedrock-agentcore` — to start, get, list, stop, and delete batch evaluations
- `logs` (CloudWatch Logs) — to read session spans and write evaluation results

### Required IAM permissions

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

###### Note

The `BedrockInvokeForCustomEvaluators` statement is required only if you use a custom evaluator that invokes Amazon Bedrock models. You can omit it when using only built-in evaluators.

## SDK and CLI requirements

- **AWS SDK (boto3):** Python 3.10 or later.
- **AgentCore CLI:** Run `agentcore --version` to check your version.
