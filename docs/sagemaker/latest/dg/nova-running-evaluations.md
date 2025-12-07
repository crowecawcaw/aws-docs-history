# Running evaluations and interpreting results

## Executing the evaluation job

### Step 1: Prepare your data

- Format your evaluation data according to the Data Format Requirements
- Upload your JSONL file to S3: `s3://your-bucket/eval-data/eval_data.jsonl`

### Step 2: Configure your recipe

Update the sample recipe with your configuration:

- Set `model_name_or_path` to your model location
- Set `lambda_arn` to your reward function ARN
- Set `output_s3_path` to your desired output location
- Adjust `inference` parameters as needed

Save the recipe as `rft_eval_recipe.yaml`

### Step 3: Run the evaluation

Execute the evaluation job using the provided notebook: [Evaluation notebooks](nova-model-evaluation.md#nova-model-evaluation-notebook "nova-model-evaluation.md#nova-model-evaluation-notebook")

**Evaluation container**

```
708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-TJ-Eval-V2-latest
```

### Step 4: Monitor progress

Monitor your evaluation job through:

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

These are general guidelines. Define your own thresholds based on:

- Business requirements
- Baseline model performance
- Domain-specific constraints
- Cost-benefit analysis of further training

### Analyzing results

**Calculate summary statistics**

```
import json
import numpy as np
scores = []
with open('evaluation_results.jsonl', 'r') as f:
    for line in f:
        result = json.loads(line)
        scores.append(result['aggregate_reward_score'])

print(f"Mean: {np.mean(scores):.3f}")
print(f"Median: {np.median(scores):.3f}")
print(f"Std Dev: {np.std(scores):.3f}")
print(f"Min: {np.min(scores):.3f}")
print(f"Max: {np.max(scores):.3f}")
```

- Identify Failure Cases: Review samples with low scores to understand weaknesses
- Compare Metrics: Analyze correlation between different metrics to identify trade-offs
- Track Over Time: Compare evaluation results across training iterations

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

## Preset reward functions

Two preset reward functions (prime_code, prime_math) from the open source [verl library](https://github.com/volcengine/verl/tree/312263169b0288d7225d011979d0d04457aec703/verl/utils/reward_score "https://github.com/volcengine/verl/tree/312263169b0288d7225d011979d0d04457aec703/verl/utils/reward_score") are available in a Lambda layer that you can bundle with your RFT Lambda.

### Overview

These preset functions provide out-of-the-box evaluation capabilities for:

- **prime_code** – Code generation and correctness evaluation
- **prime_math** – Mathematical reasoning and problem-solving evaluation

### Quick setup

1. Download the Lambda layer from the [nova-custom-eval-sdk releases](https://github.com/aws/nova-custom-eval-sdk/releases "https://github.com/aws/nova-custom-eval-sdk/releases")
2. Publish Lambda layer using AWS CLI:

```
aws lambda publish-layer-version \
    --layer-name preset-function-layer \
    --description "Preset reward function layer with dependencies" \
    --zip-file fileb://universal_reward_layer.zip \
    --compatible-runtimes python3.9 python3.10 python3.11 python3.12 \
    --compatible-architectures x86_64 arm64
```

3. Add the layer to your Lambda function in AWS Management Console (Select the preset-function-layer from custom layer and also add AWSSDKPandas-Python312 for numpy dependencies)
4. Import and use in your Lambda code:

```
from prime_code import compute_score  # For code evaluation
from prime_math import compute_score  # For math evaluation
```

### prime_code function

**Purpose**: Evaluates Python code generation tasks by executing code against test cases and measuring correctness.

**Example input dataset format from evaluation**

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

**Purpose**: Evaluates mathematical reasoning and problem-solving capabilities with symbolic math support.

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

- **Inputs** – Array of function arguments (proper types: integers, strings, etc.)
- **Outputs** – Array of expected return values (proper types: booleans, numbers, etc.)
- **Code** – Must be in Python with clear function definitions

**For math evaluation**

- **Reference answer** – Mathematical expression or numeric value
- **Response** – Can be LaTeX, plain text, or symbolic notation
- **Equivalence** – Checked symbolically, not just string matching

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
