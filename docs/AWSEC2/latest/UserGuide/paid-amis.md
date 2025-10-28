# Paid AMIs in the AWS Marketplace for Amazon EC2 instances

A _paid AMI_ is an AMI that is listed for sale in the AWS Marketplace. The
AWS Marketplace is an online store where you can buy software that runs on AWS, including AMIs
that you can use to launch your EC2 instance. The AWS Marketplace AMIs are organized into
categories, such as Developer Tools, to enable you to find products to suit your
requirements. For more information about AWS Marketplace, see the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") website.

You can purchase AMIs in the AWS Marketplace from a third party, including AMIs that come with
service contracts from organizations such as Red Hat. You can also create an AMI and sell it
in the AWS Marketplace to other Amazon EC2 users. Building a safe, secure, usable AMI for public
consumption is a fairly straightforward process, if you follow a few simple guidelines. For
information about how to create and use shared AMIs, see [Understand shared AMI usage in Amazon EC2](sharing-amis.md "sharing-amis.md").

Launching an instance from a paid AMI is the same as launching an instance from any other
AMI. No additional parameters are required. The instance is charged according to the rates
set by the owner of the AMI, as well as the standard usage fees for the related web
services, for example, the hourly rate for running an m5.small instance type in Amazon EC2.
Additional taxes might also apply. The owner of the paid AMI can confirm whether a specific
instance was launched using that paid AMI.

###### Important

Amazon DevPay is no longer accepting new sellers or products. AWS Marketplace is now the single, unified
e-commerce platform for selling software and services through AWS. For information about
how to deploy and sell software from AWS Marketplace, see [Selling in AWS
Marketplace](https://aws.amazon.com/marketplace/partners/management-tour "https://aws.amazon.com/marketplace/partners/management-tour"). AWS Marketplace supports AMIs backed by Amazon EBS.

###### Contents

- [Sell your AMI in the AWS Marketplace](#selling-your-ami "#selling-your-ami")
- [Find a paid AMI](using-paid-amis-finding-paid-ami.md "using-paid-amis-finding-paid-ami.md")
- [Purchase a paid AMI in the AWS Marketplace](using-paid-amis-purchasing-paid-ami.md "using-paid-amis-purchasing-paid-ami.md")
- [Retrieve the AWS Marketplace product code from your instance](get-product-code.md "get-product-code.md")
- [Use paid support for supported AWS Marketplace
  offerings](using-paid-amis-support.md "using-paid-amis-support.md")
- [Bills for paid and supported AMIs](#using-paid-amis-bills "#using-paid-amis-bills")
- [Manage your AWS Marketplace
  subscriptions](marketplace-manage-subscriptions.md "marketplace-manage-subscriptions.md")

## Sell your AMI in the AWS Marketplace

You can sell your AMI using AWS Marketplace. AWS Marketplace offers an organized shopping experience.
Additionally, AWS Marketplace also supports AWS features such as Amazon EBS-backed AMIs, Reserved Instances, and Spot Instances.

For information about how to sell your AMI on the AWS Marketplace, see [Selling in AWS
Marketplace](https://aws.amazon.com/marketplace/partners/management-tour "https://aws.amazon.com/marketplace/partners/management-tour").

## Bills for paid and supported AMIs

At the end of each month, you receive an email with the amount your credit card has been
charged for using any paid or supported AMIs during the month. This bill is separate
from your regular Amazon EC2 bill. For more information, see [Paying for
products](../../../marketplace/latest/buyerguide/buyer-paying-for-products.md "../../../marketplace/latest/buyerguide/buyer-paying-for-products.md") in the _AWS Marketplace Buyer Guide_.
