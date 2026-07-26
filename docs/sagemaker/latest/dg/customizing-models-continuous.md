# Continuous customization

With **continuous customization**, you can build on a previously
customized model by applying additional training — either with a
_different technique_ or the _same technique_ with
new data. For example, start with
[SFT](customizing-models-sft.md "customizing-models-sft.md") to teach domain knowledge, then apply
[DPO](customizing-models-dpo.md "customizing-models-dpo.md") to align with user preferences, then
apply [RLVR](customizing-models-rft.md "customizing-models-rft.md") to improve factual accuracy.

###### Important

Continuous customization is different from
[MTRL](model-customize-mtrl.md "model-customize-mtrl.md") (Multi-Turn Reinforcement Learning).
Continuous customization chains training jobs across techniques. MTRL trains agents for
multi-step tool-use tasks within a single training job.

## How it works

- Loads [LoRA](customizing-models-lora.md "customizing-models-lora.md") adapter
  weights from a previous training job
- Resets optimizer, scheduler, and step counter (fresh training with
  new technique or data)
- The previous job's output becomes the starting point for the new
  training run

###### Note

Continuous customization is currently available through the
[MTRL](model-customize-mtrl.md "model-customize-mtrl.md") and continuous customization
workflows using the Python SDK only. It is supported with the
[LoRA](customizing-models-lora.md "customizing-models-lora.md") training type. Continuous
customization across different techniques with
[FFT](customizing-models-fft.md "customizing-models-fft.md") is not supported.

## Supported technique transitions

The following table shows all supported combinations for continuous
customization:

| From technique | To technique     | Supported |
| -------------- | ---------------- | --------- |
| SFT            | DPO              | ✓         |
| SFT            | RLVR             | ✓         |
| SFT            | RLAIF            | ✓         |
| SFT            | SFT (new data)   | ✓         |
| SFT            | MTRL             | ✓         |
| DPO            | DPO (new data)   | ✓         |
| DPO            | RLVR             | ✓         |
| DPO            | RLAIF            | ✓         |
| DPO            | SFT              | ✓         |
| RLVR           | DPO              | ✓         |
| RLVR           | RLVR (new data)  | ✓         |
| RLAIF          | DPO              | ✓         |
| RLAIF          | RLAIF (new data) | ✓         |

## Continuous customization vs resume training

|                     | Continuous customization                                             | Resume training                                                      |
| ------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Technique**       | Different or same technique                                          | Same technique only                                                  |
| **Optimizer state** | Reset (fresh start)                                                  | Restored from checkpoint                                             |
| **Use case**        | Chain techniques (SFT → DPO → RLVR)                                  | Continue interrupted training                                        |
| **Training type**   | [LoRA](customizing-models-lora.md "customizing-models-lora.md") only | [LoRA](customizing-models-lora.md "customizing-models-lora.md") only |

## Getting started

Continuous customization is available through the Python SDK. Provide the output path
of a previous training job as the `resume_from_path` for the next
technique.

```
from sagemaker.modules.train import DPOTrainer

# Continue from a previous SFT job with DPO
trainer = DPOTrainer(
    model_id="meta-textgeneration-llama-3-1-8b-instruct",
    train_data="s3://my-bucket/dpo-preferences.jsonl",
    resume_from_path="s3://my-bucket/previous-sft-output/",
    hyperparameters={
        "max_epochs": 2,
        "learning_rate": 1e-5,
        "lora_rank": 16,
    }
)
trainer.train()
```

## Example workflows

SFT → DPO
Teach domain knowledge first, then align with user
preferences

SFT → RLVR
Teach task format first, then optimize for factual
correctness

SFT → DPO → RLVR
Full pipeline — knowledge → preferences →
accuracy

SFT → MTRL
Teach base capabilities, then train for multi-turn agentic
tasks

DPO → DPO (new data)
Iteratively refine preferences with new feedback
data
