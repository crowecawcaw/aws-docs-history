# Prerequisites

Before you run on-demand evaluations, make sure the following are in place.

## Setup

Set up the following before you run on-demand evaluations:

- An agent built with a supported framework and instrumentation library. For more information about supported frameworks and instrumentation libraries, see [Supported agent frameworks](supported-frameworks.md "supported-frameworks.md").
- An agent deployed on AgentCore Runtime with observability enabled, or an agent built with a supported framework configured with [AgentCore Observability](observability.md "observability.md"), including Transaction Search. For more information about telemetry setup, see [Telemetry setup and delivery](supported-frameworks-telemetry.md "supported-frameworks-telemetry.md").
- An agent invoked with telemetry data in CloudWatch Logs. Wait 2–5 minutes for CloudWatch to ingest the telemetry before starting an on-demand evaluation.

Your IAM user or role also needs the following permissions to run on-demand evaluations:

## Console and API operations

```
{
"Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:Evaluate"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:Converse",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:ConverseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/*",
                "arn:aws:bedrock:*:*:inference-profile/*"
            ]
        },
        {
            "Sid": "LambdaInvokeForCodeBasedEvaluators",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction",
                "lambda:GetFunction"
            ],
            "Resource": "arn:aws:lambda:*:*:function:*"
        }
    ]
}
```

###### Note

The Lambda permissions are only required if you use [Custom code-based evaluator](code-based-evaluators.md "code-based-evaluators.md"). You can scope the Lambda resource ARN to specific functions as needed.
