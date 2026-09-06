

# AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies
<a name="agentsus02-bp03"></a>

 Agent workloads have a shape that general-purpose infrastructure defaults don't fit, with bursty inference, variable-length tool execution, and unpredictable multi-step reasoning. Sizing hosting, network, and storage to the observed pattern rather than a theoretical maximum keeps infrastructure proportional to agentic work. 

 **Desired outcome:** 
+  Agent processes run on serverless infrastructure that scales with demand instead of static provisioning for peak load. 
+  Private connectivity is used where security or latency requirements justify it, not by default for every workload. 
+  Agent infrastructure is deployed close to the services it depends on, so cross-Region data transfer is minimized. 
+  Streaming responses are used for user-facing interactions to reduce memory footprint and improve time-to-first-token. 
+  Utilization is monitored continually and provisioning tracks actual workload demand. 

 **Common anti-patterns:** 
+  Applying general-purpose infrastructure configurations without analyzing the bursty inference call patterns and variable tool execution durations specific to agent workloads, producing wasteful over-allocation or performance-degrading under-provisioning. 
+  Maintaining static provisioning regardless of demand, reducing the ability for infrastructure to contract during low-activity periods. 
+  Sizing for theoretical maximum scenarios instead of right-sizing against actual demand, producing low utilization during normal operations. 
+  Deploying agent infrastructure far from the services it depends on, producing cross-Region network traffic that adds latency and transfer cost. 

 **Benefits of establishing this best practice:** 
+  Infrastructure consumption tracks demand, contracting when agents are idle and expanding during peak periods. 
+  Energy consumption stays proportional to the work agents deliver rather than their theoretical peak capacity. 
+  Private connectivity and Region colocation reduce network path length and latency where it matters. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Running agents on serverless infrastructure solves most of the static-provisioning problem by design. [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) right-sizes compute per invocation with session-isolated execution, so the orchestration overhead is scoped to the session that's actually running. There's no fleet of idle EC2 instances to size against worst-case demand, because the execution unit is the invocation rather than the instance. This default makes bursty workloads affordable. 

 Private networking is about matching the connection pattern to the workload's actual needs. Some agents process sensitive data or have latency requirements tight enough that public internet routing is the bottleneck. For those workloads, [VPC interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) establishes private paths that reduce latency and keep traffic off the public internet. For workloads without those requirements, PrivateLink adds operational complexity without proportional benefit. Default to the public endpoint and promote workloads to PrivateLink when security or latency demands it. 

 Deploying agent infrastructure in the same AWS Region as frequently accessed Amazon Bedrock endpoints and AgentCore services reduces cross-Region data transfer overhead that compounds across thousands of daily invocations. For availability, [Amazon Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) distributes foundation model requests across Regions. This is complementary rather than contradictory. Use cross-Region inference for failover and burst capacity, and keep the primary data path local. 

 Streaming responses change the memory profile of user-facing interactions. Without streaming, the agent accumulates the full response in memory before returning it, which means peak memory is proportional to response length. With streaming, tokens flow as they're generated and memory stays bounded. Turning on streaming in AgentCore reduces footprint for long-form interactions and improves time-to-first-token for users. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes the utilization data that keeps provisioning tied to actual workload demand. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Run agent processes on serverless runtime:** Deploy to [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) for automatic scaling and session isolation, so execution capacity scales with demand rather than peak estimates. 

1.  **Apply private connectivity where justified:** Configure [VPC interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) for workloads with security or latency requirements that warrant it. Default to public endpoints otherwise. 

1.  **Deploy in the same Region as dependencies:** Place agent infrastructure in the Region hosting the Amazon Bedrock endpoints and AgentCore services it uses most, and turn on [Amazon Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability. 

1.  **Enable streaming for user-facing responses:** Turn on AgentCore streaming so response tokens flow as they're generated, reducing memory footprint and improving time-to-first-token. 

1.  **Validate utilization continually:** Track infrastructure utilization through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust provisioning where observed demand is meaningfully below allocation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSUS02-BP01 Optimize context management and memory utilization](agentsus02-bp01.html) 
+  [AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads](agentsus02-bp04.html) 
+  [SUS02-BP01 Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) 
+  [VPC interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) 
+  [Amazon Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 