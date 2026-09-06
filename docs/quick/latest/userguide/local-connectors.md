# Local connectors

In addition to cloud connectors, you can add a local connector that
runs on your own machine, such as a local MCP server. A local connector
lets Amazon Quick use tools you host yourself, such as a database, an
internal API, or a developer tool, so that those tools become available
to agents in chat and in scheduled tasks. Because a local connector runs
on your machine, its tools are available only when that machine is on and
connected. For an overview of cloud connectors, see
[Connectors](action-integrations.md "action-integrations.md").

To add a local connector, open the Desktop App, go to
**Customize**, and choose the
**Connectors** tab. Choose **Create**,
and then choose **Create local connector**. A dialog
appears with three connection types: **Local**,
**Import**, and **Remote**. Choose the
type that matches how your MCP server runs.

## Local

**Local** runs an MCP server as a command on your
machine. This is the most common option for development tools and
locally installed servers.

Local connection fields| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Enter a descriptive name to identify this MCP<br>server, such as `My Database MCP`. |
| **Command** | Yes | Enter the executable to run, such as<br>`python`, `npx`,<br>`node`, or `uvx`. |
| **Arguments** | No | Enter the command line arguments, separated by<br>spaces, such as<br>`-m mcp_server --port 8080`. |
| **Description** | No | Describe what this MCP server does and what tools<br>it provides. This description helps Amazon Quick<br>understand when to use the server's tools. |
| **Environment variables** | No | Add the environment variables that the server<br>requires. Choose **+ Add variable**<br>to add key-value pairs. |
| **Timeout (seconds)** | No | Enter the maximum time to wait for the server to<br>start, from 5 to 300 seconds. The default is 30<br>seconds. |

## Import

**Import** loads MCP server configurations from an
existing configuration file. This is useful when you already have MCP
servers configured for another tool and want to reuse that
configuration. When you enter a configuration file path,
Amazon Quick scans the file, detects the MCP servers defined in it,
and detects the tools installed on your system.

Import connection fields| Field | Required | Description |
| --- | --- | --- |
| **Config file path** | Yes | Enter the path to the configuration file on your<br>machine, such as<br>`~/.kiro/settings/mcp.json`. |

## Remote

**Remote** connects to an MCP server running on a
remote machine or cloud service over HTTP. This is useful for shared
team servers or hosted MCP services.

Remote connection fields| Field | Required | Description |
| --- | --- | --- |
| **Name** | Yes | Enter a descriptive name to identify this MCP<br>server. |
| **URL** | Yes | Enter the URL of the MCP endpoint, such as<br>`https://mcp.example.com/sse`. |
| **Token** | No | Enter a bearer token for authentication with the<br>remote server. |
| **Description** | No | Describe what this MCP server does and what tools<br>it provides. |
| **Timeout (seconds)** | No | Enter the maximum time to wait for the server to<br>respond, from 5 to 300 seconds. The default is 30<br>seconds. |
