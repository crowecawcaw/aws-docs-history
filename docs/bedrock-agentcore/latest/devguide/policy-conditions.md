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

## Principal attributes

Principal attributes differ based on the authentication type configured for your
AgentCore Gateway.

### OAuth claims (tags)

For OAuth-authenticated gateways, JWT claims from the OAuth token are stored as tags on
the OAuthUser entity. Example JWT claims:

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

### IAM entity attributes

For IAM-authenticated gateways, the principal has an `id` attribute containing
the caller's IAM ARN. IAM principals do not support tags.

The `principal.id` attribute contains the full IAM ARN in one of these
formats:

- **IAM user:**
  `arn:aws:iam::123456789012:user/username`
- **IAM role (assumed):**
  `arn:aws:sts::123456789012:assumed-role/role-name/session-name`
- **IAM role:**
  `arn:aws:iam::123456789012:role/role-name`

Use the `like` operator with wildcards to match patterns in the IAM ARN:

```

// Match specific AWS account
principal.id like "*:123456789012:*"

// Match specific IAM role
principal.id like "arn:aws:iam::*:role/AdminRole"

// Match any role in a specific account
principal.id like "arn:aws:iam::123456789012:role/*"

// Match assumed role sessions
principal.id like "arn:aws:sts::*:assumed-role/ServiceRole/*"

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
