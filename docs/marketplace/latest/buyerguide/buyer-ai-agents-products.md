

# AI agent products
<a name="buyer-ai-agents-products"></a>

AI agents and tools in AWS Marketplace help you quickly deploy pre-built, production-ready AI capabilities from trusted partners without months of development work. You can discover specialized AI agents for tasks like customer service, content creation, and data analysis, as well as individual AI tools like guardrails, knowledge bases, and integration protocols.

## What are AI agents?
<a name="what-are-ai-agents-buyer"></a>

AI agents are autonomous software systems that use AI to reason, plan, and complete tasks on your behalf. Unlike traditional systems that follow fixed rules, agents operate independently and adapt through multi-step processes. They combine foundation models for reasoning and planning with discrete tools to process requests, retrieve information, and execute tasks such as searching knowledge bases, calling APIs, or updating systems based on your needs.

AI agents can handle complex workflows by:
+ Perceiving their environment across multiple modalities (text, image, audio, and video)
+ Making decisions based on context and goals
+ Taking actions to achieve specific objectives
+ Adapting their approach based on results

## What are AI tools?
<a name="what-are-ai-tools-buyer"></a>

AI tools are specialized components that enhance and support AI agent functionality. AI tools include the following types:
+ **Guardrails** – Security and compliance controls that ensure AI safety and prevent misuse.
+ **Knowledge bases** – Specialized data sources that provide domain expertise and contextual information.
+ **Integration protocols** – Standards like AWS MCP Server(MCPl) that enable seamless communication between systems.
+ **Business logic components** – Custom workflows and decision-making rules that define how the system processes information and executes tasks.

## Discovery and deployment options
<a name="discovery-deployment-options-buyer"></a>

You can find AI agents and tools through multiple methods:

### Semantic search
<a name="semantic-search-buyer"></a>

Use natural language prompts to discover relevant agents and tools. For example, search for "social media content creator" or "data analysis assistant" to see recommended solutions with descriptions, key features, and user ratings.

### Category browsing
<a name="category-browsing-buyer"></a>

Browse by business use case categories such as:
+ Content creation
+ Customer service
+ Data analysis
+ Security and compliance
+ Marketing automation

You can learn more about AI agent and tool discovery in [Discovering AI agents and tools](ai-agent-discovery.md).

### Deployment flexibility
<a name="deployment-flexibility-buyer"></a>

Choose from multiple deployment options based on your security and integration requirements:
+ **API-based deployment** - Access vendor-hosted agents through API endpoints
+ **Container deployment** - Run agents in your own AWS environment

## Dynamic endpoints
<a name="dynamic-endpoints-buyer"></a>

Some API-based AI agent products provide **dynamic endpoints**—personalized endpoint URLs that are automatically configured for you after subscription. Instead of a static URL that is the same for all buyers, a dynamic endpoint contains placeholder variables that resolve to values specific to your account. For example, a template like `https://{tenantId}.apps.example.com/mcp` resolves to a URL such as `https://acme-corp.apps.example.com/mcp` after you complete setup.

To set up a product with a dynamic endpoint, complete the following steps:

1. Subscribe to the product through AWS Marketplace.

1. On the fulfillment page, view the endpoint template and choose **Setup Account**.

1. Complete registration on the seller's site. The seller provisions your dedicated environment during this step.

1. Return to the AWS Marketplace fulfillment page. The endpoint URL is automatically resolved with your personalized values.

1. Copy the resolved URL for direct use, or choose **Add to AgentCore Gateway** to register the endpoint with Amazon Bedrock AgentCore Gateway.

After the endpoint resolves, the seller delivers your credentials securely to your AWS Secrets Manager. The resolved URL works immediately with no manual editing required.

If the endpoint does not resolve within a few minutes after you complete registration, choose **Refresh** on the fulfillment page. If the endpoint remains unresolved, contact the seller using the support information on the product detail page.

**Note**  
The **Add to AgentCore Gateway** button activates only after the endpoint is fully resolved. For products with static endpoints, the URL is immediately available without additional setup.

## Model Context Protocol (MCP) support
<a name="mcp-support-buyer"></a>

Many AI agents and tools support the AWS MCP Server, an open standard that enables seamless communication between AI systems. MCP-enabled solutions can be easily integrated into your existing agentic ecosystems, including:
+ Claude Desktop
+ Windsurf
+ Amazon Bedrock Agents
+ Other MCP-compatible platforms

When you purchase MCP-enabled agents or tools, AWS Marketplace simplifies authentication and provides configuration parameters for plug-and-play deployment.

## Integration with AWS services
<a name="integration-aws-services-buyer"></a>

AI agents and tools from AWS Marketplace integrate seamlessly with AWS AI services:
+ **Amazon Bedrock AgentCore** – Incorporate third-party capabilities into your Bedrock workflows. For more information, see [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html).
+ **Amazon Q** – Extend Q's capabilities with specialized agents and tools.
+ **AWS Lambda** – Deploy agents as serverless functions.
+ **Amazon ECS/EKS** – Run containerized agents at scale.

## Getting started
<a name="getting-started-buyer"></a>

To get started with AI agents and tools:

1. **Browse the catalog** – Visit the **AI Agents & Tools** section in AWS Marketplace.

1. **Evaluate options** – Review product descriptions, compliance certifications, and user ratings.

1. **Subscribe** – Complete the subscription process through standard AWS Marketplace workflows.

1. **Deploy** – Configure and deploy using your preferred method (API, container, or SaaS).

1. **Integrate** – Connect agents and tools to your existing workflows and systems.

For more information about specific deployment methods, refer to:
+ [Container products in AWS Marketplace](buyer-what-is-aws-marketplace-for-containers.md)
+ [SaaS products through AWS Marketplace](buyer-saas-products.md)