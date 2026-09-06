

# Security model and permissions for Runtime Instances
<a name="runtime-instances-security"></a>

When you host agents on the **Instances** compute type, your agents run on Amazon EC2 instances in your own AWS account. This changes the shared responsibility model compared to the serverless microVM compute type: the instances run in your account and VPC, your agents run with the permissions of the runtime execution role, and the data on them stays in your account. This topic describes the security model for Instances, the permissions involved, and the practices you should follow for multi-tenant deployments.

This topic complements the Runtime-wide guidance in [Security best practices for AgentCore Runtime](runtime-security-best-practices.md). The practices there — IAM least privilege, authentication, encryption, network security, and auditing — apply to Instances as well. For how the EBS volumes attached to your sessions are encrypted, see [Encryption at rest for Runtime Instances](runtime-instances-encryption.md).

**Topics**
+ [Security model](#runtime-instances-security-model)
+ [Required permissions](#runtime-instances-security-permissions)
+ [Session routing and multi-tenant isolation](#runtime-instances-session-routing)
+ [Auditing and monitoring](#runtime-instances-monitoring)
+ [Best practices](#runtime-instances-security-best-practices)

## Security model
<a name="runtime-instances-security-model"></a>
+  **The instance is in your account** — EC2 instances launched by a capacity provider run in your account and VPC as [Amazon EC2 managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html). You can inspect them, apply your own controls, and audit their activity through CloudTrail and VPC Flow Logs in your account.
+  **Agents on an instance are not isolated from each other** — Multiple agents can run on the same instance and share its filesystem. Agents run on the instance either in containers or, for directly deployed agents, as processes directly on the instance — neither provides a security boundary between workloads on the same instance. All agents that share an instance must be mutually trusted.
+  **The session is the isolation unit** — A session, identified by the combination of capacity provider and session ID, maps to one EC2 instance (1:1). The same session ID under two different capacity providers refers to two different sessions on two different instances. Agents that you intend to keep isolated from one another should not share a session.
+  **Credential vending** — AgentCore vends execution role credentials to the agents running on the instance and refreshes them periodically. Any code running on the instance can read the credentials available to it. Scope each runtime’s execution role to the least privilege its agent requires. For more information, see [Credentials Management](security-credentials-management.md).
+  **Your account controls apply** — Because the instances run in your account, your AWS Organizations service control policies (SCPs), permission boundaries, and VPC controls govern actions taken in your account. AgentCore acts through the infrastructure role you provide or approve; scope it with IAM conditions (for example, to specific VPCs, subnets, or instance types). The exception is the AgentCore service-linked role used to delete and clean up resources, which is not restricted by SCPs — consistent with how AWS treats service-linked roles generally.
+  **Data residency** — Agents run in the VPC, subnets, account, and Region you specify, and session data and EBS volumes remain in your account.

## Required permissions
<a name="runtime-instances-security-permissions"></a>

Hosting agents on Instances involves the following roles, in addition to the agent runtime execution role that grants your agent code its runtime permissions.
+  **Instance profile** — Attached to the EC2 instance. AgentCore uses it to collect system logs from the instance; it does not grant permissions to your agent code (the agent runtime execution role does that).
+  **Infrastructure role** — AgentCore assumes this role to provision and manage EC2 instances in your account on your behalf — launching, tagging, and configuring networking for instances and their network interfaces. Because this role grants AgentCore permission to manage compute in your account, scope it to the least privilege your workloads require, and use IAM conditions to restrict it to specific VPCs, subnets, or instance types where appropriate.

For the role configuration steps, see [Get started with Instances](runtime-instances-getting-started.md).

## Session routing and multi-tenant isolation
<a name="runtime-instances-session-routing"></a>

AgentCore Runtime authorizes invocations against the agent runtime resource ARN, not against individual sessions.

When you invoke an agent, you supply a `runtimeSessionId`, and AgentCore validates the format of that session ID but does not verify that it belongs to the calling identity. This has an important consequence for multi-tenant deployments:

**Important**  
In deployments where a single IAM principal invokes on behalf of multiple end users, the platform does not enforce that a `sessionId` belongs to the calling user. You are responsible for ensuring your backend passes the correct `sessionId` per user.

If multiple end users share the same IAM principal (for example, a single backend execution role that calls `InvokeAgentRuntime` for all users) and your backend does not bind sessions to users, an authenticated user can supply another user’s session ID and route a request into that user’s session. The following practices mitigate this.

### Enforce session-to-user binding in your backend
<a name="runtime-instances-app-level-binding"></a>

Implement application-level session-to-user binding in your backend. Maintain the mapping between each end user and their session IDs in your application, and ensure that a request for one user can never be issued with another user’s `runtimeSessionId`. Treat the `runtimeSessionId` as a server-side value derived from the authenticated end user — never accept it directly from untrusted client input. For shared-principal, multi-tenant deployments, application-level binding in your backend is the control that prevents one user from routing a request into another user’s session.

### Use distinct IAM principals for high-security multi-tenant deployments
<a name="runtime-instances-per-user-principals"></a>

For high-security multi-tenant deployments, use distinct IAM principals per end user (or per tenant group) to invoke agents, rather than a single shared principal. When each user or tenant invokes through its own principal, IAM itself enforces session scoping: a principal can only invoke runtimes its policy allows, which removes the shared-principal class of session-routing risk. This is the strongest control and is recommended whenever the deployment can support per-user or per-tenant principals.

## Auditing and monitoring
<a name="runtime-instances-monitoring"></a>

Use auditing to detect session-routing reconnaissance and anomalous access:
+  **Correlate principal and session ID** — AWS CloudTrail records both the authenticated principal and the target `sessionId` in the same `InvokeAgentRuntime` event. Use this to detect a principal routing to a session that was created by a different principal.
+  **Apply the Runtime-wide auditing practices** — Enable CloudTrail and VPC Flow Logs, correlate logs using request IDs, and set up metric filters and alarms as described in [Auditing and monitoring](runtime-security-best-practices.md#security-bp-auditing).

## Best practices
<a name="runtime-instances-security-best-practices"></a>
+  **Separate workloads by trust level** — Use different sessions for workloads that are not mutually trusted. Do not co-locate untrusted agents on the same session.
+  **Apply least privilege to every role** — Scope the agent runtime execution role and the infrastructure role to only the actions and resources each one needs.
+  **Bind sessions to users in your backend** — For any deployment where one principal serves multiple end users, enforce session-to-user binding in your application layer.
+  **Prefer per-user or per-tenant principals** — Where feasible, invoke through distinct IAM principals so IAM enforces session scoping.
+  **Monitor for cross-principal routing** — Use CloudTrail to detect routing anomalies, such as a principal routing to a session created by a different principal.

For Runtime-wide security guidance that also applies to Instances, see [Security best practices for AgentCore Runtime](runtime-security-best-practices.md).