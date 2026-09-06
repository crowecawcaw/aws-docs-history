

# Policy examples for Memory
<a name="memory-gateway-fgac-policy-examples"></a>

This page provides Cedar policy patterns that are specific to Amazon Bedrock AgentCore Memory — isolating a caller to their own actor, their own namespace, and a chosen set of Memory operations. For the Memory action ids and `context.input` fields these policies reference, see [Memory actions and request attributes](memory-gateway-fgac.md#memory-gateway-fgac-reference). For the generic Cedar model and a broader library of patterns (OAuth scope and role checks, IAM principal matching, `forbid` with `unless`, and input validation), see [Understanding Cedar policies](policy-understanding-cedar.md) and [Example policies](example-policies.md).

You add each Cedar policy to your gateway’s policy engine with the [CreatePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePolicy.html) operation, passing the Cedar statement as the policy `definition`. For the setup sequence, see [Set up fine-grained access control for Memory](memory-gateway-fgac.md#memory-gateway-fgac-setup).

In each Cedar example, replace `<target-name>` with your connector target name and `<gw-arn>` with your gateway ARN.

## Per-user isolation — actorId must equal the JWT subject
<a name="memory-gateway-fgac-example-user-isolation"></a>

Allow an OAuth user to access a session only when the request’s `actorId` equals their JWT `sub` claim. This is the core per-user isolation pattern for Memory: each user can reach only their own actor’s data.

```
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"<target-name>___POST:/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}",
  resource == AgentCore::Gateway::"<gw-arn>"
) when {
  principal.hasTag("sub") &&
  context has input && context.input has actorId &&
  context.input.actorId == principal.getTag("sub")
};
```

## Namespace isolation — caller can only retrieve records under their own namespace
<a name="memory-gateway-fgac-example-namespace-isolation"></a>

This policy allows an OAuth caller to retrieve memory records only when the request’s `namespacePath` matches the caller’s own namespace path, carried in a token claim.

Cedar does not support string concatenation — the `+` operator applies only to integer operands, and `like` wildcard patterns must be string literals. You therefore cannot build a namespace value from a claim inside the policy (for example, `("/actors/" + principal.getTag("sub") + "/")` is not valid Cedar). Instead, have your identity provider issue a claim that already holds the caller’s full namespace path, map it to a principal tag, and compare `namespacePath` against that tag. In this example the token provides a `namespace` claim that contains the caller’s namespace path (such as `/actors/<sub>/`).

```
permit(
  principal is AgentCore::OAuthUser,
  action == AgentCore::Action::"<target-name>___POST:/memories/{memoryId}/retrieve",
  resource == AgentCore::Gateway::"<gw-arn>"
) when {
  principal.hasTag("namespace") &&
  context has input && context.input has namespacePath &&
  context.input.namespacePath == principal.getTag("namespace")
};
```

## Action scoping — allow only a set of Memory operations
<a name="memory-gateway-fgac-example-action-scoping"></a>

Grant a fixed list of Memory operations — for example, allow listing events and retrieving records, but nothing else. Group multiple Memory actions with `action in […​]`; action-id wildcards are not supported.

```
permit(
  principal,
  action in [
    AgentCore::Action::"<target-name>___POST:/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}",
    AgentCore::Action::"<target-name>___POST:/memories/{memoryId}/retrieve"
  ],
  resource == AgentCore::Gateway::"<gw-arn>"
);
```

To ensure Memory can only be reached through your gateway — and not by a principal calling the Memory data plane directly — see [Restrict direct access to Memory](memory-gateway-restrict-access.md).