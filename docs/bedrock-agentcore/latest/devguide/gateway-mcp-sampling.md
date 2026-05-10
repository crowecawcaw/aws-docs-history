# Use sampling with your AgentCore gateway

Sampling is an MCP feature that allows an MCP server to request an LLM completion from the client during a tool call. This enables servers to leverage AI capabilities without needing direct access to a language model — the client handles the model invocation and returns the result. AgentCore Gateway forwards sampling requests from MCP server targets to your clients, replacing the request `id` with a gateway-generated identifier.

## Prerequisites

To use sampling with your gateway:

- **Sessions enabled** — Sampling requires session support. See [Use MCP sessions with your gateway](gateway-sessions.md "gateway-sessions.md").
- **Response streaming enabled** — Sampling requests are sent as SSE chunks during an open connection. Set `streamingConfiguration.enableResponseStreaming` to `true` in your gateway’s `protocolConfiguration.mcp`.
- **MCP server target type** — Sampling requests originate from MCP server targets.
- **Client declares sampling capability** — The client must declare support for sampling during the `initialize` request. The gateway only forwards sampling requests to clients that declared this capability.

## How sampling works

When an MCP server target needs an LLM completion during tool execution, it sends a `sampling/createMessage` request. The gateway forwards this request to the client as an SSE event, replacing the request `id`. The client invokes its language model and sends the result back to the gateway, which forwards it to the target.

The sampling request includes:

- `messages` — The conversation messages to send to the model.
- `modelPreferences` — Optional hints about desired model capabilities (intelligence, speed, cost).
- `systemPrompt` — Optional system prompt for the model.
- `maxTokens` — Maximum number of tokens to generate.

The client responds with:

- `model` — The model that was used.
- `role` — Always `assistant`.
- `content` — The generated content (text or image).

###### Note

The client has full control over which model to use and how to handle the request. The server’s `modelPreferences` are hints, not requirements. The client may also modify or reject the request based on its own policies.

## Sampling flow

1. Client sends a `tools/call` request with the `Mcp-Session-Id` header.
2. Gateway forwards the tool call to the MCP server target.
3. The target opens an SSE stream and sends a `sampling/createMessage` request.
4. Gateway forwards the sampling request to the client as an SSE event, replacing the request `id`.
5. The client invokes its language model with the provided messages.
6. The client sends a new request with the sampling result using the same `Mcp-Session-Id` and the `id` from the gateway’s request.
7. Gateway forwards the result to the MCP server target.
8. The target continues processing and returns the final tool result.
9. Gateway forwards the final result to the client and closes the stream.

## Guidance for MCP server target developers

###### Important

MCP server targets that send sampling requests **should** wrap sampling calls in try-catch blocks and handle the case where the client does not support sampling. If the gateway’s client did not declare sampling capability, the gateway does not declare it to the target. If the target sends a sampling request anyway, the gateway returns a `-32601` (Method not found) error to the target.

Servers should implement a fallback path (such as using a built-in model or skipping the AI-assisted step) when sampling is not available.

## Error handling

| Scenario                                                                         | Error                                | Description                                                                                                                              |
| -------------------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Client sends a sampling response when no sampling request is pending             | JSON-RPC `-32600` (Invalid Request)  | No matching sampling request found for this session.                                                                                     |
| Client sends sampling response with an `id` that doesn’t match a pending request | JSON-RPC `-32600` (Invalid Request)  | The `id` must match the one sent by the gateway in the `sampling/createMessage` request.                                                 |
| MCP server sends sampling request but gateway did not declare support            | JSON-RPC `-32601` (Method not found) | Returned to the MCP server target. See [Troubleshooting](#gateway-mcp-sampling-troubleshooting "#gateway-mcp-sampling-troubleshooting"). |

## Troubleshooting

**Error: "Error calling tool 'sample_tool': Method not found: sampling/createMessage"**

This error occurs when an MCP server target sends a sampling request but the gateway’s client did not declare sampling capability during `initialize`. The gateway returns a `-32601` (Method not found) error to the target, and the target may return this as a tool execution error to the client.

To resolve:

- **If you are the MCP server developer**: Add error handling around your sampling calls. Implement a fallback path when sampling is not supported:

###### Important

You **must** include `related_request_id=ctx.request_context.request_id` in your `create_message` call. This is required for the gateway to correctly associate the sampling request with the originating tool call. Without it, sampling will not work.

```
try:
    result = await ctx.session.create_message(
        messages=[{"role": "user", "content": {"type": "text", "text": "Summarize this document"}}],
        max_tokens=500,
        related_request_id=ctx.request_context.request_id,
    )
except Exception as e:
    # Fallback when client doesn't support sampling
    logger.warning(f"Sampling not supported: {e}")
    result = fallback_summarization(document)
```

- **If you are the gateway client developer**: Ensure your client declares sampling capability during `initialize`:

```
{
  "capabilities": {
    "sampling": {}
  }
}
```

## Code samples

###### Note

The LangGraph MCP Client (`langchain-mcp-adapters`) and Strands MCP Client do not currently support sampling. Use the MCP Client approach shown below to handle sampling requests from your gateway.

###### Example

Python requests package

1. ```
   import requests
   import json
   import sseclient
   ```

gateway_url = "https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
headers = {
"Content-Type": "application/json",
"Accept": "text/event-stream",
"Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

# Step 1: Initialize with sampling capability

init_response = requests.post(gateway_url, headers=headers, json={
"jsonrpc": "2.0",
"id": "init-request",
"method": "initialize",
"params": {
"protocolVersion": "2025-06-18",
"capabilities": {"sampling": {}},
"clientInfo": {"name": "my-agent", "version": "1.0.0"}
}
})
session_id = init_response.headers["Mcp-Session-Id"]
headers["Mcp-Session-Id"] = session_id

# Step 2: Call tool (streaming response)

response = requests.post(gateway_url, headers=headers, json={
"jsonrpc": "2.0",
"id": "tool-call-1",
"method": "tools/call",
"params": {
"name": "summarizeDocument",
"arguments": {"documentId": "doc-789"}
}
}, stream=True)

# Step 3: Process SSE events

client = sseclient.SSEClient(response)
for event in client.events():
data = json.loads(event.data)
if data.get("method") == "sampling/createMessage":
sampling_id = data["id"]
print(f"Sampling request: {data['params']['messages']}")

        # Step 4: Invoke your LLM and send result
        llm_result = invoke_your_model(data["params"])  # Your LLM invocation
        requests.post(gateway_url, headers=headers, json={
            "jsonrpc": "2.0",
            "id": sampling_id,
            "result": {
                "model": "claude-sonnet-4-20250514",
                "role": "assistant",
                "content": {"type": "text", "text": llm_result}
            }
        })
    elif "result" in data:
        print(f"Tool result: {data['result']}")
        break

````


MCP Client

1. ```
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

async def sampling_handler(request):
    """Handle sampling requests from the server by invoking an LLM."""
    messages = request.params.messages
    llm_response = await invoke_your_model(messages, max_tokens=request.params.maxTokens)
    return {
        "model": "claude-sonnet-4-20250514",
        "role": "assistant",
        "content": {"type": "text", "text": llm_response}
    }

async def use_sampling(url, token):
    headers = {"Authorization": f"Bearer {token}"}

    async with streamablehttp_client(url=url, headers=headers) as (
        read_stream, write_stream, _
    ):
        async with ClientSession(
            read_stream, write_stream,
            sampling_handler=sampling_handler
        ) as session:
            await session.initialize()
            result = await session.call_tool(
                name="summarizeDocument",
                arguments={"documentId": "doc-789"}
            )
            print(f"Tool result: {result}")
            return result

asyncio.run(use_sampling(
    url="https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp",
    token="YOUR_ACCESS_TOKEN"
))
````
