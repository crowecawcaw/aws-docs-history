# SFT

Supervised Fine-Tuning trains a model on labeled input-output pairs to align its
behavior with specific examples. The model learns to produce responses that match your
training data.

## When to use

- You have high-quality prompt-response pairs for your target task
- You want the model to learn a specific style, format, or domain knowledge
- You need consistent behavior on well-defined tasks (summarization, classification, Q&A)

## What it achieves

The model learns to mimic the patterns in your training examples, producing outputs
that match the style, format, and content of your labeled data.

## Dataset format

SFT supports two dataset formats. All datasets must be in JSONL format (one JSON
object per line). A `system` message is optional in both formats.

### Format 1: `messages`

Represent the conversation as a list of role-tagged messages. If included, the
`system` message must be the first element.

```
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

### Format 2: `prompt`/`completion`

Provide the input and expected output as separate fields, with an optional
top-level `system` field.

```
{
  "system": "...",
  "prompt": "...",
  "completion": "..."
}
```

###### Note

The `system` message is optional. Ensure diversity in prompts and
response styles.

## Hyperparameters

###### Note

The tables below show the hyperparameters available when you use
[serverless model customization](customize-model.md "customize-model.md"). Other
hyperparameters are preset by Amazon SageMaker AI using optimized defaults. When you use
[SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") or
[HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md"), you can access the
full list of hyperparameters available in the recipes. See the
[SageMaker AI Recipes
repository](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes") to get a recipe and access all hyperparameters.

### SFT LoRA

| Parameter                     | Type    | Required?    | Range / Values                     | Description                                                              |
| ----------------------------- | ------- | ------------ | ---------------------------------- | ------------------------------------------------------------------------ |
| `max_epochs`                  | integer | **Required** | 1–100                              | Number of complete passes through the training dataset.                  |
| `global_batch_size`           | integer | **Required** | 8, 16, 32, 64, 128, 256, 512, 1024 | Total samples processed per optimizer step across all instances.         |
| `learning_rate`               | float   | **Required** | 5e-07–1e-04                        | Step size for weight updates during optimization.                        |
| `lr_scheduler`                | string  | **Required** | cosine, constant                   | Learning rate decay schedule over training.                              |
| `lr_warmup_steps_ratio`       | float   | **Required** | 0–1                                | Fraction of total steps spent ramping learning rate from 0.              |
| `weight_decay`                | float   | **Required** | 0.0–1.0                            | L2 regularization coefficient. Helps prevent overfitting.                |
| `gradient_clipping`           | boolean | **Required** | true, false                        | Scale down gradients if norm exceeds threshold.                          |
| `gradient_clipping_threshold` | float   | **Required** | 0.0–5.0                            | Maximum allowed gradient norm.                                           |
| `dataset_max_len`             | integer | **Required** | 256–131072                         | Maximum sequence length in tokens. Longer sequences are truncated.       |
| `seed`                        | integer | **Required** | 0–2147483647                       | Random seed for reproducibility.                                         |
| `logging_steps`               | integer | **Required** | 1–100                              | Frequency of metric logging in optimizer steps.                          |
| `lora_rank`                   | integer | **Required** | 8, 16, 32, 64, 128                 | Dimensionality of low-rank matrices. Lower = fewer trainable parameters. |
| `lora_dropout`                | float   | **Required** | 0.0–1.0                            | Dropout probability for LoRA adapter layers.                             |
| `lora_alpha`                  | integer | **Required** | 16, 32, 64, 128, 256               | LoRA scaling factor. Effective LR scales as alpha/rank.                  |
| `merge_weights`               | boolean | **Required** | true, false                        | Merge LoRA weights into base model after training.                       |
| `train_val_split_ratio`       | float   | Optional     | 0.0–1.0                            | Fraction allocated to training vs validation.                            |
| `temperature`                 | float   | **Required** | 0.0–2.0                            | Sampling temperature for evaluation.                                     |

### SFT FFT

| Parameter                     | Type    | Required?    | Range / Values                     | Description                                             |
| ----------------------------- | ------- | ------------ | ---------------------------------- | ------------------------------------------------------- |
| `max_epochs`                  | integer | **Required** | 1–100                              | Number of complete passes through the training dataset. |
| `global_batch_size`           | integer | **Required** | 8, 16, 32, 64, 128, 256, 512, 1024 | Total samples processed per optimizer step.             |
| `learning_rate`               | float   | **Required** | 5e-07–1e-04                        | Step size for weight updates.                           |
| `lr_scheduler`                | string  | **Required** | cosine, constant                   | Learning rate decay schedule.                           |
| `lr_warmup_steps_ratio`       | float   | **Required** | 0–1                                | Fraction of steps for LR warmup.                        |
| `weight_decay`                | float   | **Required** | 0.0–1.0                            | L2 regularization coefficient.                          |
| `gradient_clipping`           | boolean | **Required** | true, false                        | Scale down gradients if norm exceeds threshold.         |
| `gradient_clipping_threshold` | float   | **Required** | 0.0–5.0                            | Maximum allowed gradient norm.                          |
| `dataset_max_len`             | integer | **Required** | 256–131072                         | Maximum sequence length in tokens.                      |
| `max_response_length`         | integer | **Required** | 100–200000                         | Maximum tokens for generated response.                  |
| `seed`                        | integer | **Required** | 0–2147483647                       | Random seed for reproducibility.                        |
| `logging_steps`               | integer | **Required** | 1–100                              | Frequency of metric logging.                            |
| `train_val_split_ratio`       | float   | Optional     | 0.0–1.0                            | Fraction allocated to training vs validation.           |
| `temperature`                 | float   | **Required** | 0.0–2.0                            | Sampling temperature for evaluation.                    |
