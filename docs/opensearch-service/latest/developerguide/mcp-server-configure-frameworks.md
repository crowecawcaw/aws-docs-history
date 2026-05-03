# Use with agent frameworks

You can integrate the OpenSearch MCP server directly into Python agent
frameworks, giving your autonomous agents programmatic access to OpenSearch as
part of a larger workflow.

## Strands Agents

[Strands Agents](https://strandsagents.com "https://strandsagents.com") is an
AWS-native agent SDK with built-in MCP support and Amazon Bedrock as the
default model provider. The following example connects a Strands agent to
either an OpenSearch Service domain or an OpenSearch Serverless collection by setting the appropriate
environment variables. Set `AWS_OPENSEARCH_SERVERLESS` to
`true` when connecting to an OpenSearch Serverless collection; omit it for a
managed domain.

```
import os
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

# For a managed domain:
#   OPENSEARCH_URL = https://<domain-endpoint>.<region>.es.amazonaws.com
#
# For an OpenSearch Serverless collection, also set:
#   AWS_OPENSEARCH_SERVERLESS = true
#   OPENSEARCH_URL = https://<collection-id>.<region>.aoss.amazonaws.com
opensearch_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["opensearch-mcp-server-py"],
            env={
                "OPENSEARCH_URL":            os.environ["OPENSEARCH_URL"],
                "AWS_REGION":                os.environ["AWS_REGION"],
                "AWS_IAM_ARN":               os.environ["AWS_IAM_ARN"],
                # Set to "true" for OpenSearch Serverless, omit for managed domains
                "AWS_OPENSEARCH_SERVERLESS": os.environ.get("AWS_OPENSEARCH_SERVERLESS", "false"),
            },
        )
    )
)

with opensearch_client:
    agent = Agent(tools=opensearch_client.list_tools_sync())
    response = agent("List all indexes and show the document count for each")
    print(response)
```

Strands uses Amazon Bedrock as its default model provider. Make sure you have
AWS credentials configured and model access enabled for Claude in your
region. For details, see the [Strands Bedrock provider](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/ "https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/") documentation.

## LangGraph

[LangGraph](https://github.com/langchain-ai/langgraph "https://github.com/langchain-ai/langgraph") is
a low-level orchestration framework for building stateful agents. The following
example uses `langchain-mcp-adapters` to load the OpenSearch MCP
tools into a LangGraph ReAct agent backed by Amazon Bedrock. As with Strands,
set `AWS_OPENSEARCH_SERVERLESS` to `true` when
connecting to an OpenSearch Serverless collection.

```
import asyncio
import os
from langchain_aws import ChatBedrock
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

async def main():
    async with MultiServerMCPClient(
        {
            "opensearch": {
                "command": "uvx",
                "args": ["opensearch-mcp-server-py"],
                "env": {
                    # Managed domain:  https://<domain-endpoint>.<region>.es.amazonaws.com
                    # Serverless:      https://<collection-id>.<region>.aoss.amazonaws.com
                    "OPENSEARCH_URL":            os.environ["OPENSEARCH_URL"],
                    "AWS_REGION":                os.environ["AWS_REGION"],
                    "AWS_IAM_ARN":               os.environ["AWS_IAM_ARN"],
                    # Set to "true" for OpenSearch Serverless, omit for managed domains
                    "AWS_OPENSEARCH_SERVERLESS": os.environ.get("AWS_OPENSEARCH_SERVERLESS", "false"),
                },
                "transport": "stdio",
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
            {"messages": [{"role": "user", "content": "Check cluster health and list all indexes"}]}
        )
        print(result["messages"][-1].content)

asyncio.run(main())
```

Install the required packages:

```
pip install langchain-aws langchain-mcp-adapters langgraph
```
