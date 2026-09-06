

# AGENTREL04-BP03 Implement fallback mechanisms and graceful degradation for collaborative workflows
<a name="agentrel04-bp03"></a>

 One unavailable agent should not take down an entire workflow. Pre-defined fallback chains let orchestrators swap in alternatives, preserving forward progress with reduced quality rather than a complete stall. 

 **Desired outcome:** 
+  You have fallback chains for each critical agent with ordered alternatives and documented quality trade-offs. 
+  You check agent health proactively and skip unavailable agents rather than waiting for timeout. 
+  You communicate degradation to downstream systems through structured events so their behavior can adapt. 

 **Common anti-patterns:** 
+  Designing multi-agent workflows without fallback paths, so one failed agent halts the entire workflow. 
+  Implementing fallbacks that silently degrade quality without telling users or downstream systems. 
+  Skipping fallback testing, discovering gaps only during production incidents. 

 **Benefits of establishing this best practice:** 
+  Partial workflow functionality persists when an individual agent fails. 
+  Transparent degradation reaches users and downstream systems so they can adapt. 
+  Faster workflow completion through pre-defined fallback paths that activate automatically. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Fallback chains give the orchestrator somewhere to go when the preferred agent is down. Each chain is an ordered sequence. First, a secondary agent with equivalent capabilities. Then, a simplified agent with reduced capabilities. Next, a cached result from a previous execution. Finally, a graceful failure response. The ordering matters because it captures the quality trade-off. The first few alternatives preserve most of the functionality, and the later ones accept larger degradation in exchange for keeping the workflow moving at all. Document the quality impact of each level so orchestrators pick the best available option rather than the first technically viable one. 

 Proactive health checking keeps fallback latency low. Without it, the orchestrator waits for the preferred agent to time out before trying the fallback, which stacks agent-level latency penalties on top of the workflow. Check [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics and [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)'s /ping endpoint before invocation. When an agent reports degraded health, skip it and move directly to the next alternative. 

 When a fallback activates, publish a structured degradation event that identifies the failed agent, the activated fallback, and the capability impact. Downstream systems subscribe and adapt by flagging outputs for additional review, displaying degradation notices to users, or routing around the affected workflow entirely. Validate fallback mechanisms through chaos engineering using [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html). Inject agent failures in non-production environments to confirm fallback chains activate correctly and workflows complete with expected degraded outputs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Design fallback chains for each critical agent:** Define an ordered sequence of alternatives with documented quality trade-offs at each level. 

1.  **Implement proactive health checking before invocation:** Check [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics and the [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) /ping endpoint, and skip agents reporting degraded health. 

1.  **Configure fallback transitions in the orchestration layer:** Distinguish transient failures (retry first) from permanent failures (immediate fallback). 

1.  **Publish structured degradation events when fallbacks activate:** Emit events for downstream systems to consume so the rest of the environment can adapt. 

1.  **Validate fallback mechanisms through chaos engineering:** Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to inject agent failures on a regular schedule and confirm the chains still work. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL04-BP01 Implement the arbiter agent pattern for coordinated multi-agent systems](agentrel04-bp01.html) 
+  [AGENTREL04-BP02 Classify agents with a thorough capability taxonomy](agentrel04-bp02.html) 
+  [AGENTREL04-BP04 Implement resilient control planes for agent coordination](agentrel04-bp04.html) 
+  [AGENTREL08-BP03 Architect agent systems with resource isolation and contention mitigation](agentrel08-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 
+  [Multi-agent collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/) 
+  [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 