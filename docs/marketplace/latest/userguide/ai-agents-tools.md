# AI agent products

## What are AI agent products?

AI agents are software systems that leverage artificial intelligence to reason, plan, and complete tasks on behalf of humans or systems. Unlike traditional software that follows fixed rules, AI agents operate independently, adapting through multi-step processes to achieve specific goals.

AI agents combine foundation models for reasoning and planning with discrete agentic tools (like guardrails, knowledge bases, and business logic) to process requests, retrieve information, and execute tasks. They can search knowledge bases, call APIs, update systems, and make decisions based on user needs and environmental context.

Agentic tools are specialized components that enhance AI agent capabilities, including:

- Knowledge bases for domain-specific information
- Guardrails for safety and compliance
- Integration protocols like Model Context Protocol (MCP)
- Specialized APIs and microservices
- Business logic components and workflows

## Types of AI agents and tools suitable for AWS Marketplace

AWS Marketplace supports a wide variety of AI agents and tools across different industries and use cases. Common types include the following, though this is not an exhaustive list:

**Content-creation agents**

Agents that generate, edit, or optimize content including text, images, videos, and multimedia. Examples include writing assistants, social media content generators, and marketing automation agents.

**Data-analysis agents**

Agents that process, analyze, and derive insights from data. Examples include business intelligence agents, financial analysis tools, and predictive analytics systems.

**Customer-service agents**

Agents that handle customer interactions, support requests, and service automation. Examples include chatbots, ticket routing systems, and customer experience optimization tools.

**Business-process-automation agents**

Agents that automate complex business workflows and processes. Examples include document processing agents, approval workflow systems, and compliance automation tools.

**Security and compliance agents**

Agents that monitor, detect, and respond to security threats or compliance requirements. Examples include threat detection systems, audit automation tools, and risk assessment agents.

**Developer-tools agents**

Agents that assist with software development, testing, and deployment. Examples include code generation assistants, testing automation agents, and deployment optimization tools.

**Agentic tools**

Specialized components that enhance other AI agents, including knowledge bases, guardrails, and integration protocols such as Model Context Protocol (MCP).

## Deployment options for AI agent products

AWS Marketplace supports multiple deployment options for AI agents, allowing you to choose the approach that best fits your architecture and customer needs:

- **API deployment option** – The API deployment option allows customers to access your AI agent through vendor-hosted endpoints. This option is ideal for agents and agent tools that require specialized infrastructure or proprietary models that you want to keep in your own environment.
- **Container deployment** – Package your AI agent and agentic tools as containerized applications that customers can run in their own AWS environments. This option provides customers with greater control over their data and infrastructure.

## Choosing the right deployment option

When selecting a deployment option for your AI agent or tool, consider the following factors:

- **Data sensitivity** – If your customers work with highly sensitive data that cannot leave their environment, container deployment may be the best option.
- **Model complexity** – For large or complex models that require specialized hardware, API deployment might be more practical.
- **Operational overhead** – Consider the resources required to maintain and update your solution across different deployment models.

Here is a quick feature comparison between the deployment options:

| Feature                     | API Deployment                            | Container Deployment                                |
| --------------------------- | ----------------------------------------- | --------------------------------------------------- |
| Hosting                     | Vendor-hosted endpoints                   | Customer's own AWS environment                      |
| Data control                | Data processed on vendor servers          | Greater customer control over data                  |
| Infrastructure requirements | Minimal - uses vendor infrastructure      | Requires customer to manage infrastructure          |
| Scalability                 | Managed by vendor                         | Customer controlled, potentially more flexible      |
| Customization               | Limited - based on API capabilities       | High - full control over the environment            |
| Maintenance                 | Handled by vendor                         | Customer responsible for updates and maintenance    |
| Security                    | Dependent on vendor's security measures   | Customizable security based on customer needs       |
| Updates and improvements    | Automatically provided by vendor          | Manual updates required, but on customer's schedule |
| Regulatory compliance       | May be limited by vendor's certifications | Easier to adapt to specific regulatory requirements |
