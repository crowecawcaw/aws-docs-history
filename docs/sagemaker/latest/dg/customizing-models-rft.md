# RFT

Reinforcement Fine-Tuning (RFT) uses reinforcement learning to optimize model behavior
based on reward signals rather than explicit input-output examples. Amazon SageMaker AI supports two
RFT variants: RLVR (Reinforcement Learning with Verifiable Rewards) and RLAIF
(Reinforcement Learning from AI Feedback).

## RLVR

RLVR uses a code-based reward function that programmatically verifies whether model
outputs are correct. Best suited for tasks with objectively right or wrong answers.

### When to use

- Your task has verifiable correct answers (math, code, factual questions)
- You can write a scoring function that evaluates response correctness
- You want to improve factual accuracy and reduce hallucinations

### Dataset format

Each record contains a prompt and reward model metadata. The reward function
evaluates model-generated responses during training.

```
{
  "data_source": "openai/gsm8k",
  "prompt": [
    {
      "content": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? Let's think step by step and output the final answer after \"####\".",
      "role": "user"
    }
  ],
  "ability": "math",
  "reward_model": {
    "ground_truth": "72",
    "style": "rule"
  }
}
```

Required fields:

- `prompt` — array of message objects with `role` and `content`
- `reward_model.style` — set to `"rule"` for programmatic verification
- `reward_model.ground_truth` — the correct answer for verification

### Preset reward functions

- `gsm8k` — Grade school math verification
- `prime_code` — Code correctness verification
- `prime_math` — Mathematical reasoning verification

### RLVR LoRA hyperparameters

###### Note

The tables below show the hyperparameters available when you use
[serverless model customization](customize-model.md "customize-model.md"). Other
hyperparameters are preset by Amazon SageMaker AI using optimized defaults. When you use
[SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") or
[HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md"), you can access the
full list of hyperparameters available in the recipes. See the
[SageMaker AI Recipes
repository](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes") to get a recipe and access all hyperparameters.

| Parameter                | Type    | Required?    | Range / Values                  | Description                                                  |
| ------------------------ | ------- | ------------ | ------------------------------- | ------------------------------------------------------------ |
| `preset_reward_function` | string  | **Required** | gsm8k, prime\_code, prime\_math | Preset reward function for verification.                     |
| `learning_rate`          | float   | **Required** | 1e-07–1e-03                     | Step size for weight updates. Set lower for RL (e.g., 1e-5). |
| `lr_warmup_steps_ratio`  | float   | **Required** | 0–1                             | Fraction of steps for LR warmup.                             |
| `max_epochs`             | integer | **Required** | 1–100                           | Number of passes through the dataset.                        |
| `global_batch_size`      | integer | **Required** | 128, 256, 512, 1024             | Total samples per optimizer step.                            |
| `max_prompt_length`      | integer | **Required** | 512–16384                       | Maximum tokens for prompt portion.                           |
| `weight_decay`           | float   | **Required** | 0.0–1.0                         | L2 regularization coefficient.                               |
| `clip_ratio`             | float   | **Required** | 0.1–1.5                         | GRPO clipping parameter. Limits policy change per update.    |
| `kl_loss_coef`           | float   | **Required** | 0–0.1                           | KL divergence penalty weight. Prevents policy drift.         |
| `rollout_n`              | integer | **Required** | 1, 2, 4, 8, 16, 32              | Candidate responses per prompt during rollouts.              |
| `rollout_temperature`    | float   | **Required** | 0.01–2.0                        | Temperature for rollout generation.                          |
| `lora_rank`              | integer | **Required** | 8, 16, 32, 64, 128              | LoRA rank. Dimensionality of low-rank matrices.              |
| `lora_alpha`             | integer | **Required** | 16, 32, 64, 128, 256            | LoRA scaling factor. Effective LR scales as alpha/rank.      |
| `warmup_steps`           | integer | **Required** | -1–100                          | Absolute warmup steps (-1 for auto).                         |
| `min_lr`                 | float   | **Required** | 0.0–1.0                         | Minimum learning rate floor.                                 |
| `clip_ratio_high`        | float   | **Required** | 0.0–0.5                         | Upper clipping threshold.                                    |
| `clip_ratio_low`         | float   | **Required** | 0.0–0.5                         | Lower clipping threshold.                                    |
| `temperature`            | float   | **Required** | 0.0–2.0                         | Sampling temperature for evaluation.                         |
| `use_kl_loss`            | boolean | **Required** | true, false                     | Add KL divergence penalty to loss.                           |
| `train_val_split_ratio`  | float   | Optional     | 0.0–1.0                         | Train/validation split.                                      |

### RLVR FFT hyperparameters

Same parameters as RLVR LoRA without `lora_rank` and
`lora_alpha`.

## RLAIF

RLAIF uses another LLM as a judge to evaluate model responses based on a natural
language reward prompt. Best suited for tasks with subjective quality criteria that
are difficult to evaluate programmatically.

### When to use

- Your quality criteria are subjective (helpfulness, safety, tone)
- You can describe what "good" looks like in natural language
- You want to scale feedback beyond what human annotation can provide

### Dataset format

Each record contains a prompt and reward model metadata. The LLM judge evaluates
model-generated responses during training.

```
{
  "data_source": "WeOpenML/PandaLM",
  "prompt": [
    {
      "role": "user",
      "content": "Below are two responses for a given task...Evaluate the responses and generate a reference answer.\n\n### Instruction:\nCompare the given products..."
    }
  ],
  "ability": "pairwise-judging",
  "reward_model": {
    "style": "llmj",
    "ground_truth": "2\n\n### Reason: Response 2 provides a more detailed comparison..."
  }
}
```

Required fields:

- `prompt` — array of message objects with `role` and `content`
- `reward_model.style` — set to `"llmj"` for LLM-as-judge
- `reward_model.ground_truth` — reference judgment for calibration

### Judge templates

The following preset judge templates are provided in the training container. Select
one using the `judge_prompt_template` hyperparameter.

- `cot.jinja` — Chain-of-thought evaluation
- `evaluate.jinja` — General quality evaluation
- `faithfulness.jinja` — Faithfulness to source material
- `summarize.jinja` — Summarization quality
- `grader.jinja` — Rubric-based grading

### RLAIF LoRA hyperparameters

Same parameters as RLVR LoRA with the following difference:

| Parameter               | Type   | Required? | Range / Values                                                               | Description                                                           |
| ----------------------- | ------ | --------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `judge_prompt_template` | string | Optional  | cot.jinja, evaluate.jinja, faithfulness.jinja, summarize.jinja, grader.jinja | Template for LLM judge evaluation. Replaces `preset_reward_function`. |

### RLAIF FFT hyperparameters

Same parameters as RLAIF LoRA without `lora_rank` and
`lora_alpha`.
