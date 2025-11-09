# On-demand inference on Custom Models

On-demand (OD) inference allows you to run inference on your custom Amazon Nova models without maintaining provisioned throughput endpoints. This helps you optimize costs and scale efficiently. With On-demand inference, you are charged based on usage, measured in tokens, both in and out.

## Compatibility requirements

The following compatibility requirements apply:

- OD inference is supported for Amazon Nova Pro, Lite, and Micro custom understanding models. OD inference is not supported for Nova custom content generation models.
- OD inference is supported for Amazon Nova custom understanding models trained after July 16, 2025. Custom models trained before July 16, 2025 are not compatible with OD inference.
- Amazon Bedrock customization: OD inference is supported for models customized with Amazon Bedrock customization and for student models that were distilled from a teacher model with Amazon Bedrock.
- SageMaker AI customization: For models customized in SageMaker AI, OD inference is supported only for Parameter-efficient fine-tuned (PEFT) models when the model is hosted on Amazon Bedrock. This includes Direct Preference Optimization plus PEFT. OD inference is not supported for Full-rank fine-tuned models.

## Model training and inference

When you train a new custom Amazon Nova Pro, Lite, or Micro model on Amazon Bedrock or SageMaker AI using PEFT after July 16, 2025, the model will automatically be compatible with both provisioned and on-demand inference options. You can select your preferred inference method when you deploy your model.

To use OD inference with a model trained after July 16, 2025, complete the following steps:

1. Create a new fine-tuning job with either the [Amazon Bedrock customization API](customize-fine-tune-bedrock.md "customize-fine-tune-bedrock.md") or the [SageMaker AI customization API](custom-fine-tune-models-sagemaker-tj.md "custom-fine-tune-models-sagemaker-tj.md").
2. Deploy the newly trained model to Amazon Bedrock using the [CreateCustomModel API](../../../bedrock/latest/APIReference/API_CreateCustomModel.md "../../../bedrock/latest/APIReference/API_CreateCustomModel.md").
3. Deploy for on-demand inference using the CustomModelDeployment API.

## Rate limits

The following requests per minute (RPM) and tokens per minute (TPM) limits apply to on-demand inference requests:

| Base Model for Custom Model | RPM per Custom Model Deployment | TPM per Custom Model Deployment |
| --------------------------- | ------------------------------- | ------------------------------- |
| Amazon Nova Micro           | 2,000                           | 4,000,000                       |
| Amazon Nova Lite            | 2,000                           | 4,000,000                       |
| Amazon Nova Pro             | 200                             | 800,000                         |

To learn more about the quotas available for Amazon Nova, see [Quotas for Amazon Nova](quotas.md "quotas.md").

## Latency

You can expect an end-to-end latency difference (that is, Time To First Token (TTFT)) of 20-55% between the base model invocation and the adapter. The exact latency value varies by model size and is in line with industry standards.
