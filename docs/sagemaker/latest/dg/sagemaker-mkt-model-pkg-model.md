# Use a Model Package to Create a

Model

Use a model package to create a deployable model that you can use to get real-time
inferences by creating a hosted endpoint or to run batch transform jobs. You can
create a deployable model from a model package by using the Amazon SageMaker AI console, the
low-level SageMaker API), or the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

###### Topics

- [Use a Model Package to
  Create a Model (Console)](#sagemaker-mkt-model-pkg-model-console "#sagemaker-mkt-model-pkg-model-console")
- [Use a Model Package to
  Create a Model (API)](#sagemaker-mkt-model-pkg-model-api "#sagemaker-mkt-model-pkg-model-api")
- [Use a Model Package to
  Create a Model (Amazon SageMaker Python SDK)](#sagemaker-mkt-model-pkg-model-sdk "#sagemaker-mkt-model-pkg-model-sdk")

## Use a Model Package to

Create a Model (Console)

###### To create a deployable model from a model package (console)

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Model packages**.
3. Choose a model package that you created from the list on the
   **My model packages** tab or choose a model package
   that you subscribed to on the **AWS Marketplace subscriptions**
   tab.
4. Choose **Create model**.
5. For **Model name**, type a name for the model.
6. For **IAM role**, choose an IAM role that has the
   required permissions to call other services on your behalf, or choose
   **Create a new role** to allow SageMaker AI to create a
   role that has the `AmazonSageMakerFullAccess` managed policy
   attached. For information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").
7. For **VPC**, choose a Amazon VPC that you want to allow
   the model to access. For more information, see [Give SageMaker AI Hosted Endpoints Access to Resources in Your
   Amazon VPC](host-vpc.md "host-vpc.md").
8. Leave the default values for **Container input
   options** and **Choose model
   package**.
9. For environment variables, provide the names and values of environment
   variables you want to pass to the model container.
10. For **Tags**, specify one or more tags to manage the
    model. Each tag consists of a key and an optional value. Tag keys must
    be unique per resource.
11. Choose **Create model**.

After you create a deployable model, you can use it to set up an endpoint for
real-time inference or create a batch transform job to get inferences on entire
datasets. For information about hosting endpoints in SageMaker AI, see [Deploy Models for Inference](deploy-model.md "deploy-model.md").

## Use a Model Package to

Create a Model (API)

To use a model package to create a deployable model by using the SageMaker API,
specify the name or the Amazon Resource Name (ARN) of the model package as the
`ModelPackageName` field of the [`ContainerDefinition`](../APIReference/API_ContainerDefinition.md "../APIReference/API_ContainerDefinition.md")
object that you pass to the [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API.

After you create a deployable model, you can use it to set up an endpoint for
real-time inference or create a batch transform job to get inferences on entire
datasets. For information about hosted endpoints in SageMaker AI, see [Deploy Models for Inference](deploy-model.md "deploy-model.md").

## Use a Model Package to

Create a Model ([Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"))

To use a model package to create a deployable model by using the SageMaker AI Python
SDK, initialize a `ModelPackage` object, and pass the Amazon Resource
Name (ARN) of the model package as the `model_package_arn` argument.
For example:

```
from sagemaker import ModelPackage
model = ModelPackage(role='SageMakerRole',
         model_package_arn='training-job-scikit-decision-trees-1542660466-6f92',
         sagemaker_session=sagemaker_session)
```

After you create a deployable model, you can use it to set up an endpoint for
real-time inference or create a batch transform job to get inferences on entire
datasets. For information about hosting endpoints in SageMaker AI, see [Deploy Models for Inference](deploy-model.md "deploy-model.md").
