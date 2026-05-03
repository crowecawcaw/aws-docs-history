# OpenSearch MCP server

[OpenSearch MCP server](https://github.com/opensearch-project/opensearch-mcp-server-py "https://github.com/opensearch-project/opensearch-mcp-server-py") (`opensearch-mcp-server-py`) is an open
source implementation of the [Model Context
Protocol](https://modelcontextprotocol.io "https://modelcontextprotocol.io") for OpenSearch. It exposes OpenSearch APIs as tools that AI
assistants and agent frameworks can call directly, so you can ask questions like
_"What indexes exist in my cluster?"_ or _"Show
me the slowest queries from the last hour"_ and the agent handles the
API calls on your behalf.

The server works with both managed OpenSearch Service domains and OpenSearch Serverless collections. You can
connect it to coding IDEs (Kiro, Claude Code, Cursor), desktop AI assistants (Claude
Desktop), and agent frameworks (Strands Agents, LangGraph).

## Prerequisites

- Python 3.10 or later.
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/") (recommended) or `pip`.
- A reachable OpenSearch endpoint: an OpenSearch Service domain, an OpenSearch Serverless collection,
  or a self-managed OpenSearch cluster.
- Credentials with permission to call the OpenSearch APIs you want to
  expose. For IAM policies on OpenSearch Service domains, see [Identity-based policies](ac.md#ac-types-identity "ac.md#ac-types-identity"). For OpenSearch Serverless data access policies, see
  [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md").

## Install

Run the server with `uvx` (no installation required) or install it
locally:

```
# Run directly with uvx (recommended – no install step)
uvx opensearch-mcp-server-py

# Or install with pip
pip install opensearch-mcp-server-py
```

Most users configure their IDE or AI assistant to start the server automatically.
See [Configure in a coding IDE](mcp-server-configure-ide.md "mcp-server-configure-ide.md") and
[Use with agent frameworks](mcp-server-configure-frameworks.md "mcp-server-configure-frameworks.md") for examples.

## Authentication

Configure authentication through environment variables (single-cluster mode) or
per cluster in a YAML config file (multi-cluster mode). The server applies
authentication methods in the following priority order: no-auth, header-based,
IAM role, basic auth, AWS access keys.

**IAM role (SigV4) – recommended for OpenSearch Service domains**

```
export OPENSEARCH_URL="`https://your-domain-endpoint`"
export AWS_IAM_ARN="arn:aws:iam::`123456789012`:role/`YourOpenSearchRole`"
export AWS_REGION="`us-east-1`"
```

The role must have permission to call the OpenSearch APIs the
server uses. See [Additional sample policies](ac.md#ac-samples "ac.md#ac-samples") for sample
policies.

**AWS credentials or profile**

```
export OPENSEARCH_URL="`https://your-domain-endpoint`"
export AWS_REGION="`us-east-1`"
export AWS_PROFILE="`your-aws-profile`"
```

**OpenSearch Serverless collections**

Set `AWS_OPENSEARCH_SERVERLESS=true` so the server signs
requests with the `aoss` service name instead of
`es`. Make sure the principal is granted access through a
data access policy on the collection (see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md")).

```
export OPENSEARCH_URL="`https://collection-id.us-east-1.aoss.amazonaws.com`"
export AWS_OPENSEARCH_SERVERLESS="true"
export AWS_REGION="`us-east-1`"
export AWS_PROFILE="`your-aws-profile`"
```

**Basic authentication**

```
export OPENSEARCH_URL="`https://your-domain-endpoint`"
export OPENSEARCH_USERNAME="`username`"
export OPENSEARCH_PASSWORD="`password`"
```

###### Important

Do not embed passwords in config files that may be checked into
source control. Use your operating system's secret manager or
shell environment to provide credentials.

## Security considerations

The MCP server runs with the credentials you provide. Anything those credentials
are authorized to do, the AI assistant can potentially trigger on your behalf.
Follow these practices:

- **Use least-privilege credentials.** Create a
  dedicated IAM role or OpenSearch user scoped to the indexes and actions
  the agent needs. Avoid reusing administrator credentials.
- **Separate development and production.**
  Point the server at non-production clusters for exploration. Use multi
  mode with explicit cluster names when production access is required.
- **Filter tools.** Disable tool categories
  your workflow does not need. Set
  `OPENSEARCH_DISABLED_CATEGORIES=core_tools` to disable the
  default set, or use `OPENSEARCH_ENABLED_CATEGORIES` to enable
  only specific categories.
- **Protect credentials.** Prefer AWS
  profiles and IAM roles over static access keys. Never commit secrets to
  config files in source control.
- **Review tool output.** MCP tool responses
  are fed back to the language model as context. Avoid running the server
  against indexes that contain sensitive data you do not want exposed to
  your AI provider.

## Troubleshooting

**The assistant does not see any OpenSearch tools**

Confirm your config file is valid JSON and restart the client fully.
Most clients only load MCP servers at startup.

**Tool calls return 403 Forbidden**

Your credentials do not have permission for the API the tool is
calling. For OpenSearch Service domains, review the domain access policy and IAM
policies attached to your role. For OpenSearch Serverless, review the collection's
data access policy.

**Signature mismatch errors with OpenSearch Serverless**

Make sure `AWS_OPENSEARCH_SERVERLESS=true` is set (or
`is_serverless: true` in multi mode). Without it, the server
signs with the `es` service name instead of
`aoss`.

**A tool you need is not available**

Check whether it lives in a non-default category and enable it with
`OPENSEARCH_ENABLED_CATEGORIES` or
`enabled_categories` in your YAML config.

For further help, open an issue in the [opensearch-mcp-server-py repository](https://github.com/opensearch-project/opensearch-mcp-server-py/issues "https://github.com/opensearch-project/opensearch-mcp-server-py/issues").

## Additional resources

- [opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py "https://github.com/opensearch-project/opensearch-mcp-server-py") on GitHub – Source, issues,
  and release notes.
- [User Guide](https://github.com/opensearch-project/opensearch-mcp-server-py/blob/main/USER_GUIDE.md "https://github.com/opensearch-project/opensearch-mcp-server-py/blob/main/USER_GUIDE.md") – Complete configuration reference including
  streaming transports and Kubernetes deployment.
- [Strands Agents](https://strandsagents.com "https://strandsagents.com") –
  AWS-native agent SDK with built-in MCP support.
- [LangGraph](https://github.com/langchain-ai/langgraph "https://github.com/langchain-ai/langgraph")
  – Low-level orchestration framework for stateful agents.
- [OpenSearch Agent Skills](opensearch-agent-skills.md "opensearch-agent-skills.md") – The companion skills
  collection for task-focused workflows.
