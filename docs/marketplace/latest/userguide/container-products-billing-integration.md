# Container product billing, metering,

and licensing integrations

AWS Marketplace integrates with other AWS services to provide both metering and contract-based
pricing for your container product. For container-based products with usage pricing, you can use
the [AWS Marketplace Metering Service](../../../marketplacemetering/latest/APIReference/Welcome.md "../../../marketplacemetering/latest/APIReference/Welcome.md")
for both checking entitlement to use your product and metering usage for billing. For container-based
products with contract pricing, you can use the AWS License Manager to associate licenses with
your product. The following sections provide more information about hourly and custom metering with AWS Marketplace Metering Service
and contract pricing with AWS License Manager.

###### Topics

- [Hourly and custom metering with
  AWS Marketplace Metering Service](#entitlement-and-metering-for-paid-products "#entitlement-and-metering-for-paid-products")
- [Contract pricing with AWS License Manager](#container-products-contracts-license-manager "#container-products-contracts-license-manager")
- [Configuring hourly metering with
  AWS Marketplace Metering Service](container-metering-registerusage.md "container-metering-registerusage.md")
- [Configuring custom metering for container products with
  AWS Marketplace Metering Service](container-metering-meterusage.md "container-metering-meterusage.md")
- [Contract pricing for container products
  with AWS License Manager](container-license-manager-integration.md "container-license-manager-integration.md")

## Hourly and custom metering with

AWS Marketplace Metering Service

To both check entitlement to use your product and to meter usage for billing, use the [AWS Marketplace
Metering Service](../../../marketplacemetering/latest/APIReference/Welcome.md "../../../marketplacemetering/latest/APIReference/Welcome.md"). If you want to define your own pricing units and meter that usage to
us for billing, integrate by using the [MeterUsage](../../../marketplacemetering/latest/APIReference/API_MeterUsage.md "../../../marketplacemetering/latest/APIReference/API_MeterUsage.md") API operation. If you want to price your product based on number of tasks
or pods used and have AWS meter that usage automatically, integrate by using the [RegisterUsage](../../../marketplacemetering/latest/APIReference/API_RegisterUsage.md "../../../marketplacemetering/latest/APIReference/API_RegisterUsage.md") API operation. For both types of pricing, you can add a long-term
contract price without changing how you integrate with the AWS Marketplace Metering Service.

When you create a new container product in the AWS Marketplace Management Portal, we provide a set of product
identifiers (the product code and public key) that are used to integrate your product with the
AWS Marketplace Metering Service.

### Entitlement

Integrating with the AWS Marketplace Metering Service allows you to verify that the customer running your paid
software is subscribed to your product on AWS Marketplace, guarding you against unauthorized use at
container startup. To verify entitlement, use the [MeterUsage](../../../marketplacemetering/latest/APIReference/API_MeterUsage.md "../../../marketplacemetering/latest/APIReference/API_MeterUsage.md") or [RegisterUsage](../../../marketplacemetering/latest/APIReference/API_RegisterUsage.md "../../../marketplacemetering/latest/APIReference/API_RegisterUsage.md") API operations, depending on your pricing model. For hourly and fixed
monthly pricing models, use the `RegisterUsage` API operation. For custom metering
pricing models, use the `MeterUsage` API operation.

If a buyer isn't entitled to your product, these API operations return the
`CustomerNotEntitledException` exception.

###### Note

If a buyer unsubscribes from your product while running it, they are entitled to
continue running it. However, they can't launch additional containers for your
product.

### Integration guidelines

As you create and publish your container products and use the `MeterUsage` or
`RegisterUsage` API operations for entitlement and metering, keep the following
guidelines in mind:

- Don't configure AWS credentials within your software or the Docker container image.
  AWS credentials for the buyer are automatically obtained at runtime when your container
  image is running within an Amazon ECS task or Amazon EKS pod.
- To call the `MeterUsage` or `RegisterUsage` API operations from
  Amazon EKS, you must [use a supported AWS SDK](../../../eks/latest/userguide/iam-roles-for-service-accounts-minimum-sdk.md "../../../eks/latest/userguide/iam-roles-for-service-accounts-minimum-sdk.md"). To test `MeterUsage` or
  `RegisterUsage` integration of Amazon EKS, you must run an Amazon EKS cluster running
  Kubernetes 1.13.x or greater. Kubernetes 1.13 is required for AWS Identity and Access Management (IAM) roles for
  pod support. IAM roles are required for the running pod to obtain the AWS credentials
  required to invoke these actions on Amazon EKS.
- You can do local development, but you will get a
  `PlatformNotSupportedException` exception. This exception won't occur when
  you launch the container on AWS container services (Amazon ECS, Amazon EKS, and Fargate).

### Supported AWS Regions

For a list of all AWS Marketplace supported AWS Regions, see [Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") on the
Global Infrastructure website.

#### Obtaining the AWS Region for

metering

When integrating your container for metering with either the `MeterUsage` or
`RegisterUsage` API operation, don't configure the AWS SDK to use a specific
AWS Region. The Region must be obtained dynamically at runtime.

###### Example

For example, a customer launches an Amazon ECS task or Amazon EKS pod. The
`RegisterUsage` API operation is called in a Region that differs from the
Region where the Amazon ECS task or Amazon EKS pod was launched. Therefore, the
`RegisterUsage` API operation throws an `InvalidRegionException`
error.

AWS SDK languages don't determine the `AWS_REGION` in a consistent manner.
If your SDK does not automatically pick up the `AWS_REGION`, software needs to be
written manually to determine the `AWS_Region`. For example, the AWS SDK for Java
automatically uses [Amazon EC2 instance
metadata](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") (specifically, `ec2InstanceMetadata`) to obtain the Region
when environment variables or other configuration aren't present. In this instance, only
call `ec2InstanceMetadata` if the `AWS_REGION` environment variable
isn’t present.

For information about how to dynamically obtain an AWS Region at runtime, refer to the
[AWS SDK Developer Guide](https://aws.amazon.com/tools "https://aws.amazon.com/tools") for your programming
language.

### Preventing metering modification

Introducing ways for buyers to modify or override calls to `RegisterUsage` or
`MeterUsage` might result in undesirable billing and payment issues. We strongly
recommend that you integrate the metering and entitlement logic.

When engineering your product to prevent metering modification, keep the following in
mind:

- If buyers can insert new image layers that contain `CMD` or
  `ENTRYPOINT` instructions, directly integrate `RegisterUsage` or
  `MeterUsage` into the software that the buyer is running through your
  container image. Otherwise, calls to `RegisterUsage` or `MeterUsage`
  executed via `CMD` or `ENTRYPOINT` from the base image will likely
  be overridden by the buyer.
- We recommend that you manage the AWS Marketplace product codes that your software uses as input
  to `RegisterUsage` or `MeterUsage` in a manner buyers can't modify.
  However, if your product manages product codes in a manner customers can override, such as
  AWS CloudFormation, Helm chart, or Kubernetes manifest, you must maintain a list of
  _trusted_ AWS Marketplace product codes. This is to ensure that the product
  code your software passes as input to `RegisterUsage` or
  `MeterUsage` is valid.
- If any of your trusted product codes are for free products, ensure that they can’t be
  used in place of a paid product code.

## Contract pricing with AWS License Manager

For container-based products with contract pricing, you use AWS License Manager to associate licenses
with your product.

AWS License Manager is a license management tool that enables your application to
track and update licenses (also known as entitlements) that have been purchased by a customer.
This section provides information about how to integrate your product with
AWS License Manager. After the integration is complete, you can publish your
product listing on AWS Marketplace.

For more information about AWS License Manager, see the [AWS License Manager User Guide](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md") and the [AWS License Manager](../../../cli/latest/reference/license-manager/index.md "../../../cli/latest/reference/license-manager/index.md") section of the _AWS CLI Command
Reference_.

###### Note

- Customers can't launch new instances of the container after the contract expiry
  period. However, during the contract duration, they can launch any number of instances.
  These licenses are not bound to a specific node or instance. Any software running on any
  container on any node can checkout the license as long as it has the assigned AWS
  credentials.
- **Private Offer Creation** – Sellers can generate private
  offers for the products using the Private offer creation tool in the AWS Marketplace Management Portal.

- **Reporting** – You can set up data feeds by setting up an
  Amazon S3 bucket in the **Report** section in the AWS Marketplace Management Portal. For more
  information, see [Seller reports, data feeds, and dashboards in AWS Marketplace](reports-and-data-feed.md "reports-and-data-feed.md").

### Integration workflow

The following steps show the workflow for integrating your container product with
AWS License Manager:

1. Seller creates a product with AWS License Manager integration.
2. Seller lists the product on AWS Marketplace.
3. Buyer finds the product on AWS Marketplace and purchases it.
4. A license is sent to the buyer in their AWS account.
5. Buyer uses the software by launching the Amazon EC2 instance, Amazon ECS task, or Amazon EKS pod
   software. The customer deploys using an IAM role.
6. Software reads the license in the buyer's AWS License Manager account,
   discovers the entitlements purchased, and provisions the features accordingly.

###### Note

License Manager doesn't do any tracking or updates; this is done by the seller’s
application.
