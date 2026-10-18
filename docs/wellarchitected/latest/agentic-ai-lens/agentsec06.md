

# Secure multi-agent orchestration
<a name="agentsec06"></a>

 Multi-agent systems introduce coordination challenges that don't exist in single-agent architectures. Agents need to discover peers, share capabilities, delegate tasks, and exchange context across trust boundaries. Without proper identity verification and communication security, agent impersonation and message tampering can affect entire multi-agent workflows. Standardized protocols like Agent-to-Agent (A2A) and Model Context Protocol (MCP) provide interoperability across frameworks, but organizations must layer security controls on top of these protocols to maintain trust boundaries. 


|  AGENTSEC06: How do you secure multi-agent orchestration and coordination?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-5"></a>
+  Agents are segmented into trust zones based on role, capability, and risk profile, and inter-zone communication flows only along documented paths enforced at both the network and the application layer. 
+  Inter-agent messages that cross trust boundaries or traverse intermediary services are signed and encrypted at the message level, so payload integrity persists beyond the transport. 
+  Orchestration layers enforce schema validation, scoped IAM permissions, and circuit breakers, so a failure in one agent can't cascade through the workflow or divert it onto unexpected execution paths. 
+  Coordination patterns are monitored continually against established baselines, so deviations are detected proactively rather than discovered after the fact. 
+  Every coordination step is attributable to a verified agent identity and recorded for investigation. This includes agent card discovery (the [A2A protocol](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) mechanism by which one agent locates a peer and reads a JSON agent card describing its name, capabilities, supported skills, and authentication requirements), task delegation, and result collection. 

## Common issues to watch for
<a name="common-issues-to-watch-for-5"></a>
+  Multi-agent systems are deployed as a single trust zone, so an issue with any one agent can spread laterally across the entire network before the scope is understood. 
+  Teams rely on transport-level encryption for inter-agent traffic and treat message-level signing as unnecessary, which means messages sitting in queues or event buses can't be verified at consumption time. 
+  Orchestrator IAM permissions authorize any principal to start, stop, or modify any workflow in the account, rather than scoping access to the specific state machines each principal needs. 
+  Monitoring covers infrastructure metrics and individual agent health but ignores coordination metrics, so inter-agent message rate spikes, unexpected communication paths, and topology changes go undetected. 
+  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) findings and coordination logs are treated as separate data streams, leaving investigators without the context to tie an API anomaly to the specific multi-agent workflow it affected. 

**Topics**
+ [Capability intent](#capability-intent-5)
+ [Common issues to watch for](#common-issues-to-watch-for-5)
+ [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.md)
+ [AGENTSEC06-BP02 Implement workflow orchestration security controls](agentsec06-bp02.md)
+ [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.md)
+ [AGENTSEC06-BP04 Monitor and detect coordination anomalies](agentsec06-bp04.md)