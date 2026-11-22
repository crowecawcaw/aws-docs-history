

# Listing Container-based AI agent products

## Managing container-based AI agents and tools
<a name="managing-container-ai-agents"></a>

You manage container-based AI agents and tools on the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central. In the **Product type** column, a product shows **AI agent or tool - Container-based** after it has a version that supports Amazon Bedrock AgentCore Runtime. Until then, it shows **Software - Container**.

## Start the listing wizard
<a name="start-container-listing-wizard"></a>

**To create a container-based AI agent or tool product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose **Create product**.

1. Under **Product details**, for **Product name**, enter the name that buyers see on your listing and in AWS Marketplace search results.

   The name must be 2 to 72 characters and unique.

1. For **Product type**, choose **AI agent or tool**.

   AI agents and tools are available in the commercial AWS Marketplace catalog only.

1. For **AI type**, choose **Container-based**.

1. (Optional) Under **Tags**, add tags to support tag-based authorization.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens its page, which shows **Complete your listing**.

**To complete product details and delivery configuration**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 1: Product details**.

   For the fields on the **Provide product details** card, see [Updating product information for your container product on AWS Marketplace](update-container-product-info.md).

1. Under **Step 2: Delivery configuration**, complete the following cards in order:

   1. **Add repositories** – See [Add repositories](#container-step-5-repositories).

   1. **Upload container images to repository** – See [Upload container images](#container-step-7-upload).

   1. **Configure version and delivery options** – See [Add a version](#container-step-8-version).

   Each card is available after you complete the one before it.

1. Choose **Advance to procurement configuration**.

1. In the **Transition to Limited** dialog box, choose **Confirm and continue**.

   After the request succeeds, your product is in the **Limited** state. To publish it, see [Review and publish your product](#container-step-9-publish).

## Provide product details
<a name="container-step-1-product-info"></a>

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Central Agents to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

You enter product information on the **Provide product details** card under **Step 1: Product details**. For the procedure and the fields, see [Updating product information for your container product on AWS Marketplace](update-container-product-info.md).

For **Product categories**, you can choose up to 3 categories. We recommend that you choose at least one category from the **AI Agents & Tools** business categories.

## Add repositories
<a name="container-step-5-repositories"></a>

Complete the cards under **Step 2: Delivery configuration** in order: **Add repositories**, **Upload container images to repository**, and **Configure version and delivery options**. Each card is locked until you complete the one before it.

**To add repositories**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Repositories** section, choose **Add repositories**.

   For a new product, you can instead choose **Start** on the **Add repositories** card under **Step 2: Delivery configuration**.

1. Under **New repositories**, for **Repository name**, enter a unique name of 2 to 256 characters.

   Use lowercase letters, numbers, hyphens (-), underscores (\_), periods (.), and slashes (/). AWS Marketplace creates the repository in its Amazon Elastic Container Registry account, and you can't delete it or use it for other products.

   To add another repository, choose **Add new repository**.

   A product can have up to 70 repositories.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Upload container images
<a name="container-step-7-upload"></a>

For information about integrating AgentCore with your container image, see [Amazon Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md).

**To upload container images**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Repositories** section, select a repository.

1. Choose **View push commands**.

   For a new product, you can instead choose **Start** on the **Upload container images to repository** card under **Step 2: Delivery configuration**, and then choose **View push commands** in the repository's row.

1. Run the push commands to push your container image from your local repository to the AWS Marketplace repository.

   Repository tags are immutable. Use a tag that matches the product version, and don't use `latest` or an empty tag.

When one of your repositories holds an image, the **Upload container images to repository** card shows **Complete**.

## Add a version
<a name="container-step-8-version"></a>

You add a version in a three-step wizard. Complete the following procedures in order.

**To add a version**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Under **Step 2: Delivery configuration**, choose **Start** on the **Configure version and delivery options** card.

   After your product leaves Draft, you can instead choose the **Delivery** tab, and then choose **Add version** in the **Versions** section.

1. On the **Provide version information** step, for **Version title**, enter a title that is unique for the product.

   Use up to 64 characters. You can't use `latest`.

1. For **Release notes**, describe what's new in this version, up to 30,000 characters.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Next**.

**To define the delivery option**

1. On the **Define delivery options** step, under **Delivery option 1**, for **Delivery method**, choose **Container image**.

1. For **Supported services**, select **Amazon Bedrock AgentCore Runtime**.

   You can't combine it with other services. Any additional delivery options and versions must also support this service.

1. For **Type**, choose **AI agent** or **A2A server**, or under **AI tools**, choose **MCP server**.

1. For **Container image URI**, enter the URI of the image that you pushed, such as `709825985650.dkr.ecr.us-east-1.amazonaws.com/{{your-seller-alias}}/{{your-image}}:{{1.0}}`.

   The tag can't be `latest`. A delivery option that supports Amazon Bedrock AgentCore Runtime can have 1 container image.

1. Under **Environment variables**, choose **Add environment variable** for each variable that buyers must provide to configure the runtime behavior of the agent, and enter the following:
   + **Variable key**: the name that your container expects, up to 100 characters. Each key must be unique.
   + **Variable description**: what the variable does and its possible values, up to 300 characters.
   + **Default value** (optional): up to 100 characters. Don't provide a default for values that are unique to each buyer, such as credentials or API keys.

   You can add up to 50 environment variables.

1. Enter the delivery option details:
   + **Delivery option title**: a title that is unique in the version, up to 72 characters.
   + **Delivery option description**: up to 1,000 characters.
   + **Usage instructions**: how buyers use your software after they launch it, up to 4,000 characters.

1. (Optional) To add another delivery option, choose **Add delivery option**.

   A version can have up to 4 delivery options.

**To submit the version**

1. Choose **Next**.

1. If you chose **AI agent** or **A2A server**, confirm the AI agent requirements:

   The **Provide version information** step shows **AI agent requirements** only after a delivery option uses one of those types, so you go back to that step to confirm them.

   1. Choose **Previous** until you return to the **Provide version information** step.

   1. Under **AI agent requirements**, select **I confirm my AI agent adheres to the preceding criteria.**

      Your agent must use reasoning large language models (LLMs) or a similar component for decision-making. It must also operate without explicit external commands or constant human input.

   1. Choose **Next** until you reach the **Review and submit** step.

1. On the **Review and submit** step, choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

AWS Marketplace scans the container images in each new version. The **Versions** section on the **Delivery** tab shows the **Scan result**.

## Configure pricing
<a name="container-step-2-pricing"></a>

You set pricing when you create the public offer under **Step 3: Procurement configuration**. You choose the pricing model on the **Set pricing model and dimensions** step, and you enter prices on the **Configure pricing details and duration** step. For the procedure, see [Review and publish your product](#container-step-9-publish).

**Hourly** pricing isn't compatible with Amazon Bedrock AgentCore Runtime, because AWS Marketplace bills it for each Amazon ECS task or Amazon EKS pod. For a product that runs on Amazon Bedrock AgentCore Runtime, choose another pricing model. To learn more about contract pricing, see [Contract pricing for container products with AWS License Manager](container-license-manager-integration.md). To learn more about custom metering for usage-based pricing, see [Configuring custom metering for container products with AWS Marketplace Metering Service](container-metering-meterusage.md).

## Specify refund policy
<a name="container-step-3-refund"></a>

You enter the refund policy on the **Specify refund policy** step when you create the public offer. Include the terms of your policy and the contact information that buyers use to request a refund. The policy can have up to 500 characters.

To change the refund policy after your public offer is released, see [Updating the refund policy for your Container-based product on AWS Marketplace](update-container-refund-policy.md).

## Configure the EULA
<a name="container-step-4-eula"></a>

You choose the EULA on the **Configure legal terms and offer documents** step when you create the public offer. For **Legal terms**, choose **Standard Contract for AWS Marketplace (SCMP)** or **Custom legal terms**. For custom legal terms, you upload up to 5 files in plain text (.txt) or PDF (.pdf) format, up to 30 MB in total.

To change the EULA after your public offer is released, see [Updating your end-user license agreement (EULA) for container products on AWS Marketplace](container-update-eula.md).

## Configure offer availability and the allowlist
<a name="container-step-6-availability"></a>

You choose the countries where buyers can purchase your product on the **Configure offer availability** step when you create the public offer. To change them after your public offer is released, see [Updating container product availability by country in AWS Marketplace](container-update-offer-avail-country.md).

To let other AWS accounts view your product while it's in the Limited state, add them on the **Share with others for testing** card under **Step 4: Testing and integrations**. For the procedure, see [Updating the allowlist of AWS account IDs](container-product-getting-started.md#container-update-allowlist).

## Review and publish your product
<a name="container-step-9-publish"></a>

**To publish a container-based AI agent or tool product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Complete **Step 3: Procurement configuration** and **Step 4: Testing and integrations**.

   In Step 3, you create the public offer, which sets your pricing, refund policy, EULA, and offer availability.

1. (Optional) Complete **Step 5: Add-ons**.

1. Choose **View on AWS Marketplace**.

1. Review your product detail page for accuracy.

   Check that the usage instructions guide buyers through the steps to launch your product.

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

## Container deployment details
<a name="container-deployment-details"></a>

Container deployment packages your AI agent or tool as a containerized application that customers can run in their own AWS environments. This approach provides the following benefits:
+ Data remains within the customer's environment
+ Customizable deployment configurations
+ Supported integration with Bedrock AgentCore Runtime and customer's existing infrastructure

When listing a containerized agent, provide clear deployment instructions, resource requirements, and configuration options to ensure successful customer implementation.

### Technical requirements for Bedrock AgentCore Runtime Containers
<a name="bedrock-agentcore-runtime-requirements"></a>

For more information, see [Amazon Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md).

When creating container-based AI agent products for AWS Marketplace, follow these requirements:

MCP Server Requirements  
+ **Transport**: Stateless streamable-http only
+ **Session Management**: Platform automatically adds `Mcp-Session-Id` header for session isolation
+ **Host**: Container must listen on `0.0.0.0`
+ **Port**: Container must expose port `8000` for MCP server communication
+ **Path**: `/mcp` - POST endpoint for receiving MCP RPC messages. InvokeAgentRuntime for MCP servers will pass through requests to this path.
+ **Protocol**: The MCP server must support the MCP protocol including protocol messages 'tools/list' and 'tools/call' (supported by common framework such as FastMCP).

Agent Requirements  
+ **/ping** Endpoint: GET endpoint for health checks
+ **/invocations** Endpoint: POST endpoint for agent interactions
+ **Docker Container**: ARM64 containerized deployment package
+ **Port**: Container must expose port `8080` for HTTP-based agent communication
+ No hardcoded credentials
+ Free of Common Vulnerabilities and Exposures (CVEs)

A2A Server Requirements  
+ **Port**: A2A servers run on port 9000 (vs 8080 for HTTP, 8000 for MCP)
+ **Host**: Container must listen on `0.0.0.0`
+ **Path**: A2A servers are mounted at `/` (vs `/invocations` for HTTP, `/mcp` for MCP)
+ **Agent Cards**: A2A provides built-in agent discovery through Agent Cards at `/.well-known/agent-card.json`
+ **Protocol**: Uses JSON-RPC for agent-to-agent communication
+ **Authentication**: Supports both SigV4 and OAuth 2.0 authentication schemes

Usage instructions  
Ensure instructions thoroughly guides customers through launching and configuring the product. Refer to [Creating AMI and container product usage instructions for AWS Marketplace](ami-container-product-usage-instructions.md).

## Testing and validation
<a name="container-testing-validation"></a>

Before publishing your MCP-compatible agent or tool to public, thoroughly test your implementation:
+ Verify usage instructions provides necessary information to launch and configure the product.
+ Test authentication flows and error handling
+ Validate performance under various load conditions
+ Ensure compatibility with popular MCP clients
+ Document any client-specific configuration requirements

## Best Practices and Recommendations
<a name="container-best-practices"></a>

### Documentation Requirements
<a name="container-documentation-requirements"></a>

When listing an Model Context Protocol-compatible agent or tool on AWS Marketplace, include comprehensive documentation:
+ Detailed capability descriptions and examples
+ Authentication and configuration instructions
+ Sample code for common integration scenarios
+ Troubleshooting guides and error reference
+ Performance considerations and best practices

### Additional resources
<a name="container-additional-resources"></a>

For more information about implementing Model Context Protocol in your AI agent or tool, refer to these resources:
+ [Amazon Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
+ [Amazon Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md)
+ [Container Technical Requirements](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html)