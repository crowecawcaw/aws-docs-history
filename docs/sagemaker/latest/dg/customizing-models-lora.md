

# LoRA
<a name="customizing-models-lora"></a>

**LoRA** (Low-Rank Adaptation) efficiently adapts large models by training a small set of *low-rank decomposition matrices* rather than all model weights. The base model weights remain frozen — only the adapter weights are learned.

## When to use LoRA
<a name="lora-when-to-use"></a>
+ Most use cases — LoRA achieves near-FFT quality with significantly lower cost
+ You want faster training and lower compute spend
+ You need to chain techniques using [continuous customization](customizing-models-continuous.md) (LoRA required)
+ You want smaller output artifacts (adapter weights only)
+ You want to serve multiple task-specific adapters from a single base model — unfused adapters can be swapped at inference time, so one base model can be reused with many bespoke tuned adapters

**Note**  
Although the output artifact is small (the adapter weights only), the adapter still requires the base model for inference. Unless you merge the adapter into the base model (see `merge_weights` below), you must load both the base model and the adapter to run the customized model.

## Key parameters
<a name="lora-key-parameters"></a>


| Parameter | Values | Description | 
| --- | --- | --- | 
| lora\_rank | 8, 16, 32, 64, 128 | Dimensionality of low-rank matrices. Higher rank = more capacity but more compute. Start with 16. | 
| lora\_alpha | 16, 32, 64, 128, 256 | Scaling factor. Effective learning rate scales as alpha/rank. Typically set to 2x the rank. | 
| lora\_dropout | 0.0–1.0 | Dropout probability for LoRA adapter layers. Helps prevent overfitting. | 
| merge\_weights | true, false | Whether to merge adapter weights back into the base model after training. Set to true for deployment without adapter overhead. | 

For the full parameter reference including LoRA-specific hyperparameters, see each technique page: [SFT](customizing-models-sft.md), [DPO](customizing-models-dpo.md), [RFT](customizing-models-rft.md).