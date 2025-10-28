# Amazon Bedrock templates

The Amazon Bedrock CloudFormation templates provision the AWS resources needed to create
connectors between OpenSearch Service and Amazon Bedrock.

First, the template creates an IAM role that allows the future Lambda function to
access your OpenSearch Service domain. The template then creates the Lambda function, which has the
domain create a connector using the ML Commons plugin. After OpenSearch Service creates the
connector, the remote inference set up is finished and you can run semantic searches
using the Amazon Bedrock API operations.

###### Note

Since Amazon Bedrock hosts its own ML models, you don’t need to deploy a model to
SageMaker Runtime. Instead, the template uses a predetermined endpoint for Amazon Bedrock and
skips the endpoint provision steps.

###### To use the Amazon Bedrock CloudFormation template

1. Open the [Amazon OpenSearch Service
   console](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home ").
2. In the left navigation pane, choose
   **Integrations**.
3. Under **Integrate with Amazon Titan Text Embeddings model through
   Amazon Bedrock**, choose **Configure domain**,
   **Configure public domain**.
4. Follow the prompt to set up your model.

###### Note

OpenSearch Service also provides a separate template to configure an Amazon VPC domain. If you
use this template, you need to provide the Amazon VPC ID for the Lambda
function.

In addition, OpenSearch Service provides the following Amazon Bedrock templates to connect to the Cohere
model and the Amazon Titan Multimodal Embeddings model:

- `Integration with Cohere Embed through Amazon Bedrock`
- `Integrate with Amazon Bedrock Titan Multi-modal`
