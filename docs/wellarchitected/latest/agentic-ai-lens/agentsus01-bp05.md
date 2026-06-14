# AGENTSUS01-BP05 Adopt specification-driven tasks for frontier agents and long-running workflows

Long-running agents without explicit success criteria and resource
budgets drift into exploration that never quite terminates,
consuming compute hours on paths that don't deliver value.
Specifications that declare acceptable outputs, cost ceilings, and
termination conditions up front make extended execution a bounded
investment rather than an open-ended one.

**Desired outcome:**

- You have specifications for each frontier agent declaring
  maximum execution duration, token budget, memory allocation, and
  termination triggers before deployment.
- Long-running workflows pause at defined checkpoints to evaluate
  progress against the specification, and decisions about
  continuing, modifying, or terminating are informed by that
  evaluation.
- Parent frontier agents cascade remaining budget and time to
  child agents they spawn, so delegation inherits the parent's
  ceiling.
- Specification compliance is monitored in production and feeds
  back into template refinement for future frontier workflows.

**Common anti-patterns:**

- Deploying long-running agents without explicit resource budgets
  or termination conditions, so unbounded exploration is
  structurally possible.
- Omitting success criteria and decision-making boundaries from
  frontier workflow configuration, producing wasteful execution
  patterns where compute is consumed without commensurate value.
- Running extended workflows without checkpoint-based evaluation,
  so nobody can make an informed decision about modifying or
  terminating a run in progress.
- Spawning child agents from frontier workflows without passing
  remaining budget downstream, breaking the cost ceiling at the
  first delegation.

**Benefits of establishing this best
practice:**

- Extended workflows come with accountability, compute investment
  is matched against business value generated rather than consumed
  open-endedly.
- Checkpoint evaluations give operators a chance to redirect or
  halt work before it burns disproportionate infrastructure.
- Specification templates accumulate institutional knowledge about
  expected behavior for common frontier workload patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Frontier agents, code writers, deep research agents, and
autonomous planners, are open-ended by design. That makes them the
place where resource discipline matters most, because the cost of
an unbounded exploration is many orders of magnitude higher than
the cost of a single misrouted call. A specification written
before deployment gives the agent something to terminate against:

- A success criterion that says "this is done"
- A token budget that caps total consumption
- A duration limit that helps prevent indefinite runs
- Explicit termination triggers for conditions where
  continuation has become pointless

Without that contract, the agent runs until it happens to produce
something or hits an infrastructure-imposed ceiling.

Budgets must cascade for the specification to hold. When a
frontier parent delegates to child agents, the parent's ceiling
becomes meaningless unless the children inherit it. This is an
orchestration concern, not a platform feature. In
[AWS Step Functions](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md"), remaining budget is passed as parameters
into child workflow invocations. In a Strands-orchestrated system,
it is included in the child agent's system prompt or invocation
context. Make cascading explicit in the design rather than
assuming children inherit by convention.

Structure long-running workflows to pause at defined points, after
plan generation, after information gathering, and after each major
phase, and evaluate whether progress to date justifies continued
investment. Persist checkpoint state in AgentCore Memory so the
evaluation can pause and resume the agent without restarting it,
which preserves the sunk cost of work already done. Define the
specifications themselves through
[Strands
Agents](https://strandsagents.com/ "https://strandsagents.com/") as first-class configuration delivered at invocation
time through
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md"). This way the contract travels
with the agent. Spec-driven development tools like
[Kiro](https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro "https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro")
apply the same pattern to code-writing agents, giving them
directed and bounded instructions instead of open interpretation.

[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") tracks how often
specifications are violated, what checkpoints are producing useful
decisions, and where budgets are binding. Specifications that
never bind and workflows that always pass checkpoints signal
templates that should be loosened. Specifications that often bind
signal workloads that need tighter scoping or smaller sub-agents.

### Implementation steps

1. **Write specifications before
   deployment:** For each frontier agent, declare the
   following and record the success criteria that define done:

   - Maximum execution duration
   - Token budget
   - Memory allocation
   - Termination triggers

2. **Deliver specifications at invocation
   time:** Pass specifications into
   [Amazon
   Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") through
   [Strands
   Agents](https://strandsagents.com/ "https://strandsagents.com/") as first-class configuration, so the contract
   is part of the invocation rather than implicit in the agent
   code.
3. **Cascade budgets to child
   agents:** When a parent frontier agent delegates,
   pass the remaining duration, token budget, and memory budget
   into the child invocation through
   [AWS Step Functions](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") parameters or Strands orchestration,
   so the ceiling holds across delegation.
4. **Implement checkpoint-based
   evaluation:** Structure long-running workflows to
   pause at defined points, evaluate progress against the
   specification, and persist state in AgentCore Memory so the
   agent resumes from the checkpoint after a
   continue/modify/terminate decision.
5. **Monitor adherence and refine
   templates:** Track the following through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), and feed the data
   back into specification templates for common frontier
   workload patterns:

   - Specification violations
   - Checkpoint outcomes
   - Budget utilization

## Resources

**Related best practices:**

- [AGENTSUS01-BP01 Design
  specialized agents with explicit resource boundaries](agentsus01-bp01.md "agentsus01-bp01.md")
- [AGENTSUS01-BP04 Scale
  cognitive processing pathways appropriately](agentsus01-bp04.md "agentsus01-bp04.md")
- [SUS02-BP03
  Stop the creation and maintenance of unused assets](../sustainability-pillar/sus_sus_software_a4.md "../sustainability-pillar/sus_sus_software_a4.md")
- [COST02-BP02
  Implement goals and targets](../cost-optimization-pillar/cost_govern_usage.md "../cost-optimization-pillar/cost_govern_usage.md")

**Related documents:**

- [AWS Frontier Agents](https://aws.amazon.com/ai/frontier-agents/ "https://aws.amazon.com/ai/frontier-agents/")
- [Introducing
  AWS Frontier Agents and Kiro](https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro "https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro")
- [AWS Step Functions - Standard workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md")
- [Strands
  Agents](https://strandsagents.com/ "https://strandsagents.com/")

**Related examples:**

- [Build
  multi-step applications and AI workflows with AWS Lambda
  durable functions](https://aws.amazon.com/blogs/aws/build-multi-step-applications-and-ai-workflows-with-aws-lambda-durable-functions/ "https://aws.amazon.com/blogs/aws/build-multi-step-applications-and-ai-workflows-with-aws-lambda-durable-functions/")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
