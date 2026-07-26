# DPO

## Description

Direct Preference Optimization (DPO) aligns a model with human preferences by
training on pairs of chosen (preferred) and rejected (non-preferred) responses to the
same prompt.

### When to use

- You have preference data showing which responses are better
- Improve response quality beyond what SFT achieves
- Model needs to avoid specific undesirable behaviors

### What it achieves

Model learns to prefer generating responses similar to chosen examples and avoid
rejected examples, without requiring a separate reward model.

## Dataset format

DPO requires pairs of chosen (preferred) and rejected (non-preferred) responses for
the same prompt. DPO supports two dataset formats. All datasets must be in JSONL format
(one JSON object per line). A `system` message is optional in both
formats.

### Format 1: `messages`

Provide `chosen` and `rejected` as full message lists. If
included, the `system` message must be the first element and must be the
same in both `chosen` and `rejected`.

```
{
  "chosen": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "rejected": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

### Format 2: `prompt`/`chosen`/`rejected`

Provide the prompt and both responses as separate string fields, with an optional
top-level `system` field.

```
{
  "system": "...",
  "prompt": "...",
  "chosen": "...",
  "rejected": "..."
}
```

### Guidance

- Chosen and rejected responses should differ meaningfully in quality
- Use the same prompt for both chosen and rejected
- The `system` message is optional

## Hyperparameters - DPO LoRA

###### Note

The tables below show the hyperparameters available when you use
[serverless model customization](customize-model.md "customize-model.md"). Other
hyperparameters are preset by Amazon SageMaker AI using optimized defaults. When you use
[SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") or
[HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md"), you can access the
full list of hyperparameters available in the recipes. See the
[SageMaker AI Recipes
repository](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes") to get a recipe and access all hyperparameters.

| Parameter                     | Type    | Required?    | Range / Values       | Description                                                                            |
| ----------------------------- | ------- | ------------ | -------------------- | -------------------------------------------------------------------------------------- |
| `max_epochs`                  | integer | **Required** | 1–100                | Number of complete passes through the training dataset.                                |
| `global_batch_size`           | integer | **Required** | 16, 32, 64, 128      | Total samples processed per optimizer step across all instances.                       |
| `learning_rate`               | float   | **Required** | 5e-07–1e-04          | Step size for weight updates during optimization.                                      |
| `lr_scheduler`                | string  | **Required** | cosine, constant     | Learning rate decay schedule over training.                                            |
| `lr_warmup_steps_ratio`       | float   | **Required** | 0–1                  | Fraction of total steps spent ramping learning rate from 0.                            |
| `weight_decay`                | float   | **Required** | 0.0–1.0              | L2 regularization coefficient. Helps prevent overfitting.                              |
| `gradient_clipping`           | boolean | **Required** | true, false          | Scale down gradients if norm exceeds threshold.                                        |
| `gradient_clipping_threshold` | float   | **Required** | 0.0–5.0              | Maximum allowed gradient norm.                                                         |
| `dataset_max_len`             | integer | **Required** | 256–131072           | Maximum sequence length in tokens. Longer sequences are truncated.                     |
| `seed`                        | integer | **Required** | 0–2147483647         | Random seed for reproducibility.                                                       |
| `logging_steps`               | integer | **Required** | 1–100                | Frequency of metric logging in optimizer steps.                                        |
| `lora_rank`                   | integer | **Required** | 8, 16, 32, 64, 128   | Dimensionality of low-rank matrices. Lower = fewer trainable parameters.               |
| `lora_dropout`                | float   | **Required** | 0.0–1.0              | Dropout probability for LoRA adapter layers.                                           |
| `lora_alpha`                  | integer | **Required** | 16, 32, 64, 128, 256 | LoRA scaling factor. Effective LR scales as alpha/rank.                                |
| `merge_weights`               | boolean | **Required** | true, false          | Merge LoRA weights into base model after training.                                     |
| `train_val_split_ratio`       | float   | Optional     | 0.0–1.0              | Fraction allocated to training vs validation.                                          |
| `temperature`                 | float   | **Required** | 0.0–2.0              | Sampling temperature for evaluation.                                                   |
| `adam_beta`                   | float   | **Required** | 1e-03–0.1            | DPO inverse temperature. Controls how strongly the model enforces preference rankings. |

## Hyperparameters - DPO FFT

| Parameter                     | Type    | Required?    | Range / Values   | Description                                                                            |
| ----------------------------- | ------- | ------------ | ---------------- | -------------------------------------------------------------------------------------- |
| `max_epochs`                  | integer | **Required** | 1–100            | Number of complete passes through the training dataset.                                |
| `global_batch_size`           | integer | **Required** | 16, 32, 64, 128  | Total samples processed per optimizer step.                                            |
| `learning_rate`               | float   | **Required** | 5e-07–1e-04      | Step size for weight updates.                                                          |
| `lr_scheduler`                | string  | **Required** | cosine, constant | Learning rate decay schedule.                                                          |
| `lr_warmup_steps_ratio`       | float   | **Required** | 0–1              | Fraction of steps for LR warmup.                                                       |
| `weight_decay`                | float   | **Required** | 0.0–1.0          | L2 regularization coefficient.                                                         |
| `gradient_clipping`           | boolean | **Required** | true, false      | Scale down gradients if norm exceeds threshold.                                        |
| `gradient_clipping_threshold` | float   | **Required** | 0.0–5.0          | Maximum allowed gradient norm.                                                         |
| `dataset_max_len`             | integer | **Required** | 256–131072       | Maximum sequence length in tokens.                                                     |
| `max_response_length`         | integer | **Required** | 100–200000       | Maximum tokens for generated response.                                                 |
| `seed`                        | integer | **Required** | 0–2147483647     | Random seed for reproducibility.                                                       |
| `logging_steps`               | integer | **Required** | 1–100            | Frequency of metric logging.                                                           |
| `train_val_split_ratio`       | float   | Optional     | 0.0–1.0          | Fraction allocated to training vs validation.                                          |
| `temperature`                 | float   | **Required** | 0.0–2.0          | Sampling temperature for evaluation.                                                   |
| `adam_beta`                   | float   | **Required** | 1e-03–0.1        | DPO inverse temperature. Controls how strongly the model enforces preference rankings. |
