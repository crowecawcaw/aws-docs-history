

# AGENTREL06-BP04 Implement idempotent task execution patterns
<a name="agentrel06-bp04"></a>

 Retry is the most common recovery mechanism, and without idempotency it can produce duplicate side effects. Deterministic idempotency keys and conditional writes let operations be retried safely without producing duplicate side effects. 

 **Desired outcome:** 
+  You generate deterministic idempotency keys from operation inputs, so retries of the same logical operation always produce the same key. 
+  You check for an existing result before executing any side-effectful operation and return the cached result if the operation already succeeded. 
+  You propagate idempotency keys through multi-step workflows and to external systems that support built-in idempotency. 

 **Common anti-patterns:** 
+  Implementing retries without idempotency guarantees, producing duplicate side effects when operations are retried after partial completion. 
+  Using non-deterministic identifiers for idempotency keys, so retries of the same operation generate different keys and defeat the guarantee. 
+  Failing to propagate idempotency keys through multi-step workflows, allowing duplicate effects at steps that don't receive the original key. 

 **Benefits of establishing this best practice:** 
+  Retry-based recovery from transient failures becomes safe without duplicate side effects. 
+  Error handling simplifies because first-attempt and retry executions look identical. 
+  Multi-step workflows recover reliably because idempotency keys flow through every step. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Idempotency key generation is where most teams go wrong. Non-deterministic keys (timestamps and UUIDs generated at retry time) defeat the mechanism because the retry computes a different key from the original attempt. Deterministic keys derived from operation inputs work. Hash the workflow ID, task type, and request body, and the same logical operation always produces the same key. This is the single most important detail to get right because everything else depends on it. 

 Once the key is stable, the pre-execution check becomes trivial. Before executing an operation with side effects, query the idempotency store for an existing result keyed on the same identifier. If you find one and it succeeded, return the cached result without re-executing. If you don't, run the operation and record the result. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) with conditional writes makes this safe under concurrency. Two parallel retries can't both create a record, and TTL-based expiration keeps the store from growing without bound while maintaining the guarantee within the expected retry window. 

 Propagation extends the guarantee across workflows. When an orchestrator delegates a subtask, include the parent workflow's key or a deterministic derivative so downstream agents maintain idempotency through every step. For operations interacting with external systems that support built-in idempotency mechanisms, pass the agent's key to the external system. Monitor idempotency store health through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), tracking cache hit rates. Retries that return cached results are the signal the mechanism is working as intended. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Design deterministic idempotency keys:** Derive keys from operation inputs through consistent hashing so retries generate the same key as the original attempt. 

1.  **Implement idempotency checking as a pre-execution step:** Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) with conditional writes and TTL-based expiration to store idempotency records safely. 

1.  **Propagate idempotency keys through multi-step workflows:** Maintain idempotency across all steps by passing the parent workflow's key or a deterministic derivative to downstream steps. 

1.  **Pass keys to external systems with built-in idempotency:** Prevent duplicate processing at the external system level by forwarding the agent's key. 

1.  **Monitor cache hit rates:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to watch for retries that return cached results, confirming the mechanism is operating. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems](agentrel06-bp01.html) 
+  [AGENTREL06-BP03 Regularly test degraded system performance](agentrel06-bp03.html) 
+  [AGENTREL06-BP05 Implement dynamic capability toggling](agentrel06-bp05.html) 

 **Related documents:** 
+  [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 