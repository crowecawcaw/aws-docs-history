

# Configuring SaaS product settings in AWS Marketplace

After you [create a software as a service (SaaS) product](saas-create-product.md) in AWS Marketplace, you can modify many of the product settings. The following sections show you how to submit change requests and modify product settings, such as updating pricing details, product visibility, and other settings.

**Topics**
+ [Manage change requests](#create-change-request)
+ [Update product information](#update-product-information)
+ [Update architecture details](#updating-architecture-details)
+ [Update the allowlist of AWS account IDs](#update-allowlist)
+ [Update product visibility](#saas-update-visibility)
+ [Update pricing terms](#saas-update-pricing-terms)
+ [Add pricing dimensions](#saas-add-pricing-dimensions)
+ [Update pricing dimensions](#saas-update-dimension)
+ [Restrict pricing dimensions](#restrict-pricing-dimensions)
+ [Determine how buyers will access your product](#configure-product-access)
+ [Configure Quick Launch](#saas-quick-launch)
+ [Update availability by country](#saas-availability-by-country)
+ [Update the refund policy of a product](#update-refund-policy)
+ [Update the end user license agreement (EULA)](#saas-update-eula)

## Manage change requests
<a name="create-change-request"></a>

In a [self-service listing](saas-create-product.md#saas-creating-self-service), you use a *change request* to make changes to your product. You start a change request from the product tab that holds the setting, and the product's **Change history** tab lists its change requests.

**To create a change request for a SaaS product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the tab that holds the setting that you want to change: **Product details**, **Delivery**, **Procurement**, or **Settings**.

   The sections later in this topic name the tab and action for each setting.

1. Choose the action for the setting, such as **Edit**.

   While a change request is in progress, some actions are unavailable until it completes.

1. Make your changes.

1. Choose the submit button for the page, such as **Submit** or **Save**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

Changes to your public offer, such as pricing terms or the refund policy, appear on the offer's **Requests log** tab instead. To open the offer, choose the link under **Offer ID** in the **Public offer** section of the **Procurement** tab.

While a request's page shows **Under review**, you can cancel the request. Choose **Cancel request**, and then choose **Cancel request** again to confirm.

Change requests that start with an update will load the current details of the project. Then, you can make updates, which overwrite the existing details. Add and restrict request pairs are specifically for updates that are provisioned after each request succeeds. This means existing subscribers can continue to use the product until their subscription or contract ends. However, no new subscribers can be added to a product that is in a **Restricted** status.

## Update product information
<a name="update-product-information"></a>

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Central Agents to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

After you create your product, you might want to change the information associated with it in AWS Marketplace. 

**To update product information**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Product details** tab.

1. In the **Product details** section, choose **Edit**.

   For a new product, you can instead choose **Start** on the **Provide product details** card under **Complete your listing**.

1. On the **Provide product details** page, update the fields that you want to change:
   + **Product title**
   + **SKU**
   + **Product logo**
   + **Short description**
   + **Long description**
   + **Highlights**
   + **Product categories**
   + **Keywords for AWS Marketplace search results**
   + **Learning resources**
   + **Support details**

   To add or change product images and videos, use the **Images and videos** section of the **Product details** tab instead.

1. Choose **Save**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Update architecture details
<a name="updating-architecture-details"></a>

To receive the special designation that your product is deployed on AWS, update your product's architecture details in AWS Partner Central by selecting a hosting pattern and uploading an architecture diagram. For list of hosting patterns that AWS considers deployed on AWS, see [Guidelines](saas-guidelines.md#march-saas-guidelines). 

**To update architecture details**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Architecture details** section, choose **Update architecture details**. If the product has no architecture details yet, choose **Create architecture details**.

   You can instead choose **Start** on the **Apply for Deployed on AWS badge** card on the **Add-ons** tab. These actions are available after your product has Limited visibility.

1. Under **AWS hosting pattern**, for **AWS hosting pattern of your application**, choose a hosting pattern.

   For the patterns that AWS considers deployed on AWS, see [Guidelines](saas-guidelines.md#march-saas-guidelines).

1. If you chose a pattern that is considered deployed on AWS, under **Architecture diagram**, for **File upload**, choose **Choose file**, and upload your diagram.

   The file must be in PNG or JPG format, smaller than 5 MB, and from 780 by 439 pixels to 7,000 by 7,000 pixels. The upload expires after 1 hour, so upload the file again if you retry a failed request. For more information, see [Creating architecture diagrams](saas-guidelines.md#arch-diagram).

1. If the page shows **Application plane**, for **Location of application plane**, choose where your application plane runs.

   For more information about the control plane and the application plane, see [SaaS Architecture Fundamentals](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/saas-architecture-fundamentals.html).

1. Choose **Update architecture details**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Update the allowlist of AWS account IDs
<a name="update-allowlist"></a>

You can change the list of AWS account IDs that can view your product in a limited state. 

**To update the allowlist**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Settings** tab.

1. In the **Allowlisted AWS accounts** section, choose **Edit**. If no accounts are allowlisted yet, choose **Add AWS accounts**.

   For a new product, you can instead choose **Start** on the **Share with others for testing** card under **Complete your listing**. You can't update the allowlist of a product with Restricted visibility.

1. For **Allowlisted AWS accounts**, enter the AWS account IDs, separated by commas.

   Each ID has 12 digits, and you can enter up to 5,000 IDs. AWS Marketplace also adds your AWS account and the AWS accounts listed on the page, so that it can test and preview your product. If you remove these accounts, the release of your product can take longer.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Update product visibility
<a name="saas-update-visibility"></a>

To change which buyers can view and buy your product in AWS Marketplace, update the product visibility. To change who can see your Quick Launch experience, see [Configure Quick Launch](#saas-quick-launch).

**To update product visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

1. In the **Update listing visibility** dialog box, under **Change to**, choose one of the following:
   + **Public**: all AWS Marketplace buyers can view and purchase the product. For a Limited product, this option appears after you complete the required steps under **Complete your listing**.
   + **Restricted**: the product is removed from public visibility. Existing subscribers keep access, but new buyers can't purchase it.

1. (Optional) If you chose **Restricted**, for **Replacement product ID**, enter the ID of the product that existing subscribers move to when their contract ends.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

A request for Public visibility goes through review before your listing goes live. Reviews typically take 3 to 5 business days.

To publish a Limited product, you can instead choose **Publish** under **Complete your listing**, and then choose **Submit for review**. Before you publish, replace any test prices in your public offer with the prices that you want buyers to pay. After your product is public, buyers can purchase at the offer prices. For more information, see [Update pricing terms](#saas-update-pricing-terms).

## Update pricing terms
<a name="saas-update-pricing-terms"></a>

**Note**  
This option isn't available for Agentic Commerce products. The offer uses a fixed rate of USD $1.00 per unit for the `agentic_commerce_default` dimension, and the price of each request comes from the signed quote that your endpoint returns.

To change the pricing per dimension on your SaaS product, use **Update pricing terms**.

**Note**  
A pricing increase for any dimension results in the pricing update option being unavailable for at least the next 90 days. If updating both a price decrease and an increase, update the price decrease first. 

**To update pricing terms**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Update**, and then choose **Update pricing terms**.

   The **Update** menu is available after your public offer is released, and unavailable while another request for the offer is in progress.

1. Enter the new price for each dimension that you want to change.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** in the **Public offer** section of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu in the **Public offer** section is unavailable.

## Add pricing dimensions
<a name="saas-add-pricing-dimensions"></a>

**Note**  
This option isn't available for Agentic Commerce products. AWS Marketplace creates the `agentic_commerce_default` pricing dimension for you and meters it for each verified payment.

You can add a dimension that you want to use to charge your product. A dimension is the foundational unit of measure that your buyer is charged for when using your product.

**Note**  
To update the name or description of an existing pricing dimension, see [Update pricing dimensions](#saas-update-dimension). 

**To add pricing dimensions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Add dimensions**.

   If **Add dimensions** is unavailable, create a public offer first.

1. On the **Add dimensions** step, choose **Add contract dimension** or **Add usage dimension**.

   The button that appears depends on your pricing model.

1. In the panel, enter the **API identifier**, **Display name**, and **Description**, and then choose **Add dimensions**.

   The API identifier can contain only letters, numbers, and underscores, and can't start with a number. The API identifier and display name must be unique across your dimensions. You can't change the API identifier after you create the dimension. To add more than one dimension, choose **Add new dimension** before you choose **Add dimensions**.

1. Choose **Next**, and then choose **Submit** on the **Review and submit** step.

   If your product has a public offer, the **Configure prices** step comes first. Enter the prices for the new dimensions, and then choose **Next**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Update pricing dimensions
<a name="saas-update-dimension"></a>

**Note**  
This option isn't available for Agentic Commerce products. AWS Marketplace creates the `agentic_commerce_default` pricing dimension for you and meters it for each verified payment.

You can update a dimension that you want to use to charge your product. A dimension is the foundational unit of measure that your buyer is charged for when using your product.

**To update pricing dimensions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Update dimensions**.

1. On the **Update dimension information** page, in the **Pricing dimensions** table, select the dimension, and then choose **Update**.

1. In the **Update pricing dimension** panel, change the **Display name** or **Description**, and then choose **Update dimension**.

   The display name can have 1 to 80 characters and can't start with a space. You can't change the API identifier, and the change doesn't affect prices.

1. At the bottom of the page, choose **Update**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

## Restrict pricing dimensions
<a name="restrict-pricing-dimensions"></a>

**Note**  
For an Agentic Commerce product, AWS Marketplace creates the `agentic_commerce_default` pricing dimension for you and meters it for each verified payment. An Agentic Commerce offer supports only that dimension. If the product has any other pricing dimensions, such as dimensions that you added through the Catalog API, restrict them before you create a public offer.

You can restrict a dimension that is currently listed in the product. This request removes the selected dimension from the product. 

**To restrict pricing dimensions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Pricing dimensions** section, choose **Update**, and then choose **Restrict dimensions**.

   A support case form for the AWS Marketplace Seller Operations team opens, with your product ID filled in.

1. In the form, enter the API name, display name, and type of each dimension that you want to restrict.

   The form doesn't prompt you for these details.

1. Submit the support case.

The AWS Marketplace Seller Operations team reviews the case. If the support case form doesn't open, try again, or contact the AWS Marketplace Seller Operations team through AWS Partner Central support.

## Determine how buyers will access your product
<a name="configure-product-access"></a>

**Note**  
These options don't apply to Agentic Commerce products. Their agents pay for each request, and Quick Launch isn't available. Your fulfillment URL leads to a sign-in page, or to a setup page if buyers don't need an account.

You can choose one of the following options for how customers can access your product:
+ [Update the SaaS URL fulfillment option](#update-fulfillment-options) – Customers use a URL for the site that they are redirected to after subscribing to your product in AWS Marketplace.
+ [Configure Quick Launch](#saas-quick-launch) – Customers use a simplified process to configure and launch your product.

### Update the SaaS URL fulfillment option
<a name="update-fulfillment-options"></a>

To change the website that buyers go to after they subscribe to your SaaS product, update the fulfillment URL.

**To update the fulfillment URL**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **SaaS delivery option** section, choose **Edit**.

   If the product has no SaaS delivery option yet, add one first. For more information, see [Adding a SaaS delivery option](saas-create-product-page.md#saas-add-delivery-option).

1. Under **Fulfillment options**, for **Fulfillment URL**, enter the new URL.

   The URL must start with `https://` and have 8 to 2,048 characters.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Update delivery option**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

If your product uses an API-based agents and tools delivery option, the **Delivery** tab shows its own sections instead. To change the fulfillment URL, choose **Edit** in the **Agent type and fulfillment** section. For more information, see [Update the API delivery option](listing-saas-ai-agents.md#update-api-delivery-option).

## Configure Quick Launch
<a name="saas-quick-launch"></a>

SaaS products listed in AWS Marketplace often require AWS resources to be deployed in the subscribing buyer's account (for example, IAM roles). Quick Launch allows you to provide your buyers with guided, step-by-step instructions and resource deployment using CloudFormation templates. Buyers use the CloudFormation templates to configure and launch products. To learn more about the Quick Launch configuration process, see the [Enable SaaS Quick Launch](https://catalog.workshops.aws/mpseller/en-US/saas/quick-launch-integration) lab.

Quick Launch requires a SaaS delivery option, so add that option first. For more information, see [Adding a SaaS delivery option](saas-create-product-page.md#saas-add-delivery-option). Quick Launch is available only in the commercial AWS Marketplace catalog, and not for products that use an API-based agents and tools delivery option. The **Quick Launch - recommended** fulfillment method in the API-based agents and tools wizard is separate from this feature. For that method, see [Configure fulfillment options](listing-saas-ai-agents.md#step-2-fulfillment-options).

Setting up Quick Launch has four stages: develop the CloudFormation template, configure Quick Launch, test the configuration with Limited visibility, and request Public visibility.

Before you configure Quick Launch, create an CloudFormation template that deploys the resources your product needs in the buyer's AWS account. Upload the template to an Amazon S3 bucket, and make its URL publicly accessible.

**Tip**  
Follow the AWS Well-Architected Framework when you create the template. For more information, see [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) on the AWS website and the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

**To configure Quick Launch**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Quick Launch** section, choose **Configure**.

   For a new product, you can instead choose **Start** on the **Add Quick Launch** card under **Step 2: Delivery configuration**. Both are unavailable until the product has a SaaS delivery option.

1. On the **Configure Quick Launch** page, under **Account linking details**, enter the **Sign-in or registration URL**: the URL where buyers sign in to or create an account on your website. The URL must start with `https://` and have up to 500 characters.

1. Under **AWS CloudFormation template**, add your templates.

   For the steps, see [To add a CloudFormation template to Quick Launch](#saas-quick-launch-add-template).

1. Enter the following:
   + **Instructions** (optional), under **Manual configuration instructions**: steps for buyers who want to configure your product manually. You can use Markdown and links, up to 30,000 characters.
   + **Launch URL**, under **Launch details**: the URL where buyers access the product after they deploy the CloudFormation stack. The URL must start with `https://` and have up to 500 characters.
   + **Tags** (optional): tags for the change request.

1. Choose **Add Quick Launch**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

Quick Launch starts with Limited visibility, which only your AWS account can see. To test it, subscribe to your product from your seller account or an allowlisted account, choose **Set up your account**, and use the **Configure and launch** page. To let other accounts test it, add them to **Allowlisted accounts for Quick Launch** when you change Quick Launch visibility.<a name="saas-quick-launch-add-template"></a>

**To add a CloudFormation template to Quick Launch**

1. On the **Configure Quick Launch** or **Update Quick Launch** page, under **AWS CloudFormation template**, choose **Add template**.

   While the table is empty, you can also choose **Add CloudFormation template** inside it.

1. In the **Add AWS CloudFormation template** dialog box, enter the following:
   + **Title**: the template name that buyers see on the configuration page. Up to 64 characters, and unique across your templates.
   + **Description** (optional): text that tells buyers how this template differs from your others. Up to 4,096 characters.
   + **CloudFormation stack name**: the name of the stack that buyers deploy in the CloudFormation console. Start with a letter, and use only letters, numbers, and hyphens, up to 128 characters.
   + **CloudFormation template URL**: the Amazon S3 URL of your template, starting with `https://`. Up to 2,048 characters, and unique across your templates.
   + **Required IAM permissions**: the IAM permissions that buyers need to use this template, up to 4,000 characters. If you share deployment parameters, which are stored as secrets in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) for the buyer, your policy must include the following actions:
     + `secretsManager:ListSecrets`
     + `secretsManager:DescribeSecret`
     + `secretsManager:ReplicateSecretToRegions`
     + `secretsManager:GetSecretValue`
**Note**  
If your product requires seller-provided CloudFormation deployment parameters (for example, API keys and [external IDs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)), use the [PutDeploymentParameter](https://docs.aws.amazon.com/marketplace-deployment/latest/api-reference/API_PutDeploymentParameter.html) operation in the *AWS Marketplace Deployment Service API Reference* to share the parameter with your customers.

1. Choose **Add template**.

You can add up to 20 templates. To simplify launch for buyers, we suggest one template that deploys the resources needed to use the product.

**To update Quick Launch**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Quick Launch** section, choose **Edit**.

1. On the **Update Quick Launch** page, change the fields that you need.

   The fields and limits are the same as on the **Configure Quick Launch** page.

1. Choose **Update Quick Launch**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**To change Quick Launch visibility**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Quick Launch** section, choose **Update visibility**.

1. Under **Quick Launch visibility options**, choose one of the following:
   + **Public**: Quick Launch is available to all AWS Marketplace buyers. Your SaaS delivery option is deactivated, and the AWS Marketplace Seller Operations team reviews the request.
   + **Limited**: only allowlisted accounts can see Quick Launch. Under **Allowlisted accounts for Quick Launch**, for **AWS accounts**, enter up to 100 AWS account IDs, separated by commas. The seller account that you're signed in to is allowlisted by default.
   + **Deactivated**: no one can see Quick Launch.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

A request for Public visibility completes after the AWS Marketplace Seller Operations team reviews it.

**Note**  
If you need support as you enable the Quick Launch experience, contact the AWS Marketplace Seller Operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).

## Update availability by country
<a name="saas-availability-by-country"></a>

You can define the countries in which your product can be offered.

**To update availability by country**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Update**, and then choose **Update availability by country**.

   The **Update** menu is available after your public offer is released, and unavailable while another request for the offer is in progress.

1. Under **Offer availability by country**, choose one of the following:
   + **All countries**: buyers can purchase your product in all countries.
   + **All countries with exclusions**: for **Excluded countries**, choose the countries where buyers can't purchase your product.
   + **Allowlisted countries only**: for **Allowlisted countries**, choose the countries where buyers can purchase your product.

   This setting controls where buyers can purchase your product. It doesn't change the AWS Regions where buyers can use your product.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** in the **Public offer** section of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu in the **Public offer** section is unavailable.

## Update the refund policy of a product
<a name="update-refund-policy"></a>

You can update the refund policy for your product by using **Update refund policy**.

**To update the refund policy**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Update**, and then choose **Update refund policy**.

   The **Update** menu is available after your public offer is released, and unavailable while another request for the offer is in progress.

1. Under **Refund policy**, edit the current policy.

   Include the terms of your policy and the contact information that buyers use to request a refund. The policy can have up to 500 characters.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** in the **Public offer** section of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu in the **Public offer** section is unavailable.

## Update the end user license agreement (EULA)
<a name="saas-update-eula"></a>

You can update your EULA for new users subscribing to your product.

**To update the EULA**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Update**, and then choose **Update EULA**.

   The **Update** menu is available after your public offer is released, and unavailable while another request for the offer is in progress.

1. Under **End-user license agreement (EULA)**, for **Legal terms**, choose one of the following:
   + **Standard Contract for AWS Marketplace (SCMP)**: use the [Standard Contract for AWS Marketplace (SCMP)](https://docs.aws.amazon.com/marketplace/latest/userguide/standardized-license-terms.html).
   + **Custom legal terms**: use your own EULA.

1. If you chose **Custom legal terms**, under **Custom legal terms and other offer documents**, choose **Choose files**, and upload your EULA.

   You can upload up to 5 files in plain text (.txt) or PDF (.pdf) format, up to 30 MB in total. AWS Partner Central combines the files into a single PDF, in the order that you upload them.

1. Choose **Submit**.

Your change request appears on the offer's **Requests log** tab. To open the offer, choose the link under **Offer ID** in the **Public offer** section of the **Procurement** tab. Its status moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the **Update** menu in the **Public offer** section is unavailable.