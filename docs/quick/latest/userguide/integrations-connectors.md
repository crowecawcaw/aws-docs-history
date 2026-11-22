

# Connectors

Connectors bring cloud connectors, system tools, local connectors, and coding agents together in one place, with a catalog to discover and add new ones. A connector links AWS Quick to an external application or a native tool so agents can access data and act on your behalf. You manage connectors from the **Integrations** page. Connectors cover four capabilities.
+ Cloud connectors connect Quick to external services such as Outlook, SharePoint, OneDrive, Slack, Jira, Asana, Airtable, and Salesforce, as well as remotely hosted Model Context Protocol (MCP) servers. After a cloud connector is connected, it is reachable from any device where you use Quick, including the web, mobile, and desktop application. For the full list, see [Supported integrations](supported-integrations.md).
+ System tools are the capabilities that Quick provides out of the box, such as image generation, browser automation, and research. You do not install or sign in to them, but you can turn them on or off. Some run in the cloud, and others, such as browser automation, are specific to a device. For the full list, see [Built-in system tools](system-tools.md).
+ Local connectors run on your own machine and cover local MCP servers that you host yourself. Local connectors are a capability of the AWS Quick desktop application, and their tools are available only when that machine is on and connected.
+ Coding agents, such as Kiro and Claude Code, run on your own machine so you can delegate development work to them from chat. Coding agents are a capability of the AWS Quick desktop application.

## Discovering and adding connectors
<a name="connectors-discovering"></a>

You can discover and add connectors that expand what AWS Quick can do for you. To see the full catalog, choose **Browse all**. Each connector card shows its name and a short description of what it does. Connectors that you add appear automatically in the connectors table.

**Adding a cloud connector**  
Cloud connectors in the catalog are either connectors that have been shared with you or connectors that you can set up with a single choice of **Install** followed by a sign-in. The **Suggested for you** area contains cloud connectors that have already been set up and shared with you, along with the most popular cloud connectors for Quick users. When you install one of these connectors, by default AWS Quick connects to the external service through an Amazon-hosted OAuth application for that service. OAuth applications are the standard way an application, such as Quick, makes calls to an external application, such as Outlook or Salesforce, on your behalf. An end-user sign-in is also required.

Some enterprises prefer to use their own OAuth application rather than the Amazon default. To do this, choose **Create**, and then choose **Cloud connector**. This option gives additional enterprise admin controls during setup, such as setting a connector's name, description, who it is shared with, and its tool permissions. Connectors that do not have an Amazon default OAuth application are also found in the **Create** section. Creating a custom connection to a remotely hosted MCP server also uses **Create** and then **Cloud connector**.

**Adding a local connector**  
Beyond the connectors in the catalog, you can add a local connector that runs on your own machine, such as a local MCP server. Adding a local connector is a capability of the AWS Quick desktop application. A local connector lets Quick use tools that you host yourself, such as a database, an internal API, or a developer tool, so those tools become available to agents in chat and in scheduled tasks. Because a local connector runs on your machine, its tools are available only when that machine is on and connected. For the MCP server fields, see [MCP servers](#connectors-mcp-servers).

**Adding a coding agent**  
You can also connect a coding agent, an external AI coding tool such as Kiro or Claude Code, that AWS Quick can hand development work to. Adding a coding agent is a capability of the AWS Quick desktop application. After a coding agent is connected and enabled, you can delegate tasks to it from chat, and it does the work and reports back. For more information, see [Coding agents](#connectors-coding-agents).

## Managing your installed connectors
<a name="connectors-managing-installed"></a>

The connectors table lists all your installed connectors. Each connector shows its name and description, its type (Cloud, Local, or System), its owner, and its status. You can manage your connectors in the following ways.


| Action | Description | 
| --- | --- | 
| Search | Find a connector by name. | 
| Filter | Narrow the list to Cloud, Local, or System connectors. Additional filters are available from the filter control next to the connector type filters. | 
| Sort | Order the list, for example by Recommended. | 
| Sign in | Complete the authentication flow for a connector that requires it before it can be used. | 
| Enable or disable | Turn an individual connector on or off with its status toggle, without removing it. | 
| Create | Add a new connector, such as a cloud connector, a local connector, or a coding agent, using the Create button. | 
| Browse all | Open the Add to Quick catalog to discover and install more connectors. | 

Each connector also has an actions menu with options that depend on its type. For all connectors, you can manage tool permissions and enable or disable the connector.


| Connector type | Actions menu options | 
| --- | --- | 
| Cloud connectors | Try it (see example prompts in chat), About connector (view connector details), Sign out, and Uninstall. | 
| Local connectors | Try it, Edit, and Delete. | 
| System tools | Try it. | 

Some connectors are shared with you by your organization. A connector's owner shows whether you own it or it was shared with you. For a connector that supports more than one workspace, such as Slack, choose **Set preferred workspace** to pick which workspace Quick uses.

## Managing tool permissions
<a name="connectors-tool-permissions"></a>

Connectors provide tools that agents can use on your behalf. Because a tool can make changes in an external application, AWS Quick can pause for a consent step before a tool runs, which keeps a human in the loop on the changes an agent makes. Whether this consent step is needed is controlled with tool permissions, which are set at two levels: a connector owner level and a user preference level.

Connector owners, usually the application admins who share connectors with users, control one level of settings, and those settings are enforced for everyone who uses the connector. At the owner level, each tool can be set to one of three options.


| Owner setting | Description | 
| --- | --- | 
| Let users choose | Hands the decision to each user, who then chooses how the tool behaves for them. This is the default. | 
| Always ask | The tool always pauses for a consent step before it runs, for every user. | 
| Disabled | The tool is turned off and is not available to users. | 

When a tool is set to **Let users choose** at the connector level, each user can set their own preference for the tools they use. The following options are available at the user level.


| User setting | Description | 
| --- | --- | 
| Always allow | The tool runs without a consent step. | 
| Ask each time | The tool pauses for a consent step each time it runs. | 
| Always deny | The tool is turned off for you and does not run. | 

By default, tools are set to **Let users choose** at the connector level. The user-level default then depends on whether the tool performs a write task or a read task.


| Task type | Connector-level default | User-level default | 
| --- | --- | --- | 
| Write tasks | Let users choose | Ask each time (can be changed by the user) | 
| Read tasks | Let users choose | Always allow (can be changed by the user) | 

For tools from an MCP server, Quick treats a tool as a read task only when the server marks it as read-only with the `readOnlyHint` annotation. Quick treats every other MCP tool as a write task.

New tools that are discovered during an MCP sync are disabled by default, so a connector owner can review them before making them available.

## MCP servers
<a name="connectors-mcp-servers"></a>

AWS Quick supports the Model Context Protocol (MCP), an open standard that extends Quick with custom tools and integrations. When you connect an MCP server, its tools become available in your chat conversations and scheduled runs, for example a server that provides database query tools.

An MCP server that you add on your own machine is a local connector that belongs to you, which is a capability of the AWS Quick desktop application. The desktop application stores its configuration on your computer, and only you can use it. To share an MCP server across the web, mobile, and desktop applications, its owner sets it up as a cloud connector instead. For more information, see [Model Context Protocol (MCP) integration](mcp-integration.md). A cloud connector runs from your AWS Quick account, supports OAuth with Dynamic Client Registration (DCR), and stores its tokens in the account's token vault.

How a local MCP server communicates depends on where the server runs. A server that runs as a command on your computer communicates over standard input and output (stdio). A server at a URL communicates over Streamable HTTP, and Quick falls back to HTTP with server-sent events (SSE) when the server doesn't support Streamable HTTP. Local connectors don't support OAuth or DCR, because the desktop application doesn't store or renew tokens for them. To authenticate to a URL server, add a header, such as an API key, and store its value as a secret.

To add a local MCP server in the desktop application, choose **Create**, and then choose **Local connector**. A dialog offers three connection types. You can also paste a standard MCP server JSON configuration to populate the form.

**Local**  
Run an MCP server as a command on your machine, which is the most common option for development tools and locally installed servers.


| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | A friendly name, for example "My Database MCP". | 
| Command | Yes | The executable to run. Common values are python, npx, node, and uvx. | 
| Arguments | No | Command-line arguments, separated by spaces, for example -m mcp\_server --port 8080. | 
| Description | No | What the server does and what tools it provides, so Quick knows when to use it. | 
| Environment variables | No | Key-value pairs that the server requires. | 
| Startup timeout | No | Seconds to wait for the server to start, from 5 to 300 (default 30). | 

In the **Command** and **Arguments** fields, you can start a path with `~` for your home folder. If **Command** is a program name instead of a full path, Quick finds it on your PATH. On macOS, Quick uses the PATH from your login shell.

**Import**  
Load MCP server definitions from an existing configuration file, so you can reuse configurations from other tools. Quick supports configuration files from Kiro, Claude Code, AIM, Antigravity, and QuickWork exports. Enter the configuration file path, for example `~/.kiro/settings/mcp.json`. Quick scans the file and detects the servers defined in it, and it also detects compatible tools installed on your system, showing them as chips under **Detected on this system**. Choose **Load file** to import the servers.

An MCP server receives only an allowed set of system environment variables from your computer, such as PATH and your proxy and certificate settings. If a server needs another value, such as an API token, add it to the server's **Environment variables** field and mark it as a secret.

**Remote**  
Connect to an MCP server over HTTP, for shared team servers or hosted services.


| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | A friendly name. | 
| URL | Yes | The MCP endpoint URL. It must start with http:// or https://. | 
| Headers | No | HTTP request headers as key-value rows, for example an Authorization header. A header value can be stored as a secret in your operating system keychain. | 
| Description | No | What the server does and what tools it provides. | 
| Startup timeout | No | Seconds to wait for the server, from 5 to 300 (default 30). | 

After you add servers, they appear in the MCP servers section, where you can search, filter by status, toggle individual servers on or off, edit, and remove them. You can attach MCP servers to a schedule so that automated runs use their tools.

## Coding agents
<a name="connectors-coding-agents"></a>

Coding agents are external AI coding tools that AWS Quick delegates development tasks to, using the Agent Client Protocol (ACP). Coding agents are a capability of the AWS Quick desktop application. When a coding agent is enabled, you ask Quick to send work to it, for example "refactor this module," and Quick reports the results back.

**To add a coding agent in the desktop application**

1. Choose **Customize**, and then choose the **Connectors** tab.

1. Choose **Create**, and then choose **Coding agent**.

1. Configure the agent, and then save your changes.

You add a coding agent from a preset, which is a one-click add for a supported agent that you edit afterward, or with a custom configuration. A custom agent is configured with a name, the launch command and arguments, an optional description, and optional advanced settings.
+ **Environment variables** are values that the agent needs at launch.
+ **Override path** sets where the agent runs. When it is empty, the agent runs in the current conversation's workspace. An absolute path supports mounted, external-volume, or remote setups.
+ **MCP server forwarding** sets which MCP servers are forwarded to the agent: None (the default), All enabled, or specific servers that you choose.

For Kiro, you can set each tool to **Off**, **Ask**, or **Auto**, or choose a preset of **Read-only**, **Supervised**, or **Trust all**. Under **Allowed paths**, you list folders where Kiro can edit files without asking. You can also choose Kiro's model and test the connection before you save. Claude Code doesn't support ACP permission enforcement, so it runs with full access.

Add only coding agents that your organization approves. You are responsible for the security and data-handling compliance of any coding agent that you register.