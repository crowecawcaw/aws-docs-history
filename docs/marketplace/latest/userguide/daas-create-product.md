

# Creating a DaaS product in AWS Marketplace

You create a Data as a Service (DaaS) product in AWS Partner Central by choosing the **Data** product type and the **Data as a Service** data type. After you create the product, you complete your listing in four steps: product details, delivery configuration, procurement configuration, and optional add-ons.

## Creating the product
<a name="daas-create-product-create"></a>

Use the following procedure to create the product. The product summary then shows the product type as **Data - DaaS**.

**To create a DaaS product**

1. Open the [Products page in AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/products/), and then choose **Create product**.

1. For **Product name**, enter a unique name. Buyers see this name on your listing page and in AWS Marketplace search results.

1. For **Product type**, choose **Data**. For **Data type**, choose **Data as a Service**. Then choose **Create product**.

1. In the **Product summary** section, copy the product ID, which starts with `prod-`. You use it in later steps.

## Completing your listing
<a name="daas-create-product-listing"></a>

The **Complete your listing** section of your product page shows four steps. Before you start, have your fulfillment URL ready. It must accept the registration token that AWS Marketplace sends, so don't use a link to an existing registration form unless the form can do this. For what your fulfillment URL must do, see [Onboarding customers to your DaaS product through AWS Marketplace](daas-product-customer-setup.md).

**To complete your DaaS listing**

1. Provide your product details. On **Step 1: Product details**, in the **Provide product details** box, choose **Start**. Enter your product description, highlights, support details, and search keywords, and then choose **Submit**. Optionally, in the **Add images and videos** box, choose **Start** and upload media that showcases your product.

   Your product detail page must meet the DaaS publishing requirements. For more information, see [DaaS publishing requirements](daas-publishing-requirements.md).

1. Configure delivery. On **Step 2: Delivery configuration**, choose **Start** on the **Configure fulfillment options** tile, and then enter your **Fulfillment URL**. AWS Marketplace sends subscribed buyers to this URL to complete registration. You can change it later in the **Fulfillment options** section of your product.

   (Optional) Choose **Start** on the **Add usage instructions - optional** tile, and then enter instructions that tell buyers how to start using your product after they subscribe. Buyers see these instructions on the **Set up your account** page.

   Choose **Advance to procurement configuration**.

1. Configure procurement. When you reach **Step 3: Procurement configuration**, your product has the **Limited** status, so only your account and the accounts that you allowlist can open its detail page. For more information, see [DaaS product lifecycle in AWS Marketplace](daas-product-lifecycle.md).

   In this step, you create a public offer, which is the standard price and terms that any buyer can accept through self-service purchase without contacting you. Buyers other than the accounts on your allowlist can subscribe to it only after your product is public. You can also choose to accept private offer requests, if your AWS Partner Central account is eligible for [APN Customer Engagements (ACE)](https://aws.amazon.com/partners/programs/ace/) on the AWS Partner Network website. After you create the public offer, you can't change its pricing model, so choose it carefully. For more information, see [DaaS product pricing in AWS Marketplace](daas-pricing-models.md).

   Choose **Create public offer**, and then complete the offer. For the steps, see [Creating the public offer](#daas-create-product-offer).

1. (Optional) On **Step 4: Add-ons**, add features to your listing. For example, apply for the **Deployed on AWS** badge. The badge tells buyers that your product runs on AWS infrastructure. Products with the badge are easier to find in AWS Marketplace search, and purchases of these products can count toward a buyer's AWS spend commitments.

1. On your product page, in the **Product summary** section, choose **Show more**, and then copy the **Product code**. You use it to confirm that the `ResolveCustomer` response is for your product.

## Creating the public offer
<a name="daas-create-product-offer"></a>

After you choose **Create public offer** in the procurement configuration step, complete the six offer steps.

**To create a public offer for your DaaS product**

1. On **Step 1: Set pricing model and dimensions**, choose your pricing model and dimension unit type, and add your pricing dimensions.

1. On **Step 2: Configure pricing details and duration**, set your prices and contract durations.
**Note**  
For paid pricing models, the price of each dimension defaults to USD $0.001 while your product has the **Limited** status, so that you can test your product without a large bill. You set your actual prices when you request that the product become public.

1. On **Step 3: Specify refund policy**, enter your refund policy.

1. On **Step 4: Configure legal terms and offer documents**, add your legal terms.

1. On **Step 5: Configure offer availability**, choose where the offer is available. You can make it available in all countries, or include or exclude specific countries to meet data licensing, regulatory, or export requirements.

1. On **Step 6: Review and create**, review all details, and then choose **Create offer**.