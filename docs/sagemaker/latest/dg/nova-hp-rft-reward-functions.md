# Custom reward functions in your AWS

environment

Custom reward functions in your AWS environment support single-turn RFT only. This
trains models on tasks where a single prompt receives a single response, evaluated
independently. The model receives one prompt and generates one response, which is then
scored by your reward function—there's no back-and-forth conversation. This is in contrast
to multi-turn RFT where the model engages in multiple rounds of interaction with an
environment or user before receiving a final reward.

###### Topics

- [Architecture overview](#nova-hp-rft-reward-architecture "#nova-hp-rft-reward-architecture")
- [Recipe configuration](#nova-hp-rft-reward-recipe "#nova-hp-rft-reward-recipe")
- [Recipe parameters](#nova-hp-rft-reward-params "#nova-hp-rft-reward-params")
- [Reasoning mode selection](#nova-hp-rft-reward-reasoning "#nova-hp-rft-reward-reasoning")
- [Reward function implementation](#nova-hp-rft-reward-implementation "#nova-hp-rft-reward-implementation")

## Architecture overview

The architecture consists of two main components:

**Training VPC:**

- **Rollout**: Loads dataset and model, sends rollouts
  to the reward function, and receives rewards
- **Trainer**: Receives rollouts from Rollout
  component, performs forward and backward passes, and updates model weights

**Customer VPC:**

- **Reward Lambda**: Customer-implemented reward
  function that evaluates model responses and returns reward scores

**Workflow:**

1. Rollout loads dataset and model
2. Rollout generates model responses and calls Lambda for rewards
3. Lambda returns reward scores
4. Rollout sends rollouts to Trainer
5. Trainer updates policy weights based on rewards

## Recipe configuration

Use this recipe when your reward function completes processing within 15
minutes.

```
## Nova Lite RLVR Training (PEFT)
run:
  name: my-rft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://example-bucket/train.jsonl
  output_s3_path: ""

  replicas: 2 # Number of compute instances for training. All supported values: {2, 4, 8, 16}
  generation_replicas: 2 # LLM inference replicas
  rollout_worker_replicas: 1

  # Lambda functions for RFT
  reward_lambda_arn: ""

## Training config - essential fields for all services
training_config:
  max_length: 10240
  global_batch_size: 256
  reasoning_effort: high

  data:
    shuffle: false

  rollout:
    rollout_strategy:
      type: off_policy_async
      age_tolerance: 2
    advantage_strategy:
      number_generation: 8
    generator:
      max_new_tokens: 8192
      set_random_seed: true
      temperature: 1
      top_k: 0
    rewards:
      api_endpoint:
        lambda_arn: ${run.reward_lambda_arn}
        lambda_concurrency_limit: 100 # Lambda should be able to handle (rollout_worker_replicas * 64) requests

  # Training configuration
  trainer:
    max_steps: 100
    save_steps: 5
    save_top_k: 5

    # RL parameters
    refit_freq: 4
    clip_ratio_high: 0.2
    ent_coeff: 0.001
    loss_scale: 1

    optim_config:                    # Optimizer settings
        lr: 7e-7                       # Learning rate
        weight_decay: 0.0              # L2 regularization strength (0.0–1.0)
        adam_beta1: 0.9
        adam_beta2: 0.95

    peft:                            # Parameter-efficient fine-tuning (LoRA)
        peft_scheme: "lora"            # Enable LoRA for PEFT
        lora_tuning:
            alpha: 32
            lora_plus_lr_ratio: 64.0     # LoRA+ learning rate scaling factor (0.0–100.0)
```

```
## Nova Lite RLVR Training
run:
  name: my-rft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://example-bucket/train.jsonl
  output_s3_path: ""

  replicas: 2 # Number of compute instances for training. All supported values: {2, 4, 8, 16}
  generation_replicas: 2 # LLM inference replicas
  rollout_worker_replicas: 1

  # Lambda functions for RFT
  reward_lambda_arn: ""

## Training config - essential fields for all services
training_config:
  max_length: 10240
  global_batch_size: 256
  reasoning_effort: high

  data:
    shuffle: false

  rollout:
    rollout_strategy:
      type: off_policy_async
      age_tolerance: 2
    advantage_strategy:
      number_generation: 8
    generator:
      max_new_tokens: 8192
      set_random_seed: true
      temperature: 1
      top_k: 0
    rewards:
      api_endpoint:
        lambda_arn: ${run.reward_lambda_arn}
        lambda_concurrency_limit: 100 # Lambda should be able to handle (rollout_worker_replicas * 64) requests

  # Training configuration
  trainer:
    max_steps: 100
    save_steps: 5
    save_top_k: 5

    # RL parameters
    refit_freq: 4
    clip_ratio_high: 0.2
    ent_coeff: 0.001
    loss_scale: 1

    optim_config:                    # Optimizer settings
        lr: 7e-7                       # Learning rate
        weight_decay: 0.0              # L2 regularization strength (0.0–1.0)
        adam_beta1: 0.9
        adam_beta2: 0.95

    peft:                            # Parameter-efficient fine-tuning (LoRA)
        peft_scheme: "null"            # Disable LoRA for PEFT
```

## Recipe parameters

- `max_steps`: Number of gradient updates to the model. Each update uses
  `global_batch_size × refit_freq` samples. Each sample corresponds to one
  model generation. Total training samples = `max_steps ×
global_batch_size`.
- `max_seq_length`: Maximum context length (in tokens) the model
  processes during training. Should accommodate input prompt length + generated response
  length. Setting too short causes training errors; setting too large wastes GPU memory
  and slows training. Available presets: 8K (default), 16K, 32K.
- `global_batch_size`: Number of samples per gradient update of the
  model. Larger values provide more stable gradients but require more memory. Note that
  each sample corresponds to a generation by the model, and not a prompt. A single
  prompt is used to create `number_generation` samples. Recommended: 64-4096
  in powers of 2.
- `refit_freq`: Frequency at which model weight updates. The number of
  samples in each update is `refit_freq * global_batch_size`. Controls how
  often the generation models is updated. Higher values increases effective batch size,
  leads to more stable learning. Lower values increases training speed, but increases
  variance. Increase in refit_freq, increases "off_policy" data. **Recommended: 4** (min: 1, max: 4).
- `rollout_strategy.off_policy_async`: Enables updates to the model to be
  "off-policy", i.e. the generations that are used to compute the loss may come from a
  previous versions of the model than the current model. Enabling off-policy leads to
  faster training, but can be unstable if the `age_tolerance` is high.
  **Recommended: True** (True, False).
- `rollout_strategy.age_tolerance`: Only works when
  `off_policy_async` is enabled. Only keep the data from the model version
  that is less than `age_tolerance` older from the current model. Lower
  values discards data, higher values holds more data from previous versions of the
  model. **Recommended: 2** (min: 1, max: 20).
- `clip_ratio_high`: Clipping helps prevent large policy updates that
  could destabilize training. Larger values encourage updates that fixes model mistakes
  but can destabilize training. Smaller values lead to less learning. **Recommended: 0.3** (0.1, 10).
- `ent_coeff`: Short for "entropy coefficient," this parameter encourages
  exploration during training by adding an entropy bonus to the loss function. Higher
  values promote more diverse/exploratory behavior, while lower values focus on
  exploiting current knowledge. **Recommended: 0.0** (min:
  0, max: 0.1).

## Reasoning mode selection

Choose from three reasoning effort levels based on your task complexity:

| Reasoning Effort          | Use Case                                      | Cost/Latency | Best For                            |
| ------------------------- | --------------------------------------------- | ------------ | ----------------------------------- |
| omit field (no reasoning) | Simple factual queries, classifications       | Low          | Speed and cost optimization         |
| low                       | Moderate complexity requiring some reasoning  | Medium       | Balanced performance and efficiency |
| high                      | Complex analytical tasks, multi-step problems | High         | Maximum reasoning capability        |

Default behavior: When `reasoning_effort` is specified without a value, it
defaults to `high`.

**Guidelines:**

- Use `high` for complex analytical tasks where step-by-step thinking
  adds value (math, logic, code debugging)
- Use `low` for moderate complexity tasks requiring some reasoning
- Omit the field entirely for direct factual queries, simple classifications, and
  when optimizing for speed and cost

###### Important

Higher reasoning modes improve performance for tasks requiring logical analysis and
complex reasoning, but increase costs and latency during both training and deployment.
They are not helpful for simple factual queries like "What is the capital of
France?"

## Reward function implementation

The reward function (also called scorer or grader) is the core component that
evaluates model responses and provides feedback signals for training. It must be
implemented as an Lambda function that accepts model responses and returns reward
scores.

### Prerequisites

Ensure your Lambda functions and SQS queues follow the required naming format and
that your execution role has the necessary permissions.

**Lambda ARN naming:**

Lambda ARN must follow this naming format:

```
arn:aws:lambda:*:*:function:*SageMaker*
```

**SQS naming (required only for remote reward functions in your
own AWS environment):**

- Ensure SQS permissions in the execution role created for the HyperPod
  cluster
- SQS ARN must match one of these naming formats:

```
arn:aws:sqs:*:*:*SageMaker*
arn:aws:sqs:*:*:*Sagemaker*
arn:aws:sqs:*:*:*sagemaker*
```

- In SQS client, use endpoint override: `--endpoint
https://sqs.us-west-2.amazonaws.com` because in VPCE, legacy SQS Service
  Endpoint is not available

**IAM policy for execution role:**

```
{
  "Action": "lambda:InvokeFunction",
  "Resource": [
    "arn:aws:lambda:*:*:function:*SageMaker*"
  ],
  "Effect": "Allow"
},
{
  "Action": [
    "sqs:DeleteMessage",
    "sqs:ReceiveMessage",
    "sqs:SendMessage"
  ],
  "Resource": [
    "arn:aws:sqs:*:*:*SageMaker*"
  ],
  "Effect": "Allow"
}
```

**VPC endpoint:**

For the HyperPod cluster to invoke Lambda functions, you must:

- Create a VPC endpoint for the Lambda service in your HyperPod cluster's
  VPC
- Associate the endpoint with the cluster's security group
- Ensure the VPC endpoint policy allows the lambda:InvokeFunction action

Verify that you see a lambda endpoint in the VPC attached to the EKS.

### Interface format

Your reward function must accept and return data in the following format.

**Sample input to training:**

```
[{
  "messages": [
    {
      "role": "user",
      "content": "Do you have a dedicated security team?"
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

**Sample payload for the reward Lambda:**

The system appends the assistant turn (generated response) to the last turn of the
`messages` field and adds a unique `id`:

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
      "content": "As an AI developed by Amazon, I do not have a dedicated security team..."
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

**Reward Lambda contract:**

```
def lambda_handler(event, context):
    return lambda_grader(event)

def lambda_grader(samples: list[dict]) -> list[dict]:
    """
    Args:
        samples: List of dictionaries in OpenAI format

        Example input (List of such sample):
        {
            "id": "123",
            "messages": [
                {
                    "role": "user",
                    "content": "Do you have a dedicated security team?"
                },
                {
                    "role": "assistant",
                    "content": "As an AI developed by Company, I do not have a dedicated security team..."
                }
            ],
            "metadata": {
                "reference_answer": {
                    "compliant": "No",
                    "explanation": "As an AI developed by Company, I do not have a traditional security team..."
                },
                "my_key": "sample-001"
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

**Input fields:**

| Field              | Description                           | Additional Notes                                  |
| ------------------ | ------------------------------------- | ------------------------------------------------- |
| id                 | Unique identifier for the sample      | Echoed back in output. String format              |
| messages           | Ordered chat history in OpenAI format | Array of message objects                          |
| messages[].role    | Speaker of the message                | Common values: "user", "assistant", "system"      |
| messages[].content | Text content of the message           | Plain string                                      |
| metadata           | Free-form information to aid grading  | Object; optional fields passed from training data |

**Output fields:**

| Field                  | Description                                 | Additional Notes                            |
| ---------------------- | ------------------------------------------- | ------------------------------------------- |
| id                     | Same identifier as input sample             | Must match input                            |
| aggregate_reward_score | Overall score for the sample                | Float (e.g., 0.0–1.0 or task-defined range) |
| metrics_list           | Component scores that make up the aggregate | Array of metric objects                     |
| metrics_list[].name    | Name of the component metric/reward         | String (e.g., "accuracy", "policy_reward")  |
| metrics_list[].value   | Value of the component metric/reward        | Float                                       |
| metrics_list[].type    | Category of component                       | String: "Reward" or "Metric"                |

### Technical constraints

- **Timeout limit**: 15 minutes maximum execution
  time per Lambda invocation
- **Concurrency**: Must handle
  `rollout_worker_replicas × 64` concurrent requests
- **Reliability**: Must implement proper error
  handling and return valid scores consistently
- **Performance**: Optimize for fast execution
  (seconds, not minutes) to enable efficient training

**Best practices:**

- Minimize external API calls
- Use efficient algorithms and data structures
- Implement retry logic for transient failures
- Cache reusable computations
- Test thoroughly before training to ensure bug-free execution

### Using custom reward functions

Implement custom reward functions when you have task-specific evaluation
criteria:

1. **Define evaluation criteria**: Determine what
   makes a good response for your task
2. **Implement Lambda function**: Create an Lambda
   function following the interface format
3. **Test locally**: Validate your function returns
   correct scores for sample inputs
4. **Deploy to AWS**: Deploy your Lambda and note
   the ARN
5. **Configure recipe**: Add the Lambda ARN to your
   recipe's `reward_lambda_arn` field
6. **Test with small dataset**: Run RFT with minimal
   data to verify integration

### Example Lambda function

This example validates input format and compares model output against reference
answers. Replace the scoring logic with your actual evaluation criteria.

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
    """ Main lambda handler """
    return lambda_grader(event)


def lambda_grader(samples: list[dict]) -> list[dict]:
    """ Core grader function """
    scores: List[RewardOutput] = []
    for sample in samples:

        # Extract components
        idx = sample["id"]
        ground_truth = sample.get("metadata", {}).get("reference_answer")

        if "messages" not in sample:
            print(f"Messages is None/empty for id: {idx}")
            ro = RewardOutput(id=idx, aggregate_reward_score=0.0)
            scores.append(ro)

        if ground_truth is None:
            print(f"No answer found in ground truth for id: {idx}")
            ro = RewardOutput(id=idx, aggregate_reward_score=0.0)
            scores.append(ro)

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

    # Convert to dict format for JSON serialization
    return [asdict(score) for score in scores]


def _extract_ground_truth_text(ground_truth) -> str:
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
```

### Using LLM as a judge for reward

functions

Large Language Models (LLMs) are increasingly being used as judges in reinforcement
fine-tuning (RFT) workflows, providing automated reward signals that guide model
optimization. In this approach, an LLM evaluates model outputs against specified
criteria—whether assessing correctness, quality, style adherence, or semantic
equivalence—and assigns rewards that drive the reinforcement learning process.

This is particularly valuable for tasks where traditional reward functions are
difficult to define programmatically, such as determining whether different
representations (like "1/3", "0.333", and "one-third") are semantically equivalent, or
evaluating nuanced qualities like coherence and relevance. By leveraging LLM-based
judges as reward functions, you can scale RFT to complex domains without requiring
extensive human annotation, enabling rapid iteration and continuous improvement of your
models across diverse use cases beyond traditional alignment problems.

Before deploying an LLM-as-a-Judge in production, validate that the judge model's
evaluations align with human judgment. This involves measuring agreement rates between
the LLM judge and human evaluators on representative samples of your task, ideally
ensuring that the LLM's agreement with humans meets or exceeds inter-human agreement
rates. This validation step helps identify potential biases, ensures the reward signal
is guiding your model in the intended direction, and builds confidence that the
automated evaluation process will produce models that meet your production quality
criteria.

Using LLM-as-a-Judge is a simple extension of using Lambda functions for
Reinforcement Learning with Verifiable Rewards (RLVR). Inside the Lambda function, you
make a call to one of the models hosted in Amazon Bedrock. To ensure the training and evaluation
works well with the judge model, ensure your throughput quota for the Amazon Bedrock model used is
sufficient.

Configure your Lambda function so that the timeout is long, up to a maximum of 15
minutes. The default setting for Lambda is 3 seconds, and changing the timeout in the
Lambda configuration is essential to account for longer response times from Amazon Bedrock models
compared to logic-based reward functions. The Lambda also gets invoked in parallel
during training, so increase the concurrency to fully maximize the throughput available.
Note that the concurrency limit needs to be set in both the Lambda configuration as well
as the training job recipe.

**Sample training recipe:**

```
display_name: "Nova Lite V2 LoRA RLVR SMTJ training on GPU"
version: "1.0"
instance_types: ["ml.p5.48xlarge", "ml.p5en.48xlarge"]

run:
  name: <experiment_name>
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "nova-lite-2/prod"
  data_s3_path: s3://<path>/<training_data>.jsonl
  replicas: 4
  reward_lambda_arn: arn:aws:lambda:<region>:<account>:function:<lambda-name>

## SMTJ RFT Training specific configs
training_config:
  max_length: 1200                             # Context window (tokens) for inputs+prompt
  global_batch_size: 64                         # Total samples per optimizer step across all replicas (16/32/64/128/256)
  reasoning_effort: high                        # Enables reasoning mode High / Low / or null for non-reasoning
  test_freq: 10

  rollout:                                      # How responses are generated for GRPO/advantage calc
    advantage_strategy:
      number_generation: 4                      # N samples per prompt to estimate advantages (variance vs cost)
    generator:
      max_new_tokens: 1024                     # Cap on tokens generated per sample
      set_random_seed: true                     # Seed generation for reproducibility across runs
      temperature: 1                            # Softmax temperature
      top_k: 1                                  # Sample only from top-K logits
    rewards:
      preset_reward_function: null              # Usage of reward functions built into Verl [exact_match, code_executions, math_answers]
      api_endpoint:
        lambda_arn: arn:aws:lambda:<region>:<account>:function:<lambda-name>
        lambda_concurrency_limit: 12             # Max concurrent Lambda invocations (throughput vs. throttling)

  trainer:
    max_steps: 100                                 # Steps to train for. One Step = global_batch_size
    save_steps: 20
    test_freq:10

    # RL parameters
    ent_coeff: 0.0                              # A bonus added to the policy loss that rewards higher-output entropy
    kl_loss_coef: 0.0                         # Weight on the KL penalty between the actor (trainable policy) and a frozen reference model

    optim_config:                    # Optimizer settings
        lr: 1e-6                       # Learning rate
        weight_decay: 0.0              # L2 regularization strength (0.0–1.0)
        adam_beta1: 0.9
        adam_beta2: 0.95
```

**Example Lambda:**

This Lambda function implements an LLM-as-a-Judge reward scoring system for
reinforcement fine-tuning. It processes batches of model-generated responses by
extracting answers from well-formatted outputs (looking for `\boxed{}`
notation), then uses Claude Haiku as a judge model to evaluate semantic similarity
between the extracted answer and the ground truth reference answer on a 0.0-1.0 scale.
The judge compares responses to determine if they're semantically equivalent (even if
represented differently, like "1/3" vs "0.333"), handling cases where answers may be
formatted in various ways. The function includes retry logic for throttling, validates
message structure, and returns a list of reward scores that can be used as training
signals in the reinforcement learning process, with scores of 0.0 assigned when answers
can't be extracted or validation fails.

```
import json
import random

from dataclasses import asdict, dataclass

import re

from typing import Dict, Optional, Any, List
import boto3

from botocore.exceptions import ClientError

from copy import deepcopy
import time

import base64


def extract_solution_nova(solution_str: str) -> Optional[str]:
    """
    Extract solution from Nova-formatted response.

    Args:
        solution_str: The solution text from Nova model
        method: "strict" or "flexible" extraction method

    Returns:
        Extracted numerical answer or None
    """
    boxed_matches = re.findall(r'\\boxed\{([^}]+)\}', solution_str)
    if boxed_matches:
        final_answer = boxed_matches[-1].replace(",", "").replace("$", "")
        return final_answer

    return 0.0

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')
JUDGE_MODEL_ID = "global.anthropic.claude-haiku-4-5-20251001-v1:0"
SYSTEM_PROMPT = "You must output ONLY a number between 0.0 and 1.0. No explanations, no text, just the number."

JUDGE_PROMPT_TEMPLATE = """Compare the following two responses and rate how similar they are on a scale of 0.0 to 1.0, where:
- 1.0 means the responses are semantically equivalent (same meaning, even if worded differently)
- 0.5 means the responses are partially similar
- 0.0 means the responses are completely different or contradictory

Response A: {response_a}

Response B: {response_b}

Output ONLY a number between 0.0 and 1.0. No explanations."""

def lambda_graded(id: str, response_a: str, response_b: str, max_retries: int = 50) -> float:
    """Call Bedrock to compare responses and return similarity score."""
    prompt = JUDGE_PROMPT_TEMPLATE.format(response_a=response_a, response_b=response_b)
    print(f"Calling judge: {JUDGE_MODEL_ID}")
    for attempt in range(max_retries):
        try:
            print(f"Attempt: {attempt}")
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
                print(f"Throttling {id}")
            else:
                print(f"Bedrock call failed: {e}")
                return 0.0
    print("Max retries reached. Unable to complete the request.")
    return 0.0


def compute_score(id: str, solution_str: str, ground_truth: str, method: str = "strict",
                      format_score: float = 0.0, score: float = 1.0,
                      data_source: str ='dataset_name', extra_info: Optional[dict] = None) -> float:
    """
    The scoring function for PandaLM with Nova format.

    Args:
        solution_str: The solution text from Nova model
        ground_truth: JSON string containing the ground truth answer
        method: The method to extract the solution, choices are 'strict' and 'flexible'
        format_score: The score for format compliance
        score: The score for correct answer
        data_source: Should match the data_source in the given dataset
        extra_info: Optional dict with additional fields. Required in function signature.

    Returns:
        Score between 0 and 1
    """
    import json

    answer = extract_solution_nova(solution_str=solution_str, method=method)
    if answer is None:
        return 0.0
    print(f"Answer: {str(answer)}, Reference: {str(ground_truth)}")

    # Clean both answers for comparison
    clean_answer = str(answer)
    clean_ground_truth = str(ground_truth)

    score = lambda_graded(id, response_a=clean_answer, response_b=clean_ground_truth)
    print(f"Raw score: {score}")
    return score


@dataclass
class RewardOutput:
    """Reward service."""

    id: str
    aggregate_reward_score: float

def lambda_handler(event, context):

    scores: List[RewardOutput] = []

    samples = event
    print(len(samples))
    for sample in samples:
        # Extract the ground truth key. In the current dataset it's answer
        print("Sample: ", json.dumps(sample, indent=2))
        ground_truth = sample["reference_answer"]

        idx = "no id"
        # print(sample)
        if not "id" in sample:
            print(f"ID is None/empty for sample: {sample}")
        else:
            idx = sample["id"]

        ro = RewardOutput(id=idx, aggregate_reward_score=0.0)

        if not "messages" in sample:
            print(f"Messages is None/empty for id: {idx}")
            scores.append(RewardOutput(id="0", aggregate_reward_score=0.0))
            continue

        # Extract answer from ground truth dict
        if ground_truth is None:
            print(f"No answer found in ground truth for id: {idx}")
            scores.append(RewardOutput(id="0", aggregate_reward_score=0.0))
            continue

        # Get completion from last message (assistant message)
        last_message = sample["messages"][-1]
        completion_text = last_message["content"]

        if last_message["role"] not in ["assistant", "nova_assistant"]:
            print(f"Last message is not from assistant for id: {idx}")
            scores.append(RewardOutput(id="0", aggregate_reward_score=0.0))
            continue

        if not "content" in last_message:
            print(f"Completion text is empty for id: {idx}")
            scores.append(RewardOutput(id="0", aggregate_reward_score=0.0))
            continue

        random_score = compute_score(id=id, solution_str=completion_text, ground_truth=ground_truth)
        ro = RewardOutput(id=idx, aggregate_reward_score=random_score)

        print(f"Response for id: {idx} is {ro}")
        scores.append(ro)

    return [asdict(score) for score in scores]
```
