

# FFT
<a name="customizing-models-fft"></a>

**FFT** (Full Fine-Tuning) updates *all* model weights during training. This provides the deepest level of customization but requires more compute resources and longer training time.

## When to use FFT
<a name="fft-when-to-use"></a>
+ Large domain shifts where the model needs fundamental knowledge changes
+ You have a large, high-quality dataset (small datasets risk catastrophic forgetting)
+ You want no adapter overhead at inference time
+ Maximum customization depth is required

## Key differences from LoRA
<a name="fft-key-differences"></a>
+ No `lora_rank`, `lora_alpha`, or `merge_weights` parameters
+ Adds `max_response_length` parameter for controlling generated output length
+ Higher compute cost and longer training time
+ Larger output artifacts (full model weights)
+ Not compatible with [continuous customization](customizing-models-continuous.md) 

For the full parameter reference including FFT-specific hyperparameters, see each technique page: [SFT](customizing-models-sft.md), [DPO](customizing-models-dpo.md), [RFT](customizing-models-rft.md).

## Dataset compatibility
<a name="fft-dataset-compatibility"></a>

FFT uses the same dataset formats as LoRA for each customization technique. You do not need a separate dataset schema when you switch from LoRA to FFT.
+ SFT FFT uses the same dataset formats described in [Dataset format](customizing-models-sft.md#customizing-models-sft-dataset).
+ DPO FFT uses the same dataset formats described in [Dataset format](customizing-models-dpo.md#customizing-models-dpo-dataset).
+ RLVR FFT uses the same dataset format described in [Dataset format](customizing-models-rft.md#rlvr-dataset-format).
+ RLAIF FFT uses the same dataset format described in [Dataset format](customizing-models-rft.md#rlaif-dataset-format).

The main difference between LoRA and FFT is how weights are updated and which hyperparameters are available, not how you structure your training data.