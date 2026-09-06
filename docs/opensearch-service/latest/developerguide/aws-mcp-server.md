

# Set up the AWS MCP Server
<a name="aws-mcp-server"></a>

The AWS MCP Server is a managed Model Context Protocol server from the Agent Toolkit for AWS. It gives your AI agent authenticated access to AWS – running AWS API calls on your behalf, executing scripts in a sandboxed environment, and serving AWS skills (including the [amazon-opensearch-service skill](amazon-opensearch-service-skill.md)) on demand. Use it to work with OpenSearch Service domains and OpenSearch Serverless collections from your agent.

**Note**  
The AWS MCP Server connects to public Amazon OpenSearch Service endpoints. It does not support domains or collections deployed in a VPC. If your OpenSearch Service domain or OpenSearch Serverless collection uses VPC access, use the open source [opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py) instead, which supports VPC connectivity through local configuration.

## Prerequisites
<a name="aws-mcp-server-prerequisites"></a>
+ An AI coding agent that supports the Agent Toolkit for AWS (such as Kiro, Claude Code, Cursor, and Codex).
+ AWS credentials configured locally (for example, an AWS CLI profile or environment credentials) with permission for the OpenSearch operations you intend to run. For domains, see [Identity-based policies](ac.md#ac-types-identity); for Serverless, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md).

## Install the aws-data-analytics plugin (recommended)
<a name="aws-mcp-server-install-plugin"></a>

The `aws-data-analytics` plugin bundles the AWS MCP Server configuration and the `amazon-opensearch-service` skill in a single install, so you do not have to configure the MCP endpoint or install the skill separately.

**Claude Code**

```
/plugin install aws-data-analytics@claude-plugins-official
/reload-plugins
```

**Codex**

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Then launch Codex and run `/plugins` to browse and install the `aws-data-analytics` plugin.

## Configure the AWS MCP Server directly
<a name="aws-mcp-server-configure-directly"></a>

If your agent does not support plugins, configure the AWS MCP Server directly. Follow [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) in the Agent Toolkit for AWS documentation, then ask your agent an OpenSearch question – it discovers the `amazon-opensearch-service` skill at runtime through the server.

## Use the AWS MCP Server without skills
<a name="aws-mcp-server-without-skills"></a>

You can use the AWS MCP Server directly without loading the `amazon-opensearch-service` skill. In this mode, the agent uses the server's built-in `call_aws` tool to invoke AWS API operations directly. This is useful for ad-hoc operations or when you want precise control over the API calls your agent makes.

For example, to create an OpenSearch Serverless collection:

```
Create an OpenSearch Serverless search collection named "my-collection" in us-east-1
```

The agent calls the OpenSearch Serverless `CreateCollection` API on your behalf using your configured credentials:

```
{
  "name": "my-collection",
  "type": "SEARCH",
  "description": "My search collection"
}
```

You can also run operations against existing resources without skills. For example:

```
List all my OpenSearch Service domains in us-east-1
Show the cluster health for my domain named production-domain
Create an index called products in my collection endpoint
```

The AWS MCP Server handles authentication and translates your natural language requests into the appropriate AWS API or OpenSearch API calls.

## Verify the setup
<a name="aws-mcp-server-verify"></a>

After installing, restart your agent so it loads the new configuration. Then ask:

```
What AWS skills do you have available for OpenSearch?
```

The agent should report the `amazon-opensearch-service` skill. Try a task such as *"List my OpenSearch Service domains"* – the agent runs the call through the AWS MCP Server using your configured credentials.

## Security considerations
<a name="aws-mcp-server-security"></a>

The AWS MCP Server runs with the credentials you provide. Follow these practices:
+ **Use least-privilege credentials.** Scope a dedicated IAM principal to the OpenSearch resources and actions the agent needs. Avoid administrator credentials.
+ **Separate development and production.** Point the server at non-production resources for exploration, and require confirmation before production changes.
+ **Protect credentials.** Prefer IAM roles and AWS CLI profiles over static access keys, and never commit secrets to configuration files in source control.
+ **Review tool output.** MCP tool responses are returned to the model as context. Avoid running the server against indexes with sensitive data you do not want exposed to your model provider.

## Troubleshooting
<a name="aws-mcp-server-troubleshooting"></a>
+ **The agent does not see any OpenSearch skills or tools** – Confirm the plugin or MCP configuration is valid and restart your agent fully. Most agents load MCP servers only at startup.
+ **Calls return 403 Forbidden** – Your credentials lack permission for the API being called. For domains, review the domain access policy and the IAM policies on your principal. For Serverless, review the collection's data access policy.

## Use with agent frameworks
<a name="aws-mcp-server-frameworks"></a>

You can integrate the AWS MCP Server into Python agent frameworks for programmatic workflows. The following examples connect to the AWS MCP Server endpoint, which provides authenticated access to OpenSearch and other AWS services.

### Strands Agents
<a name="aws-mcp-server-strands"></a>

[Strands Agents](https://strandsagents.com) is an AWS-native agent SDK with built-in MCP support and Amazon Bedrock as the default model provider.

```
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client

ENDPOINT = "https://aws-mcp.us-east-1.api.aws/mcp"
AWS_REGION = "us-east-1"

opensearch_client = MCPClient(
    lambda: aws_iam_streamablehttp_client(
        endpoint=ENDPOINT,
        aws_service="aws-mcp",
        aws_region=AWS_REGION,
    )
)

with opensearch_client:
    agent = Agent(tools=opensearch_client.list_tools_sync())
    response = agent("What OpenSearch Service domains do I have?")
    print(response)
```

Install the required packages:

```
pip install strands-agents mcp-proxy-for-aws
```

### LangGraph
<a name="aws-mcp-server-langgraph"></a>

[LangGraph](https://github.com/langchain-ai/langgraph) is a low-level orchestration framework for building stateful agents. The following example uses `mcp-proxy-for-aws` to provide an authenticated transport and `langchain-mcp-adapters` to load the AWS MCP tools into a LangChain agent backed by Amazon Bedrock.

```
import asyncio
from mcp import ClientSession
from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_aws import ChatBedrock
from langchain.agents import create_agent

ENDPOINT = "https://aws-mcp.us-east-1.api.aws/mcp"
AWS_REGION = "us-east-1"

async def main():
    async with aws_iam_streamablehttp_client(
        endpoint=ENDPOINT,
        aws_service="aws-mcp",
        aws_region=AWS_REGION,
    ) as (read_stream, write_stream, _get_session_id):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            model = ChatBedrock(
                model_id="us.anthropic.claude-opus-4-8",
                region_name=AWS_REGION,
            )
            agent = create_agent(model, tools)
            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": "What OpenSearch Service domains do I have?"}]}
            )
            print(result["messages"][-1].content)

asyncio.run(main())
```

Install the required packages:

```
pip install mcp-proxy-for-aws langchain langchain-aws langchain-mcp-adapters langgraph
```

## More information
<a name="aws-mcp-server-more-information"></a>
+ [Agent Toolkit for AWS components](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/components.html)