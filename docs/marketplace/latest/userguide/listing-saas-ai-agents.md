

# Listing SaaS API-based AI agent products
<a name="listing-saas-ai-agents"></a>

As an AWS Marketplace seller, you can add your software as a service (SaaS) API-based AI agent or tools product to AWS Marketplace. This includes creating your product and integrating it with the appropriate AWS Marketplace API operations, based on your billing model.

To sell software as a SaaS API-based AI agent or tools products in AWS Marketplace, follow these steps:
+ Create the SaaS API-based AI agent or tools product in AWS Marketplace.
+ Integrate your product with AWS Marketplace based on your pricing model:
  + For information about subscription-based products, see [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md).
  + For information about contract-based products, see [Integrating your SaaS contract product with AWS Marketplace](saas-integrate-contract.md).
  + For information about contract with pay-as-you-go products, see [Integrating your SaaS contract-based product with AWS Marketplace](saas-integrate-contract-with-pay.md).
+ Test your product's integration:
  + For information about testing subscription-based products, see [Testing your SaaS subscription product integration](saas-integrate-subscription.md#saas-subscription-integration-testing).
  + For information about testing contract-based products, see [Testing your SaaS contract product integration](saas-integrate-contract.md#saas-contract-integration-testing).
  + For information about testing contract with pay-as-you-go products, see [Testing your SaaS contract with pay-as-you-go integration](saas-integrate-contract-with-pay.md#saas-contract-consumption-integration-testing).
+ Submit your product for launch.

## Prerequisites
<a name="saas-ai-agents-prerequisites"></a>

Before beginning, ensure that you have the following:
+ Clear understanding of your AI agent capabilities and target use cases
+ Appropriate security measures and compliance certifications
+ Technical documentation for integration and deployment
+ Pricing strategy aligned with your business model
  + For information about pricing strategy, see [SaaS product pricing in AWS Marketplace](saas-pricing-models.md).

## Managing SaaS API-based AI agents and tools
<a name="managing-saas-ai-agents"></a>

All SaaS API-based AI agents and tools can be managed through the unified **AI agents and tools** products page or the **SaaS** products page in the AWS Marketplace Management Console.

## Start the listing wizard
<a name="start-listing-wizard"></a>

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. In the navigation bar, select **Build**, then choose **AI agents and tools**.

1. From the **Create AI Agents & Tools product** menu, choose **API-based AI agents & tools**. 

1. Enter a product title.

1. Choose **Generate product ID and product code**.

1. (Optional) Add tags to support tag-based authorization.

1. Choose **Continue to wizard**.

**Note**  
For information about tag-based authorization, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources) in the AWS Identity and Access Management User Guide.

## Step 1: Provide product information
<a name="step-1-product-information"></a>

The information you provide in this step communicates the value proposition of your product.

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Assistant to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

1. Provide details for Product information tab:
   + **Product title**
   + **SKU** (optional)
   + **Product logo S3 URL**
   + **Short description**
   + **Long description**
   + **Product video URL** (optional)
   + **Highlights** (1-3)

1. Enter support details and add optional learning resources by choosing **Add resource**.

1. In the **Product categories** menu, choose 1-3 categories.
   + We recommend that you choose at least one category from the **AI Agents & Tools** business categories.

1. Enter keywords to improve search discoverability.

1. (Optional) Add video and image assets according to the guidelines.

1. Choose **Next**.

## Step 2: Configure fulfillment options
<a name="step-2-fulfillment-options"></a>

1. Choose a fulfillment method:
   + **Quick Launch** (Recommended) - Sellers integrate with the [AWS Marketplace Deployment API](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Deployment_Service.html) and provides API keys directly to customers' AWS account upon subscription.
   + **Redirect to your website** - Customers will be redirected to your website to obtain API keys or OAuth tokens.
**Note**  
You cannot change the fulfillment method after you publish the product.

1. Enter the fulfillment URL. This is the URL where users sign in or create an account.

1. Choose your AI agent or tool details:
   + **AI Agent** - Software that uses AI to process requests and completes tasks through reasoning and decision-making.
   + **AI tools**:
     + **MCP Server** - A server that manages communication and context exchange between AI models and applications.
     + **Knowledge base** - A structured collection of information that AI agents use to inform decision and responses.
     + **Guardrail** - Rules and controls that define boundaries for AI agent behavior and operations.
     + **Other** - Additional tools that enhance AI agent capabilities.

1. Enter the endpoint URL. This is the URL where your API receives requests. For MCP servers, list the MCP endpoint.
   + **Static endpoint** – Enter a fixed URL with no parameters. For example: `https://api.example.com/v1/mcp`.
   + **Dynamic endpoint** – Enter a URL that contains one or more placeholder parameters using `{paramName}` syntax. For example: `https://{tenantId}.apps.example.com/v1/mcp`.

     Dynamic endpoints resolve to buyer-specific URLs after subscription. When you choose this option, you must use the **Quick Launch** fulfillment method.

     Configure your endpoint URL parameters:
     + **Name** (required) – A machine identifier that matches a `{paramName}` placeholder in your URL. Names must start with a letter and contain only letters, digits, and underscores. Maximum length is 64 characters.
     + **Description** (optional) – Help text displayed to buyers that explains the purpose of the parameter.
     + **Default value** (optional) – A fallback value used when a buyer-specific value has not yet been delivered. Values can contain letters, numbers, hyphens, periods, underscores, and tildes. Maximum length is 256 characters.
**Note**  
You can define up to 5 parameters per endpoint. Every `{paramName}` placeholder in the URL must have a matching parameter entry, and every parameter entry must correspond to a placeholder in the URL.

     After a buyer subscribes, call the `PutDeploymentParameter` API operation to deliver buyer-specific parameter values. The Fulfillment Widget resolves the final URL automatically using the delivered values. For more information, see [Delivering dynamic endpoint parameters](integrating-api-ai-agents-tools.md#dynamic-endpoint-parameter-delivery).

1. Add usage instructions:
   + Provide detailed instructions for buyers to use your API such as API schema, rate limits, and usage examples.
   + You can also provide additional links to your documentation.

1. Choose an authorization method:
   + **API Keys** – Customers authenticate using API keys that you provide.
   + **OAuth** – Customers authenticate using OAuth 2.0 authorization flow. If you choose OAuth, provide clear usage instructions for customers, including:
     + OAuth authorization URL and token endpoint
     + Required scopes and permissions
     + Step-by-step authentication flow instructions
     + Example API calls with proper authentication headers
     + Troubleshooting common authentication issues

1. (Optional) Amazon Bedrock AgentCore integration 
   + If you list an MCP server that supports two-legged OAuth authentication, you can enable integration with Amazon Bedrock AgentCore Gateway using your MCP server endpoint as the target. For more information, see [MCP server targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-MCPservers.html). In this case, OpenAPI spec is not required.
   + If you list any other API-based product or MCP servers with API Key authentication, you can enable integration with Amazon Bedrock AgentCore by providing OpenAPI spec.
   + To learn more about AgentCore's capabilities for deploying and scaling AI agents, see [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)

1. (Optional) - Choose API integration protocols and provide usage instructions:
   + **MCP** - Model Context Protocol (MCP) standardizes access to external tools, data, and services for enhanced functionality.
   + **A2A** - Agent2Agent (A2A) enables direct communication and task delegation across different platforms.

1. If you selected an AI agent tool type, confirm that your agent uses reasoning LLMs and demonstrates autonomous capabilities. These requirements help ensure that agents offered on AWS Marketplace meet a high quality bar. If your agent does not meet both requirements, choose a different tool type.

## Step 3: Configure product pricing
<a name="step-3-product-pricing"></a>

To make your product available on AWS Marketplace, decide on a pricing model and define your product's pricing dimensions. For more information about available pricing options, see [SaaS product pricing in AWS Marketplace](saas-pricing-models.md).

Each dimension is a feature, service, or other aspect of your product for which you can set a per-unit price.

1. Choose a pricing model.

1. Choose **Next**.

## Step 4: Review prices
<a name="step-4-review-prices"></a>

1. Review Product Pricing.

1. Choose **Next**.

**Note**  
For testing purposes, we set the price to $0.001 or $0.00000001. You don't need to change the price now. This allows both your team and AWS Marketplace Seller Operations team to test the product at a reduced price and not incur a large bill for testing. You will provide actual pricing when you request product visibility for the product to go public.

## Step 5: Specify refund policy
<a name="step-5-refund-policy"></a>

1. Enter refund policy for your product.

1. Choose **Next**.

## Step 6: Configure End-User License Agreement (EULA)
<a name="step-6-eula"></a>

1. Choose **Standard Contract for AWS Marketplace** or provide a S3 URL to your **Custom EULA**.
   + For more information about using the Standard Contract, see [Using standardized contracts in AWS Marketplace](standardized-license-terms.md).

1. Choose **Next**.

## Step 7: Configure offer availability
<a name="step-7-offer-availability"></a>

By default, products listed on AWS Marketplace are available for purchase in all countries that AWS supports. You have the option to enable country-specific availability by identifying countries where buyers can or cannot purchase your product from.

1. Choose your offer availability by country.

1. Choose **Next**.

## (Optional) Step 8: Configure allowlist
<a name="step-8-allowlist"></a>

All new product listings published to AWS Marketplace start out with limited visibility. You can control which accounts have access to your limited product, including limited versions of your product, by adding select AWS account IDs to an allowlist.

To add AWS accounts to the allowlist:

1. Enter comma-separated AWS account IDs that you need to add to the allowlist.

1. Choose **Submit**.

**Note**  
Only add test accounts to the allowlist for the purpose of testing.

## Modifying SaaS API-based AI agent products settings in AWS Marketplace
<a name="modifying-saas-ai-agents"></a>

After you create a **SaaS API-Based Agent & Tool Product** in AWS Marketplace, you can modify many of the product settings. For information about submitting change requests and modifying product settings, see the following topics:

### Product changes and requests
<a name="product-changes-requests"></a>
+ For information about managing change requests, see [Manage change requests](saas-product-settings.md#create-change-request).
+ For information about updating product information, see [Update product information](saas-product-settings.md#update-product-information).
+ For information about updating architecture details, see [Update architecture details](saas-product-settings.md#updating-architecture-details).

### Access and visibility
<a name="access-visibility"></a>
+ For information about updating the allowlist, see [Update the allowlist of AWS account IDs](saas-product-settings.md#update-allowlist).
+ For information about changing product visibility, see [Update product visibility](saas-product-settings.md#saas-update-visibility).
+ For information about managing buyer access, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).
+ For information about country availability, see [Update availability by country](saas-product-settings.md#saas-availability-by-country).

### Pricing and terms
<a name="pricing-terms"></a>
+ For information about updating pricing terms, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).
+ For information about adding pricing dimensions, see [Add pricing dimensions](saas-product-settings.md#saas-add-pricing-dimensions).
+ For information about updating pricing dimensions, see [Update pricing dimensions](saas-product-settings.md#saas-update-dimension).
+ For information about restricting pricing dimensions, see [Restrict pricing dimensions](saas-product-settings.md#restrict-pricing-dimensions).

### Legal and licensing
<a name="legal-licensing"></a>
+ For information about updating the refund policy, see [Update the refund policy of a product](saas-product-settings.md#update-refund-policy).
+ For information about updating the EULA, see [Update the end user license agreement (EULA)](saas-product-settings.md#saas-update-eula).

### To provide a free product
<a name="free-product"></a>

If your product has limited visibility:
+ Submit a request to change visibility from limited to public.
+ Enter $0 for all pricing dimensions.

If your product is already public:
+ Submit an **Update Pricing Terms** change request.
+ Enter $0 for all pricing dimensions.

**Note**  
After a product is set as free, you cannot convert it to a paid product.