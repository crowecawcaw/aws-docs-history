

# AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering
<a name="agentcost02-bp02"></a>

 Every token in a system prompt is paid for on every invocation, so prompt bloat compounds linearly with traffic. Compressing system prompts, tool descriptions, and output formats makes the fixed cost of each agent call proportional to the decision it has to make, not the verbosity of its instructions. 

 **Desired outcome:** 
+  You have agent system prompts compressed to the minimum tokens needed for accurate task completion. 
+  You have tool descriptions presented dynamically based on the current task rather than transmitted in full on every call. 
+  You constrain output length explicitly so verbose responses don't compound across multi-turn reasoning. 
+  You version prompts and track cost-per-task per version so efficiency changes are measurable over time. 

 **Common anti-patterns:** 
+  Writing verbose system prompts with lengthy persona descriptions and redundant explanations, inflating the fixed token cost on every invocation. 
+  Including every tool description in every invocation regardless of task relevance, which inflates input tokens when only a subset of tools applies. 
+  Allowing unconstrained output length without formatting directives, enabling verbose responses that compound across multi-turn reasoning cycles. 
+  Treating prompts as uncontrolled strings rather than versioned artifacts, so regressions in token efficiency go unnoticed until a billing review. 

 **Benefits of establishing this best practice:** 
+  Fixed-cost reductions from prompt compression compound across every agent invocation in high-volume deployments. 
+  Dynamic tool loading transmits only task-relevant tools, reducing tool description overhead in proportion to catalog size. 
+  Prompt versioning with token tracking makes compression an ongoing, measurable practice rather than a one-off cleanup. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The system prompt is the largest fixed cost in every model invocation, which means every unnecessary sentence is paid for again each time the agent is called. Start by auditing prompts with [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token footprints, then compress systematically. Replace verbose instructions with structured directives, tighten role definitions, and remove redundant explanations. 

 Tool descriptions behave the same way. If the prompt carries the full tool catalog even when only three tools are relevant, you are paying for the rest of the catalog on every call. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) uses MCP-based Semantic Tool Selection to present only the tools relevant to the current intent, and [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state across multi-turn sessions so you don't pay for manual history concatenation. 

 In your context window, allocate tokens across the system prompt (20 to 30%), user context (30 to 40%), few-shot examples (10 to 20%), and agent scratchpad (20 to 30%), and adjust based on your agent's reasoning patterns. For few-shot examples in particular, test whether the model performs well zero-shot before paying for examples on every call. When examples are needed, identify the minimum count that maintains task accuracy against the quality baseline. Two or three examples are typically enough, and dynamic example selection from a semantic index keeps only the relevant ones in context. 

 Output length is the last thing to adjust. Explicit formatting directives in the system prompt (response structure, maximum length) directly control output token costs. Treat prompts as versioned artifacts. Record token count, task success rate, and cost-per-task for each version using AgentCore Observability telemetry, and establish a monthly review cadence that tracks cumulative savings in AWS Cost Explorer. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit and compress system prompts:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token footprints for every prompt, then apply compression to minimize prompt size while maintaining decision accuracy. 

1.  **Present tools dynamically through Gateway:** Use [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Semantic Tool Selection to present only relevant tools per invocation, and compress tool descriptions to tool name, one-sentence description, and concise parameter schema. 

1.  **Constrain output length:** Add explicit output formatting directives to the system prompt and configure model-specific token limit parameters to enforce hard caps on response size. 

1.  **Use managed memory for multi-turn context:** Configure [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) so conversation state is maintained automatically instead of re-transmitted as full history. 

1.  **Reduce few-shot example overhead:** Evaluate whether each agent task needs examples at all, then reduce to the minimum effective count of two to three. Load examples dynamically from an Amazon S3-hosted library using semantic similarity retrieval. 

1.  **Version prompts and track efficiency:** Record token count and task success rate per prompt version, and establish a monthly optimization review cadence that tracks cumulative savings against cost-per-task targets. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST01-BP01 Use the reflection pattern to design efficient agent reasoning loops](agentcost01-bp01.html) 
+  [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html) 
+  [AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations](agentcost02-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess) 
+  [Strands Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime) 

 **Related tools:** 
+  [Strands Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 