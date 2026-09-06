

# Actions, resources, and condition keys for Amazon WorkSpaces AgentAccess MCP Server
<a name="list_agentaccess-mcp"></a>

Amazon WorkSpaces AgentAccess MCP Server (service prefix: `agentaccess-mcp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appstream2/latest/developerguide/agent-access.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appstream2/latest/developerguide/agent-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/agentaccess-mcp/agentaccess-mcp.json) for this service.

**Topics**
+ [Actions defined by Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-actions-as-permissions)
+ [Resource types defined by Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-resources-for-iam-policies)
+ [Condition keys for Amazon WorkSpaces AgentAccess MCP Server](#list_agentaccess-mcp-policy-keys)

## Actions defined by Amazon WorkSpaces AgentAccess MCP Server
<a name="list_agentaccess-mcp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CallForwardedTool](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to invoke a forwarded tool on a remote instance |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [CheckConnectionStatus](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to check the connection status of a streaming session |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Read | 
|   [DoubleClick](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to perform double click at coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [GetScreenshot](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to capture screen state |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Read | 
|   [HoldKey](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to hold key down |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [InvokeMcp](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to initialize sessions and discover tools |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [KeyPress](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to press key or key combination |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [LeftClick](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to perform left mouse click at coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [LeftClickDrag](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to click and drag between coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [LeftMouseDown](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to press and hold left mouse button |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [LeftMouseUp](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to release left mouse button |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [MiddleClick](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to perform middle mouse click at coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [MovePointer](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to move cursor to coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [RightClick](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to perform right mouse click at coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [Scroll](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to scroll in any direction |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [TripleClick](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to perform triple click at coordinates |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 
|   [TypeText](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Grants permission to type text string |  | [agentaccess-mcp:StackArn](#list_agentaccess-mcp-agentaccess-mcp_StackArn) | Write | 

## Resource types defined by Amazon WorkSpaces AgentAccess MCP Server
<a name="list_agentaccess-mcp-resources-for-iam-policies"></a>

Amazon WorkSpaces AgentAccess MCP Server does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon WorkSpaces AgentAccess MCP Server
<a name="list_agentaccess-mcp-policy-keys"></a>

Amazon WorkSpaces AgentAccess MCP Server defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [agentaccess-mcp:StackArn](https://docs.aws.amazon.com/appstream2/latest/developerguide/)  | Filters access by the ARN of the WorkSpaces Applications stack | ARN | 