# Receive logging messages from your AgentCore gateway

MCP server targets can send log messages to clients during tool execution using the `notifications/message` method. These messages provide real-time visibility into what the server is doing, useful for debugging, auditing, and monitoring tool behavior. AgentCore Gateway forwards these log notifications from MCP server targets to your client as Server-Sent Events (SSE) chunks.

## Prerequisites

To receive logging messages from your gateway:

- **Response streaming enabled** — Log messages are delivered as SSE chunks during an open connection. Set `streamingConfiguration.enableResponseStreaming` to `true` in your gateway’s `protocolConfiguration.mcp`.
- **MCP server target type** — Log messages originate from MCP server targets.
- **Client sends `Accept: text/event-stream` header** — The client must request an SSE response to receive streaming events.

## Log levels

MCP defines the following log levels, in order of increasing severity:

| Level       | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `debug`     | Detailed diagnostic information for troubleshooting.         |
| `info`      | General informational messages about normal operation.       |
| `notice`    | Normal but significant events.                               |
| `warning`   | Potentially harmful situations that don’t prevent operation. |
| `error`     | Error conditions that prevented a specific operation.        |
| `critical`  | Critical conditions requiring immediate attention.           |
| `alert`     | Action must be taken immediately.                            |
| `emergency` | System is unusable.                                          |

## How logging messages work

When an MCP server target emits a `notifications/message` during tool execution, the gateway forwards it to the client as an SSE event. Each log message includes:

- `level` — The severity level of the message.
- `logger` — Optional name identifying the source component.
- `data` — The log content (string or structured object).

Log messages are informational and do not require a response from the client. They are delivered alongside other SSE events such as progress notifications and the final tool result.

## Code samples

###### Example

curl

1. Call a tool and receive log messages in the SSE stream:

```
curl -N -X POST \
  https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "id": "tool-call-1",
    "method": "tools/call",
    "params": {
      "name": "deployService",
      "arguments": {
        "serviceName": "my-api",
        "environment": "staging"
      }
    }
}'
```

The gateway returns an SSE stream with log messages followed by the final result:

```
event: message
data: {"jsonrpc":"2.0","method":"notifications/message","params":{"level":"info","logger":"deploy-service","data":"Starting deployment of my-api to staging"}}

event: message
data: {"jsonrpc":"2.0","method":"notifications/message","params":{"level":"info","logger":"deploy-service","data":"Building container image..."}}

event: message
data: {"jsonrpc":"2.0","method":"notifications/message","params":{"level":"warning","logger":"deploy-service","data":"Deprecated configuration detected in service manifest"}}

event: message
data: {"jsonrpc":"2.0","method":"notifications/message","params":{"level":"info","logger":"deploy-service","data":"Deployment complete"}}

event: message
data: {"jsonrpc":"2.0","id":"tool-call-1","result":{"content":[{"type":"text","text":"Successfully deployed my-api to staging environment."}]}}
```

Python requests package

1. ```

   ```

import requests
import json
import sseclient

gateway_url = "https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
headers = {
"Content-Type": "application/json",
"Accept": "text/event-stream",
"Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

# Call tool (streaming response)

response = requests.post(gateway_url, headers=headers, json={
"jsonrpc": "2.0",
"id": "tool-call-1",
"method": "tools/call",
"params": {
"name": "deployService",
"arguments": {"serviceName": "my-api", "environment": "staging"}
}
}, stream=True)

# Process SSE events

client = sseclient.SSEClient(response)
for event in client.events():
data = json.loads(event.data)
if data.get("method") == "notifications/message":
params = data["params"]
print(f"[{params['level'].upper()}] {params.get('logger', '')}: {params['data']}")
elif "result" in data:
print(f"Tool result: {data['result']}")
break

````


MCP Client

1. ```
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

async def log_handler(level, logger, data):
    """Handle log messages from the server."""
    print(f"[{level.upper()}] {logger or 'server'}: {data}")

async def use_logging(url, token):
    headers = {"Authorization": f"Bearer {token}"}

    async with streamablehttp_client(url=url, headers=headers) as (
        read_stream, write_stream, _
    ):
        async with ClientSession(
            read_stream, write_stream,
            logging_handler=log_handler
        ) as session:
            await session.initialize()

            # Call tool - log messages handled by callback
            result = await session.call_tool(
                name="deployService",
                arguments={"serviceName": "my-api", "environment": "staging"}
            )
            print(f"Tool result: {result}")
            return result

asyncio.run(use_logging(
    url="https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp",
    token="YOUR_ACCESS_TOKEN"
))
````

Strands MCP Client

1. ```

   ```

from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp import MCPClient

mcp_url = "https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
access_token = "YOUR_ACCESS_TOKEN"

mcp_client = MCPClient(
lambda: streamablehttp_client(
mcp_url, headers={"Authorization": f"Bearer {access_token}"}
)
)

# Strands handles streaming and log messages automatically

with mcp_client:
agent = Agent(tools=mcp_client.list_tools_sync())
response = agent("Deploy my-api to staging")
print(response)

```

```
