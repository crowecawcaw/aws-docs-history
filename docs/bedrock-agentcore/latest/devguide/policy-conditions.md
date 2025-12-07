# Policy conditions

Conditions add fine-grained logic to policies using `when` and
`unless` clauses:

```

when {
  principal.hasTag("username") &&
  principal.getTag("username") == "refund-agent" &&
  context.input.amount < 500
}

```

## Condition types

- `when { ... }` - Policy applies only if the condition is true
- `unless { ... }` - Policy applies only if the condition is false

## Tool arguments

`context.input` contains the arguments passed to the tool call:

```

context.input.amount < 500

```

When a user calls `RefundTool__process_refund` with arguments like:

```

{
  "orderId": "12345",
  "amount": 450,
  "reason": "Defective product"
}

```

The policy can access these values:

- `context.input.orderId` → "12345"
- `context.input.amount` → 450
- `context.input.reason` → "Defective product"

Policies can make decisions based on specific tool call parameters.

## OAuth claims

OAuth claims from the JWT token are stored as tags on the OAuthUser entity. Example JWT
claims:

```

{
  "sub": "user-123",
  "username": "refund-agent",
  "scope": "refund:write admin:read",
  "role": "admin"
}

```

These claims become tags on the principal entity. Check if a tag exists:

```

principal.hasTag("username")

```

Get a tag value:

```

principal.getTag("username") == "refund-agent"

```

Pattern matching:

```

principal.getTag("scope") like "*refund:write*"

```

## Logical operators

Combine multiple conditions using logical operators:

- `&&` - AND (all conditions must be true)
- `||` - OR (at least one condition must be true)
- `!` - NOT (negates a condition)

Example:

```

principal.hasTag("username") &&              // User must have username tag
principal.getTag("username") == "refund-agent" &&  // Username must be "refund-agent"
context.input.amount < 500                   // Amount must be less than $500

```
