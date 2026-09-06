

# AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns
<a name="agentperf05-bp04"></a>

 Smooth agent-to-agent transitions make multi-agent workflows feel like a single cohesive experience, where the receiving agent picks up exactly where the delegating agent left off. Delegation and handoff both require efficient context transfer. The receiving agent needs enough context to act, but transferring too much wastes time and tokens. 

 **Desired outcome:** 
+  You have agent delegation and handoff operations that complete with minimal latency, transferring precisely the context needed by the receiving agent. 
+  You have receiving agents that begin productive processing immediately without re-deriving context the delegating agent already possessed. 
+  You have standardized context transfer mechanisms that let any agent delegate to or receive handoffs from any other agent. 
+  You have handoff latency measured and optimized as part of the overall workflow performance budget. 

 **Common anti-patterns:** 
+  Transferring the entire conversation history and all accumulated context during every delegation, regardless of what the receiving agent actually needs, wasting serialization time and context window capacity. 
+  Requiring receiving agents to re-derive context (re-query databases, re-retrieve documents) that the delegating agent already had, duplicating work and adding latency. 
+  Implementing delegation as synchronous blocking calls where the parent agent waits idle for the child agent to complete, wasting the parent's compute resources. 

 **Benefits of establishing this best practice:** 
+  Selective context transfer and shared context stores reduce delegation latency. 
+  Receiving agents reuse context already gathered by delegating agents instead of repeating the work. 
+  Asynchronous delegation patterns improve parent agent throughput. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement a shared context store using [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) where delegating agents write context and receiving agents read it, avoiding the need to serialize and transfer large context payloads through the orchestration layer. Context transfer schemas define the minimum context required for each delegation type, a data validation agent needs the data and validation rules, not the full conversation history. For agents built with Strands Agents, the built-in agent-as-tool pattern automatically inherits relevant context from the parent agent's session. 

 For handoff patterns in conversational agents, context summarization compresses the conversation into a concise handoff summary tailored to the receiving agent's role, rather than transferring raw conversation history. For predictable delegation patterns, for example, a triage agent that consistently delegates to one of several specialist agents, pre-warming through [AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools on AgentCore Runtime removes cold-start latency from the receiving side. Asynchronous delegation lets the parent agent continue processing other tasks while the child agent works, using callbacks or [Amazon EventBridge](https://aws.amazon.com/eventbridge/) notifications to receive results. 

 [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) standardizes delegation interfaces, letting any agent delegate to any other agent through a consistent API that handles context transfer, authentication, and result delivery. Handoff latency belongs in agent performance dashboards as a distinct metric, measured from delegation initiation to the receiving agent's first productive action. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify delegation and handoff patterns in existing multi-agent workflows and measure current transition latency:** Map delegation and handoff points and measure the current transition latency so optimization targets are grounded in data. 

1.  **Implement shared context stores using AgentCore Memory or DynamoDB for context transfer between agents:** Use [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) so delegating agents write context once and receiving agents read it without serializing large payloads. 

1.  **Define minimum context schemas for each delegation type, specifying exactly what the receiving agent needs:** Keep the delegation payload small and purpose-specific so receivers only get the context required for their role. 

1.  **Implement context summarization for conversational handoffs that compresses history into role-appropriate summaries:** Summarize raw conversation history into a handoff summary tailored to the receiving agent's role rather than forwarding the full transcript. 

1.  **Configure pre-warming for predictable delegation patterns using provisioned concurrency or warm session pools:** For recurring delegation targets, use [AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools on AgentCore Runtime to remove cold-start latency. 

1.  **Convert synchronous delegations to asynchronous patterns with callback-based result delivery:** Let the parent agent continue other work while the child agent runs, receiving results through callbacks or EventBridge notifications. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF05-BP01 Design efficient workflow orchestration patterns](agentperf05-bp01.html) 
+  [AGENTPERF05-BP02 Implement optimized multi-agent collaboration models](agentperf05-bp02.html) 
+  [AGENTPERF04-BP01 Optimize asynchronous message handling patterns](agentperf04-bp01.html) 

 **Related documents:** 
+  [Blog: Multi-agent collaboration patterns with Strands Agents and Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/) 
+  [Agentic AI patterns and workflows on AWS, Multi-agent collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html) 
+  [Operationalizing agentic AI on AWS, Design for composability and collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 

 **Related videos:** 
+  [AgentCore Memory: Episodic Memory & Patterns](https://www.youtube.com/watch?v=1EEIGsKIjGA) 

 **Related examples:** 
+  [GitHub: Guidance for multi-agent orchestration using Bedrock AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws) 
+  [GitHub: Amazon Bedrock AgentCore samples, Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 