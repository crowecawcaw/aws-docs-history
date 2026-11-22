

# Creating a change request for an EC2 Image Builder product in AWS Marketplace

To make changes to a product or version in AWS Marketplace, you submit a **change request** in AWS Partner Central. Change requests are added to a queue and can take from minutes to days to resolve, depending on the type of request. You can see the status of each request on the **Change history** tab of your product. This topic shows how to create a change request for an EC2 Image Builder product in AWS Marketplace and how to check its status.

You can create a change request for the following situations:
+ You created a product, but you didn't complete all the cards under **Complete your listing** on your product's page. When you complete a card, such as **Provide product details** or **Add Regions**, you create a change request. For the steps, see [EC2 Image Builder component-based products in AWS Marketplace](ec2-ib-component-products.md).
+ You want to make modifications to the product information for your product that is in either a **Limited** or **Public** state. To update the information, you create a change request. For more information about the types of changes that you can request for EC2 Image Builder products, see [Create a change request by using self-service](#ib-self-service-change-req).

**Note**  
You can also create change requests by using the [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html).

**Topics**
+ [Create a change request by using self-service](#ib-self-service-change-req)
+ [Create a change request](#single-ib-creating-change-request)
+ [Get the status of a change request](#single-ib-getting-change-request-status)
+ [Additional resources](#ib-single-change-req-resources)

## Create a change request by using self-service
<a name="ib-self-service-change-req"></a>

To make modifications to versions or the product information, you create a *change request*. Change requests are the building blocks of a self-service listing that you use to make changes to your product.

You start each change from your product's page:
+ AWS Regions and future Region support – The **Region availability** section of the **Delivery** tab. For more information, see [Managing EC2 Image Builder product availability by AWS Region and country](single-ib-regions.md).
+ Instance types – The **Instance type configuration** section of the **Delivery** tab. For more information, see [Adding and restricting Amazon EC2 instances for AWS Marketplace](single-ib-instance-types.md).
+ Versions – The **Versions** section of the **Delivery** tab. For more information, see [Add a new version](single-ib-versions.md#single-ib-adding-version), [Update version information](single-ib-versions.md#single-ib-updating-version), and [Restrict a version](single-ib-versions.md#single-ib-restricting-version).
+ Product information – The **Product details** tab.
+ Product visibility – **Edit visibility** on your product's page.

**To create a change request**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the action for your change.

   The list earlier in this section shows where each change starts.

1. Enter your changes.

1. Submit the change.

   The button name depends on the change, for example **Save Regions** or **Save**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Create a change request
<a name="single-ib-creating-change-request"></a>

To create a change request, follow the procedure in [Create a change request by using self-service](#ib-self-service-change-req).

For more information about the status of a change request, see [Get the status of a change request](#single-ib-getting-change-request-status). For insight into potential issues with change requests, see [Troubleshooting common errors for change requests on AWS Marketplace](request-errors-and-issues.md).

## Get the status of a change request
<a name="single-ib-getting-change-request-status"></a>

You see the status of each request on the **Change history** tab of your product: **Preparing**, **Applying**, **Succeeded**, **Failed**, or **Cancelled**. To see the details of a request, including the **Failure details** of a failed request, choose its name. To retry a failed request, fix the issues that the failure details describe, and then submit the change again.

## Additional resources
<a name="ib-single-change-req-resources"></a>

For more details about change requests for specific types of updates, see the following resources:
+ [Updating EC2 Image Builder product information on AWS Marketplace](single-ib-updating-product.md)