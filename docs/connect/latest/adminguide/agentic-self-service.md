

# Use agentic self-service
<a name="agentic-self-service"></a>

**Tip**  
Check out this course from AWS Workshop: [Building advanced, generative AI with AI agents](https://catalog.us-east-1.prod.workshops.aws/workshops/f77f49a2-1eae-4223-a9da-7044d6da51f8/en-US/01-introduction).

Agentic self-service enables AI agents to autonomously resolve customer issues across voice and chat channels. Unlike [legacy self-service](generative-ai-powered-self-service.md), where the AI agent returns control to the contact flow when a custom tool is selected, agentic self-service uses orchestrator AI agents that can reason across multiple steps, invoke MCP tools to take actions on behalf of customers, and maintain a continuous conversation until the issue is resolved or escalation is needed.

For example, when a customer calls about a hotel reservation, an orchestrator AI agent can greet them by name, ask clarifying questions, look up their booking, and process a modification—all within a single conversation, without returning control to the contact flow between each step.

**Topics**
+ [Key capabilities](#agentic-self-service-key-capabilities)
+ [Tools for orchestrator AI agents](#agentic-self-service-default-tools)
+ [Set up agentic self-service](#agentic-self-service-setup)
+ [Custom Return to Control tools](#agentic-self-service-custom-escalate)
+ [Handle Return to Control tools in your flow](#agentic-self-service-escalation-flow)
+ [Constant tools](#agentic-self-service-constant-tools)
+ [Set up agentic self service chat end to end](setup-agentic-selfservice-end-to-end.md)

## Key capabilities
<a name="agentic-self-service-key-capabilities"></a>

Agentic self-service provides the following capabilities:
+ **Autonomous multi-step reasoning** – The AI agent can chain multiple tool calls and reasoning steps within a single conversation turn to resolve complex requests.
+ **MCP tool integration** – Connect to backend systems through Model Context Protocol (MCP) tools to take actions such as looking up order status, processing refunds, and updating records. For more information, see [AI agent MCP tools](ai-agent-mcp-tools.md).
+ **Security profiles** – AI agents use the same security profile framework as human agents, controlling which tools the AI agent can access. For more information, see [Assign security profile permissions to AI agents](ai-agent-security-profile-permissions.md).

## Tools for orchestrator AI agents
<a name="agentic-self-service-default-tools"></a>

You can configure your orchestrator AI agent for self-service with the following tool types:
+ **[MCP tools](ai-agent-mcp-tools.md)** – Extend AI agent capabilities through the Model Context Protocol. MCP tools connect to backend systems to take actions such as looking up order status, processing refunds, and updating records. The AI agent invokes MCP tools during the conversation without returning control to the contact flow.
+ **Return to Control** – Signal the AI agent to stop and return control to the contact flow. By default, the `SelfServiceOrchestrator` AI agent includes `Complete` (to end the interaction) and `Escalate` (to transfer to a human agent). You can remove these defaults or create your own. For more information, see [Custom Return to Control tools](#agentic-self-service-custom-escalate).
+ **Constant** – Return a configured static string value to the AI agent. Useful for testing and rapid iteration during development. For more information, see [Constant tools](#agentic-self-service-constant-tools).

## Set up agentic self-service
<a name="agentic-self-service-setup"></a>

Follow these high-level steps to set up agentic self-service:

1. Create an orchestrator AI agent. In the Connect Customer admin website, go to **AI agent designer**, choose **AI agents**, and choose **Create AI agent**. Select **Orchestration** as the AI agent type. For **Copy from existing**, select **SelfServiceOrchestrator** to use the system AI agent for self-service as your starting configuration.

1. Create a security profile for your AI agent. Go to **Users**, choose **Security profiles**, and create a profile that grants access to the tools your AI agent needs. Then, in your AI agent configuration, scroll to the **Security Profiles** section and select the profile from the **Select Security Profiles** dropdown. For more information, see [Assign security profile permissions to AI agents](ai-agent-security-profile-permissions.md).

1. Configure your AI agent with tools. Add MCP tools from your connected namespaces and configure the default Return to Control tools (`Complete` and `Escalate`). For more information about MCP tools, see [AI agent MCP tools](ai-agent-mcp-tools.md).

1. Create and attach an orchestration prompt. The `SelfServiceOrchestrator` includes a default `SelfServiceOrchestration` prompt that you can use as-is or create a new one to define your AI agent's personality, behavior, and instructions for using tools. For more information about prompts, see [Customize AI agents](customize-connect-ai-agents.md).
**Important**  
Orchestrator AI agents require responses to be wrapped in `<message>` tags. Without this formatting, customers will not see messages from the AI agent. For more information, see [Message parsing](use-orchestration-ai-agent.md#message-parsing).

1. Set your AI agent as the default self-service agent. On the **AI Agents** page, scroll to **Default AI Agent Configurations** and select your agent in the **Self Service** row.

1. Create a Conversational AI bot. Go to **Routing**, **Flows**, **Conversational AI**, and create a bot with the Connect Customer AI agent intent enabled. For more information, see [Create an agent assist intent](create-qic-intent-connect.md).

1. Build a contact flow that routes contacts to your AI agent. Add a [Get customer input](get-customer-input.md) block that invokes your Conversational AI bot, and a [Check contact attributes](check-contact-attributes.md) block to route based on the Return to Control tool selected by the AI agent. For more information, see [Create a flow and add your conversational AI bot](create-bot-flow.md).

   The following image shows an example contact flow for agentic self-service.  
![Example agentic self-service contact flow with Set logging behavior, Set voice, Get customer input with a Lex bot.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agentic-self-service-contact-flow.png)

**Tip**  
If you want to enable chat streaming for agentic self-service, see [Enable message streaming for AI-powered chat](message-streaming-ai-chat.md). For a complete end-to-end chat walkthrough with streaming, see [Set up agentic self service chat end to end](setup-agentic-selfservice-end-to-end.md).

## Create custom Return to Control tools
<a name="agentic-self-service-custom-escalate"></a>

Return to Control tools signal the AI agent to stop processing and return control to the contact flow. When a Return to Control tool is invoked, the tool name and its input parameters are stored as Amazon Lex session attributes, which your contact flow can read using a [Check contact attributes](check-contact-attributes.md) block to determine the next action.

While the `SelfServiceOrchestrator` AI agent includes default `Complete` and `Escalate` Return to Control tools, you can create custom Return to Control tools with input schemas that capture additional context for your contact flow to act on.

To create a custom Return to Control tool:

1. In your AI agent configuration, choose **Add tool**, then choose **Create new AI Tool**.

1. Enter a tool name and select **Return to Control** as the tool type.

1. Define an input schema that specifies the context the AI agent should capture when invoking the tool.

1. (Optional) In the **Instructions** field, describe when the AI agent should use this tool.

1. (Optional) Add examples to guide the AI agent's behavior when invoking the tool.

1. Choose **Create**, then choose **Publish** to save your AI agent.

### Example: Custom Escalate tool with context
<a name="agentic-self-service-custom-escalate-schema"></a>

The following example shows how to replace the default Escalate tool with a custom version that captures escalation reason, summary, customer intent, and sentiment. This additional context gives human agents a head start when they pick up the conversation.

First, remove the default Escalate tool from your AI agent. Then create a new Return to Control tool named **Escalate** with the following input schema:

```
{
    "type": "object",
    "properties": {
        "customerIntent": {
            "type": "string",
            "description": "A brief phrase describing what the customer wants to accomplish"
        },
        "sentiment": {
            "type": "string",
            "description": "Customer's emotional state during the conversation",
            "enum": ["positive", "neutral", "frustrated"]
        },
        "escalationSummary": {
            "type": "string",
            "description": "Summary for the human agent including what the customer asked for, what was attempted, and why escalation is needed",
            "maxLength": 500
        },
        "escalationReason": {
            "type": "string",
            "description": "Category for the escalation reason",
            "enum": [
                "complex_request",
                "technical_issue",
                "customer_frustration",
                "policy_exception",
                "out_of_scope",
                "other"
            ]
        }
    },
    "required": [
        "escalationReason",
        "escalationSummary",
        "customerIntent",
        "sentiment"
    ]
}
```

In the **Instructions** field, describe when the AI agent should escalate. For example:

```
Escalate to a human agent when:
1. The customer's request requires specialized expertise
2. Multiple tools fail or return errors repeatedly
3. The customer expresses frustration or explicitly requests a human
4. The request involves complex coordination across multiple services
5. You cannot provide adequate assistance with available tools
```

(Optional) Add examples to guide the AI agent's tone during escalation. For example:

```
<message>
I understand this requires some specialized attention. Let me connect you
with a team member who can help coordinate all the details. I'll share
everything we've discussed so they can pick up right where we left off.
</message>
```

## Handle Return to Control tools in your contact flow
<a name="agentic-self-service-escalation-flow"></a>

When the AI agent invokes a Return to Control tool, control returns to your contact flow. You need to configure your flow to detect which tool was invoked and route the contact accordingly.

### How Return to Control detection works
<a name="agentic-self-service-escalation-detection"></a>

When the AI agent invokes a Return to Control tool:

1. The AI conversation ends.

1. Control returns to the contact flow.

1. The tool name and input parameters are stored as Amazon Lex session attributes.

1. Your flow checks these attributes and routes accordingly.

### Configure routing based on Return to Control tools
<a name="agentic-self-service-escalation-flow-steps"></a>

Follow these steps to add Return to Control routing to your contact flow:

1. Add a [Check contact attributes](check-contact-attributes.md) block after the **Default** output of your **Get customer input** block.

1. Configure the block to check the tool name:
   + **Namespace**: **Lex**
   + **Key**: **Session attributes**
   + **Session Attribute Key**: **Tool**

   Add conditions for each Return to Control tool you want to handle. For example, add conditions where the value equals **Complete**, **Escalate**, or the name of any custom Return to Control tool you created.

1. (Optional) Add a [Set contact attributes](set-contact-attributes.md) block to copy the tool's input parameters from Amazon Lex session attributes to contact attributes. This makes the context available for downstream routing and agent screen pops.

1. Connect each condition to the appropriate routing logic. For example:
   + **Complete** – Route to a **Disconnect** block to end the interaction.
   + **Escalate** – Route to a **Set working queue** and **Transfer to queue** block to transfer the contact to a human agent.
   + **Custom tools** – Route to any additional flow logic specific to your use case.

1. Connect the **No match** output from the [Check contact attributes](check-contact-attributes.md) block to a **Disconnect** block or additional routing logic.

#### Example: Routing an Escalate tool with context
<a name="agentic-self-service-escalation-example"></a>

If you created a custom Escalate tool with context (see [Example: Custom Escalate tool with context](#agentic-self-service-custom-escalate-schema)), you can copy the escalation context to contact attributes using a [Set contact attributes](set-contact-attributes.md) block. Set the following attributes dynamically:


| Destination key (User defined) | Source namespace | Source session attribute key | 
| --- | --- | --- | 
| escalationReason | Lex – Session attributes | escalationReason | 
| escalationSummary | Lex – Session attributes | escalationSummary | 
| customerIntent | Lex – Session attributes | customerIntent | 
| sentiment | Lex – Session attributes | sentiment | 

(Optional) Add a **Set event flow** block to display the escalation context to the human agent when they accept the contact. Set the event to **Default flow for agent UI** and select a flow that presents the escalation summary, reason, and sentiment to the agent.

## Use Constant tools for testing and development
<a name="agentic-self-service-constant-tools"></a>

Constant tools return a configured static string value to the AI agent when invoked. Unlike Return to Control tools, Constant tools do not end the AI conversation—the AI agent receives the string and continues the conversation. This makes Constant tools useful for testing and rapid iteration during development, allowing you to simulate tool responses without connecting to backend systems.

To create a Constant tool:

1. In your AI agent configuration, choose **Add tool**, then choose **Create new AI Tool**.

1. Enter a tool name and select **Constant** as the tool type.

1. In the **Constant value** field, enter the static string that the tool should return to the AI agent.

1. Choose **Create**, then choose **Publish** to save your AI agent.

For example, you can create a Constant tool named **getOrderStatus** that returns a sample JSON response. With this Constant tool, you can test how your AI agent handles order status requests before connecting to your actual order management system through an MCP tool.