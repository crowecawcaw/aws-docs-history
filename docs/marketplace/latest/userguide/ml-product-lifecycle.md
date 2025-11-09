#

Machine learning product lifecycle

A machine learning product in AWS Marketplace consists of one or more software versions and associated metadata.
Product configuration includes essential properties such as name, description, usage instructions, pricing, categorization, and search keywords.

## Machine learning product creation process

To list a machine learning product in AWS Marketplace, you must complete the following:

1. [Preparing your product in SageMaker AI](ml-prepare-your-product-in-sagemaker.md "ml-prepare-your-product-in-sagemaker.md")
2. [Listing your product in
   AWS Marketplace](ml-publishing-your-product-in-aws-marketplace.md "ml-publishing-your-product-in-aws-marketplace.md")

Once you have created your machine learning product, you can edit and manage your product. For more information, see [Managing your machine learning products](ml-product-management.md "ml-product-management.md").

## Machine learning product status

New products initially have limited visibility, accessible only to allowlisted accounts
and the product creator. After testing and validation, you can publish your product to make it
available in the AWS Marketplace catalog for all buyers. Products in AWS Marketplace can have
the following status values:

| Status     | Definition                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Staging    | This status indicates an incomplete product for which you're still adding<br>information. After you first save and exit the self-service experience, AWS Marketplace creates an<br>unpublished product containing information from the completed steps. From this status,<br>you can continue to add information or modify submitted details.                                                                                  |
| Limited    | A product attains this status after it's submitted to AWS Marketplace and passes all validation<br>checks. At this point, the product has a detail page accessible only to your account and<br>allowlisted entities. You can conduct product testing through this detail page.                                                                                                                                                 |
| Public     | When you're prepared to make your product visible to buyers for subscription, update the<br>product visibility in the console. Once processed, the product transitions from Limited to<br>Public status. For information about AWS guidelines, see [Requirements and best practices for<br>creating machine learning products](ml-listing-requirements-and-best-practices.md "ml-listing-requirements-and-best-practices.md"). |
| Restricted | To prevent new users from subscribing to your product, you can restrict it by<br>updating the visibility settings. A Restricted status allows existing allowlisted users<br>to continue using the product, but it will no longer be visible to the public or<br>available to new users.                                                                                                                                        |

For more information or support, contact the [AWS Marketplace Seller Operations team](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/").
