# Example policies

This section provides comprehensive examples of Cedar authorization policies for an
insurance management system. These examples demonstrate various Cedar language features and
authorization patterns that you can adapt for your own applications.

###### Topics

- [Available tools](#available-tools "#available-tools")
- [Authorization policies](#authorization-policies "#authorization-policies")
- [Understanding authorization semantics](#authorization-semantics "#authorization-semantics")
- [Test scenarios](#test-scenarios "#test-scenarios")

## Available tools

The Insurance API provides five tools for managing insurance policies and claims:

InsuranceAPI\_\_get_policy

Retrieve insurance policy details.

**Parameters:**

- `policyId` (string, required) - The policy identifier

InsuranceAPI\_\_file_claim

File an insurance claim.

**Parameters:**

- `policyId` (string, required) - The policy identifier
- `claimType` (string, required) - Type of claim (e.g., "health",
  "property", "auto")
- `amount` (number, required) - Claim amount
- `description` (string, optional) - Claim description

InsuranceAPI\_\_update_coverage

Update policy coverage.

**Parameters:**

- `policyId` (string, required) - The policy identifier
- `coverageType` (string, required) - Type of coverage (e.g.,
  "liability", "collision")
- `newLimit` (number, required) - New coverage limit

InsuranceAPI\_\_get_claim_status

Check claim status.

**Parameters:**

- `claimId` (string, required) - The claim identifier

InsuranceAPI\_\_calculate_premium

Calculate insurance premium.

**Parameters:**

- `coverageType` (string, required) - Type of coverage
- `coverageAmount` (number, required) - Coverage amount
- `riskFactors` (object, optional) - Risk assessment factors

## Authorization policies

The following policies demonstrate various Cedar language features and authorization
patterns. Each policy includes natural language description, Cedar code, and detailed
explanation.

### Policy 1: Multi-action permit

This policy demonstrates how to grant access to multiple related actions using a single
policy statement.

**Natural language:** Allow all principals to get policy
and get claim status.

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action in [
    AgentCore::Action::"InsuranceAPI__get_policy",
    AgentCore::Action::"InsuranceAPI__get_claim_status"
  ],
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
);

```

**Explanation:** This policy demonstrates multi-action
permits using the `in` operator. Instead of writing separate policies for each
read operation, a single policy grants access to multiple related actions. This is useful
for grouping similar operations that share the same authorization requirements.

### Policy 2: Scope-based authorization

This policy shows how to use OAuth scopes to control access to specific
operations.

**Natural language:** Allow principals with scope
containing "insurance:claim" to file claims.

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__file_claim",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
when {
  principal.hasTag("scope") &&
  principal.getTag("scope") like "*insurance:claim*"
};

```

**Explanation:** This policy demonstrates OAuth scope
validation using tags. The `hasTag` method checks if the tag exists, and
`getTag` retrieves its value. The `like` operator with wildcards (\*)
performs pattern matching, allowing flexible scope formats like "insurance:claim",
"insurance:claim:write", or "admin insurance:claim".

### Policy 3: Role-based authorization with unless

This policy demonstrates using the `unless` clause to create exceptions to
restrictions.

**Natural language:** Block principals from updating
coverage unless the principal has role "senior-adjuster" or "manager".

**Cedar policy:**

```

forbid(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__update_coverage",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
unless {
  principal.hasTag("role") &&
  (principal.getTag("role") == "senior-adjuster" || principal.getTag("role") == "manager")
};

```

**Explanation:** This policy demonstrates the
`unless` clause, which inverts the condition logic. The forbid applies unless
the user has one of the specified roles. This is useful for creating exceptions to
restrictions. The policy also shows OR logic for checking multiple acceptable values.

### Policy 4: String equality with OR logic

This policy shows how to validate input parameters and use OR logic for multiple
acceptable values.

**Natural language:** Allow principals to file claims when
the claim type is health, property, or auto.

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__file_claim",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
when {
  context.input has claimType &&
  (context.input.claimType == "health" ||
   context.input.claimType == "property" ||
   context.input.claimType == "auto")
};

```

**Explanation:** This policy demonstrates accessing tool
input parameters via `context.input` and string equality checks with OR logic.
The `has` operator first verifies the field exists before accessing it,
preventing errors when optional fields are missing.

### Policy 5: Field existence check

This policy demonstrates how to enforce business rules by requiring optional
fields.

**Natural language:** Block principals from filing claims
unless a description is provided.

**Cedar policy:**

```

forbid(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__file_claim",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
unless {
  context.input has description
};

```

**Explanation:** This policy demonstrates enforcing
required fields for optional parameters. The description field is optional in the tool
schema, but this policy makes it mandatory by forbidding requests that don't include it.
This shows how policies can add business rules beyond schema validation.

### Policy 6: Username-based authorization

This policy shows how to grant access based on specific user identities.

**Natural language:** Allow principals with username
"Clare" to update coverage.

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__update_coverage",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
when {
  principal.hasTag("username") &&
  principal.getTag("username") == "Clare"
};

```

**Explanation:** This policy demonstrates username-based
authorization using exact string matching. Combined with Policy 3, this creates a two-part
authorization: users must have the username "insurance-agent" AND have the role
"senior-adjuster" or "manager" to update coverage.

### Policy 7: Pattern matching with like

This policy demonstrates flexible pattern matching using wildcards for category-based
access control.

**Natural language:** Allow principals to calculate premium
when the coverage type contains "auto".

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__calculate_premium",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
when {
  context.input has coverageType &&
  context.input.coverageType like "*auto*"
};

```

**Explanation:** This policy demonstrates flexible pattern
matching with the `like` operator. The wildcard \* matches any characters, so
"auto", "auto-liability", "comprehensive-auto", or "auto-collision" would all match. This is
useful when you want to match a category of values rather than exact strings.

### Policy 8: Combined conditions with

AND

This policy shows how to combine multiple conditions to create complex authorization
rules.

**Natural language:** Allow principals to update coverage
when the coverage type is liability or collision and a new limit is provided.

**Cedar policy:**

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"InsuranceAPI__update_coverage",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:us-west-2:123456789012:gateway/insurance"
)
when {
  context.input has coverageType &&
  context.input has newLimit &&
  (context.input.coverageType == "liability" || context.input.coverageType == "collision")
};

```

**Explanation:** This policy demonstrates combining
multiple conditions with AND logic. All three conditions must be true: coverageType must
exist, newLimit must exist, and coverageType must be either "liability" or "collision". This
works with Policy 6 to create layered authorization: who can update (Policy 6) and what they
can update (Policy 8).

## Understanding authorization semantics

These policies demonstrate key Cedar authorization semantics:

### Default deny

If no policy explicitly permits an action, it's denied. For example, a user without the
"insurance:claim" scope cannot file claims even though no policy explicitly forbids
it.

### Forbid wins

If any forbid policy matches, the request is denied even if permit policies also match.
Policy 5 (forbid without description) overrides Policy 2 (permit with scope) when
description is missing.

### Policy layering

Multiple policies can apply to the same request:

- Policy 6 permits insurance-agent to update coverage
- Policy 3 forbids updates unless user has senior-adjuster or manager role
- Policy 8 permits updates only for liability or collision types

For a request to succeed, it must satisfy all three: be insurance-agent (Policy 6), have
senior-adjuster or manager role (Policy 3), and update liability or collision (Policy
8).

## Test scenarios

The following scenarios demonstrate how the policies work together in practice:

Scenario 1: Regular user viewing policy

**User:** username="john",
scope="insurance:view"

**Action:** get_policy

**Expected:** ALLOW (Policy 1)

Scenario 2: User filing health claim with description

**User:** username="jane",
scope="insurance:claim"

**Action:** file_claim with claimType="health",
description="Medical expenses"

**Expected:** ALLOW (Policy 2, Policy 4, Policy 5 does
not forbid)

Scenario 3: User filing claim without description

**User:** username="jane",
scope="insurance:claim"

**Action:** file_claim with claimType="health", no
description

**Expected:** DENY (Policy 5 forbid wins)

Scenario 4: Insurance agent updating coverage

**User:** username="insurance-agent",
role="senior-adjuster"

**Action:** update_coverage with
coverageType="liability"

**Expected:** ALLOW (Policy 6, Policy 3 does not
forbid, Policy 8)

Scenario 5: Insurance agent without senior role

**User:** username="insurance-agent",
role="agent"

**Action:** update_coverage with
coverageType="liability"

**Expected:** DENY (Policy 3 forbid wins)

Scenario 6: Premium calculation for auto coverage

**User:** username="anyone", scope="any"

**Action:** calculate_premium with
coverageType="auto-liability"

**Expected:** ALLOW (Policy 7, pattern matches
"auto")
