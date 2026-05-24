# Release notes for Amazon Bedrock AgentCore

We recommend subscribing to the RSS feed so updates to these notes are delivered to your Inbox.

## May 2026

### Harness: Bring-Your-Own File System (Amazon S3 Files and Amazon EFS)

AgentCore harnesses now support Amazon S3 Files and Amazon EFS access points alongside managed session storage. Attach access points at `CreateHarness` or `UpdateHarness` time and the harness mounts them into every session at a path you specify. Use S3 Files for round-trip with an S3 bucket, EFS for low-latency shared storage, or combine up to five mounts on a single harness. See [Filesystem](harness-memory.md#harness-filesystem "harness-memory.md#harness-filesystem").

### Runtime: Bring-Your-Own File System (Amazon S3 Files and Amazon EFS)

Developers can now attach Amazon S3 Files and Amazon EFS access points directly to agent runtimes. AgentCore Runtime mounts the file system into every session at a path you specify, and your agent reads and writes using standard file operations — no custom mount code, no privileged containers, and no download orchestration required. Mount an S3 Files file system for automatic synchronization between file operations and the S3 bucket, or an EFS access point for a shared NFS file system with sub-millisecond latency. This enables agents to load shared skills, prompt templates, or datasets at session start without re-downloading, persist intermediate results across sessions, and collaborate on the same data across multiple agents. Available across all 15 AWS Regions where AgentCore Runtime is supported. See [File system configurations in AgentCore Runtime](runtime-filesystem-configurations.md "runtime-filesystem-configurations.md").

### Agent Performance Loop: Optimization, Batch Evaluation, and User Simulation

Three new capabilities close the observe-evaluate-optimize-deploy loop, enabling teams to continuously improve agent quality using real production data. Optimization analyzes production traces and evaluator outputs to recommend targeted updates to system prompts and tool descriptions, with built-in A/B testing to validate changes before rollout. Batch evaluation replays curated or historical sessions to compare pre/post scores and catch regressions before changes reach end users. User simulation generates realistic, multi-turn conversations using LLM-backed actors to reveal behaviors beyond scripted test cases. See [Optimization](optimization.md "optimization.md"), [Batch Evaluations](batch-evaluations-getting-started.md "batch-evaluations-getting-started.md"), and [User Simulation](user-simulation.md "user-simulation.md").

### AgentCore is generally available in AWS GovCloud (US-West)

Enterprise-grade agentic AI capabilities are now available for workloads with elevated compliance needs. With AgentCore, organizations can accelerate agents from prototype to production using any framework and any model, while maintaining the security and compliance controls required for government and regulated workloads. For details about AgentCore in AWS GovCloud (US), visit the [GovCloud Documentation](../../../govcloud-us/latest/UserGuide/govcloud-bedrock-agentcore.md "../../../govcloud-us/latest/UserGuide/govcloud-bedrock-agentcore.md").

### Amazon Bedrock AgentCore payments is now in Preview

Teams can now enable AI agents to autonomously access and pay for APIs, MCP servers, web content, and other agents. Built in partnership with Coinbase and Stripe, AgentCore payments is the first managed payment capabilities purpose-built for autonomous agents, handling the full payment lifecycle from wallet authentication through transaction execution to spending governance and observability. As AI agents become more capable and services shift to pay-per-use models built for machine consumption, developers need infrastructure that lets their agents transact without building bespoke billing integrations, credential management, orchestration logic, budgeting, and observability from scratch. See [documentation](payments.md "payments.md").

### Runtime: Custom Header Passthrough

AgentCore now supports passing arbitrary custom headers through to agents, aligned with Gateway’s header propagation model. Previously restricted to `Authorization` and `X-Amzn-Bedrock-AgentCore-Runtime-Custom-*` headers only, customers can now forward headers like transitive authentication tokens and webhook signatures without modification. See [documentation](runtime-header-allowlist.md "runtime-header-allowlist.md").

## April 2026

### Identity, Gateway, and Runtime: VPC Egress Support

Identity, Gateway, and Runtime now support secure egress to resources within customer VPCs, available in managed and self-managed configurations. Enables agents to invoke private resources (e.g., EKS-hosted MCP servers) directly through Gateway and connect to Identity Providers operating within customer VPCs. Includes private DNS resolution for managed VPC egress. See documentation for more details: [Gateway](gateway-quick-start.md "gateway-quick-start.md") | [Identity](identity-private-idp.md "identity-private-idp.md").

### Runtime: Node.js Direct Code Deployment

AgentCore now supports Node.js as a managed language runtime for direct code deployment, alongside existing Python support. Developers can package their Node.js-based agents into a .zip archive without building or managing container images. See [documentation](runtime-get-started-code-deploy-node.md "runtime-get-started-code-deploy-node.md").

### Agent Optimization Loop capabilities in Public Preview

AgentCore launches recommendations and two validation methods (batch evaluations and A/B tests), completing the observe-evaluate-improve loop for production agents. Developers can now act on evaluation findings through systematic, validated improvements rather than manual intervention. See [documentation](optimization.md "optimization.md").

### Identity: On-Behalf-Of (OBO) Token Exchange

AgentCore Identity now supports OBO token exchange, enabling agents to securely access protected resources on behalf of authenticated users without requiring multiple consent flows. See [documentation](on-behalf-of-token-exchange.md "on-behalf-of-token-exchange.md").

### Region Expansion: São Paulo and Canada Central

AgentCore Identity, Runtime, Code Interpreter, Browser Tool, Gateway, Policy, and Observability are now generally available in São Paulo (GRU). Policy launched in Canada Central (YUL).

### Memory: Structured Metadata Filtering on Long-Term Memory

Teams can now attach structured attributes to memory records and narrow retrieval to only results that match specific values, like priority, department, tags, or time range. Indexed keys can be declared when creating a memory (and cannot be removed once created), metadata schemas can be configured on strategies for automatic LLM extraction from conversations, and metadata filters can be applied when retrieving or listing memory records. See [documentation](long-term-memory-metadata.md "long-term-memory-metadata.md").

### Observability: Trace Latency Improvements

Put-to-get latency for complete traces (spans and logs) reduced to under 10 seconds. Previous release had reduced latency to 10 seconds for spans and 30 seconds for logs separately.

### AgentCore harness is now in Public Preview

Teams can now deploy production-ready AI agents without building infrastructure from scratch. The managed harness provides tools, environment management, context systems, memory, identity controls, and observability — all configurable through three API calls. Supports any model provider (Bedrock, Anthropic, OpenAI, Gemini) and runs agents in secure isolated microVMs with persistent memory. See [documentation](harness.md "harness.md").

### AgentCore MCP Server in awslabs/mcp

Your coding agent can now spin up an AgentCore agent, cloud browser, run code in a Code Interpreter sandbox, or stand up a Memory resource from any MCP-compatible client (Kiro, Claude Code, Cursor, and others) — without writing a single boto3 call. The official AgentCore MCP server in [awslabs/mcp](https://github.com/awslabs/mcp "https://github.com/awslabs/mcp") covers Runtime, Memory, Browser, and Code Interpreter, and authenticates through your default AWS credential chain. See [documentation](https://github.com/awslabs/mcp/blob/main/src/amazon-bedrock-agentcore-mcp-server/README.md "https://github.com/awslabs/mcp/blob/main/src/amazon-bedrock-agentcore-mcp-server/README.md") for installation notes.

### AgentCore CLI: Agent Inspector

Developers running `agentcore dev` now get a browser-based UI for chatting with agents, inspecting token usage and tool calls, viewing execution traces on a timeline, and browsing deployed AgentCore Memory — all locally before pushing to the cloud. See [documentation](agentcore-get-started-cli.md "agentcore-get-started-cli.md").

### Observability: UI Enhancements for Trace and Trajectory

Trace tree details now bundle repeated spans, add visual span icons, and implement default agent span filters to reduce infrastructure noise. Trajectory diagrams eliminate repeated nodes and align layout with industry standards. See [documentation](observability-view.md "observability-view.md").

### Gateway and Policy: Full Availability Zone Coverage

Gateway and Policy services are now available across all availability zones within launched regions.

### AgentCore Registry is now in Public Preview

AWS Agent Registry for centralized agent discovery and governance launched in Preview. Customers can create a private, governed catalog and discovery layer for agents, tools, skills, MCP servers, and custom resources. Accessible via Console UI, APIs, or as an MCP server queryable from IDEs. Supports IAM and OAuth (Custom JWT) based access. See [blog](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/ "https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/") and [documentation](registry.md "registry.md").

### Observability: Cross-Account Monitoring

AgentCore launched cross-account observability. Customers can monitor logs, metrics, traces, and Evaluations results from a centralized monitoring account by linking multiple source accounts. Each monitoring account can link up to 100,000 log groups across source accounts, and each source account can share data with up to five monitoring accounts. See [documentation](observability-cross-account.md "observability-cross-account.md").

### AgentCore CLI: Resource Import and Bash Commands

CLI now supports importing existing AgentCore resources (evaluator and online evaluation config) from your account, executing bash commands within the agent’s Runtime or locally within its container, BYO Dockerfile for Runtime, and Memory streaming. See [documentation](agentcore-get-started-cli.md "agentcore-get-started-cli.md").

### Browser: OS-Level Interaction Capabilities

AgentCore Browser launched OS-level interaction capabilities, enabling automation of workflows requiring direct operating system control beyond Chrome DevTools Protocol — including mouse operations, print dialogs, native system alerts, and keyboard shortcuts. See [documentation](browser-tool.md "browser-tool.md").

### Gateway: 3LO Support for MCP Targets is now GA

Three-legged OAuth (3LO) support for MCP servers reached general availability. Gateways with MCP targets can now obtain user-specific tokens for different end users, enabling access to user-specific data from external services that require explicit user consent. See [documentation](gateway-target-MCPservers.md "gateway-target-MCPservers.md").

### Observability: Unlimited X-Ray Policy Limits

X-Ray policy limits expanded from 1,200 AgentCore resources to unlimited through wildcard support in resource policies. Removes scaling constraints for enterprise deployments with large agent portfolios.

### Integrations: LangChain Deep Agents Partnership

AgentCore Code Interpreter is now the first AWS-native sandbox provider in LangChain’s Deep Agents framework. New PyPI package `langchain-agentcore-codeinterpreter` published under the LangChain org with documentation live on the LangChain site. Native CLI support via `--sandbox agentcore`.

### Integrations: AG-UI Partnership with CopilotKit

CopilotKit published a joint blog announcing AgentCore as the recommended deployment target for AG-UI agents. AgentCore is now listed as a first-party deployment platform in the [AG-UI GitHub repository](https://github.com/ag-ui-protocol/ag-ui "https://github.com/ag-ui-protocol/ag-ui").

## March 2026

### AgentCore Evaluations is now Generally Available

AgentCore Evaluations became generally available, providing automated quality assessment for AI agents. Teams can evaluate using 13 built-in evaluators for response quality, safety, task completion, and tool usage. Ground Truth support measures agent performance against reference answers, behavioral assertions, and expected tool execution sequences. Custom evaluators support LLM-based or code-based (Lambda) evaluation logic. See [documentation](evaluations.md "evaluations.md").

### Observability: One-Click Enablement for Memory and Gateway

One-click observability enablement launched for Memory and Gateway. Customers can now enable logging and tracing for these resource types individually as a one-time effort. This capability was already available for Runtime, Browser Tool, and Code Interpreter. See [documentation](observability-configure.md "observability-configure.md").

### Runtime: Additional IAM Condition Keys

Support deployed for `bedrock-agentcore:RuntimeAuthorizerType` (mandate specific authorization mechanisms) and `aws:VpceOrgID` (restrict invocations to organization-owned VPC endpoints). Essential for OAuth runtimes where principal-based keys are not applicable. See [documentation](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

### AgentCore CLI is now Generally Available

AgentCore CLI reached GA (v0.4.0), providing a comprehensive command-line tool for building and deploying AI agents in minutes. Streamlines the full lifecycle — scaffolding projects with multiple frameworks (Strands, LangChain, Google ADK, OpenAI Agents), local development with hot reload, adding capabilities like memory and credentials, and deploying to production with full infrastructure management. See [documentation](agentcore-get-started-cli.md "agentcore-get-started-cli.md").

### Browser and Code Interpreter: Chrome Policies and Custom Root CA Support

AgentCore launched Chrome Enterprise policies (100+ configurable policies for browser behavior) and custom root CA certificates for both Browser and Code Interpreter. Enables agents to connect to internal services using organization-signed SSL certificates. See [documentation](browser-tool.md "browser-tool.md").

### Runtime: Managed Session Storage in Public Preview

AgentCore Runtime now offers managed session storage, enabling agents to persist filesystem state across stop and resume cycles. Supports standard Linux filesystem operations with up to 1 GB per session and 14-day retention. See [documentation](runtime-persistent-filesystems.md "runtime-persistent-filesystems.md").

### Control Plane Private Link Support for Gateway and Evaluations

AWS PrivateLink support launched for control plane operations for Gateway and Evaluations. AgentCore now has PLE support for all control plane and data plane operations except Identity control plane. See [documentation](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

### Code Interpreter: Node.js Support

AgentCore Code Interpreter launched Node.js runtime support for JavaScript and TypeScript with pre-installed libraries available immediately. Removes a critical barrier for enterprise customers with substantial Node.js investments. See [documentation](code-interpreter-runtime-selection.md "code-interpreter-runtime-selection.md").

### Memory: Resource-Based Policies (RBP)

Resource-Based Policy support launched for Memory resources. Customers can attach policies directly to memory resources for granular access control without updating caller IAM roles for every new principal. See [documentation](resource-based-policies.md "resource-based-policies.md").

### Runtime: Execute Shell Commands (InvokeAgentRuntimeCommand)

AgentCore Runtime introduced a new API enabling customers to execute shell commands directly within running microVM sessions with real-time HTTP/2 streaming output. Allows organizations to delegate deterministic operations — testing, version control, builds, deployments — to direct execution while preserving agent resources for reasoning. See [documentation](runtime-execute-command.md "runtime-execute-command.md").

### Runtime: OAuth Authentication for WebSocket Connections

AgentCore Runtime now supports OAuth authentication for browser-based WebSocket connections. Browser JavaScript clients can authenticate directly with AgentCore Runtime using an OAuth bearer token without requiring a proxy or server-side relay. See [documentation](runtime-get-started-websocket.md "runtime-get-started-websocket.md").

### Memory: Record Streaming

Developers can now receive push-based notifications whenever memory records are created, updated, or deleted — eliminating polling. Enables event-driven architectures that react to memory record lifecycle changes including triggering downstream workflows and tracking state changes across agents and sessions. See [documentation](memory-record-streaming.md "memory-record-streaming.md").

### Runtime: AG-UI Protocol Support

AgentCore Runtime launched native support for the AG-UI (Agent User Interface) protocol, enabling real-time streaming of text chunks, reasoning steps, tool calls, and results to frontends; state synchronization for UI elements; structured tool call visualization; and bidirectional WebSocket transport. See [documentation](runtime-agui-protocol-contract.md "runtime-agui-protocol-contract.md").

### Control Plane Private Link Support for Runtime, Memory, and Built-in Tools

AWS PrivateLink launched for control plane operations across Runtime, Memory, and Built-in Tools. Customers can now create, update, and delete these resources from within their VPC using the new endpoint `com.amazonaws.region.bedrock-agentcore-control`. See [documentation](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

### AgentCore Policy is now Generally Available

Developers can now use AgentCore Policy in production across thirteen AWS Regions worldwide. Policy gives organizations centralized, fine-grained control over agent-tool interactions by defining exactly what tools an agent can access and under what conditions. See [documentation](policy.md "policy.md").

### Stateful MCP Support in Runtime

MCP servers running in AgentCore Runtime can now maintain session context across interactions. When configured in stateful mode, servers unlock advanced capabilities including elicitation (collect user input mid-workflow), sampling (server-initiated LLM calls from within tool execution), and real-time progress notifications (stream updates during long-running tasks). See the [Stateful MCP Server guide](mcp-stateful-features.md "mcp-stateful-features.md").

### Python 3.14 Support in Runtime

AgentCore Runtime now supports [Python 3.14 for Direct Code Deploy](runtime-get-started-code-deploy-python.md "runtime-get-started-code-deploy-python.md"). Build and deploy agents using the latest Python release and take advantage of its performance improvements and new language features without custom containers.

### AgentCore CLI: Additional Features

AgentCore CLI integrates with AgentCore Gateway and introduces logs/traces commands. New and updated commands: `agentcore add` (incorporate Gateways and Gateway Targets into your project), `agentcore logs` (view logs for deployed agents), `agentcore traces` (view traces for deployed agents). Individual memory resources can now be deployed independently. See [documentation](agentcore-get-started-cli.md "agentcore-get-started-cli.md").

### Latency Improvements in Runtime

Sequential calls within a session are now 25-35% faster. AgentCore Runtime now caches authentication tokens for their full 30-minute validity window, eliminating redundant token fetches on every invocation. Platform overhead TM99 decreased 35% in PDX and 25% in IAD, with other regions seeing 12-18% improvements.

## February 2026

### Latency Improvements in Evaluations

Evaluation scores now arrive approximately 50% faster. AgentCore Evaluations moved to incremental state management in the evaluation pipeline, replacing a previous approach that rescanned logs every 5 minutes. P90 end-to-end processing time decreased 37-50% by region. Log query volume is down 70-90% and log query costs down 60-80%.

### AgentCore is now ISO and CSA STAR Certified

AgentCore achieved ISO and CSA STAR compliance standards. The service is now officially listed on the [AWS compliant services page](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

### AgentCore CLI: Public Preview Launch

[AgentCore CLI](https://github.com/aws/agentcore-cli "https://github.com/aws/agentcore-cli") launched in public preview. Developers can create, develop locally, and deploy AI agents using popular frameworks (Strands, LangChain, AutoGen, Google ADK, OpenAI Agents). Manages the full lifecycle from project creation to teardown, with support for memory and identity.

### Browser: Proxy Configuration, Browser Profiles, and Browser Extensions

AgentCore Browser now supports three new capabilities: proxy configuration for IP stability and corporate network integration; browser profiles for persisting cookies and local storage across sessions; and browser extensions for loading Chrome extensions (ad blocking, auth helpers, custom routing). See docs: [Proxies](browser-proxies.md "browser-proxies.md") | [Profiles](browser-profiles.md "browser-profiles.md") | [Extensions](browser-extensions.md "browser-extensions.md").

## January 2026

### Runtime, Tools, and Observability: Region Expansion

AgentCore Runtime and Tools (Browser, Code Interpreter) launched in 5 new regions — Europe (Stockholm, Paris, London), Asia Pacific (Seoul), and Canada (Central) — followed by Observability. This brings the full AgentCore capability set to these regions.

### Runtime: VPC Condition Keys Support

AgentCore launched IAM policy condition key support for VPC configurations across Runtime, Browser, and Code Interpreter. Two new condition keys — `bedrock-agentcore:Subnets` and `bedrock-agentcore:SecurityGroups` — enable enterprises to enforce organizational network policies, mandate VPC-connected deployments, and restrict to approved subnets and security groups. See [documentation](agentcore-vpc.md "agentcore-vpc.md").

## December 2025

### Policy in Amazon Bedrock AgentCore

Added documentation for the Policy in AgentCore feature, which enables policy-based governance and control for agent interactions. This feature provides policy evaluation, monitoring, and enforcement capabilities for agent workflows.

### Episodic memory strategy

Added documentation for using the episodic memory strategy in AgentCore Memory. See [Episodic memory strategy](episodic-memory-strategy.md "episodic-memory-strategy.md").

### Custom claims value support for AgentCore Gateway authentication

Added documentation for specifying custom claims values in AgentCore Gateway authentication. See [The authorization configuration](gateway-create-api.md "gateway-create-api.md").

### Bidirectional streaming

Added documentation for bidirectional streaming with AgentCore Runtime, which enables real-time, full-duplex communication between clients and agents using WebSocket protocol for interactive agent experiences. See [Bidirectional streaming with AgentCore Runtime](runtime-bidirectional-streaming.md "runtime-bidirectional-streaming.md").

### Authentication token support for AgentCore Gateway

Added documentation for setting up authentication tokens for AgentCore Gateway gateways. See [OAuth authorization](gateway-building-adding-targets-authorization.md "gateway-building-adding-targets-authorization.md").

### Amazon Bedrock AgentCore Evaluations

Added documentation for Amazon Bedrock AgentCore Evaluations, a comprehensive suite of capabilities for measuring and monitoring the performance, accuracy, and reliability of your agent or tools in both development and production environments. See [Evaluate agent performance with Amazon Bedrock AgentCore Evaluations](evaluation/evaluation.md "evaluation/evaluation.md").

### API gateways as gateway targets

Added documentation for adding an Amazon API Gateway gateway as a target. See [Amazon API Gateway REST API stages as targets](gateway-target-api-gateway.md "gateway-target-api-gateway.md").

## November 2025

### Direct code deployment

Added documentation for direct code deployment, which enables you to deploy Python agents to Amazon Bedrock AgentCore Runtime using ZIP file archives for faster development and simpler packaging. See [Get started with direct code deployment](runtime-get-started-code-deploy.md "runtime-get-started-code-deploy.md").

## October 2025

### General Availability

Amazon Bedrock AgentCore is now generally available across nine AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), and Asia Pacific (Tokyo). The platform enables building, deploying, and operating agents securely at scale using any framework and any foundation model.

### Web Bot Auth (Preview)

Added documentation for Browser Web Bot Auth feature, which enables AI agents to cryptographically sign HTTP requests to reduce CAPTCHA challenges when browsing websites.

### Runtime identity service-linked role

Added documentation for the new runtime identity service-linked role that manages workload identity access tokens and OAuth credentials. Updated BedrockAgentCoreFullAccess policy to include permission for creating the Amazon Bedrock AgentCore runtime identity service-linked role.

### Model Context Protocol (MCP) servers as Gateway targets

Added documentation for the Model Context Protocol (MCP) servers as Gateway targets and using synchronization operations.

### Model Context Protocol (MCP) server support

Added documentation for the Model Context Protocol (MCP) server that helps you transform, deploy, and test AgentCore-compatible agents directly from your development environment. The MCP server works with popular MCP clients including Kiro, Cursor, Claude Code, and Amazon Q CLI.

## September 2025

### Runtime and Memory: VPC Support

AgentCore Runtime and Memory now support deployment within customer VPCs, enabling secure connectivity to private resources such as databases, internal APIs, and services that are not publicly accessible. Agents running in VPC-connected runtimes can access resources in private subnets while maintaining the same managed infrastructure experience. See [documentation](agentcore-vpc.md "agentcore-vpc.md").

### Tagging and AWS CloudFormation Support

AgentCore resources now support tagging for cost allocation, access control, and organizational tracking. Additionally, AWS CloudFormation support enables infrastructure-as-code provisioning and management of AgentCore Runtime and Memory resources, allowing teams to define, version, and deploy agent infrastructure through standard CloudFormation templates. See [Tagging](tagging.md "tagging.md").

## July 2025

### Initial release (preview)

Initial release of the Amazon Bedrock AgentCore Developer Guide.
