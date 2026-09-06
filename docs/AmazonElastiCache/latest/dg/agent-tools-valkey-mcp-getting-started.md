

# Getting started
<a name="agent-tools-valkey-mcp-getting-started"></a>

## Installation
<a name="agent-tools-valkey-mcp-installation"></a>

**Prerequisites:** Python 3.10 or later, `uv`, Access to a Valkey datastore

**Configure your MCP client:** Add the following to your MCP client configuration:

```
{
  "mcpServers": {
    "valkey": {
      "command": "uvx",
      "args": ["awslabs.valkey-mcp-server@latest"],
      "env": {
        "VALKEY_HOST": "<your-endpoint>",
        "VALKEY_USE_SSL": "true"
      }
    }
  }
}
```

Replace `<your-endpoint>` with the endpoint of your Valkey datastore. Your coding agent must have network access to the endpoint.

**Connecting to Amazon ElastiCache:** ElastiCache Valkey clusters live in a private VPC and aren't reachable directly from your local machine. For SSM tunnel setup, IAM auth token generation, and TLS handling in tunnel mode, see the [ElastiCache connection guide](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/specialized-skills/database-skills/amazon-elasticache/references/setup/connection-guide.md) in the AWS Agent Toolkit, or install the [Amazon ElastiCache Skill](agent-tools-skills.md) to let your agent handle the connection setup end-to-end. After the tunnel is established, use `VALKEY_HOST=127.0.0.1` in the config above.

Restart your MCP client after saving the configuration.

You can prompt your agent to verify the connection with:

*Use the Valkey MCP server to verify the connection to my datastore and confirm that Valkey operations are available.*

## Configuration
<a name="agent-tools-valkey-mcp-configuration"></a>

Configure the Valkey MCP server through environment variables in your MCP client configuration. You can also use the `--readonly` flag to restrict agent access to read-only operations.


<table>
<thead>
  <tr><th>Variable</th><th>Purpose</th></tr>
</thead>
<tbody>
  <tr><td><code>VALKEY_HOST</code></td><td>Specifies the endpoint of your Valkey datastore. Use <code>127.0.0.1</code> when connecting to a private ElastiCache cluster through a tunnel.</td></tr>
  <tr><td><code>VALKEY_USE_SSL</code></td><td>Set to <code>true</code> to enable TLS. This is required for ElastiCache clusters with encryption in transit enabled.</td></tr>
  <tr><td><code>--readonly</code></td><td>Restricts the server to the read tier and disables all write and administrative tools, making it suitable for production exploration.</td></tr>
  <tr><td colspan="2"><b>Optional Search Parameters</b></td></tr>
  <tr><td><code>EMBEDDINGS_PROVIDER</code></td><td>Selects the embedding provider used by <code>add_documents</code> and <code>search</code>. Supported options are <code>bedrock</code>, <code>openai</code>, <code>ollama</code>, and <code>hash</code>. Use <code>hash</code> for local testing without credentials.</td></tr>
  <tr><td><code>BEDROCK_MODEL_ID</code></td><td>Overrides the default Amazon Bedrock embedding model.</td></tr>
  <tr><td><code>OPENAI_API_KEY</code></td><td>Provides the API key required when <code>EMBEDDING_PROVIDER</code> is set to <code>openai</code>.</td></tr>
</tbody>
</table>
