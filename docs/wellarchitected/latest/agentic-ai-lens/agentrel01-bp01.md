

# AGENTREL01-BP01 Implement a resilient messaging layer
<a name="agentrel01-bp01"></a>

 Direct agent-to-agent calls couple failure modes. When one agent fails, everything downstream fails with it. A messaging layer with persistence, retry, and dead-letter handling absorbs transient faults and lets workflows resume from where they stopped. 

 **Desired outcome:** 
+  Your agents communicate through an intermediary messaging layer with persistence, retry, and dead-letter handling rather than direct synchronous calls. 
+  You have durable workflow state that survives the restart or loss of any single component. 
+  You can trace every agent message across synchronous and asynchronous boundaries. 

 **Common anti-patterns:** 
+  Wiring agents together through direct synchronous calls, so a single failure cascades through every dependent agent. 
+  Running messaging infrastructure without persistence, making workflow recovery impossible after a component outage. 
+  Treating every interaction as synchronous, creating bottlenecks that block independent agent operation. 

 **Benefits of establishing this best practice:** 
+  Persistence and retry contain transient failures within the messaging layer instead of exposing them as agent outages. 
+  Dead-letter handling helps prevent poison messages from blocking healthy workflow execution. 
+  A durable messaging substrate is the foundation for advanced orchestration patterns including saga and arbiter. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every agent-to-agent call is a coupling decision. Synchronous calls tie the caller's availability to the callee's availability. In a network of agents that multiplies quickly. Five agents with four synchronous dependencies, and the availability product drops below any single agent's SLA. A messaging layer breaks the coupling by buffering the call in durable infrastructure. The caller emits a message and moves on. The receiver processes it on its own schedule, with retries and dead-letter routing handled outside the agent's own code. 

 Pattern selection follows the interaction shape. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) for content-based routing where a single event fans out to multiple consumers, with EventBridge Schema Registry documenting the contract between agents. Use [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) for durable point-to-point delivery with configurable visibility timeouts and dead-letter queues. Use Amazon SNS for fan-out to multiple downstream consumers. 

 Workflow durability ties the messaging layer to business outcomes. A message that reaches its queue still needs orchestration to coordinate multi-step work across agents. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) persists execution state at every step transition, so recovery starts from the last completed step rather than the beginning. Without that persistence, a failure in step five of a seven-step workflow re-executes every prior step, wasting compute and risking duplicate side effects. Dead-letter handling complements durability. Poison messages get isolated for triage rather than blocking healthy traffic behind them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map every agent communication path and classify it:** Document each interaction as synchronous direct communication (A2A), loosely coupled tool invocation (MCP), or asynchronous event-driven through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). 

1.  **Configure EventBridge rules and SQS queues:** Set up Amazon EventBridge content-based routing for event-driven paths and [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) queues for durable point-to-point messaging. 

1.  **Define event schemas in EventBridge Schema Registry:** Register a schema for each agent message type so sender and receiver agree on the contract. 

1.  **Configure dead-letter queues with automated triage:** Route repeatedly failed messages to DLQs and wire Amazon CloudWatch alarms so operators see poison messages before they block traffic. 

1.  **Instrument the messaging layer with AgentCore Observability:** Enable [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) for distributed tracing so you can follow a message across EventBridge, SQS, and agent boundaries. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL01-BP02 Establish modular, fault-isolated layers](agentrel01-bp02.html) 
+  [AGENTREL01-BP03 Design specialized agents following actor model principles](agentrel01-bp03.html) 
+  [AGENTREL01-BP04 Standardize communication protocols](agentrel01-bp04.html) 

 **Related documents:** 
+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) 
+  [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) 
+  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 

 **Related services:** 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 