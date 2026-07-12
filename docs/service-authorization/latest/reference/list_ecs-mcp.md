# Actions, resources, and condition keys for Amazon ECS MCP Service

Amazon ECS MCP Service (service prefix: `ecs-mcp`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md "../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md").
- View a list of the [API operations available for
  this service](../../../AmazonECS/latest/developerguide/ecs-mcp-tool-configurations.md "../../../AmazonECS/latest/developerguide/ecs-mcp-tool-configurations.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md "../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/ecs-mcp/ecs-mcp.json "https://servicereference.us-east-1.amazonaws.com/v1/ecs-mcp/ecs-mcp.json") for this service.

###### Topics

- [Actions defined by Amazon ECS MCP Service](#list_ecs-mcp-actions-as-permissions "#list_ecs-mcp-actions-as-permissions")
- [Resource types defined by Amazon ECS MCP Service](#list_ecs-mcp-resources-for-iam-policies "#list_ecs-mcp-resources-for-iam-policies")
- [Condition keys for Amazon ECS MCP Service](#list_ecs-mcp-policy-keys "#list_ecs-mcp-policy-keys")

## Actions defined by Amazon ECS MCP Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                          | Description                                              | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [InvokeReadOnlyTools](../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md "../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md") | Grants permission to call read-only tools in MCP service |                             |                | Read         |
| [UseMcp](../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md "../../../AmazonECS/latest/developerguide/ecs-mcp-getting-started.md")              | Grants permission to use MCP service                     |                             |                | Read         |

## Resource types defined by Amazon ECS MCP Service

Amazon ECS MCP Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon ECS MCP Service

Amazon ECS MCP Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
