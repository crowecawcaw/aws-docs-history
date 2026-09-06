

# Listing Container-based AI agent products
<a name="listing-container-ai-agents"></a>

## Managing container-based AI agents and tools
<a name="managing-container-ai-agents"></a>

Container-based AI agents and tools running on Amazon Bedrock AgentCore Runtime can be managed through the unified **AI agents and tools** products page or the **Server** products page in the AWS Marketplace Management Console. Only products with versions that support Amazon Bedrock AgentCore Runtime will be visible in the **AI agents and tools** product page.

## Start the listing wizard
<a name="start-container-listing-wizard"></a>

1. Sign in to [AWS Partner Central](https://aws.amazon.com/marketplace/management/homepage/) with your AWS seller account.

1. Select **Build** and then select **AI Agents and Tools** in the navigation bar.

1. Select the **Create AI Agents and Tools product** menu, then choose **Container-based AI agents & tools**.

1. Select **Generate product ID and product code**. 

1. (Optional) Add tags to support tag-based authorization.

1. Select **Continue**.

## Step 1: Provide product Information
<a name="container-step-1-product-info"></a>

**Use AI-assisted product listing**  
You can use AI-assisted product listing in AWS Partner Assistant to generate product information for this step from a website URL or uploaded documents. The tool scores listing quality against AWS Marketplace standards and provides field-level recommendations to improve discoverability and buyer engagement before you submit. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

1. In **Product information**, enter:
   + **Product title**
   + **Product logo S3 URL**
   + **Short description**
   + **Long description**
   + **Highlight (1-3)**

1. Enter support details and add optional learning resources by choosing Add resource.

1. In the **Product categories** menu, choose 1-3 categories. We recommend that you choose at least one category from the **AI Agents & Tools** business categories.

1. Enter keywords to improve search discoverability.

1. (Optional) Add video and image assets according to the guidelines.

1. Choose **Next**.

## Step 2: Configure AI Agent Container pricing
<a name="container-step-2-pricing"></a>

1. Choose pricing model.
**AgentCore pricing limitations**  
If the container image uses AgentCore, the **Hourly** and **Usage with long-term contract** pricing models are not supported. To learn more about contract pricing, see [Contract pricing for container products with AWS License Manager](container-license-manager-integration.md). To learn more about custom metering for usage-based pricing, see [Configuring custom metering for container products with AWS Marketplace Metering Service](container-metering-meterusage.md).

1. Select **Next**.

1. In **Set prices**.

1. Select **Next**.

## Step 3: Specify refund policy
<a name="container-step-3-refund"></a>

1. Enter a refund policy.

1. Select **Next**.

**Note**  
If you chose the free product pricing model, you do not have to enter a refund policy.

## Step 4: Configure EULA
<a name="container-step-4-eula"></a>

1. Choose **Standard Contract for AWS Marketplace** or **Custom EULA**.
**Note**  
If you choose Custom EULA, enter a URL for the end-user license agreement.

1. Select **Next**.

## Step 5: Add repositories
<a name="container-step-5-repositories"></a>

1. Add an initial repository for your container product.
**Note**  
Repository names must be unique across all products in your seller account. You can create up to 50 repositories per product.

1. Select **Next**.

## Step 6: Configure offer availability / Allow list
<a name="container-step-6-availability"></a>

1. In **Configure offer availability**, choose your geographic availability settings.

1. Select **Next**.

1. In **Configure allowlist**, list any AWS accounts that should have access to the listing while in the limited state.

1. Select **Submit** to create a new change request for limited visibility testing.

   Wait 10-15 minutes until your request status is in the *Succeeded* state.

## Step 7: Upload Container images and artifacts to repository
<a name="container-step-7-upload"></a>

**Note**  
See [Amazon Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md) on how to integrate AgentCore with your Container Image.

1. Locate the URL for the ECR repository:
   + Open the Server products page in AWS Partner Central.
   + Select your container product to view the details.
   + Select the Repositories tab to copy the URL of the repository.

1. Select **View push commands** to open a list of instructions, including commands you can use to push Docker container images and Helm charts to that repository. For general information about how to push container images and other artifacts to repositories, see [Pushing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the Amazon Elastic Container Registry User Guide.
**Note**  
You can use the following Amazon Elastic Container Registry (Amazon ECR) API operations when calling docker pull or docker push:  
DescribeImages - Use this to review the metadata about the images in a repository.
GetAuthorizationToken - Use to authenticate before uploading artifacts to the repository, then use docker pull or docker push commands.
ListImages - Use to view a list of images you pushed.

1. Use the commands listed to push any needed artifacts from your local repository to the AWS Marketplace repository for your product.
**Note**  
The tag that you provide in the push commands is used to differentiate the version of the artifact that you are uploading to the repository. Use a tag that makes sense for the version the artifacts are a part of.

1. Repeat for each container image or artifact you need in your version.
**Note**  
Your version can include up to 50 container images or artifacts in each delivery option. Refer to the following procedure for more information about delivery options.

1. After you upload your artifacts, you're ready to create the version of your product.
**Note**  
Your container images are scanned automatically to see if they meet the [Container-based product requirements for AWS Marketplace](container-product-policies.md). For more information, see [Container product scans for security issues](container-product-getting-started.md#container-security).

## Step 8: Add New Product Version with Assets
<a name="container-step-8-version"></a>

1. Open the **AI Agents and Tools** products page in AWS Partner Central.
**Note**  
Only container products with versions that support Amazon Bedrock AgentCore Runtime are visible in the **AI Agents and Tools** products page. Before adding the first version, you will only find your product within the **Server** products page in AWS Partner Central. Once you've created the version for Amazon Bedrock AgentCore Runtime, you will find your container product within the **AI Agents and Tools** products page.

1. Select your container product and choose the **Request changes** dropdown menu, select **Update versions**, and select **Add new version**.

1. In **Delivery options**, enter:
   + **Version title**
   + **Release notes**

1. Select **Add delivery option**.

1. For **Delivery method**, select **Container image** and fill in:
   + **Supported services**: select the environment that buyers can launch the software in.
   + For **Bedrock AgentCore** service, select **AI Agent, MCP Server, or A2A Server** in the **Type** field.
   + **Container image**: *Repository URL* and *version tag* you specified previously.
   + **Delivery option title** and **Deployment option description**: Enter a title and description for this delivery option.
   + **Usage instructions**: Enter detailed information to help your buyers use your software after launching it.
   + **Environment Variables**: Specify the environment variables buyers must provide to configure the runtime behavior of the agent. These variables can be used to pass settings, credentials, or custom flags to the container at startup. For each variable, provide the name as expected by your container, a description, and an optional default value. For variables such as credentials or API keys that are unique, do not provide a default value. You can use the description to specify details about the variable as well as possible values. All of the provided variables with their default values will be pre-populated when buyers launch your product.

1. If you selected an **AI agent** or **A2A Server** tool type, confirm that your agent uses reasoning LLMs and demonstrates autonomous capabilities. These requirements help ensure that agents offered on AWS Marketplace meet a high quality bar. If your agent does not meet both requirements, choose a different tool type.

1. Select **Add version**.

   Wait and refresh the page until the request status shows *Succeeded*.

   Adding a new version automatically scans the container images for vulnerabilities.

## Step 9: Review Product Listing and Publish to Public
<a name="container-step-9-publish"></a>

1. Open the **AI Agent and Tools** products page in AWS Partner Central.

1. Select your container product in the list.

1. Select **View on AWS Marketplace**.

1. Review your product detail page for accuracy. Ensure the usage instructions sufficiently guide the buyer through the necessary steps to launch your product.

1. Submit an Update visibility request to public:
   + From the **Server products** page, on the **Current server product** tab, select the container-based product that you want to modify. From the **Request changes** dropdown, choose **Update visibility**.

## Container deployment details
<a name="container-deployment-details"></a>

Container deployment packages your AI agent or tool as a containerized application that customers can run in their own AWS environments. This approach provides the following benefits:
+ Data remains within the customer's environment
+ Customizable deployment configurations
+ Supported integration with Bedrock AgentCore Runtime and customer's existing infrastructure

When listing a containerized agent, provide clear deployment instructions, resource requirements, and configuration options to ensure successful customer implementation.

### Technical requirements for Bedrock AgentCore Runtime Containers
<a name="bedrock-agentcore-runtime-requirements"></a>

**Note**  
See [Amazon Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md) for more details.

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