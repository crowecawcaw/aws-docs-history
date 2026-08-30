# Access AgentCore Memory through a gateway

By default, an application calls the Amazon Bedrock AgentCore Memory data plane directly, and each request is authenticated with AWS Signature Version 4 (SigV4). You can control this access with both IAM identity-based and resource-based policies. This works well when your backend service calls Memory on behalf of all users and does not need to enforce per-user isolation at the Memory layer.

When your backend calls Memory for many users, Memory sees only your backend’s IAM role. It cannot verify which end user a request is for. Your application code must set the correct `actorId` and namespace on each request to isolate one user’s data from another’s.

With an [AgentCore Gateway](gateway.md "gateway.md") in front of AgentCore Memory, you can move that enforcement out of your application code and into the infrastructure. The gateway becomes a single, secure entry point for Memory traffic. It authenticates each caller, evaluates access-control policies, and forwards allowed requests to Memory. Fronting Memory with a gateway gives you two features that direct access does not:

**OAuth authentication for end users**

Memory’s data plane is SigV4-only. With a gateway configured for OAuth (JWT) inbound authentication, your end users can authenticate with a standard OpenID Connect provider, and your application does not distribute AWS credentials to them. For more information, see [Authenticate end users to Memory with OAuth](memory-gateway-oauth.md "memory-gateway-oauth.md").

**Fine-grained access control**

A gateway can evaluate policies that restrict callers to their own actor, their own namespace, or a specific set of Memory operations, including for callers authenticated with OAuth. For more information, see [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").

###### Note

Fine-grained access control is not supported for the Memory batch operations (`BatchCreateMemoryRecords`, `BatchUpdateMemoryRecords`, and `BatchDeleteMemoryRecords`). Each of these operations carries multiple records in a single request, which the policy engine cannot evaluate individually.

Both features are built on the AgentCore Memory connector described on this page. Setting up the connector is a prerequisite for either one.

###### Topics

- [The AgentCore Memory connector](#memory-gateway-connector-what "#memory-gateway-connector-what")
- [How a request flows through the gateway](#memory-gateway-connector-flow "#memory-gateway-connector-flow")
- [Inbound and outbound authentication modes](#memory-gateway-connector-auth-modes "#memory-gateway-connector-auth-modes")
- [How the outbound credential mode affects Memory access control](#memory-gateway-connector-credential-modes "#memory-gateway-connector-credential-modes")
- [Set up a gateway with a Memory connector target](memory-gateway-setup.md "memory-gateway-setup.md")
- [Create a Memory connector using the console](memory-gateway-connector-console.md "memory-gateway-connector-console.md")
- [Authenticate end users to Memory with OAuth](memory-gateway-oauth.md "memory-gateway-oauth.md")
- [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md")
- [Restrict direct access to Memory](memory-gateway-restrict-access.md "memory-gateway-restrict-access.md")

## The AgentCore Memory connector

The AgentCore Memory connector (`agentcore-memory`) is a managed gateway connector that wires a [gateway target](gateway-core-concepts.md "gateway-core-concepts.md") to the AgentCore Memory data plane. Connectors are a built-in target type: rather than authoring an API schema and managing endpoint wiring yourself, you create a target of the connector type and supply only the connector id and the target parameters.

When you create a Memory connector target, you provide:

- the connector id (`agentcore-memory`), and
- the target parameters, notably the `memoryId` of the Memory resource the target fronts.

The connector then:

**Resolves the Memory endpoint**

It determines the correct Memory data-plane endpoint for the target’s Memory resource.

**Makes supported Memory operations available as Cedar actions**

The connector makes the following Memory data-plane operations available as Cedar actions, each with the request fields it accepts: `ListEvents`, `CreateEvent`, `GetEvent`, `DeleteEvent`, `ListSessions`, `ListActors`, `RetrieveMemoryRecords`, `ListMemoryRecords`, `GetMemoryRecord`, `DeleteMemoryRecord`, `ListMemoryExtractionJobs`, and `StartMemoryExtractionJob`. This is what lets fine-grained access-control policies allow or deny specific Memory operations and condition on their request attributes. For the action ids and request attributes, see [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").

###### Note

The Memory batch operations (`BatchCreateMemoryRecords`, `BatchUpdateMemoryRecords`, and `BatchDeleteMemoryRecords`) are not supported for fine-grained access control. Each of these operations carries multiple records in a single request, which the policy engine cannot evaluate individually.

**Forwards requests**

It forwards each allowed request to the Memory data plane using the target’s configured outbound credential mode.

Because the connector provides the Memory model out of the box, you do not hand-author a schema or manage endpoint wiring.

## How a request flows through the gateway

When a client calls Memory through the gateway, the gateway processes the request in four steps:

1. **Inbound authentication** — the gateway validates the caller according to its inbound authorizer type: an OAuth (JWT) bearer token, AWS SigV4, or an unauthenticated request. See [Inbound and outbound authentication modes](#memory-gateway-connector-auth-modes "#memory-gateway-connector-auth-modes").
2. **Action resolution** — the gateway maps the incoming HTTP request (method and path) to the Cedar action for the Memory operation the caller is attempting. Path parameters and request-body fields are extracted into a request context object.
3. **Policy evaluation** — if the gateway has an attached policy engine, it evaluates the configured access-control policies against the request. Evaluation is deny-by-default. See [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").
4. **Outbound authentication** — if the request is allowed, the gateway forwards it to the Memory data plane using the target’s outbound credential mode. See [Outbound credential mode](#memory-gateway-connector-outbound "#memory-gateway-connector-outbound").

## Inbound and outbound authentication modes

A gateway has an _inbound_ authorizer type that controls how it authenticates callers, and each Memory connector target has an _outbound_ credential mode that controls the identity the gateway uses to call Memory. Most deployments use one of two combinations:

**OAuth end users (the primary fine-grained access control path)**

`CUSTOM_JWT` inbound with `GATEWAY_IAM_ROLE` outbound. Your users or agents authenticate with an OpenID Connect provider, and the gateway calls Memory under its own gateway execution role. This is the combination to use when you want per-user isolation for callers who are not IAM principals. For more information, see [Authenticate end users to Memory with OAuth](memory-gateway-oauth.md "memory-gateway-oauth.md").

**IAM backend services with identity pass-through**

`AWS_IAM` inbound with `CALLER_IAM_CREDENTIALS` outbound. The gateway forwards each caller’s own IAM identity to Memory, so Memory evaluates the caller’s IAM permissions and you can source-pin gateway-forwarded traffic. Use this when your callers are already IAM principals and you want Memory to authorize them directly.

Other combinations — such as `AWS_IAM` or `NONE` inbound with `GATEWAY_IAM_ROLE` outbound — are supported for specialized scenarios such as centralized Cedar enforcement for IAM callers or development and testing. See the [compatibility matrix](#memory-gateway-connector-compatibility "#memory-gateway-connector-compatibility") for the full set.

### Inbound authorizer types

You choose the inbound authorizer when you create the gateway. The Memory connector supports all inbound authorizer types that AgentCore Gateway supports. For more information, see [Core concepts for Amazon Bedrock AgentCore Gateway](gateway-core-concepts.md "gateway-core-concepts.md").

- `CUSTOM_JWT` (OAuth/JWT) — the primary path for fine-grained access control. Makes the caller’s JWT claims available to access-control policies and enables OAuth authentication for end users. See [Authenticate end users to Memory with OAuth](memory-gateway-oauth.md "memory-gateway-oauth.md").
- `AWS_IAM` (SigV4) — makes the caller’s IAM identity available to access-control policies. Use it for IAM-authenticated backend callers, centralized Cedar enforcement, or source-pinning.
- `AUTHENTICATE_ONLY` — requires a valid signed request but does not expose a typed caller identity for identity-based policy rules.
- `NONE` — no authorization. Intended for development and testing only; do not use it for production Memory access.

### Outbound credential mode

The outbound credential mode determines the identity the Memory data plane sees. The rule is simple:

- If your inbound authentication is `CUSTOM_JWT` or `NONE`, the gateway always uses `GATEWAY_IAM_ROLE` — it calls Memory under its gateway execution role. There is no other valid option and nothing to choose.
- If your inbound authentication is `AWS_IAM` or `AUTHENTICATE_ONLY`, you can additionally choose `CALLER_IAM_CREDENTIALS` to forward the caller’s own IAM identity to Memory, instead of using the gateway execution role.

| Outbound mode            | How the gateway calls Memory                                                                                                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GATEWAY_IAM_ROLE`       | The gateway calls Memory under its gateway execution role (a first-party call). Works with every inbound type.                                                                         |
| `CALLER_IAM_CREDENTIALS` | The gateway forwards the caller’s own IAM identity to Memory (delegated access). Requires `AWS_IAM` or `AUTHENTICATE_ONLY` inbound, because it needs a caller IAM identity to forward. |

#### Compatibility matrix

The following table lists every supported combination of inbound authorizer and outbound credential mode on the Memory connector target.

| Inbound             | `GATEWAY_IAM_ROLE` | `CALLER_IAM_CREDENTIALS`    |
| ------------------- | ------------------ | --------------------------- |
| `CUSTOM_JWT`        | Supported          | Rejected at target creation |
| `AWS_IAM`           | Supported          | Supported                   |
| `NONE`              | Supported          | Rejected at target creation |
| `AUTHENTICATE_ONLY` | Supported          | Supported                   |

## How the outbound credential mode affects Memory access control

The outbound credential mode determines which identity Memory authorizes, so IAM policies that are scoped to the caller behave differently in each mode. It also determines how you can restrict gateway-forwarded traffic with a Memory [resource-based policy](resource-based-policies.md "resource-based-policies.md").

**`GATEWAY_IAM_ROLE`**

The gateway calls Memory under its gateway execution role, so Memory authorizes the request as that role. To restrict access to this gateway, you can use the `aws:PrincipalArn` condition against the gateway execution role ARN, and scope that role’s identity policy to only the Memory actions the gateway needs. Requests forwarded by the gateway also carry the `aws:SourceArn` condition key set to the gateway ARN (see the following mode).

**`CALLER_IAM_CREDENTIALS`**

The gateway forwards the caller’s IAM identity to Memory, so Memory authorizes the request as the caller. Because the principal is the caller rather than the gateway, use the `aws:SourceArn` condition to restrict access to gateway-forwarded traffic.

In both outbound modes, the gateway stamps the `aws:SourceArn` condition key with the ARN of the gateway that forwarded the request. A Memory [resource-based policy](resource-based-policies.md "resource-based-policies.md") can therefore restrict access to a specific gateway by matching `aws:SourceArn` against the gateway ARN, regardless of the outbound credential mode.

###### Important

Because the outbound credential mode changes which identity Memory authorizes, IAM policies scoped to the caller behave differently:

- With `CALLER_IAM_CREDENTIALS`, Memory sees the caller’s own IAM identity. IAM identity-based and resource-based policies that reference the caller — including a `Deny` on a specific `actorId`, or Memory condition keys such as `bedrock-agentcore:namespace` and `bedrock-agentcore:namespacePath` — are evaluated against that caller.
- With `GATEWAY_IAM_ROLE`, Memory sees only the gateway execution role. Every caller’s request reaches Memory under that single role, so IAM policies scoped to an individual caller’s identity (such as a `Deny` on a specific `actorId`) are **not** evaluated against the original caller and do not take effect. Do not rely on caller-scoped IAM policies to enforce per-caller access in this mode.
  If you use `GATEWAY_IAM_ROLE` and need per-caller access control (for example, restricting a caller to their own `actorId` or namespace), enforce it with fine-grained access control (Cedar policies) on the gateway rather than with caller-scoped IAM policies. This is the primary fine-grained access control path. For more information, see [Fine-grained access control for Memory](memory-gateway-fgac.md "memory-gateway-fgac.md").

For the resource-based policy condition keys and JSON policy examples, see [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md "resource-based-policies.md").
