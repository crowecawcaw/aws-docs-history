# AGENTSUS01-BP04 Scale cognitive processing pathways appropriately

Foundation model inference is the single most energy-intensive
operation in an agent workflow, and it runs hundreds or thousands of
times a day. Matching model size, retrieval depth, and memory scope
to actual task complexity keeps cognitive resource consumption
proportional to the value delivered, rather than defaulting every
call to the largest available model.

**Desired outcome:**

- You have tiered model routing in place, so each task goes to the
  smallest model that meets its quality bar.
- Retrieval depth and context window size are scoped to task
  complexity, so routine tasks don't carry the retrieval overhead
  of complex reasoning.
- Multimodal extraction uses purpose-built services where
  applicable, not raw vision models for every document.
- Agents operate within token budgets and rate limits enforced at
  the runtime layer for each agent.

**Common anti-patterns:**

- Routing every request to the largest foundation model without
  checking whether a smaller model or cached response would meet
  the quality bar, which is the largest single opportunity for
  energy reduction.
- Allowing agents to call models without token budgets or
  concurrency limits, enabling single agents to consume
  disproportionate resources under load.
- Configuring retrieval-augmented generation to return the same
  context depth for every task regardless of complexity, producing
  oversized context windows and redundant vector queries.
- Sending raw document images to large vision models when a
  purpose-built extraction service would return the same
  structured data at a fraction of the compute cost.

**Benefits of establishing this best
practice:**

- Cognitive resource consumption scales with task demand rather
  than agent count, so the energy cost of scaling up agent fleets
  stays proportional to the work they do.
- Token budgets for each agent help prevent one agent from
  starving the rest of the fleet under load.
- Right-sizing across hundreds of daily model calls compounds into
  substantial energy savings that are not visible on a single-call
  basis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The Performance Efficiency pillar covers tiered model selection in
[AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.md "agentperf02-bp02.md"). The
Cost Optimization pillar covers model cascading in
[AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.md "agentcost02-bp01.md"). The sustainability view adds one thing. The
objective isn't latency or cost alone, but total energy and
compute footprint per unit of business value delivered. A task
taxonomy that ranks requests by reasoning complexity, then routes
them to appropriately sized
[Amazon
Bedrock](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md") models, makes the routing data-driven rather than
default-to-biggest.

Tracking successful task completions divided by total compute
consumed gives a better signal than either metric alone. A
workflow that gets the right answer on the first try with a small
model is more sustainable than one that uses the largest model and
still retries. Tag invocations so this ratio can be calculated per
task category, and use it to shift routing thresholds over time.
With
[Amazon
Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md"), you can distribute
non-urgent requests to Regions with favorable energy profiles when
latency constraints permit.

Retrieval depth in
[Amazon
Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") should be a parameter of the task,
not a constant. A routine question with a bounded answer doesn't
need the same retrieval fanout as a complex reasoning task.
Oversized retrieval wastes vector queries and bloats context
windows. For document-heavy workloads,
[Amazon
Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md") extracts structured data from
documents at a fraction of the compute cost of routing raw images
through a vision model. The cheaper path is often the better one.

Configure AgentCore Memory with tiered TTLs and automated pruning
so working memory doesn't grow unboundedly, and add semantic
caching so similar queries serve cached responses instead of
repeated invocations. Enforce token budgets and concurrency limits
for each agent through AgentCore Runtime execution constraints.
Measure actual consumption through
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") so thresholds stay tied to
observed reality.

### Implementation steps

1. **Implement tiered model
   routing:** Follow the patterns in
   [AGENTPERF02-BP02
   Implement task-appropriate model selection strategies](agentperf02-bp02.md "agentperf02-bp02.md")
   and
   [AGENTCOST02-BP01
   Architect tiered model selection for cost-performance
   optimization](agentcost02-bp01.md "agentcost02-bp01.md") to direct tasks to appropriately sized
   [Amazon
   Bedrock](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md") models based on a complexity taxonomy.
2. **Scope retrieval depth to task
   complexity:** Parameterize
   [Amazon
   Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") retrieval so vector queries
   and context tokens scale with the work. Use tighter limits
   for routine tasks and broader retrieval only for complex
   reasoning.
3. **Route document extraction to
   purpose-built services:** For multimodal tasks, use
   [Amazon
   Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md") instead of sending raw images
   through large vision models.
4. **Apply memory lifecycle
   policies:** Configure AgentCore Memory with tiered
   TTLs and automated pruning so working memory stays bounded
   and stale entries are removed automatically.
5. **Enforce budgets and track
   efficiency:** Set token budgets and rate limits for
   each agent through AgentCore Runtime execution constraints,
   and track successful completions per unit of compute
   consumed through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") to adjust routing
   thresholds from data.

## Resources

**Related best practices:**

- [AGENTPERF02-BP02
  Implement task-appropriate model selection strategies](agentperf02-bp02.md "agentperf02-bp02.md")
- [AGENTCOST02-BP01
  Architect tiered model selection for cost-performance
  optimization](agentcost02-bp01.md "agentcost02-bp01.md")
- [AGENTSUS01-BP01 Design
  specialized agents with explicit resource boundaries](agentsus01-bp01.md "agentsus01-bp01.md")
- [SUS02-BP02
  Align SLAs with sustainability goals](../sustainability-pillar/sus_sus_user_a3.md "../sustainability-pillar/sus_sus_user_a3.md")

**Related documents:**

- [Amazon
  Bedrock model support](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md")
- [Amazon
  Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md")
- [Amazon
  Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md")
- [Effective
  cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/")
- [Build
  trustworthy AI agents with Amazon Bedrock AgentCore
  Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/ "https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/")
- [Agentic
  AI patterns and workflows on AWS - Routing dynamic dispatch
  patterns](../../../prescriptive-guidance/latest/agentic-ai-patterns/routing.md "../../../prescriptive-guidance/latest/agentic-ai-patterns/routing.md")

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
  with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess "https://www.youtube.com/watch?v=tFiDkSG2ess")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Evaluations
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations")

**Related services:**

- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
