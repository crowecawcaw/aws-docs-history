# Model invocation and token cost optimization

Teams that right-size model selection to task complexity and
optimize token consumption per invocation can improve their cost
reductions without sacrificing agent decision quality. Foundation
model costs can dominate agentic AI budgets, with agents
potentially invoking expensive models for simple tasks or
consuming excessive tokens through verbose reasoning.

| AGENTCOST02: How do you optimize agent model invocation<br>and token consumption costs? |
| --------------------------------------------------------------------------------------- |
|                                                                                         |

## Capability intent

- Model selection matches task complexity, with routine
  classification and formatting handled by cost-efficient
  models and premium models reserved for reasoning that
  genuinely needs them.
- Prompts, tool descriptions, and output constraints are kept
  at the minimum size required to maintain decision quality
  across planning, execution, and reflection phases.
- Repeated reasoning and stable context are served from caches
  rather than regenerated, so equivalent requests don't pay
  the full inference cost twice.
- High-volume recurring tasks run on specialized or customized
  models whose one-time training cost amortizes against
  sustained per-invocation savings.
- Cost-per-correct-response, token consumption, cache hit
  rate, and cascade escalation rate are tracked per model tier
  and fed back into routing, caching, and customization
  decisions.

## Maturity levels

These levels summarize what each stage of maturity looks like
for model invocation and token cost optimization as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Teams invoke a single default foundation model for every<br>agent task regardless of complexity, and prompts, tool<br>lists, and outputs grow without review. No prompt<br>caching, semantic caching, or model customization is in<br>place. Cost surprises are attributed to traffic growth<br>rather than investigated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2     | Emerging  | A documented model routing policy maps task types to<br>specific model tiers, and environments are aligned to<br>the appropriate<br>[Amazon<br>Bedrock on-demand pricing tier](../../../bedrock/latest/userguide/capacity-limits-cost-optimization.md "../../../bedrock/latest/userguide/capacity-limits-cost-optimization.md") (Flex, Standard,<br>Priority). Prompt compression, explicit output length<br>constraints, and<br>[Amazon<br>Bedrock prompt caching](../../../bedrock/latest/userguide/prompt-caching.md "../../../bedrock/latest/userguide/prompt-caching.md") for stable system prompts<br>are applied to the highest-volume agents. Token<br>consumption is reviewed periodically against aggregate<br>cost dashboards.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 3     | Defined   | A pre-classifier routes every invocation to a model tier<br>based on task complexity, and model cascading with<br>confidence-based escalation is the default pattern for<br>non-trivial reasoning. Semantic caching and plan<br>template reuse run alongside prompt caching, with TTLs<br>differentiated by task freshness. Token consumption,<br>cache hit rates, and cascade escalation rates are<br>tracked per reasoning phase using<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), and<br>[Bedrock<br>batch inference](../../../bedrock/latest/userguide/batch-inference.md "../../../bedrock/latest/userguide/batch-inference.md") is used for non-time-sensitive<br>work.                                                                                                                                                                                                                                                                                                                                                                      |
| 4     | Proactive | Routing, caching, and guardrails are automated.<br>[Amazon<br>Bedrock AgentCore](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md") policies enforce model tier<br>limits, cache policies are event-driven, and fallback<br>chains handle timeouts without same-tier retries.<br>High-volume task categories run on distilled or<br>parameter-efficient fine-tuned models in production,<br>validated through A/B testing with<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") and served through<br>[Custom<br>Model Import](../../../bedrock/latest/userguide/model-customization-import-model.md "../../../bedrock/latest/userguide/model-customization-import-model.md") on<br>[AgentCore<br>Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md"). Cost-per-correct-response is a tracked<br>service-level metric and drives quarterly refresh<br>decisions. |
| 5     | Optimized | Model portfolios are continuously optimized. Complexity<br>classifiers, cascade thresholds, cache similarity<br>thresholds, and customization refresh cadences are all<br>tuned from production telemetry. Customized models are<br>refreshed on a continuous pipeline with automated<br>training data extraction, evaluation, and promotion<br>gates. The organization drives cost-per-outcome<br>improvements quarter over quarter while maintaining or<br>raising decision quality baselines, and contributes<br>patterns and benchmarks back to the broader practitioner<br>community.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Common issues to watch for

- Every agent invocation defaults to the most capable
  general-purpose model, resulting in higher inference costs
  for routine classification and formatting that could use
  cost-effective alternatives.
- System prompts and tool catalogs accumulate without review,
  so the fixed input-token tax paid on every invocation rises
  silently across months even when traffic is flat.
- Caching is treated as a one-time enablement rather than an
  ongoing discipline, so stale invalidation policies, weak
  similarity thresholds, or drifting cacheable prefixes erode
  hit rates and savings without anyone noticing.
- Model customization is pursued on low-volume or vanity
  workloads rather than on high-volume recurring tasks where
  training cost can amortize, leaving the investment
  permanently underwater.
- Cost signals are tracked only at aggregate level, so teams
  can't see which tier, reasoning phase, or cache layer is
  driving spend and can't prioritize optimization work against
  evidence.

###### Best practices

- [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.md "agentcost02-bp01.md")
- [AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering](agentcost02-bp02.md "agentcost02-bp02.md")
- [AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations](agentcost02-bp03.md "agentcost02-bp03.md")
- [AGENTCOST02-BP04 Implement model customization for long-term cost reduction](agentcost02-bp04.md "agentcost02-bp04.md")
