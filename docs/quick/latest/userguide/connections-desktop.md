# Connectors

The **Connectors** tab in **Settings** > **Capabilities** lets you
manage web connectors, MCP servers, and coding agents. You can search connectors by
name, refresh the list, browse additional connectors, or create new ones using the
**+ Create** button.

## Web Connectors

Web connectors link Quick to external services such as Slack,
Microsoft Outlook, Jira, Google Calendar, and more. When you connect a service,
Quick can read from and write to that service during conversations
and agent runs.

For integration-specific setup guides, see [Integration-specific guides](integration-guides.md "integration-guides.md").

### Connecting a service

1. Expand **Settings**, and then choose
   **Capabilities**.
2. On the **Connectors** tab, find the
   service under **Web Connectors**.
3. Choose **Browse** to discover
   available connectors if none are listed.
4. Complete the authentication flow for that service.

To browse and add connectors beyond those listed, choose **Browse more**. Connectors added on the web appear
automatically in the desktop application.

## MCP Servers

The Amazon Quick desktop application supports the Model Context Protocol
(MCP), an open standard that extends the capabilities of Quick with
custom tools and integrations. You can connect MCP servers to give
Quick access to databases, internal APIs, developer tools, and
other systems that are not available through built-in connectors.

### What is MCP?

Model Context Protocol (MCP) is a protocol that allows AI assistants to
interact with external tools and data sources. When you connect an MCP
server to Quick, the tools provided by that server become
available in your chat conversations and scheduled tasks. For example, you
can connect an MCP server that provides database query tools, and then ask
Quick to query your database directly in chat.

### Accessing MCP settings

To manage your MCP servers, open **Settings**
in the sidebar, choose **Capabilities**, and
then choose the **Connectors** tab. MCP servers
are listed in the **MCP Servers** section.

You can add new servers by choosing **+ Add
MCP**.

### Adding an MCP server

When you choose **+ Create** and then choose
**MCP server**, a dialog appears with three
connection types: **Local**,
**Import**, and **Remote**. Choose the connection type that matches how your MCP
server runs.

#### Local

Use the **Local** connection type to run
an MCP server as a command on your machine. This is the most common
option for development tools and locally installed servers.

The following table describes the fields for a Local MCP
connection.

| Field                        | Required | Description                                                                                                                              |
| ---------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                     | Yes      | A friendly name to identify this MCP server (for<br>example, "My Database MCP").                                                         |
| **Command**                  | Yes      | The executable to run. Common values include<br>`python`, `npx`,<br>`node`, and `uvx`.                                                   |
| **Arguments**                | No       | Command line arguments, separated by spaces (for<br>example, `-m mcp_server --port 8080`).                                               |
| **Description**              | No       | A description of what this MCP server does and what<br>tools it provides. This helps Quick<br>understand when to use the server's tools. |
| **Environment<br>variables** | No       | Environment variables required by the server. Choose<br>\*_+ Add variable_<br>• to add<br>key-value pairs.                               |
| **Timeout<br>(seconds)**     | No       | Maximum time to wait for the server to start, from 5<br>to 300 seconds. The default is 30 seconds.                                       |

###### To add a local MCP server

Use the following procedure.

1. Open **Settings** in the sidebar
   and choose **Capabilities**.
2. Choose the **Connectors**
   tab.
3. In the **MCP Servers** section,
   choose **+ Create**, and then choose **MCP server**.
4. Choose **Local** as the
   connection type.
5. Enter a **Name** and the
   **Command** to run (for example,
   `python`).
6. Enter any **Arguments** the
   command requires (for example,
   `-m my_mcp_server`).
7. Choose **Save**.

#### Import

Use the **Import** connection type to
load MCP server configurations from an existing configuration file. This
is useful when you already have MCP servers configured for other tools
and want to reuse that configuration in Quick.

Quick supports configuration files from the following
tools.

- Kiro
- Claude Code
- AIM
- Antigravity
- QuickWork exports

The following table describes the fields for an Import MCP
connection.

| Field                   | Required | Description                                                                                          |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| **Config file<br>path** | Yes      | The path to the configuration file on your machine<br>(for example,<br>`~/.kiro/settings/mcp.json`). |

When you enter a configuration file path, Quick
automatically scans the file and detects the MCP servers defined in it.
Quick also detects tools installed on your system and
displays them as chips (for example, "Kiro", "AIM", "Claude Code")
under **Detected on this system**.

###### To import MCP servers from a config file

Use the following procedure.

1. Open **Settings** in the sidebar
   and choose **Capabilities**.
2. Choose the **Connectors**
   tab.
3. In the **MCP Servers** section,
   choose **+ Create**, and then choose **MCP server**.
4. Choose **Import** as the
   connection type.
5. Enter the **Config file path**
   to your existing MCP configuration file.
6. Review the detected servers and system tools.
7. Choose **Load file** to import
   the servers.

#### Remote

Use the **Remote** connection type to
connect to an MCP server running on a remote machine or cloud service
over HTTP. This is useful for shared team servers or hosted MCP
services.

The following table describes the fields for a Remote MCP
connection.

| Field                    | Required | Description                                                                                             |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------- |
| **Name**                 | Yes      | A friendly name to identify this MCP<br>server.                                                         |
| **URL**                  | Yes      | The URL of the MCP endpoint (for example,<br>`https://mcp.example.com/sse`).                            |
| **Token**                | No       | A bearer token for authentication with the remote<br>server.                                            |
| **Description**          | No       | A description of what this MCP server does and what<br>tools it provides.                               |
| **Timeout<br>(seconds)** | No       | Maximum time to wait for the server to respond,<br>from 5 to 300 seconds. The default is 30<br>seconds. |

###### To add a remote MCP server

Use the following procedure.

1. Open **Settings** in the sidebar
   and choose **Capabilities**.
2. Choose the **Connectors**
   tab.
3. In the **MCP Servers** section,
   choose **+ Create**, and then choose **MCP server**.
4. Choose **Remote** as the
   connection type.
5. Enter a **Name** and the
   **URL** of the MCP
   endpoint.
6. (Optional) Enter a **Token** if
   the server requires authentication.
7. Choose **Save**.

### Managing MCP servers

After you add MCP servers, they appear in the MCP Servers section of the
Connectors tab. You can manage your servers using the following
features.

- **Search** – Use the search bar
  to find servers by name.
- **Filter** – Use the dropdown
  filter to show all servers or filter by status.
- **Toggle** – Turn individual
  MCP servers on or off without removing them.
- **Edit** – Modify server
  configuration.
- **Remove** – Delete a server
  connection.

### Using MCP tools in scheduled tasks

You can attach MCP servers to scheduled tasks as capabilities. When you
create or edit a scheduled task, you can select which MCP servers the task
has access to. This allows your automated tasks to use custom tools when
they run.

To attach MCP capabilities to a scheduled task, open **Mission Control** from the top bar, select the task,
choose the **Capabilities** tab, and select
the MCP servers you want to make available.

###### Note

MCP servers must be running and accessible when a scheduled task
attempts to use their tools. For local MCP servers, the server process
starts automatically when needed. For remote servers, verify that the
server is online and reachable.

## Coding Agents

Coding agents are external AI coding tools that Quick can
delegate development tasks to. They use the Agent Client Protocol (ACP) to
communicate with tools such as Kiro or Claude Code. When enabled, you can ask
Quick to send work to a coding agent for implementation. Each
coding agent shows its name, description, and a toggle to enable or disable
it.

###### To add a coding agent

Use the following procedure.

1. Open **Settings** in the sidebar and
   choose **Capabilities**.
2. Choose the **Connectors** tab.
3. In the **Coding Agents** section, choose
   **+ Create**, and then choose **Coding agent**.
4. Configure the agent connection settings and choose **Save**.

After you configure a coding agent, you can delegate tasks to it from chat.
For example, you can say "use Kiro to refactor this module" or "ask Claude Code
to write tests for this function." Quick dispatches the work to the
coding agent and reports the results back to you.

## Activity feed integration

After you connect messaging, email, or calendar services, you can configure
which services surface items in your activity feed. To configure feed sources,
expand **Settings**, choose **Customization**, and then choose **Activity
feed**.
