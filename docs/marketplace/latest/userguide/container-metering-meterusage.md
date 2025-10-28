# Configuring custom metering for container products with

AWS Marketplace Metering Service

###### Note

For Amazon EKS deployments, your software must use [IAM
roles for service accounts (IRSA)](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") to sign the API call for the [`MeterUsage`](../APIReference/API_marketplace-metering_MeterUsage.md "../APIReference/API_marketplace-metering_MeterUsage.md") API operation. Using [EKS Pod
Identity](../../../eks/latest/userguide/pod-identities.md "../../../eks/latest/userguide/pod-identities.md"), the node role, or long-term access keys are not supported.

For Amazon ECS deployments, your software must use [Amazon ECS
task IAM](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") role to sign the API call for the [`MeterUsage`](../APIReference/API_marketplace-metering_MeterUsage.md "../APIReference/API_marketplace-metering_MeterUsage.md") API operation. Using the node role or
long-term access keys are not supported.

For Amazon Bedrock AgentCore Runtime deployments, your software must use the
[AgentCore Runtime execution role](../../../bedrock-agentcore/latest/devguide/runtime-permissions.md#runtime-permissions-execution "../../../bedrock-agentcore/latest/devguide/runtime-permissions.md#runtime-permissions-execution")
to sign the API call for the `MeterUsage` API operation. Long-term access keys are not supported.

AWS Marketplace container products can have custom metering on up to 24 different pricing dimensions
per product. Each dimension can have a long-term contract price associated with it. To enable
custom metering, integrate your container product with AWS Marketplace Metering Service. You can define your own
pricing units and custom metering for that usage to AWS for billing using the [`MeterUsage`](../../../marketplacemetering/latest/APIReference/API_MeterUsage.md "../../../marketplacemetering/latest/APIReference/API_MeterUsage.md") API operation. The following sections show you how to
configure custom metering for your container product.

Price dimensions are defined in two locations, once when creating your product in the
AWS Marketplace Management Portal (seller portal) and once in your software to perform the `MeterUsage`
operation. This two-factor method ensures that the subsequent offers are working as intended
before they're made available to the public.

To set up custom metering, you'll need to choose the usage category, the unit type, and
pricing dimensions:

- Usage category – The usage category helps buyers
  understand what your product is and how to use it.
- Unit type – The unit type defines the unit of
  measure for billing. For example, bandwidth measured in GBps or MBps, the number of hosts,
  or data measured in MB, GB, or TB.
- Pricing dimensions – The pricing dimensions
  represents a feature or service that you've set a per-unit price for (for example, users,
  scans, vCPUs, or deployed agents). Pricing dimensions are public. However, you can still
  define private and Bring Your Own License (BYOL) offers for public products. Don't send
  pricing in the metering records. You meter the quantity of units, and we use that along with
  the prices you defined when creating your product to compute the buyer's bill.

If your product pricing doesn't fit with any of the predefined categories or unit types,
you can choose the generic **Units** category. Then, use the dimension
description to describe what the unit is.
Optionally, you may distribute the usage into allocations by properties that you track. The
allocations are represented as tags to the buyer. These tags allow the buyer to view their costs
split into usage by tag values. For example, if you charge by the user, and users have a
"Department" property, you could create usage allocations with tags that have a key of
"Department", and one allocation per value. This does not change the price, dimensions, or the
total usage that you report, but allows your customer to view their costs by categories
appropriate to your product.

We recommend that you send a metering record every hour. However, you can aggregate usage
over daily or monthly periods as well. If you experience an outage, you can aggregate buyer
software use and send it in the following hours metering. You can't send more than one record
per hour.

For more information about integrating AWS Marketplace Metering Service API for container products with custom
metering pricing, see the [Integrate with
custom metering](https://catalog.workshops.aws/mpseller/en-US/container/integrate-custom "https://catalog.workshops.aws/mpseller/en-US/container/integrate-custom") lab of the _AWS Marketplace seller
workshop_.

###### Important

Free trial and prepaid entitlement are tracked on an hourly level. As a result, sending
these records in separately might lead to the buyer being overcharged.

###### Topics

- [Custom metering prerequisites](#custom-metering-prereqs "#custom-metering-prereqs")
- [Testing MeterUsage
  integration for ECS and EKS](#testing-meterusage-integration "#testing-meterusage-integration")
- [Testing MeterUsage integration for AgentCore](#testing-agentcore-metering "#testing-agentcore-metering")
- [Error handling for
  MeterUsage](#custom-metering-entitlement-error-handling "#custom-metering-entitlement-error-handling")
- [(Optional) Vendor-metered tagging](#container-vendor-metered-tagging "#container-vendor-metered-tagging")
- [Code example](#container-meter-code-example "#container-meter-code-example")
- [Integrating your container product using
  custom metering with the AWS Marketplace Metering Service and AWS SDK for Java](java-integration-example-meterusage.md "java-integration-example-meterusage.md")

## Custom metering prerequisites

Before publishing the product, you must do the following:

1. Create a new container product in the AWS Marketplace Management Portal, and make a note of its product
   code.
2. Use an AWS Identity and Access Management (IAM) role for the task, pod, or AgentCore Runtime endpoint running your application with the
   IAM permissions necessary to call `MeterUsage`. The IAM managed policy
   `AWSMarketplaceMeteringRegisterUsage` has these permissions. For more information about the policy, see
   [AWSMarketplaceMeteringFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md") in the _AWS Managed Policy Reference_.
3. (Optional) We recommend that you enable AWS CloudTrail logging in the task or pod definition
   if you want to see logging.
4. Make a test call to the `MeterUsage` API operation with a record for all of
   the pricing dimensions you define.

## Testing `MeterUsage`

integration for ECS and EKS

Use the `MeterUsage` operation to test your integration before submitting your
image to AWS Marketplace for publishing.

Call `MeterUsage` from the container images by running your product on
Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS) with the AWS account you use to list the product on
AWS Marketplace. Your metering integration must dynamically set the AWS Region, rather than hard
coding it. However, when testing, launch at least one Amazon ECS task or Amazon EKS pod containing your
paid container in the US East (N. Virginia) Region so that the AWS Marketplace operations team can verify
your work with the logs in that Region.

###### Note

- If your product supports both Amazon ECS and Amazon EKS, you only need to launch in Amazon EKS for
  us to validate your integration.
- Test every dimension before launching your product to the public and after adding a
  new dimension. If you don't send a metering record for each dimension associated with a
  container product, it will result in an error with the request failing.

You can't fully test the integration until your product is published with all the required
metadata and pricing information. If requested, the AWS Marketplace catalog operations team can verify
receipt of your metering records.

## Testing MeterUsage integration for AgentCore

Use the `MeterUsage` operation to test your integration before submitting your image to AWS Marketplace for publishing.

Call `MeterUsage` from the container images by running your product on Amazon Bedrock AgentCore with the AWS account you use to list the product on AWS Marketplace. Your
metering integration must dynamically set the AWS Region, rather than hard coding it. However,
when testing, launch at least one Amazon Bedrock AgentCore agent containing your paid
container in the US East (N. Virginia) Region so that the AWS Marketplace operations team can verify
your work with the logs in that Region.

You don’t need to aggregate hourly usage records. Call `MeterUsage` on every
agent invocation with the usage for that invocation.

You must use the latest released version of the AWS SDK for your language. This
automatically populates the `ClientToken` parameter with an auto-generated value to
help with idempotency. Prior releases of the SDK that do not populate this field will not work
for `MeterUsage` calls from within Amazon Bedrock AgentCore. Due to a network issue, you must re-use the
same exact request when retrying. Doing that ensures that the requests are
treated idempotently.

Due to differences in expected metering behavior between Amazon Bedrock AgentCore and other container products, we do not recommend
sharing the same container image for use on Amazon Bedrock AgentCore and on Amazon ECS or EKS.

## Error handling for

`MeterUsage`

Call `MeterUsage` setting the `DryRun` parameter to true at
container startup to validate that metering integration is working. If your container image
integrates with the `MeterUsage` operation and receives an exception other than
`ThrottlingException` at container startup, you should terminate the container to prevent
unauthorized use.

Exceptions other than `ThrottlingException` are thrown only on the initial call
to `MeterUsage`. Subsequent calls from the same Amazon ECS task or Amazon EKS pod or AgentCore Runtime endpoint do not
throw `CustomerNotSubscribedException`, even if the customer unsubscribes while the
task or pod is still running. Those customers are still charged for running containers after
they unsubscribe, and their usage is tracked.

See [MeterUsage](../../../marketplacemetering/latest/APIReference/API_MeterUsage.md "../../../marketplacemetering/latest/APIReference/API_MeterUsage.md") in the
*AWS Marketplace Metering Service API Reference*for detailed descriptions of common
errors for `MeterUsage`. Each AWS SDK programming language has a set of error
handling guidelines that you can refer to for additional information.

## (Optional) Vendor-metered tagging

Vendor-metered tagging helps Independent Software Vendors (ISVs) give the buyer more
granular insight into their software usage and can help them perform cost allocation.

###### Note

Vendor-metered tagging is not supported for metering requests for Amazon Bedrock AgentCore products.

You have several ways to tag a buyer's software usage. One is to first ask your buyers
what they want to see in their cost allocation. Then you can split the usage across properties
that you track for the buyer’s account. Examples of properties include `AccountId`,
`Business Unit`, `Cost Centers`, and other relevant metadata for your
product. These properties are exposed to the buyer as tags. Using tags, buyers can view their
costs split into usage by the tag values in their AWS Billing Console
([https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/")). Vendor-metered tagging doesn't change the price, dimensions,
or the total usage that you report. It allows your customer to view their costs by categories
appropriate to your product.

In a common use case, a buyer subscribes to your product with one AWS account. The buyer
also has numerous users associated with the same product subscription. You can create usage
allocations with tags that have a key of `AccountId`, and then allocate usage to
each user. In this case, buyers can activate the `AccountId` tag in their Billing and Cost Management
console and analyze individual user usage.

### Seller experience

Sellers can aggregate the metering records for resources with the same set of tags
instead of aggregating usage for all resources. For example, sellers can construct the
metering record that includes different `UsageAllocations` buckets. Each
bucket represents the `UsageQuantity` for a set of tags, such as
`AccountId` and `BusinessUnit`.

In the following diagram, **Resource 1** has a unique set of
`AccountId` and `BusinessUnit` tags, and appears in the
**Metering Record** as a single entry.

**Resource 2** and **Resource 3** both have the same
`AccountId` tag, `2222`, and the same `BusinessUnit` tag,
`Operations`. As a result, they're combined into a single
`UsageAllocations` entry in the **Metering Record**.

![Diagram showing how vendor metering tags combine usage data. Three resources (Resource 1, 2, and 3) with different AccountIds and BusinessUnits are consolidated into a single Metering Record with UsageAllocations grouped by AccountId and BusinessUnit before being sent to the AWS Marketplace Metering Service.](../images/seller-vendor-meter-tag.png)

Sellers can also combine resources without tags into a single
`UsageAllocation` with the allocated usage quantity and send it as one of the
entries in `UsageAllocations`.

Limits include:

- Number of tags – 5
- Size of `UsageAllocations` (cardinality) – 2,500

Validations include:

- Characters allowed for the tag key and value – a-zA-Z0-9+ -=.\_:\/@
- Maximum tags across `UsageAllocation` list – 5
- Two `UsageAllocations` can't have the same tags (that is, the same
  combination of tag keys and values). If that's the case, they must use the same
  `UsageAllocation`.
- The sum of `AllocatedUsageQuantity` of `UsageAllocation` must
  equal the `UsageQuantity`, which is the aggregate usage.

### Buyer experience

The following table shows an example of the buyer experience after a buyer activates the
`AccountId` and `BusinessUnit` vendor tags.

In this example, the buyer can see allocated usage in their **Cost Usage
Report**. The vendor-metered tags use the prefix
`“aws:marketplace:isv”`. Buyers can activate them in the Billing and Cost Management, under
**Cost Allocation Tags**, **AWS-generated cost allocation
tags**.

The first and last rows of the **Cost Usage Report** are relevant to
what the Seller sends to the Metering Service (as shown in the [Seller experience](#container-vendor-metered-tag-seller "#container-vendor-metered-tag-seller") example).

| Cost Usage Report (Simplified) | ProductCode  | Buyer                       | UsageDimension | UsageQuantity | `aws:marketplace:isv:AccountId` | `aws:marketplace:isv:BusinessUnit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | ------------ | --------------------------- | -------------- | ------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| xyz                            | 111122223333 | Network: per (GB) inspected | 70             | 2222          | Operations                      |
| xyz                            | 111122223333 | Network: per (GB) inspected | 30             | 3333          | Finance                         |
| xyz                            | 111122223333 | Network: per (GB) inspected | 20             | 4444          | IT                              |
| xyz                            | 111122223333 | Network: per (GB) inspected | 20             | 5555          | Marketing                       |
| xyz                            | 111122223333 | Network: per (GB) inspected | 30             | 1111          | Marketing                       | For a code example, see [MeterUsage code example with usage allocation tagging (Optional)](#container-meterusage-code-example "#container-meterusage-code-example"). ## Code example The following code example is provided to help you integrate your container product with the AWS Marketplace APIs required for publishing and maintaining your product. ### `MeterUsage` code example with usage allocation tagging (Optional) The following code example is relevant for container products with consumption pricing models. The Python example sends a metering record with appropriate usage allocation tags to AWS Marketplace to charge your customers for pay-as-you-go fees. `# NOTE: Your application will need to aggregate usage for the #       customer for the hour and set the quantity as seen below. #       AWS Marketplace can only accept records for up to an hour in the past. # # productCode is supplied after the AWS Marketplace Ops team has # published the product to limited # Import AWS Python SDK import boto3 import time usageRecord = [ { "AllocatedUsageQuantity": 2, "Tags": [ { "Key": "BusinessUnit", "Value": "IT" }, { "Key": "AccountId", "Value": "123456789" }, ] }, { "AllocatedUsageQuantity": 1, "Tags": [ { "Key": "BusinessUnit", "Value": "Finance" }, { "Key": "AccountId", "Value": "987654321" }, ] } ] marketplaceClient = boto3.client("meteringmarketplace") response = marketplaceClient.meter_usage( ProductCode="testProduct", Timestamp=int(time.time()), UsageDimension="Dimension1", UsageQuantity=3, DryRun=False, UsageAllocations=usageRecord )` For more information about `MeterUsage`, see [MeterUsage](../../../marketplacemetering/latest/APIReference/API_MeterUsage.md "../../../marketplacemetering/latest/APIReference/API_MeterUsage.md") in the _AWS Marketplace Metering Service API Reference_. ### Example response `{ "MeteringRecordId": "string" }` |
