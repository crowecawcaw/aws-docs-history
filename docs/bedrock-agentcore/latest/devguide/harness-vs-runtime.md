

# AgentCore harness vs. Runtime
<a name="harness-vs-runtime"></a>

AgentCore harness and AgentCore Runtime solve different parts of the same problem. This page explains the conceptual difference and provides a feature-by-feature comparison to help you choose between them.

## Conceptual difference
<a name="_conceptual_difference"></a>

 **AgentCore Runtime** is a *serverless hosting environment*. You bring agent code - written in any framework or no framework - wrap it with the AgentCore SDK’s `BedrockAgentCoreApp` entrypoint, package it into an ARM64 container, push it to Amazon ECR, and deploy. *The orchestration loop is yours.* To use any other AgentCore primitive (Memory, Gateway, Browser, Code Interpreter, outbound Identity), you call it from your code, typically through the AgentCore SDK. Runtime provides the infrastructure - isolation, scaling, sessions, auth gating, and observability plumbing - while the agent logic is code you write.

 **AgentCore harness** is a *managed agent harness* - the orchestration loop itself is provided, powered by [Strands Agents](https://strandsagents.com). You declare what the agent is (model, system prompt, tools, memory, limits) as configuration, and AgentCore runs the loop. Most features are a single config field: switching a model or adding a tool is a config change, not a redeploy. The harness is a managed abstraction that runs inside Runtime - CloudTrail records harness operations under `AWS::BedrockAgentCore::Runtime`.

For nearly every feature, the pattern is the same:
+  **Harness** - configuration, no code.
+  **Runtime** - you write code, usually with the AgentCore SDK plus your framework.

The grid below makes the per-feature exceptions explicit.

## Feature grid
<a name="_feature_grid"></a>

The **Supported?** columns use the following legend:
+ ✅ - Supported with no custom code required.
+ 🔵 - Supported, but you must maintain your own implementation.
+ 🟣 - Configuration enables it, but code is required to fully use it.
+ ❌ - Not supported.


| Feature / Capability | Harness: supported? | Harness: customer code required? | Runtime: supported? | Runtime: customer code required? | 
| --- | --- | --- | --- | --- | 
| Model selection (Bedrock / OpenAI / Gemini / LiteLLM) | ✅ | No | 🔵 | Yes | 
| Switch model provider mid-session | ✅ | No | 🔵 | Yes | 
| Built-in shell and `file_operations` tools | ✅ | No | 🔵 | Yes | 
| Agent Skills | ✅ | No | 🔵 | Yes | 
| Observability | ✅ | No | 🔵 | Yes | 
| AgentCore Memory - short-term | ✅ | No | 🔵 | Yes | 
| AgentCore Memory - long-term (semantic, summarization, user-pref, episodic) | ✅ | No | 🔵 | Yes | 
| Per-user memory scoping (actor ID) | ✅ | No | 🔵 | Yes | 
| AgentCore Gateway | ✅ | No | 🔵 | Yes | 
| AgentCore Browser | ✅ | No | 🔵 | Yes | 
| AgentCore Code Interpreter | ✅ | No | 🔵 | Yes | 
| MCP server tools (remote) | ✅ | No | 🔵 | Yes | 
| Inline / client-side tools | 🔵 | Yes | 🔵 | Yes | 
| Context-window truncation | ✅ | No | 🔵 | Yes | 
| Custom container image / environment | 🟣 | Mixed | 🟣 | Mixed | 
| Execution limits (`maxIterations`, `timeoutSeconds`, `maxTokens`, idle/lifetime) | ✅ | No | 🔵 | Yes | 
| Filesystem - service-managed session storage | ✅ | No | ✅ | No | 
| Filesystem - EFS access point | ✅ | No | ✅ | No | 
| Filesystem - S3 Files access point | ✅ | No | ✅ | No | 
| Environment variables | ✅ | No | ✅ | No | 
| Direct shell command execution (`InvokeAgentRuntimeCommand` API) | ✅ | No | ✅ | No | 
| Inbound auth - IAM (SigV4) | ✅ | No | ✅ | No | 
| Inbound auth - OAuth | ✅ | No | ✅ | No | 
| Outbound auth / Identity token vault (OAuth and API keys) | ✅ | No | 🔵 | Yes | 
| Session isolation | ✅ | No | ✅ | No | 
| VPC networking | ✅ | No | ✅ | No | 
| Streaming responses | ✅ | No | 🔵 | Yes | 
| Versioning and endpoints | ✅ | No | ✅ | No | 
| Choice of agent framework | ❌ | N/A | 🔵 | Yes | 
| Bidirectional streaming | ❌ | N/A | 🔵 | Yes | 
| Non-agent-loop patterns (graph, workflow style) | ❌ | N/A | 🔵 | Yes | 
| Hooks | ❌ | N/A | 🔵 | Yes | 

## Related topics
<a name="_related_topics"></a>
+  [Get started](harness-get-started.md) - create and invoke your first harness
+  [Models and instructions](harness-models.md) - configure agents, models, and providers
+  [Tools](harness-tools.md) - connect tools to your harness
+  [Environment and filesystem](harness-environment.md) - bring a custom container image or environment