# AMI-based products in AWS Marketplace

As an AWS Marketplace seller, you can deliver your products to buyers with [Amazon Machine Images (AMIs)](../../../glossary/latest/reference/glos-chap.md#AmazonMachineImage "../../../glossary/latest/reference/glos-chap.md#AmazonMachineImage"). An AMI
provides the information required to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance. You create a custom
AMI for your product, and buyers can use it to create EC2 instances with your product already
installed and ready to use. This topic provides information about using AMIs to deliver your AWS Marketplace product.

When buyers use the AMI that you provide, they're billed for instances that they create,
following the pricing and metering options that you create for your product. Buyers can use your
product AMI in the same way that they use other AMIs in AWS, including making new custom
versions of the AMI. EC2 instances created from the AMI are still billed as your product, based
on the AMI product code.

## AMI-based product delivery methods

You can deliver AMI-based products in one of the following ways:

- **Single AMI** – Buyers select and use the AMI as
  a template for an EC2 instance. Buyers can find these products using the **Amazon
  Machine Image** delivery method filter. For more information, see [Creating AMI-based products](ami-single-ami-products.md "ami-single-ami-products.md").
- **AWS CloudFormation templates** – You create templates
  that allow buyers to install a system of multiple instances with different roles as a
  single unit. Buyers can find these products using the **CloudFormation**
  delivery method filter. For more information, see [Add CloudFormation templates to your product](cloudformation.md "cloudformation.md").

## Additional resources

For more information about AMI products, see the following topics.

###### AWS Marketplace

- [Product pricing for AWS Marketplace](pricing.md "pricing.md")
- [Configuring custom metering for AMI products with
  AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md "custom-metering-with-mp-metering-service.md")

###### AMI-based products

- [Understanding AMI-based products in AWS Marketplace](ami-getting-started.md "ami-getting-started.md")
- [Creating AMI-based products](ami-single-ami-products.md "ami-single-ami-products.md")
- [Managing AMI-based products as an AWS Marketplace
  seller](concept-chapter-servicename.md "concept-chapter-servicename.md")
- [Add CloudFormation templates to your product](cloudformation.md "cloudformation.md")
- [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md "best-practices-for-building-your-amis.md")
- [AMI product pricing for AWS Marketplace](pricing-ami-products.md "pricing-ami-products.md")
- [Receiving Amazon SNS notifications for AMI products on AWS Marketplace](ami-notification.md "ami-notification.md")
- [AMI product checklist for AWS Marketplace](aws-marketplace-listing-checklist.md "aws-marketplace-listing-checklist.md")
- [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md")
