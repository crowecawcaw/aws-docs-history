# Agent lifecycle and deployment processes

Agent lifecycle management extends beyond traditional software deployment to include
behavioral evolution, capability updates, and operational governance. Agents require
ongoing management as they adapt to changing business requirements, integrate new tools,
and scale across different environments.

| AGENTOPS03: How do you manage agent lifecycle and deployment<br>processes? |
| -------------------------------------------------------------------------- |
|                                                                            |

## Capability intent

- Every agent has a documented owner, lifecycle state, and set of transition
  criteria, from initial development through to clean decommissioning.
- Agent changes reach production through automated deployment pipelines with
  agent-specific quality gates, staged rollout, and automatic rollback on
  regression.
- Agent capacity adjusts to workload demand within per-environment
  boundaries, and deployments are kept right-sized through regular capacity
  reviews.
- The agent portfolio is visible in a single catalog with cross-team
  dependencies tracked, so teams discover existing capabilities before
  building new agents.
- Portfolio-level rationalization (retirement, consolidation, continued
  investment) is driven by evidence of utilization, cost, and business value
  rather than team-level preference.

## Maturity levels

These levels summarize what each stage of maturity looks like for agent lifecycle
and deployment processes as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent lifecycle is informal. Teams spin up agents on demand,<br>often straight to production, with no documented stages, no<br>registry, and no designated owners. Deployments are manual. There is<br>no agent-specific CI/CD or behavioral evaluation. Scaling is static<br>or per-workload and revisited only when something breaks. No<br>portfolio-level visibility exists across teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2     | Emerging  | A lifecycle with defined stages exists on paper and most teams<br>follow it. Agents are tracked in a team-level registry. Basic CI/CD<br>runs unit tests, and deployments use infrastructure as code<br>templates. Per-environment scaling boundaries are set manually.<br>Teams can list the agents they own, but there is no cross-team<br>catalog or dependency view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3     | Defined   | Lifecycle stages are standardized across the organization with<br>validation gates at each transition. AgentOps pipelines include<br>agent-specific evaluation through [Amazon Bedrock Evaluations](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md") and staged rollout through<br>[Amazon Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") versioning.<br>Auto-scaling is driven by agent-specific metrics rather than raw CPU<br>or memory. A shared agent catalog is emerging, and the first<br>quarterly portfolio reviews are held.                                                                                                                                                                                               |
| 4     | Proactive | Lifecycle transitions are fully automated, including emergency<br>termination switch and decommissioning runbooks. CI/CD behavioral<br>gates block release when task accuracy or hallucination thresholds<br>regress, with automated rollback from [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms. Scaling policies, stored<br>centrally, adjust as agents move between lifecycle stages. [AWS Agent Registry](../../../bedrock-agentcore/latest/devguide/registry.md "../../../bedrock-agentcore/latest/devguide/registry.md") with semantic capability search<br>and [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") dependency notifications is the<br>default path for new agent creation. |
| 5     | Optimized | Lifecycle, deployment, scaling, and portfolio management are<br>policy-codified and continuously refined from operational data. A<br>dependency graph backs impact analysis before any agent change.<br>Portfolio rationalization (consolidation, retirement, reinvestment)<br>runs as a regular operating rhythm with business-value measurement.<br>Governance overhead scales sub-linearly with agent count, and the<br>organization contributes its patterns back to the industry.                                                                                                                                                                                                                                                                                                                                                                                                        |

## Common issues to watch for

- Agents accumulate in production without documented owners or lifecycle
  states, so retirement and incident response stall because nobody knows who
  is accountable for each agent.
- Agent deployments rely on traditional software CI/CD without
  agent-specific behavioral evaluation, letting prompt or tool regressions
  reach users that unit tests would never catch.
- Scaling is configured identically across environments, either wasting cost
  in development or degrading production latency during traffic spikes.
- Teams build redundant agents in parallel because the organization lacks a
  shared catalog and discovery path, inflating cost and operational burden
  without adding capability.
- Cross-team agent dependencies are undocumented, so deprecating or
  modifying an upstream agent causes cascading failures in downstream agents
  that were silently consuming it.

###### Best practices

- [AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance](agentops03-bp01.md "agentops03-bp01.md")
- [AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)](agentops03-bp02.md "agentops03-bp02.md")
- [AGENTOPS03-BP03 Implement agent-specific scaling policies and capacity planning](agentops03-bp03.md "agentops03-bp03.md")
- [AGENTOPS03-BP04 Implement organizational agent portfolio management and governance at scale](agentops03-bp04.md "agentops03-bp04.md")
