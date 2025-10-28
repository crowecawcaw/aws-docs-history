# Best practices for endpoint security

and health with Amazon SageMaker AI

To address the latest security issues, Amazon SageMaker AI automatically patches endpoints to the
latest and most secure software. However, if you incorrectly modify your endpoint
dependencies, Amazon SageMaker AI can't automatically patch your endpoints or replace your
unhealthy instances. To ensure your endpoints remain eligible for automatic updates,
apply the following best practices.

## Don't delete resources while your

endpoints use them

Avoid deleting any of the following resources if you have existing endpoints that
use them:

- The model definition that you create with the [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") action in the Amazon SageMaker API.
- Any model artifacts that you specify for the [`ModelDataUrl`](../APIReference/API_ContainerDefinition.md#sagemaker-Type-ContainerDefinition-ModelDataUrl "../APIReference/API_ContainerDefinition.md#sagemaker-Type-ContainerDefinition-ModelDataUrl") parameter.
- The IAM role and permissions that you specify for the [`ExecutionRoleArn`](../APIReference/API_CreateModel.md#sagemaker-CreateModel-request-ExecutionRoleArn "../APIReference/API_CreateModel.md#sagemaker-CreateModel-request-ExecutionRoleArn") parameter.

###### Reminder

In the model definition that your endpoint uses, ensure that the IAM
role that you specified has the correct permissions. For more
information about the required permissions for Amazon SageMaker AI endpoints, see
[CreateModel API: Execution Role
Permissions](sagemaker-roles.md#sagemaker-roles-createmodel-perms "sagemaker-roles.md#sagemaker-roles-createmodel-perms").

- The inference images that you specify for the [`Image`](../APIReference/API_ContainerDefinition.md#sagemaker-Type-ContainerDefinition-Image "../APIReference/API_ContainerDefinition.md#sagemaker-Type-ContainerDefinition-Image") parameter, if you use your own inference
  code.

###### Reminder

If you use the private registry feature, ensure that Amazon SageMaker AI can
access the private registry as long as you're using the endpoint.

- The Amazon VPC subnets and security groups that you specify for the [`VpcConfig`](../APIReference/API_CreateModel.md#sagemaker-CreateModel-request-VpcConfig "../APIReference/API_CreateModel.md#sagemaker-CreateModel-request-VpcConfig") parameter.
- The endpoint configuration that you create with the [CreateEndpointConfig](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md") action in the Amazon SageMaker API.
- Any KMS keys or Amazon S3 buckets that you specify in the
  endpoint configuration.

###### Reminder

Ensure you don’t disable these KMS keys.

## Follow these procedures to update

your endpoints

When you update your Amazon SageMaker AI endpoints, use any of the following procedures that
apply to your needs.

###### To update your model definition settings

1. Create a new model definition with your updated settings by using the
   CreateModel action in the Amazon SageMaker API.
2. Create a new endpoint configuration that uses the new model definition. To
   do this, use the CreateEndpointConfig action in the Amazon SageMaker API.
3. Update your endpoint with the new endpoint configuration so that your
   updated model definition settings take effect.
4. (Optional) Delete the old endpoint configuration if you're not using it
   with any other endpoints. You can also delete the resources that you
   specified in the model definition if you're not using them with any other
   endpoints. These resources include model artifacts in Amazon S3 and inference
   images.

###### To update your endpoint configuration

1. Create a new endpoint configuration with your updated settings.
2. Update your endpoint with the new configuration so that your updates take
   effect.
3. (Optional) Delete the old endpoint configuration if you're not using it
   with any other endpoints. You can also delete the resources that you
   specified in the model definition if you're not using them with any other
   endpoints. These resources include model artifacts in Amazon S3 and inference
   images.

Whenever you create a new model definition or endpoint configuration, we recommend
that you use a unique name. If you want to update these resources and retain their
original names, use the following procedures.

###### To update your model settings and retain the original model name

1. Delete the existing model definition. At this point, any endpoint that
   uses the model is broken, but you fix this in the following steps.
2. Create the model definition again with your updated settings, and use the
   same model name.
3. Create a new endpoint configuration that uses the updated model
   definition.
4. Update your endpoint with the new endpoint configuration so that your
   updates take effect.

###### To update your endpoint configuration and retain the original configuration

name

1. Delete the existing endpoint configuration.
2. Create a new endpoint configuration with your updated settings, and use
   the original name.
3. Update your endpoint with the new configuration so that your updates take
   effect.
