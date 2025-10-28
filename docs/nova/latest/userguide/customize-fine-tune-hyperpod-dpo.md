# Direct preference optimization (DPO)

DPO is an advanced technique that fine-tunes models based on human preferences rather than fixed labels. It uses paired examples where humans have indicated which response is better for a given prompt. The model learns to generate outputs that align with these preferences, helping to improve response quality, reduce harmful outputs, and better align with human values. DPO is particularly valuable for refining model behavior after initial SFT.

Both full-rank DPO and low-rank adapter (LoRA) DPO are available.

For detailed instructions about using DPO with Amazon Nova model customization, see the [Direct Preference Optimization (DPO)](../../../sagemaker/latest/dg/nova-dpo.md "../../../sagemaker/latest/dg/nova-dpo.md") section from SageMakeruser guide.
