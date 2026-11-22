

# Scenario 7: Implementation of advertising agents with Ad Context Protocol (AdCP) framework

 The advertising workflow spans multiple sequential stages from lead intake through campaign execution to insights delivery. AI agents can automate operational tasks including RFP processing, pricing optimization, proposal assembly, campaign trafficking, performance monitoring, and reporting generation. The Ad Context Protocol (AdCP) provides a standardized open framework for AI agents to interact across the advertising value chain. 

## Characteristics
<a name="s07-characteristics"></a>
+  Multiple specialized AI agents (media buying, creative, signals, and governance) collaborating on advertising workflows through standardized protocols. 
+  Human-in-the-loop oversight is required at critical decision points (campaign approval, creative review, budget thresholds, policy exceptions). 
+  Governance agents enforce brand safety, frequency capping, privacy compliance, and quality measurement across all layers. 
+  Agents communicate over two transport protocols: MCP for AI assistants calling tools and A2A for agent-to-agent collaboration. 
+  Cost management requires per-agent token tracking and model selection aligned to task complexity, because not all tasks require flagship models. 
+  Delayed adoption of Agentic AI capabilities reduces competitive advantage for publishers, advertisers, and agencies. 

## Reference architecture
<a name="s07-reference-architecture"></a><a name="scenario-07-fig1"></a>

![Ad Context Protocol (AdCP) product roadmap showing the sequence of specialized advertising agents and capabilities](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-07a-adcp-product-roadmap.jpg)

*Ad Context Protocol (AdCP) product roadmap*
<a name="scenario-07-fig2"></a>

![Ad Context Protocol (AdCP) advertising agent architecture on AWS, part 1, showing the business principals, media orchestration platform with specialized agents, and execution layer](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-07b-advertising-agents-1.jpg)

*Advertising agents on AWS, part 1*


 The architecture consists of the following components: 

1.  **Media Orchestration Platform**: Evaluates sellers and audiences, executes buying strategies. Communicates with specialized agents through MCP (Model Context Protocol). Implemented using Amazon Bedrock multi-agent collaboration with a supervisor agent for dynamic routing decisions and AWS Step Functions for deterministic sequential workflows. 

1.  **Signals Agent (MCP Server)**: Exposes audience and targeting data discovery and activation capabilities. Accesses AWS Clean Rooms for privacy-preserved audience analysis, Amazon Bedrock Knowledge Bases for campaign intelligence, and real-time signals from Amazon Kinesis. 

1.  **Sales Agent (MCP Server)**: Exposes media product discovery and campaign execution capabilities. Manages campaign booking through DynamoDB-stored deal structures and inventory availability queries. 

1.  **Creative Agent (MCP Server)**: Exposes ad format discovery and AI-powered creative generation. Uses Amazon Bedrock (Amazon Nova Canvas for image generation, Claude for copy generation) with guardrails for brand safety and content policy enforcement. 

1.  **Agentic eXecution Engine (AXE)**: Real-time execution layer for brand suitability checks, frequency capping, first-party data activation, and dynamic audience targeting. Connects through key-value pairs or RTB protocols to the Decisioning Platform. 

1.  **Governance Agents**: Monitor across all layers: property lists, brand suitability scoring, quality measurement, ad density, and privacy compliance (COPPA, TCF, and GDPR). Operate at setup time, real-time, and post-bid. Implemented using Amazon Bedrock Guardrails and Cedar policy engine through AgentCore Policy. 

1.  **Amazon Bedrock AgentCore Runtime**: Serverless execution for all agent workloads with built-in session management, automatic scaling, and deployment workflows. Removes the need for manual container orchestration, session routing, and scaling logic. AgentCore Identity manages credentials, and AgentCore Policy (Cedar) enforces agent-to-tool interaction controls. 

1.  **Human-in-the-loop oversight**: Amazon SES or Slack integration through AWS Chatbot delivers approval requests to human reviewers at key decision points. AWS Step Functions Wait for Callback implements the approval gate. The workflow pauses until a reviewer approves or rejects through API Gateway \+ Lambda. 

## Configuration notes
<a name="s07-configuration-notes"></a>

### Agent infrastructure
<a name="agent-infrastructure"></a><a name="scenario-07-fig3"></a>

![Ad Context Protocol (AdCP) advertising agent architecture on AWS, part 2, showing agent deployment infrastructure, governance agents, and human-in-the-loop oversight points](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-07b-advertising-agents-2.jpg)

*Advertising agents on AWS, part 2*


 Deploy advertising agents using Amazon Bedrock AgentCore Runtime for serverless execution. Use AgentCore Gateway for MCP-compatible tool access. Configure AgentCore Policy (Cedar policy engine) for fine-grained agent-to-tool interaction controls. This reduces the operational overhead of managing ECS tasks or EKS pods for agent workloads. 

### Multi-agent orchestration patterns
<a name="multi-agent-orchestration-patterns"></a>

 Implement deterministic advertising workflows (campaign planning, trafficking, and reporting) as AWS Step Functions Express Workflows that invoke agents sequentially. This bypasses supervisor agent overhead and avoids per-step routing inference costs. Use Bedrock multi-agent collaboration (with supervisor) only for workflows that require dynamic routing decisions based on input content. 

### Model selection by task complexity
<a name="model-selection-by-task-complexity"></a>

 Assign task-appropriate models: lightweight models (Amazon Nova Lite, Claude Haiku) for classification tasks (brand safety screening, ad format detection, audience segment matching), and capable models (Claude Sonnet, Amazon Nova Pro) for complex reasoning (media strategy generation, creative concept development). Configure Amazon Bedrock Intelligent Prompt Routing for agents handling variable-complexity queries. 

### Cost controls
<a name="cost-controls"></a>

 Set MaxIterations on all agents (start at 5, increase only when needed). Set timeouts on all external tools (Lambda functions, API endpoints). Use Amazon Bedrock Prompt Caching for stable context blocks (campaign taxonomies, channel definitions, brand safety rule sets) that appear in every invocation. Cached tokens cost up to 90% less than standard input tokens. Track cost-per-business-outcome using Bedrock inference profiles and Quick dashboards. 

### Security and identity
<a name="security-and-identity"></a>

 Use Amazon Bedrock AgentCore Identity for credential management. Grant agents minimal permissions scoped to their specific function. Bid optimization agents should not have access to creative asset storage or financial reporting. Implement RBAC for agent actions with separate IAM roles per agent type. Use short-lived OAuth 2.1 and AWS STS credentials for machine-to-machine communications. 