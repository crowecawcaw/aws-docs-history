# Distilling Amazon Nova models

###### Note

This documentation is for Amazon Nova Version 1. Amazon Nova 2 is now available with new models and enhanced capabilities. For information on how to customize Amazon Nova 2, visit [Customizing Amazon Nova 2 models](../nova2-userguide/customization.md "../nova2-userguide/customization.md").

You can customize the Amazon Nova models using the _distillation_ method
for Amazon Bedrock to transfer knowledge from a larger advanced model (known as
teacher) to a smaller, faster, and cost-efficient model (known as student). This results in a
new customized model that is as performant as the teacher for a specific use-case, and as
cost-efficient as the student model you choose.

Model distillation allows you to fine-tune and improve the performance of more efficient
models when sufficient high quality labeled training data is not available and therefore could
benefit from generating such data from an advanced model. You can choose to do so by
leveraging their prompts without labels or their prompts with low- to medium-quality labels
for a use case that:

- Has particularly tight latency, cost, and accuracy requirements. You can benefit from
  matching the performance on specific tasks of advanced models with smaller models that are
  optimized for cost and latency.
- Needs a custom model that is tuned for a specific set of tasks, but sufficient
  quantity or quality of labeled training data is not available for fine-tuning.
  The distillation method used with Amazon Nova can deliver a custom model that exceeds the
  performance of the teacher model for the specific use case when some labeled prompt-response
  pairs that demonstrate the customer’s expectation is provided to supplement the unlabeled
  prompts.

For step-by-step instructions for model distillation in Amazon Bedrock, see [Customize a model with distillation in Amazon Bedrock](../../../bedrock/latest/userguide/model-distillation.md "../../../bedrock/latest/userguide/model-distillation.md")

## Available models

The following table shows which models you can use for teacher and student
models. If you use a Cross Region Inference Profile, only System Inference Profiles are supported for model distillation.
For more information about Cross-Region inference, see [Increase throughput with cross-Region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md").

| Teacher      | Teacher ID               | Inference profile support | Student                     | Student ID                                                                     | Region                |
| ------------ | ------------------------ | ------------------------- | --------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| Nova Pro     | amazon.nova-pro-v1:0     | Both                      | Nova LiteNova Micro         | amazon.nova-lite-v1:0:300kamazon.nova-micro-v1:0:128k                          | US East (N. Virginia) |
| Nova Premier | amazon.nova-premier-v1:0 | Inference profile only    | Nova LiteNova MicroNova Pro | amazon.nova-lite-v1:0:300kamazon.nova-micro-v1:0:128kamazon.nova-pro-v1:0:300k | US East (N. Virginia) |
