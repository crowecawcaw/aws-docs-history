

# Local connectors
<a name="local-connectors"></a>

In addition to cloud connectors, you can add a local connector that runs on your own machine, such as a local MCP server. A local connector lets Amazon Quick use tools you host yourself, such as a database, an internal API, or a developer tool, so that those tools become available to agents in chat and in scheduled tasks. Because a local connector runs on your machine, its tools are available only when that machine is on and connected. For an overview of cloud connectors, see [Connectors](action-integrations.md).

To add a local connector, open the Desktop App, go to **Customize**, and choose the **Connectors** tab. Choose **Create**, and then choose **Create local connector**. A dialog appears with three connection types: **Local**, **Import**, and **Remote**. Choose the type that matches how your MCP server runs.

## Local
<a name="local-connectors-local"></a>

**Local** runs an MCP server as a command on your machine. This is the most common option for development tools and locally installed servers.


**Local connection fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | Enter a descriptive name to identify this MCP server, such as My Database MCP. | 
| Command | Yes | Enter the executable to run, such as python, npx, node, or uvx. | 
| Arguments | No | Enter the command line arguments, separated by spaces, such as -m mcp\_server --port 8080. | 
| Description | No | Describe what this MCP server does and what tools it provides. This description helps Amazon Quick understand when to use the server's tools. | 
| Environment variables | No | Add the environment variables that the server requires. Choose \+ Add variable to add key-value pairs. | 
| Timeout (seconds) | No | Enter the maximum time to wait for the server to start, from 5 to 300 seconds. The default is 30 seconds. | 

## Import
<a name="local-connectors-import"></a>

**Import** loads MCP server configurations from an existing configuration file. This is useful when you already have MCP servers configured for another tool and want to reuse that configuration. When you enter a configuration file path, Amazon Quick scans the file, detects the MCP servers defined in it, and detects the tools installed on your system.


**Import connection fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| Config file path | Yes | Enter the path to the configuration file on your machine, such as \~/.kiro/settings/mcp.json. | 

## Remote
<a name="local-connectors-remote"></a>

**Remote** connects to an MCP server running on a remote machine or cloud service over HTTP. This is useful for shared team servers or hosted MCP services.


**Remote connection fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | Enter a descriptive name to identify this MCP server. | 
| URL | Yes | Enter the URL of the MCP endpoint, such as https://mcp.example.com/sse. | 
| Token | No | Enter a bearer token for authentication with the remote server. | 
| Description | No | Describe what this MCP server does and what tools it provides. | 
| Timeout (seconds) | No | Enter the maximum time to wait for the server to respond, from 5 to 300 seconds. The default is 30 seconds. | 