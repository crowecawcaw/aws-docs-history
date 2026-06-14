# AGENTSEC02-BP01 Implement tool authorization

An agent with unconstrained tool access has no meaningful privilege
boundary. Externally enforced authorization at the gateway, combined
with identity propagation and human review for mutating operations,
enforces bounded autonomy at the tool layer.

**Desired outcome:**

- You authorize every tool invocation against a defined policy
  before execution, with agent identity and user context
  propagated through the authorization chain.
- Agents can invoke only the tools within their approved scope,
  and attempts to access unauthorized tools are blocked and
  logged.
- Human-in-the-loop checkpoints intercept high-risk mutating
  operations so consequential actions receive review before
  execution.

**Common anti-patterns:**

- Granting agents blanket access to every available tool rather
  than scoping access to the tools each agent requires.
- Relying on the agent's own judgment to decide whether a tool
  invocation is appropriate, with no independent check at the tool
  or API layer.
- Failing to propagate user identity context through tool
  invocations, so downstream services can't enforce user-level
  access controls and every call runs with the agent's
  permissions.
- Skipping human-in-the-loop controls for mutating operations
  because they add latency, accepting unbounded risk for actions
  that are difficult or impossible to reverse.

**Benefits of establishing this best
practice:**

- RBAC policies scope each agent to the tools its defined tasks
  require, implementing least-privilege tool access.
- Identity propagation lets downstream services enforce user-level
  access controls on resources reached through agent tool calls.
- Rate limiting and human-in-the-loop controls constrain
  autonomous execution to operations with acceptable risk
  profiles.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Authorization implemented only through prompt instructions is
insufficient because prompts can be manipulated through
adversarial phrasing or prompt injection. Implement authorization
as an external, deterministic check that happens before the tool
executes, regardless of how the agent arrived at the call.
[Amazon
Bedrock AgentCore Gateway](../../../bedrock/latest/userguide/agentcore-gateway.md "../../../bedrock/latest/userguide/agentcore-gateway.md") is the enforcement point, and
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/ "https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/") is the rules engine.

Gateway runs a dual-sided security model. On the inbound side, it
follows the MCP authorization specification and acts as an OAuth
resource server, working with Amazon Cognito, Okta, Auth0, or your
own OAuth provider. You configure approved client IDs and
audiences to control which applications and agents can reach your
tools, and Gateway supports both authorization code flow (3LO) and
client credentials flow (2LO) for service-to-service
communication. On the outbound side, the authentication model
depends on target type: AWS Lambda and Smithy model targets use
IAM-based authorization through a role you configure with scoped
permissions, and OpenAPI targets support API key or OAuth 2LO
client credentials grant.
[Amazon
Bedrock AgentCore Identity](../../../bedrock/latest/userguide/agentcore-identity.md "../../../bedrock/latest/userguide/agentcore-identity.md") resource credentials providers
handle token caching and secure storage, and each target is
associated with exactly one authentication configuration for clear
boundaries and auditability.

Policy is where fine-grained authorization lives. Cedar policies
evaluate every agent-to-tool request at the gateway before
execution, with a default-deny posture where forbid always wins
over permit. Conditions can reference OAuth claims from the JWT
token (user role, scopes, tenant-level identifiers like patient
ID), tool input parameters, and runtime context such as time of
day. That lets you express rules like "role=clinician can
reschedule appointments for patients in their own panel" as
a deterministic policy rather than a hope about the prompt.
Policies can be authored directly in Cedar or generated from
natural language, and Gateway supports a LOG_ONLY mode so you can
validate policy behavior against live traffic before switching to
enforce mode.

Tool overload is its own risk. Presenting an agent with hundreds
of tools increases the chance it selects the wrong one or follows
an inefficient execution path. Gateway's built-in
x_amz_bedrock_agentcore_search tool exposes
semantic tool discovery so agents locate relevant tools through
natural language rather than seeing the full inventory. That
reduces the surface the model reasons across on any given turn.

For tools that perform mutating operations (writes to databases,
outbound emails, financial transactions), human-in-the-loop review
belongs in the execution path, not the prompt. AWS Step Functions
callback patterns let an agent pause and wait for approval. The
workflow sends an approval request through Amazon SNS or Amazon SES and resumes only after a human responds within a defined
timeout. Configure escalation paths for timeouts so a non-response
doesn't silently block a legitimate action. Rate limiting at both
the Gateway and tool API levels helps prevent resource exhaustion:
Amazon API Gateway usage plans and throttling enforce per-agent
rate limits, and AWS Lambda reserved concurrency caps the maximum
parallel tool invocations. Gateway publishes usage, invocation,
performance, and error metrics to Amazon CloudWatch and integrates
with AWS CloudTrail for a full audit trail, so runaway loops and
unexpected call patterns surface as signal.

### Implementation steps

1. **Configure Gateway inbound
   OAuth:** Create an
   [Amazon
   Bedrock AgentCore Gateway](../../../bedrock/latest/userguide/agentcore-gateway.md "../../../bedrock/latest/userguide/agentcore-gateway.md") and wire inbound OAuth
   authorization to your identity provider (Amazon Cognito,
   Okta, Auth0, or your own OAuth provider), specifying
   approved client IDs and audiences.
2. **Add targets with scoped outbound
   credentials:** Register tool APIs as gateway
   targets, configuring IAM roles for Lambda and Smithy targets
   and API key or OAuth 2LO for OpenAPI targets, and manage
   outbound credentials through
   [Amazon
   Bedrock AgentCore Identity](../../../bedrock/latest/userguide/agentcore-identity.md "../../../bedrock/latest/userguide/agentcore-identity.md") resource credentials
   providers.
3. **Author Cedar policies for
   authorization:** Create a policy engine in
   [Policy
   in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/ "https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/") and define Cedar policies
   with identity-aware conditions on OAuth claims (user role,
   scopes, user ID) and tool input parameters. Author directly
   in Cedar or generate policies from natural language
   descriptions.
4. **Validate policies in LOG_ONLY before
   enforcing:** Associate the policy engine with
   Gateway in LOG_ONLY mode, review observability logs to
   confirm the policies produce the expected permit and deny
   decisions, then switch to enforce mode.
5. **Enable semantic tool
   discovery:** Opt in to the built-in
   x_amz_bedrock_agentcore_search tool so
   agents locate relevant tools through natural language
   queries rather than reasoning over the full inventory.
6. **Add human-in-the-loop approvals for
   mutating tools:** Wire AWS Step Functions callback
   patterns for high-risk tools, send approval requests through
   Amazon SNS or Amazon SES, and configure escalation paths for
   reviewer timeouts.
7. **Cap concurrency and request
   rates:** Enforce per-agent rate limits through
   Amazon API Gateway usage plans and cap parallel invocations
   with AWS Lambda reserved concurrency to help prevent
   resource exhaustion.
8. **Monitor authorization
   decisions:** Use Gateway's Amazon CloudWatch
   metrics and AWS CloudTrail integration to track tool
   invocations, authorization failures, and rate-limit events,
   and configure alarms for authorization-failure spikes.
9. **Review tool authorization
   quarterly:** Remove unused permissions and tighten
   access boundaries on a regular cadence as workloads and
   tools evolve.

## Resources

**Related best practices:**

- [AGENTSEC02-BP02 Validate
  tool inputs and outputs](agentsec02-bp02.md "agentsec02-bp02.md")
- [AGENTSEC02-BP03 Maintain
  approved tool registry with security assessments](agentsec02-bp03.md "agentsec02-bp03.md")
- [AGENTSEC03-BP03
  Implement least privilege with dynamic boundaries](agentsec03-bp03.md "agentsec03-bp03.md")
- [AGENTREL02-BP02
  Limit agent permissions to minimum required access](agentrel02-bp02.md "agentrel02-bp02.md")
- [AGENTCOST04-BP01
  Design cost effective tool selection to minimize unnecessary
  invocations](agentcost04-bp01.md "agentcost04-bp01.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Gateway documentation](../../../bedrock/latest/userguide/agentcore-gateway.md "../../../bedrock/latest/userguide/agentcore-gateway.md")
- [Introducing
  Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
  agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/ "https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/")
- [Apply
  fine-grained access control with Bedrock AgentCore Gateway
  interceptors](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/ "https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/")
- [Secure
  AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/ "https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/")
- [Amazon
  Bedrock AgentCore Identity documentation](../../../bedrock/latest/userguide/agentcore-identity.md "../../../bedrock/latest/userguide/agentcore-identity.md")

**Related examples:**

- [Healthcare
  appointment agent with Policy enforcement (GitHub)](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases/healthcare-appointment-agent "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases/healthcare-appointment-agent")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
