# Amazon SageMaker templates

The Amazon SageMaker CloudFormation templates define multiple AWS resources in order to
set up the neural plugin and semantic search for you.

Begin by using the **Integration with text embedding models through
Amazon SageMaker** template to deploy a text embedding model in SageMaker Runtime
as a server. If you don't provide a model endpoint, CloudFormation creates an IAM role
that allows SageMaker Runtime to download model artifacts from Amazon S3 and deploy them to the
server. If you provide an endpoint, CloudFormation creates an IAM role that allows the
Lambda function to access the OpenSearch Service domain or, if the role already exists, updates and
reuses the role. The endpoint serves the remote model that is used for the ML
connector with the ML Commons plugin.

Then, use the **Integration with Sparse Encoders through
Amazon SageMaker** template to create a Lambda function that has your domain
set up remote inference connectors. After the connector is created in OpenSearch Service, the
remote inference can run semantic search using the remote model in SageMaker Runtime. The
template returns the model ID in your domain back to you to so you can start
searching.

###### To use the Amazon SageMaker AI CloudFormation templates

1. Open the [Amazon OpenSearch Service
   console](https://console.aws.amazon.com//aos/home "https://console.aws.amazon.com//aos/home ").
2. In the left navigation pane, choose
   **Integrations**.
3. Under each of the Amazon SageMaker AI templates, choose **Configure
   domain**, **Configure public domain**.
4. Follow the prompt in the CloudFormation console to provision your stack and
   set up a model.

###### Note

OpenSearch Service also provides a separate template to configure VPC domain. If you use
this template, you need to provide the VPC ID for the Lambda function.
