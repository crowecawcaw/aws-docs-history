

# Creating an initial SaaS product page on AWS Marketplace

You can use your software as a service (SaaS) application metadata to create an initial SaaS product page in the AWS Marketplace catalog, using AWS Partner Central. You can then also add product information, product deployment details, and public offer details. Optionally, you can add accounts to the allowlist to test the product. For more information see the following procedure.

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Central Agents to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

**To create a SaaS product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. Under **Product details**, for **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique.

1. For **Product type**, choose **Software**.

1. For **Software type**, choose **SaaS**.

1. (Optional) Under **Tags**, add tags to your product.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens its page, which shows **Complete your listing**.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

1. Under **Step 2: Delivery configuration**, complete the **Add delivery option** card.

   For more information, see [Adding a SaaS delivery option](#saas-add-delivery-option).

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. When the request succeeds, your product is in the **Limited** state.

While your product is Limited, only your account and the accounts on its allowlist can view it. To see the listing as buyers see it, choose **View on AWS Marketplace** on the product's page. To add accounts to the allowlist, use the **Share with others for testing** card under **Step 4: Testing and integrations**. This step is locked until you complete **Step 3: Procurement configuration**. For more information, see [Update the allowlist of AWS account IDs](saas-product-settings.md#update-allowlist).

Next, complete the remaining steps under **Complete your listing**. To set up pricing in **Step 3: Procurement configuration**, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

## Adding a SaaS delivery option
<a name="saas-add-delivery-option"></a>

After you create your SaaS product in AWS Partner Central, add the fulfillment URL that buyers go to after they subscribe. You must complete the **Add delivery option** card to finish **Step 2: Delivery configuration**.

Your fulfillment URL must authenticate buyers, create their accounts, provision resources, and control access. For more information, see [Onboarding customers to your SaaS product through AWS Marketplace](saas-product-customer-setup.md).

**To add a SaaS delivery option**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 2: Delivery configuration**, choose **Start** on the **Add delivery option** card.

1. In the commercial AWS Marketplace catalog, for **Delivery method**, keep **SaaS** selected. In other catalogs, this field doesn't appear.

   To list an API-based AI agent or tool instead, see [Configure fulfillment options](listing-saas-ai-agents.md#step-2-fulfillment-options).

1. Under **Fulfillment options**, for **Fulfillment URL**, enter the URL of the website that buyers go to after they subscribe.

   The URL must start with `https://` and have 8 to 2,048 characters.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Add delivery option**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

If the product already has a SaaS delivery option, change its URL instead. For more information, see [Update the SaaS URL fulfillment option](saas-product-settings.md#update-fulfillment-options).

After you add the delivery option, you can add Quick Launch with the optional **Add Quick Launch** card. Quick Launch is available only in the commercial AWS Marketplace catalog. For more information, see [Configure Quick Launch](saas-product-settings.md#saas-quick-launch).