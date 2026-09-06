

# Secure agent memory and state
<a name="agentsec01"></a>

 One reason agentic AI is effective is the ability to perform long-running tasks. To achieve a goal, agents need to store context, tasks, and results. Agent memory systems can be targeted to introduce false information or influence agent decisions, so securing memory and state helps maintain agent integrity. 


|  AGENTSEC01: How do you secure agentic memory and securely manage state between agents?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent"></a>
+  Agent memory is partitioned along the isolation axes that matter for the workload, with each principal restricted to the namespaces its task requires. 
+  Tamper detection runs on every memory read, and an append-only versioned history supports forensic replay when a poisoning attempt is suspected. 
+  Every write path into memory, including user inputs, tool outputs, inter-agent messages, and consolidation, passes through a layered validation pipeline before data reaches the store. 
+  Hallucinations are detected and contained before they cascade across sessions or propagate to downstream agents in a multi-agent workflow. 
+  Memory operations are monitored continually, and anomalous access or injection signals are routed to the incident response pipeline for review. 

## Maturity levels
<a name="maturity-levels"></a>

 These levels summarize what each stage of maturity looks like for secure agent memory and state as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Memory is shared across agents, users, or sessions with no namespace partitioning, stored without encryption, and written without validation. Hallucinations propagate unchecked, cross-session contamination is indistinguishable from normal operation, and there is no tamper detection on reads.  | 
|  2  |  Emerging  |  Memory is partitioned per session or per user with basic identity and access management (IAM) scoping on the store, and encryption at rest is turned on. Syntactic validation checks types, lengths, and formats before memory writes, and memory events flow to centralized logs. Detection is largely reactive and depends on human review.  | 
|  3  |  Defined  |  Memory resources use hierarchical namespace schemas, for example [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) with per-actor and per-session placeholders, to partition data automatically. Multi-layer validation combines schema checks with [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) for policy enforcement and personally identifiable information (PII) filtering, and [contextual grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) run on high-stakes outputs before consolidation.  | 
|  4  |  Proactive  |  Cryptographic integrity verification using HMAC signatures backed by [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) runs on every memory read. All write paths share the same validation pipeline, including tool outputs and inter-agent messages. Anomaly detection in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms on unusual access patterns, and a hallucination circuit breaker broadcasts through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to quarantine affected entries across downstream agents.  | 
|  5  |  Optimized  |  Memory architecture is validated through routine red-team exercises that simulate poisoning and propagation. Validation policies and grounding thresholds adapt based on observed patterns, and detection signals feed directly into automated containment. Memory governance is codified and auditable.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for"></a>
+  Shared namespaces treated as the default rather than an explicit design decision, so one affected session can read or overwrite context that belongs to a different user or tenant. 
+  Validation applied only at the public API boundary, whereas tool outputs, inter-agent messages, and consolidation writes bypass the pipeline. This creates a blind spot for content that originates inside the agent system. 
+  Model outputs written directly into long-term memory without grounding checks, so hallucinated facts persist across sessions and compound because each agent builds its reasoning chain on fabricated context from earlier runs. 
+  Monitoring that captures memory events but routes no signals into alerts or incident response, so poisoning and propagation are discovered only during post-incident review. 
+  Memory access policies that are set once at deployment and never revisited, so permissions drift as the agent system evolves and the least-privilege posture decays over time. 

**Topics**
+ [Capability intent](#capability-intent)
+ [Maturity levels](#maturity-levels)
+ [Common issues to watch for](#common-issues-to-watch-for)
+ [AGENTSEC01-BP01 Implement memory isolation and integrity controls](agentsec01-bp01.md)
+ [AGENTSEC01-BP02 Validate and sanitize memory inputs](agentsec01-bp02.md)
+ [AGENTSEC01-BP03 Monitor for hallucination propagation](agentsec01-bp03.md)