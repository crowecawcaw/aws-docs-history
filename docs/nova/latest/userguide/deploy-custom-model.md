

# Deploy a custom model for on-demand inference
<a name="deploy-custom-model"></a>

After you successfully create a custom model with a model customization job (fine-tuning, distillation, or continued pre-training), you can set up on-demand inference for the model.

To set up on-demand inference for a custom model, you deploy the model with a custom model deployment. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the `modelId` parameter in your `InvokeModel` or `Converse` API operations. You can use the deployed model for on-demand inference with Amazon Bedrock features such as playgrounds, Agents, and Knowledge Bases. 

**Topics**
+ [Supported models](#custom-model-inference-supported-models)
+ [Deploy a custom model](deploying-custom-model.md)
+ [Use a deployment for on-demand inference](use-custom-model-on-demand.md)
+ [Delete a custom model deployment](delete-custom-model-deployment.md)

## Supported models
<a name="custom-model-inference-supported-models"></a>

You can set up on-demand inference for the following models:
+ Amazon Nova Canvas
+ Amazon Nova Lite
+ Amazon Nova Micro
+ Amazon Nova Pro