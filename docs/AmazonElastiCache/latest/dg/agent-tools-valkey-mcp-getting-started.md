# Getting started

## Installation

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
        "VALKEY_SSL": "true"
      }
    }
  }
}
```

Replace `<your-endpoint>` with the endpoint of your Valkey datastore. Your coding agent must have network access to the endpoint.

**Connecting to Amazon ElastiCache:** ElastiCache Valkey clusters live in a private VPC and aren't reachable directly from your local machine. For SSM tunnel setup, IAM auth token generation, and TLS handling in tunnel mode, see the [ElastiCache connection guide](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/specialized-skills/database-skills/amazon-elasticache/references/setup/connection-guide.md "https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/specialized-skills/database-skills/amazon-elasticache/references/setup/connection-guide.md") in the AWS Agent Toolkit, or install the [Amazon ElastiCache Skill](agent-tools-skills.md "agent-tools-skills.md") to let your agent handle the connection setup end-to-end. After the tunnel is established, use `VALKEY_HOST=127.0.0.1` in the config above.

Restart your MCP client after saving the configuration.

You can prompt your agent to verify the connection with:

_Use the Valkey MCP server to verify the connection to my datastore and confirm that Valkey operations are available._

## Configuration

Configure the Valkey MCP server through environment variables in your MCP client configuration. You can also use the `--readonly` flag to restrict agent access to read-only operations.

| Variable                       | Purpose                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VALKEY_HOST`                  | Specifies the endpoint of your Valkey datastore. Use `127.0.0.1` when connecting to a private ElastiCache cluster through a tunnel.                                                     |
| `VALKEY_USE_SSL`               | Set to `true` to enable TLS. This is required for ElastiCache clusters with encryption in transit enabled.                                                                              |
| `--readonly`                   | Restricts the server to the read tier and disables all write and administrative tools, making it suitable for production exploration.                                                   |
| **Optional Search Parameters** |
| `EMBEDDINGS_PROVIDER`          | Selects the embedding provider used by `add_documents` and `search`. Supported options are `bedrock`, `openai`, `ollama`, and `hash`. Use `hash` for local testing without credentials. |
| `BEDROCK_MODEL_ID`             | Overrides the default Amazon Bedrock embedding model.                                                                                                                                   |
| `OPENAI_API_KEY`               | Provides the API key required when `EMBEDDING_PROVIDER` is set to `openai`.                                                                                                             |
