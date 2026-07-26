# Deploying customized models

After customizing and evaluating your model, deploy it for inference. The deployment
path depends on the model type. For end-to-end serverless deployment workflows
(including one-click deploy from **Studio UI**), see
[Serverless model customization](customize-model.md "customize-model.md").

## Amazon Nova models

Customized Amazon Nova models deploy to Amazon Bedrock. After your training job
completes, the model is registered in SageMaker AI Model Registry and can be deployed
as a Bedrock imported model.

For deployment instructions, see [Importing custom
models in Amazon Bedrock](../../../bedrock/latest/userguide/model-customization-import.md "../../../bedrock/latest/userguide/model-customization-import.md").

## Open weight models (OSS)

Customized open weight models deploy to SageMaker AI Inference endpoints.

### Studio UI

Navigate to Models → My models → select your logged model → Deploy.
