# Configuring hourly metering with

AWS Marketplace Metering Service

###### Note

For Amazon EKS deployments, your software must use [IAM
roles for service accounts (IRSA)](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") to sign the API call for the [`RegisterUsage`](../APIReference/API_marketplace-metering_RegisterUsage.md "../APIReference/API_marketplace-metering_RegisterUsage.md") API operation. Using [EKS Pod
Identity](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md"), the node role, or long-term access keys are not supported.

For Amazon ECS deployments, your software must use [Amazon ECS
task IAM](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") role to sign the API call for the [`RegisterUsage`](../APIReference/API_marketplace-metering_RegisterUsage.md "../APIReference/API_marketplace-metering_RegisterUsage.md") API operation. Using the node role
or long-term access keys are not supported.

If your container product uses per-hour per-task or per-pod pricing instead of custom
metered pricing dimensions, you don't have to define custom metering dimensions. You can use
AWS Marketplace Metering Service for hourly metering with container products in AWS Marketplace. The following sections show
you how to configure hourly metering with AWS Marketplace Metering Service.

The `RegisterUsage` API operation meters software use per Amazon Elastic Container Service (Amazon ECS) task
or per Amazon Elastic Kubernetes Service (Amazon EKS) pod, per hour, with usage prorated to the second. A minimum of 1 minute
of usage applies to tasks or pods that are short lived. Continuous metering for software use is
automatically handled by the AWS Marketplace Metering Control Plane. Your software isn't
required to perform any metering specific actions except calling `RegisterUsage` once
for metering of software use to commence.

`RegisterUsage` must be called immediately at the time of launching a container.
If you don't register the container in the first 6 hours of the container launch, AWS Marketplace Metering Service
doesn't provide any metering guarantees for previous months. However, the metering will continue
for the current month forward until the container ends.

The AWS Marketplace Metering Control Plane continues to bill customers for running
Amazon ECS tasks and Amazon EKS pods, regardless of the customer's subscription state. This removes the
need for your software to perform entitlement checks after the initial successful launch of the
task or pod.

For more information about integrating AWS Marketplace Metering Service API with container products with hourly
pricing, see the [Integrate with
hourly metering](https://catalog.workshops.aws/mpseller/en-US/container/integrate-hourly "https://catalog.workshops.aws/mpseller/en-US/container/integrate-hourly") lab of the _AWS Marketplace seller workshop_.

###### Topics

- [Hourly metering prerequisites](#hourly-metering-prereqs "#hourly-metering-prereqs")
- [Testing integration for
  RegisterUsage](#testing-integration-for-registerusage "#testing-integration-for-registerusage")
- [Error handling for
  RegisterUsage](#hourly-metering-entitlement-error-handling "#hourly-metering-entitlement-error-handling")
- [Integrating your container product
  with the AWS Marketplace Metering Service using the AWS SDK for Java](java-integration-example-registerusage.md "java-integration-example-registerusage.md")

## Hourly metering prerequisites

Before publishing the product, you must do the following:

1. Create a new container product in the AWS Marketplace Management Portal, and make a note of its product
   code.

For more information, see [Overview: Create a container product](container-product-getting-started.md#create-container-product "container-product-getting-started.md#create-container-product"). 2. Use an AWS Identity and Access Management (IAM) role for the task or pod running your application with the
IAM permissions necessary to call `RegisterUsage`. The IAM managed policy
`AWSMarketplaceMeteringRegisterUsage` has these permissions. For more information about the policy, see
[AWSMarketplaceMeteringFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md") in the _AWS Managed Policy Reference_. 3. (Optional) If you want to see logging, we recommend that you enable AWS CloudTrail logging
in the task or pod definition. 4. Make a test call to the `RegisterUsage` API operation with a record for all
of the pricing dimensions you define.

## Testing integration for

`RegisterUsage`

Use the `RegisterUsage` API operation to test your integration before
submitting your image to AWS Marketplace for publishing.

Call `RegisterUsage` from the container image by running your product on Amazon ECS
or Amazon EKS. Use the AWS account that you're using to list the product on AWS Marketplace. Your metering
integration must dynamically set the AWS Region, rather than hardcoding it. However, when
testing, launch at least one Amazon ECS task or Amazon EKS pod containing your paid container in the
US East (N. Virginia) Region. By doing this, the AWS Marketplace operations team can verify your work with
the logs in that Region.

###### Note

If your product supports both Amazon ECS and Amazon EKS, you only need to launch in Amazon EKS for us
to validate your integration.

You can't fully test the integration until your product is published with all the required
metadata and pricing information. If requested, the AWS Marketplace catalog operations team can verify
receipt of your metering records.

## Error handling for

`RegisterUsage`

If your container image integrates with the AWS Marketplace Metering Service and receives an exception other
than `ThrottlingException` at container startup, you should terminate the container
to prevent unauthorized use.

Exceptions other than `ThrottlingException` are thrown only on the initial call
to the `RegisterUsage` API operation. Subsequent calls from the same Amazon ECS task or
Amazon EKS pod don't throw `CustomerNotSubscribedException` even if the customer
unsubscribes while the task or pod is still running. These customers are still charged for
running containers after they unsubscribe, and their usage is tracked.

The following table describes the errors that the `RegisterUsage` API operation
might throw. Each AWS SDK programming language has a set of error handling guidelines that
you can refer to for additional information.

| **Error**                       | **Description**                                                                                                                                                                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `InternalServiceErrorException` | `RegisterUsage` isn't available.                                                                                                                                                                                                                   |
| `CustomerNotEntitledException`  | The customer doesn't have a valid subscription for the product.                                                                                                                                                                                    |
| `InvalidProductCodeException`   | The `ProductCode` value passed in as part of the request doesn't<br>exist.                                                                                                                                                                         |
| `InvalidPublicKeyException`     | The `PublicKeyVersion` value passed in as part of the request doesn't<br>exist.                                                                                                                                                                    |
| `PlatformNotSupportedException` | AWS Marketplace doesn't support metering usage from the underlying platform. Only Amazon ECS,<br>Amazon EKS, and AWS Fargate are supported.                                                                                                        |
| `ThrottlingException`           | The calls to `RegisterUsage` are throttled.                                                                                                                                                                                                        |
| `InvalidRegionException`        | `RegisterUsage` must be called in the same AWS Region that the Amazon ECS task<br>or Amazon EKS pod was launched in. This prevents a container from choosing a Region (for<br>example, `withRegion(“us-east-1”)`) when calling<br>`RegisterUsage`. |
