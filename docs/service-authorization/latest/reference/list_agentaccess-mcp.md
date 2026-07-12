# Actions, resources, and condition keys for Amazon WorkSpaces AgentAccess MCP Server

Amazon WorkSpaces AgentAccess MCP Server (service prefix: `agentaccess-mcp`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../appstream2/latest/developerguide/what-is-appstream.md "../../../appstream2/latest/developerguide/what-is-appstream.md").
- View a list of the [API operations available for
  this service](../../../appstream2/latest/developerguide/agent-access.md "../../../appstream2/latest/developerguide/agent-access.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../appstream2/latest/developerguide/agent-access.md "../../../appstream2/latest/developerguide/agent-access.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/agentaccess-mcp/agentaccess-mcp.json "https://servicereference.us-east-1.amazonaws.com/v1/agentaccess-mcp/agentaccess-mcp.json") for this service.

###### Topics

- [Actions defined by Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-actions-as-permissions "#list_agentaccess-mcp-actions-as-permissions")
- [Resource types defined by Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-resources-for-iam-policies "#list_agentaccess-mcp-resources-for-iam-policies")
- [Condition keys for Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-policy-keys "#list_agentaccess-mcp-policy-keys")

## Actions defined by Amazon WorkSpaces AgentAccess MCP Server

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                              | Description                                                             | Resource types (\*required) | Condition keys                                                                                                              | Access level |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [CallForwardedTool](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")     | Grants permission to invoke a forwarded tool on a remote instance       |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [CheckConnectionStatus](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md") | Grants permission to check the connection status of a streaming session |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Read         |
| [DoubleClick](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")           | Grants permission to perform double click at coordinates                |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [GetScreenshot](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")         | Grants permission to capture screen state                               |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Read         |
| [HoldKey](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")               | Grants permission to hold key down                                      |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [InvokeMcp](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")             | Grants permission to initialize sessions and discover tools             |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [KeyPress](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")              | Grants permission to press key or key combination                       |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [LeftClick](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")             | Grants permission to perform left mouse click at coordinates            |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [LeftClickDrag](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")         | Grants permission to click and drag between coordinates                 |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [LeftMouseDown](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")         | Grants permission to press and hold left mouse button                   |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [LeftMouseUp](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")           | Grants permission to release left mouse button                          |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [MiddleClick](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")           | Grants permission to perform middle mouse click at coordinates          |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [MovePointer](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")           | Grants permission to move cursor to coordinates                         |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [RightClick](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")            | Grants permission to perform right mouse click at coordinates           |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [Scroll](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")                | Grants permission to scroll in any direction                            |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [TripleClick](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")           | Grants permission to perform triple click at coordinates                |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |
| [TypeText](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md")              | Grants permission to type text string                                   |                             | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn "#list_agentaccess-mcp-agentaccess-mcp_StackArn") | Write        |

## Resource types defined by Amazon WorkSpaces AgentAccess MCP Server

Amazon WorkSpaces AgentAccess MCP Server does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon WorkSpaces AgentAccess MCP Server

Amazon WorkSpaces AgentAccess MCP Server defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                          | Description                                                    | Type |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---- |
| [agentaccess-mcp:StackArn](../../../appstream2/latest/developerguide.md "../../../appstream2/latest/developerguide.md") | Filters access by the ARN of the WorkSpaces Applications stack | ARN  |
