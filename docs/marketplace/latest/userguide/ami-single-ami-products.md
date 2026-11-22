

# Creating AMI-based products

The Amazon Machine Image (AMI) self-service experience guides you as you create your product listing and make change requests. By using the self-service experience, you can update your product listing directly with less time needed for processing by the AWS Marketplace Seller Operations team. Many steps of the self-service experience align with the catalog system in AWS Marketplace, which facilitates direct validation instead of waiting for processing and validation from the AWS Marketplace Seller Operations team. This topic explains how to use the AMI self-service experience to create a product listing for a single AMI. Customers use AMIs to create Amazon EC2 instances with your product already installed and configured. 

**Topics**
+ [Prerequisites](#single-ami-prerequisites)
+ [Understand the self-service experience](#understand-ami-self-service-exp)
+ [Create the listing](#ami-create-product)
+ [Additional resources](#ami-single-create-resources)

## Prerequisites
<a name="single-ami-prerequisites"></a>

Before you create an AMI product listing, you must complete the following prerequisites:

1. You need access to AWS Partner Central. This is the tool that you use to register as a seller and manage the products that you sell on AWS Marketplace. To learn more about getting access to AWS Partner Central, see [Policies and permissions for AWS Marketplace sellers](detailed-management-portal-permissions.md).

1. Register as a seller and, if you want to charge for your products, submit your tax and banking information. To learn more about becoming a seller, see [Getting started as an AWS Marketplace seller](user-guide-for-sellers.md).

1. Have a product that you want to sell. For AMI-based products, this typically means you have created or modified your server software, and created an AMI for your customers to use. To learn more about preparing an AMI for use in AWS Marketplace, see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md). 

## Understand the self-service experience
<a name="understand-ami-self-service-exp"></a>

The self-service experience guides you through creating your product on AWS Marketplace. As you proceed through the steps, you specify product information and AMI deployment settings, such as AWS Region, instance types, and AMI details. You also configure transaction details including the pricing, country availability, EULA, and refund policy. As an option, you can specify an allowlist of AWS account IDs to access and test the product while it is in the **Limited** status. 

You create the product as a draft, and then complete the cards under **Complete your listing** on the product's page. Each card opens a page where you complete and submit one part of your listing. Each submission creates a change request. While the request is in progress, you can't edit that card. For the procedure, see [Create the listing](#ami-create-product).

## Create the listing
<a name="ami-create-product"></a>

The steps in this section explain how to create a listing for an AMI-based product.

**To create an AMI-based product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. Under **Product details**, for **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique. **Catalog** shows the catalog that you create the product in.

1. For **Product type**, choose **Software**.

1. For **Software type**, choose **AMI-based**.

   This type covers standalone AMIs, AMIs with CloudFormation, and EC2 Image Builder components.

1. (Optional) Under **Tags**, add tags to your product.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens its page, which shows **Complete your listing**.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

1. Under **Step 2: Delivery configuration**, complete the **Add Regions**, **Add instance types**, and **Configure version and delivery options** cards, in that order.

   Each card is available after you complete the one before it. For the fields on each card, see [Add an AWS Region](single-ami-regions.md#single-ami-adding-regions), [Adding an instance](single-ami-instance-types.md#single-ami-adding-instance-types), and [Add a new version](single-ami-versions.md#single-ami-adding-version).

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   Your product is now in the **Limited** state, and you can test it with allowlisted accounts.

**To publish an AMI-based product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 3: Procurement configuration** and **Step 4: Testing and integrations**.

1. (Optional) Complete **Step 5: Add-ons**.

1. Test your product, and make sure that it meets the requirements in [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md) and [AMI product checklist for AWS Marketplace](aws-marketplace-listing-checklist.md).

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

For more information about preparing and submitting both your single-AMI product and your product information, see [Additional resources](#ami-single-create-resources).

## Additional resources
<a name="ami-single-create-resources"></a>

For more information about preparing your product information and submitting it for publication, see the following resources:
+ [Preparing your product for AWS Marketplace](product-preparation.md)
+ [Submitting your product for publication on AWS Marketplace](product-submission.md)

For more information about preparing your single-AMI product for submission to AWS Marketplace, see the following resources:
+ [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md)
+ [AMI product checklist for AWS Marketplace](aws-marketplace-listing-checklist.md)
+ [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md)