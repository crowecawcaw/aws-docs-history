# Agent governance

Organizations that deliberately design how agents interact with
users and business processes sustain both automation value and
institutional expertise as adoption scales. As agents proliferate,
there is a risk that internal expertise will be diluted or lost to
fully automated processes. The patterns governing agent
interactions must be deliberately designed and maintained,
establishing reusable approaches based on real-world
organizational needs.

| AGENTSUS03: How do I establish durable patterns for agent<br>interactions with users and business processes? |
| ------------------------------------------------------------------------------------------------------------ |
|                                                                                                              |

## Capability intent

- Organizational competencies are deliberately categorized
  across human-owned, agent-augmented, and fully automated
  tiers, with clear boundaries enforced by routing and
  guardrail policies.
- Agent development targets processes the organization has
  already mastered, so automation accelerates proven workflows
  rather than substituting for process discovery.
- Agents ship with declarative specifications, dependency
  graphs, and policy documentation that remain current as
  agents evolve, so institutional knowledge is preserved in an
  accessible form.
- A central catalog of deployed agents captures owner,
  purpose, dependencies, and usage, and teams consult it
  before building new agents.
- The agent portfolio is actively rationalized, with inactive
  agents flagged for review, decommissioned through a
  structured lifecycle, and reclaimed infrastructure returned
  to the shared pool.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent governance as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Agents are built and deployed without competency<br>tiering, ownership assignment, or portfolio oversight.<br>Documentation is thin, decommissioning is one-time, and<br>institutional knowledge is held only by the original<br>developers rather than recorded in any specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2     | Emerging  | Teams have categorized competencies into human-owned,<br>agent-augmented, and fully automated tiers, and<br>[Amazon<br>Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") are in place for high-stakes<br>escalation. Declarative configuration in<br>[Amazon<br>Bedrock AgentCore](../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md "../../../bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.md") captures the baseline agent<br>specification. Basic ownership metadata is recorded for<br>each deployed agent.                                                                                                                                                                                                                        |
| 3     | Defined   | Documented workflows feed agent development through<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") RAG sources, and<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") routing separates<br>routine tasks from cases that require human judgment.<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") compares agent<br>outputs against expert baselines, and rotation programs<br>keep subject matter experts practiced in the underlying<br>work. A central agent catalog with ownership and purpose<br>is maintained. |
| 4     | Proactive | Runtime documentation generated through<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") validates design<br>specifications against actual behavior, and production<br>promotion is gated on current documentation.<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") metrics flag inactive agents for owner<br>review, and a structured decommissioning lifecycle moves<br>agents through active, under review, deprecated, and<br>decommissioned states. Quarterly portfolio<br>rationalization reviews are a standing cadence.                                                                               |
| 5     | Optimized | Governance is continuous rather than periodic. Portfolio<br>health metrics (total agent count, percentage with<br>active usage, percentage with current documentation) are<br>reviewed at the organizational level. Specification<br>currency, evaluation baselines, and competency tiering<br>adjust based on operational telemetry, and the<br>organization shares its agent governance patterns with<br>its communities of practice.                                                                                                                                                                                                                                                                                                                                                                                                          |

## Common issues to watch for

- Teams automate unfamiliar or poorly understood processes
  where decision criteria and success metrics are not
  documented, so agent development wastes resources on
  untested methodologies.
- Organizations skip competency tiering, so agents end up
  handling high-stakes or ambiguous decisions that should be
  routed to human experts and subject matter expertise quietly
  atrophies.
- Teams treat agent development as code-only artifacts without
  capturing the expert decision-making patterns and business
  logic rationale, leaving institutional knowledge locked
  inside implementations that only the original developers
  understand.
- Agents are deployed without ownership assignment or usage
  tracking, so there is no basis for evaluating whether an
  agent is still delivering value or has fallen out of use.
- Teams build new agents for capabilities that already exist
  elsewhere in the organization because no one searches the
  catalog first, creating redundant implementations and
  undermining reuse.

###### Best practices

- [AGENTSUS03-BP01 Maintain organizational skills and competencies](agentsus03-bp01.md "agentsus03-bp01.md")
- [AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies](agentsus03-bp02.md "agentsus03-bp02.md")
- [AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems](agentsus03-bp03.md "agentsus03-bp03.md")
- [AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl](agentsus03-bp04.md "agentsus03-bp04.md")
