# Listing Container-based AI agent products

## Start the listing wizard

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/homepage/ "https://aws.amazon.com/marketplace/management/homepage/") with your AWS seller account.
2. Select **Products** and then select **AI Agents and Tools** in the navigation bar.
3. Select the **Create AI Agents and Tools product**
   menu, then choose **Container-based AI agents &
   tools**.
4. Select **Generate product ID and product code**.
5. (Optional) Add tags to support tag-based authorization.
6. Select **Continue**.

## Step 1: Provide product Information

1. In **Product information**, enter:
   - **Product title**
   - **Product logo S3 URL**
   - **Short description**
   - **Long description**
   - **Highlight (1-3)**

2. Enter support details and add optional learning resources by choosing Add resource.
3. In the **Product categories** menu, choose 1-3 categories. We recommend that you choose at least one category from the **AI Agents & Tools** business categories.
4. Enter keywords to improve search discoverability.
5. (Optional) Add video and image assets according to the guidelines.
6. Choose **Next**.

## Step 2: Configure AI Agent Container pricing

1. Choose pricing model.

###### AgentCore pricing limitations

If the container image utilizes AgentCore, the **Hourly**
and **Usage with long-term contract** pricing models are
not supported. To learn more about contract pricing, see
[Contract pricing for container products](pricing-container-products.md#container-contracts "pricing-container-products.md#container-contracts").
To learn more about custom metering for usage-based
pricing, see [Usage pricing](usage-pricing.md "usage-pricing.md"). 2. Select **Next**. 3. In **Set prices**. 4. Select **Next**.

## Step 3: Specify refund policy

1. Enter a refund policy.
2. Select **Next**.

###### Note

If you chose the free product pricing model, you do not have to enter a refund policy.

## Step 4: Configure EULA

1. Choose **Standard Contract for AWS Marketplace** or **Custom EULA**.

###### Note

If you choose Custom EULA, enter a URL for the end-user license agreement. 2. Select **Next**.

## Step 5: Add repositories

1. Add an initial repository for your container product.

###### Note

Repository names must be unique across all products in your seller account. You can create up to 50 repositories per product. 2. Select **Next**.

## Step 6: Configure offer availability / Allow list

1. In **Configure offer availability**, choose your geographic availability settings.
2. Select **Next**.
3. In **Configure allowlist**, list any AWS accounts that should have access to the listing while in the limited state.
4. Select **Submit** to create a new change request for limited visibility testing.

Wait 10-15 minutes until your request status is in the _Succeeded_ state.

## Step 7: Upload Container images and artifacts to repository

###### Note

See [AWS Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md "bedrock-agentcore-runtime.md") on how to integrate AgentCore with your Container Image.

1. Locate the URL for the ECR repository:
   - Open the Server products page in AWS Marketplace Management Portal.
   - Select your container product to view the details.
   - Select the Repositories tab to copy the URL of the repository.

2. Select **View push commands** to open a list of instructions, including commands you can use to push Docker container images and Helm charts to that repository. For general information about how to push container images and other artifacts to repositories, see [Pushing an image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md") in the Amazon Elastic Container Registry User Guide.

###### Note

You can use the following Amazon Elastic Container Registry (Amazon ECR) API operations when calling docker pull or docker push:

    * DescribeImages - Use this to review the metadata about the images in a repository.
    * GetAuthorizationToken - Use to authenticate before uploading artifacts to the repository, then use docker pull or docker push commands.
    * ListImages - Use to view a list of images you pushed.

3. Use the commands listed to push any needed artifacts from your local repository to the AWS Marketplace repository for your product.

###### Note

The tag that you provide in the push commands is used to differentiate the version of the artifact that you are uploading to the repository. Use a tag that makes sense for the version the artifacts are a part of. 4. Repeat for each container image or artifact you need in your version.

###### Note

Your version can include up to 50 container images or artifacts in each delivery option. Refer to the following procedure for more information about delivery options. 5. After you upload your artifacts, you're ready to create the version of your product.

###### Note

Your container images are scanned automatically to see if they meet the [Container-based product requirements for AWS Marketplace](container-product-policies.md "container-product-policies.md"). For more information, see [Container product scans for security issues](container-product-getting-started.md#container-security "container-product-getting-started.md#container-security").

## Step 8: Add New Product Version with Assets

1. Open the **AI Agents and Tools** products page in the
   AWS Marketplace Management Portal.
2. Select your container product and click the **Request changes** dropdown menu, select **Update versions**, and select **Add new version**.
3. In **Delivery options**, enter:
   - **Version title**
   - **Release notes**

4. Select **Add delivery option**.
5. For **Delivery method**, select **Container image** and fill in:
   - **Supported services**: select the environment that buyers can launch the software in.
   - For **Bedrock AgentCore** service, **Type** select
     **AI Agent** or **MCP Server**
   - **Container image**: _Repository URL_ and _version tag_
     you specified previously.
   - **Delivery option title** and **Deployment option description**:
     Enter a title and description for this delivery option.
   - **Usage instructions**: Enter detailed information to help your buyers use your software after launching it.

6. If you selected an **AI agent** tool type, confirm that your agent uses
   reasoning LLMs and demonstrates autonomous capabilities. These requirements help
   ensure that agents offered on AWS Marketplace meet a high quality bar. If your
   agent does not meet both requirements, choose a different tool type.
7. Select **Add version**.

Wait and refresh the page until the request status shows _Succeeded_.

Adding a new version automatically scans the container images for vulnerabilities.

## Step 9: Review Product Listing and Publish to Public

1. Open the **AI Agent and Tools** products page in the
   AWS Marketplace Management Portal.
2. Select your container product in the list.
3. Select **View on AWS Marketplace**.
4. Review your product detail page for accuracy. Ensure the usage instructions sufficiently guide the buyer through the necessary steps to launch your product.
5. Submit an Update visibility request to public:
   - From the **Server products** page, on the **Current server product** tab, select the container-based product that you want to modify. From the **Request changes** dropdown, choose **Update visibility**.

## Container deployment details

Container deployment packages your AI agent or tool as a containerized application that customers can run in their own AWS environments. This approach provides the following benefits:

- Data remains within the customer's environment
- Customizable deployment configurations
- Supported integration with Bedrock AgentCore Runtime and customer's existing infrastructure

When listing a containerized agent, provide clear deployment instructions, resource requirements, and configuration options to ensure successful customer implementation.

### Technical requirements for Bedrock AgentCore Runtime Containers

###### Note

See [AWS Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md "bedrock-agentcore-runtime.md") for more details.

When creating container-based AI agent products for AWS Marketplace, follow these requirements:

MCP Server Requirements

- **Transport**: Stateless streamable-http only
- **Session Management**: Platform automatically adds `Mcp-Session-Id` header for session isolation
- **Host**: Container must listen on `0.0.0.0`
- **Port**: Container must expose port `8000` for MCP server communication
- **Path**: `/mcp` - POST endpoint for receiving MCP RPC messages. InvokeAgentRuntime for MCP servers will pass through requests to this path.
- **Protocol**: The MCP server must support the MCP protocol including protocol messages 'tools/list' and 'tools/call' (supported by common framework such as FastMCP).

Agent Requirements

- **/ping** Endpoint: GET endpoint for health checks
- **/invocations** Endpoint: POST endpoint for agent interactions
- **Docker Container**: ARM64 containerized deployment package
- **Port**: Container must expose port `8080` for HTTP-based agent communication
- No hardcoded credentials
- Free of Common Vulnerabilities and Exposures (CVEs)

Usage instructions

Ensure instructions thoroughly guides customers through launching and configuring the product. Refer to [Creating AMI and container product usage
instructions for AWS Marketplace](ami-container-product-usage-instructions.md "ami-container-product-usage-instructions.md").

## Testing and validation

Prior to publishing your MCP-compatible agent or tool to public, thoroughly test your implementation:

- Verify usage instructions provides necessary information to launch and configure the product.
- Test authentication flows and error handling
- Validate performance under various load conditions
- Ensure compatibility with popular MCP clients
- Document any client-specific configuration requirements

## Best Practices and Recommendations

### Documentation Requirements

When listing an Model Context Protocol-compatible agent or tool on AWS Marketplace, include comprehensive documentation:

- Detailed capability descriptions and examples
- Authentication and configuration instructions
- Sample code for common integration scenarios
- Troubleshooting guides and error reference
- Performance considerations and best practices

### Additional resources

For more information about implementing Model Context Protocol in your AI agent or tool, refer to these resources:

- [Amazon Bedrock AgentCore Documentation](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md")
- [AWS Bedrock AgentCore Runtime for AWS Marketplace](bedrock-agentcore-runtime.md "bedrock-agentcore-runtime.md")
- [Container Technical Requirements](container-product-getting-started.md "container-product-getting-started.md")
