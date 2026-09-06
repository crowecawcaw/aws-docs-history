

# AGENTPERF05-BP01 Design efficient workflow orchestration patterns
<a name="agentperf05-bp01"></a>

 Agents that coordinate specialized sub-agents can solve complex tasks faster than any single agent, and the orchestration pattern you choose determines whether that coordination adds milliseconds or seconds. Orchestration patterns range from static workflows (the execution graph is fully defined at design time) to dynamic workflows (the agent's reasoning determines the next step at runtime). Efficient orchestration means decomposing tasks for parallelism, minimizing data passed between steps, and matching the orchestration pattern to the task's dependency structure. 

 **Desired outcome:** 
+  You have multi-agent workflows that execute with minimal orchestration overhead, with independent subtasks running in parallel and dependent tasks executing as soon as prerequisites complete. 
+  You have task routing decisions that are fast and accurate. 
+  You have end-to-end workflow latency that approaches the theoretical minimum defined by the critical path of dependent operations. 

 **Common anti-patterns:** 
+  Running all workflow steps sequentially even when some steps have no data dependencies and could run in parallel, making end-to-end latency equal to the sum of all step durations rather than the critical path. 
+  Using the orchestrator agent as a pass-through for all data between worker agents, creating a serialization bottleneck at every step instead of having workers write results directly to shared storage. 
+  Implementing dynamic graph orchestration without cycle detection or maximum depth limits, allowing LLM-driven routing decisions to produce infinite loops where agents repeatedly invoke each other without converging. 

 **Benefits of establishing this best practice:** 
+  Parallel execution of independent subtasks reduces end-to-end latency. 
+  Managed orchestration with built-in retry and error handling improves reliability. 
+  Scalable orchestration handles dynamic fan-out patterns without code changes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Most agentic workflows are dynamic, meaning that the LLM's reasoning determines which tool or sub-agent to invoke next based on intermediate results. For these workflows, use your agentic framework's built-in orchestration capabilities: 
+  Strands Agents provides graph-based orchestration (GraphBuilder), supervisor patterns, and swarm coordination 
+  LangGraph offers stateful graph workflows 
+  CrewAI provides role-based crew orchestration 

 These framework-driven patterns are the natural fit for agent workloads because the execution path emerges from the model's reasoning rather than being predefined. To keep dynamic orchestration high-performing, implement cycle detection (track visited nodes with input hashing), maximum depth limits (10–15 steps), and bounded fan-out cardinality (5–10 concurrent branches) to help prevent unbounded execution chains. 

 For deterministic workflows where the run graph is fully known at design time, batch processing pipelines, approval workflows, data transformation chains, use [AWS Step Functions](https://aws.amazon.com/step-functions/) with Parallel and Map states to run steps concurrently, Choice states for conditional branching, and built-in Catch and Retry for error handling. Step Functions is also valuable as a hybrid layer that handles durable orchestration and state persistence while invoking LLM-based agents only at decision points that require reasoning. 

 Keep state payloads small by storing large intermediate results in [Amazon S3](https://aws.amazon.com/s3/) or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and passing only references through the orchestration layer. 

 For all orchestration patterns, configure per-step and workflow-level timeouts that help prevent slow agents from blocking the entire workflow. For dynamic graph workflows, allocate per-branch latency budgets derived from the overall task SLO, if a branch exceeds its budget, terminate it and proceed with the best available partial result. Design workflows to maximize parallelism by analyzing task dependencies and executing independent subtasks concurrently. 

 Monitor workflow execution metrics including step duration, parallel efficiency, state payload sizes, and graph depth distribution. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze multi-agent task dependencies and classify each workflow:** Classify each workflow as dynamic graph (LLM-driven routing, most agent workflows), hybrid (deterministic flow with LLM decision points), or static (fully predefined execution graph), and use the classification to drive the orchestration choice. 

1.  **For dynamic graph workflows, use your agentic framework's native orchestration:** Use Strands GraphBuilder, LangGraph, or equivalent with cycle detection, maximum depth limits, and bounded fan-out cardinality to help prevent unbounded execution chains. 

1.  **For static/hybrid workflows, implement using Step Functions with Parallel and Map states:** Use [AWS Step Functions](https://aws.amazon.com/step-functions/) Parallel and Map states to run steps concurrently with built-in retry and error handling on deterministic paths. 

1.  **Implement efficient state passing using S3/DynamoDB references rather than inline payloads:** Keep orchestration payloads small by storing large intermediate results in S3 or DynamoDB and passing only references. 

1.  **Configure per-step and workflow-level timeouts with fallback strategies for slow agents:** Set timeouts at both the step and workflow level, and define fallback behavior so a single slow agent can't stall the whole workflow. 

1.  **Monitor workflow execution metrics: step duration, parallel efficiency, state payload sizes, and graph depth distribution:** Publish these metrics to CloudWatch so orchestration performance can be tuned from data rather than assumption. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF05-BP02 Implement optimized multi-agent collaboration models](agentperf05-bp02.html) 
+  [AGENTPERF05-BP03 Optimize multi-stage AI pipeline execution](agentperf05-bp03.html) 
+  [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.html) 

 **Related documents:** 
+  [Blog: Customize agent workflows with advanced orchestration techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/) 
+  [Agentic AI patterns and workflows on AWS, Workflow orchestration agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html) 
+  [Building serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html) 
+  [Blog: Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/) 

 **Related videos:** 
+  [Architecting scalable and secure agentic AI with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc) 
+  [Build Your First Agent Workflow with Strands](https://www.youtube.com/watch?v=oGzEKQVhKQU) 
+  [Build Reliable AI Agents with LangGraph](https://www.youtube.com/watch?v=E0BtW2yt2pA) 

 **Related examples:** 
+  [GitHub: Guidance for multi-agent orchestration using Bedrock AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 