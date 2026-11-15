

# Use Amazon Bedrock AgentCore
<a name="agent-access-agentcore"></a>

You can build and run agents with Amazon Bedrock AgentCore that operate desktop and mainframe applications through WorkSpaces Applications agent access. AgentCore provides a managed environment to create, test, and run your agent, and agent access gives each agent a secure Windows or Linux desktop with built-in monitoring, auditing, and governance. There are no extra components to build: an AgentCore agent connects to the managed MCP server the same way any other agent does.

You can start in the AgentCore Harness Playground and run your first agent without writing code. The playground runs the same managed loop as the production harness. After you test an agent, you can promote it, along with its model, system prompt, tools, skills, memory, and limits, to a versioned harness that runs behind an endpoint and supports policy controls. AgentCore Gateway and AgentCore Identity connect agents to your identity provider, while each agent's desktop stays inside your corporate network. After you deploy, you can use AgentCore evaluations and cost management features to improve accuracy and reduce cost.

## Connect an agent to a desktop from AgentCore
<a name="agent-access-agentcore-connect"></a>

To connect an agent to a WorkSpaces Applications desktop, add a remote MCP server tool to your agent in the Harness Playground, then configure it for agent access:

1. Set the stack and user ID headers so that the agent connects to your non-domain-joined stack. For more information about identifying a session, see [Session identification](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-session-id).

1. Set the outbound authorization to either IAM or OAuth. When you use IAM, the request is signed with SigV4 so that WorkSpaces Applications can verify it. For more information about the authorization options, see [Request authorization](agent-access-mcp-server-endpoint.md#agent-access-mcp-server-authorization).

The agent connects to the MCP server at the endpoint described in [Connecting to the MCP server](agent-access-mcp-server-endpoint.md). The other steps in the Harness Playground, such as adding tools and setting your prompts, are the same as for any other agent.