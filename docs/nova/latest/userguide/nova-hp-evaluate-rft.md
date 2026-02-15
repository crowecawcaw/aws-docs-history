# RFT evaluation

###### Note

Evaluation via remote reward functions in your own AWS environment is only available
if you are Nova Forge customer.

###### Important

The `rl_env` configuration field is used exclusively for evaluation, not
for training. During training, you configure reward functions using
`reward_lambda_arn` (single-turn) or BYOO infrastructure with
`rollout.delegate: true` (multi-turn).

###### What is RFT Evaluation?

RFT Evaluation allows you to assess your model's performance using custom reward
functions before, during, or after reinforcement learning training. Unlike standard
evaluations that use pre-defined metrics, RFT Evaluation lets you define your own success
criteria through a Lambda function that scores model outputs based on your specific
requirements.

###### Why Evaluate with RFT?

Evaluation is crucial to determine whether the RL fine-tuning process has:

- Improved model alignment with your specific use case and human values
- Maintained or improved model capabilities on key tasks
- Avoided unintended side effects such as reduced factuality, increased verbosity, or
  degraded performance on other tasks
- Met your custom success criteria as defined by your reward function

###### When to Use RFT Evaluation

Use RFT Evaluation in these scenarios:

- Before RFT Training: Establish baseline metrics on your evaluation dataset
- During RFT Training: Monitor training progress with intermediate checkpoints
- After RFT Training: Validate that the final model meets your requirements
- Comparing Models: Evaluate multiple model versions using consistent reward
  criteria

###### Note

Use RFT Evaluation when you need custom, domain-specific metrics. For general-purpose
evaluation (accuracy, perplexity, BLEU), use standard evaluation methods.

###### Topics

- [Data format requirements](#nova-hp-evaluate-rft-data-format "#nova-hp-evaluate-rft-data-format")
- [Preparing your evaluation recipe](#nova-hp-evaluate-rft-recipe "#nova-hp-evaluate-rft-recipe")
- [Preset reward functions](#nova-hp-evaluate-rft-preset "#nova-hp-evaluate-rft-preset")
- [Creating your reward
  function](#nova-hp-evaluate-rft-create-function "#nova-hp-evaluate-rft-create-function")
- [IAM permissions](#nova-hp-evaluate-rft-iam "#nova-hp-evaluate-rft-iam")
- [Executing the evaluation job](#nova-hp-evaluate-rft-execution "#nova-hp-evaluate-rft-execution")
- [Understanding evaluation results](#nova-hp-evaluate-rft-results "#nova-hp-evaluate-rft-results")

## Data format requirements

###### Input data structure

RFT evaluation input data must follow the OpenAI Reinforcement Fine-Tuning format.
Each example is a JSON object containing:

- `messages`: Array of conversational turns with `system` and
  `user` roles
- Optional other metadata, e.g. reference_answer

###### Data format example

The following example shows the required format:

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Solve for x. Return only JSON like {\"x\": <number>}. Equation: 2x + 5 = 13"
        }
      ]
    }
  ],
  "reference_answer": {
    "x": 4
  }
}
```

###### Current limitations

The following limitations apply to RFT evaluation:

- Text only: No multimodal inputs (images, audio, video) are supported
- Single-turn conversations: Only supports single user message (no multi-turn
  dialogues)
- JSON format: Input data must be in JSONL format (one JSON object per line)
- Model outputs: Evaluation is performed on generated completions from the specified
  model

## Preparing your evaluation recipe

###### Sample recipe configuration

The following example shows a complete RFT evaluation recipe:

```
run:
  name: nova-lite-rft-eval-job
  model_type: amazon.nova-lite-v1:0:300k
  model_name_or_path: s3://escrow_bucket/model_location    # [MODIFIABLE] S3 path to your model or model identifier
  replicas: 1                                             # [MODIFIABLE] For SageMaker Training jobs only; fixed for  SageMaker AI Hyperpod  jobs
  data_s3_path: ""                                        # [REQUIRED FOR HYPERPOD] Leave empty for SageMaker Training jobs
  output_s3_path: ""                                      # [REQUIRED] Output artifact S3 path for evaluation results

evaluation:
  task: rft_eval                                          # [FIXED] Do not modify
  strategy: rft_eval                                      # [FIXED] Do not modify
  metric: all                                             # [FIXED] Do not modify

# Inference Configuration
inference:
  max_new_tokens: 8196                                    # [MODIFIABLE] Maximum tokens to generate
  top_k: -1                                               # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0                                              # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0                                          # [MODIFIABLE] Sampling temperature (0 = deterministic)
  top_logprobs: 0

# Evaluation Environment Configuration (NOT used in training)
rl_env:
  reward_lambda_arn: arn:aws:lambda:<region>:<account_id>:function:<reward-function-name>
```

## Preset reward functions

We have made available 2 preset reward functions (prime_code, prime_math) from Open
source [verl](https://github.com/volcengine/verl/tree/312263169b0288d7225d011979d0d04457aec703/verl/utils/reward_score "https://github.com/volcengine/verl/tree/312263169b0288d7225d011979d0d04457aec703/verl/utils/reward_score") library into a lambda layer where you can easily bundle with your RFT
lambda to use.

###### Overview

These preset functions provide out-of-the-box evaluation capabilities for:

- **prime_code**: Code generation and correctness
  evaluation
- **prime_math**: Mathematical reasoning and
  problem-solving evaluation

###### Quick setup

To use preset reward functions:

1. Download the Lambda layer from the [nova-custom-eval-sdk
   releases](https://github.com/aws/nova-custom-eval-sdk/releases "https://github.com/aws/nova-custom-eval-sdk/releases")
2. Publish Lambda layer using AWS CLI:

```
aws lambda publish-layer-version \
    --layer-name preset-function-layer \
    --description "Preset reward function layer with dependencies" \
    --zip-file fileb://universal_reward_layer.zip \
    --compatible-runtimes python3.9 python3.10 python3.11 python3.12 \
    --compatible-architectures x86_64 arm64
```

3. Add the layer to your Lambda function in AWS Console (Select the
   preset-function-layer from custom layer and also add AWSSDKPandas-Python312 for numpy
   dependencies)
4. Import and use in your Lambda code:

```
from prime_code import compute_score  # For code evaluation
from prime_math import compute_score  # For math evaluation
```

###### prime_code function

**Purpose**: Evaluates Python code generation tasks by
executing code against test cases and measuring correctness.

**Example input dataset format from evaluation**:

```
{"messages":[{"role":"user","content":"Write a function that returns the sum of two numbers."}],"reference_answer":{"inputs":["3\n5","10\n-2","0\n0"],"outputs":["8","8","0"]}}
{"messages":[{"role":"user","content":"Write a function to check if a number is even."}],"reference_answer":{"inputs":["4","7","0","-2"],"outputs":["True","False","True","True"]}}
```

**Key features**:

- Automatic code extraction from markdown code blocks
- Function detection and call-based testing
- Test case execution with timeout protection
- Syntax validation and compilation checks
- Detailed error reporting with tracebacks

###### prime_math function

**Purpose**: Evaluates mathematical reasoning and
problem-solving capabilities with symbolic math support.

**Input format**:

```
{"messages":[{"role":"user","content":"What is the derivative of x^2 + 3x?."}],"reference_answer":"2*x + 3"}
```

**Key features**:

- Symbolic math evaluation using SymPy
- Multiple answer formats (LaTeX, plain text, symbolic)
- Mathematical equivalence checking
- Expression normalization and simplification

###### Best practices

Follow these best practices when using preset reward functions:

- Use proper data types in test cases (integers vs strings, booleans vs
  "True")
- Provide clear function signatures in code problems
- Include edge cases in test inputs (zero, negative numbers, empty inputs)
- Format math expressions consistently in reference answers
- Test your reward function with sample data before deployment

## Creating your reward

function

###### Lambda ARN

You must refer to the following format for the Lambda ARN:

```
"arn:aws:lambda:*:*:function:*SageMaker*"
```

If the Lambda does not have this naming scheme, the job will fail with this
error:

```
[ERROR] Unexpected error: lambda_arn must contain one of: ['SageMaker', 'sagemaker', 'Sagemaker'] when running on SMHP platform (Key: lambda_arn)
```

###### Lambda function structure

Your Lambda function receives batches of model outputs and returns reward scores.
Below is a sample implementation:

```
from typing import List, Any
import json
import re
from dataclasses import asdict, dataclass


@dataclass
class MetricResult:
    """Individual metric result."""
    name: str
    value: float
    type: str


@dataclass
class RewardOutput:
    """Reward service output."""
    id: str
    aggregate_reward_score: float
    metrics_list: List[MetricResult]


def lambda_handler(event, context):
    """ Main lambda handler """
    return lambda_grader(event)


def lambda_grader(samples: list[dict]) -> list[dict]:
    """ Core grader function """
    scores: List[RewardOutput] = []

    for sample in samples:
        print("Sample: ", json.dumps(sample, indent=2))

        # Extract components
        idx = sample.get("id", "no id")
        if not idx or idx == "no id":
            print(f"ID is None/empty for sample: {sample}")

        ground_truth = sample.get("reference_answer")

        if "messages" not in sample:
            print(f"Messages is None/empty for id: {idx}")
            continue

        if ground_truth is None:
            print(f"No answer found in ground truth for id: {idx}")
            continue

        # Get model's response (last turn is assistant turn)
        last_message = sample["messages"][-1]

        if last_message["role"] != "nova_assistant":
            print(f"Last message is not from assistant for id: {idx}")
            continue

        if "content" not in last_message:
            print(f"Completion text is empty for id: {idx}")
            continue

        model_text = last_message["content"]

        # --- Actual scoring logic (lexical overlap) ---
        ground_truth_text = _extract_ground_truth_text(ground_truth)

        # Calculate main score and individual metrics
        overlap_score = _lexical_overlap_score(model_text, ground_truth_text)

        # Create two separate metrics as in the first implementation
        accuracy_score = overlap_score  # Use overlap as accuracy
        fluency_score = _calculate_fluency(model_text)  # New function for fluency

        # Create individual metrics
        metrics_list = [
            MetricResult(name="accuracy", value=accuracy_score, type="Metric"),
            MetricResult(name="fluency", value=fluency_score, type="Reward")
        ]

        ro = RewardOutput(
            id=idx,
            aggregate_reward_score=overlap_score,
            metrics_list=metrics_list
        )

        print(f"Response for id: {idx} is {ro}")
        scores.append(ro)

    # Convert to dict format
    result = []
    for score in scores:
        result.append({
            "id": score.id,
            "aggregate_reward_score": score.aggregate_reward_score,
            "metrics_list": [asdict(metric) for metric in score.metrics_list]
        })

    return result


def _extract_ground_truth_text(ground_truth: Any) -> str:
    """
    Turn the `ground_truth` field into a plain string.
    """
    if isinstance(ground_truth, str):
        return ground_truth

    if isinstance(ground_truth, dict):
        # Common patterns: { "explanation": "...", "answer": "..." }
        if "explanation" in ground_truth and isinstance(ground_truth["explanation"], str):
            return ground_truth["explanation"]
        if "answer" in ground_truth and isinstance(ground_truth["answer"], str):
            return ground_truth["answer"]
        # Fallback: stringify the whole dict
        return json.dumps(ground_truth, ensure_ascii=False)

    # Fallback: stringify anything else
    return str(ground_truth)


def _tokenize(text: str) -> List[str]:
    # Very simple tokenizer: lowercase + alphanumeric word chunks
    return re.findall(r"\w+", text.lower())


def _lexical_overlap_score(model_text: str, ground_truth_text: str) -> float:
    """
    Simple lexical overlap score in [0, 1]:
      score = |tokens(model) ∩ tokens(gt)| / |tokens(gt)|
    """
    gt_tokens = _tokenize(ground_truth_text)
    model_tokens = _tokenize(model_text)

    if not gt_tokens:
        return 0.0

    gt_set = set(gt_tokens)
    model_set = set(model_tokens)
    common = gt_set & model_set

    return len(common) / len(gt_set)


def _calculate_fluency(text: str) -> float:
    """
    Calculate a simple fluency score based on:
    - Average word length
    - Text length
    - Sentence structure

    Returns a score between 0 and 1.
    """
    # Simple implementation - could be enhanced with more sophisticated NLP
    words = _tokenize(text)

    if not words:
        return 0.0

    # Average word length normalized to [0,1] range
    # Assumption: average English word is ~5 chars, so normalize around that
    avg_word_len = sum(len(word) for word in words) / len(words)
    word_len_score = min(avg_word_len / 10, 1.0)

    # Text length score - favor reasonable length responses
    ideal_length = 100  # words
    length_score = min(len(words) / ideal_length, 1.0)

    # Simple sentence structure check (periods, question marks, etc.)
    sentence_count = len(re.findall(r'[.!?]+', text)) + 1
    sentence_ratio = min(sentence_count / (len(words) / 15), 1.0)

    # Combine scores
    fluency_score = (word_len_score + length_score + sentence_ratio) / 3

    return fluency_score
```

###### Lambda request format

Your Lambda function receives data in this format:

```
[
  {
    "id": "sample-001",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Do you have a dedicated security team?"
          }
        ]
      },
      {
        "role": "nova_assistant",
        "content": [
          {
            "type": "text",
            "text": "As an AI developed by Company, I don't have a dedicated security team in the traditional sense. However, the development and deployment of AI systems like me involve extensive security measures, including data encryption, user privacy protection, and other safeguards to ensure safe and responsible use."
          }
        ]
      }
    ],
    "reference_answer": {
      "compliant": "No",
      "explanation": "As an AI developed by Company, I do not have a traditional security team. However, the deployment involves stringent safety measures, such as encryption and privacy safeguards."
    }
  }
]
```

###### Note

The message structure includes the nested `content` array, matching the
input data format. The last message with role `nova_assistant` contains the
model's generated response.

###### Lambda response format

Your Lambda function must return data in this format:

```
[
  {
    "id": "sample-001",
    "aggregate_reward_score": 0.75,
    "metrics_list": [
      {
        "name": "accuracy",
        "value": 0.85,
        "type": "Metric"
      },
      {
        "name": "fluency",
        "value": 0.90,
        "type": "Reward"
      }
    ]
  }
]
```

**Response fields**:

- `id`: Must match the input sample ID
- `aggregate_reward_score`: Overall score (typically 0.0 to 1.0)
- `metrics_list`: Array of individual metrics with:
  - `name`: Metric identifier (e.g., "accuracy", "fluency")
  - `value`: Metric score (typically 0.0 to 1.0)
  - `type`: Either "Metric" (for reporting) or "Reward" (used in
    training)

## IAM permissions

###### Required permissions

Your SageMaker AI execution role must have permissions to invoke your Lambda function. Add
this policy to your SageMaker AI execution role:

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

###### Lambda execution role

Your Lambda function's execution role needs basic Lambda execution
permissions:

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

**Additional permissions**: If your Lambda function
accesses other AWS services (e.g., Amazon S3 for reference data, DynamoDB for logging), add
those permissions to the Lambda execution role.

## Executing the evaluation job

1. **Prepare your data**
   - Format your evaluation data according to the data format requirements
   - Upload your JSONL file to Amazon S3:
     `s3://your-bucket/eval-data/eval_data.jsonl`

2. **Configure your recipe**

Update the sample recipe with your configuration:

    * Set `model_name_or_path` to your model location
    * Set `lambda_arn` to your reward function ARN
    * Set `output_s3_path` to your desired output location
    * Adjust `inference` parameters as needed

Save the recipe as `rft_eval_recipe.yaml` 3. **Run the evaluation**

Execute the evaluation job using the provided notebook: [Nova model evaluation notebook](../../../sagemaker/latest/dg/nova-model-evaluation.md#nova-model-evaluation-notebook "../../../sagemaker/latest/dg/nova-model-evaluation.md#nova-model-evaluation-notebook") 4. **Monitor progress**

Monitor your evaluation job through:

    * SageMaker AI Console: Check job status and logs
    * CloudWatch Logs: View detailed execution logs
    * Lambda Logs: Debug reward function issues

## Understanding evaluation results

###### Output format

The evaluation job outputs results to your specified Amazon S3 location in JSONL format.
Each line contains the evaluation results for one sample:

```
{
  "id": "sample-001",
  "aggregate_reward_score": 0.75,
  "metrics_list": [
    {
      "name": "accuracy",
      "value": 0.85,
      "type": "Metric"
    },
    {
      "name": "fluency",
      "value": 0.90,
      "type": "Reward"
    }
  ]
}
```

###### Note

The RFT Evaluation Job Output is identical to the Lambda Response format. The
evaluation service passes through your Lambda function's response without modification,
ensuring consistency between your reward calculations and the final results.

###### Interpreting results

**Aggregate Reward Score**:

- Range: Typically 0.0 (worst) to 1.0 (best), but depends on your
  implementation
- Purpose: Single number summarizing overall performance
- Usage: Compare models, track improvement over training

**Individual Metrics**:

- Metric Type: Informational metrics for analysis
- Reward Type: Metrics used during RFT training
- Interpretation: Higher values generally indicate better performance (unless you
  design inverse metrics)

###### Performance benchmarks

What constitutes "good" performance depends on your use case:

| Score Range  | Interpretation | Action                                   |
| ------------ | -------------- | ---------------------------------------- |
| 0.8<br>• 1.0 | Excellent      | Model ready for deployment               |
| 0.6<br>• 0.8 | Good           | Minor improvements may be beneficial     |
| 0.4<br>• 0.6 | Fair           | Significant improvement needed           |
| 0.0<br>• 0.4 | Poor           | Review training data and reward function |

###### Important

These are general guidelines. Define your own thresholds based on business
requirements, baseline model performance, domain-specific constraints, and cost-benefit
analysis of further training.
