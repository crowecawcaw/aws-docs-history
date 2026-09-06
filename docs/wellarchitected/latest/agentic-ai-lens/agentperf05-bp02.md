

# AGENTPERF05-BP02 Implement optimized multi-agent collaboration models
<a name="agentperf05-bp02"></a>

 Multi-agent systems typically deliver the strongest results when each collaboration pattern is matched to the task it was designed for (for example, supervisor-worker for structured decomposition, swarm for creative exploration, and pipeline for sequential processing). Before picking any multi-agent pattern, decide whether a capability should be a sub-agent or a tool that a single agent invokes. A tool call completes in milliseconds, while a sub-agent delegation is a full LLM reasoning loop that costs time and tokens. 

 **Desired outcome:** 
+  You have multi-agent workflows that use collaboration models matched to their task characteristics. 
+  You have each capability implemented at the right abstraction level, tool for deterministic single-step operations, sub-agent for tasks that require independent reasoning. 
+  You have coordination overhead minimized through appropriate pattern selection and implementation. 

 **Common anti-patterns:** 
+  Delegating to a sub-agent for capabilities that are deterministic, stateless, and single-step, API calls, database lookups, or format conversions, paying the full cost of an LLM reasoning loop for work that a tool call would handle in milliseconds. 
+  Using a supervisor-worker model for all multi-agent workflows, creating a bottleneck at the supervisor that must process every intermediate result and make every delegation decision. 
+  Deploying swarm patterns without explicit convergence criteria or resource budgets, letting agents continue exploring indefinitely without converging on a shared outcome. 

 **Benefits of establishing this best practice:** 
+  Matching the collaboration model to task structure minimizes coordination overhead. 
+  Appropriate model selection for decomposable tasks maximizes parallelism. 
+  Timeouts and fallback mechanisms keep collaboration resilient when individual agents fail or slow down. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Use a sub-agent when the capability requires its own reasoning (LLM inference for ambiguous inputs or judgment calls), its own context or memory scope, multi-step tool orchestration where sequencing requires reasoning, a different model or prompt, or independent failure isolation. 

 Use a tool when the capability is deterministic, stateless, single-step, and fast (under 2-3 seconds). 

 For borderline cases, start with a tool and promote to a sub-agent only when frequent re-invocation patterns indicate the capability needs its own reasoning loop. 

 Once multi-agent architecture is warranted, select the collaboration model based on task characteristics. Use supervisor-worker when the task has clear decomposition and centralized quality control is needed. Strands Agents's agent-as-tool pattern and Amazon Bedrock Agents' multi-agent collaboration provide supervisor-worker orchestration with automatic context passing and result aggregation. 

 Use pipeline when the task has a natural sequential flow, balance stage durations and use your framework's graph orchestration to chain agents sequentially. 

 Use peer-to-peer or blackboard when multiple agents need to contribute partial solutions asynchronously, implement a shared workspace using AgentCore Memory or DynamoDB with event-driven notifications. 

 Use swarm when the task benefits from parallel exploration and emergent behavior, implement convergence detection and per-swarm token budgets to help prevent unbounded resource consumption. 

 For deterministic delegation logic or durable long-running workflows, [AWS Step Functions](https://aws.amazon.com/step-functions/) remains a strong alternative for orchestrating agent invocations. 

 For all collaboration models, implement timeout and fallback mechanisms that help prevent a single slow or failed agent from blocking the entire workflow. Deploy multi-agent systems on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling and observability, or on Amazon EKS or Amazon ECS for custom container-based deployments. Monitor collaboration overhead metrics including coordination latency, redundant work rate, and throughput per model. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate whether each capability should be a tool or a sub-agent:** Default to tools and promote to sub-agents only when re-invocation patterns indicate the need for independent reasoning. 

1.  **Classify multi-agent workflows by task characteristics:** Assess decomposability, dependency structure, latency requirements, and whether the task benefits from parallel exploration. 

1.  **Select the collaboration model:** Use supervisor-worker for clear decomposition, pipeline for sequential flow, peer-to-peer for shared problem spaces, and swarm for parallel exploration. 

1.  **Implement using your framework's native multi-agent patterns:** Use Strands agent-as-tool, Amazon Bedrock multi-agent collaboration, or an equivalent, and use [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for shared context across agents. 

1.  **Implement timeout and fallback mechanisms for all collaboration models:** Set per-agent timeouts and define fallback behavior so one slow or failed agent can't block the full workflow. 

1.  **Monitor collaboration overhead metrics and optimize model selection over time:** Track coordination latency, redundant work rate, and throughput per model, and re-evaluate the collaboration choice as traffic shifts. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF05-BP01 Design efficient workflow orchestration patterns](agentperf05-bp01.html) 
+  [AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns](agentperf05-bp04.html) 
+  [AGENTPERF04-BP02 Implement efficient protocol-based agent communications](agentperf04-bp02.html) 

 **Related documents:** 
+  [Blog: Multi-agent collaboration patterns with Strands Agents and Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/) 
+  [Blog: Multi-agent collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/) 
+  [Agentic AI patterns and workflows on AWS, Multi-agent collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html) 
+  [Agentic AI patterns and workflows on AWS, Workflow orchestration agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html) 
+  [Use multi-agent collaboration with Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html) 

 **Related videos:** 
+  [Amazon Bedrock Agents and AgentCore Design Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU) 

 **Related examples:** 
+  [GitHub: Bedrock multi-agent collaboration workshop](https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop) 
+  [GitHub: Multi-agent collaboration with Strands](https://github.com/aws-samples/sample-multi-agent-collaboration-with-strands) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 