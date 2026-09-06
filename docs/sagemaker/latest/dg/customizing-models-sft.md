

# SFT
<a name="customizing-models-sft"></a>

Supervised Fine-Tuning trains a model on labeled input-output pairs to align its behavior with specific examples. The model learns to produce responses that match your training data.

## When to use
<a name="customizing-models-sft-when-to-use"></a>
+ You have high-quality prompt-response pairs for your target task
+ You want the model to learn a specific style, format, or domain knowledge
+ You need consistent behavior on well-defined tasks (summarization, classification, Q&A)

## What it achieves
<a name="customizing-models-sft-what-it-achieves"></a>

The model learns to mimic the patterns in your training examples, producing outputs that match the style, format, and content of your labeled data.

## Dataset format
<a name="customizing-models-sft-dataset"></a>

SFT supports two dataset formats. All datasets must be in JSONL format (one JSON object per line). A `system` message is optional in both formats.

### Format 1: `messages`
<a name="customizing-models-sft-dataset-format-1"></a>

Represent the conversation as a list of role-tagged messages. If included, the `system` message must be the first element.

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
<a name="customizing-models-sft-dataset-format-2"></a>

Provide the input and expected output as separate fields, with an optional top-level `system` field.

```
{
  "system": "...",
  "prompt": "...",
  "completion": "..."
}
```

**Note**  
The `system` message is optional. Ensure diversity in prompts and response styles.

## Hyperparameters
<a name="customizing-models-sft-hyperparameters"></a>

**Note**  
The tables below show the hyperparameters available when you use [serverless model customization](customize-model.md). Other hyperparameters are preset by Amazon SageMaker AI using optimized defaults. When you use [SageMaker AI Training Jobs](customizing-models-training-jobs.md) or [HyperPod](customizing-models-hyperpod.md), you can access the full list of hyperparameters available in the recipes. See the [SageMaker AI Recipes repository](https://github.com/aws/sagemaker-hyperpod-recipes) to get a recipe and access all hyperparameters.

### SFT LoRA
<a name="customizing-models-sft-lora-hyperparameters"></a>


| Parameter | Type | Required? | Range / Values | Description | 
| --- | --- | --- | --- | --- | 
| max\_epochs | integer | Required | 1–100 | Number of complete passes through the training dataset. | 
| global\_batch\_size | integer | Required | 8, 16, 32, 64, 128, 256, 512, 1024 | Total samples processed per optimizer step across all instances. | 
| learning\_rate | float | Required | 5e-07–1e-04 | Step size for weight updates during optimization. | 
| lr\_scheduler | string | Required | cosine, constant | Learning rate decay schedule over training. | 
| lr\_warmup\_steps\_ratio | float | Required | 0–1 | Fraction of total steps spent ramping learning rate from 0. | 
| weight\_decay | float | Required | 0.0–1.0 | L2 regularization coefficient. Helps prevent overfitting. | 
| gradient\_clipping | boolean | Required | true, false | Scale down gradients if norm exceeds threshold. | 
| gradient\_clipping\_threshold | float | Required | 0.0–5.0 | Maximum allowed gradient norm. | 
| dataset\_max\_len | integer | Required | 256–131072 | Maximum sequence length in tokens. Longer sequences are truncated. | 
| seed | integer | Required | 0–2147483647 | Random seed for reproducibility. | 
| logging\_steps | integer | Required | 1–100 | Frequency of metric logging in optimizer steps. | 
| lora\_rank | integer | Required | 8, 16, 32, 64, 128 | Dimensionality of low-rank matrices. Lower = fewer trainable parameters. | 
| lora\_dropout | float | Required | 0.0–1.0 | Dropout probability for LoRA adapter layers. | 
| lora\_alpha | integer | Required | 16, 32, 64, 128, 256 | LoRA scaling factor. Effective LR scales as alpha/rank. | 
| merge\_weights | boolean | Required | true, false | Merge LoRA weights into base model after training. | 
| train\_val\_split\_ratio | float | Optional | 0.0–1.0 | Fraction allocated to training vs validation. | 
| temperature | float | Required | 0.0–2.0 | Sampling temperature for evaluation. | 

### SFT FFT
<a name="customizing-models-sft-fft-hyperparameters"></a>


| Parameter | Type | Required? | Range / Values | Description | 
| --- | --- | --- | --- | --- | 
| max\_epochs | integer | Required | 1–100 | Number of complete passes through the training dataset. | 
| global\_batch\_size | integer | Required | 8, 16, 32, 64, 128, 256, 512, 1024 | Total samples processed per optimizer step. | 
| learning\_rate | float | Required | 5e-07–1e-04 | Step size for weight updates. | 
| lr\_scheduler | string | Required | cosine, constant | Learning rate decay schedule. | 
| lr\_warmup\_steps\_ratio | float | Required | 0–1 | Fraction of steps for LR warmup. | 
| weight\_decay | float | Required | 0.0–1.0 | L2 regularization coefficient. | 
| gradient\_clipping | boolean | Required | true, false | Scale down gradients if norm exceeds threshold. | 
| gradient\_clipping\_threshold | float | Required | 0.0–5.0 | Maximum allowed gradient norm. | 
| dataset\_max\_len | integer | Required | 256–131072 | Maximum sequence length in tokens. | 
| max\_response\_length | integer | Required | 100–200000 | Maximum tokens for generated response. | 
| seed | integer | Required | 0–2147483647 | Random seed for reproducibility. | 
| logging\_steps | integer | Required | 1–100 | Frequency of metric logging. | 
| train\_val\_split\_ratio | float | Optional | 0.0–1.0 | Fraction allocated to training vs validation. | 
| temperature | float | Required | 0.0–2.0 | Sampling temperature for evaluation. | 