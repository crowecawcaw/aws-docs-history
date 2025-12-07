# Policy scope

The scope defines what the policy applies to. Every Cedar policy specifies three
components:

###### Topics

- [Entities and namespaces](#policy-entities-namespaces "#policy-entities-namespaces")
- [Principal](#policy-principal "#policy-principal")
- [Action](#policy-action "#policy-action")
- [Resource](#policy-resource "#policy-resource")

```

permit(
  principal is AgentCore::OAuthUser,    // WHO is making the request
  action == AgentCore::Action::"...",   // WHAT they want to do
  resource is AgentCore::Gateway::"..." // WHICH resource they want to access
)

```

## Entities and namespaces

Cedar uses entities to represent principals, actions, and resources. All entities in
AgentCore Gateway use the AgentCore namespace.

Entity format: `Namespace::EntityType::"identifier"`

## Principal

The principal identifies the entity making the authorization request:

```

principal is AgentCore::OAuthUser

```

Components:

- `principal` - The entity making the authorization request
- `AgentCore::OAuthUser` - Entity type representing authenticated users
- `is` - Type check operator (matches any OAuthUser entity)

Principals are OAuth-authenticated users. Each user has a unique ID from the JWT sub
claim.

## Action

The action specifies the operation being requested:

```

action == AgentCore::Action::"RefundTool__process_refund"

```

Components:

- `action` - The operation being requested
- `AgentCore::Action::"RefundTool__process_refund"` - Specific action
  entity
- `==` - Exact match operator (only this specific action)

Actions represent tool calls in the MCP AgentCore Gateway. Each tool has a corresponding action
entity.

## Resource

The resource identifies the target of the request:

```

resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/refund-gateway"

```

Components:

- `resource` - The target of the request
- `AgentCore::Gateway` - Entity type representing gateway instances
- `==` - Exact match operator (matches this specific AgentCore Gateway)

The AgentCore Gateway is the MCP server that routes tool calls.

### Resource specificity requirements

When specifying one or more specific actions, you must use specific AgentCore Gateway ARNs:

```

// Required: Specific Gateway ARN for specific action(s)
resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/refund-gateway"

```

This applies to:

- Single action: `action == AgentCore::Action::"ToolName"`
- Multiple specific actions: `action in [AgentCore::Action::"Tool1",
AgentCore::Action::"Tool2"]`

Use type checks only when matching any action:

```

// For policies covering any action (not specific tools)
resource is AgentCore::Gateway

```

Examples:

```

// Blocks all actions
forbid(principal, action, resource);

// Allow any CallTool action
permit(principal, action in AgentCore::Action::"CallTool", resource is AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/refund-gateway");

```

Specific AgentCore Gateway ARNs provide:

- Security isolation between AgentCore Gateway instances
- Separation of production and development environments
- Fine-grained access control per AgentCore Gateway
