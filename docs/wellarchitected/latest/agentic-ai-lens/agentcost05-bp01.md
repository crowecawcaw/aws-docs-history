# AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution

Account-level billing shows what an agent fleet costs, but it
doesn't show where the specific costs come from. Granular tracking
by agent, workflow, and reasoning phase provides trackable detail
about your spending, which makes opaque costs into the input for
targeted optimization.

**Desired outcome:**

- You have a standard tag taxonomy applied consistently across all
  agent invocations.
- You track per-phase token consumption (planning, execution,
  reflection, and verification) separately.
- You monitor tool invocation costs separately from model
  inference costs.
- You calculate cost-per-decision, cost-per-reasoning-cycle, and
  cost-per-task-completion as primary agent metrics.

**Common anti-patterns:**

- Tracking only account-level AWS billing without per-agent or
  per-workflow attribution, reducing the risk of identification of
  cost drivers.
- Deploying agents without consistent resource tagging across
  model invocations, function executions, and data operations.
- Monitoring total agent costs without distinguishing between
  supervisor overhead, worker execution, and individual reasoning
  phases.
- Monitoring only infrastructure costs without calculating
  cost-per-autonomous-task-completion, reducing the risk of
  economic evaluation of agent efficiency.

**Benefits of establishing this best
practice:**

- Agent-specific metrics identify cost anomalies and enable
  comparison of agent performance across the fleet.
- Per-phase token tracking reveals which reasoning phases consume
  disproportionate tokens, enabling targeted optimization.
- Business-relevant metrics like cost-per-task-completion enable
  economic evaluation of different reasoning strategies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The foundation of agent cost visibility is a tag taxonomy applied
consistently everywhere spend happens, like:

- agent-id
- agent-role (like supervisor, worker, and
  specialist)
- workflow-id
- task-type
- Environment on every
  [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") invocation and
  [Amazon
  Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") session

These tags are the primary key for all downstream cost
attribution. Activating tag-based cost allocation in AWS Cost Explorer generates per-agent and per-workflow reports without
custom pipeline work, so as soon as tagging is consistent, the
reports become usable.

[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") decomposes agent execution
into individual operations with token counts and latency through
distributed tracing. Per-phase tracking becomes possible because
you can attribute tokens to planning, execution, reflection, and
verification without manual instrumentation. The AgentCore Runtime
consumption-based pricing and microVM session isolation keep cost
boundaries aligned with execution boundaries, so the telemetry and
the billing see the same unit of work.

A single user request triggers multiple agents, each making
multiple model calls, tool invocations, and memory operations, so
raw invocation cost has to roll up through a hierarchy to be
useful. The aggregation pattern is:

1. Collect per-invocation costs from Amazon Bedrock API responses
2. Associate them with the parent agent using session tags
3. Roll agent costs into workflow totals using
   workflow-id
4. Attribute workflow costs to tenants for multitenant
   deployments

Once aggregation is in place, cost reports work at every level:
invocation-level for optimization, agent-level for performance
comparison, workflow-level for business justification, and
tenant-level for billing.

Publishing per-phase token counts as Amazon CloudWatch custom
metrics enables you to build dashboards for cost-per-decision,
cost-per-reasoning-cycle, and cost-per-task-completion segmented
by agent type. CloudWatch alarms on cost-per-task-completion
thresholds and AWS Budgets alerts for per-agent monthly spending
limits turn the tracking from a passive report into an active
signal that tells the team when an agent's economics have shifted.

### Implementation steps

1. **Define and apply a standard tag
   taxonomy:** Apply agent-id,
   agent-role,
   workflow-id,
   task-type, and environment tags
   consistently to all
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") invocations and
   [Amazon
   Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") sessions, and enable AWS Cost Explorer tag-based cost allocation.
2. **Enable end-to-end cost
   traces:** Configure
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") to capture
   distributed traces, and export telemetry to Amazon CloudWatch for per-operation cost analysis.
3. **Aggregate costs
   hierarchically:** Implement a Lambda function that
   runs every 15 minutes to collect model inference, tool
   invocation, and memory costs, storing aggregated results by
   agent and session in a DynamoDB cost tracking table with
   rollups from invocation to agent to workflow to tenant.
4. **Build cost-per-task
   dashboards:** Create CloudWatch dashboards
   displaying cost-per-decision, cost-per-reasoning-cycle, and
   cost-per-task-completion by agent type.
5. **Configure alerts and
   budgets:** Set AWS Budgets alerts for per-agent
   monthly spending limits and CloudWatch alarms for
   cost-per-task-completion thresholds.

## Resources

**Related best practices:**

- [AGENTCOST05-BP02
  Implement distributed cost tracing for multi-agent
  workflows](agentcost05-bp02.md "agentcost05-bp02.md")
- [AGENTCOST05-BP03 Design
  tenant-aware cost allocation for AaaS pricing models](agentcost05-bp03.md "agentcost05-bp03.md")
- [AGENTCOST05-BP04 Create
  chargeback and ROI reporting](agentcost05-bp04.md "agentcost05-bp04.md")
- [AGENTCOST07-BP02
  Establish proactive anomaly detection for agent cost
  patterns](agentcost07-bp02.md "agentcost07-bp02.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [Using
  cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
- [Economics
  for agentic AI on AWS](../../../prescriptive-guidance/latest/agentic-ai-economics/index.md "../../../prescriptive-guidance/latest/agentic-ai-economics/index.md")
- [Guidance
  for Cost Analysis and Optimization with Amazon Bedrock
  Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/ "https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/")

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
  OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k "https://www.youtube.com/watch?v=wWQgawUPr1k")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Observability
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability")

**Related workshops:**

- [Diving
  Deep into Bedrock AgentCore - Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability "https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/")
