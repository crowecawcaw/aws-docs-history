# Deploy a custom model for on-demand inference

After you create a custom model with a model customization job or import a SageMaker AI-trained custom Amazon Nova model, you can
set up on-demand inference for the model. With on-demand inference, you only pay for what you use and you don't need to set up
provisioned compute resources.

To set up on-demand inference for a custom model, you deploy it with a custom model deployment. After
you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the `modelId`
parameter when you submit prompts and generate responses with model inference.

For information about on-demand inference pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing "https://aws.amazon.com/bedrock/pricing").
You can deploy a custom model for on-demand inference in the following Regions (for more information about Regions supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")):

- US East (N. Virginia)
- US West (Oregon)

###### Topics

- [Prerequisites for deploying a custom model for on-demand inference](custom-model-inference-prerequisites.md "custom-model-inference-prerequisites.md")
- [Supported base models](#custom-model-inference-supported-models "#custom-model-inference-supported-models")
- [Deploy a custom model](deploy-custom-model.md "deploy-custom-model.md")
- [Use a deployment for on-demand inference](use-custom-model-on-demand.md "use-custom-model-on-demand.md")
- [Delete a custom model deployment](delete-custom-model-deployment.md "delete-custom-model-deployment.md")

## Supported base models

You can set up on-demand inference for the following base models:

- Amazon Nova Lite
- Amazon Nova Micro
- Amazon Nova Pro
- Meta Llama 3.3 70B Instruct
