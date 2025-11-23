# List available tools in an AgentCore gateway

To list all available tools that an AgentCore gateway provides, make a POST request to the gateway's MCP endpoint and specify `tools/list` as the method in the request body:

```
POST /mcp HTTP/1.1
Host: `${GatewayEndpoint}`
Content-Type: application/json
Authorization: `${Authorization header}`

`${RequestBody}`
```

Replace the following values:

- `${GatewayEndpoint}` – The URL of the gateway, as provided in the response of the [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") API.
- `${Authorization header}` – The authorization credentials from the identity provider when you set up [inbound authorization](gateway-inbound-auth.md "gateway-inbound-auth.md").
- `${RequestBody}` – The JSON payload of the request body, as specified in [Listing tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#listing-tools "https://modelcontextprotocol.io/specification/2025-06-18/server/tools#listing-tools") in the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro"). Include `tools/list` as the `method`.

###### Note

For a list of optionally supported parameters for `tools/list`, see the `params` object in the request body at [Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools "https://modelcontextprotocol.io/specification/2025-06-18/server/tools") in the [Model Context Protocol documentation](https://modelcontextprotocol.io/specification/2025-06-18 "https://modelcontextprotocol.io/specification/2025-06-18"). At the top of the page next to the search bar, you can select the MCP version whose documentation you want to view. Make sure that the version is one [supported by Amazon Bedrock AgentCore](gateway-using.md "gateway-using.md").

The response returns a list of available tools with their names, descriptions, and parameter schemas.

## Code samples for listing tools

To see examples of listing available tools in the gateway, select one of the following methods:

Python requests package

```
import requests
import json

def list_tools(gateway_url, access_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "jsonrpc": "2.0",
        "id": "list-tools-request",
        "method": "tools/list"
    }

    response = requests.post(gateway_url, headers=headers, json=payload)
    return response.json()

# Example usage
gateway_url = "https://`${GatewayEndpoint}`/mcp" # Replace with your actual gateway endpoint
access_token = "`${AccessToken}"` # Replace with your actual access token
tools = list_tools(gateway_url, access_token)
print(json.dumps(tools, indent=2))
```

MCP Client

```
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def execute_mcp(
    url,
    token,
    headers=None
):
    default_headers = {
        "Authorization": f"Bearer {token}"
    }
    headers = {**default_headers, **(headers or {})}

    async with streamablehttp_client(
       url=url,
       headers=headers,
    ) as (
        read_stream,
        write_stream,
        callA,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            # 1. Perform initialization handshake
            print("Initializing MCP...")
            _init_response = await session.initialize()
            print(f"MCP Server Initialize successful! - {_init_response}")

            # 2. List available tools
            print("Listing tools...")
            cursor = True
            tools = []
            while cursor:
                next_cursor = cursor
                if type(cursor) == bool:
                    next_cursor = None
                list_tools_response = await session.list_tools(next_cursor)
                tools.extend(list_tools_response.tools)
                cursor = list_tools_response.nextCursor

            tool_names = []
            if tools:
                for tool in tools:
                    tool_names.append(tool.name)
            tool_names_string = "\n".join(tool_names)
            print(
                f"List MCP tools. # of tools - {len(tools)}"
                f"List of tools - \n{tool_names_string}\n"
            )

async def main():
    url = "https://${GatewayEndpoint}/mcp"
    token = "your_bearer_token_here"

    # Optional additional headers
    additional_headers = {
        "Content-Type": "application/json",
    }

    await execute_mcp(
        url=url,
        token=token,
        headers=additional_headers
    )

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())

```

Strands MCP Client

```
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client
import os

def create_streamable_http_transport(mcp_url: str, access_token: str):
       return streamablehttp_client(mcp_url, headers={"Authorization": f"Bearer {access_token}"})

def get_full_tools_list(client):
    """
    List tools w/ support for pagination
    """
    more_tools = True
    tools = []
    pagination_token = None
    while more_tools:
        tmp_tools = client.list_tools_sync(pagination_token=pagination_token)
        tools.extend(tmp_tools)
        if tmp_tools.pagination_token is None:
            more_tools = False
        else:
            more_tools = True
            pagination_token = tmp_tools.pagination_token
    return tools

def run_agent(mcp_url: str, access_token: str):
    mcp_client = MCPClient(lambda: create_streamable_http_transport(mcp_url, access_token))

    with mcp_client:
        tools = get_full_tools_list(mcp_client)
        print(f"Found the following tools: {[tool.tool_name for tool in tools]}")

run_agent(<MCP URL>, <Access token>)

```

LangGraph MCP Client

```

import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


def list_tools(
    url,
    headers
):
    mcp_client = MultiServerMCPClient(
        {
            "agent": {
                "transport": "streamable_http",
                "url": url,
                "headers": headers,
            }
        }
    )
    tools = asyncio.run(mcp_client.get_tools())
    tool_details = []
    tool_names = []
    for tool in tools:
        tool_names.append(f"{tool.name}")
        tool_detail = f"{tool.name} - {tool.description} \n"

        tool_properties = tool.args_schema.get('properties', {})
        properties = []
        for property_name, tool_property in tool_properties.items():
            properties.append(f"{property_name} - {tool_property.get('description', None)} \n")
        tool_details.append(f"{tool_detail}{"\n".join(properties)}")

    tool_details_string = "\n".join(tool_details)
    tool_names_string = "\n".join(tool_names)
    print(
        f"Langchain: List MCP tools. # of tools - {len(tools)}\n",
        f"Langchain: List of tool names - \n{tool_names_string}\n"
        f"Langchain: Details of tools - \n{tool_details_string}\n"
    )

```

###### Note

If search is enabled on the gateway, then the search tool, `x_amz_bedrock_agentcore_search`
will be listed first in the response.
