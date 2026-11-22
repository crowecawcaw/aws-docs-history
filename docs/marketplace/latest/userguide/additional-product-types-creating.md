

# Creating your product

You create an RTB Fabric module product the same way as you would other product types in AWS Marketplace: in AWS Partner Central or with the AWS Marketplace Catalog API. You create an initial product page, configure product settings, set contract pricing, and set up delivery by associating your module in AWS RTB Fabric. This topic covers the create steps and how you deliver the product.

Broadly, the steps are:
+ Create the product in AWS Marketplace.
+ Associate your module in AWS RTB Fabric with the product that you created.
+ Optionally check entitlements with the AWS Marketplace Entitlement Service, if your systems enforce the purchased quantity.
+ Test the product's integration with AWS Marketplace.
+ Submit your product for launch.

The following procedure shows you how to create a product in AWS Marketplace.

**Topics**
+ [Create a product](#additional-product-types-creating-create-product)
+ [Creating an initial product page](#additional-product-types-creating-product)
+ [Private offers](#additional-product-types-creating-private-offers)

## Create a product
<a name="additional-product-types-creating-create-product"></a>

Use the following procedures to create and configure the product, and then to test and launch it.

**To create and configure the product**

1. **Decide to list a product on AWS Marketplace.** Have an RTB Fabric module that you want to sell in AWS Marketplace. Confirm with the AWS RTB Fabric onboarding documentation that your module is ready to be listed.

1. **Determine pricing.** RTB Fabric module products use contract pricing: the buyer pays up front for a term of 1, 12, 24, or 36 months and receives an entitlement for that term. Free trials, private offers with custom terms and durations, flexible payment schedules, and renewals are supported. You define the units that buyers purchase as `Entitled` dimensions on the product.

1. **Collect assets.** Collect the assets needed to submit your product. Assets include the following:
   + Product logo URL (a publicly accessible Amazon S3 URL with a clear image of the product logo)
   + End User License Agreement (EULA) URL (a PDF in an Amazon S3 bucket)
   + Your module in AWS RTB Fabric, which you associate with the product
   + Product information such as the title, description, categories, and keywords, which you provide in AWS Partner Central or with the AWS Marketplace Catalog API
   + Support information (email addresses and URLs for support channels)

1. **Create your product on AWS Marketplace using AWS Partner Central.** Create the product in AWS Partner Central or with the AWS Marketplace Catalog API. In AWS Partner Central, do the following:

   1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page.

   1. Choose **Create product**.

   1. Select **Software**.

   1. Select AWS RTB Fabric. A product has one delivery option, which identifies the AWS service that you are integrating with, and you can't change it after you create the product.

   1. Add your product information.

   1. Add the delivery option with its usage instructions.

   1. Release your product to the `Limited` state. Released products have `Limited` visibility: only your account, and buyer accounts that you add to the product's allowlist, can see and subscribe to them. Use `Limited` visibility to test your integration end to end.

   Your product ID and product code are shown on the product overview page in AWS Partner Central and are available from the Catalog API.
**Note**  
Your product must remain at a reduced price so that you and the AWS Marketplace Seller Operations team can test it without incurring a large cost. We ask you for the product's actual price when you request public visibility.

1. **Create an offer on AWS Marketplace.** A product can have one paid public offer, and can also add a free trial. If you want buyers to request pricing instead of subscribing, release the product without a public offer and turn on **Request private offer**. Interested buyers contact you through the product page, and you send them a private offer.

   1. Create a public offer with your contract pricing, EULA, support terms, and renewal terms.

   1. Release the offer.

**To test and launch the product**

1. **Associate your module in AWS RTB Fabric.** Your solution exists in two places: the listing in AWS Marketplace and the module that buyers use in AWS RTB Fabric. After you release the product to the `Limited` state, link the two: in the AWS RTB Fabric console, register your module and enter your AWS Marketplace product ID. AWS RTB Fabric uses this association to verify a buyer's entitlement before granting access, so complete it before you test a subscription. For more information, see [RTB Fabric module documentation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/discovering-attaching-modules.html).

1. **Check entitlements.** AWS RTB Fabric verifies the buyer's entitlement, so you don't need to build an integration to grant access. To check whether an agreement is a free trial, call `DescribeAgreement` and look for the free trial summary, or call `GetAgreementTerms` and look for a free trial pricing term.

1. **Test your product.** After integration, subscribe to your own product to evaluate the customer experience:
   + Review product information.
   + Examine purchase options.
   + Process test payments.
   + Verify links to your product website.
   + Validate the end-to-end experience with AWS RTB Fabric.

1. **Submit your product for launch.** When you are ready, choose **Update visibility**. You set the product's price, and the AWS Marketplace Seller Operations team reviews your product before visibility can become `Public`.

Next, to keep your systems in sync with AWS Marketplace, you can subscribe to the seller events for agreements created, renewed, amended, cancelled, and ended.

## Creating an initial product page
<a name="additional-product-types-creating-product"></a>

You can use your product metadata to create an initial product page in the AWS Marketplace catalog, using AWS Partner Central. You can then add product information, product usage instructions, and public offer details. Optionally, you add accounts to the allowlist to test the product.

You can use AI-assisted product listing in AWS Partner Central Agents to generate product information from a website URL or uploaded documents. It scores listing quality against AWS Marketplace standards and gives field-level recommendations. For more information, see [AI-assisted product listing](https://docs.aws.amazon.com/marketplace/latest/userguide/ai-assisted-product-listing.html).

**To create the product page**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Create the product:

   1. Choose **Create Product**.

   1. Choose **Software**.

   1. Choose AWS RTB Fabric.

1. Generate a product ID and product code. You can also add optional tags to support tag-based authorization.

1. In **Step 1: Product details**, provide the product details: product title, SKU, short description, long description, product logo URL, highlights, product categories, keywords, product video URL, resources, and support information.

1. In **Step 2: Delivery configuration**, AWS Marketplace redirects you to the AWS RTB Fabric console to associate your module with your AWS Marketplace product ID. For more information, see [RTB Fabric module documentation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/discovering-attaching-modules.html).

   From **Step 2**, you can also add usage instructions. Usage instructions tell customers the next steps to start using your product. They appear on the product detail page before purchase, and they are shown to the buyer again on the fulfillment page after purchase. Provide usage instructions that help the buyer successfully configure and use your product: assume that the reader is interested but uninformed, include all configuration settings and special steps, and be clear and complete.

**To configure procurement and testing**

1. In **Step 3: Procurement configuration**, you define what buyers purchase and how they pay: dimensions, pricing model, and public offer terms. RTB Fabric module products support contract pricing only.

   Create a public offer with contract pricing. Buyers pay up front for a term. Set a price per `Entitled` dimension for a duration of 1, 12, 24, or 36 months.

   Define your dimensions. A dimension is a unit that buyers purchase, for example access to a module. Provide a key, display name, description, and unit. In **Purchasing options**, select the contract duration. For RTB Fabric module products, use a single dimension per contract to avoid confusing the buyer about how purchasing multiple dimensions affects entitlement on AWS RTB Fabric. Add the price per dimension.
**Tip**  
Keep prices low while the product is `Limited` for testing. Set real prices before you request public visibility. Buyers can't see test prices.

   State your refund policy. Choose the Standard Contract for AWS Marketplace or upload your own EULA PDF. Add offer availability, and then review and create the offer.

1. (Optional) Add a free trial of 7 to 90 days on one or more `Entitled` dimensions. The trial is a separate public offer alongside your paid offer. A buyer who starts a trial receives an ordinary entitlement that expires at the end of the trial.

1. (Optional) Choose a leads-only listing. If you negotiate every deal, don't create a paid public offer. In **Step 3: Procurement configuration**, turn on **Request private offer**. Buyers see the request button instead of subscribe, and you send each buyer a private offer. You can still publish a free trial offer on a leads-only listing. **Request private offer** requires AWS Customer Engagement (ACE) eligibility.

1. In **Step 4: Testing and integrations**, use the **Share with others for testing** card to add test accounts to the allowlist. While the product is `Limited`, only your account can see it. Add the AWS account IDs of your test buyers so that they can view and subscribe to the product. While the product is `Limited`, to see the listing as buyers see it, choose **View on AWS Marketplace**.

## Private offers
<a name="additional-product-types-creating-private-offers"></a>

After your public offer is released, you can create private offers for individual buyers with negotiated prices, custom contract durations of up to 144 months, future start dates, flexible payment schedules, and renewals. Private offers inherit your product's dimensions.