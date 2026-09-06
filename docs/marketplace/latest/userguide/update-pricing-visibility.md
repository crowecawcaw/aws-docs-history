

# Update pricing visibility
<a name="update-pricing-visibility"></a>

**Note**  
The pricing visibility feature is in preview release for AWS Marketplace and is subject to change.

With the pricing visibility feature, you can list products without displaying public pricing. This feature is also known as leads-only listing. Your product remains visible in the catalog, but buyers can't purchase it through a public offer. Instead, interested buyers contact you through the **Request for private offer** button replacing the common **Subscribe** button. You receive an AWS originated opportunity in AWS Customer Engagement (ACE) tool on AWS Partner Central to initiate the deal negotiation process that can become a private offer. Buyers who get a private offer from you can accept and subscribe through the standard workflow.

Use this feature when you need to customize pricing for individual buyers. This feature is also useful for complex pricing that doesn't fit a standard public offer.

## Prerequisites
<a name="update-pricing-visibility-prereqs"></a>

Before you update pricing visibility, make sure that the following requirements are met:
+ **Request for private offer** must be enabled on your listing. To enable it, you must be AWS Customer Engagement (ACE) eligible. You must also link your AWS Partner Central and AWS Marketplace accounts. For more information, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos) and the [APN Customer Engagements program](https://aws.amazon.com/partners/programs/ace/).
+ Your product must be a contract-based SaaS, AMI, or container listing.
+ Your public offer must not have any active subscriptions. If buyers have active subscriptions, you can't remove public pricing. This includes test subscriptions.

## Set up a new product
<a name="update-pricing-visibility-new-product"></a>

Use the following steps to set up a new product with public pricing removed.

**To set up a new product with public pricing removed**

1. Complete the product creation process for your product type. For more information, see [Getting started with SaaS products on AWS Marketplace](saas-getting-started.md), [Understanding AMI-based products in AWS Marketplace](ami-getting-started.md), or [Getting started with container products](container-product-getting-started.md).

1. During listing creation, create a public offer. After you update pricing visibility, buyers can't see this offer.

1. Publish the product listing in **Limited** status.

1. Enable **Request for private offer** on your listing. For instructions, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos).

After you enable **Request for private offer**, proceed to remove public pricing from your listing.

## Remove public pricing from your listing
<a name="update-pricing-visibility-hide"></a>

Use these steps to remove public pricing from a new or existing product listing.

**To remove public pricing from your listing**

1. Open your product overview page.

1. Choose **Request changes**.

1. Choose **Update public offer**, then choose **Update pricing visibility**.

1. For **Product pricing visibility options**, choose **Don't display product pricing for buyers**.

   To re-enable public pricing later, return to this step and choose **Display product pricing for buyers**.
**Required before you continue**  
**Request for private offer** must be active on your listing before you proceed. If you remove public pricing without an active request button, your listing might be removed. For instructions on enabling the button, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos).

1. Choose **Update pricing visibility** to save your changes.

1. After the request succeeds, choose **View on AWS Marketplace** from the product overview page. Verify the updates on your product listing. Test your lead generation workflow to confirm it creates opportunities correctly.

1. When you are ready, choose **Update product visibility** to make your listing available to buyers.

**Note**  
Buyers can't see pricing after you remove public pricing. If the update request to switch product into Public visibility needs a minimum price, increase the test price slightly. Buyers can't see this price because public pricing has been removed.