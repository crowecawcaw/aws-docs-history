

# Connectors
<a name="connections-desktop"></a>

Connectors bring cloud connectors, system tools, local connectors, and coding agents together in one place, with a catalog to discover and add new ones. A connector links Amazon Quick to an external application or a native tool so agents can access data and act on your behalf. You manage them from Customize, on the Connectors tab, which supports four capabilities.
+ Cloud connectors connect Quick to external services such as Outlook, SharePoint, OneDrive, Slack, Jira, Asana, Airtable, and Salesforce, as well as remotely hosted Model Context Protocol (MCP) servers. Once connected, they are reachable from any Quick device, including desktop, mobile, and web.
+ System tools are the capabilities Quick provides out of the box, such as image generation, browser automation, and research. You do not install or sign in to them, but you can turn them on or off. Some run in the cloud; others, such as browser automation, are device specific. For the full list, see [System tools](system-tools-desktop.md).
+ Local connectors run on your own machine, covering local MCP servers you host yourself. Their tools are available only when that machine is on and connected.
+ Coding agents such as Kiro and Claude Code can be connected so you can delegate development work to them from chat. See the Coding agents section.

## Discovering and adding connectors
<a name="desktop-discovering-adding-connectors"></a>

On the Connectors tab, you can discover and add connectors that expand what Amazon Quick can do for you. To see the full catalog, choose **Browse all**. Each connector card shows its name and a short description of what it does.

**Adding a cloud connector**  
Cloud connectors in the catalog are either connectors that have been shared with you or connectors that you can set up with a single click of Install followed by a sign-in. The Suggested for you area contains cloud connectors that have already been set up and shared with you, along with the most popular cloud connectors for Quick users. When you install one of these connectors, by default Amazon Quick connects to the external service using an Amazon-hosted OAuth application for that service. OAuth applications are the standard way an application, such as Quick, makes calls to an external application, such as Outlook or Salesforce, on your behalf. An end-user sign-in is also required.

Some enterprises prefer to use their own OAuth application rather than the Amazon default. To do this, choose Create and then choose Cloud Connector. This Create option gives additional enterprise admin controls during setup, such as setting a connector's name, description, who it is shared with, and its tool permissions. Connectors that do not have an Amazon default OAuth application are also found in the Create section. Creating a custom connection to a remotely hosted MCP server also uses Create and then Cloud Connector.

Connectors you add appear automatically in the connectors table in the lower half of the Connectors tab.

**Adding a local connector**  
Beyond the connectors in the catalog, you can add a local connector that runs on your own machine, such as a local MCP server. A local connector lets Amazon Quick use tools you host yourself, such as a database, an internal API, or a developer tool, so those tools become available to agents in chat and in scheduled tasks. To add one, choose Create and then choose Create local connector. Because a local connector runs on your machine, its tools are available only when that machine is on and connected. For the MCP server fields, see the MCP servers section.

**Adding a coding agent**  
You can also connect a coding agent, an external AI coding tool such as Kiro or Claude Code, that Amazon Quick can hand development work to. Once a coding agent is connected and enabled, you can delegate tasks to it from chat, and it does the work and reports back. To add one, choose Create and then choose Coding agent. See the Coding agents section.

## Managing your installed connectors
<a name="desktop-managing-installed-connectors"></a>

The Connectors tab has a table of all your installed connectors. Each connector shows its name and description, its Type (Cloud, Local, or System), its Owner, and its Status. To manage your connectors, you can do the following.


| Action | Description | 
| --- | --- | 
| Search | Find a connector by name. | 
| Filter | Narrow the list to Cloud, Local, or System connectors. Additional filters are available from the filter control next to the connector type filters. | 
| Sort | Order the list, for example by Recommended. | 
| Sign in | Complete the authentication flow for a connector that requires it before it can be used. | 
| Enable or disable | Turn an individual connector on or off with its status toggle, without removing it. | 
| Create | Add a new connector (an MCP server or a coding agent) using the Create button. | 
| Browse all | Open Add to Quick to discover and install more connectors. | 

Each connector also has an actions menu with options that depend on its type. For all connectors, you can manage tool permissions (see the next section) and enable or disable the connector.


| Connector type | Actions menu options | 
| --- | --- | 
| Cloud connectors | Try it (see example prompts in chat), About connector (view connector details), Sign out, and Uninstall. | 
| Local connectors | Try it, Edit, and Delete. | 
| System tools | Try it. | 

Some connectors are shared with you by your organization. A connector's Owner column shows whether you own it or it was shared with you. For a connector that supports more than one workspace, for example Slack, choose Set preferred workspace to pick which workspace Quick uses.

## Managing tool permissions
<a name="desktop-managing-tool-permissions"></a>

Connectors provide tools that agents can use on your behalf. Because a tool can make changes in an external application, Amazon Quick can pause for a consent step before a tool runs, keeping a human in the loop on the changes an agent makes. Whether this consent step is needed is controlled with tool permissions, which are set at two levels: a connector owner level and a user preference level.

Connector owners, usually the application admins who share connectors with users, control one level of settings, and those settings are enforced for everyone who uses the connector. At the owner level, each tool can be set to one of three options.


| Owner setting | Description | 
| --- | --- | 
| Let Users Choose | Hands the decision to each user, who then chooses how the tool behaves for them. This is the default. | 
| Always Ask | The tool always pauses for a consent step before it runs, for every user. | 
| Disable | The tool is turned off and is not available to users. | 

When a tool is set to Let Users Choose at the connector level, each user can set their own preference for the tools they use. The following options are available at the user level.


| User setting | Description | 
| --- | --- | 
| Always Allow | The tool runs without a consent step. | 
| Ask Each Time | The tool pauses for a consent step each time it runs. | 
| Disable | The tool is turned off for you and does not run. | 

By default, tools are set to Let Users Choose at the connector level. The user-level default then depends on whether the tool performs a write task or a read task.


| Task type | Connector-level default | User-level default | 
| --- | --- | --- | 
| Write tasks | Let Users Choose | Ask Each Time (can be changed by the user) | 
| Read tasks | Let Users Choose | Always Allow (can be changed by the user) | 

New tools discovered during an MCP sync are disabled by default, so a connector owner can review them before making them available.

## MCP servers
<a name="desktop-mcp-servers"></a>

Amazon Quick supports the Model Context Protocol (MCP), an open standard that extends Quick with custom tools and integrations. When you connect an MCP server, its tools become available in your chat conversations and scheduled runs, for example a server that provides database query tools.

To add one, choose Create and then MCP server. A dialog offers three connection types. You can also paste a standard MCP server JSON configuration to populate the form.

**Local**  
Run an MCP server as a command on your machine, the most common option for development tools and locally installed servers.


| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | A friendly name, for example "My Database MCP". | 
| Command | Yes | The executable to run. Common values: python, npx, node, uvx. | 
| Arguments | No | Command-line arguments, space-separated, for example -m mcp\_server --port 8080. | 
| Description | No | What the server does and what tools it provides, so Quick knows when to use it. | 
| Environment variables | No | Key-value pairs the server requires. | 
| Startup timeout | No | Seconds to wait for the server to start, 5 to 300 (default 30). | 

**Import**  
Load MCP server definitions from an existing configuration file, so you reuse configurations from other tools. Quick supports configuration files from Kiro, Claude Code, AIM, Antigravity, and QuickWork exports. Enter the configuration file path (for example, `~/.kiro/settings/mcp.json`). Quick scans the file and detects the servers defined in it, and also detects compatible tools installed on your system, showing them as chips under "Detected on this system". Choose Load file to import the servers.

**Remote**  
Connect to an MCP server over HTTP, for shared team servers or hosted services.


| Field | Required | Description | 
| --- | --- | --- | 
| Name | Yes | A friendly name. | 
| URL | Yes | The MCP endpoint URL. Must start with http:// or https://. | 
| Headers | No | HTTP request headers as key-value rows, for example an Authorization header. A header value can be stored as a secret in your operating system keychain. | 
| Description | No | What the server does and what tools it provides. | 
| Startup timeout | No | Seconds to wait for the server, 5 to 300 (default 30). | 

After you add servers, they appear in the MCP servers section, where you search, filter by status, toggle individual servers on or off, edit, and remove them. You can attach MCP servers to a schedule so automated runs use their tools.

## Coding agents
<a name="desktop-coding-agents"></a>

Coding agents are external AI coding tools that Amazon Quick delegates development tasks to, using the Agent Client Protocol (ACP). When enabled, you ask Quick to send work to a coding agent, for example "refactor this module," and Quick reports the results back.

**To add a coding agent**

1. Choose Customize, and then choose the Connectors tab.

1. Choose Create, and then choose Coding agent.

1. Configure the agent, and then save.

You add a coding agent from a preset (a one-click add for a supported agent, which you edit afterward) or with a custom configuration. A custom agent is configured with a Name, the launch Command and Arguments, an optional Description, and optional advanced settings.
+ Environment variables: values the agent needs at launch.
+ Override path: where the agent runs. When empty, the agent runs in the current conversation's workspace. An absolute path supports mounted, external-volume, or remote setups.
+ MCP server forwarding: which MCP servers are forwarded to the agent: None (the default), All enabled, or Choose specific servers.

For a supported preset agent, additional configuration is available: tool permissions with three states per tool (Off, Ask for Permission, or Auto-approve), write-path scoping, and model selection. You can test the connection before saving.

Add only coding agents your organization approves. You are responsible for the security and data-handling compliance of any coding agent you register.