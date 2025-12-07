# Reinforcement Fine-Tuning (RFT) with Amazon Nova models

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

Nova Lite 2.0

## Data format overview

RFT training data must follow the OpenAI Reinforcement Fine-Tuning [format](https://platform.openai.com/docs/api-reference/fine-tuning/reinforcement-input "https://platform.openai.com/docs/api-reference/fine-tuning/reinforcement-input"). Each training example is a JSON object containing:

- A `messages` array with conversational turns using `system` and `user` roles
- A `reference_answer` field containing the expected output or evaluation criteria for reward calculation

**Current limitations**

- Text only

### Data format examples

Each example should be on a single line in your JSONL file, with one JSON object per line.

Chemistry problem

```
{
  "id": "chem-01",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful chemistry assistant"
    },
    {
      "role": "user",
      "content": "Calculate the molecular weight of caffeine (C8H10N4O2)"
    }
  ],
  "reference_answer": {
    "molecular_weight": 194.19,
    "unit": "g/mol",
    "calculation": "8(12.01) + 10(1.008) + 4(14.01) + 2(16.00) = 194.19"
  }
}
```

Math problem

```
{
  "id": "sample-001",  // Optional
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

Code problem

```
{
  "id": "code-002",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful programming assistant"
    },
    {
      "role": "user",
      "content": "Write a Python function that reverses a string without using built-in reverse methods"
    }
  ],
  "reference_answer": {
    "code": "def reverse_string(s):  \n    result = ''  \n    for i in range(len(s) - 1, -1, -1):  \n        result += s[i]  \n    return result",
    "test_cases": [
      {
        "input": "hello",
        "expected_output": "olleh"
      },
      {
        "input": "",
        "expected_output": ""
      },
      {
        "input": "a",
        "expected_output": "a"
      },
      {
        "input": "Python123",
        "expected_output": "321nohtyP"
      }
    ],
    "all_tests_pass": true
  }
}
```

The `reference_answer` field contains the expected output or evaluation criteria that your reward function uses to score the model's response. It is not limited to structured outputs—it can contain any format that helps your reward function evaluate quality.

## Dataset size recommendations

**Starting point**

- Minimum 100 training examples
- Minimum 100 evaluation examples

**Evaluation-first approach**

Before investing in large-scale RFT training, evaluate your model's baseline performance:

- **High performance (>95% reward)** – RFT may be unnecessary—your model already performs well
- **Very poor performance (0% reward)** – Switch to SFT first to establish basic capabilities
- **Moderate performance** – RFT is likely appropriate

Starting with a small dataset allows you to:

- Validate your reward function is bug-free
- Confirm RFT is the right approach for your use case
- Identify and fix issues early
- Test the workflow before scaling up

Once validated, you can expand to larger datasets to further improve performance.

## Characteristics of effective training data

**Clarity and consistency**

Good RFT examples require clear, unambiguous input data that enables accurate reward calculation across different model outputs. Avoid noise in your data, including:

- Inconsistent formatting
- Contradictory labels or instructions
- Ambiguous prompts
- Conflicting reference answers

Any ambiguity will mislead the training process and cause the model to learn unintended behaviors.

**Diversity**

Your dataset should capture the full diversity of production use cases to ensure robust real-world performance. Include:

- Different input formats and edge cases
- Map actual production usage patterns from logs and user analytics
- Sample across user types, geographic regions, and seasonal variations
- Include difficulty levels from simple to complex problems

**Reward function considerations**

Design your reward function for efficient training:

- Execute within seconds (not minutes)
- Parallelize effectively with Lambda
- Return consistent, reliable scores
- Handle different types of model outputs gracefully

Fast, scalable reward functions enable rapid iteration and cost-effective experimentation.

## Additional properties

The RFT data format supports custom fields beyond the core schema requirements (`messages` and `reference_answer`). This flexibility lets you add any additional data your reward function needs for proper evaluation.

###### Note

You don't need to configure this in your recipe—the data format inherently supports additional fields. Simply include them in your training data JSON, and they will be passed to your reward function in the `metadata` field.

**Common additional properties**

Example metadata fields:

- `task_id` – Unique identifier for tracking
- `difficulty_level` – Problem complexity indicator
- `domain` – Subject area or category
- `expected_reasoning_steps` – Number of steps in solution

**Example with additional properties**

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

These additional fields are passed to your reward function during evaluation, enabling sophisticated scoring logic tailored to your specific use case.

## Training configuration

**Sample recipe**

```
# Note:
# This recipe can run on p5.48xlarge and p5en.48xlarge instance types.
run:
  name: "my-rft-run"                           # Unique run name (appears in logs/artifacts).
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://<bucket>/<data file>      # Training dataset in JSONL;
  replicas: 4
  reward_lambda_arn: ""

## SMTJ GRPO Training specific configs
training_config:
  max_length: 8192                              # Context window (tokens) for inputs+prompt;
  global_batch_size: 16                         # Total samples per optimizer step across all replicas (16/32/64/128/256).
  reasoning_effort: high                        # Enables reasoning mode high / low / or null for non-reasoning

  rollout:                                      # How responses are generated for GRPO/advantage calc.
    advantage_strategy:
      number_generation: 2                      # N samples per prompt to estimate advantages (variance vs cost).
    generator:
      max_new_tokens: 6000                      # Cap on tokens generated per sample
      set_random_seed: true                     # Seed generation for reproducibility across runs.
      temperature: 1                            # Softmax temperature;
      top_k: 1                                  # Sample only from top-K logits
    rewards:
      preset_reward_function: null              # Usage of reward functions built into Verl [exact_match, code_executions, math_answers]
      api_endpoint:
        lambda_arn: ""
        lambda_concurrency_limit: 12             # Max concurrent Lambda invocations (throughput vs. throttling).

  trainer:
    max_steps: 2                                 # Steps to train for. One Step = global_batch_size
    save_steps: 5
    test_steps: 1
    save_top_k: 5

    # RL parameters
    ent_coeff: 0.0                              # A bonus added to the policy loss that rewards higher-output entropy.
    kl_loss_coef: 0.001                         # Weight on the KL penalty between the actor (trainable policy) and a frozen reference model

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

## RFT training using LLM as a judge

### Overview

Large language models (LLMs) are increasingly being used as judges in reinforcement fine-tuning (RFT) workflows, providing automated reward signals that guide model optimization. In this approach, an LLM evaluates model outputs against specified criteria—whether assessing correctness, quality, style adherence, or semantic equivalence—and assigns rewards that drive the reinforcement learning process.

This is particularly valuable for tasks where traditional reward functions are difficult to define programmatically, such as determining whether different representations (like "1/3", "0.333", and "one-third") are semantically equivalent, or evaluating nuanced qualities like coherence and relevance. By using LLM-based judges as reward functions, you can scale RFT to complex domains without requiring extensive human annotation, enabling rapid iteration and continuous improvement of your models across diverse use cases beyond traditional alignment problems.

### Reasoning mode selection

**Available modes**

- none – No reasoning (omit the reasoning_effort field)
- low – Minimal reasoning overhead
- high – Maximum reasoning capability (default when reasoning_effort is specified)

###### Note

There is no medium option for RFT. If the reasoning_effort field is absent from your configuration, reasoning is disabled. When reasoning is enabled, you should set `max_new_tokens` to 32768 to accommodate extended reasoning outputs.

**When to use each mode**

Use high reasoning for:

- Complex analytical tasks
- Mathematical problem-solving
- Multi-step logical deduction
- Tasks where step-by-step thinking adds value

Use none (omit reasoning_effort) or low reasoning for:

- Simple factual queries
- Direct classifications
- Speed and cost optimization
- Straightforward question-answering

**Cost and performance trade-offs**

Higher reasoning modes increase:

- Training time and cost
- Inference latency and cost
- Model capability for complex reasoning tasks

### Validating your LLM judge

Before deploying an LLM-as-a-judge in production, validate that the judge model's evaluations align with human judgment. This involves:

- Measuring agreement rates between the LLM judge and human evaluators on representative samples of your task
- Ensuring that the LLM's agreement with humans meets or exceeds inter-human agreement rates
- Identifying potential biases in the judge model
- Building confidence that the reward signal guides your model in the intended direction

This validation step helps ensure the automated evaluation process will produce models that meet your production quality criteria.

### Lambda configuration for LLM judge

Using an LLM as a judge is an extension of using Lambda functions for Reinforcement Learning with Verifiable Rewards (RLVR). Inside the Lambda function, you make a call to one of the models hosted in Amazon Bedrock.

**Important configuration requirements:**

| Configuration             | Requirement           | Details                                                                                                                                                            |
| ------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Amazon Bedrock throughput | Sufficient quota      | Ensure your throughput quota for the Amazon Bedrock model used is sufficient for your training workload                                                            |
| Lambda timeout            | Extended timeout      | Configure your Lambda function timeout up to the maximum of 15 minutes. The default setting is 3 seconds, which is insufficient for Amazon Bedrock model responses |
| Lambda concurrency        | Increased concurrency | The Lambda gets invoked in parallel during training. Increase concurrency to maximize available throughput                                                         |
| Recipe configuration      | Match Lambda settings | The concurrency limit must be configured in your recipe                                                                                                            |

## Creating and running jobs

**Starting a training job**

Use the SageMaker AI Training Job notebook template: [https://docs.aws.amazon.com/sagemaker/latest/dg/nova-fine-tuning-training-job.html#nova-model-training-jobs-notebook](nova-fine-tuning-training-job.md#nova-model-training-jobs-notebook "nova-fine-tuning-training-job.md#nova-model-training-jobs-notebook")

**Instance requirements**

The container supports both Full-Rank and LoRA training:

- **LoRA training** – 2/4/6/8 × p5.48xlarge or p5en.48xlarge instances
- **Full-Rank training** – 2/4/6/8 × p5.48xlarge instances (required)

## Monitoring training

Training logs include comprehensive metrics at each step. Key metric categories:

**Reward metrics**

- `critic/rewards/mean`, `critic/rewards/max`, `critic/rewards/min` – Reward distribution
- `val-score/rewards/mean@1` – Validation rewards

**Model behavior**

- `actor/entropy` – Policy variation (higher = more exploratory)

**Training health**

- `actor/pg_loss` – Policy gradient loss
- `actor/pg_clipfrac` – Frequency of clipped updates
- `actor/grad_norm` – Gradient magnitude

**Response characteristics**

- `prompt_length/mean`, `prompt_length/max`, `prompt_length/min` – Input token statistics
- `response_length/mean`, `response_length/max`, `response_length/min` – Output token statistics
- `response/aborted_ratio` – Incomplete generation rate (0 = all completed)

**Performance**

- `perf/throughput` – Training throughput
- `perf/time_per_step` – Time per training step
- `timing_per_token_ms/*` – Per-token processing times

**Resource usage**

- `perf/max_memory_allocated_gb`, `perf/max_memory_reserved_gb` – GPU memory
- `perf/cpu_memory_used_gb` – CPU memory

## Using fine-tuned models

After training completes, the final model checkpoint is saved to your specified output location. The checkpoint path is available in:

- Training logs
- `manifest.json` file in the output Amazon S3 location (defined by `output_s3_uri` in your notebook)

## Limitations and best practices

**Limitations**

- **Lambda timeout** – Reward functions must complete within 15 minutes (prevents runaway processes and manages costs)
- **Single-turn only** – Multi-turn conversations are not supported
- **Data requirements** – Needs sufficient diversity; struggles with sparse rewards (<5% positive examples)
- **Computational cost** – More expensive than supervised fine-tuning
- **No multi-modal data** – Only text data type is supported

**Best practices**

**Start small**

- Begin with 100-200 examples
- Validate reward function correctness
- Scale gradually based on results

**Pre-training evaluation**

- Test baseline model performance before RFT
- If rewards are consistently 0%, use SFT first to establish basic capabilities
- If rewards are >95%, RFT may be unnecessary

**Monitor training**

- Track average reward scores and distribution
- Watch for overfitting (training rewards increase while validation rewards decrease)
- Look for concerning patterns:
  - Rewards plateauing below 0.15
  - Increasing reward variance over time
  - Declining validation performance

**Optimize reward functions**

- Execute within seconds (not minutes)
- Minimize external API calls
- Use efficient algorithms
- Implement proper error handling
- Take advantage of Lambda's parallel scaling

**Iteration strategy**

If rewards aren't improving:

- Adjust reward function design
- Increase dataset diversity
- Add more representative examples
- Verify reward signals are clear and consistent

## Advanced capabilities: Nova Forge

For users requiring advanced capabilities beyond standard RFT limitations, Nova Forge is available as a paid subscription service offering:

- Multi-turn conversation support
- Reward functions with >15 minute execution time
- Additional algorithms and tuning options
- Custom training recipe modifications
- State-of-the-art AI techniques

Nova Forge runs on SageMaker AI HyperPod and is designed to support enterprise customers to build their own frontier models.

## Useful commands and tips

A collection of [observability scripts](https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/SageMakerUilts/SageMakerJobsMonitoring "https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/SageMakerUilts/SageMakerJobsMonitoring") is available to help monitor the status and progress of training jobs.

Available scripts are:

- Enabling email notifications for training job status updates
- Obtaining training time estimates based on job configurations
- Obtaining approximations for how long training is expected to take for in-progress jobs

**Installation**

###### Note

Be sure to refresh your AWS credentials prior to using any of the following scripts.

```
pip install boto3
git clone https://github.com/aws-samples/amazon-nova-samples.git
cd amazon-nova-samples/customization/SageMakerUilts/SageMakerJobsMonitoring/
```

**Basic usage**

```
# Enabling email notifications for training job status updates
python enable_sagemaker_job_notifs.py --email test@amazon.com test2@gmail.com --region us-east-1 --platform SMTJ

Creating resources........
Please check your email for a subscription confirmation email, and click 'Confirm subscription' to start receiving job status email notifications!
You'll receive the confirmation email within a few minutes.
```

```
# Obtaining training time estimates based on job configurations
python get_training_time_estimate.py
```

```
# Obtaining approximations for how long training is expected to take for in-progress jobs
python get-training-job-progress.py --region us-east-1 --job-name my-training-job --num-dataset-samples 1000
```

Please see [here](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/SageMakerUilts/SageMakerJobsMonitoring/README.md "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/SageMakerUilts/SageMakerJobsMonitoring/README.md") for additional details and examples.
