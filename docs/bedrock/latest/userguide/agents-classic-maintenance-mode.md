

# Amazon Bedrock Agents Classic maintenance mode
<a name="agents-classic-maintenance-mode"></a>

Amazon Bedrock Agents (launched November 2023) is now Amazon Bedrock Agents Classic and will no longer be open to new customers starting on July 30, 2026. For capabilities similar to Amazon Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Amazon Bedrock continues to be available, but the Agents Classic service will be in maintenance mode.

This guide provides information about the maintenance mode migration options for Amazon Bedrock Agents Classic customers.

**Note**  
Amazon Bedrock continues to be fully supported. Only the Amazon Bedrock Agents Classic service is no longer open to new customers as of July 30, 2026. Your existing Amazon Bedrock models, Knowledge Bases, and Guardrails are not affected.

## Migration plan
<a name="agents-maintenance-mode-migration"></a>

We recommend that you migrate your Amazon Bedrock Agents Classic workloads to Amazon Bedrock AgentCore. AgentCore is the platform to build, connect, and optimize AI agents. The managed harness in AgentCore provides a config-based starting point where developers can declare the agent's model, tools, and instructions. AgentCore handles the environment, compute, memory, identity, and observability.

### The managed agent harness in AgentCore (recommended)
<a name="agents-maintenance-mode-harness"></a>

The managed harness in AgentCore provides a config-based starting point where builders can declare the agent's model, tools, and instructions. AgentCore handles compute, environment, memory, identity, and observability. The harness supports:
+ Managed orchestration loop with built-in tool connectivity
+ Action groups exposed as MCP tools through AgentCore gateway (REST APIs, Lambda functions, or code-level @tools)
+ Gateway-fronted knowledge base integration
+ Inline function tools for return-of-control and human-in-the-loop patterns
+ Code interpreter for sandboxed code execution
+ Short-term and long-term memory with configurable strategies
+ Guardrail enforcement through AgentCore gateway
+ Persistent, end-to-end tracing of all agent actions
+ System prompt configuration for overall agent behavior

### Code-defined agents on AgentCore
<a name="agents-maintenance-mode-code-defined"></a>

For workloads that require capabilities beyond the harness's declarative model, customers can deploy code-defined agents directly on AgentCore. This path supports:
+ Prompt overrides at specific orchestration stages
+ Multi-agent collaboration and supervisor patterns
+ Custom orchestration logic
+ Broader OpenAI-compatible endpoints
+ Any framework (Strands, LangChain, OpenAI Agents SDK, Claude Agent SDK, or custom)

Code-defined agents still benefit from AgentCore's managed infrastructure while giving developers full control over the agent loop.

Use the harness unless you have a specific reason to own the loop yourself (for example, an existing agent codebase to migrate, or advanced orchestration the harness does not yet express). Customers can also use the AgentCore CLI to import existing Bedrock Agents Classic configurations as a starting point for either path.

## Comparing capabilities
<a name="agents-maintenance-mode-comparison"></a>


| Bedrock Agents Classic | AgentCore Equivalent | 
| --- | --- | 
| Managed orchestration loop | Supported out-of-the-box with AgentCore harness | 
| Action groups defined through OpenAPI / function schema \+ optional Lambda executor, called from the managed agent | Tools exposed through AgentCore gateway as MCP tools wrapping REST APIs and Lambda functions or code-level @tools. | 
| Association of Bedrock Knowledge Bases directly on the agent config for RAG | Gateway-fronted knowledge base integration in AgentCore. Knowledge base accessible through code-level retrieval tool. | 
| Trace UI and APIs that show pre-processing, orchestration, action group calls, KB queries, and observations end-to-end | AgentCore provides persistent, end-to-end tracing of all agent actions. | 
| Prompt override configuration at specific stages (pre-processing, orchestration, KB response generation, post-processing) | System prompt on harness (--system-prompt) covers the overall agent behavior. Stage-specific prompt overrides (pre-processing, KB response generation, post-processing) are not directly replicated. Achieving equivalent behavior requires combining the system prompt with command execution and self-managed scripts. | 
| Built-in AMAZON.UserInput tool for automatic user reprompting and parameter elicitation during orchestration | Inline function tools in harness. The agent calls the tool, harness pauses and returns tool\_use to client code, which handles user interaction and sends the result back. Equivalent to return-of-control. Requires explicit tool definition rather than automatic elicitation. | 
| Built-in AMAZON.CodeInterpreter action group for sandboxed code execution | AgentCore code interpreter | 
| Session and memory configuration on the agent (idle TTL, memory types, cross-session memory) | AgentCore memory for short and long term (with different memory strategies) | 
| Guardrails and agent policy attached declaratively to the agent and enforced during orchestration | Guardrail configuration in Bedrock, with policy enforcement on AgentCore gateway | 
| Multi-agent collaboration roles and routing (for example, supervisor agents and orchestration roles) | Limited. The supervisor pattern is possible by exposing agents as MCP tools (agent-as-tool). Routing mode multi-agent is not straightforward today. Full multi-agent collaboration requires custom framework code. | 
| Custom orchestrator | Supported through AgentCore runtime (deploy custom orchestration code directly). Not available through harness. | 
| Return of control (agent pauses for external input) | Inline function tools in harness. Agent pauses, returns tool\_use to client. | 

## Migration procedure
<a name="agents-maintenance-mode-procedure"></a>

### Prerequisites to migrate to AgentCore harness
<a name="agents-maintenance-mode-prereqs"></a>
+ Node.js 20\+ and AgentCore CLI, or Python 3.10\+ with boto3
+ AWS credentials in a region where AgentCore harness is available. For more information, see [Supported AWS Regions for AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html).
+ IAM execution role with required permissions
+ (Optional) The [agent toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website provides specialized skills to guide your AI agents through the migration.

### Migrate with the agent toolkit for AWS (recommended)
<a name="agents-maintenance-mode-skill"></a>

The [agent toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website includes an `amazon-bedrock` skill that guides your AI agent (or coding assistant) through the migration end-to-end. It inspects your existing Bedrock Agent, checks migration eligibility, and maps each component to its AgentCore harness equivalent. The skill then drives the AgentCore CLI to scaffold and deploy the harness. It never modifies your source agent.

To use the skill:

1. Install the agent toolkit for AWS. For instructions on installing the agent toolkit and enabling the skill, see the [agent toolkit for AWS README](https://github.com/aws/agent-toolkit-for-aws/blob/main/README.md) on the GitHub website.

1. Enable the `amazon-bedrock` skill for your agent.

1. (Optional) For streamlined AWS access, configure the AWS MCP server. The skill also works with the AWS CLI and boto3.

1. Install the latest version of the AgentCore CLI. The skill uses the AgentCore CLI to scaffold and deploy the harness.

1. Prompt your agent with *"Help me migrate my Bedrock Agent to AgentCore harness"*. Provide the agent ID, name, or ARN, along with the AWS region and profile when the skill asks.

1. Confirm the account, region, and source agent at each checkpoint. The skill presents a component inventory, an eligibility assessment, and a written migration plan. It pauses for your approval before deploying.

You can also use the skill to answer migration questions without performing a migration. If your agent uses a feature with no validated harness path, the skill stops and suggests alternatives.

### Migrate manually
<a name="agents-maintenance-mode-manual"></a>

If you prefer to migrate without the skill, or your agent is not eligible for the skill-driven path, follow these steps to build the harness with the AgentCore CLI. Use the latest version of the AgentCore CLI.

#### Step 1: Create and configure
<a name="agents-maintenance-mode-step1"></a>

```
agentcore create --name my-research-agent
```

If you have an existing Bedrock Agent you want to replicate, review its configuration (model, action groups, KBs, prompt overrides) and map each to the corresponding harness parameter:
+ `model` — `--model-id`
+ `action groups` — Gateway tools
+ `KBs` — Gateway or retrieval tool
+ `prompt` — `--system-prompt`

Add tools:

```
agentcore add tool --harness my-research-agent \
  --type agentcore_browser --name browser
agentcore add tool --harness my-research-agent \
  --type agentcore_code_interpreter --name code-interpreter
```

To connect existing action groups through gateway:

```
agentcore add tool --harness my-research-agent \
  --type agentcore_gateway --name my-gateway \
  --gateway-arn arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/my-gw
```

#### Step 2: Configure model and system prompt
<a name="agents-maintenance-mode-step2"></a>

```
agentcore add harness \
  --name my-research-agent \
  --model-id us.anthropic.claude-sonnet-4-6-20250514-v1:0 \
  --system-prompt "You are a research assistant." \
  --tools agentcore-browser,code-interpreter
```

#### Step 3: Deploy and invoke
<a name="agents-maintenance-mode-step3"></a>

```
agentcore deploy
agentcore invoke --harness my-research-agent \
  --session-id "$(uuidgen)" \
  "Research tropical vacation options under $3k"
```

Override model on any invocation without redeploying:

```
agentcore invoke --harness my-research-agent \
  --model-id us.anthropic.claude-opus-4-5-20251101-v1:0 \
  "Summarize this research paper"
```

##### Memory
<a name="agents-maintenance-mode-memory"></a>

Enabled by default. To scope memory to individual users, pass `--actor-id`:

```
agentcore invoke --harness my-research-agent \
  --session-id "$(uuidgen)" --actor-id alice \
  "What did we discuss about the Portugal trip?"
```

Each actor gets isolated memory. Long-term strategies scope extracted knowledge by actor ID.

## Frequently asked questions
<a name="agents-classic-maintenance-mode-faq"></a>

### Impact
<a name="agents-classic-faq-impact"></a>

Will my existing agents stop working?  
No. Existing agents continue to function normally. All APIs (UpdateAgent, GetAgent, ListAgents, DeleteAgent, PrepareAgent, InvokeAgent, action group APIs, knowledge base APIs, alias APIs, etc.) remain available to all customers. Only CreateAgent and InvokeInlineAgent are restricted for accounts without prior usage.

How do I know if my account is affected?  
If your account has had Bedrock Agents activity in the past 12 months, you are allowlisted and unaffected. This applies per-account. If you have multiple AWS accounts, only those with prior Bedrock Agents usage are allowlisted. Accounts without prior usage will receive an AccessDeniedException (HTTP 403) when calling CreateAgent or InvokeInlineAgent.

What error will I see if my account is not allowlisted?  
Error Code: AccessDeniedException (HTTP 403)  
Message: "Bedrock Agents is in Maintenance Mode. New agent creation is not available for accounts without prior service usage. To learn more, see [Amazon Bedrock Agents Classic maintenance mode](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html)."

Do I need to take action?  
Not immediately. Your existing workloads are unaffected. However, we recommend evaluating AgentCore for new agent development and future migrations, as no new features will be added to Bedrock Agents Classic.

Can I request an exception to Bedrock Agents in a new account after July 30?  
No. There is no exception process. AWS automatically determines the allowlist based on whether your account has had Bedrock Agents activity in the past 12 months. If you need agent capabilities in a new account, use [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), which offers equivalent and expanded functionality.

What about the name change to "Bedrock Agents Classic"?  
This is a naming update only. No action is required on your part. Existing API namespaces (bedrock-agent), SDK clients, CloudFormation resource types, and IAM action prefixes remain unchanged.

Will my CloudFormation, CDK, or Terraform templates still work?  
Yes. Existing IaC templates that create or manage Bedrock Agents will continue to work for allowlisted accounts. If you are provisioning new environments in accounts without prior Bedrock Agents usage, use [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) resources in your templates instead.

Will new model versions be available in Bedrock Agents Classic?  
No. The model catalog available in Bedrock Agents Classic is frozen as of the maintenance mode effective date (July 30, 2026). New models released after that date will be available through AgentCore. Amazon Bedrock itself (model inference, Knowledge Bases, Guardrails) continues to receive new models. This restriction applies only to the Bedrock Agents Classic orchestration layer.

Will pricing change for Bedrock Agents Classic?  
There is no charge for Bedrock Agents Classic itself. You continue to pay only for the underlying model inference and any associated resources (Knowledge Bases, Lambda invocations, etc.) as before.

### Migration
<a name="agents-classic-faq-migration"></a>

What is the recommended migration path?  
AgentCore is the recommended platform. Two paths are available:  
+ **AgentCore harness** — A config-based experience similar to Bedrock Agents Classic. Declare your model, tools, and instructions; AgentCore handles compute, memory, identity, and observability. This is the closest analog to the Bedrock Agents managed experience.
+ **Code-defined agents on AgentCore** — For workloads requiring advanced orchestration, multi-agent collaboration, or custom logic. Deploy any framework (Strands, LangChain, OpenAI Agents SDK, Claude Agent SDK, or custom) on AgentCore's managed infrastructure.

Is there an automated migration tool?  
Yes. An agent skill to guide you through migrating Bedrock Agents Classic directly to AgentCore harness is available in the [agent toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website. The skill is also available through the AWS MCP server. For instructions on installing and using the skill, see the agent toolkit for AWS README on the GitHub website. Start with the prompt *"Help me migrate my Bedrock Agent to AgentCore harness."*

How long does migration take?  
For straightforward agents (model \+ action groups \+ knowledge base), CLI import or harness setup takes hours. Primary effort involves reviewing generated code or redeploying action groups behind AgentCore gateway. Complex agents with custom orchestrators or multi-agent collaboration will require more significant code work.

Is there a deadline to migrate?  
There is no migration deadline. Bedrock Agents Classic remains available to existing customers in maintenance mode with no planned end-of-life date. However, since no new features are planned, we recommend migrating to AgentCore to benefit from ongoing innovation.

What about my Bedrock Knowledge Bases?  
Knowledge Bases continue to work and are not affected by maintenance mode. When migrating to AgentCore, connect them through AgentCore gateway. The underlying Knowledge Base resource is unchanged.

What about my Bedrock Guardrails?  
Guardrails configured on the Bedrock model still apply when the model is invoked through AgentCore. Agent-level guardrail enforcement is available through AgentCore gateway policies.

Can I still use the same models?  
Yes. AgentCore supports the full Bedrock model catalog plus additional providers (OpenAI, Gemini, and any OpenAI-compatible endpoint). You can switch between model providers mid-session without redeploying.

What about multi-agent collaboration?  
You can build multi-agent patterns on AgentCore runtime using any supported framework. The managed harness supports an agent-as-tool pattern for simpler multi-agent use cases.

What about inline agents?  
Accounts with InvokeInlineAgent usage in the past 12 months can continue using inline agents. For new development, the AgentCore managed harness provides equivalent ephemeral agent capabilities with additional features (memory, stateful sessions, tool connectivity through gateway). Migration guidance for inline agents is forthcoming.

In which regions is AgentCore available?  
AgentCore is available in [these regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html). If your Bedrock Agents Classic workloads run in a region where AgentCore is not yet available, you can continue using Bedrock Agents Classic in those regions while migrating new development to AgentCore in a supported region.

### Pricing and support
<a name="agents-classic-faq-pricing"></a>

How much does AgentCore cost?  
AgentCore uses consumption-based pricing across its capabilities (runtime, memory, gateway). There is no separate harness orchestration charge. AgentCore's harness is more token-efficient than Bedrock Agents Classic's internal prompts, so customers may see comparable or lower model inference costs. See [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) for details.

## Additional resources
<a name="agents-maintenance-mode-resources"></a>
+ [AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html)
+ [AgentCore managed harness documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html)
+ [AWS Support](https://aws.amazon.com/support)
+ Contact your AWS account team for migration planning assistance