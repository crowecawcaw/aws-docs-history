# Reinforcement fine-tuning (RFT) for Amazon Nova models

## Overview

**What is RFT?**

Reinforcement fine-tuning (RFT) improves model performance by training on feedback signals—measurable scores or rewards indicating how well the model performed—rather than exact correct answers. Unlike supervised fine-tuning that learns from input-output pairs, RFT uses reward functions to evaluate model responses and iteratively optimizes the model to maximize these rewards. This approach excels when defining the exact correct output is challenging, but you can reliably measure response quality.

**When to use RFT**

Use RFT when you can define clear, measurable success criteria but struggle to provide exact correct outputs for training. It's ideal for:

- Tasks where quality is subjective or multifaceted (creative writing, code optimization, complex reasoning)
- Scenarios with multiple valid solutions where some are clearly better than others
- Applications requiring iterative improvement, personalization, or adherence to complex business rules
- Cases where collecting high-quality labeled examples is expensive or impractical

**Best use cases**

RFT excels in domains where output quality can be objectively measured but optimal responses are difficult to define upfront:

- Mathematical problem-solving and code generation
- Scientific reasoning and structured data analysis
- Tasks requiring step-by-step reasoning or multi-turn problem solving
- Applications balancing multiple objectives (accuracy, efficiency, style)
- Scenarios where success can be verified programmatically through execution results or performance metrics

**Supported models**

Amazon Nova Lite 2.0

## Data format

RFT training data must follow the OpenAI Reinforcement Fine-Tuning format. Each training example is a JSON object containing:

- A `messages` array with conversational turns using `system` and `user` roles
- A `reference_answer` field containing the expected output or evaluation criteria for reward calculation

###### Note

Current limitation: Text only. Multimodal inputs are not supported for RFT.

**Example: Math problem**

```
{
  "id": "sample-001",
  "messages": [
    {
      "role": "system",
      "content": "You are a math tutor"
    },
    {
      "role": "user",
      "content": "Solve: 2x + 5 = 13"
    }
  ],
  "reference_answer": {
    "solution": "x = 4",
    "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
  }
}
```

The `reference_answer` field contains the expected output or evaluation criteria that your reward function uses to score the model's response. It is not limited to structured outputs—it can contain any format that helps your reward function evaluate quality.

### Dataset size recommendations

**Starting point**

- Minimum 100 training examples
- Minimum 100 evaluation examples

**Evaluation-first approach**

Before investing in large-scale RFT training, evaluate your model's baseline performance:

- **High performance (greater than 95 percent reward)** – RFT might be unnecessary because your model already performs well
- **Very poor performance (0 percent reward)** – Switch to SFT first to establish basic capabilities
- **Moderate performance** – RFT is likely appropriate

Starting with a small dataset allows you to validate your reward function is bug-free, confirm RFT is the right approach for your use case, identify and fix issues early, and test the workflow before scaling up.

### Characteristics of effective training data

**Clarity and consistency**

Good RFT examples require clear, unambiguous input data that enables accurate reward calculation across different model outputs. Avoid noise in your data, including inconsistent formatting, contradictory labels or instructions, ambiguous prompts, and conflicting reference answers. Any ambiguity will mislead the training process and cause the model to learn unintended behaviors.

**Diversity**

Your dataset should capture the full diversity of production use cases to ensure robust real-world performance. Include different input formats and edge cases, map actual production usage patterns from logs and user analytics, sample across user types, geographic regions, and seasonal variations, and include difficulty levels from simple to complex problems.

**Reward function considerations**

Design your reward function for efficient training. It should execute within seconds (not minutes), parallelize effectively with AWS Lambda, return consistent, reliable scores, and handle different types of model outputs gracefully. Fast, scalable reward functions enable rapid iteration and cost-effective experimentation.

### Additional properties

The RFT data format supports custom fields beyond the core schema requirements (`messages` and `reference_answer`). This flexibility allows you to add any additional data your reward function needs for proper evaluation.

###### Note

You don't need to configure this in your recipe. The data format inherently supports additional fields. Simply include them in your training data JSON, and they will be passed to your reward function in the `metadata` field.

**Common additional properties**

- `task_id` – Unique identifier for tracking
- `difficulty_level` – Problem complexity indicator
- `domain` – Subject area or category
- `expected_reasoning_steps` – Number of steps in solution

These additional fields are passed to your reward function during evaluation, enabling sophisticated scoring logic tailored to your specific use case.

**Examples with additional properties**

Chemistry problem

```
{
  "id": "chem-001",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful chemistry assistant"
    },
    {
      "role": "user",
      "content": "Predict hydrogen bond donors and acceptors for this SMILES: CCN(CC)CCC(=O)c1sc(N)nc1C"
    }
  ],
  "reference_answer": {
    "donor_bond_counts": 2,
    "acceptor_bond_counts": 4
  }
}
```

The `reference_answer` field contains the expected output or evaluation criteria that your reward function uses to score the model's response. It is not limited to structured outputs—it can contain any format that helps your reward function evaluate quality.

Math problem with metadata

```
{
  "messages": [
    {
      "role": "system",
      "content": "You are a math tutor"
    },
    {
      "role": "user",
      "content": "Solve: 2x + 5 = 13"
    }
  ],
  "reference_answer": {
    "solution": "x = 4",
    "steps": ["2x = 13 - 5", "2x = 8", "x = 4"]
  },
  "task_id": "algebra_001",
  "difficulty_level": "easy",
  "domain": "algebra",
  "expected_reasoning_steps": 3
}
```

## Implementing reward functions

Reward functions are implemented as Lambda functions that evaluate model responses and return numerical scores. The Lambda function receives messages and ground truth in the OpenAI format and must return scores as a dictionary.

### IAM permissions

Ensure your SageMaker AI execution role has `InvokeFunction` permissions for the Lambda function.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:my-reward-function-lambda"
    }
  ]
}
```

### Design guidelines

When writing reward functions, do the following:

- **Rank responses** – Give the best answer a clearly higher score
- **Use consistent checks** – Evaluate task completion, format adherence, safety, and reasonable length
- **Maintain stable scaling** – Keep scores normalized and non-exploitable

### Interface format

Your reward function must accept and return data in the following format.

**Input structure**

```
[{
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
  "metadata": {
    "reference_answer": {
      "compliant": "No",
      "explanation": "As an AI developed by Company, I do not have a traditional security team..."
    },
    "my_key": "sample-001"
  }
}]
```

**Output structure**

```
[{
  "id": "123",
  "aggregate_reward_score": 0.85,
  "metrics_list": [
    {
      "name": "accuracy",
      "value": 0.9,
      "type": "Reward"
    },
    {
      "name": "policy_compliance",
      "value": 0.8,
      "type": "Metric"
    }
  ]
}]
```

**Example Lambda function**

```
from typing import List
import json
from dataclasses import asdict, dataclass

@dataclass
class RewardOutput:
    """Reward service output."""
    id: str
    aggregate_reward_score: float

def lambda_handler(event, context):
    """Main lambda handler"""
    return lambda_grader(event)

def lambda_grader(samples: list[dict]) -> list[dict]:
    """Core grader function"""
    scores: List[RewardOutput] = []
    for sample in samples:
        idx = sample["id"]
        ground_truth = sample.get("metadata", {}).get("reference_answer")

        if "messages" not in sample:
            print(f"Messages is None/empty for id: {idx}")
            ro = RewardOutput(id=idx, aggregate_reward_score=0.0)
            scores.append(ro)
            continue

        if ground_truth is None:
            print(f"No answer found in ground truth for id: {idx}")
            ro = RewardOutput(id=idx, aggregate_reward_score=0.0)
            scores.append(ro)
            continue

        # Get model's response (last turn is assistant turn)
        last_message = sample["messages"][-1]
        assert last_message["role"] == "assistant", "Last message must be from assistant"
        model_text = last_message["content"]

        ground_truth_text = _extract_ground_truth_text(ground_truth)

        if model_text.lower() == ground_truth_text.lower():
            score = 1.0
        else:
            score = 0.0

        ro = RewardOutput(id=idx, aggregate_reward_score=score)
        scores.append(ro)

    return [asdict(score) for score in scores]

def _extract_ground_truth_text(ground_truth) -> str:
    """Turn the ground_truth field into a plain string."""
    if isinstance(ground_truth, str):
        return ground_truth

    if isinstance(ground_truth, dict):
        if "explanation" in ground_truth and isinstance(ground_truth["explanation"], str):
            return ground_truth["explanation"]
        if "answer" in ground_truth and isinstance(ground_truth["answer"], str):
            return ground_truth["answer"]
        return json.dumps(ground_truth, ensure_ascii=False)

    return str(ground_truth)
```

## Training configuration

Use the SageMaker AI Training Job notebook template to start a training job. For more information, see [Create a training job](../../../sagemaker/latest/dg/nova-fine-tuning-training-job.md#nova-model-training-jobs-notebook "../../../sagemaker/latest/dg/nova-fine-tuning-training-job.md#nova-model-training-jobs-notebook").

**Training container**

`708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-RFT-latest`

**Instance requirements**

The container supports both Full Rank and LoRA training:

- **LoRA training** – 2/4/6/8 × p5.48xlarge or p5en.48xlarge instances
- **Full Rank training** – 2/4/6/8 × vv48xlarge instances (required)

### Reasoning mode selection

**Available modes**

- `none` – No reasoning (omit the `reasoning_effort` field)
- `low` – Minimal reasoning overhead
- `high` – Maximum reasoning capability (default when `reasoning_effort` is specified)

###### Note

There is no medium option for RFT. If the `reasoning_effort` field is absent from your configuration, reasoning is disabled. When reasoning is enabled, you should set `max_new_tokens` to 32768 to accommodate extended reasoning outputs.

**When to use each mode**

Use `high` reasoning for complex analytical tasks, mathematical problem-solving, multi-step logical deduction, and tasks where step-by-step thinking adds value.

Use `none` (omit `reasoning_effort`) or `low` reasoning for simple factual queries, direct classifications, speed and cost optimization, and straightforward question-answering.

**Cost and performance trade-offs**

Higher reasoning modes increase training time and cost, inference latency and cost, and model capability for complex reasoning tasks.

## Monitoring training

Training logs include comprehensive metrics at each step. Key metric categories include the following:

- **Reward metrics** – `critic/rewards/mean`, `critic/rewards/max`, `critic/rewards/min` (reward distribution), and `val-score/rewards/mean@1` (validation rewards)
- **Model behavior** – `actor/entropy` (policy variation; higher equals more exploratory)
- **Training health** – `actor/pg_loss` (policy gradient loss), `actor/pg_clipfrac` (frequency of clipped updates), and `actor/grad_norm` (gradient magnitude)
- **Response characteristics** – `prompt_length/mean`, `prompt_length/max`, `prompt_length/min` (input token statistics), `response_length/mean`, `response_length/max`, `response_length/min` (output token statistics), and `response/aborted_ratio` (incomplete generation rate; 0 equals all completed)
- **Performance** – `perf/throughput` (training throughput), `perf/time_per_step` (time per training step), and `timing_per_token_ms/*` (per-token processing times)
- **Resource usage** – `perf/max_memory_allocated_gb`, `perf/max_memory_reserved_gb` (GPU memory), and `perf/cpu_memory_used_gb` (CPU memory)

## Using fine-tuned models

After training completes, the final model checkpoint is saved to your specified output location. The checkpoint path is available in training logs and the `manifest.json` file in the output Amazon S3 location (defined by `output_s3_uri` in your notebook).

## Limitations and best practices

**Limitations**

- **Lambda timeout** – Reward functions must complete within 15 minutes (prevents runaway processes and manages costs)
- **Single-turn only** – Multi-turn conversations are not supported
- **Data requirements** – Needs sufficient diversity; struggles with sparse rewards (less than 5 percent positive examples)
- **Computational cost** – More expensive than supervised fine-tuning

**Best practices**

- **Start small** – Begin with 100-200 examples, validate reward function correctness, and scale gradually based on results
- **Pre-training evaluation** – Test baseline model performance before RFT. If rewards are consistently 0 percent, use SFT first to establish basic capabilities. If rewards are greater than 95 percent, RFT might be unnecessary.
- **Monitor training** – Track average reward scores and distribution. Watch for overfitting (training rewards increase while validation rewards decrease). Look for concerning patterns such as rewards plateauing below 0.15, increasing reward variance over time, and declining validation performance.
- **Optimize reward functions** – Execute within seconds (not minutes), minimize external API calls, use efficient algorithms, implement proper error handling, and take advantage of Lambda's parallel scaling
- **Iteration strategy** – If rewards aren't improving, adjust reward function design, increase dataset diversity, add more representative examples, and verify reward signals are clear and consistent
