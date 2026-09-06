

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Using the AWS Marketplace Metering API
<a name="metering-apis"></a>

This reference provides descriptions of the AWS Marketplace Metering Service API. AWS Marketplace sellers can use this API to submit data for custom usage dimensions. For more information about the necessary permissions to use this API, see [AWS Marketplace metering and entitlement API permissions](https://docs.aws.amazon.com/marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.html) in the *AWS Marketplace Seller Guide.* 

 **Submitting metering records** 

[*MeterUsage*](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_MeterUsage.html) 
+ Submits the metering record for an AWS Marketplace product
+ Called from: Amazon Elastic Compute Cloud (Amazon EC2) instance or a container running on either Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS)
+ Supported product types: Amazon Machine Images (AMIs) and containers
+ Vendor-metered tagging: supported allocation tagging

[*BatchMeterUsage*](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_BatchMeterUsage.html) 
+ Submits the metering record for a set of customers. AWS CloudTrail captures `BatchMeterUsage` API calls. Use CloudTrail to verify that the software as a subscription (SaaS) metering records that you sent are accurate by searching for records using the `eventName` of `BatchMeterUsage`. You can also use CloudTrail to audit records over time. For more information, see [CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html).
+ Called from: SaaS applications
+ Supported product type: SaaS
+ Vendor-metered tagging: supports allocation tagging

 **Accepting new customers** 

[*ResolveCustomer*](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_ResolveCustomer.html) 
+ Resolves the registration token that the buyer submits through the browser during the registration process. Obtains a `CustomerIdentifier` along with the `CustomerAWSAccountId` and `ProductCode`.
+ Called from: SaaS application during the registration process
+ Supported product type: SaaS
+ Vendor-metered tagging: not applicable

 **Entitlement and metering for paid container products**

[*RegisteredUsage*](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_RegisterUsage.html) 
+ Provides software entitlement and metering. Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the `RegisterUsage` operation. Free and Bring Your Own License model (BYOL) products for Amazon ECS or Amazon EKS aren't required to call `RegisterUsage`. However, you can do so if you want to receive usage data in your seller reports. For more information about using the `RegisterUsage` operation, see [Container-based products on AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html).
+ Called from: paid container software products
+ Supported product type: containers
+ Vendor-metered tagging: not applicable