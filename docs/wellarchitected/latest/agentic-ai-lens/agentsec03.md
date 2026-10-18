

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

## Common issues to watch for
<a name="common-issues-to-watch-for-2"></a>
+  Shared API keys or static tokens left in use for agent authentication, with no rotation cadence or revocation path defined. The credential becomes a long-lived secret distributed across environments, and any disclosure exposes every agent that holds it until each one is rotated. 
+  Agent roles and human roles blurred at the edges, whether through role reuse, role chaining, or missing trust-policy and SCP guardrails, so audit trails can't cleanly distinguish agent actions from human actions during incident investigation. 
+  Agent permissions expanded reactively in response to access-denied errors without investigating whether the access pattern is consistent with the agent's intended scope, leading to steady privilege creep that no single review catches and that pushes agent roles toward the broad permission posture autonomous agents should not have. 
+  Access reviews for agent identities conducted on a cadence inherited from human-user reviews (annual or post-incident), even though agent permissions can drift much faster as new tools, prompts, and orchestration patterns are added, so reviewers can't distinguish permissions that are genuinely unused from permissions held for upcoming agent capability changes. 
+  Delegated access implemented by having the agent assume a user's role rather than carrying user context as signed token claims, which collapses the audit trail and gives the agent the user's full permission set for the duration of the session. 

**Topics**
+ [Capability intent](#capability-intent-2)
+ [Common issues to watch for](#common-issues-to-watch-for-2)
+ [AGENTSEC03-BP01 Implement strong authentication for agent identities](agentsec03-bp01.md)
+ [AGENTSEC03-BP02 Separate agent and human user permission](agentsec03-bp02.md)
+ [AGENTSEC03-BP03 Implement least privilege with dynamic boundaries](agentsec03-bp03.md)
+ [AGENTSEC03-BP04 Regular permission audits and access reviews](agentsec03-bp04.md)