

# Amazon Bedrock inference
<a name="nova-model-bedrock-inference"></a>

Once you’ve trained and tested your Amazon Nova model, you can deploy it to Amazon Bedrock for production-scale inference. The deployment process involves creating an Amazon Bedrock model with the CreateCustomModel API, exporting your model artifacts to it from a managed Amazon S3 bucket, and then once the model is ACTIVE configuring an endpoint with on-demand or provisioned-throughput inference.

After you create a custom model in SageMaker, you can use the CreateCustomModel API to deploy it to Amazon Bedrock from SageMaker escrow to run inference. You can then use CreateCustomModelDeployment to create an OD inference endpoint or set up provisioned throughput inference for a Parameter Efficient Fine Tuned (PEFT) model. You can set up provisioned throughput inference for a Full Rank custom model.

You can also use the SageMaker Python SDK to deploy customized Amazon Nova models. The SageMaker Python SDK provides a streamlined experience for deploying trained models to Amazon Bedrock On-Demand or SageMaker AI Real-time Inference endpoints. For more information, see [Customizing with SageMaker Python SDK](nova-forge-sdk.md).

For detailed steps to set up Amazon Bedrock inference for a custom model, see [Deploying customized Amazon Nova models to Amazon Bedrock](deploy-custom-model.md).

The following section gives more detail about On-Demand Inference on Custom Models.

## On-demand inference on Custom Models
<a name="custom-fine-tune-odi"></a>

On-demand (OD) inference allows you to run inference on your custom Amazon Nova models without maintaining provisioned throughput endpoints. This helps you optimize costs and scale efficiently. With On-demand inference, you are charged based on usage, measured in tokens, both in and out.

### Compatibility requirements
<a name="custom-fine-tune-odi-compatibility"></a>

The following compatibility requirements apply:
+ OD inference is supported for Amazon Nova Pro, Lite and Micro custom understanding models. OD inference is not supported for Nova custom content generation models.
+ OD inference is supported for Amazon Nova custom understanding models trained after July 16, 2025. Custom models trained before July 16, 2025 are not compatible with OD inference. 
+ Amazon Bedrock customization: OD inference is supported for models customized with Amazon Bedrock customization and for student models that were distilled from a teacher model with Amazon Bedrock.
+ SageMaker AI customization: For models customized in SageMaker AI, OD inference is supported only for Parameter-efficient fine-tuned (PEFT) models when the model is hosted on Amazon Bedrock. This includes Direct Preference Optimization plus PEFT. OD inference is not supported for Full-rank fine-tuned models.

### Model training and inference
<a name="custom-fine-tune-odi-training"></a>

When you train a new custom Amazon Nova Pro, Lite, or Micro model on Amazon Bedrock or SageMaker AI using PEFT after July 16, 2025, the model will automatically be compatible with both provisioned and on-demand inference options. You can select your preferred inference method when you deploy your model.

To use OD inference with a model trained after July 16, 2025, complete the following steps:

1. Create a new fine-tuning job with either the [Amazon Bedrock customization API](https://docs.aws.amazon.com/nova/latest/userguide/customize-fine-tune-bedrock.html) or the [SageMaker AI customization API](https://docs.aws.amazon.com/nova/latest/userguide/custom-fine-tune-models-sagemaker-tj.html).

1. Deploy the newly trained model to Amazon Bedrock using the [CreateCustomModel API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html).

1. Deploy for on-demand inference using the CustomModelDeployment API.

### Rate limits
<a name="custom-fine-tune-odi-limits"></a>

The following requests per minute (RPM) and tokens per minute (TPM) limits apply to on-demand inference requests:


| Base Model for Custom Model | RPM per Custom Model Deployment | TPM per Custom Model Deployment | 
| --- |--- |--- |
| Nova 2 Lite | 2,000 | 4,000,000 | 

To learn more about the quotas available for Amazon Nova, see [Quotas for Amazon Nova](quotas.md).

### Latency
<a name="custom-fine-tune-odi-latency"></a>

You can expect an end-to-end latency difference (that is, Time To First Token (TTFT)) of 20-55% between the base model invocation and the adapter. The exact latency value varies by model size and is in line with industry standards.