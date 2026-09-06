

# MCP configuration for Q Developer in the IDE
<a name="mcp-ide"></a>

This page covers IDE-specific options for configuring MCP servers. 

## Understanding MCP configuration files for Q Developer in the IDE
<a name="mcp-ide-configuration-understanding"></a>

When you use the GUI to add an MCP server to Q Developer in the IDE, the configuration is stored in one of two files:
+ At the global scope: \~/.aws/amazonq/default.json
+ At the local scope: .amazonq/default.json

However, for legacy reasons, it is also possible to put MCP configuration information in two other locations: 
+ At the global scope: \~/.aws/amazonq/mcp.json
+ At the local scope: .amazonq/mcp.json

Q Developer gives precedence to workspace level configurations for MCP servers, their permissions, and the settings stored.

**Note**  
If you have already set up an MCP configuration in an mcp.json file, and you are using the MCP configuration GUI for the first time, you will see that configuration in the GUI. 

Support for legacy mcp.json files is enabled by the useLegacyMcpJson field in your global default.json config file. By default, this field is set to true. For more information, see [UseLegacyMcpJson Field](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#uselegacymcpjson-field) in the Q Developer CLI GitHub repo.

Note that the mcp.json files may also be used by the Q CLI.

For information about how to set granular controls on MCP tooling, see the [Built-in tools reference](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#tools-field).

## Accessing the MCP configuration UI
<a name="mcp-ide-configuration-access-ui"></a>

To access the MCP configuration UI in Q Developer in the IDE:

1. Open your IDE (VS Code, JetBrains, etc.).

1. Open the Q Developer panel.

1. Open the **Chat** panel.

1. Choose the tools icon. ![tools icon](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/tools-icon-full.png) 

## Adding an MCP server
<a name="mcp-ide-configuration-add-mcp-server"></a>

There are two primary transport mechanisms for communication between AI clients and MCP servers: STDIO and HTTP.

### Adding an HTTP MCP server
<a name="mcp-ide-configuration-add-http-server"></a>

To add an HTTP MCP server to the IDE:

1.  [Access the MCP configuration UI](#mcp-ide-configuration-access-ui). 

1. Choose the plus (\+) symbol.

1. Select the scope: global or local.

   If you select global scope, the MCP server configuration is stored in \~/.aws/amazonq/default.json and available across all your projects. If you select local scope, the configuration is stored in .amazonq/default.json within your current project.

1. In the **Name** field, enter the name of the MCP server.

1. Select `http` as the transport protocol.

1. In the **URL** field, enter the URL that the MCP server will call when it initializes.

1. Under **Headers - optional**, you can enter key-value pairs that must be sent as HTTP request headers. .

1. Enter a **Timeout** value, as applicable.

1. Choose **Save**. 

   The configuration panel will be replaced with the tool permissions panel.

1. Follow the procedure under [Reviewing and adjusting tool permissions](#mcp-ide-configuration-review-adjust-tool) .

**Note**  
If the MCP HTTP endpoint requires authorization, then Amazon Q will automatically open a browser page so that you can authorize Amazon Q to access the MCP server.

### Adding an STDIO MCP server
<a name="mcp-ide-configuration-add-stdio-server"></a>

To add an STDIO MCP server to the IDE:

1.  [Access the MCP configuration UI](#mcp-ide-configuration-access-ui). 

1. Choose the plus (\+) symbol.

1. Select the scope: global or local.

   If you select global scope, the MCP server configuration is stored in \~/.aws/amazonq/default.json and available across all your projects. If you select local scope, the configuration is stored in .amazonq/default.json within your current project.

1. In the **Name** field, enter the name of the MCP server.

   For example, if we were installing the [AWS Documentation MCP server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/), the name might be {{AWSDocMCPServer}}. 

1. Select `stdio` as the transport protocol.

1. In the **Command** field, enter the shell command that the MCP server will run when it initializes.

   In the case of the AWS Documentation MCP Server, the command is `uvx`. This is an alias for `uv tool run`, which creates an ephemeral Python environment.

1. In the **Arguments** field, enter an argument to be given to the shell command, if applicable.

   In the case of the AWS Documentation MCP Server, the argument is {{awslabs.aws-documentation-mcp-server@latest}}. This is a Python package identifier that points to a package hosted on PyPI (Python Package Index).

   Add more arguments as necessary.

1. Fill in environment variables as applicable.

   In the case of our example, we first fill in Name: {{FASTMCP\_LOG\_LEVEL}} and Value: {{ERROR}}. 

   We will also use the name {{AWS\_DOCUMENTATION\_PARTITION}} and the value {{aws}} to indicate the [partition](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) that we'll be working with.

1. Enter a **Timeout** value, as applicable.

   For our example, we'll keep the recommended value of 60 (seconds).

1. Choose **Save**. 

   The configuration panel will be replaced with the tool permissions panel.

1. Follow the procedure under [Reviewing and adjusting tool permissions](#mcp-ide-configuration-review-adjust-tool) .

## Troubleshooting your MCP configuration
<a name="mcp-ide-configuration-troubleshooting"></a>

After you add an MCP server in the IDE, Amazon Q will attempt to connect to it.

If there are connection issues, then an alert appears in the panel. You should not expect the tools from that MCP server to function properly until the alert is resolved.

Choose **Fix Configuration** to return to the MCP configuration screen so that you can make the appropriate changes.

## Enabling an MCP server
<a name="mcp-ide-configuration-disable-server"></a>

The following procedure assumes that the MCP server in question is not already enabled.

To enable an MCP server in the IDE:

1. Open the MCP Servers panel.

1. Next to the server that you want to enable, choose **Enable**. 

## Disabling an MCP server
<a name="mcp-ide-configuration-disable-server"></a>

To disable an MCP server in the IDE:

1. Open the MCP Servers panel.

1. Choose the server you want to disable.

1. Choose the three dots next to **Edit setup**. 

1. Choose **Disable MCP Server**. 

## Deleting an MCP server that is currently enabled
<a name="mcp-ide-configuration-delete-enabled-server"></a>

To delete an MCP server that is currently enabled from the IDE:

1. Open the MCP Servers panel.

1. Choose the server you want to delete.

   A panel will open with details about that server.

1. Choose the three dots next to **Edit setup**. 

1. Choose **Delete MCP server**. 

1. Confirm the deletion when prompted.

## Deleting an MCP server that is currently disabled
<a name="mcp-ide-configuration-delete-disabled-server"></a>

To delete an MCP server that is currently disabled from the IDE:

1. Open the MCP Servers panel.

1. Next to the server that you want to delete, choose **Delete**. 

1. Confirm the deletion when prompted.

## Reviewing and adjusting tool permissions
<a name="mcp-ide-configuration-review-adjust-tool"></a>

To review and adjusting tool permissions:

1. Open the MCP Servers panel.

1. Choose the MCP server for which you want to review and adjust permissions.

1. For each tool, you can set one of the following permission levels:
   + Ask: Prompt for permission each time the tool is used.
   + Always allow: Allow the tool to run without prompting.
   + Deny: Do not use this tool.