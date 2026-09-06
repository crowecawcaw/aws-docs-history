

# Deploy a Model
<a name="neo-deployment-hosting-services"></a>

To deploy an Amazon SageMaker Neo-compiled model to an HTTPS endpoint, you must configure and create the endpoint for the model using Amazon SageMaker AI hosting services. Currently, developers can use Amazon SageMaker APIs to deploy modules on to ml.c5, ml.c4, ml.m5, ml.m4, ml.p3, ml.p2, and ml.inf1 instances. 

For [Inferentia](https://aws.amazon.com/machine-learning/inferentia/) and [Trainium](https://aws.amazon.com/machine-learning/trainium/) instances, models need to be compiled specifically for those instances. Models compiled for other instance types are not guaranteed to work with Inferentia or Trainium instances.

When you deploy a compiled model, you need to use the same instance for the target that you used for compilation. This creates a SageMaker AI endpoint that you can use to perform inferences. You can deploy a Neo-compiled model using any of the following: [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/), [SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/), and the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

**Note**  
For deploying a model using AWS CLI, the console, or Boto3, see [Neo Inference Container Images](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-deployment-hosting-services-container-images.html) to select the inference image URI for your primary container. 

**Topics**
+ [Prerequisites](neo-deployment-hosting-services-prerequisites.md)
+ [Deploy a Compiled Model Using SageMaker SDK](neo-deployment-hosting-services-sdk.md)
+ [Deploy a Compiled Model Using Boto3](neo-deployment-hosting-services-boto3.md)
+ [Deploy a Compiled Model Using the AWS CLI](neo-deployment-hosting-services-cli.md)
+ [Deploy a Compiled Model Using the Console](neo-deployment-hosting-services-console.md)