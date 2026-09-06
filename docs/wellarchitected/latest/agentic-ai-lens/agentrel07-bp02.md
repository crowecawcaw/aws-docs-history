

# AGENTREL07-BP02 Enable automatic recovery from agent execution failures
<a name="agentrel07-bp02"></a>

 Uniform retry wastes effort on non-retryable failures and creates thundering herds on transient ones. Classifying failures by type and applying targeted strategies, retry for transient errors, fallback for persistent ones, escalation for unrecoverable ones, keeps availability high without manual intervention. 

 **Desired outcome:** 
+  You classify agent failures into retryable and non-retryable categories at the point of failure. 
+  You use exponential backoff with full jitter on retryable failures, with failure-type-specific retry counts. 
+  You enforce retry budgets to help prevent retry storms, and escalate to fallback or human review when retries are exhausted. 

 **Common anti-patterns:** 
+  Applying uniform retry logic to every failure type, retrying non-retryable failures that will never succeed. 
+  Retrying at fixed intervals without exponential backoff and jitter, producing thundering-herd effects during recovery. 
+  Implementing only retry-based recovery without fallback strategies for failures that persist after retries. 

 **Benefits of establishing this best practice:** 
+  Availability stays high because transient failures resolve automatically. 
+  Resource utilization is efficient because non-retryable failures don't consume retry budget. 
+  Persistent failures get handled gracefully through fallback strategies when retries are exhausted. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Failure classification comes first because the recovery strategy depends on the category. Retryable failures include transient infrastructure errors, LLM throttling, and temporary unavailability, conditions that a short wait and a retry are likely to resolve. Non-retryable failures include authentication errors, invalid inputs, and permission denials, conditions where the same call will fail the same way no matter how many times you retry. Collapsing the two into a single category means either retrying things that will never succeed or giving up on things that would have worked. 

 Backoff strategy matters as much as classification. Exponential backoff with full jitter spreads retry attempts across time, avoiding the thundering herd that fixed-interval retries produce during widespread failures. Failure-type-specific retry counts help too: aggressive retry for transient errors, conservative retry with longer intervals for rate limiting. Enforce retry budgets at two levels. For each invocation, use [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to cap retries within a single agent execution. This helps prevent runaway loops without external dependencies. Across invocations, implement a shared circuit-breaker backed by a low-latency store (e.g., DynamoDB atomic counters or ElastiCache) that tracks cumulative retry counts across concurrent executions. AgentCore Policy evaluates the circuit-breaker state as a policy input, rejecting new retries when the global budget is exhausted. This two-tier approach avoids the anti-pattern of assuming single-invocation limits provide system-wide protection. 

 Self-healing workflows extend retry into recovery. Common failure patterns have targeted remediations. Automatic prompt refinement handles LLM output validation failures, tool substitution handles tool call failures, and context reconstruction handles memory access failures. When retries are exhausted, transition to fallback strategies or human review rather than terminating. Log every recovery action through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with structured metadata including retry counts, strategy used, and outcome, so recovery effectiveness can be analyzed and tuned. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement failure classification:** Categorize agent failures into retryable and non-retryable types at the point of failure. 

1.  **Configure retry with exponential backoff and full jitter:** Use failure-type-specific retry counts so the strategy matches the failure mode. 

1.  **Enforce retry budgets through AgentCore Policy:** Use [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to help prevent retry storms during widespread failures. 

1.  **Build self-healing workflows for common patterns:** Implement prompt refinement, tool substitution, and context reconstruction as targeted recovery paths. 

1.  **Log recovery actions for analysis:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture retry counts, strategies, and outcomes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL06-BP04 Implement idempotent task execution patterns](agentrel06-bp04.html) 
+  [AGENTREL07-BP01 Design workflows in stages with incremental recovery](agentrel07-bp01.html) 
+  [AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery](agentrel07-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 