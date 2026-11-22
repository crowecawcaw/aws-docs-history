

# ADVCOST05-BP05 Design small, focused agents and use appropriate orchestration patterns to minimize multi-agent collaboration costs

 Each inter-agent call in a multi-agent advertising system incurs additional inference costs. A poorly configured agentic architecture creates excessive handoffs, when instead a deterministic workflow would work better. Design small, focused agents with bounded iteration limits, and replace supervisor agent overhead with deterministic workflows. 

 **Desired outcome:** 
+  Multi-agent advertising systems use the minimum number of agent invocations needed to produce quality outputs. 
+  Deterministic workflows (fixed-sequence steps) use AWS Step Functions instead of supervisor agents, removing routing overhead. 
+  Iteration limits are set on all agents to guard against runaway reasoning loops. 

 **Common anti-patterns:** 
+  Using a supervisor agent for deterministic workflows that consistently follow the same sequence. 
+  Not setting an iteration limit on agents, which enables reasoning loops that consume tokens without converging on better outputs. 
+  Over-decomposing agent architecture into too many fine-grained agents. 

 **Benefits of establishing this best practice:** 
+  Reduced per-workflow inference costs by avoiding unnecessary supervisor invocations. 
+  Bounded worst-case costs through iteration limits and timeouts. 
+  Cleaner agent architectures where each agent has a narrow scope. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A supervisor agent that routes work to sub-agents pays for its own invocation (reading the request, deciding where to route, and synthesizing results) on top of the sub-agent costs. When the routing decision is deterministic (the workflow consistently follows the same sequence regardless of input), the supervisor's inference cost is pure overhead. For cost optimization in a multi-agent system, first decide whether a workflow is deterministic or dynamic. 

 Deterministic workflows follow a fixed sequence: the campaign brief arrives, the media planner runs, the inventory optimizer runs, and then the ad load optimizer runs. [AWS Step Functions](https://aws.amazon.com/step-functions/) can orchestrate this sequence directly, invoking each [Amazon Bedrock agent](https://aws.amazon.com/bedrock/agents/) as a state in the workflow and passing outputs between states. The cost of a Step Functions state transition is orders of magnitude lower than a supervisor agent invocation. If the workflow later needs conditional routing based on intermediate results, a Step Functions implementation requires code changes, while a supervisor agent adapts through prompt modification alone. 

 Dynamic workflows require a routing agent. When the next step depends on the output of the previous step (for example, a brand safety assessment that escalates to human review only for borderline cases), a supervisor agent provides value. To keep costs down in dynamic workflows, minimize supervisor scope. Have the routing agent decide only which sub-agent to invoke next, not re-read or synthesize sub-agent outputs. A supervisor that summarizes or transforms intermediate results doubles inference cost without improving routing quality. 

 Unbounded iteration is the most likely cause of runaway costs. Without an iteration ceiling, an agent that fails to converge on a satisfactory answer continues reasoning indefinitely, consuming tokens with each loop. In advertising workflows, this appears as an agent that repeatedly queries a knowledge base, reformulates its approach, and generates new outputs without improving quality. The cost scales linearly with iterations. Capping reasoning iterations creates a hard ceiling on worst-case per-invocation cost. Timeouts on external tool calls (Lambda functions and API endpoints) keep a single slow dependency from holding an agent invocation open and accumulating reasoning tokens while it waits. 

 Agent granularity also affects cost. Design each agent to own a coherent task whose entire context fits within a manageable prompt size, and whose output can pass to the next agent without a supervisor to interpret or transform it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map all advertising agent workflows and classify as deterministic or dynamic:** For each workflow (campaign planning, brand safety review, and ad load optimization), document the sequence of agent invocations. If the sequence never varies based on input, classify as deterministic and implement as a Step Functions state machine. 

1.  **Implement deterministic workflows as Step Functions state machines:** Create Express Workflow state machines that invoke agents sequentially, bypassing supervisor agents entirely. Each state calls the appropriate agent directly and passes outputs to the next state. This removes routing overhead on every step. 

1.  **Bound reasoning iterations on all agents:** Cap reasoning depth where the runtime exposes a limit. Amazon Bedrock AgentCore Harness accepts a maxIterations parameter, settable as a harness default or overridden per invocation, and its default allows far more cycles than most advertising agents need. Deployments on the bare AgentCore Runtime don't expose that parameter, so bound iterations in the agent framework code instead. Set the cap to the minimum your task requires. Set timeouts on all external tools (Lambda functions, API endpoints). Configure alarms when any invocation hits the iteration ceiling, which signals a prompt design issue or task scope problem. 

1.  **Use agent tracing to identify optimization opportunities:** Enable Bedrock agent tracing for all production agents. Analyze traces for: unnecessary tool calls, redundant knowledge base queries, high iteration counts, and long reasoning chains that don't produce proportionally better outputs. Use findings to refine agent configurations quarterly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP02 Select the right foundation model for each advertising agent's task complexity](advcost05-bp02.md) 

 **Related documents:** 
+  [Best practices for building robust generative AI applications with Amazon Bedrock Agents, Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/) 

 **Related services:** 
+  [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 