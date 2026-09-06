

# AGENTCOST01-BP01 Use the reflection pattern to design efficient agent reasoning loops
<a name="agentcost01-bp01"></a>

 Unbounded reasoning loops consume tokens unpredictably and can result in higher than expected token consumption for routine tasks. A bounded reflection pattern gives you predictable token budgets and preserves decision quality. 

 **Desired outcome:** 
+  You have explicit termination conditions for every agent: a maximum iteration count, a confidence threshold, and a per-session token budget. 
+  You apply reflection selectively, triggering full self-correction only when initial output quality falls below a threshold. 
+  You track per-cycle token consumption and decision quality so termination parameters can be tuned from data rather than guesswork. 

 **Common anti-patterns:** 
+  Running agents without iteration limits or cost caps, allowing indefinite token consumption without progress toward the task. 
+  Applying expensive reflection and self-correction to every output, regardless of whether the initial answer was already good. 
+  Operating without per-cycle token instrumentation, so no one can tell which reasoning phase drives cost. 
+  Using fixed iteration counts instead of confidence thresholds, which either wastes tokens on unnecessary iterations or cuts off complex reasoning prematurely. 
+  Building reflection patterns without budget guardrails, so unbounded loops consume tokens before alerts fire. 

 **Benefits of establishing this best practice:** 
+  Predictable token consumption through bounded reasoning cycles with explicit termination conditions. 
+  Selective reflection preserves decision quality for ambiguous cases while reducing token waste on straightforward tasks. 
+  Cost-quality baselines reveal which reasoning patterns deliver the best trade-offs, enabling data-driven tuning of thresholds. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every reflection loop assumes that another iteration will improve the answer more than it costs, which works with ambiguous tasks but often loses value on straightforward ones. Without that contract, agents reflect on every output regardless of whether reflection improves quality. The discipline is to emit a structured confidence signal alongside each action, inspect it in the orchestration layer, and short-circuit the loop when confidence clears a threshold. Otherwise the loop runs until it hits a hard iteration ceiling, which is both the slowest and most expensive outcome for the common case. 

 Enforcement matters as much as the contract. Iteration caps expressed only in the system prompt can drift past under adversarial inputs or prompt injections. [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies at the [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) boundary, so iteration and token limits are rejected at the traffic layer rather than noticed after they're exceeded. [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides session-isolated execution and consumption-based pricing, so each session carries its own budget and one runaway session doesn't corrupt accounting for others. 

 Selective reflection separates ambiguity handling from cheaper routine work. Score the initial output against a lightweight rubric, a small model or heuristic, and gate full reflection on that score. Tag reflection outcomes with the task category so you can see where reflection consistently improves quality and where it adds cost with no benefit. Categories that never benefit from reflection should have the trigger disabled entirely. [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) supports LLM-as-a-Judge assessment of decision quality, which gives you an objective confidence signal rather than a self-reported one from the agent being evaluated. 

 The plan, execute, verify, and reflect phases within a reflection cycle have different reasoning intensities. Routing planning and verification to smaller, faster models while reserving the largest model for execution captures cumulative savings on the frequent low-cost phases, offsetting the higher per-token cost of the infrequent high-intensity phase. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define explicit termination conditions per agent:** Set a maximum iteration count, a confidence threshold, and a per-session token budget, and enforce them through [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies at the AgentCore Gateway boundary so enforcement happens at the traffic layer rather than in application code. 

1.  **Instrument per-cycle token consumption:** Enable [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture per-session token counts through OpenTelemetry, and configure Amazon CloudWatch alarms on anomalous per-cycle patterns. 

1.  **Establish objective confidence thresholds:** Configure [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to score decision quality through LLM-as-a-Judge, and anchor early-termination thresholds to measured quality rather than self-reported confidence. 

1.  **Gate reflection on initial output quality:** Score each initial output with a lightweight rubric and trigger the full reflection pass only when the score falls below a configurable threshold, keeping reflection overhead off the straightforward cases. 

1.  **Recalibrate thresholds on a cadence:** Review cost-quality baselines monthly (or quarterly for stable workloads) and adjust confidence thresholds, iteration limits, and reflection triggers based on the distribution of observed outcomes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST01-BP02 Optimize multi-agent collaboration cost through efficient handoff patterns](agentcost01-bp02.html) 
+  [AGENTCOST01-BP03 Implement cost-effective patterns like hybrid supervisor for multi-agent coordination](agentcost01-bp03.html) 
+  [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html) 
+  [AGENTCOST07-BP01 Implement automated cost controls with intelligent cutoffs](agentcost07-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Evaluate models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) 
+  [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html) 
+  [Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k) 
+  [AWS re:Invent 2024 - Balance cost, performance & reliability for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE) 
+  [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime) 

 **Related workshops:** 
+  [Diving Deep into Bedrock AgentCore - Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 