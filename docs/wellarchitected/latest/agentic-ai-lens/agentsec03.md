

# Agent identity and permission management
<a name="agentsec03"></a>

 Agents access resources, invoke tools, and interact with other services in two patterns: 
+  Explicitly on behalf of a user, where a human initiated the request and the agent's actions must be bounded by that user's permissions 
+  Autonomously, where the agent acts without a user in the loop (triggered by a schedule, an event, an alarm, or another agent) 

 Identity and permission management needs to handle both. Without it, agent permissions can lead to unauthorized access to resources and data. To maintain security boundaries, apply least-privilege principles, separate agent and human permissions, and set up strong authentication for agent identities. 


|  AGENTSEC03: How do you manage agent identities, permissions, and prevent privilege escalation?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-2"></a>
+  Every agent-to-agent and agent-to-service communication authenticates through verifiable mechanisms, whether that is certificate-based mutual TLS, signed OAuth tokens, or platform-managed workload identity. 
+  Agents operate under service identities that are distinct from human identities, and audit trails attribute every action unambiguously to either an agent or a human actor. 
+  When an agent acts on behalf of a user, the user context propagates as signed token claims through the call chain without the agent ever assuming the user's credentials. 
+  Agents run with the minimum permissions their task requires, through short-lived credentials, permission boundaries, and IAM Conditions. 
+  Permission posture is continually validated, with automated drift detection, unused-access findings, and documented periodic reviews keeping privilege aligned with actual usage. 

## Maturity levels
<a name="maturity-levels-2"></a>

 These levels summarize what each stage of maturity looks like for agent identity and permission management as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agents authenticate with shared API keys or static tokens, and some roles are reused across agents and human users. Permissions are broad, credentials are long-lived, and audit trails don't clearly distinguish agent actions from human actions. There is no permission boundary, no revocation path, and no review cadence.  | 
|  2  |  Emerging  |  Each agent has a dedicated [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) role with a consistent naming and tagging convention. Certificates from [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) are used where mutual TLS is required, credentials rotate through [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), and [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) logs agent activity separately from human activity. Initial least-privilege policies are in place, although drift is common.  | 
|  3  |  Defined  |  [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) centralizes agent workload identities, token issuance, and the token vault, with customer-managed [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) keys protecting secrets. Human operators access AWS through [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html), and Service Control Policies (SCPs) in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) help prevent agents from assuming human roles. [AWS STS AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) issues short-lived credentials with session policies, and [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) provides baseline findings.  | 
|  4  |  Proactive  |  When an agent acts on behalf of a user, [GetWorkloadAccessTokenForJWT](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetWorkloadAccessTokenForJWT.html) embeds user context as claims so that downstream services enforce user-level authorization without the agent holding the user's credentials. [IAM permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) cap every agent role, [IAM Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) restrict access by region, tag, time window, and source VPC, and just-in-time elevation with automatic revocation handles high-privilege operations. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) alert on policy changes in near real time.  | 
|  5  |  Optimized  |  Identity and permission governance is fully codified, with continuously validated least-privilege baselines derived from CloudTrail data and aggregated findings in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Unused-access and unusual-authentication findings feed automated remediation. Access reviews run on a cadence that matches the customer's risk profile, with timestamped, documented sign-off, and identity controls are validated through red-team exercises against impersonation and privilege-escalation paths.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-2"></a>
+  Shared API keys or static tokens left in use for agent authentication, with no rotation cadence or revocation path defined. The credential becomes a long-lived secret distributed across environments, and any disclosure exposes every agent that holds it until each one is rotated. 
+  Agent roles and human roles blurred at the edges, whether through role reuse, role chaining, or missing trust-policy and SCP guardrails, so audit trails can't cleanly distinguish agent actions from human actions during incident investigation. 
+  Agent permissions expanded reactively in response to access-denied errors without investigating whether the access pattern is consistent with the agent's intended scope, leading to steady privilege creep that no single review catches and that pushes agent roles toward the broad permission posture autonomous agents should not have. 
+  Access reviews for agent identities conducted on a cadence inherited from human-user reviews (annual or post-incident), even though agent permissions can drift much faster as new tools, prompts, and orchestration patterns are added, so reviewers can't distinguish permissions that are genuinely unused from permissions held for upcoming agent capability changes. 
+  Delegated access implemented by having the agent assume a user's role rather than carrying user context as signed token claims, which collapses the audit trail and gives the agent the user's full permission set for the duration of the session. 

**Topics**
+ [Capability intent](#capability-intent-2)
+ [Maturity levels](#maturity-levels-2)
+ [Common issues to watch for](#common-issues-to-watch-for-2)
+ [AGENTSEC03-BP01 Implement strong authentication for agent identities](agentsec03-bp01.md)
+ [AGENTSEC03-BP02 Separate agent and human user permission](agentsec03-bp02.md)
+ [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.md)
+ [AGENTSEC03-BP04 Regular permission audits and access reviews](agentsec03-bp04.md)