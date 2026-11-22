

# Leads-only listings

With a leads-only listing, you can list a product in AWS Marketplace without displaying public pricing. Your product remains visible in the catalog, but buyers can't purchase it through a public offer. Instead, interested buyers contact you through the **Request for private offer** button, which replaces the **Subscribe** button. You receive an AWS originated opportunity in AWS Partner Central, which you use to start the deal negotiation that can lead to a private offer. Buyers who receive a private offer from you can accept and subscribe through the standard workflow.

Use a leads-only listing when you need to customize pricing for individual buyers, or when your pricing is too complex for a standard public offer.

You can create a leads-only listing in two ways:
+ **Create a new leads-only listing.** You don't need to create a public offer. For more information, see [Create a new leads-only listing](#leads-only-create-new).
+ **Update pricing visibility on an existing product.** You hide the pricing of your existing public offer. For more information, see [Update pricing visibility on an existing product](#leads-only-update-existing).

## Prerequisites
<a name="leads-only-prereqs"></a>

Before you create a leads-only listing, make sure that the following requirements are met:
+ Your listing must allow private offer requests. To allow them, your account must be enrolled in APN Customer Engagements (ACE). You must also link your AWS Partner Central and AWS Marketplace accounts. For more information, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos) and the [APN Customer Engagements program](https://aws.amazon.com/partners/programs/ace/).
+ The following product type and pricing model are supported:
  + **SaaS products:** contract, or contract with consumption pricing
  + **Server products (AMI and container):** contract
  + **RTB Fabric module products:** contract
+ Machine learning products, AWS Data Exchange products, and other product types don't support leads-only listings.

## Create a new leads-only listing
<a name="leads-only-create-new"></a>

When you create a new product, you can make it a leads-only listing without creating a public offer.

**To create a new leads-only listing**

1. Start the product creation process for your product type. For more information, see [Getting started with SaaS products on AWS Marketplace](saas-getting-started.md), [Understanding AMI-based products in AWS Marketplace](ami-getting-started.md), [Getting started with container products](container-product-getting-started.md), or [Getting started with products integrated with AWS services](additional-product-types-getting-started.md).

1. Complete steps 1 and 2 of product creation. Your product moves from **Draft** to **Limited** status.

1. Under **Step 3: Procurement configuration**, on the **Allow private offer requests** card, choose **Enable**.

1. Complete step 4.

1. Using the test private offer from step 4, complete and test your integration. For more information, see seller testing documentation.

1. Choose **Publish**. This submits a visibility update request, which AWS Marketplace reviews before your product becomes public.

After your product is public, buyers see the **Request for private offer** button on your product page, and you receive their requests as leads and opportunities in AWS Partner Central. Test your lead generation workflow to confirm that it creates opportunities correctly.

## Update pricing visibility on an existing product
<a name="leads-only-update-existing"></a>

You can convert an existing product to a leads-only listing by hiding the pricing of its public offer. Your public offer stays in place, but buyers can't see or subscribe to it.

Before you update pricing visibility, make sure that the following requirements are met:
+ **Request for private offer** is enabled on your listing. If you hide public pricing without the request button, your listing might be removed. For instructions, see [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos).
+ Your public offer has no active subscriptions, including test subscriptions. If buyers have active subscriptions, you can't hide public pricing.

**To update pricing visibility on an existing product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. Find your public offer, and choose **View**.

1. From the **Update** menu, choose **Update pricing visibility**.

   This option appears only for a contract-based AMI, container, or SaaS product that has Limited or Public visibility and allows private offer requests.

1. Choose **Don't display product pricing for buyers**.

1. Submit the request.

1. After the request succeeds, choose **View on AWS Marketplace** from your product page and confirm that pricing is hidden. Test your lead generation workflow to confirm that it creates opportunities correctly.

To show public pricing again later, repeat these steps and choose **Display product pricing for buyers**.

## Limitations
<a name="leads-only-limitations"></a>
+ **One pricing model per product.** Each product supports one pricing model. For a new leads-only listing, the dimension type in your test private offer sets it. For example, if your product supports contract private offers and you also want to offer contract with consumption pricing, you must create a separate product for each additional pricing model.

## Related topics
<a name="leads-only-related"></a>
+ [Adding private offer and demo request buttons](creating-private-offer.md#private-offer-requests-demos)