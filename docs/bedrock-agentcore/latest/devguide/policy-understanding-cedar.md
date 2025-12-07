# Understanding Cedar policies

AgentCore Policy uses Cedar policies to control access to AgentCore Gateway tools. This section explains
Cedar policy structure, evaluation semantics, and key concepts.

###### Topics

- [Example policy](#policy-example "#policy-example")
- [Policy structure](#policy-structure "#policy-structure")
- [Policy effects](#policy-effects "#policy-effects")
- [Default deny](#policy-default-deny "#policy-default-deny")
- [Authorization evaluation](#policy-authorization-evaluation "#policy-authorization-evaluation")
- [Policy independence](#policy-independence "#policy-independence")

## Example policy

Consider a refund processing tool with these requirements:

- Only the user "John" can process refunds
- Refunds are limited to $500 or less

The Cedar policy that enforces these requirements:

```

permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"RefundTool__process_refund",
  resource == AgentCore::Gateway::"arn:aws:bedrock-agentcore:your-region:your-account-id:gateway/refund-gateway"
)
when {
  principal.hasTag("username") &&
  principal.getTag("username") == "John" &&
  context.input.amount < 500
};

```

This policy allows refund processing only when the user is "John" and the refund amount is
less than $500.

## Policy structure

Cedar policies consist of three main components:

1. **Effect** - Determines whether to allow or deny access
   (`permit` or `forbid`)
2. **Scope** - Specifies the principal, action, and resource
   the policy applies to
3. **Condition** - Defines additional logic that must be
   satisfied (`when` or `unless`) and can refer to the tool parameters
   (through the context) and the OAuth token (through the tags)

## Policy effects

Cedar policies use two effects to control access:

- `permit` - Allows the action to proceed
- `forbid` - Denies the action

## Default deny

All actions are denied by default. If no policies match a request, Cedar returns DENY. You
must explicitly write permit policies to allow actions.

## Authorization evaluation

Cedar uses a forbid-overrides-permit evaluation model:

1. Cedar evaluates all policies that apply to the request
2. If any forbid policy matches, the result is DENY
3. If at least one permit policy matches and no forbid policies does, the result is
   ALLOW
4. If no policies match, the result is DENY (default deny)

## Policy independence

Each Cedar policy evaluates independently. A policy's evaluation depends only on:

- The scope (principal, action, resource)
- The context and tags

Policies do not reference or depend on other policies.
