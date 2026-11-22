

# AMI-based products in AWS Marketplace

As an AWS Marketplace seller, you can deliver your products to buyers with [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#AmazonMachineImage). An AMI provides the information required to launch an Amazon Elastic Compute Cloud (Amazon EC2) instance. You create a custom AMI for your product, and buyers can use it to create EC2 instances with your product already installed and ready to use. This topic provides information about using AMIs to deliver your AWS Marketplace product.

When buyers use the AMI that you provide, they're billed for instances that they create, following the pricing and metering options that you create for your product. Buyers can use your product AMI in the same way that they use other AMIs in AWS, including making new custom versions of the AMI. EC2 instances created from the AMI are still billed as your product, based on the AMI product code.

## AMI-based product delivery methods
<a name="ami-product-delivery-methods"></a>

You can deliver AMI-based products in the following ways:
+ **Single AMI** – Buyers select and use the AMI as a template for an EC2 instance. Buyers can find these products using the **Amazon Machine Image** delivery method filter. For more information, see [Creating AMI-based products](ami-single-ami-products.md).
+ **AWS CloudFormation templates** – You create templates that allow buyers to install a system of multiple instances with different roles as a single unit. Buyers can find these products using the **CloudFormation** delivery method filter. For more information, see [Add CloudFormation templates to your product](cloudformation.md).
+ **EC2 Image Builder components** – You publish your software as an Image Builder component, and buyers add it to their own image pipelines. For more information, see [EC2 Image Builder component-based products in AWS Marketplace](ec2-ib-component-products.md).

In AWS Partner Central, you create one AMI-based product for all three delivery methods. When you add a version, you can include **AMI (standalone)**, **AMI with CloudFormation**, and **EC2 Image Builder component** delivery options. In the AWS European Sovereign Cloud catalog, only **AMI (standalone)** is available. For more information, see [Add a new version](single-ami-versions.md#single-ami-adding-version).

## Additional resources
<a name="ami-delivery-methods-additional-resources"></a>

For more information about AMI products, see the following topics.

**AWS Marketplace**
+ [Product pricing for AWS Marketplace](pricing.md)
+ [Configuring custom metering for AMI products with AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md)

**AMI-based products**
+ [Understanding AMI-based products in AWS Marketplace](ami-getting-started.md)
+ [Creating AMI-based products](ami-single-ami-products.md)
+ [Managing AMI-based products as an AWS Marketplace seller](concept-chapter-servicename.md)
+ [Add CloudFormation templates to your product](cloudformation.md)
+ [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md)
+ [AMI product pricing for AWS Marketplace](pricing-ami-products.md)
+ [Receiving Amazon SNS notifications for AMI products on AWS Marketplace](ami-notification.md)
+ [AMI product checklist for AWS Marketplace](aws-marketplace-listing-checklist.md)
+ [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md)