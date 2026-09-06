

# Troubleshoot agentic self-service issues
<a name="ts-agentic-self-service"></a>

The following issues are specific to [agentic self-service](agentic-self-service.md).

## AI agent is not responding to customers
<a name="ts-ai-agent-not-responding"></a>

If your AI agent is processing requests but customers are not seeing any responses, the orchestration prompt might be missing the required message formatting instructions.

Orchestrator AI agents only display messages to customers when the model's response is wrapped in `<message>` tags. If your prompt does not instruct the model to use these tags, responses will not be rendered to the customer.

**Solution**: Ensure your orchestration prompt includes formatting instructions that require the model to wrap responses in `<message>` tags. For more information, see [Message parsing](use-orchestration-ai-agent.md#message-parsing).

## MCP tool invocation failures
<a name="ts-mcp-tool-failures"></a>

If your AI agent fails to invoke MCP tools during a conversation, check the following:
+ **Security profile permissions** – Verify that the AI agent's security profile grants access to the specific MCP tools it needs. The AI agent can only invoke tools it has explicit permission to access.
+ **Gateway connectivity** – Confirm that the Amazon Bedrock AgentCore Gateway is correctly configured and that the discovery URL is valid. Verify that the inbound authentication audiences are set to the gateway ID. Check the gateway status in the AgentCore console.
+ **API endpoint health** – Verify that the backend API or Lambda function behind the MCP tool is running and responding correctly. Check CloudWatch Logs for errors in the target service.

## IAM permissions for MCP tools
<a name="ts-mcp-iam-permissions"></a>

If MCP tool calls return access denied errors, verify that the IAM roles have the required permissions:
+ **Amazon Bedrock AgentCore Gateway role** – The gateway's execution role must have permission to invoke the backend APIs or Lambda functions that your MCP tools connect to.