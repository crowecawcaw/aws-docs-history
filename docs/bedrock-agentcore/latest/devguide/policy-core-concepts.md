# Core concepts

Before using Policy in Amazon Bedrock AgentCore, it’s important to understand the key concepts and components that work together to provide policy-based governance for your AI agents.

###### Topics

- [Gateway](#concept-gateway "#concept-gateway")
- [Gateway Target](#concept-gateway-target "#concept-gateway-target")
- [Principal types](#concept-principal-types "#concept-principal-types")
- [Cedar](#concept-cedar "#concept-cedar")
- [Cedar Policy](#concept-cedar-policy "#concept-cedar-policy")
- [Dogwood](#concept-dogwood "#concept-dogwood")
- [Temporal policies](#concept-temporal-policy "#concept-temporal-policy")
- [Guardrails](#concept-guardrails "#concept-guardrails")
- [Policy session](#concept-policy-session "#concept-policy-session")
- [Policy engine](#concept-policy-engine "#concept-policy-engine")
- [Cedar Schema](#concept-cedar-schema "#concept-cedar-schema")
- [Cedar validation](#concept-cedar-validation "#concept-cedar-validation")
- [Cedar analysis](#concept-cedar-analysis "#concept-cedar-analysis")
- [Policy authoring service](#concept-policy-authoring-service "#concept-policy-authoring-service")

## Gateway

An Amazon Bedrock AgentCore Gateway provides an endpoint to connect to MCP servers and convert APIs and lambda to MCP compatible tools, providing a single access point for an agent to interact with its tools. A Gateway can have multiple targets, each representing a different tool or set of tools.

## Gateway Target

A target defines the APIs or Lambda function that a Gateway will provide as tools to an agent. Targets can be Lambda functions, OpenAPI specifications, Smithy models, or other tool definitions.

## Principal types

Cedar policies use principals to represent the entity making an authorization request. Policy in AgentCore supports two principal types depending on how your AgentCore Gateway is configured for authentication:

- **AgentCore::OAuthUser** - Represents OAuth-authenticated users. When a AgentCore Gateway uses OAuth authorization, the principal is created from the JWT token’s `sub` claim. OAuth principals support tags that contain JWT claims such as username, scope, role, etc.
- **AgentCore::IamEntity** - Represents IAM-authenticated callers. When a AgentCore Gateway uses AWS\_IAM authorization, the principal is created from the caller’s IAM identity. IAM principals have an `id` attribute containing the IAM ARN (format: `arn:aws:sts::<account>:assumed-role/<role-name>` for assumed roles), enabling stable `principal ==` matching. See [Policy conditions](policy-conditions.md "policy-conditions.md") for details.

## Cedar

[Cedar](https://docs.cedarpolicy.com "https://docs.cedarpolicy.com") is an open-source policy language developed by AWS for writing and enforcing authorization policies. Cedar policies are human-readable, analyzable, and can be validated against a schema. Policy in AgentCore uses Cedar to provide precise, verifiable access control for gateway tools.

## Cedar Policy

A Cedar policy is a declarative statement that permits or forbids access to gateway tools. Each policy specifies who (principal) can perform what action (tool invocation) on which resource (gateway) under what conditions. Policies are evaluated for every tool invocation request.

## Dogwood

[Dogwood](https://dogwood-policy.github.io/dogwood/index.html "https://dogwood-policy.github.io/dogwood/index.html") is an open-source policy language on the Dogwood Policy website that is compatible with Cedar: every valid Cedar policy is
also a valid Dogwood policy, so your existing Cedar policies work unchanged. Beyond the point-in-time
conditions you can already express, Dogwood also supports session-aware _temporal_ conditions and
_information providers_, such as Guardrails, that supply computed signals to a policy. Dogwood
policies are evaluated against a policy session that groups related requests.

## Temporal policies

Most Cedar policies are stateless: each request is evaluated on its own. A _temporal policy_ adds
conditions that depend on what happened earlier in the same session, such as requiring a prior
approval, limiting how often an action runs, or keeping a running total under a threshold. Temporal
policies are written in Dogwood, which is compatible with Cedar, and are evaluated against a policy session that
groups related requests. For more information, see [Temporal policies](policy-temporal.md "policy-temporal.md").

## Guardrails

Guardrails are information providers that a Dogwood policy can consult inline. At evaluation time, a
guardrail computes a content-safety signal for the request — such as a content-filter, prompt-attack,
or sensitive-information score — and the policy permits or forbids the action based on that result.
For more information, see [Guardrails in policies](policy-guardrails-in-policies.md "policy-guardrails-in-policies.md").

## Policy session

A policy session is a sequence of related Gateway invocations grouped under one session ID, which you
supply on requests in the `x-amzn-bedrock-agentcore-policy-session-id` header. Temporal policies
evaluate against a policy session: a temporal condition considers only the events recorded for the
same session as the request being authorized. For more information, see
[Policy sessions and identity propagation](policy-session-based-temporal.md "policy-session-based-temporal.md").

## Policy engine

The policy engine is the core component of Policy in AgentCore that stores and evaluates Cedar policies. When you create policies, they apply to every gateway which is associated with the engine, as long as the policy scope matches the request. For every tool invocation, the policy engine evaluates all applicable policies against the request to determine whether to allow or deny access. The engine enforces default-deny and forbid-wins semantics automatically.

## Cedar Schema

A Cedar schema defines the structure of entities, actions, and context for policy validation. The policy engine automatically generates a schema from the gateway’s tool definitions, mapping each tool to an action and defining the expected input parameters. The schema ensures policies are validated at creation time, catching errors before deployment.

## Cedar validation

Cedar validation checks that policies are syntactically correct and comply with the schema. When you associate policies to a gateway, the policy engine validates them against the auto-generated schema to ensure they reference valid actions, use correct data types, and access only defined context fields. Validation catches errors before policies are deployed, preventing runtime authorization failures.

## Cedar analysis

Cedar analysis uses automated reasoning to examine policies and detect potential issues. Policy in AgentCore uses automated reasoning to identify policies that always allow (no conditions restrict access) or always deny (forbid policies with no exceptions), helping ensure policies implement intended access control rather than being overly permissive or unnecessarily restrictive.

## Policy authoring service

The policy authoring service automatically converts natural language authorization requirements into Cedar policies. When you submit a natural language policy, the service generates syntactically correct Cedar code, validates it against the gateway schema, and runs automated analysis to detect potential issues. This ensures all generated policies are valid and helps identify overly permissive or restrictive rules before deployment.
