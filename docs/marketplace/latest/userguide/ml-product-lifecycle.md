

# Machine learning product lifecycle

A machine learning product in AWS Marketplace consists of one or more software versions and associated metadata. Product configuration includes essential properties such as name, description, usage instructions, pricing, categorization, and search keywords. 

## Machine learning product creation process
<a name="ml-publication-process"></a>

 To list a machine learning product in AWS Marketplace, you must complete the following: 

1. [Preparing your product in SageMaker AI](ml-prepare-your-product-in-sagemaker.md)

1. [Listing your machine learning product in AWS Marketplace](ml-publishing-your-product-in-aws-marketplace.md)

 Once you have created your machine learning product, you can edit and manage your product. For more information, see [Managing your machine learning products](ml-product-management.md). 

## Machine learning product status
<a name="ml-product-status"></a>

New products start with Draft visibility while you set them up. After you add the first version, you can move the product to Limited visibility, accessible only to allowlisted accounts and the product creator. After testing and validation, you can publish your product to make it available in the AWS Marketplace catalog for all buyers. Products in AWS Marketplace can have the following status values: 


| Status | Definition | 
| --- |--- |
| Draft | This status indicates an incomplete product for which you're still adding information. Your product has this status when you create it in AWS Partner Central. To move it to Limited, complete **Step 1: Product details** and **Step 2: Delivery configuration**, and then choose **Advance to procurement configuration**. | 
| Limited | Your product has this status after you choose Advance to procurement configuration, and then choose Confirm and continue in the Transition to Limited dialog box. The product has a detail page that only your account and allowlisted accounts can access. You can test your product through this detail page. | 
| Public | Buyers can find and subscribe to your product. To publish a Limited product, choose Publish, and then choose Submit for review. You can also use Edit visibility. AWS Marketplace reviews the product, which usually takes 3 to 5 business days, and then the product moves to Public. For more information, see [Updating product visibility](ml-update-visibility.md). For information about AWS guidelines, see [Requirements and best practices for creating machine learning products](ml-listing-requirements-and-best-practices.md).  | 
| Restricted | New buyers can't find or subscribe to your product. Existing subscribers keep access, but they can't renew contracts from private offers. To restrict a product, choose **Edit visibility**, and then choose **Restricted**. For more information, see [Updating product visibility](ml-update-visibility.md). | 

 For more information or support, contact the AWS Marketplace support team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console. 