# Fine-grained access control for Amazon Bedrock AgentCore Gateway

Amazon Bedrock AgentCore Gateway provides fine-grained access control capabilities that allow you to control which users and agents can access specific tools and resources. You can implement access control through gateway interceptors for custom logic, or use resource-based policies for standard AWS-style access control. For information about resource-based policies, see [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md "resource-based-policies.md").

## Using interceptors for access control

Gateway interceptors provide the most flexible way to implement fine-grained access control. REQUEST interceptors execute before the gateway makes a call to the target, allowing you to:

- Validate user permissions based on JWT claims or custom logic
- Control access to specific tools or MCP operations
- Implement role-based or attribute-based access control
- Filter or modify requests based on user context
- Return authorization errors for unauthorized requests

For detailed information on implementing and configuring interceptors, including examples of authorization logic, see [Using interceptors with Gateway](gateway-interceptors.md "gateway-interceptors.md").

## Access control levels

Fine-grained access control in Gateway can be implemented at multiple levels:

**Gateway-level access**

Controls which users or agents can connect to and authenticate with the gateway through OAuth authorization servers.

**Tool-level access**

Controls access to specific tools within a gateway using interceptor logic to validate permissions before tool execution.

**Operation-level access**

Controls access to specific MCP operations (such as `tools/list` or `tools/call`) using interceptors to validate operation permissions.

**Parameter-level access**

Controls access to specific parameters or data within operations using interceptors to filter or validate request parameters.

## Implementation approaches

You can implement fine-grained access control using:

**JWT claims validation**

Use interceptors to examine JWT claims such as user roles, departments, or custom attributes to make authorization decisions.

**External authorization services**

Configure interceptors to call external authorization services or databases to validate user permissions.

**Request context filtering**

Use interceptors to modify requests based on user context, such as adding user-specific filters or limiting data scope.

## Best practices

- **Principle of least privilege** - Grant users only the minimum access required to perform their tasks.
- **Use structured claims** - Leverage JWT claims to carry user context and authorization information to your interceptors.
- **Implement fail-safe defaults** - Design interceptors to deny access by default when authorization cannot be determined.
- **Log authorization decisions** - Ensure your interceptors log access decisions for auditing purposes.
