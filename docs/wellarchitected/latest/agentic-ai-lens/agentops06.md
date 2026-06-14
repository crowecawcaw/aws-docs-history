# Testing, evaluation, and validation frameworks

Systematic testing and evaluation processes confirm agent quality, reliability, and
alignment with business objectives through both traditional software testing and
AI-specific quality assessment. Without a framework that covers every stage of the agent
lifecycle, quality regressions from prompt changes, tool updates, or model updates reach
users before anyone notices.

| AGENTOPS06: How do you implement testing, evaluation, and validation<br>frameworks? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

## Capability intent

- Agents are validated at every layer, from isolated components to entire
  workflows running in production-shadow mode, before changes reach
  users.
- Quality, safety, efficiency, and business-alignment metrics are measured
  continually against version-controlled benchmarks, with regressions surfaced
  as soon as they appear.
- Change governance is proportional to risk. Low-risk changes flow through
  automated gates, and high-risk changes receive SME and business-owner
  review.
- Evaluation datasets, prompts, and scoring rubrics are versioned and kept
  current as agent capabilities and use cases evolve.
- Rollback paths for prompts, tools, models, and agent versions are defined,
  rehearsed, and wired to the same telemetry that detects quality threshold
  violations.

## Maturity levels

These levels summarize what each stage of maturity looks like for testing,
evaluation, and validation frameworks as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Testing is one-time and focused on the happy path. Teams rely on<br>manual inspection of agent outputs and infrequent exact-match<br>assertions, missing failures that only appear in tool-use,<br>multi-agent, or production traffic paths. No formal evaluation<br>metrics exist beyond deployment-time smoke tests. Approvals are<br>informal emails or chats, and rollback is a manual, untested<br>redeploy of an older artifact.                                                                                                                                                                                                                                                                                                               |
| 2     | Emerging  | Unit and integration tests exist for the core reasoning, tool,<br>and memory components, and run in a [CI/CD](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") pipeline. Evaluation is performed at key<br>milestones using [Amazon Bedrock model evaluation](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md") and documented<br>acceptance criteria. Approval workflows distinguish at least two<br>risk tiers, and rollback procedures are documented per agent.<br>Coverage of edge cases, adversarial inputs, and production shadow<br>runs is still patchy.                                                                 |
| 3     | Defined   | A four-layer testing pyramid, covering unit, integration,<br>end-to-end, and shadow, is standard across agent teams, with [Amazon Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") supplying built-in<br>evaluators as standardized quality gates. Continuous evaluation<br>tracks output quality, safety, efficiency, and business alignment<br>over time, and risk-tiered approval workflows route changes by scope<br>of impact. Rollback procedures are automated through pipeline<br>triggers and exercised regularly.                                                                                                                     |
| 4     | Proactive | Shadow testing runs alongside production for every significant<br>release, with divergences triaged through [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") traces correlated to evaluation<br>scores. Online evaluation samples live interactions continuously,<br>with thresholds that trigger automated rollback through deployment<br>alarms. Risk-tiered approvals include business owners and SMEs for<br>autonomy-increasing changes, and evaluation datasets evolve<br>automatically from incident and feedback data. Quality, safety, and<br>business metrics are tracked across agent versions as first-class<br>release artifacts. |
| 5     | Optimized | Testing, evaluation, and validation are an integrated,<br>self-healing system. Custom evaluators encode organization-specific<br>quality standards and are versioned with the agents they cover.<br>Policy-as-code expresses risk-tier rules and approval routing, and<br>rollback is provably correct, tested quarterly through game-day<br>exercises. Evaluation scoring, shadow comparisons, and human<br>feedback feed a continuous improvement loop that updates datasets,<br>prompts, and guardrails automatically. The organization contributes<br>patterns and evaluators back to internal communities and external<br>forums.                                                                                                               |

## Common issues to watch for

- Teams stop at deterministic unit tests and skip shadow testing on real
  traffic, so agents ship with unknown behavior on edge cases, adversarial
  inputs, and production data distributions.
- Quality is measured once at release and never again, so data drift, prompt
  decay, and upstream model updates silently erode output quality between
  releases.
- All changes flow through either a heavyweight board or a rubber-stamp
  review, which either bottlenecks minor tweaks or waves through autonomy
  increases without SME scrutiny.
- Test and evaluation datasets are created once and never refreshed, so
  scores stay green while real-world failure modes go undetected.
- Rollback procedures live in a runbook but are never rehearsed, so the
  first real attempt during an incident discovers broken artifact stores,
  missing permissions, or prompt and tool version mismatches.

###### Best practices

- [AGENTOPS06-BP01 Design multi-layered testing frameworks](agentops06-bp01.md "agentops06-bp01.md")
- [AGENTOPS06-BP02 Evaluate and track ongoing agent performance](agentops06-bp02.md "agentops06-bp02.md")
- [AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows](agentops06-bp03.md "agentops06-bp03.md")
