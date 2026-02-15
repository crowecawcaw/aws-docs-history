# Implementing reward functions

## Overview

The reward function (also called scorer or grader) is the core component that evaluates model responses and provides feedback signals for training. It must be implemented as an Lambda function that accepts model responses and returns reward scores.

## Interface format

Your reward function must accept and return data in the following format:

**Sample input sample to training**

```
{
    "messages": [
        {
            "role": "user",
            "content": "Do you have a dedicated security team?"
        }
    ],
   "reference_answer": {
       "compliant": "No",
       "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    }
}
```

**Sample payload for the reward lambda**

The container automatically transforms your data before sending it to your Lambda function by:

1. Generating a model response for each prompt
2. Appending the assistant turn (generated response) to the messages array
3. Adding a unique `id` field for tracking

Your Lambda function will receive data in this transformed format:

```
{
   "id": "123",
    "messages": [
        {
            "role": "user",
            "content": "Do you have a dedicated security team?"
        },
        {
            "role": "assistant",
            "content": "As an AI developed by Amazon, I don not have a dedicated security team..."
        }
    ],
    # Following section will be same as your training dataset sample
    "reference_answer": {
        "compliant": "No",
        "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    }
}
```

**Reward Lambda contract**

```
def lambda_handler(event, context):
   return lambda_grader(event)

def lambda_grader(samples: list[dict]) -> list[dict]:
    """
    Args:
        samples: List of dictionaries in OpenAI format

        Example input:
        {
            "id": "123",
            "messages": [
                {
                    "role": "user",
                    "content": "Do you have a dedicated security team?"
                },
                {
                    "role": "assistant",
                    "content": "As an AI developed by Company, I don nott have a dedicated security team..."
                }
            ],
            # This section will be same as your training dataset
            "reference_answer": {
                "compliant": "No",
                "explanation": "As an AI developed by Company, I do not have a traditional security team..."
            }
        }

    Returns:
        List of dictionaries with reward scores:
        {
            "id": str,                              # Same id as input sample
            "aggregate_reward_score": float,        # Overall score for the sample
            "metrics_list": [                       # OPTIONAL: Component scores
                {
                    "name": str,                    # Name of the component score
                    "value": float,                 # Value of the component score
                    "type": str                     # "Reward" or "Metric"
                }
            ]
        }
    """
```

## Input and output fields

### Input fields

| Field              | Description                           | Additional notes                                  |
| ------------------ | ------------------------------------- | ------------------------------------------------- |
| id                 | Unique identifier for the sample      | Echoed back in output. String format              |
| messages           | Ordered chat history in OpenAI format | Array of message objects                          |
| messages[].role    | Speaker of the message                | Common values: "user", "assistant", "system"      |
| messages[].content | Text content of the message           | Plain string                                      |
| \*\*metadata       | Free-form information to aid grading  | Object; optional fields passed from training data |

### Output fields

| Field                  | Description                                 | Additional notes                            |
| ---------------------- | ------------------------------------------- | ------------------------------------------- |
| id                     | Same identifier as input sample             | Must match input                            |
| aggregate_reward_score | Overall score for the sample                | Float (e.g., 0.0–1.0 or task-defined range) |
| metrics_list           | Component scores that make up the aggregate | Array of metric objects                     |

## Technical constraints

- **Timeout limit** – 15 minutes maximum execution time per Lambda invocation
- **Concurrency** – Must handle `rollout_worker_replicas * 64` concurrent requests
- **Reliability** – Must implement proper error handling and return valid scores consistently
- **Performance** – Optimize for fast execution (seconds, not minutes) to enable efficient training

**Best practices**

- Minimize external API calls
- Use efficient algorithms and data structures
- Implement retry logic for transient failures
- Cache reusable computations
- Test thoroughly before training to ensure bug-free execution

## Using custom reward functions

Implement custom reward functions when you have task-specific evaluation criteria:

- **Define evaluation criteria** – Determine what makes a good response for your task
- **Implement Lambda function** – Create an Lambda function following the interface format
- **Test locally** – Validate your function returns correct scores for sample inputs
- **Deploy to AWS** – Deploy your Lambda and note the ARN
- **Configure recipe** – Add the Lambda ARN to your recipe's `reward_lambda_arn` field
- **Test with small dataset** – Run RFT with minimal data to verify integration

## IAM permissions

### Required permissions

Your SageMaker execution role must have permissions to invoke your Lambda function. Add this policy to your SageMaker execution role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Resource": "arn:aws:lambda:region:account-id:function:function-name"
    }
  ]
}
```

### Lambda execution role

Your Lambda function's execution role needs basic Lambda execution permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```

Additional permissions: If your Lambda function accesses other AWS services (for example, S3 for reference data, DynamoDB for logging), add those permissions to the Lambda execution role.

## Example: LLM As a Judge reward function

This example demonstrates using Amazon Bedrock models as judges to evaluate model responses by comparing them against reference answers. This Lambda template provides a framework for customers to implement calls to Amazon Bedrock for inference requests to process judge evaluations. The Lambda function maintains the same input/output contract as other reward functions.

### Implementation

This Lambda function implements a two-stage evaluation process: the `lambda_handler` extracts model responses and reference answers from incoming samples, then the `lambda_graded` function calls Amazon Bedrock to score the semantic similarity between them. The implementation includes robust error handling with automatic retries for transient failures and supports flexible reference answer formats (both string and structured dictionary formats).

**Implementation details:**

- **Retry Logic**: Implements exponential backoff (1s, 2s, 4s) for throttling exceptions to handle Bedrock API rate limits
- **Error Handling**: Returns score of 0.0 for failed evaluations rather than raising exceptions
- **Deterministic Scoring**: Uses temperature=0.0 to ensure consistent scores across evaluations
- **Flexible Reference Format**: Automatically handles both string and dictionary reference answers
- **Score Clamping**: Ensures all scores fall within valid [0.0, 1.0] range
- **Model Agnostic**: Change JUDGE_MODEL_ID to use any Amazon Bedrock model (Nova, Llama, Mistral, etc.)

```
"""
LLM Judge Lambda POC - Working implementation using Amazon Bedrock
"""

import json
import time
import boto3

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')
JUDGE_MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
SYSTEM_PROMPT = "You must output ONLY a number between 0.0 and 1.0. No explanations, no text, just the number."

JUDGE_PROMPT_TEMPLATE = """Compare the following two responses and rate how similar they are on a scale of 0.0 to 1.0, where:
- 1.0 means the responses are semantically equivalent (same meaning, even if worded differently)
- 0.5 means the responses are partially similar
- 0.0 means the responses are completely different or contradictory

Response A: {response_a}

Response B: {response_b}

Output ONLY a number between 0.0 and 1.0. No explanations."""


def lambda_graded(response_a: str, response_b: str, max_retries: int = 3) -> float:
    """Call Bedrock to compare responses and return similarity score."""
    prompt = JUDGE_PROMPT_TEMPLATE.format(response_a=response_a, response_b=response_b)

    for attempt in range(max_retries):
        try:
            response = bedrock_runtime.converse(
                modelId=JUDGE_MODEL_ID,
                messages=[{"role": "user", "content": [{"text": prompt}]}],
                system=[{"text": SYSTEM_PROMPT}],
                inferenceConfig={"temperature": 0.0, "maxTokens": 10}
            )
            print(f"Bedrock call successful: {response}")
            output = response['output']['message']['content'][0]['text'].strip()
            score = float(output)
            print(f"Score parsed: {score}")
            return max(0.0, min(1.0, score))

        except Exception as e:
            if "ThrottlingException" in str(e) and attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"Bedrock call failed: {e}")
                return None
    return None


def lambda_handler(event, context):
    """AWS Lambda handler - processes samples from RFTEvalInvoker."""
    try:
        samples = event if isinstance(event, list) else [event]
        results = []

        for sample in samples:
            sample_id = sample.get("id", "unknown")
            messages = sample.get("messages", [])

            # Extract assistant response (response A)
            response_a = ""
            for msg in messages:
                if msg.get("role") in ["assistant", "nova_assistant"]:
                    response_a = msg.get("content", "")
                    break

            # Extract reference answer from root level (no longer in metadata)
            reference_answer = sample.get("reference_answer", "")

            # Handle both string and dict reference_answer formats
            if isinstance(reference_answer, dict):
                # If reference_answer is a dict, extract the explanation or compliant field
                response_b = reference_answer.get("explanation", reference_answer.get("compliant", ""))
            else:
                response_b = reference_answer

            if not response_a or not response_b:
                results.append({
                    "id": sample_id,
                    "aggregate_reward_score": 0.0,
                    "metrics_list": [{"name": "similarity_score", "value": 0.0, "type": "Metric"}]
                })
                continue

            # Get similarity score
            score = lambda_graded(response_a, response_b)

            results.append({
                "id": sample_id,
                "aggregate_reward_score": score,
                "metrics_list": [
                    {
                        "name": "similarity_score",
                        "value": score,
                        "type": "Metric"
                    }
                ]
            })

        return {"statusCode": 200, "body": json.dumps(results)}

    except Exception as e:
        print(f"Error: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
```

### Input format

The Lambda receives the same input format as other reward functions:

```
{
    "id": "sample-001",
    "messages": [
        {
            "role": "user",
            "content": "Do you have a dedicated security team?"
        },
        {
            "role": "assistant",
            "content": "As an AI developed by Amazon, I don't have a dedicated security team..."
        }
    ],
    "reference_answer": {
        "compliant": "No",
        "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    },
    "my_custom_field": "custom_value"
}
```

### Output format

```
{
    "id": "sample-001",
    "aggregate_reward_score": 0.85,
    "metrics_list": [
        {
            "name": "similarity_score",
            "value": 0.85,
            "type": "Metric"
        }
    ]
}
```

### Deployment considerations

You may also need to adjust the prompt template and inference parameters based on your chosen model's capabilities and API format.

- **IAM Permissions**: Lambda execution role must have `bedrock:InvokeModel` permission for your chosen model
- **Timeout**: Set Lambda timeout to at least 60 seconds to accommodate Bedrock API latency and retries
- **Region**: Deploy in a region where your chosen Bedrock model is available
- **Cost**: Monitor Bedrock API usage as each evaluation makes one API call per sample
- **Throughput**: For large-scale evaluations, request increased Bedrock quotas to avoid throttling

**Increasing Bedrock Throughput**

If you experience throttling during evaluation, increase your Bedrock model quotas:

- Navigate to the AWS Service Quotas console
- Search for "Bedrock" and select your region
- Find the quota for your chosen model (for example, "Invocations per minute for Claude 3.5 Sonnet")
- Click "Request quota increase" and specify your desired throughput
- Provide justification for the increase (for example, "RFT evaluation workload")

The Lambda's built-in retry logic handles occasional throttling, but sustained high-volume evaluations require appropriate quota increases.

**Required IAM Policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "arn:aws:bedrock:*::foundation-model/*"
        }
    ]
}
```
