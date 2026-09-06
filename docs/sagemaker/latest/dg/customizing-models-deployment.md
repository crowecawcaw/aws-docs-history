

# Deploying customized models
<a name="customizing-models-deployment"></a>

After customizing and evaluating your model, deploy it for inference. The deployment path depends on the model type. For end-to-end serverless deployment workflows (including one-click deploy from **Studio UI**), see [Serverless model customization](customize-model.md).

## Amazon Nova models
<a name="deployment-nova"></a>

Customized Amazon Nova models deploy to Amazon Bedrock. After your training job completes, the model is registered in SageMaker AI Model Registry and can be deployed as a Bedrock imported model.

For deployment instructions, see [Importing custom models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import.html).

## Open weight models (OSS)
<a name="deployment-oss"></a>

Customized open weight models deploy to SageMaker AI Inference endpoints.

### Studio UI
<a name="deployment-oss-studio-ui"></a>

Navigate to Models → My models → select your logged model → Deploy.