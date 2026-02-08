# How to use orchestrator AI agents

Orchestrator AI Agents serve as primary agents for resolving customer interactions across use cases
like self-service and agent assistance. They integrate with tools and security profiles to enhance issue
resolution capabilities.

- **Tools**: You can configure your Orchestrator AI Agent with these tool types:
  - [MCP tools](ai-agent-mcp-tools.md "ai-agent-mcp-tools.md"): Extend agent capabilities through the Model Context Protocol.
  - Return to control: Ends the conversation and exits the GCI block in self-service flows
  - Constant: Returns a static string value. Useful for testing and rapid iteration during development

- **Security Profiles**: Security profiles control which tools an AI Agent can execute.
  Agents can only use tools they have explicit permission to access through their assigned security profile.

###### Note

Orchestration AI agents require chat streaming to be enabled for chat contacts.
Without chat streaming enabled, some messages will fail to render. See - [Enable message streaming for AI-powered chat](message-streaming-ai-chat.md "message-streaming-ai-chat.md").

## Message parsing

Orchestrator AI Agents only display messages to customers when the model's response is wrapped
in `<message>` tags. The prompt instructions must specify these formatting
instruction, otherwise customers will not see any messages from the AI Agent. In our system prompts,
we instruct the model to respect our formatting instructions as follows:

```

<formatting_requirements>
MUST format all responses with this structure:

<message>
Your response to the customer goes here. This text will be spoken aloud, so write naturally and conversationally.
</message>

<thinking>
Your reasoning process can go here if needed for complex decisions.
</thinking>

MUST NEVER put thinking content inside message tags.
MUST always start with `<message>` tags, even when using tools, to let the customer know you are working to resolve their issue.
</formatting_requirements>

<response_examples>
NOTE: The following examples are for formatting and structure only. The specific tools, domains, and capabilities shown are examples and may not reflect your actual available tools. Always check your actual available tools before making capability claims.

Example - Simple response without tools:
User: "Can you help me with my account?"
<message>
I'd be happy to help you. Let me see what I can do.
</message>

```

You can use multiple `<message>` tags in a single response to provide an initial message for immediate acknowledgment while the agent processes the request, then follow up with additional messages containing results or updates. This improves the customer experience by providing instant feedback and breaking information into logical chunks.
