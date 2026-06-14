# Agent identity and permission management

Agents access resources, invoke tools, and interact with other
services in two patterns:

- Explicitly on behalf of a user, where a human initiated the
  request and the agent's actions must be bounded by that user's
  permissions
- Autonomously, where the agent acts without a user in the loop
  (triggered by a schedule, an event, an alarm, or another
  agent)

Identity and permission management needs to handle both. Without
it, agent permissions can lead to unauthorized access to resources
and data. To maintain security boundaries, apply least-privilege
principles, separate agent and human permissions, and set up
strong authentication for agent identities.

| AGENTSEC03: How do you manage agent identities,<br>permissions, and prevent privilege escalation? |
| ------------------------------------------------------------------------------------------------- |
|                                                                                                   |

## Capability intent

- Every agent-to-agent and agent-to-service communication
  authenticates through verifiable mechanisms, whether that is
  certificate-based mutual TLS, signed OAuth tokens, or
  platform-managed workload identity.
- Agents operate under service identities that are distinct
  from human identities, and audit trails attribute every
  action unambiguously to either an agent or a human actor.
- When an agent acts on behalf of a user, the user context
  propagates as signed token claims through the call chain
  without the agent ever assuming the user's credentials.
- Agents run with the minimum permissions their task requires,
  through short-lived credentials, permission boundaries, and
  IAM Conditions.
- Permission posture is continually validated, with automated
  drift detection, unused-access findings, and documented
  periodic reviews keeping privilege aligned with actual
  usage.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent identity and permission management as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents authenticate with shared API keys or static<br>tokens, and some roles are reused across agents and<br>human users. Permissions are broad, credentials are<br>long-lived, and audit trails don't clearly distinguish<br>agent actions from human actions. There is no permission<br>boundary, no revocation path, and no review cadence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2     | Emerging  | Each agent has a dedicated<br>[AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") role with a<br>consistent naming and tagging convention. Certificates<br>from<br>[AWS Private Certificate Authority](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") are used where<br>mutual TLS is required, credentials rotate through<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), and<br>[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") logs agent activity separately from<br>human activity. Initial least-privilege policies are in<br>place, although drift is common.                                                                                                                                                                                                                                                                                                                                                  |
| 3     | Defined   | [Amazon<br>Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md") centralizes agent<br>workload identities, token issuance, and the token<br>vault, with customer-managed<br>[AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") keys protecting secrets. Human operators<br>access AWS through<br>[AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"), and Service Control Policies<br>(SCPs) in<br>[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") help prevent agents from assuming<br>human roles.<br>[AWS STS AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") issues short-lived credentials<br>with session policies, and<br>[IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") provides baseline findings.                                                  |
| 4     | Proactive | When an agent acts on behalf of a user,<br>[GetWorkloadAccessTokenForJWT](../../../bedrock-agentcore-control/latest/APIReference/API_GetWorkloadAccessTokenForJWT.md "../../../bedrock-agentcore-control/latest/APIReference/API_GetWorkloadAccessTokenForJWT.md")<br>embeds user context as claims so that downstream<br>services enforce user-level authorization without the<br>agent holding the user's credentials.<br>[IAM<br>permission boundaries](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") cap every agent role,<br>[IAM<br>Conditions](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") restrict access by region, tag, time<br>window, and source VPC, and just-in-time elevation with<br>automatic revocation handles high-privilege operations.<br>[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") and<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") alert on policy changes in near real<br>time. |
| 5     | Optimized | Identity and permission governance is fully codified,<br>with continuously validated least-privilege baselines<br>derived from CloudTrail data and aggregated findings in<br>[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md"). Unused-access and<br>unusual-authentication findings feed automated<br>remediation. Access reviews run on a cadence that<br>matches the customer's risk profile, with timestamped,<br>documented sign-off, and identity controls are validated<br>through red-team exercises against impersonation and<br>privilege-escalation paths.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Common issues to watch for

- Shared API keys or static tokens left in use for agent
  authentication, with no rotation cadence or revocation path
  defined. The credential becomes a long-lived secret
  distributed across environments, and any disclosure exposes
  every agent that holds it until each one is rotated.
- Agent roles and human roles blurred at the edges, whether
  through role reuse, role chaining, or missing trust-policy
  and SCP guardrails, so audit trails can't cleanly
  distinguish agent actions from human actions during incident
  investigation.
- Agent permissions expanded reactively in response to
  access-denied errors without investigating whether the
  access pattern is consistent with the agent's intended
  scope, leading to steady privilege creep that no single
  review catches and that pushes agent roles toward the broad
  permission posture autonomous agents should not have.
- Access reviews for agent identities conducted on a cadence
  inherited from human-user reviews (annual or post-incident),
  even though agent permissions can drift much faster as new
  tools, prompts, and orchestration patterns are added, so
  reviewers can't distinguish permissions that are genuinely
  unused from permissions held for upcoming agent capability
  changes.
- Delegated access implemented by having the agent assume a
  user's role rather than carrying user context as signed
  token claims, which collapses the audit trail and gives the
  agent the user's full permission set for the duration of the
  session.

###### Best practices

- [AGENTSEC03-BP01 Implement strong authentication for agent identities](agentsec03-bp01.md "agentsec03-bp01.md")
- [AGENTSEC03-BP02 Separate agent and human user permission](agentsec03-bp02.md "agentsec03-bp02.md")
- [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.md "agentsec03-bp03.md")
- [AGENTSEC03-BP04 Regular permission audits and access reviews](agentsec03-bp04.md "agentsec03-bp04.md")
