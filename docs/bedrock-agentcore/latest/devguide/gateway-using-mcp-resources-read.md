# Read a resource from an AgentCore gateway

To read a specific resource, make a POST request to the gateway’s MCP endpoint and specify `resources/read` as the method in the request body and the URI of the resource:

```
POST /mcp HTTP/1.1
Host: ${GatewayEndpoint}
Content-Type: application/json
Authorization: ${Authorization header}

${RequestBody}
```

Replace the following values:

- `${GatewayEndpoint}` – The URL of the gateway, as provided in the response of the [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") API.
- `${Authorization header}` – The authorization credentials from the identity provider when you set up [inbound authorization](gateway-inbound-auth.md "gateway-inbound-auth.md").
- `${RequestBody}` – The JSON payload of the request body, as specified in [Reading resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#reading-resources "https://modelcontextprotocol.io/specification/2025-06-18/server/resources#reading-resources") in the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro") . Include `resources/read` as the `method` and include the `uri` of the resource.
  The response returns a `contents` array where each entry includes the `uri`, `mimeType`, and either `text` (for text content) or `blob` (base64-encoded binary content).

###### Note

The `resources/read` operation proxies the request live to the downstream MCP server. The resource URI is the raw URI as returned by `resources/list` (no target prefix).

###### Note

When multiple targets expose the same resource URI, the gateway routes the request to the target with the lowest `resourcePriority` value.

###### Important

The `uri` parameter is passed through to the downstream MCP server target without sanitization. A user-provided resource URI could contain a malicious URL endpoint intended for SSRF attacks or attempt to read local filesystem paths (for example, `file:///etc/passwd`). Validate resource URIs against an allowlist of expected URI schemes and patterns before calling `resources/read`. Only use URIs returned by `resources/list` from trusted MCP server targets.

## Code samples for reading a resource

To see examples of reading a resource from the gateway, select one of the following methods:

###### Example

curl

1. The following curl request shows an example request to read a resource with URI `config://app-settings` through a gateway with the ID `mygateway-abcdefghij`.

```
curl -X POST \
  https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "id": "read-resource-request",
    "method": "resources/read",
    "params": {
      "uri": "config://app-settings"
    }
}'
```

Python requests package

1. ```
   import requests
   import json
   ```

def read_resource(gateway_url, access_token, resource_uri):
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {access_token}"
}

    payload = {
        "jsonrpc": "2.0",
        "id": "read-resource-request",
        "method": "resources/read",
        "params": {
            "uri": resource_uri
        }
    }

    response = requests.post(gateway_url, headers=headers, json=payload)
    return response.json()

# Example usage

gateway_url = "https://${GatewayEndpoint}/mcp" # Replace with your actual gateway endpoint
access_token = "${AccessToken}" # Replace with your actual access token
result = read_resource(
gateway_url,
access_token,
"config://app-settings" # Replace with the resource URI from resources/list
)
print(json.dumps(result, indent=2))

````


MCP Client

1. ```
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from pydantic import AnyUrl
import asyncio

async def execute_mcp(
    url,
    token,
    resource_uri,
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

            # 2. Read specific resource
            print(f"Reading resource: {resource_uri}")
            resource_response = await session.read_resource(uri=AnyUrl(resource_uri))
            for content in resource_response.contents:
                print(f"URI: {content.uri}, MIME: {content.mimeType}")
                if hasattr(content, 'text') and content.text:
                    print(f"Text: {content.text}")
                elif hasattr(content, 'blob') and content.blob:
                    print(f"Blob (base64): {content.blob[:100]}...")
            return resource_response

async def main():
    url = "https://${GatewayEndpoint}/mcp"
    token = "your_bearer_token_here"
    resource_uri = "config://app-settings"
    await execute_mcp(
        url=url,
        token=token,
        resource_uri=resource_uri
    )


if __name__ == "__main__":
    asyncio.run(main())
````

Strands MCP Client

1. NOTE: Strands SDK resource support may vary. Use the MCP Client approach above for the most reliable `resources/read` implementation.

```
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client

def create_streamable_http_transport(mcp_url: str, access_token: str):
    return streamablehttp_client(mcp_url, headers={"Authorization": f"Bearer {access_token}"})

def run_agent(mcp_url: str, access_token: str):
    mcp_client = MCPClient(lambda: create_streamable_http_transport(mcp_url, access_token))

    with mcp_client:
        result = mcp_client.read_resource_sync(uri="config://app-settings")
        print(result)

run_agent(<MCP URL>, <Access token>)
```

LangGraph MCP Client

1. NOTE: LangGraph MCP adapter resource support may vary. Use the MCP Client approach above for the most reliable `resources/read` implementation.

```
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from pydantic import AnyUrl

async def read_resource(url, token, resource_uri):
    headers = {"Authorization": f"Bearer {token}"}
    async with streamablehttp_client(url=url, headers=headers) as (
        read_stream, write_stream, callA
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            response = await session.read_resource(uri=AnyUrl(resource_uri))
            for content in response.contents:
                if hasattr(content, 'text') and content.text:
                    print(f"{content.uri}: {content.text}")
                elif hasattr(content, 'blob') and content.blob:
                    print(f"{content.uri}: <blob, {len(content.blob)} chars base64>")

asyncio.run(read_resource(
    "https://${GatewayEndpoint}/mcp",
    "${AccessToken}",
    "config://app-settings"
))
```

## Errors

The `resources/read` operation can return the following types of errors:

- Errors returned as part of the HTTP status code:

**AuthenticationError**

The request failed due to invalid authentication credentials.

**HTTP Status Code** : 401

**AuthorizationError**

The caller does not have permission to read the resource.

**HTTP Status Code** : 403

**ResourceNotFoundError**

The specified resource URI does not exist or is not exposed by any target.

**HTTP Status Code** : 404

**ValidationError**

The provided URI is malformed or missing.

**HTTP Status Code** : 400

**InternalServerError**

An internal server error occurred.

**HTTP Status Code** : 500

- MCP errors. For more information about these types of errors, see [Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources "https://modelcontextprotocol.io/specification/2025-06-18/server/resources") in the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro") documentation.
