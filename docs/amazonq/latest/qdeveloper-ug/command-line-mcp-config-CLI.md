

# MCP configuration in the CLI
<a name="command-line-mcp-config-CLI"></a>

This page covers CLI-specific options for configuring MCP servers.

## Configuration commands
<a name="command-line-mcp-config-commands"></a>

Usage: `qchat mcp [OPTIONS] {{COMMAND}} ` 


**MCP configuration commands**  

| Command | Description | 
| --- | --- | 
|  qchat mcp add  | Add or replace a configured server | 
|  qchat mcp remove  | Remove a server from the MCP configuration | 
|  qchat mcp list  | List configured servers | 
|  qchat mcp import  | Import a server configuration from another file | 
|  qchat mcp status  | Get the status of a configured server | 
|  qchat mcp help  | Print this list of commands or help for the given subcommand(s) | 

### MCP server arguments
<a name="command-line-mcp-enhanced-args"></a>

The `--args` parameter now supports comma-containing arguments using escaping or JSON array format:

```
# Escaped commas
q mcp add --name server --command cmd --args "arg1,arg2\,with\,commas,arg3"

# JSON array format  
q mcp add --name server --command cmd --args '["arg1", "arg2,with,commas", "arg3"]'
```

## Remote MCP servers
<a name="command-line-mcp-remote-servers"></a>

In addition to local MCP servers that run as processes, Amazon Q Developer CLI supports remote MCP servers that communicate over HTTP. Remote servers can use OAuth authentication or be open (no authentication required).

### Configuration
<a name="command-line-mcp-remote-config"></a>

Remote MCP servers are configured in your agent configuration file using the `type` and `url` fields:

```
{
  "mcpServers": {
    "find-a-domain": {
      "type": "http",
      "url": "https://api.findadomain.dev/mcp"
    }
  }
}
```

### OAuth authentication flow
<a name="command-line-mcp-oauth-flow"></a>

When using remote MCP servers that require OAuth authentication:

1. Start your Q CLI session with an agent that includes the remote MCP server

1. The server will initially show as "not yet loaded"

1. Use the `/mcp` command to begin authentication

1. Q CLI will indicate that the server requires authentication and provide a URL

1. Open the provided URL in your browser while keeping the Q CLI session open

1. Follow the authentication instructions in your browser

1. Return to the Q CLI window - you will be signed into the MCP server if authentication was successful

The server's tools will become available once authentication is complete.