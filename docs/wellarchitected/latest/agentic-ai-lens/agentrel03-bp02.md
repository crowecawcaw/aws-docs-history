

# AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover
<a name="agentrel03-bp02"></a>

 Memory failures don't need to mean agent failures. With redundancy, fallback paths, and a discipline of testing failover under controlled conditions, an agent keeps serving reduced-capability responses until its primary stores recover instead of becoming completely unavailable. 

 **Desired outcome:** 
+  You have primary memory infrastructure with built-in durability and availability, backed by explicit fallback stores for degraded operation. 
+  You have fail-fast logic on memory access that routes to fallback when primary stores are unavailable. 
+  You exercise failover regularly in non-production environments to validate degraded-mode behavior. 

 **Common anti-patterns:** 
+  Running memory stores as single points of failure without replication or failover, causing complete memory loss during outages. 
+  Leaving failover manual, so recovery waits on operators and extends agent downtime. 
+  Skipping failover testing, discovering the gaps only when production incidents force the issue. 

 **Benefits of establishing this best practice:** 
+  Downtime drops because automated failover takes over before operators can intervene. 
+  Agents keep behaving consistently during memory store failures through graceful degradation. 
+  Memory replication across Availability Zones helps protect against data loss. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides managed memory infrastructure with built-in durability and availability, so the default path is already fault-tolerant. The design work is on the degraded path: what does the agent do when even the managed store is briefly unreachable, or when a custom store sits alongside it? Fail-fast logic on memory access is the first answer. When a store shows elevated error rates, the caller stops waiting and routes to a fallback. For short-term memory, that fallback is an in-process cache. For long-term memory, it is a read-through cache of frequently accessed items. 

 For agents running on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's managed session storage persists filesystem-level state across stop and resume cycles. For workflow-stage-aware checkpointing with redrive from specific failure points, use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or framework-level orchestration such as LangGraph with AgentCore Memory. The choice depends on how granular the recovery needs to be. Step Functions gives you durability for each step, while managed session storage gives you whole-agent durability at session boundaries. 

 Regular testing validates that failover mechanisms work as designed. [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) simulates memory store failures in non-production environments so you can validate that failover mechanisms activate correctly and agents continue operating in degraded mode. Document expected behavior for each failure scenario and compare observed behavior against the expectations every time you run the test. Drift between what you expect and what actually happens is the signal that a regression slipped in. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use AgentCore Memory as the primary managed store:** Default to [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for its built-in durability and availability. 

1.  **Implement fail-fast logic for memory access:** Detect elevated error rates on memory calls and route to fallback stores. 

1.  **Maintain in-process fallback caches for short-term memory:** Keep current sessions moving through a last-resort cache that lets the task complete. 

1.  **Implement read-through caching for long-term memory:** Serve cached copies of frequently accessed items during temporary unavailability. 

1.  **Test failover with AWS Fault Injection Service:** Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to validate degraded-mode behavior against documented expectations on a regular schedule. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL01-BP02 Establish modular, fault-isolated layers](agentrel01-bp02.html) 
+  [AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories](agentrel03-bp01.html) 
+  [AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery](agentrel03-bp03.html) 
+  [AGENTREL03-BP04 Implement graceful degradation for memory and state operations](agentrel03-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) 
+  [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 