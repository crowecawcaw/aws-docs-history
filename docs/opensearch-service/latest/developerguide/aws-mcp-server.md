# Set up the AWS MCP Server

The AWS MCP Server is a managed Model Context Protocol server from the Agent
Toolkit for AWS. It gives your AI agent authenticated access to AWS – running
AWS API calls on your behalf, executing scripts in a sandboxed environment, and serving
AWS skills (including the [amazon-opensearch-service skill](amazon-opensearch-service-skill.md "amazon-opensearch-service-skill.md")) on demand.
Use it to work with OpenSearch Service domains and OpenSearch Serverless collections from your agent.

###### Note

The AWS MCP Server connects to public Amazon OpenSearch Service endpoints. It does not support
domains or collections deployed in a VPC. If your OpenSearch Service domain or OpenSearch Serverless collection
uses VPC access, use the open source [opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py "https://github.com/opensearch-project/opensearch-mcp-server-py") instead, which supports VPC connectivity
through local configuration.

## Prerequisites

- An AI coding agent that supports the Agent Toolkit for AWS (such as
  Kiro, Claude Code, Cursor, and Codex).
- AWS credentials configured locally (for example, an AWS CLI profile
  or environment credentials) with permission for the OpenSearch operations
  you intend to run. For domains, see [Identity-based policies](ac.md#ac-types-identity "ac.md#ac-types-identity"); for
  Serverless, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md").

## Install the aws-data-analytics plugin (recommended)

The `aws-data-analytics` plugin bundles the AWS MCP Server
configuration and the `amazon-opensearch-service` skill in a single
install, so you do not have to configure the MCP endpoint or install the skill
separately.

**Claude Code**

```
/plugin install aws-data-analytics@claude-plugins-official
/reload-plugins
```

**Codex**

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Then launch Codex and run `/plugins` to browse and install the
`aws-data-analytics` plugin.

## Configure the AWS MCP Server directly

If your agent does not support plugins, configure the AWS MCP Server directly.
Follow [Setting up the AWS MCP Server](../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md "../../../agent-toolkit/latest/userguide/getting-started-aws-mcp-server.md") in the Agent Toolkit for AWS
documentation, then ask your agent an OpenSearch question – it discovers
the `amazon-opensearch-service` skill at runtime through the
server.

## Use the AWS MCP Server without skills

You can use the AWS MCP Server directly without loading the
`amazon-opensearch-service` skill. In this mode, the agent uses the
server's built-in `call_aws` tool to invoke AWS API operations
directly. This is useful for ad-hoc operations or when you want precise control
over the API calls your agent makes.

For example, to create an OpenSearch Serverless collection:

```
Create an OpenSearch Serverless search collection named "my-collection" in us-east-1
```

The agent calls the OpenSearch Serverless `CreateCollection` API on your behalf
using your configured credentials:

```
{
  "name": "my-collection",
  "type": "SEARCH",
  "description": "My search collection"
}
```

You can also run operations against existing resources without skills. For
example:

```
List all my OpenSearch Service domains in us-east-1
Show the cluster health for my domain named production-domain
Create an index called products in my collection endpoint
```

The AWS MCP Server handles authentication and translates your natural language
requests into the appropriate AWS API or OpenSearch API calls.

## Verify the setup

After installing, restart your agent so it loads the new configuration. Then
ask:

```
What AWS skills do you have available for OpenSearch?
```

The agent should report the `amazon-opensearch-service` skill. Try a
task such as _"List my OpenSearch Service domains"_
– the agent runs the call through the AWS MCP Server using your configured
credentials.

## Security considerations

The AWS MCP Server runs with the credentials you provide. Follow these
practices:

- **Use least-privilege credentials.** Scope a
  dedicated IAM principal to the OpenSearch resources and actions the
  agent needs. Avoid administrator credentials.
- **Separate development and production.** Point
  the server at non-production resources for exploration, and require
  confirmation before production changes.
- **Protect credentials.** Prefer IAM roles
  and AWS CLI profiles over static access keys, and never commit secrets to
  configuration files in source control.
- **Review tool output.** MCP tool responses
  are returned to the model as context. Avoid running the server against
  indexes with sensitive data you do not want exposed to your model
  provider.

## Troubleshooting

- **The agent does not see any OpenSearch skills or
  tools** – Confirm the plugin or MCP configuration is
  valid and restart your agent fully. Most agents load MCP servers only at
  startup.
- **Calls return 403 Forbidden** – Your
  credentials lack permission for the API being called. For domains, review
  the domain access policy and the IAM policies on your principal. For
  Serverless, review the collection's data access policy.

## Use with agent frameworks

You can integrate the AWS MCP Server into Python agent frameworks for
programmatic workflows. The following examples connect to the AWS MCP Server
endpoint, which provides authenticated access to OpenSearch and other AWS
services.

### Strands Agents

[Strands Agents](https://strandsagents.com "https://strandsagents.com") is an
AWS-native agent SDK with built-in MCP support and Amazon Bedrock as the
default model provider.

```
import boto3
import os
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

# Get credentials for signing
session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

opensearch_client = MCPClient(
    lambda: streamablehttp_client(
        "https://aws-mcp.us-east-1.api.aws/mcp",
        headers={
            "AWS_REGION": os.environ.get("AWS_REGION", "us-east-1"),
        }
    )
)

with opensearch_client:
    agent = Agent(tools=opensearch_client.list_tools_sync())
    response = agent("List all OpenSearch Service domains and show the cluster health for each")
    print(response)
```

### LangGraph

[LangGraph](https://github.com/langchain-ai/langgraph "https://github.com/langchain-ai/langgraph") is
a low-level orchestration framework for building stateful agents. The following
example uses `langchain-mcp-adapters` to load AWS MCP tools into
a LangGraph ReAct agent backed by Amazon Bedrock.

```
import asyncio
import os
from langchain_aws import ChatBedrock
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

async def main():
    async with MultiServerMCPClient(
        {
            "aws-mcp": {
                "url": "https://aws-mcp.us-east-1.api.aws/mcp",
                "transport": "streamable_http",
                "headers": {
                    "AWS_REGION": os.environ.get("AWS_REGION", "us-east-1"),
                },
            }
        }
    ) as mcp_client:
        tools = mcp_client.get_tools()
        model = ChatBedrock(
            model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
            region_name=os.environ["AWS_REGION"],
        )
        agent = create_react_agent(model, tools)
        result = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "Check cluster health and list all OpenSearch indexes"}]}
        )
        print(result["messages"][-1].content)

asyncio.run(main())
```

Install the required packages:

```
pip install langchain-aws langchain-mcp-adapters langgraph
```

## More information

- [Agent Toolkit for AWS components](../../../agent-toolkit/latest/userguide/components.md "../../../agent-toolkit/latest/userguide/components.md")
