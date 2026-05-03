# Configure in a coding IDE

Coding IDEs that support MCP use a JSON configuration file to declare which
servers to start. The server runs over stdio, so the IDE launches it as a
subprocess when you open a project.

## Kiro

Create or edit `.kiro/settings/mcp.json` in your project
directory (workspace-level) or `~/.kiro/settings/mcp.json`
(user-level, available in all projects). Because Kiro runs on your local
machine, use `AWS_PROFILE` to pick up credentials from your
existing `~/.aws/credentials` file:

**Amazon OpenSearch Service domain:**

```
{
  "mcpServers": {
    "opensearch": {
      "command": "uvx",
      "args": ["opensearch-mcp-server-py"],
      "env": {
        "OPENSEARCH_URL": "`https://your-domain-endpoint.region.es.amazonaws.com`",
        "AWS_REGION":     "`us-east-1`",
        "AWS_PROFILE":    "`your-aws-profile`"
      }
    }
  }
}
```

**OpenSearch Serverless collection:**

```
{
  "mcpServers": {
    "opensearch": {
      "command": "uvx",
      "args": ["opensearch-mcp-server-py"],
      "env": {
        "OPENSEARCH_URL":            "`https://collection-id.region.aoss.amazonaws.com`",
        "AWS_OPENSEARCH_SERVERLESS": "true",
        "AWS_REGION":                "`us-east-1`",
        "AWS_PROFILE":               "`your-aws-profile`"
      }
    }
  }
}
```

After saving, Kiro reconnects the server automatically. You can then ask
questions like _"List the indexes in my cluster"_
or _"What is the health of my cluster?"_

## Claude Code

Add the server to your project's `.mcp.json` file. As with
Kiro, use `AWS_PROFILE` to authenticate with your local AWS
credentials:

**Amazon OpenSearch Service domain:**

```
{
  "mcpServers": {
    "opensearch": {
      "command": "uvx",
      "args": ["opensearch-mcp-server-py"],
      "env": {
        "OPENSEARCH_URL": "`https://your-domain-endpoint.region.es.amazonaws.com`",
        "AWS_REGION":     "`us-east-1`",
        "AWS_PROFILE":    "`your-aws-profile`"
      }
    }
  }
}
```

**OpenSearch Serverless collection:**

```
{
  "mcpServers": {
    "opensearch": {
      "command": "uvx",
      "args": ["opensearch-mcp-server-py"],
      "env": {
        "OPENSEARCH_URL":            "`https://collection-id.region.aoss.amazonaws.com`",
        "AWS_OPENSEARCH_SERVERLESS": "true",
        "AWS_REGION":                "`us-east-1`",
        "AWS_PROFILE":               "`your-aws-profile`"
      }
    }
  }
}
```

You can also add the server globally via the CLI so it is available in every
project:

```
claude mcp add opensearch \
  --command uvx \
  --args opensearch-mcp-server-py \
  --env OPENSEARCH_URL=`https://your-domain-endpoint.region.es.amazonaws.com` \
  --env AWS_REGION=`us-east-1` \
  --env AWS_PROFILE=`your-aws-profile`
```

## Claude Desktop

Open **Settings > Developer** and edit
`claude_desktop_config.json`:

```
{
  "mcpServers": {
    "opensearch": {
      "command": "uvx",
      "args": ["opensearch-mcp-server-py"],
      "env": {
        "OPENSEARCH_URL": "`https://your-domain-endpoint`",
        "AWS_REGION": "`us-east-1`",
        "AWS_PROFILE": "`your-aws-profile`"
      }
    }
  }
}
```

## Kiro CLI

If you use the Kiro CLI, add the server to your project's
`.kiro/settings/mcp.json` using the same JSON structure shown
above. The Kiro CLI picks up the config automatically when you start a
session in that directory.
