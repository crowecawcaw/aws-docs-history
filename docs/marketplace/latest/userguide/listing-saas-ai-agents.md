

# Listing SaaS API-based AI agent products

As an AWS Marketplace seller, you can add your software as a service (SaaS) API-based AI agent or tools product to AWS Marketplace. This includes creating your product and integrating it with the appropriate AWS Marketplace API operations, based on your billing model.

To sell software as a SaaS API-based AI agent or tools products in AWS Marketplace, follow these steps:
+ Create the SaaS API-based AI agent or tools product in AWS Marketplace.
+ Integrate your product with AWS Marketplace based on your pricing model:
  + For information about subscription-based products, see [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md).
  + For information about contract-based products, see [Integrating your SaaS contract product with AWS Marketplace](saas-integrate-contract.md).
  + For information about contract with pay-as-you-go products, see [Integrating your SaaS contract with consumption product with AWS Marketplace](saas-integrate-contract-with-pay.md).
+ Test your product's integration:
  + For information about testing subscription-based products, see [Testing your SaaS subscription product integration](saas-integrate-subscription.md#saas-subscription-integration-testing).
  + For information about testing contract-based products, see [Testing your SaaS contract product integration](saas-integrate-contract.md#saas-contract-integration-testing).
  + For information about testing contract with pay-as-you-go products, see [Testing your SaaS contract with pay-as-you-go integration](saas-integrate-contract-with-pay.md#saas-contract-consumption-integration-testing).
+ Submit your product for launch.

If you want AI agents to pay for each request through x402, list an Agentic Commerce product instead. Agentic Commerce products don't need a SaaS subscription integration or metering. Instead, you need an x402 endpoint and a quote-signing key. For more information, see [Listing Agentic Commerce products](agentic-commerce-products.md).

## Prerequisites
<a name="saas-ai-agents-prerequisites"></a>

Before beginning, ensure that you have the following:
+ Clear understanding of your AI agent capabilities and target use cases
+ Appropriate security measures and compliance certifications
+ Technical documentation for integration and deployment
+ Pricing strategy aligned with your business model
  + For information about pricing strategy, see [SaaS product pricing in AWS Marketplace](saas-pricing-models.md).
+ For Agentic Commerce products, an HTTPS endpoint that returns signed x402 quotes, and a quote-signing key. For more information, see [Listing Agentic Commerce products](agentic-commerce-products.md).

## Managing SaaS API-based AI agents and tools
<a name="managing-saas-ai-agents"></a>

You manage SaaS API-based AI agents and tools on the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central.

## Create and publish the product
<a name="start-listing-wizard"></a>

**To create an API-based AI agent or tool product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. Under **Product details**, for **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique.

1. For **Product type**, choose **AI agent or tool**.

   AI agents and tools are available in the commercial AWS Marketplace catalog only.

1. For **AI type**, choose **API-based**.

1. (Optional) Under **Tags**, add tags to support tag-based authorization.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens its page, which shows **Complete your listing**.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

   For the fields on the **Provide product details** card, see [Update product information](saas-product-settings.md#update-product-information).

1. Under **Step 2: Delivery configuration**, complete the **Add delivery option** card.

   For more information, see [Configure fulfillment options](#step-2-fulfillment-options).

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   After the request succeeds, your product is in the **Limited** state, and you can test it with the accounts on its allowlist.

**To publish an API-based AI agent or tool product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 3: Procurement configuration** and **Step 4: Testing and integrations**.

   In Step 3, you create the public offer, which sets your pricing, refund policy, EULA, and offer availability. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

1. (Optional) Complete **Step 5: Add-ons**.

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

**Note**  
For information about tag-based authorization, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources) in the AWS Identity and Access Management User Guide.

## Provide product information
<a name="step-1-product-information"></a>

The information you provide in **Step 1: Product details** communicates the value proposition of your product. You enter it on the **Provide product details** card. For the procedure, see [Update product information](saas-product-settings.md#update-product-information).

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Central Agents to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

For **Product categories**, choose up to 3 categories. We recommend that you choose at least one category from the AI Agents & Tools business categories.

## Configure fulfillment options
<a name="step-2-fulfillment-options"></a>

You add the delivery option in a four-step wizard. Complete the following procedures in order.

**To configure fulfillment options**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 2: Delivery configuration**, choose **Start** on the **Add delivery option** card.

1. For **Delivery method**, choose **API-based agents and tools**.

   The page opens with **SaaS** selected, even for an AI agent or tool product.

**Note**  
If you're listing an Agentic Commerce product, follow the steps in [Add the Agentic Commerce delivery option](agentic-commerce-products.md#agentic-commerce-add-delivery-option) instead of the remaining procedures.

**To select the agent type and fulfillment**

1. Under **Agent type**, for **Type**, choose one of the following:
   + **AI agent**: software that uses AI to process requests and complete tasks through reasoning and decision-making.
   + Under **AI tools**: **MCP server**, **Knowledge base**, **Guardrail**, or **Other**.

   To request a tool type that isn't listed, choose **Other**, and then choose **Contact us** in the **Additional agent tool types** alert.

1. Under **Fulfillment**, for **Access model**, keep **Registration with seller**.

   Buyers subscribe, and then register with you to get API credentials. To have buyer agents pay for each request through AWS Marketplace instead, see [Add the Agentic Commerce delivery option](agentic-commerce-products.md#agentic-commerce-add-delivery-option).
**Note**  
After you add the delivery option, you can't change the access model or the fulfillment method. To use a different one, create a new product.

1. For **Fulfillment method**, choose one of the following:
   + **Quick Launch - recommended**: you integrate with the [AWS Marketplace Deployment API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Deployment_Service.html) and deliver API keys or OAuth credentials directly to the buyer's AWS account. For more information, see [Quick Launch fulfillment](integrating-api-ai-agents-tools.md#quicklaunch-fulfillment).
   + **Redirect to your website**: buyers go to your website to get their API keys or OAuth tokens. For more information, see [Redirect to your website fulfillment](integrating-api-ai-agents-tools.md#redirect-website-fulfillment).

1. For **Fulfillment URL**, enter the URL that AWS Marketplace sends buyers to after they subscribe, such as your sign-in or registration page.

   The URL must start with `https://` and have up to 500 characters.

1. Choose **Next**.

**To configure the endpoint and usage**

1. If you chose **Quick Launch - recommended**, on the **Configure endpoint and usage** step, for **Endpoint type**, choose **Static** or **Dynamic**.

   A static endpoint is a fixed URL that is the same for all buyers. A dynamic endpoint is a URL template with buyer-specific placeholders. With **Redirect to your website**, the endpoint is static.

1. For **API endpoint URL**, enter the publicly accessible URL where your API receives requests.

   For an MCP server, the field is **MCP endpoint URL**. The URL must start with `https://`. A static URL has up to 500 characters, for example `https://api.example.com/v1/mcp`. A dynamic URL has up to 2,048 characters and uses `{paramName}` placeholders, for example `https://{tenantId}.apps.example.com/v1/mcp`.

1. If you chose **Dynamic**, under **Endpoint parameters**, enter one parameter for each placeholder in the URL. To add a parameter, choose **Add parameter**.
   + **Parameter name**: matches a placeholder in your URL. Start with a letter, and use only letters, numbers, and underscores, up to 64 characters.
   + **Description** (optional): help text that tells buyers what the parameter is for, up to 1,000 characters.
   + **Default value** (optional): a value used until you deliver a buyer-specific value. Use letters, numbers, hyphens, periods, underscores, and tildes, up to 256 characters.

   You can add up to 5 parameters. Every placeholder needs a matching parameter, and every parameter needs a matching placeholder. After a buyer subscribes, deliver the values with the `PutDeploymentParameter` operation. For more information, see [Delivering dynamic endpoint parameters](integrating-api-ai-agents-tools.md#dynamic-endpoint-parameter-delivery).

1. Under **Usage instructions**, for **API usage instructions**, describe how buyers call your API: the request format, rate limits, and examples, with links to your documentation.

   You can use Markdown, up to 4,000 characters. The field is optional for an MCP server, which gets its own instructions on the next step. For templates, see [Usage instructions templates](integrating-api-ai-agents-tools.md#usage-instructions-templates).

1. Under **Authorization**, for **Authorization method**, choose one or both of the following:
   + **API key**: buyers authenticate with API keys that you provide.
   + **OAuth 2.0**: buyers authenticate with an OAuth 2.0 flow. In your usage instructions, include the authorization URL and token endpoint, the required scopes, the step-by-step flow, example calls with authentication headers, and troubleshooting tips.

1. If you chose **AI agent**, under **AI agent requirements**, select **I confirm my AI agent adheres to the preceding requirements.**

   Your agent must use reasoning large language models (LLMs) or a similar component for decision-making. It must also operate without explicit external commands or constant human input. If your agent doesn't meet both requirements, choose a different type.

1. Choose **Next**.

**To set protocols and integration**

1. On the **Set protocols and integration** step, under **Amazon Bedrock AgentCore Gateway integration**, for **Integration status**, choose **Enable tool for AgentCore Gateway integration - recommended** or **Do not enable tool for AgentCore Gateway integration**.

1. For **OpenAPI specification file upload**, choose **Choose file**, and select your OpenAPI specification.

   Use .json, .yml, or .yaml format, up to 1 MB. The uploaded file expires after 6 hours, so submit the delivery option within that time. The file is required when you enable Gateway integration, except for an MCP server that uses **OAuth 2.0**. For specification requirements, see [Amazon Bedrock AgentCore Gateway](bedrock-agentcore-gateway.md).

1. (Optional) Under **API integration protocols**, for **Supported protocols**, select **MCP (Model Context Protocol)**, **A2A (Agent-to-Agent Protocol)**, or both.

1. For each protocol, enter its usage instructions, up to 4,000 characters.

   An MCP server always includes MCP, so it has no MCP check box and requires **MCP usage instructions**. For a template, see [MCP server usage instructions template](integrating-api-ai-agents-tools.md#mcp-server-template).

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

1. On the **Review and submit** step, choose **Add delivery option**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Configure product pricing
<a name="step-3-product-pricing"></a>

To make your product available on AWS Marketplace, decide on a pricing model and define your product's pricing dimensions. For more information about available pricing options, see [SaaS product pricing in AWS Marketplace](saas-pricing-models.md).

Each dimension is a feature, service, or other aspect of your product for which you can set a per-unit price.

You choose the pricing model and dimensions on the **Set pricing model and dimensions** step when you create the public offer in **Step 3: Procurement configuration**. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

You can't change the pricing model later. To use a different pricing model, create a new product.

For an Agentic Commerce product, AWS Marketplace sets the pricing model and one fixed-rate usage dimension. You can't add, edit, or remove dimensions.

## Set prices
<a name="step-4-review-prices"></a>

You set prices on the **Configure pricing details and duration** step when you create the public offer. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

Before you publish, replace any test prices in your public offer with the prices that you want buyers to pay. After your product is public, buyers can purchase at the offer prices. For more information, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).

For an Agentic Commerce product, you don't set prices. Your endpoint sets the price in each signed quote, and buyers pay that amount.

## Specify refund policy
<a name="step-5-refund-policy"></a>

You enter the refund policy on the **Specify refund policy** step when you create the public offer. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

## Configure End-User License Agreement (EULA)
<a name="step-6-eula"></a>

You choose the EULA on the **Configure legal terms and offer documents** step when you create the public offer. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

Choose **Standard Contract for AWS Marketplace (SCMP)**, or choose **Custom legal terms** and upload your EULA as .txt or .pdf files. For more information about the SCMP, see [Using standardized contracts in AWS Marketplace](standardized-license-terms.md).

## Configure offer availability
<a name="step-7-offer-availability"></a>

By default, products listed on AWS Marketplace are available for purchase in all countries that AWS supports. You have the option to enable country-specific availability by identifying countries where buyers can or cannot purchase your product from.

You choose the countries where buyers can purchase your product on the **Configure offer availability** step when you create the public offer. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

## Configure the allowlist
<a name="step-8-allowlist"></a>

All new product listings published to AWS Marketplace start out with limited visibility. You can control which accounts have access to your limited product, including limited versions of your product, by adding select AWS account IDs to an allowlist.

You add accounts with the **Share with others for testing** card under **Step 4: Testing and integrations**. For the procedure, see [Update the allowlist of AWS account IDs](saas-product-settings.md#update-allowlist).

**Note**  
Only add test accounts to the allowlist for the purpose of testing.

## Modifying SaaS API-based AI agent products settings in AWS Marketplace
<a name="modifying-saas-ai-agents"></a>

After you create a SaaS API-based AI agent or tool product in AWS Marketplace, you can modify many of the product settings. To change the delivery option, see [Update the API delivery option](#update-api-delivery-option). For information about change requests and other product settings, see the following topics:

### Update the API delivery option
<a name="update-api-delivery-option"></a>

The update wizard has the same steps and fields as the wizard that you used to add the option, with the following differences:
+ There's no **Delivery method** choice.
+ You can't change **Access model** or **Fulfillment method**.
+ If the option has an OpenAPI specification, the wizard shows it as **Current API specification**. To upload a new file, choose **Replace**. You can't remove a stored specification.
+ The wizard doesn't ask you to confirm the **AI agent requirements** again.

**To update an API delivery option**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the section that you want to change, choose **Edit**.

   The update wizard opens on the step with that section's fields.

1. Change the fields that you need. To move between steps, choose **Next** or **Previous**.

   For field rules and limits, see [Configure fulfillment options](#step-2-fulfillment-options).

1. On the **Review and submit** step, choose **Update delivery option**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

To turn on Amazon Bedrock AgentCore Gateway integration for an existing MCP server, A2A, or other API option, see [Enabling Bedrock AgentCore Gateway](bedrock-agentcore-gateway.md#enabling-bedrock-agentcore). Agentic Commerce options don't offer this setting.

### Product changes and requests
<a name="product-changes-requests"></a>
+ For information about managing change requests, see [Manage change requests](saas-product-settings.md#create-change-request).
+ For information about updating product information, see [Update product information](saas-product-settings.md#update-product-information).
+ For information about updating architecture details, see [Update architecture details](saas-product-settings.md#updating-architecture-details).

### Access and visibility
<a name="access-visibility"></a>
+ For information about updating the allowlist, see [Update the allowlist of AWS account IDs](saas-product-settings.md#update-allowlist).
+ For information about changing product visibility, see [Update product visibility](saas-product-settings.md#saas-update-visibility).
+ For information about country availability, see [Update availability by country](saas-product-settings.md#saas-availability-by-country).

### Pricing and terms
<a name="pricing-terms"></a>
+ For information about updating pricing terms, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).
+ For information about adding pricing dimensions, see [Add pricing dimensions](saas-product-settings.md#saas-add-pricing-dimensions).
+ For information about updating pricing dimensions, see [Update pricing dimensions](saas-product-settings.md#saas-update-dimension).
+ For information about restricting pricing dimensions, see [Restrict pricing dimensions](saas-product-settings.md#restrict-pricing-dimensions).

**Note**  
You can't update pricing terms for an Agentic Commerce product. In the console, you also can't add or update pricing dimensions. AWS Marketplace creates the `agentic_commerce_default` dimension for you and meters it for each verified payment. An Agentic Commerce offer supports only that dimension. If the product has any other pricing dimensions, such as dimensions that you added through the Catalog API, restrict them before you create a public offer. Until you do, the console doesn't let you create the offer.

### Legal and licensing
<a name="legal-licensing"></a>
+ For information about updating the refund policy, see [Update the refund policy of a product](saas-product-settings.md#update-refund-policy).
+ For information about updating the EULA, see [Update the end user license agreement (EULA)](saas-product-settings.md#saas-update-eula).

### To provide a free product
<a name="free-product"></a>

To offer your product for free, create its public offer with the **Free** pricing model. You choose it on the **Set pricing model and dimensions** step, and you don't add pricing dimensions or prices. For the procedure, see [Pricing for SaaS contracts](saas-contracts.md) or [Pricing for SaaS subscriptions](saas-subscriptions.md).

If your product already has a public offer, update its pricing terms and set the price of every dimension to zero. This change converts the product to the Free pricing model. For the procedure, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).

**Note**  
After a product is set as free, you cannot convert it to a paid product.