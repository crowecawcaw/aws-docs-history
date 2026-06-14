# Operational practices for agentic AI systems

Agentic systems that are built on strong operational foundations (with clear roles,
reliable handoffs, and tested failure recovery) earn stakeholder trust and scale
confidently into production. These systems combine precedent and best practices from
several architectural disciplines, including generative AI and multi-agent coordination.
These practices can't be combined without careful consideration. They must be
judiciously selected and refined based on the workload being built and the business
problem being addressed.

| AGENTOPS01: How do you establish operational practices for agentic AI<br>systems? |
| --------------------------------------------------------------------------------- |
|                                                                                   |

## Capability intent

- Each agent has a documented purpose, measurable success criteria, and
  autonomy boundaries that stakeholders can trace back to a specific business
  outcome.
- Multi-agent coordination flows through standardized handoff protocols that
  transfer context reliably and route work to a human reviewer when
  confidence, stakes, or capability thresholds are exceeded.
- Agent systems are validated against realistic failure modes across
  dependent components, orchestration protocols, and business processes before
  they reach production, and on every behavioral change after.
- Operational signals, failure test outcomes, and business metrics feed a
  continuous improvement loop that keeps agent behavior aligned with evolving
  business needs.
- Operational artifacts such as job descriptions, handoff runbooks, and
  failure test scenarios are treated as living documents that stay in sync
  with the agents they describe.

## Maturity levels

These levels summarize what each stage of maturity looks like for operational
practices for agentic AI systems as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent scope, handoffs, and failure testing are ad-hoc. Knowledge<br>about what each agent is meant to do, and how agents interact, lives<br>with individual builders. Out-of-scope requests produce<br>unpredictable responses, handoffs lose context, and failure modes<br>are typically first encountered during production incidents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 2     | Emerging  | Each agent has a documented job description covering purpose,<br>stakeholders, and measurable success criteria. Basic handoff<br>runbooks and human escalation paths cover the most common scenarios.<br>An initial failure test suite covers the happy path and a handful of<br>dependent component failures, and reviews happen on an informal<br>cadence.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 3     | Defined   | Agent job descriptions, handoff protocols, and failure test<br>suites are standardized across teams and stored in shared<br>repositories. [Amazon Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") enforce scope at runtime,<br>structured context packages accompany every handoff, and failure<br>tests run in CI/CD as a mandatory gate across dependent components,<br>orchestration protocols, and business processes. Handoff success<br>rates and failure test pass rates are tracked as first-class<br>metrics.                                                                                                                                                                                                                   |
| 4     | Proactive | Operational controls are automated and data-driven. [AWS Agent Registry](../../../bedrock-agentcore/latest/devguide/registry.md "../../../bedrock-agentcore/latest/devguide/registry.md") supports runtime discovery and<br>intelligent routing across agents and tools. [Amazon Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") run on a regular<br>cadence to validate agent performance and resilience, and [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms on handoff and evaluation<br>metrics trigger automated remediation.                                                          |
| 5     | Optimized | Operational practice is a continuously refined, self-improving<br>system. Production incidents automatically generate new failure test<br>scenarios, and agent job descriptions evolve through spec-driven<br>development with reproducible audit trails. Multi-agent<br>orchestration uses and contributes to industry standards such as<br>[Model Context Protocol](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") and [Agent-to-Agent communication](../../../prescriptive-guidance/latest/agentic-ai-frameworks/introduction.md "../../../prescriptive-guidance/latest/agentic-ai-frameworks/introduction.md"). Resilience metrics and<br>business outcome metrics are correlated in real time and feed<br>directly into roadmap decisions. |

## Common issues to watch for

- Teams define agents by what they can do rather than what they are
  accountable for, leaving operators without a clear way to judge whether the
  agent is working or to decide when to escalate.
- Multi-agent workflows are assembled bottom-up from individual agent
  capabilities, without documented handoff protocols or human escalation
  paths, producing systems that are hard to operate when a single agent
  fails.
- Failure testing is treated as a phase rather than a living practice, so
  resilience degrades quietly with each prompt, tool, or model change that
  ships without a matching regression test.
- Success criteria and resilience metrics are tracked in silos separate from
  business metrics, so agent owners can't explain the business impact of a
  coordination failure or a drop in failure-test pass rate.
- Operational artifacts such as job descriptions, runbooks, and failure test
  scenarios are authored once and never revisited, so documented intent drifts
  away from actual runtime behavior.

###### Best practices

- [AGENTOPS01-BP01 Establish well-defined agent roles, responsibilities, and success criteria](agentops01-bp01.md "agentops01-bp01.md")
- [AGENTOPS01-BP02 Design multi-agent handoff procedures with human-in-the-loop escalation](agentops01-bp02.md "agentops01-bp02.md")
- [AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes](agentops01-bp03.md "agentops01-bp03.md")
