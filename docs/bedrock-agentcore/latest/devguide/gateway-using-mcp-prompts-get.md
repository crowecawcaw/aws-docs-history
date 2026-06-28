# Get a prompt from an AgentCore gateway

To get a specific prompt, make a POST request to the gateway’s MCP endpoint and specify `prompts/get` as the method in the request body, name of the prompt, and the arguments:

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
- `${RequestBody}` – The JSON payload of the request body, as specified in [Getting a prompt](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts#getting-a-prompt "https://modelcontextprotocol.io/specification/2025-06-18/server/prompts#getting-a-prompt") in the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro") . Include `prompts/get` as the `method` and include the `name` of the prompt and its `arguments`.
  The response returns the rendered prompt as an array of messages, each with a role and content.

###### Note

The `prompts/get` operation proxies the request live to the downstream MCP server. The prompt name must include the target prefix (for example, `myTarget___myPrompt`).

## Code samples for getting a prompt

To see examples of getting a prompt from the gateway, select one of the following methods:

###### Example

curl

1. The following curl request shows an example request to get a prompt called `myTarget___code_review` through a gateway with the ID `mygateway-abcdefghij`.

```
curl -X POST \
  https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "id": "get-prompt-request",
    "method": "prompts/get",
    "params": {
      "name": "myTarget___code_review",
      "arguments": {
        "language": "python",
        "code": "print(\"hello\")"
      }
    }
}'
```

Python requests package

1. ```

   ```

import requests
import json

def get_prompt(gateway_url, access_token, prompt_name, arguments):
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {access_token}"
}

    payload = {
        "jsonrpc": "2.0",
        "id": "get-prompt-request",
        "method": "prompts/get",
        "params": {
            "name": prompt_name,
            "arguments": arguments
        }
    }

    response = requests.post(gateway_url, headers=headers, json=payload)
    return response.json()

# Example usage

gateway_url = "https://${GatewayEndpoint}/mcp" # Replace with your actual gateway endpoint
access_token = "${AccessToken}" # Replace with your actual access token
result = get_prompt(
gateway_url,
access_token,
"myTarget___code_review", # Replace with {targetName}___{promptName}
{"language": "python", "code": "print('hello')"}
)
print(json.dumps(result, indent=2))

````


MCP Client

1. ```
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

async def execute_mcp(
    url,
    token,
    prompt_name,
    prompt_arguments,
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

            # 2. Get specific prompt
            print(f"Getting prompt: {prompt_name}")
            prompt_response = await session.get_prompt(
                name=prompt_name,
                arguments=prompt_arguments
            )
            print(f"Prompt response: {prompt_response}")
            return prompt_response

async def main():
    url = "https://${GatewayEndpoint}/mcp"
    token = "your_bearer_token_here"
    prompt_name = "myTarget___code_review"
    prompt_arguments = {
        "language": "python",
        "code": "print('hello')"
    }
    await execute_mcp(
        url=url,
        token=token,
        prompt_name=prompt_name,
        prompt_arguments=prompt_arguments
    )


if __name__ == "__main__":
    asyncio.run(main())
````

LangGraph MCP Client

1. NOTE: LangGraph MCP adapter prompt support may vary. Use the MCP Client approach above for the most reliable `prompts/get` implementation.

```
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def get_prompt(url, token, prompt_name, arguments):
    headers = {"Authorization": f"Bearer {token}"}
    async with streamablehttp_client(url=url, headers=headers) as (
        read_stream, write_stream, callA
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            response = await session.get_prompt(
                name=prompt_name,
                arguments=arguments
            )
            for message in response.messages:
                print(f"{message.role}: {message.content}")

asyncio.run(get_prompt(
    "https://${GatewayEndpoint}/mcp",
    "${AccessToken}",
    "myTarget___code_review",
    {"language": "python", "code": "print('hello')"}
))
```

## Errors

The `prompts/get` operation can return the following types of errors:

- Errors returned as part of the HTTP status code:

**AuthenticationError**

The request failed due to invalid authentication credentials.

**HTTP Status Code** : 401

**AuthorizationError**

The caller does not have permission to get the prompt.

**HTTP Status Code** : 403

**ResourceNotFoundError**

The specified prompt does not exist.

**HTTP Status Code** : 404

**ValidationError**

The provided arguments do not satisfy the prompt’s required arguments.

**HTTP Status Code** : 400

**InternalServerError**

An internal server error occurred.

**HTTP Status Code** : 500

- MCP errors. For more information about these types of errors, see [Prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts "https://modelcontextprotocol.io/specification/2025-06-18/server/prompts") in the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro "https://modelcontextprotocol.io/docs/getting-started/intro") documentation.
