# Use a AgentCore Gateway with AgentCore Policy

Follow the gateway authorization and authentication guide to obtain the credentials
needed for gateway access.

###### Topics

- [List AgentCore Gateway Tools with AgentCore Policy](#list-gateway-tools "#list-gateway-tools")
- [Call gateway tools with policy](#call-gateway-tools "#call-gateway-tools")
- [Policy responses](#policy-responses "#policy-responses")

## List AgentCore Gateway Tools with AgentCore Policy

List available tools in your gateway. Depending on your policies, only authorized
tools will be returned in the response.

Select one of the following methods:

curl

```

curl -X POST \
  https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "id": "list-tools-request",
    "method": "tools/list"
  }'

```

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
gateway_url = "https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
access_token = "YOUR_ACCESS_TOKEN"
tools = list_tools(gateway_url, access_token)
print(json.dumps(tools, indent=2))

```

The response returns only the tools that your policies allow you to
see. Tools that are denied by policies will not appear in the
list.

## Call gateway tools with policy

Make tool calls to your gateway. Policy evaluation determines whether the call is
allowed or denied.

Select one of the following methods:

curl

```

# Call a tool to test policy enforcement
curl -X POST \
  https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "jsonrpc": "2.0",
    "id": "test-policy",
    "method": "tools/call",
    "params": {
      "name": "tool_name",
      "arguments": {arguments}
    }
  }'

```

Python requests package

```

import requests
import json

def call_gateway_tool(gateway_url, access_token, tool_name, arguments):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "jsonrpc": "2.0",
        "id": "test-policy",
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }

    response = requests.post(gateway_url, headers=headers, json=payload)
    return response.json()

# Example usage
gateway_url = "https://mygateway-abcdefghij.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
access_token = "YOUR_ACCESS_TOKEN"
result = call_gateway_tool(
    gateway_url,
    access_token,
    "RefundTool__process_refund",
    {
        "orderId": "12345",
        "amount": 450,
        "reason": "Defective product"
    }
)
print(json.dumps(result, indent=2))

```

## Policy responses

When a policy allows the request:

```

{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "isError": false,
    "content": [
      {
        "type": "text",
        "text": "ToolResult"
      }
    ]
  }
}

```

When a policy denies the request:

```

{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "AuthorizeActionException - Tool Execution Denied: Tool call not allowed due to policy enforcement [No policy applies to the request (denied by default).]"
      }
    ],
    "isError": true
  }
}

```
