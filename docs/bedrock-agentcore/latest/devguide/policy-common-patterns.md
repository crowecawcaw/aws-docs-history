# Common policy patterns

These examples demonstrate frequently used Cedar policy patterns for common authorization
scenarios in Amazon Bedrock AgentCore Gateway.

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

Prevent a specific user from performing any actions:

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

## Data type operations

Cedar supports various data types in conditions. Here are examples showing how to work with
them:

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
