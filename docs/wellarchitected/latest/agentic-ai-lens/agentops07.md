# Operational recovery and consumption monitoring

Agentic systems must handle operational failures gracefully and help prevent runaway
behavior that could affect business operations. Recovery mechanisms need to balance
automation with appropriate escalation, and consumption monitoring must detect agents
that exceed expected operational boundaries.

| AGENTOPS07: How do you establish operational recovery and consumption<br>monitoring? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

## Capability intent

- Agent failures trigger automated cutoffs, fallback chains, and recovery
  workflows that restore service within defined recovery time
  objectives.
- Operational knowledge about agent behavior, failure modes, and resolutions
  is captured centrally and remains searchable as people and systems
  change.
- Every agent change passes through a documented workflow that validates
  both technical correctness and continued alignment with business processes,
  policies, and regulatory obligations.
- Human operators have tested, rehearsed runbooks they can execute without
  the agent infrastructure, so business operations continue through
  worst-case agent outages.
- Recovery mechanisms, knowledge bases, and emergency procedures are
  exercised regularly, and findings feed back into improvements to the agent
  infrastructure and to the runbooks themselves.

## Maturity levels

These levels summarize what each stage of maturity looks like for operational
recovery and consumption monitoring as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent failures are handled reactively by whoever notices first.<br>Recovery procedures are not documented and runbooks for worst-case<br>scenarios are missing. Operational knowledge lives with individuals,<br>and change management treats agent updates as generic code changes<br>without considering business alignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2     | Emerging  | Retries and basic fallbacks are implemented for the most<br>important dependencies. Post-incident reviews are held for<br>significant incidents and findings are filed, although they are not<br>systematically propagated into runbooks. An initial set of<br>break-glass procedures is documented for the highest-impact business<br>processes, and change management explicitly covers agent prompts,<br>tools, and [foundation models](../../../bedrock/latest/userguide/models-supported.md "../../../bedrock/latest/userguide/models-supported.md").                                                                                                                                                                                                                                                 |
| 3     | Defined   | Automatic cutoffs, fallback chains, and recovery workflows cover<br>every external dependency and are monitored in [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"). Operational knowledge is captured in<br>a centralized searchable system such as [Amazon Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md"), with post-incident<br>reviews feeding entries directly. Change management classifies agent<br>changes by technical scope and business impact and routes approvals<br>accordingly, and break-glass runbooks are walked through in tabletop<br>exercises.                                            |
| 4     | Proactive | Recovery time objectives are defined for each failure scenario,<br>tracked in dashboards, and validated through regular chaos<br>engineering exercises. Business-alignment reviews run on a defined<br>cadence, and agent-to-business-process mappings generate automated<br>notifications through [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") when processes or policies change.<br>Break-glass drills execute end-to-end in non-production<br>environments, runbook updates are tied to drill findings, and<br>operational knowledge has explicit owners who keep entries<br>current.                                                                                                                                |
| 5     | Optimized | Agent recovery is self-healing and continuously tuned based on<br>production telemetry, with automatic cutoffs, model fallbacks, and<br>multi-agent degradation modes all adjusted against measured<br>outcomes. Operational knowledge is queryable in natural language<br>through internal assistants built on [Amazon Bedrock Agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md") and is continuously maintained as<br>part of normal operations. Change management feedback loops visibly<br>drive infrastructure and business-process improvements. Break-glass<br>readiness is assessed continuously through instrumented drills, and<br>lessons from incidents shape both automated recovery and manual<br>fallback procedures in the next iteration. |

## Common issues to watch for

- Recovery logic is implemented per component but is never tested in
  combination, so cascading failures that span multiple components are
  discovered only during real incidents when business impact is already
  significant.
- Post-incident reviews produce documents that are filed but never
  translated into runbook or platform changes, so the organization pays the
  cost of learning from each incident without compounding the value.
- Agent changes are approved on purely technical criteria while the business
  processes they support evolve separately, creating silent drift between
  agent behavior and current business rules.
- Break-glass runbooks and contact lists are created once and not
  maintained, so by the time they are needed they reference retired systems,
  decommissioned tools, or people who have moved on.
- Emergency procedures are stored in systems that depend on the same agent
  infrastructure they are meant to work around, leaving operators without
  documentation when it is needed.

###### Best practices

- [AGENTOPS07-BP01 Implement automated response and recovery mechanisms](agentops07-bp01.md "agentops07-bp01.md")
- [AGENTOPS07-BP02 Establish operational knowledge management systems](agentops07-bp02.md "agentops07-bp02.md")
- [AGENTOPS07-BP03 Augment change management to accommodate technical improvements and business requirements](agentops07-bp03.md "agentops07-bp03.md")
- [AGENTOPS07-BP04 Implement break-glass operational runbooks](agentops07-bp04.md "agentops07-bp04.md")
