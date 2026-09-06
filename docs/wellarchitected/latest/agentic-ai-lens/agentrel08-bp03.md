

# AGENTREL08-BP03 Architect agent systems with resource isolation and contention mitigation
<a name="agentrel08-bp03"></a>

 Shared resource pools let one noisy agent starve the rest. Priority tiers with dedicated resource allocations and contention detection keep user-facing agents responsive even when background workloads spike. 

 **Desired outcome:** 
+  You have separate runtime infrastructure for different agent priority tiers so high-priority agents have dedicated resources. 
+  You track token consumption for each agent and enforce per-agent access to shared model capacity. 
+  You detect contention early through composite signals and activate automated mitigation before failures occur. 

 **Common anti-patterns:** 
+  Sharing resource pools across every agent without isolation, letting high-volume agents consume resources needed by others. 
+  Skipping API quota management, so throttling affects every agent whenever any single agent exceeds quotas. 
+  Treating every agent as equally important, letting background workload spikes degrade user-facing agents. 

 **Benefits of establishing this best practice:** 
+  Performance stays predictable because resource isolation helps prevent cross-workload interference. 
+  Service quality for high-priority agents holds through priority-based resource allocation. 
+  Contention gets detected early through composite monitoring before it becomes a failure. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Isolation starts at the execution surface. Deploy separate [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) instances for different agent priority tiers, so high-priority user-facing agents run on dedicated Runtime instances with their own resource allocations that background agents can't consume. This is the cleanest form of bulkheading for agent workloads, separate pools that physically can't interfere with each other, with no shared scheduler to introduce coupling. 

 Quota protection handles the shared-model case. Amazon Bedrock inference capacity is shared across the account. Track token consumption for each agent through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch alarms to catch individual agents approaching consumption thresholds. [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies control which agents can access which models. Combining policy with Amazon Bedrock service quotas and [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) helps prevent one agent from exhausting shared model capacity. For latency-sensitive agents that need predictable inference performance regardless of overall service demand, Provisioned Throughput gives you fixed model units and the predictable latency that goes with them. 

 With contention detection, you can act before the incident hits. Amazon CloudWatch composite alarms combine multiple resource utilization signals into a contention score. These signals include concurrency utilization, token consumption rates, and queue depths. When the score crosses the threshold, trigger automated mitigation. Use [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to deny tool access for low-priority agents, or activate graceful degradation for non-critical capabilities. Monitor resource utilization across priority tiers through AgentCore Observability dashboards so emerging contention becomes visible before it causes user-visible failures. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy separate AgentCore Runtime instances per priority tier:** Give high-priority user-facing agents dedicated [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) resource allocations. 

1.  **Track per-agent token consumption and enforce access:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to control model access per agent. 

1.  **Use Amazon Bedrock Provisioned Throughput for latency-sensitive agents:** Use [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) for predictable inference performance. 

1.  **Configure composite alarms on resource utilization signals:** Combine concurrency, token consumption, and queue depth signals through Amazon CloudWatch into a contention score. 

1.  **Implement automated contention mitigation:** Deny tool access for low-priority agents through AgentCore Policy when pressure is detected. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL01-BP05 Implement adaptive provisioning](agentrel01-bp05.html) 
+  [AGENTREL08-BP01 Establish consistent configuration management practices](agentrel08-bp01.html) 
+  [AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing](agentrel08-bp02.html) 
+  [AGENTREL08-BP04 Track agent memory utilization metrics](agentrel08-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [Securely launch and scale your agents and tools on Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/) 
+  [Amazon Bedrock Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 