The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Using the AWS Marketplace Metering API

This reference provides descriptions of the AWS Marketplace Metering Service
API. AWS Marketplace sellers can use this API to submit data for custom usage
dimensions. For more information about the necessary permissions to use this API, see [AWS Marketplace metering and entitlement API permissions](../userguide/iam-user-policy-for-aws-marketplace-actions.md "../userguide/iam-user-policy-for-aws-marketplace-actions.md") in the
_AWS Marketplace Seller Guide._

**Submitting metering records**

[_MeterUsage_](../APIReference/API_marketplace-metering_MeterUsage.md "../APIReference/API_marketplace-metering_MeterUsage.md")

- Submits the metering record for an AWS Marketplace product
- Called from: Amazon Elastic Compute Cloud (Amazon EC2) instance or a container running on either
  Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS)
- Supported product types: Amazon Machine Images (AMIs) and containers
- Vendor-metered tagging: supported allocation
  tagging
  [_BatchMeterUsage_](../APIReference/API_marketplace-metering_BatchMeterUsage.md "../APIReference/API_marketplace-metering_BatchMeterUsage.md")

- Submits the metering record for a set of customers.
  AWS CloudTrail captures `BatchMeterUsage` API calls. Use CloudTrail to
  verify that the software as a subscription (SaaS) metering records
  that you sent are accurate by searching for records using the
  `eventName` of `BatchMeterUsage`. You can also
  use CloudTrail to audit records over time. For more information, see
  [CloudTrail concepts](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md").
- Called from: SaaS applications
- Supported product type: SaaS
- Vendor-metered tagging: supports allocation tagging

**Accepting new customers**

[_ResolveCustomer_](../APIReference/API_marketplace-metering_ResolveCustomer.md "../APIReference/API_marketplace-metering_ResolveCustomer.md")

- Resolves the registration token that the buyer submits through the browser
  during the registration process. Obtains a `CustomerIdentifier` along
  with the `CustomerAWSAccountId` and `ProductCode`.
- Called from: SaaS application during the registration process
- Supported product type: SaaS
- Vendor-metered tagging: not applicable

**Entitlement and metering for paid container
products**

[_RegisteredUsage_](../APIReference/API_marketplace-metering_RegisterUsage.md "../APIReference/API_marketplace-metering_RegisterUsage.md")

- Provides software entitlement and metering. Paid container software products
  sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the
  `RegisterUsage` operation. Free and Bring Your Own License model
  (BYOL) products for Amazon ECS or Amazon EKS aren't required to call
  `RegisterUsage`. However, you can do so if you want to receive
  usage data in your seller reports. For more information about using the
  `RegisterUsage` operation, see [Container-based products on AWS Marketplace](../userguide/container-based-products.md "../userguide/container-based-products.md").
- Called from: paid container software products
- Supported product type: containers
- Vendor-metered tagging: not applicable
