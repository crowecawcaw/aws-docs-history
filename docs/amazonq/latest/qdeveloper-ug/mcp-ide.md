# MCP configuration for Q Developer in the IDE

This page covers IDE-specific options for configuring MCP servers.

## Understanding MCP configuration files for Q Developer in the IDE

When you use the GUI to add an MCP server to Q Developer in the IDE, the configuration is stored in one of two files:

- At the global scope: ~/.aws/amazonq/default.json
- At the local scope: .amazonq/default.json

However, for legacy reasons, it is also possible to put MCP configuration information in two other locations:

- At the global scope: ~/.aws/amazonq/mcp.json
- At the local scope: .amazonq/mcp.json

Q Developer gives precedence to workspace level configurations for MCP servers, their permissions, and the settings stored.

###### Note

If you have already set up an MCP configuration in an mcp.json file, and you are using the MCP configuration GUI for the first time, you will see that configuration in the GUI.

Support for legacy mcp.json files is enabled by the useLegacyMcpJson field in your global default.json config file. By default, this field is set to true. For more information, see [UseLegacyMcpJson Field](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#uselegacymcpjson-field "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#uselegacymcpjson-field") in the Q Developer CLI GitHub repo.

Note that the mcp.json files may also be used by the Q CLI.

For information about how to set granular controls on MCP tooling, see the [Built-in tools reference](https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#tools-field "https://github.com/aws/amazon-q-developer-cli/blob/main/docs/agent-format.md#tools-field").

## Accessing the MCP configuration UI

To access the MCP configuration UI in Q Developer in the IDE:

1. Open your IDE (VS Code, JetBrains, etc.).
2. Open the Q Developer panel.
3. Open the **Chat** panel.
4. Choose the tools icon.
   ![tools icon](images/tools-icon-full.png)

## Adding an MCP server

There are two primary transport mechanisms for communication between AI clients and MCP servers: STDIO and HTTP.

### Adding an HTTP MCP server

To add an HTTP MCP server to the IDE:

1. [Access the MCP configuration UI](#mcp-ide-configuration-access-ui "#mcp-ide-configuration-access-ui").
2. Choose the plus (+) symbol.
3. Select the scope: global or local.

If you select global scope, the MCP server configuration is stored in ~/.aws/amazonq/default.json and available across all your projects. If you select local scope, the configuration is stored in .amazonq/default.json within your current project. 4. In the **Name** field, enter the name of the MCP server. 5. Select `http` as the transport protocol. 6. In the **URL** field, enter the URL that the MCP server will call when it initializes. 7. Under **Headers - optional**, you can enter key-value pairs that must be sent as HTTP request headers.
. 8. Enter a **Timeout** value, as applicable. 9. Choose **Save**.

The configuration panel will be replaced with the tool permissions panel. 10. Follow the procedure under [Reviewing and adjusting tool permissions](#mcp-ide-configuration-review-adjust-tool "#mcp-ide-configuration-review-adjust-tool")
.

###### Note

If the MCP HTTP endpoint requires authorization, then Amazon Q will automatically open a browser page so that you can authorize Amazon Q to access the MCP server.

### Adding an STDIO MCP server

To add an STDIO MCP server to the IDE:

1. [Access the MCP configuration UI](#mcp-ide-configuration-access-ui "#mcp-ide-configuration-access-ui").
2. Choose the plus (+) symbol.
3. Select the scope: global or local.

If you select global scope, the MCP server configuration is stored in ~/.aws/amazonq/default.json and available across all your projects. If you select local scope, the configuration is stored in .amazonq/default.json within your current project. 4. In the **Name** field, enter the name of the MCP server.

For example, if we were installing the [AWS Documentation MCP server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/ "https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/"), the name might be `AWSDocMCPServer`. 5. Select `stdio` as the transport protocol. 6. In the **Command** field, enter the shell command that the MCP server will run when it initializes.

In the case of the AWS Documentation MCP Server, the command is `uvx`. This is an alias for `uv tool run`, which creates an ephemeral Python environment. 7. In the **Arguments** field, enter an argument to be given to the shell command, if applicable.

In the case of the AWS Documentation MCP Server, the argument is `awslabs.aws-documentation-mcp-server@latest`. This is a Python package identifier that points to a package hosted on PyPI (Python Package Index).

Add more arguments as necessary. 8. Fill in environment variables as applicable.

In the case of our example, we first fill in Name: `FASTMCP_LOG_LEVEL` and Value: `ERROR`.

We will also use the name `AWS_DOCUMENTATION_PARTITION` and the value `aws` to indicate the [partition](../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md") that we'll be working with. 9. Enter a **Timeout** value, as applicable.

For our example, we'll keep the recommended value of 60 (seconds). 10. Choose **Save**.

The configuration panel will be replaced with the tool permissions panel. 11. Follow the procedure under [Reviewing and adjusting tool permissions](#mcp-ide-configuration-review-adjust-tool "#mcp-ide-configuration-review-adjust-tool")
.

## Troubleshooting your MCP configuration

After you add an MCP server in the IDE, Amazon Q will attempt to connect to it.

If there are connection issues, then an alert will be displayed at the top of the panel. You should not expect the tools from that MCP server to function properly until the alert is resolved.

Choose **Fix Configuration** to return to the MCP configuration screen so that you can make the appropriate changes.

## Enabling an MCP server

The following procedure assumes that the MCP server in question is not already enabled.

To enable an MCP server in the IDE:

1. Open the MCP Servers panel.
2. Next to the server that you want to enable, choose **Enable**.

## Disabling an MCP server

To disable an MCP server in the IDE:

1. Open the MCP Servers panel.
2. Choose the server you want to disable.
3. Choose the three dots next to **Edit setup**.
4. Choose **Disable MCP Server**.

## Deleting an MCP server that is currently enabled

To delete an MCP server that is currently enabled from the IDE:

1. Open the MCP Servers panel.
2. Choose the server you want to delete.

A panel will open with details about that server. 3. Choose the three dots next to **Edit setup**. 4. Choose **Delete MCP server**. 5. Confirm the deletion when prompted.

## Deleting an MCP server that is currently disabled

To delete an MCP server that is currently disabled from the IDE:

1. Open the MCP Servers panel.
2. Next to the server that you want to delete, choose **Delete**.
3. Confirm the deletion when prompted.

## Reviewing and adjusting tool permissions

To review and adjusting tool permissions:

1. Open the MCP Servers panel.
2. Choose the MCP server for which you want to review and adjust permissions.
3. For each tool, you can set one of the following permission levels:
   - Ask: Prompt for permission each time the tool is used.
   - Always allow: Allow the tool to run without prompting.
   - Deny: Do not use this tool.
