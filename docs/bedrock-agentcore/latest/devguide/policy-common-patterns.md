# Common policy patterns

These examples demonstrate frequently used Cedar policy patterns. The patterns work with
both OAuth and IAM authentication—select the appropriate principal type for your AgentCore Gateway
configuration. For details on principal attributes, see
[Principal attributes](policy-conditions.md#policy-principal-attributes "policy-conditions.md#policy-principal-attributes").

These patterns apply regardless of authentication type.

## Emergency shutdown

Disable all tool calls across the entire Gateway:

```
forbid(
  principal,
  action,
  resource
);
```

**Use case:** Emergency shutdown, maintenance mode, or
incident response.

**Effect:** Overrides all permit policies due to forbid-wins
semantics.

## Disable specific tool

Disable a specific tool while keeping others operational:

```
forbid(
  principal,
  action == AgentCore::Action::"RefundTool__process_refund",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/refund-gateway"
);
```

**Use case:** Temporarily disable a problematic tool without
affecting other functionality.

## Block user access

Prevent specific users or accounts from performing any actions:

### OAuth: Block specific user

Block a user by matching their username tag:

```
forbid(
  principal is AgentCore::OAuthUser,
  action,
  resource
)
when {
  principal.hasTag("username") &&
  principal.getTag("username") == "suspended-user"
};
```

**Use case:** Immediately revoke access for a compromised or
suspended user account.

### IAM: Block specific account

Block callers from a specific AWS account:

```
forbid(
  principal is AgentCore::IamEntity,
  action,
  resource
)
when {
  principal.id like "*:444455556666:*"
};
```

**Use case:** Block test or unauthorized accounts from
accessing production tools.

## Role-based access control

Restrict access based on roles. OAuth uses role tags; IAM uses role ARN patterns.

### OAuth: Using role tags

Permit access only to users with specific roles:

```
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"AdminAPI__delete_resource",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/admin"
)
when {
  principal.hasTag("role") &&
  (principal.getTag("role") == "admin" || principal.getTag("role") == "manager")
};
```

**Use case:** Allow administrative operations only for users
with admin or manager roles.

### IAM: Using IAM role ARNs

Permit access only to callers using specific IAM roles:

```
permit(
  principal is AgentCore::IamEntity,
  action == AgentCore::Action::"AdminAPI__delete_resource",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/admin"
)
when {
  principal.id like "arn:aws:iam::*:role/AdminRole"
};
```

**Use case:** Allow administrative operations only for
callers using the AdminRole IAM role.

**Variations:**

```
// Match assumed role sessions
principal.id like "arn:aws:sts::*:assumed-role/AdminRole/*"

// Match any role in a specific account
principal.id like "arn:aws:iam::123456789012:role/*"
```

## Data type operations

Cedar supports various data types in conditions. These examples use OAuth principals
(`AgentCore::OAuthUser`). For IAM-authenticated gateways, use
`AgentCore::IamEntity` instead - the input validation logic remains identical.

### Integers (Long)

```
// Check if passenger count is exactly 2
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"TravelAPI__search_flights",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/travel"
)
when {
  context.input.passengers == 2
};
```

### Strings

```
// Check if payment method is credit card
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"PaymentAPI__process_payment",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/payment"
)
when {
  context.input.paymentMethod == "credit-card"
};
```

### Lists (Sets)

```
// Check if country is in allowed list
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"ShippingAPI__calculate_rate",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/shipping"
)
when {
  ["US", "CA", "MX"].contains(context.input.country)
};
```

### Checking for Optional Fields

```
// Require optional field to be present
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"OrderAPI__create_order",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/order"
)
when {
  context.input has shippingAddress
};
```
