# FFT

**FFT** (Full Fine-Tuning) updates
_all_ model weights during training. This provides the deepest level
of customization but requires more compute resources and longer training time.

## When to use FFT

- Large domain shifts where the model needs fundamental knowledge
  changes
- You have a large, high-quality dataset (small datasets risk
  catastrophic forgetting)
- You want no adapter overhead at inference time
- Maximum customization depth is required

## Key differences from LoRA

- No `lora_rank`, `lora_alpha`, or
  `merge_weights` parameters
- Adds `max_response_length` parameter for controlling
  generated output length
- Higher compute cost and longer training time
- Larger output artifacts (full model weights)
- Not compatible with
  [continuous customization](customizing-models-continuous.md "customizing-models-continuous.md")

For the full parameter reference including FFT-specific hyperparameters, see each
technique page: [SFT](customizing-models-sft.md "customizing-models-sft.md"),
[DPO](customizing-models-dpo.md "customizing-models-dpo.md"),
[RFT](customizing-models-rft.md "customizing-models-rft.md").
