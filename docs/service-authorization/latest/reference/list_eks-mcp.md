

# Actions, resources, and condition keys for Amazon EKS MCP Server
<a name="list_eks-mcp"></a>

Amazon EKS MCP Server (service prefix: `eks-mcp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/eks-mcp/eks-mcp.json) for this service.

**Topics**
+ [Actions defined by Amazon EKS MCP Server](#list_eks-mcp-actions-as-permissions)
+ [Resource types defined by Amazon EKS MCP Server](#list_eks-mcp-resources-for-iam-policies)
+ [Condition keys for Amazon EKS MCP Server](#list_eks-mcp-policy-keys)

## Actions defined by Amazon EKS MCP Server
<a name="list_eks-mcp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CallPrivilegedTool](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html)  | Grants permission to call privileged tools in MCP service |  |   | Write | 
|   [CallReadOnlyTool](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html)  | Grants permission to call read-only tools in MCP service |  |   | Read | 
|   [InvokeMcp](https://docs.aws.amazon.com/eks/latest/userguide/eks-mcp-tool-configurations.html)  | Grants permission to use MCP service |  |   | Read | 

## Resource types defined by Amazon EKS MCP Server
<a name="list_eks-mcp-resources-for-iam-policies"></a>

Amazon EKS MCP Server does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon EKS MCP Server
<a name="list_eks-mcp-policy-keys"></a>

Amazon EKS MCP Server has no service-specific condition keys that can be used in the `Condition` element of policy statements.