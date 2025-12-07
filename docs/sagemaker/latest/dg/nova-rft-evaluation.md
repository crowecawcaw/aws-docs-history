# RFT evaluation

## What is RFT evaluation?

RFT Evaluation allows you to assess your model's performance using custom reward functions before, during, or after reinforcement learning training. Unlike standard evaluations that use pre-defined metrics, RFT Evaluation lets you define your own success criteria through a Lambda function that scores model outputs based on your specific requirements.

## Why evaluate with RFT?

Evaluation is crucial to determine whether the RL fine-tuning process has:

- Improved model alignment with your specific use case and human values
- Maintained or improved model capabilities on key tasks
- Avoided unintended side effects such as reduced factuality, increased verbosity, or degraded performance on other tasks
- Met your custom success criteria as defined by your reward function

## When to use RFT evaluation

Use RFT Evaluation in these scenarios:

- Before RFT Training: Establish baseline metrics on your evaluation dataset
- During RFT Training: Monitor training progress with intermediate checkpoints
- After RFT Training: Validate that the final model meets your requirements
- Comparing Models: Evaluate multiple model versions using consistent reward criteria

###### Note

Use RFT Evaluation when you need custom, domain-specific metrics. For general-purpose evaluation (accuracy, perplexity, BLEU), use standard evaluation methods.

## Data format requirements

### Input data structure

RFT evaluation input data must follow the OpenAI Reinforcement Fine-Tuning format. Each example is a JSON object containing:

- `messages` – Array of conversational turns with `system` and `user` roles
- `reference_answer` – Expected output or ground truth data used by your reward function for scoring

### Data format example

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

### Current limitations

- Text only: No multimodal inputs (images, audio, video) are supported
- Single-turn conversations: Only supports single user message (no multi-turn dialogues)
- JSON format: Input data must be in JSONL format (one JSON object per line)
- Model outputs: Evaluation is performed on generated completions from the specified model

## Preparing your evaluation recipe

### Sample notebook

For a complete example, see [Evaluation notebooks](nova-model-evaluation.md#nova-model-evaluation-notebook "nova-model-evaluation.md#nova-model-evaluation-notebook").

### Sample recipe configuration

```
run:
  name: nova-lite-rft-eval-job
  model_type: amazon.nova-lite-v1:0:300k
  model_name_or_path: s3://escrow_bucket/model_location # [MODIFIABLE] S3 path to your model or model identifier
  replicas: 1 # [MODIFIABLE] For SageMaker Training jobs only; fixed for HyperPod jobs
  data_s3_path: "" # [REQUIRED FOR HYPERPOD] Leave empty for SageMaker Training jobs and use TrainingInput in sagemaker python SDK
  output_s3_path: "" # [REQUIRED] Output artifact S3 path for evaluation results

evaluation:
  task: rft_eval # [FIXED] Do not modify
  strategy: rft_eval # [FIXED] Do not modify
  metric: all # [FIXED] Do not modify

# Inference Configuration
inference:
  max_new_tokens: 8192 # [MODIFIABLE] Maximum tokens to generate
  top_k: -1 # [MODIFIABLE] Top-k sampling parameter
  top_p: 1.0 # [MODIFIABLE] Nucleus sampling parameter
  temperature: 0 # [MODIFIABLE] Sampling temperature (0 = deterministic)
  top_logprobs: 0 # [MODIFIABLE] Set between 1-20 to enable logprobs output

# =============================================================================
# Bring Your Own Reinforcement Learning Environment
# =============================================================================
rl_env:
  reward_lambda_arn: arn:aws:lambda:<region>:<account_id>:function:<reward-function-name>
```

## Preset reward functions

Two preset reward functions (`prime_code` and `prime_math`) from the open source verl library are available as a Lambda layer for easy integration with your RFT Lambda functions.

### Overview

These preset functions provide out-of-the-box evaluation capabilities for:

- `prime_code` – Code generation and correctness evaluation
- `prime_math` – Mathematical reasoning and problem-solving evaluation

### Quick setup

1. Download the Lambda layer from the [nova-custom-eval-sdk releases](https://github.com/aws/nova-custom-eval-sdk/releases "https://github.com/aws/nova-custom-eval-sdk/releases").
2. Publish Lambda layer using AWS Command Line Interface (AWS CLI):

```
aws lambda publish-layer-version \
    --layer-name preset-function-layer \
    --description "Preset reward function layer with dependencies" \
    --zip-file fileb://universal_reward_layer.zip \
    --compatible-runtimes python3.9 python3.10 python3.11 python3.12 \
    --compatible-architectures x86_64 arm64
```

3. Add the layer to your Lambda function in AWS Management Console (Select the preset-function-layer from custom layer and also add AWSSDKPandas-Python312 for numpy dependencies).
4. Import and use in your Lambda code:

```
from prime_code import compute_score  # For code evaluation
from prime_math import compute_score  # For math evaluation
```

### prime_code function

Evaluates Python code generation tasks by executing code against test cases and measuring correctness.

**Example input dataset format**

```
{"messages":[{"role":"user","content":"Write a function that returns the sum of two numbers."}],"reference_answer":{"inputs":["3\n5","10\n-2","0\n0"],"outputs":["8","8","0"]}}
{"messages":[{"role":"user","content":"Write a function to check if a number is even."}],"reference_answer":{"inputs":["4","7","0","-2"],"outputs":["True","False","True","True"]}}
```

**Key features**

- Automatic code extraction from markdown code blocks
- Function detection and call-based testing
- Test case execution with timeout protection
- Syntax validation and compilation checks
- Detailed error reporting with tracebacks

### prime_math function

Evaluates mathematical reasoning and problem-solving capabilities with symbolic math support.

**Input format**

```
{"messages":[{"role":"user","content":"What is the derivative of x^2 + 3x?."}],"reference_answer":"2*x + 3"}
```

**Key features**

- Symbolic math evaluation using SymPy
- Multiple answer formats (LaTeX, plain text, symbolic)
- Mathematical equivalence checking
- Expression normalization and simplification

### Data format requirements

**For code evaluation**

- Inputs: Array of function arguments (proper types: integers, strings, etc.)
- Outputs: Array of expected return values (proper types: booleans, numbers, etc.)
- Code: Must be in Python with clear function definitions

**For math evaluation**

- Reference answer: Mathematical expression or numeric value
- Response: Can be LaTeX, plain text, or symbolic notation
- Equivalence: Checked symbolically, not just string matching

### Best practices

- Use proper data types in test cases (integers vs strings, booleans vs "True")
- Provide clear function signatures in code problems
- Include edge cases in test inputs (zero, negative numbers, empty inputs)
- Format math expressions consistently in reference answers
- Test your reward function with sample data before deployment

### Error handling

Both functions include robust error handling for:

- Compilation errors in generated code
- Runtime exceptions during execution
- Malformed input data
- Timeout scenarios for infinite loops
- Invalid mathematical expressions

## Creating your reward function

### Lambda ARN requirements

Your Lambda ARN must follow this format:

```
"arn:aws:lambda:*:*:function:*SageMaker*"
```

If the Lambda does not have this naming scheme, the job will fail with this error:

```
[ERROR] Unexpected error: lambda_arn must contain one of: ['SageMaker', 'sagemaker', 'Sagemaker'] when running on SMHP platform (Key: lambda_arn)
```

### Lambda request format

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
            "text": "As an AI developed by Company, I don't have a dedicated security team..."
          }
        ]
      }
    ],
    "reference_answer": {
      "compliant": "No",
      "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    }
  }
]
```

###### Note

The message structure includes the nested `content` array, matching the input data format. The last message with role `nova_assistant` contains the model's generated response.

### Lambda response format

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

**Response fields**

- `id` – Must match the input sample ID
- `aggregate_reward_score` – Overall score (typically 0.0 to 1.0)
- `metrics_list` – Array of individual metrics with:
  - `name` – Metric identifier (e.g., "accuracy", "fluency")
  - `value` – Metric score (typically 0.0 to 1.0)
  - `type` – Either "Metric" (for reporting) or "Reward" (used in training)

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

If your Lambda function accesses other AWS services (e.g., S3 for reference data, DynamoDB for logging), add those permissions to the Lambda execution role.

## Executing the evaluation job

1.  **Prepare your data** – Format your evaluation data according to the data format requirements and upload your JSONL file to S3: `s3://your-bucket/eval-data/eval_data.jsonl`
2.  **Configure your recipe** – Update the sample recipe with your configuration:

        * Set `model_name_or_path` to your model location
        * Set `lambda_arn` to your reward function ARN
        * Set `output_s3_path` to your desired output location
        * Adjust `inference` parameters as needed

    Save the recipe as `rft_eval_recipe.yaml`

3.  **Run the evaluation** – Execute the evaluation job using the provided notebook: [Evaluation notebooks](nova-model-evaluation.md#nova-model-evaluation-notebook "nova-model-evaluation.md#nova-model-evaluation-notebook")
4.  **Monitor progress** – Monitor your evaluation job through:
    - SageMaker Console: Check job status and logs
    - CloudWatch Logs: View detailed execution logs
    - Lambda Logs: Debug reward function issues

## Understanding evaluation results

### Output format

The evaluation job outputs results to your specified S3 location in JSONL format. Each line contains the evaluation results for one sample:

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

The RFT Evaluation Job Output is identical to the Lambda Response format. The evaluation service passes through your Lambda function's response without modification, ensuring consistency between your reward calculations and the final results.

### Interpreting results

**Aggregate reward score**

- Range: Typically 0.0 (worst) to 1.0 (best), but depends on your implementation
- Purpose: Single number summarizing overall performance
- Usage: Compare models, track improvement over training

**Individual metrics**

- Metric Type: Informational metrics for analysis
- Reward Type: Metrics used during RFT training
- Interpretation: Higher values generally indicate better performance (unless you design inverse metrics)

### Performance benchmarks

What constitutes "good" performance depends on your use case:

| Score range  | Interpretation | Action                                   |
| ------------ | -------------- | ---------------------------------------- |
| 0.8<br>• 1.0 | Excellent      | Model ready for deployment               |
| 0.6<br>• 0.8 | Good           | Minor improvements may be beneficial     |
| 0.4<br>• 0.6 | Fair           | Significant improvement needed           |
| 0.0<br>• 0.4 | Poor           | Review training data and reward function |

###### Important

These are general guidelines. Define your own thresholds based on business requirements, baseline model performance, domain-specific constraints, and cost-benefit analysis of further training.

## Troubleshooting

### Common issues

| Issue               | Cause                             | Solution                                     |
| ------------------- | --------------------------------- | -------------------------------------------- |
| Lambda timeout      | Complex reward calculation        | Increase Lambda timeout or optimize function |
| Permission denied   | Missing IAM permissions           | Verify SageMaker role can invoke Lambda      |
| Inconsistent scores | Non-deterministic reward function | Use fixed seeds or deterministic logic       |
| Missing results     | Lambda errors not caught          | Add comprehensive error handling in Lambda   |

### Debug checklist

- Verify input data follows the correct format with nested content arrays
- Confirm Lambda ARN is correct and function is deployed
- Check IAM permissions for SageMaker → Lambda invocation
- Review CloudWatch logs for Lambda errors
- Validate Lambda response matches expected format

## Best practices

- Start Simple: Begin with basic reward functions and iterate
- Test Lambda Separately: Use Lambda test events before full evaluation
- Validate on Small Dataset: Run evaluation on subset before full dataset
- Version Control: Track reward function versions alongside model versions
- Monitor Costs: Lambda invocations and compute time affect costs
- Log Extensively: Use print statements in Lambda for debugging
- Set Timeouts Appropriately: Balance between patience and cost
- Document Metrics: Clearly define what each metric measures

## Next steps

After completing RFT evaluation:

- If results are satisfactory: Deploy model to production
- If improvement needed:
  - Adjust reward function
  - Collect more training data
  - Modify training hyperparameters
  - Run additional RFT training iterations

- Continuous monitoring: Re-evaluate periodically with new data
