

# Creating a change request for an AMI-based product in AWS Marketplace

To make changes to a product or version in AWS Marketplace, you submit a **change request** in AWS Partner Central. Change requests are added to a queue and can take from minutes to days to resolve, depending on the type of request. You can see the status of each request on the **Change history** tab of your product. This topic shows how to create a change request for a single-AMI product in AWS Marketplace and how to check its status.

You can create a change request for the following situations:
+ You created a single-AMI product as a draft, but didn't complete all the cards under **Complete your listing** on the product's page. Each card that you submit creates a change request. For the procedure, see [Create the listing](ami-single-ami-products.md#ami-create-product).
+ You want to make modifications to the product information for your product that is in either a **Limited** or **Public** state. To update the information, you create a change request. For more information about the types of changes that you can request for AMI-based products, see [Create a change request by using self-service](#ami-self-service-change-req).

**Note**  
You can also create change requests by using the [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html).

**Topics**
+ [Create a change request by using self-service](#ami-self-service-change-req)
+ [Create a change request](#single-ami-creating-change-request)
+ [Get the status of a change request](#single-ami-getting-change-request-status)
+ [Additional resources](#ami-single-change-req-resources)

## Create a change request by using self-service
<a name="ami-self-service-change-req"></a>

To make modifications to versions or the product information, you create a *change request*. Change requests are the building blocks of a self-service listing that you use to make changes to your product.

You start each change from your product's page:
+ AWS Regions and future Region support – The **Region availability** section of the **Delivery** tab. For more information, see [Managing AMI-based product availability by AWS Region and country](single-ami-regions.md).
+ Instance types – The **Instance type configuration** section of the **Delivery** tab. For more information, see [Adding and restricting AMI instances for AWS Marketplace](single-ami-instance-types.md).
+ Versions – The **Versions** section of the **Delivery** tab. For more information, see [Add a new version](single-ami-versions.md#single-ami-adding-version), [Update version information](single-ami-versions.md#single-ami-updating-version), and [Restrict a version](single-ami-versions.md#single-ami-restricting-version).
+ Product information – The **Product details** tab.
+ Product visibility – **Edit visibility** on your product's page.

**To create a change request**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the action for your change.

   The preceding list shows where each change starts.

1. Enter your changes.

1. Submit the change.

   The button name depends on the change, for example **Save Regions** or **Save**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Create a change request
<a name="single-ami-creating-change-request"></a>

To create a change request, follow the procedure in [Create a change request by using self-service](#ami-self-service-change-req).

For more information about the status of a change request, see [Get the status of a change request](#single-ami-getting-change-request-status). For insight into potential issues with change requests, see [Troubleshooting common errors for change requests on AWS Marketplace](request-errors-and-issues.md).

## Get the status of a change request
<a name="single-ami-getting-change-request-status"></a>

You see the status of each request on the **Change history** tab of your product: **Preparing**, **Applying**, **Succeeded**, **Failed**, or **Cancelled**. To see the details of a request, including the **Failure details** of a failed request, choose its name. To retry a failed request, fix the issues that the failure details describe, and then submit the change again.

## Additional resources
<a name="ami-single-change-req-resources"></a>

For more details about change requests for specific types of updates, see the following resources:
+ [Updating AMI-based product information on AWS Marketplace](single-ami-updating-product.md)
+ [Update version information](single-ami-versions.md#single-ami-updating-version)
+ [Add a new version](single-ami-versions.md#single-ami-adding-version)
+ [Restrict a version](single-ami-versions.md#single-ami-restricting-version)