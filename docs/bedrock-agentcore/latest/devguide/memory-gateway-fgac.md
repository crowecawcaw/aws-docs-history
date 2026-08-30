# Fine-grained access control for Memory

With fine-grained access control (FGAC) for Amazon Bedrock AgentCore Memory, you can bind Memory access to an OAuth-authenticated caller’s identity.

When callers reach Memory with AWS IAM credentials, you can already restrict access by action, by Memory resource, and by the request’s actor, session, and namespace scopes, using IAM identity-based and resource-based policies with Memory’s condition keys. For those controls, see [Memory organization in AgentCore Memory](memory-organization.md "memory-organization.md") and [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md "resource-based-policies.md").

Those IAM controls match against the _IAM principal_ that calls Memory. They cannot express a rule keyed on an _OAuth/JWT_ identity, because an OAuth-authenticated caller is not an IAM principal. This matters for applications where callers authenticate with OAuth rather than AWS credentials — for example, an agent application whose end users sign in through an OpenID Connect provider. In that architecture the HTTP caller is typically the agent or backend, which passes the end user’s (or the agent’s own) JWT with each request; FGAC evaluates policies against the identity in that token. With FGAC, you can write policies that compare a request attribute to the token’s claims, so you can enforce rules such as:

- A caller can only access events where the request’s `actorId` equals their JWT `sub` claim.
- A caller can only retrieve memory records under the namespace carried in their own token claim.
- Access is granted only to callers presenting a specific OAuth `client_id`.
  FGAC policies can also condition on the same action, Memory-resource, and request-attribute scopes that IAM offers, so a single policy can combine who the caller is with which operations and data they can access.

FGAC for Memory is implemented with [Policy in Amazon Bedrock AgentCore](policy.md "policy.md"). You attach a _policy engine_ to the [gateway](memory-gateway-connector.md "memory-gateway-connector.md") that fronts your Memory resource and write policies in Cedar, an open-source policy language documented on the [Cedar Policy website](https://www.cedarpolicy.com/ "https://www.cedarpolicy.com/"). The gateway evaluates these policies before it forwards a request to Memory. The Cedar policy language, principal types, policy engines, and policy validation are all documented in [Policy in Amazon Bedrock AgentCore](policy.md "policy.md") — this page describes only what is specific to Memory: the actions and request attributes the Memory connector exposes, and the policy patterns that isolate Memory data by caller.

###### Note

FGAC for Memory is built on the AgentCore Memory connector. Set up a gateway with a Memory connector target first. For more information, see [Access AgentCore Memory through a gateway](memory-gateway-connector.md "memory-gateway-connector.md").

###### Topics

- [How fine-grained access control works](#memory-gateway-fgac-how "#memory-gateway-fgac-how")
- [Set up fine-grained access control for Memory](#memory-gateway-fgac-setup "#memory-gateway-fgac-setup")
- [Memory actions and request attributes](#memory-gateway-fgac-reference "#memory-gateway-fgac-reference")
- [What you can enforce](#memory-gateway-fgac-enforced "#memory-gateway-fgac-enforced")
- [Adopt fine-grained access control on an existing Memory](#memory-gateway-fgac-adopting "#memory-gateway-fgac-adopting")
- [Relationship to other access-control options](#memory-gateway-fgac-relationship "#memory-gateway-fgac-relationship")
- [Policy examples for Memory](memory-gateway-fgac-policy-examples.md "memory-gateway-fgac-policy-examples.md")

## How fine-grained access control works

A policy engine holds a set of Cedar policies and evaluates them for each request that flows through an associated gateway. After the gateway authenticates the caller and resolves the request to a Memory operation, the policy engine evaluates the policies against the request’s **principal** (who is calling), **action** (which Memory operation), **resource** (which gateway), and **context** (the request’s attributes, such as path parameters and body fields). Evaluation is deny-by-default and `forbid` overrides `permit`.

Because the Memory connector makes each Memory operation available as a Cedar action with its request fields, your policies can allow or deny specific Memory operations and condition on their request attributes. The generic Cedar model — policy structure, `permit`/`forbid`, the `AgentCore::OAuthUser` and `AgentCore::IamEntity` principal types, tags, and `context.input` — is described in [Understanding Cedar policies](policy-understanding-cedar.md "policy-understanding-cedar.md") and [Core concepts](policy-core-concepts.md "policy-core-concepts.md").

## Set up fine-grained access control for Memory

###### Note

You can set up fine-grained access control for Memory through the AWS Management Console, the AWS SDK, and the AWS Command Line Interface (AWS CLI).

After you have a gateway with a Memory connector target (see [Access AgentCore Memory through a gateway](memory-gateway-connector.md "memory-gateway-connector.md")):

1. Create a policy engine and add your Cedar policies. For the steps, see [Create a policy engine](policy-create-engine.md "policy-create-engine.md") and [Create a policy](policy-create-policies.md "policy-create-policies.md"). For the policies to write, see [Policy examples for Memory](memory-gateway-fgac-policy-examples.md "memory-gateway-fgac-policy-examples.md").
2. Associate the policy engine with the gateway that fronts your Memory resource, by setting the gateway’s `policyEngineConfiguration`. You can set it when you create the gateway with [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md"), or add it later with [UpdateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md").

The policy engine’s `mode` controls whether policies are enforced (`ENFORCE`) or only evaluated and logged without blocking traffic (`LOG_ONLY`). Test your policies in `LOG_ONLY` before switching to `ENFORCE` to avoid unintended denials. For enforcement modes, policy validation, and testing, see [Validate and test policies](policy-validate-policies.md "policy-validate-policies.md") and [Use policies](policy-use-policies.md "policy-use-policies.md").

## Memory actions and request attributes

This section is the Memory-specific reference for writing policies: the Cedar action id for each Memory operation, and the request attributes available under `context.input`.

### Memory action ids

Each Memory operation is a Cedar action named `<target-name>___<METHOD>:<uri-template>`, where `<target-name>` is your connector target’s name. The URI keeps its path-parameter placeholders — they are not substituted with concrete values. In the following table, replace `<target-name>` with your connector target’s name.

| Memory operation         | Cedar action id                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| ListEvents               | `<target-name>___POST:/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}`                    |
| CreateEvent              | `<target-name>___POST:/memories/{memoryId}/events`                                                  |
| GetEvent                 | `<target-name>___GET:/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}/events/{eventId}`    |
| DeleteEvent              | `<target-name>___DELETE:/memories/{memoryId}/actor/{actorId}/sessions/{sessionId}/events/{eventId}` |
| ListSessions             | `<target-name>___POST:/memories/{memoryId}/actor/{actorId}/sessions`                                |
| ListActors               | `<target-name>___POST:/memories/{memoryId}/actors`                                                  |
| RetrieveMemoryRecords    | `<target-name>___POST:/memories/{memoryId}/retrieve`                                                |
| ListMemoryRecords        | `<target-name>___POST:/memories/{memoryId}/memoryRecords`                                           |
| GetMemoryRecord          | `<target-name>___GET:/memories/{memoryId}/memoryRecord/{memoryRecordId}`                            |
| DeleteMemoryRecord       | `<target-name>___DELETE:/memories/{memoryId}/memoryRecords/{memoryRecordId}`                        |
| ListMemoryExtractionJobs | `<target-name>___POST:/memories/{memoryId}/extractionJobs`                                          |
| StartMemoryExtractionJob | `<target-name>___POST:/memories/{memoryId}/extractionJobs/start`                                    |

Action-id wildcards are not supported; to grant several operations in one policy, list them with `action in […​]`.

###### Note

The Memory batch operations (`BatchCreateMemoryRecords`, `BatchUpdateMemoryRecords`, and `BatchDeleteMemoryRecords`) are not available as Cedar actions and cannot be governed by fine-grained access control. Each carries multiple records in a single request, which the policy engine cannot evaluate individually — so per-record or per-namespace conditions cannot be applied to them.

You can still allow or deny a batch operation as a whole with IAM identity-based and resource-based policies (for example, by allowing or denying the `bedrock-agentcore:BatchCreateMemoryRecords` action). What is missing is only the per-record granularity: at the fine-grained access control layer, a batch operation is all-or-nothing.

### Request context fields

The gateway exposes each request’s attributes under `context.input`, combining path parameters and request-body fields. Guard each field with `has` before you read it (for example, `context has input && context.input has actorId`).

**Path parameters** (from the URI):

- `context.input.memoryId`
- `context.input.actorId`
- `context.input.sessionId`
- `context.input.eventId`
- `context.input.memoryRecordId`

**Request-body fields** (operation-dependent, from the request payload):

- `context.input.namespace`
- `context.input.namespacePath`
- `context.input.metadata`
- `context.input.filter`
- `context.input.payload`
- and other body fields defined by each operation’s schema

The available fields differ by operation. A field that one operation carries (for example, `actorId` on `ListEvents`) might not be present on another operation that the same policy matches.

###### Warning

A policy that references a context field is validated against the schema for the actions in its scope, but not against every operation the request might reach at runtime. If a policy references a field that the incoming request does not carry, the policy can be created successfully and reach `ACTIVE`, yet deny the request with a `403` response when the policy engine evaluates it, because the referenced field is missing. This condition is not reported when you create the policy.

To avoid unexpected denials:

- Scope each policy to the specific actions whose requests carry the fields the policy references, and confirm those fields against each operation in the [Memory action ids](#memory-gateway-fgac-action-ids "#memory-gateway-fgac-action-ids") table.
- Guard every field access with `has` (for example, `context has input && context.input has actorId`) so a `permit` condition evaluates predictably when a field is absent.
- Test policies in `LOG_ONLY` mode before enforcing them, so you can observe evaluation outcomes without denying live traffic. For more information, see [Set up fine-grained access control for Memory](#memory-gateway-fgac-setup "#memory-gateway-fgac-setup").

## What you can enforce

FGAC enforcement through the Memory connector is available across all of the gateway’s inbound authentication modes. Using the actions and attributes above, you can enforce:

- **Principal-type gating** — policies scoped to OAuth-only or IAM-only callers match or deny by caller class.
- **Per-identity isolation** — a request attribute such as `actorId` can be required to equal the `sub` claim of the authenticated user or agent in the JWT, allowing the owner and denying others.
- **Namespace isolation** — comparing the request’s `namespace` or `namespacePath` against a literal, or against a namespace path carried in a token claim, restricts which records a caller can retrieve.
- **Action scoping** — a single action, a set of actions, or any action can be permitted; non-permitted actions are denied.
- **Path-parameter conditions** — path parameters such as `memoryId`, `actorId`, and `sessionId`.
- **Request-body conditions** — body fields such as `metadata` and `namespacePath`.
- **Resource pinning** — a matching gateway ARN is allowed; a different ARN is denied.
- **JWT claim conditions** — token claims such as `sub` and `client_id` gate access (OAuth inbound).
- **IAM identity conditions** — the caller’s IAM ARN can be matched by pattern (IAM inbound).

For policies that implement these, see [Policy examples for Memory](memory-gateway-fgac-policy-examples.md "memory-gateway-fgac-policy-examples.md").

## Adopt fine-grained access control on an existing Memory

The primary isolation pattern requires that the `actorId` on a request equal the caller’s JWT `sub` claim (`context.input.actorId == principal.getTag("sub")`). Existing deployments often use an internal user id as the `actorId` that does not match the `sub` value from their identity provider. If your `actorId` values already equal your provider’s `sub`, no changes are needed. Otherwise, choose one of the following approaches:

**Match on a custom JWT claim**

If your identity provider can issue a claim that already holds your internal user id (for example, a custom claim that mirrors your `actorId` scheme), compare against that claim instead of `sub` — for example, `context.input.actorId == principal.getTag("custom:app_user_id")`. Guard it with `hasTag` first. This avoids changing any stored data.

**Isolate by namespace instead of `actorId`**

If your long-term memory records are organized into per-user namespaces, enforce isolation on the namespace rather than on `actorId`. Have your identity provider issue a claim that holds the caller’s full namespace path, and compare the request’s `namespacePath` against that claim. For the namespace isolation pattern, see [Policy examples for Memory](memory-gateway-fgac-policy-examples.md "memory-gateway-fgac-policy-examples.md").

**Align `actorId` with `sub`**

If you want to use the default `actorId == sub` pattern, migrate new events and records to use the provider’s `sub` as the `actorId`. Because AgentCore Memory stores events and records under the `actorId` you supply, this typically applies going forward rather than rewriting historical data; plan for a transition period in which both schemes might be present.

###### Tip

You can validate any of these approaches without affecting live traffic by attaching the policy in `LOG_ONLY` mode first and reviewing the evaluation logs. See [Set up fine-grained access control for Memory](#memory-gateway-fgac-setup "#memory-gateway-fgac-setup").

## Relationship to other access-control options

Cedar policies evaluated by the policy engine are the identity-aware, per-request authorization layer for Memory traffic through a gateway. They complement, and can be combined with, the gateway’s other access-control options:

- **Gateway interceptors** let you implement custom authorization logic in code. For more information, see [Fine-grained access control for Amazon Bedrock AgentCore Gateway](gateway-fine-grained-access-control.md "gateway-fine-grained-access-control.md").
- **Resource-based policies** on the Memory resource control which IAM principals — including a specific gateway — can call Memory at all, using condition keys such as `aws:SourceArn` and `aws:PrincipalArn`. For more information, see [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md "resource-based-policies.md") and [How the outbound credential mode affects Memory access control](memory-gateway-connector.md#memory-gateway-connector-credential-modes "memory-gateway-connector.md#memory-gateway-connector-credential-modes").
