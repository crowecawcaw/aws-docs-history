

# AGENTOPS07-BP01 Implement automated response and recovery mechanisms
<a name="agentops07-bp01"></a>

 Agents that recover from failure without human intervention keep service running and give the team the failure data they need to help prevent recurrence. Manual-only recovery scales poorly and can turn routine degradations into incidents. 

 **Desired outcome:** 
+  Agent systems detect and recover from common failure scenarios automatically, maintaining service availability and user experience continuity. 
+  Automatic cutoffs help prevent cascading failures from propagating across the agent environment. 
+  Fallback strategies keep agents degrading gracefully rather than failing completely when primary capabilities are unavailable. 
+  Recovery time objectives are defined, met, and tested regularly. 

 **Common anti-patterns:** 
+  Implementing retry logic without automatic cutoffs, causing agents to repeatedly invoke failing services and amplifying load on degraded systems rather than failing fast. 
+  Designing fallback strategies that silently degrade quality without notifying users, producing a poor experience where users receive low-quality responses without understanding why. 
+  Failing to define recovery time objectives for different failure scenarios, making it impossible to assess whether recovery mechanisms meet operational requirements. 
+  Implementing recovery mechanisms that work in isolation but fail in combination, missing failure scenarios where multiple components degrade simultaneously. 
+  Never testing recovery procedures under realistic failure conditions, discovering problems only during actual production incidents. 

 **Benefits of establishing this best practice:** 
+  Automated recovery captures detailed failure data that drives systematic improvement of agent resilience, letting teams address root causes rather than repeatedly responding to the same incidents. 
+  Self-healing capabilities adapt to different failure contexts, transient tool unavailability, complete service outages, and model degradation, with recovery strategies proportional to severity. 
+  Automatic cutoffs break cascading failures at the source rather than allowing them to propagate. 
+  Chaos engineering exercises validate that recovery works under realistic conditions, not just in theory. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Establish automatic cutoffs for every external dependency. Store state for the cutoff (healthy, degraded, and open) in a fast data store where every agent can read it. Thresholds depend on each dependency's reliability characteristics. Set an error rate threshold (for example, 50% errors in a 60-second window), a timeout threshold (for example, 5 consecutive timeouts), and a recovery probe interval (for example, attempt recovery every 30 seconds). Emit [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics on state transitions so cutoff health becomes visible across the environment. 

 Fallback strategies need to be designed for each capability, not copied from a template. Tool failures get fallback chains: alternative tools with equivalent capabilities, then graceful degradation, and then manual escalation. LLM inference failures get model fallback chains that route to alternative models (Claude 3.5 Sonnet to Claude 3 Haiku, for example) when the primary is unavailable. Multi-agent coordination failures get single-agent fallback modes that handle tasks with reduced capability rather than failing completely. Each fallback should notify users when quality is degraded, not silently return a worse answer. 

 [AWS Step Functions](https://aws.amazon.com/step-functions/) or equivalent durable workflow orchestration handles recovery workflows with built-in error handling, retry logic, and compensating transactions. Health check endpoints for each agent verify dependency availability and report overall health status. 

 Monitoring actual recovery times against objectives tells the team whether the mechanisms actually meet operational requirements. Quarterly chaos engineering exercises validate that recovery works under realistic conditions rather than just in the happy-path scenarios the original design anticipated. For reliability-focused automated recovery with classify-route-escalate patterns, see [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement automatic cutoffs for every external dependency:** Define thresholds for error rate, timeout count, and recovery probing per dependency. 

1.  **Design fallback chains per agent capability:** Specify alternative tools, models, and degraded-mode operations, and notify users when quality is degraded. 

1.  **Build durable recovery workflows:** Use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or equivalent with error handling, retry logic, and compensating transactions. 

1.  **Configure health check endpoints:** Verify dependency availability and report overall health status for each agent. 

1.  **Define RTOs per failure scenario:** Monitor actual recovery times against objectives in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). 

1.  **Run quarterly chaos engineering exercises:** Inject failures in non-production environments to validate recovery mechanisms under realistic conditions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS07-BP03 Augment change management to accommodate technical improvements and business requirements](agentops07-bp03.xml) 
+  [AGENTOPS04-BP03 Develop fallback behavior and error handling for tool invocations](../agentops04/agentops04-bp03.xml) 
+  [AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies](../agentops05/agentops05-bp02.xml) 
+  [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 
+  [Agentic AI in the Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) 
+  [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent) 
+  [Introducing Amazon Bedrock AgentCore: Securely deploy and operate AI agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/) 

 **Related services:** 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 