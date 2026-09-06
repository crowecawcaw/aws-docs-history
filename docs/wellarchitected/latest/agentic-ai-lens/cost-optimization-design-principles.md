

# Design principles
<a name="cost-optimization-design-principles"></a>

In addition to the lens-level design principles, the cost optimization best practices in this lens are represented by at least one of the following principles:
+ **Pay only for the reasoning the task requires:** Match model class, context length, and reasoning depth to task complexity instead of provisioning the largest model and longest context for the worst case.
+ **Enforce consumption ceilings at every layer:** Token budgets, iteration limits, time bounds, and concurrency caps live as policy at the gateway, runtime, and orchestration tiers so unbounded execution is rejected at the boundary rather than paid for and discovered later.
+ **Reuse before you recompute:** Caching of prompts, tool results, retrievals, and intermediate state turns repeat work into lookups. Inference is the most expensive operation in the system; build the architecture around that fact.
+ **Attribute spend to the unit that drives it:** Tag every invocation with agent, tenant, session, and workflow so reporting moves from infrastructure-level to per-decision accounting and over-provisioned components become visible.
+ **Close the loop between cost data and architecture:** Cost telemetry feeds back into model selection, prompt design, and orchestration choices on a regular cadence. Optimization is continuous, not a one-time review.