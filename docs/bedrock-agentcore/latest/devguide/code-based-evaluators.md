# Custom code-based evaluator

Custom code-based evaluators let you use your own AWS Lambda function to programmatically
evaluate agent performance, instead of using an LLM as a judge. This gives you full control
over the evaluation logic — you can implement deterministic checks, call external APIs, run
regex matching, compute custom metrics, or apply any business-specific rules.

## Prerequisites

To use custom code-based evaluators, you need:

- An AWS Lambda function deployed in the same Region as your AgentCore Evaluations
  resources.
- An IAM execution role that grants the AgentCore Evaluations service permission to
  invoke your Lambda function.
- The Lambda function must return a JSON response conforming to the response
  schema described in [Response schema](#code-based-response-schema "#code-based-response-schema").

## IAM permissions

Your service execution role needs the following additional permission to invoke Lambda
functions for code-based evaluation:

```
{
    "Sid": "LambdaInvokeStatement",
    "Effect": "Allow",
    "Action": [
        "lambda:InvokeFunction",
        "lambda:GetFunction"
    ],
    "Resource": "arn:aws:lambda:`region`:`account-id`:function:`function-name`"
}
```

## Lambda function contract

###### Note

The maximum runtime timeout for the Lambda function is 5 minutes (300 seconds).
The maximum input payload size sent to the Lambda function is 6 MB.

### Input schema

Your Lambda function receives a JSON payload with the following structure:

```
{
    "schemaVersion": "1.0",
    "evaluatorId": "my-evaluator-abc1234567",
    "evaluatorName": "MyCodeEvaluator",
    "evaluationLevel": "TRACE",
    "evaluationInput": {
        "sessionSpans": [...]
    },
    "evaluationTarget": {
        "traceIds": ["trace123"],
        "spanIds": ["span123"]
    }
}
```

| Field                          | Type   | Description                                                                                                 |
| ------------------------------ | ------ | ----------------------------------------------------------------------------------------------------------- |
| `schemaVersion`                | String | Schema version of the payload. Currently<br>`"1.0"`.                                                        |
| `evaluatorId`                  | String | The ID of the code-based evaluator.                                                                         |
| `evaluatorName`                | String | The name of the code-based evaluator.                                                                       |
| `evaluationLevel`              | String | The evaluation level: `TRACE`,<br>`TOOL_CALL`, or `SESSION`.                                                |
| `evaluationInput`              | Object | Contains the session spans for evaluation.                                                                  |
| `evaluationInput.sessionSpans` | List   | The session spans to evaluate. May be truncated if the original<br>payload exceeds 6 MB.                    |
| `evaluationTarget`             | Object | Identifies the specific traces or spans to evaluate. For<br>session-level evaluators, this value is `None`. |
| `evaluationTarget.traceIds`    | List   | The trace IDs of the evaluation target. Present for trace-level<br>and tool-level evaluations.              |
| `evaluationTarget.spanIds`     | List   | The span IDs of the evaluation target. Present for tool-level<br>evaluations.                               |

### Response schema

Your Lambda function must return a JSON object matching one of two formats:

**Success response**

```
{
    "label": "PASS",
    "value": 1.0,
    "explanation": "All validation checks passed."
}
```

| Field         | Required | Type   | Description                                                                                     |
| ------------- | -------- | ------ | ----------------------------------------------------------------------------------------------- |
| `label`       | Yes      | String | A categorical label for the evaluation result (for example,<br>"PASS", "FAIL", "Good", "Poor"). |
| `value`       | No       | Number | A numeric score (for example, 0.0 to 1.0).                                                      |
| `explanation` | No       | String | A human-readable explanation of the evaluation result.                                          |

**Error response**

```
{
    "errorCode": "VALIDATION_FAILED",
    "errorMessage": "Input spans missing required tool call attributes."
}
```

| Field          | Required | Type   | Description                                |
| -------------- | -------- | ------ | ------------------------------------------ |
| `errorCode`    | Yes      | String | A code identifying the error.              |
| `errorMessage` | Yes      | String | A human-readable description of the error. |

## Create a code-based evaluator

The `CreateEvaluator` API creates a code-based evaluator by specifying a
Lambda function ARN and optional timeout.

**Required parameters:** A unique evaluator name,
evaluation level (`TRACE`, `TOOL_CALL`, or
`SESSION`), and a code-based evaluator configuration containing the Lambda
ARN.

**Code-based evaluator configuration:**

```
{
    "codeBased": {
        "lambdaConfig": {
            "lambdaArn": "arn:aws:lambda:`region`:`account-id`:function:`function-name`",
            "lambdaTimeoutInSeconds": 60
        }
    }
}
```

| Field                    | Required | Default | Description                                           |
| ------------------------ | -------- | ------- | ----------------------------------------------------- |
| `lambdaArn`              | Yes      | —       | The ARN of the Lambda function to invoke.             |
| `lambdaTimeoutInSeconds` | No       | 60      | Timeout in seconds for the Lambda invocation (1–300). |

The following code samples demonstrate how to create code-based evaluators using
different development approaches.

AgentCore SDK

```
from bedrock_agentcore.evaluation.code_based_evaluators import (
    EvaluatorInput,
    EvaluatorOutput,
    code_based_evaluator,
)
import json as _json

@code_based_evaluator()
def json_response_evaluator(input: EvaluatorInput) -> EvaluatorOutput:
    """Check if the agent response in the target trace contains valid JSON."""
    for span in input.session_spans:
        if span.get("traceId") != input.target_trace_id:
            continue
        if span.get("name", "").startswith("Model:") or span.get("name") == "Agent.invoke":
            output = span.get("attributes", {}).get("gen_ai.completion", "")
            try:
                _json.loads(output)
                return EvaluatorOutput(
                    value=1.0,
                    label="Pass",
                    explanation="Response contains valid JSON"
                )
            except (ValueError, TypeError):
                pass

    return EvaluatorOutput(
        value=0.0,
        label="Fail",
        explanation="No valid JSON found in agent response"
    )
```

AWS SDK

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.create_evaluator(
    evaluatorName="MyCodeEvaluator",
    level="TRACE",
    evaluatorConfig={
        "codeBased": {
            "lambdaConfig": {
                "lambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:my-eval-function",
                "lambdaTimeoutInSeconds": 120
            }
        }
    }
)

print(f"Evaluator ID: {response['evaluatorId']}")
print(f"Evaluator ARN: {response['evaluatorArn']}")
```

AWS CLI

```
aws bedrock-agentcore-control create-evaluator \
    --evaluator-name 'MyCodeEvaluator' \
    --level TRACE \
    --evaluator-config '{
        "codeBased": {
            "lambdaConfig": {
                "lambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:my-eval-function",
                "lambdaTimeoutInSeconds": 120
            }
        }
    }'
```

## Run on-demand evaluation with a code-based evaluator

Once created, use the custom code-based evaluator with the `Evaluate` API
the same way you would use any other evaluator. The service handles Lambda invocation,
parallel fan-out, and result mapping automatically.

AgentCore SDK

```
from bedrock_agentcore.evaluation.client import EvaluationClient

client = EvaluationClient(
    region_name="`region`"
)

results = client.run(
    evaluator_ids=[
        "`code-based-evaluator-id`",
    ],
    session_id="`session-id`",
    log_group_name="`log-group-name`",
)
```

AWS SDK

```
import boto3

client = boto3.client('bedrock-agentcore')

response = client.evaluate(
    evaluatorId="`code-based-evaluator-id`",
    evaluationInput={"sessionSpans": session_span_logs}
)

for result in response["evaluationResults"]:
    if "errorCode" in result:
        print(f"Error: {result['errorCode']} - {result['errorMessage']}")
    else:
        print(f"Label: {result['label']}, Value: {result.get('value')}")
        print(f"Explanation: {result.get('explanation', '')}")
```

AWS CLI

```
aws bedrock-agentcore evaluate \
    --cli-input-json file://session_span_logs.json
```

### Using evaluation targets

You can target specific traces or spans, just like with LLM-based
evaluators:

```
# Trace-level evaluation
response = client.evaluate(
    evaluatorId="`code-based-evaluator-id`",
    evaluationInput={"sessionSpans": session_span_logs},
    evaluationTarget={"traceIds": ["`trace-id-1`", "`trace-id-2`"]}
)

# Tool-level evaluation
response = client.evaluate(
    evaluatorId="`code-based-evaluator-id`",
    evaluationInput={"sessionSpans": session_span_logs},
    evaluationTarget={"spanIds": ["`span-id-1`", "`span-id-2`"]}
)
```
