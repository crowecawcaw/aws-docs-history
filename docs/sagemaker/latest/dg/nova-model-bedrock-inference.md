# Amazon Bedrock inference

In this topic, you will learn how to deploy a trained Amazon Nova model to Amazon Bedrock for
inference. The purpose of inference is to deploy trained model to Amazon Bedrock for production
use. The deployment process typically involves the steps to use [Amazon Bedrock
APIs](../../../bedrock/latest/APIReference/API_CreateCustomModel.md "../../../bedrock/latest/APIReference/API_CreateCustomModel.md") to create custom model, point to model artifacts in service-managed
Amazon S3 bucket, wait for model to become `ACTIVE`, and configure provisioned
throughput. The output of the process is a deployed model endpoint for application
integration.

For detailed explanation, see [Import a
SageMaker AI-trained Amazon Nova model](../../../bedrock/latest/userguide/import-with-create-custom-model.md "../../../bedrock/latest/userguide/import-with-create-custom-model.md").
