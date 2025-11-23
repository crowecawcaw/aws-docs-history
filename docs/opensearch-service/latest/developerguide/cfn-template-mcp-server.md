# MCP server integration templates

With the Model Context Protocol (MCP) server templates, you can deploy an
OpenSearch hosted MCP server on Amazon Bedrock AgentCore, reducing the integration
complexity between AI agents and OpenSearch tools. For more information, see [What is
Amazon Bedrock AgentCore?](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md").

## Template features

This template includes the following key features for deploying and managing
your MCP server.

**Managed MCP server deployment**

Deploys **opensearch-mcp-server-py** using Amazon Bedrock
AgentCore Runtime, and provides an agent endpoint that proxies
requests to the underlying MCP server. For more information, see
[opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py "https://github.com/opensearch-project/opensearch-mcp-server-py") on
_GitHub_.

**Authentication and security**

Handles both inbound authentication (from users to MCP server) and
outbound authentication (from MCP server to OpenSearch), and supports
OAuth for enterprise authentication.

###### Note

The MCP server template is only available in the following
AWS Regions:

- US East (N. Virginia)
- US West (Oregon)
- Europe (Frankfurt)
- Asia Pacific (Sydney)

## To use the MCP server

template

Follow these steps to deploy the MCP server template and connect it to your
OpenSearch domain.

1. Open the [Amazon OpenSearch Service
   console](https://console.aws.amazon.com//aos/home "https://console.aws.amazon.com//aos/home ").
2. In the left navigation pane, choose
   **Integrations**.
3. Locate the **MCP server integration**
   template.
4. Choose **Configure domain**. Then, enter your
   OpenSearch domain endpoint.

The template creates an AgentCore Runtime and the following components, if the
corresponding optional parameters are not specified:

- An Amazon ECR repository
- An Amazon Cognito user pool as the OAuth authorizer
- An execution role used by the AgentCore Runtime

After you complete this procedure, you should follow these post-creation
steps:

1. **For Amazon OpenSearch Service**: Map your execution role
   ARN to an OpenSearch backend role to control access to your
   domain.

**For Amazon OpenSearch Serverless**: Create a data access
policy that allows your execution role to access your collection. 2. Get an OAuth access token from your authorizer. Then use this token to
access the MCP server at the URL listed in your CloudFormation stack
output.

For more information, see [Policy actions for
OpenSearch Serverless](security-iam-serverless.md#security-iam-serverless-id-based-policies-actions "security-iam-serverless.md#security-iam-serverless-id-based-policies-actions").

## Integration with AI

agents

After deployment, you can integrate the MCP server with any MCP compatible
agent. For more information, see [Invoke your deployed MCP server](../../../bedrock-agentcore/latest/devguide/runtime-mcp.md#runtime-mcp-invoke-server "../../../bedrock-agentcore/latest/devguide/runtime-mcp.md#runtime-mcp-invoke-server") in the _Amazon Bedrock Developer
Guide_.

**Developer Integration**

You can add the MCP server endpoint to your agent configuration.
You can also use it with the Amazon Q Developer CLI, custom agents, or other
MCP-compatible agents.

**Enterprise Deployment**

Central hosted agents can connect to multiple services with
OpenSearch as one component. This agent supports OAuth and enterprise
authentication systems, and scales to support multiple users and use
cases.

```
import os
import requests
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

def get_bearer_token(discovery_url: str, client_id: str, client_secret: str):
    response = requests.get(discovery_url)
    discovery_data = response.json()
    token_endpoint = discovery_data['token_endpoint']

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(token_endpoint, data=data, headers=headers)
    token_data = response.json()
    return token_data['access_token']

if __name__ == "__main__":
    discovery_url = os.environ["DISCOVERY_URL"]
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    mcp_url = os.environ["MCP_URL"]

    bearer_token = get_bearer_token(discovery_url, client_id, client_secret)

    opensearch_mcp_client = MCPClient(lambda: streamablehttp_client(mcp_url, {
        "authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }))

    with opensearch_mcp_client:
        tools = opensearch_mcp_client.list_tools_sync()
        agent = Agent(tools=tools)
        agent("list indices")
```

For more information, see [Hosting OpenSearch MCP Server with Amazon Bedrock AgentCore](https://opensearch.org/blog/hosting-opensearch-mcp-server-with-amazon-bedrock-agentcore/ "https://opensearch.org/blog/hosting-opensearch-mcp-server-with-amazon-bedrock-agentcore/") on the
_OpenSearch website_.
