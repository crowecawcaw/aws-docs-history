# Agent goal alignment and manipulation prevention

Agents can be directed to pursue unintended objectives or exhibit
behaviors outside their defined scope. Without goal alignment
mechanisms, agents might take actions that conflict with
organizational policies or user intent. Implementing guardrails,
layered validation controls, and human-in-the-loop approvals helps
verify that agents operate within intended boundaries.

| AGENTSEC04: How do you support agent goal alignment and<br>prevent manipulation? |
| -------------------------------------------------------------------------------- |
|                                                                                  |

## Capability intent

- Operational and policy boundaries for each agent are defined
  up front and enforced through layered controls rather than
  prompt instructions alone.
- Deterministic enforcement (IAM scoping, input schema
  validation, and policy engines) and probabilistic content
  controls (input and output filtering, behavioral evaluation)
  operate at distinct stages of the call chain, so a failure
  at one layer rarely results in a boundary violation.
- Risk classification is deterministic, with high-risk
  operations routed to human review before execution and
  routine low-risk operations proceeding autonomously.
- Reviewers receive sufficient decision context, timeout
  policies, and escalation paths to make informed approvals
  without stalling the workflow or defaulting to
  rubber-stamping.
- Guardrail interventions, approval decisions, and evaluation
  results are logged, alerted on, and reviewed on a defined
  cadence to keep policies current with emerging patterns.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent goal alignment and manipulation prevention as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Operational boundaries exist only as natural-language<br>instructions in the system prompt. No content<br>guardrails, input validation, or human-in-the-loop<br>controls are in place. Alignment depends on the model<br>following instructions, and a single adversarial input<br>can redirect the agent with no defense in depth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 2     | Emerging  | [Amazon<br>Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") are configured with basic<br>[content<br>filters](../../../bedrock/latest/userguide/guardrails-content-filter.md "../../../bedrock/latest/userguide/guardrails-content-filter.md") covering inputs and outputs. A single<br>approval tier exists for a subset of consequential<br>actions, implemented through built-in mechanisms such as<br>[Amazon<br>Bedrock Agents user confirmation](../../../bedrock/latest/userguide/agents-userconfirmation.md "../../../bedrock/latest/userguide/agents-userconfirmation.md") or routed<br>through ad-hoc channels such as email or chat. Guardrail<br>interventions are captured in logs but reviewed<br>irregularly.                                                                                                                                                                                                                                                                           |
| 3     | Defined   | Tiered guardrail configurations align filter strengths<br>to each agent's use case, and<br>[denied<br>topics and word filters](../../../bedrock/latest/userguide/guardrails-content-filters-overview.md "../../../bedrock/latest/userguide/guardrails-content-filters-overview.md") are calibrated per risk<br>profile. Deterministic risk classification routes<br>approvals through a structured workflow mechanism such<br>as<br>[AWS Step Functions callback workflows](../../../step-functions/latest/dg/connect-to-resource.md "../../../step-functions/latest/dg/connect-to-resource.md") or<br>[return<br>of control](../../../bedrock/latest/userguide/agents-returncontrol.md "../../../bedrock/latest/userguide/agents-returncontrol.md"), with defined timeouts and escalation<br>paths.<br>[Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") fire on intervention spikes,<br>and guardrail versioning supports rollback of policy<br>changes. |
| 4     | Proactive | Validation runs at every stage of the call chain: input,<br>inference, output, and tool invocation.<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") run on a defined<br>cadence with alarms on correctness, tool selection<br>accuracy, and safety score drift. Persistent trust<br>grants are scoped narrowly by command and parameter<br>shape, tiered by risk, and made auditable and revocable.<br>Full decision context is written to durable storage<br>before approval notifications, and approval records are<br>linked to the centralized audit trail.                                                                                                                                                                                                                                                                                                                                                                                          |
| 5     | Optimized | Alignment controls are calibrated from intervention and<br>evaluation data, and risk classification adapts to<br>dynamic signals such as operation frequency, time of<br>day, and source location. Multi-reviewer consensus is<br>available for the highest-risk operations, including<br>asynchronous workflows running on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md"). Policy updates flow<br>through versioned configurations with provable change<br>history, and the feedback loop from logged interventions<br>back into policy is automated rather than manual.                                                                                                                                                                                                                                                                                                                                                                                           |

## Common issues to watch for

- Alignment is treated as a prompt-engineering exercise rather
  than a layered enforcement problem, so a single adversarial
  input that influences the model can collapse multiple
  boundaries at once.
- Content filtering is applied only to model outputs, leaving
  the inference path open to prompt injection and consuming
  capacity on adversarial inputs that could have been rejected
  up front.
- A single guardrail profile is applied to every agent, which
  either over-constrains low-risk informational agents or
  leaves high-risk operational agents under-constrained.
- Approval workflows either route every action through human
  review (producing reviewer fatigue and rubber-stamping) or
  skip review for operations that warrant it, giving the worst
  of both extremes.
- Risk classification is delegated to an LLM exposed to the
  same untrusted content as the request it is evaluating,
  which can be influenced into marking that request as
  low-risk.

###### Best practices

- [AGENTSEC04-BP01 Implement guardrails and alignment controls](agentsec04-bp01.md "agentsec04-bp01.md")
- [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](agentsec04-bp02.md "agentsec04-bp02.md")
