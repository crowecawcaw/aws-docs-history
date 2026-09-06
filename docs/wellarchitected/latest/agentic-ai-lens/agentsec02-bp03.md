

# AGENTSEC02-BP03 Maintain approved tool registry with security assessments
<a name="agentsec02-bp03"></a>

 Every tool an agent can reach is part of its effective privilege surface. A version-controlled registry with documented security boundaries, enforced at invocation time, keeps unvetted or deprecated tools off the agent's call path. 

 **Desired outcome:** 
+  You maintain a centralized, version-controlled registry of approved tools, each with documented security boundaries, required permissions, data classification levels, and a current vulnerability assessment. 
+  Agents can access only tools present in the registry, and unapproved tools are blocked by default. 
+  You continually validate the registry for compliance, and deprecated tools are removed from agent access automatically. 

 **Common anti-patterns:** 
+  Allowing agents to discover and invoke any available tool or MCP server without prior security review and registry approval. 
+  Maintaining the tool registry as a static document rather than an enforced control, so agents can bypass it and invoke unapproved tools directly. 
+  Failing to distinguish between locally hosted tools and remote MCP servers in the risk assessment, underestimating the expanded scope from external network connectivity. 
+  Skipping version pinning for approved tools, so agents pick up new versions that have not undergone security review. 

 **Benefits of establishing this best practice:** 
+  A deny-by-default posture constrains agent capabilities to a pre-approved, security-reviewed set of tools and operations. 
+  Version control helps prevent agents from using tool versions that have not been reviewed and provides an audit trail of which versions were approved and when. 
+  Automated compliance checks detect drift from the approved registry and trigger remediation workflows. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A tool registry must be enforced at runtime to be effective. Document approved tools in a registry and configure the invocation path to refuse tools that are not on the list. The design pattern is a registry that agents can't bypass: tools reachable only through a gateway target, agents authorized only through a policy engine with default-deny semantics, and an out-of-band compliance process that detects drift between the registry and what is actually configured. 

 [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) provides the consolidation point for agent-to-tool traffic. Each gateway target represents a backend service or group of APIs exposed as tools to agents, with defined tool schemas, authentication configurations, and access controls. Gateway alone isn't deny-by-default, however: adding a target makes it immediately accessible as an MCP tool to any agent that reaches the gateway endpoint. To restrict which agents can invoke which tools, layer [Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) Cedar policies with a default-deny posture, Gateway Interceptor for custom Lambda-based access logic, or both. The policy layer is what turns a populated registry into enforced authorization. 

 Development environments need a second control. When developers and agents interact with MCP servers through IDE-based tools, an MCP registry, a JSON allowlist of approved servers hosted on an HTTPS endpoint such as Amazon S3 or an internal web server, gives clients a list of servers to fetch at startup and re-sync periodically (typically every 24 hours). Servers not in the registry are blocked, and if a locally installed server is removed from the registry, the client terminates it and helps prevent it from being re-added. The registry supports version pinning so that a new version automatically relaunches clients with the updated version, and the file format follows the [MCP Registry open standard](https://github.com/modelcontextprotocol/registry) so the investment isn't tied to a single tool or provider. MCP registry governance can be configured at the organization level with account-level overrides, for example disabling MCP for the organization by default but enabling it with a specific allowlist for certain teams. 

 At enterprise scale, a centralized MCP server hub consolidates what would otherwise become a proliferation of team-specific connections. Teams develop MCP servers for their specific functions, but servers are hosted centrally and accessible across the organization through a shared registry or discovery API backed by Amazon DynamoDB that catalogs available servers with their descriptions, tool definitions, and access requirements. Network-level access uses AWS PrivateLink and VPC endpoints so agents connect only to trusted organization-hosted servers, and each server runs as an isolated container on Amazon ECS with AWS Fargate for independent scaling without impact on other servers. 

 Remote MCP servers need a heightened security review. They introduce network connectivity to external services, expanding scope beyond the organization's direct control. Assess authentication mechanisms, data handling practices, and network exposure, and apply network controls such as VPC endpoints and security groups to restrict connectivity to the required endpoints. When onboarding tools to Gateway or the MCP registry, scan API specifications for security risks, validate authentication, assess data handling, enrich tool metadata with descriptions, usage examples, and performance characteristics, and group APIs into gateway targets by business domain, outbound authorization requirements, and API type. 

 Gateway supports six target types: 
+  Lambda functions 
+  API Gateway REST APIs 
+  OpenAPI schemas 
+  Smithy models 
+  External MCP servers 
+  Built-in templates from integration providers 

 Built-in templates provide pre-configured, curated integrations for popular SaaS platforms including Salesforce, Slack, Jira, Asana, Zendesk, and ServiceNow, with a vetted subset of provider APIs exposed through the gateway. Routing all tool access through Gateway (internal services, external MCP servers, and native SaaS integrations) consolidates authentication, schema enforcement, and policy evaluation under one endpoint. IDEs such as Kiro, Claude Code, and Cursor connect through the Amazon Bedrock AgentCore MCP Server, which bridges IDE-based MCP clients to the gateway endpoint. 

 Continuous compliance detection keeps the registry enforceable over time. Maintain a configuration store in Parameter Store, a capability of AWS Systems Manager or AWS AppConfig alongside the gateway configuration, with entries for tool name, approved version, required IAM permissions, data classification level, security review date, and expiration date. Use AWS Config rules to validate that agent deployments reference only registry-approved tools, and trigger Amazon EventBridge notifications for non-compliance. Automated deprecation workflows remove expired tools from the registry, update agent configurations, and help prevent continued use. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build the structured registry:** Create a tool registry in Parameter Store, a capability of AWS Systems Manager or AWS AppConfig with entries for each approved tool covering version, permissions, data classification, and review metadata. 

1.  **Add approved tools as Gateway targets:** For agent-to-tool traffic, register approved tools as [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) targets with defined tool schemas, outbound authentication configurations, and access controls. Group targets by business domain, authorization requirements, and API type. 

1.  **Publish an MCP registry for development:** Create an MCP registry JSON file that follows the [MCP Registry open standard](https://github.com/modelcontextprotocol/registry), host it on an HTTPS endpoint, and configure it in your organization's admin settings with version pinning for each server entry. 

1.  **Define the security review process:** Establish a review covering API specification scanning, permission assessment, data flow mapping, and authentication mechanism validation, with findings documented in the registry entry and a review expiration date. 

1.  **Build a centralized hub at enterprise scale:** For multi-LOB deployments, implement a centralized MCP server hub with an Amazon DynamoDB-backed discovery API, network-level access through AWS PrivateLink and VPC endpoints, and isolated container hosting on Amazon ECS with AWS Fargate. 

1.  **Enforce default-deny through Policy:** Configure Cedar policies in AgentCore Policy so only explicitly permitted tools can be invoked, providing a second enforcement layer beyond Gateway target configuration. 

1.  **Apply heightened review to remote MCP servers:** Assess network exposure and external authentication, and apply VPC endpoints and security groups to restrict connectivity. 

1.  **Detect registry drift continually:** Deploy AWS Config rules to detect agent configurations referencing unapproved tools, and trigger Amazon EventBridge notifications for remediation. 

1.  **Automate deprecation:** Expire tools past their review date, remove them from Gateway targets and the MCP registry, and update agent configurations to help prevent continued use. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC02-BP01 Implement tool authorization](agentsec02-bp01.html) 
+  [AGENTSEC02-BP02 Validate tool inputs and outputs](agentsec02-bp02.html) 
+  [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) 
+  [Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) 
+  [Transform your MCP architecture: Unite MCP servers through AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/) 
+  [Enterprise governance: control your MCP servers and models](https://kiro.dev/blog/enterprise-governance-mcp-and-models/) 
+  [MCP governance for Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-governance.html) 
+  [Accelerating AI innovation: Scale MCP servers for enterprise workloads with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerating-ai-innovation-scale-mcp-servers-for-enterprise-workloads-with-amazon-bedrock/) 
+  [Secure AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) 
+  [Parameter Store, a capability of AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) 

 **Related examples:** 
+  [Accelerating AI Innovation: Scaling Model Context Protocol Servers for Enterprise Workloads on AWS (GitHub)](https://github.com/aws-samples/sample-deploy-mcp-servers-at-scale-on-aws) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/) 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 