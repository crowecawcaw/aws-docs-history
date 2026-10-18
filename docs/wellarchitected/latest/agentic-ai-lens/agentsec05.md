

# Agent observability and non-repudiation
<a name="agentsec05"></a>

 Without proper logging and traceability, agent actions can't be investigated or attributed. Agents operate autonomously across multiple services, tools, and data sources, generating complex interaction chains that are difficult to reconstruct after the fact. Observability through logging, distributed tracing, and decision artifact storage supports security investigations, compliance reporting, and continuous improvement of agent behavior. 

 Two decisions drive this question. First, what record of agent behavior you keep, where it lives, and how it is protected against tampering by the agent itself. Second, how you follow a single request across agents, tools, and asynchronous boundaries so that any action can be reconstructed end-to-end. 


|  AGENTSEC05: How do you implement observability and prevent repudiation?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-4"></a>
+  Agent decisions, reasoning chains, tool invocations, and intermediate steps are captured to tamper-evident, queryable storage that sits outside the agent's own operational scope. 
+  Every logged action carries the initiating source that caused the agent to act, whether a human user session, an upstream event, a schedule, or another agent, so logged actions can typically be traced back to what triggered them. 
+  A single correlation identifier, independent of the tracing system's trace ID, survives asynchronous boundaries and connects every span, log, and decision artifact generated during a request. 
+  Sensitive fields are masked or redacted before logs reach long-term storage, so completeness of behavioral records doesn't conflict with data protection obligations. 
+  Security investigators can reconstruct the complete chain of agent interactions for past requests, without relying on the agent's own account of its reasoning. 

## Common issues to watch for
<a name="common-issues-to-watch-for-4"></a>
+  Only final outputs are captured, so incident responders can see what the agent did but not why it did it, which is the first question asked in nearly every investigation. 
+  Decision artifacts share the credentials and lifetime of the agent that generated them, which means an affected agent can modify or delete its own record of what happened. 
+  Trace context is re-generated at every asynchronous boundary without a complementary correlation identifier, breaking the chain exactly where investigations need it most. 
+  Sensitive data protection applied at inference time but not at logging time, so prompts and responses containing PII, secrets, or regulated fields end up unmasked in long-term storage. CloudWatch Logs has built-in data protection policies that mask known sensitive types in place. For S3 destinations, masking has to be applied at write time before the object lands in the bucket, and any retroactive remediation requires re-processing existing objects. Plan the masking strategy per destination rather than assuming one control covers both. 
+  Artifacts are retained indefinitely without a queryable index, producing petabytes of S3 objects that are technically complete but practically unsearchable during a time-sensitive incident. 

**Topics**
+ [Capability intent](#capability-intent-4)
+ [Common issues to watch for](#common-issues-to-watch-for-4)
+ [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.md)
+ [AGENTSEC05-BP02 Implement distributed tracing for agent interactions](agentsec05-bp02.md)