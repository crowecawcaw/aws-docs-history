# Secure agent inputs and outputs

Agents process inputs from users, tools, and other agents, and
they generate outputs for downstream systems, memory stores, and
end users. Without proper validation, adversarial inputs such as
prompt injection can influence agent behavior, and agent outputs
can inadvertently disclose sensitive information or generate
harmful content. Multi-layer validation at both the input and
output boundaries helps verify that agents operate safely within
their intended scope.

| AGENTSEC08: How do you validate and secure agent inputs<br>and outputs? |
| ----------------------------------------------------------------------- |
|                                                                         |

## Capability intent

- Every agent input surface (direct user messages, tool
  outputs, inter-agent messages, retrieved external content,
  and memory reads) has validation appropriate to its risk
  profile, with no input reaching the agent's reasoning
  process unchecked.
- Indirect prompt injection through retrieved documents, web
  pages, and API responses is treated as a first-class risk
  and filtered with the same rigor applied to direct user
  inputs.
- Agent outputs are inspected for personally identifiable
  information (PII), credentials, and other sensitive data on
  every outbound path (user responses, inter-agent messages,
  memory writes, and audit logs), with consistent masking or
  blocking applied at each boundary.
- Validation strictness is calibrated to the likelihood and
  impact of each risk scenario rather than applied uniformly,
  and telemetry on confidence scores, blocked content, and
  false-positive rates drives continual tuning.
- Filtering and guardrail decisions are logged with enough
  context to support compliance auditing, to detect systemic
  data leakage patterns, and to feed periodic re-optimization
  of denied topics, sample prompts, and filter thresholds.

## Maturity levels

These levels summarize what each stage of maturity looks like
for secure agent inputs and outputs as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Input validation, if present, runs only on direct user<br>messages. Retrieved external content, tool outputs,<br>inter-agent messages, and memory reads are treated as<br>trusted. Sensitive information in agent outputs is<br>controlled, if at all, by asking the model to<br>self-censor. Prompt injection and data leakage incidents<br>are found by users or downstream systems rather than by<br>controls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2     | Emerging  | [Amazon<br>Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") is deployed with<br>[prompt<br>attack detection](../../../bedrock/latest/userguide/guardrails-prompt-attack.md "../../../bedrock/latest/userguide/guardrails-prompt-attack.md") and basic<br>[sensitive<br>information filters](../../../bedrock/latest/userguide/guardrails-sensitive-info.md "../../../bedrock/latest/userguide/guardrails-sensitive-info.md") covering common PII<br>categories, primarily on user inputs and user-facing<br>responses. Denied topics are defined but not tuned<br>against representative data, and assessment modes use<br>default settings. Inter-agent messages, memory writes,<br>and tool outputs are covered inconsistently.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3     | Defined   | Every agent has its input surfaces mapped and a<br>validation control assigned to each, applied through the<br>[ApplyGuardrail<br>API](../../../bedrock/latest/APIReference/API_runtime_ApplyGuardrail.md "../../../bedrock/latest/APIReference/API_runtime_ApplyGuardrail.md") with prompt attack detection in block mode.<br>Output filtering runs on every outbound path, including<br>inter-agent messages, writes to<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md"), and audit logs, with<br>masking or blocking chosen per data classification.<br>Guardrail telemetry captures per-filter confidence<br>scores and blocked content in<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") for review.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 4     | Proactive | Guardrails configuration is tuned periodically using the<br>[Amazon<br>Bedrock Guardrails Optimizer](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer "https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer") against annotated<br>production samples. Denied topic definitions use the<br>full character budget with representative sample<br>prompts, and assessment modes are selected per filter<br>category based on likelihood and impact.<br>[Amazon Comprehend custom entity recognizers](../../../comprehend/latest/dg/custom-entity-recognition.md "../../../comprehend/latest/dg/custom-entity-recognition.md") extend<br>coverage to organization-specific data types, and<br>filtering decisions feed alarms that detect systemic<br>increases in sensitive-data generation or<br>blocked-content volume. Compliance auditing is in place:<br>guardrail and filtering decisions are written to<br>tamper-evident storage with the input, output,<br>intervention type, filter scores, and the originating<br>agent and user identity, retention is aligned to the<br>applicable regulatory framework, and standard audit<br>queries support reporting against frameworks such as the<br>EU AI Act, SOC 2, and HIPAA. |
| 5     | Optimized | Input validation and output filtering are self-tuning:<br>optimization runs on a schedule against fresh production<br>samples, false-positive and false-negative rates are<br>primary metrics, and validation telemetry is correlated<br>with runtime threat detection and penetration-test<br>findings to identify active exploitation. Content<br>retrieval is restricted to approved sources with runtime<br>attestation, and evolving attack patterns flow directly<br>into updated guardrails, denied topics, and filter<br>thresholds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Common issues to watch for

- Input and output boundaries receive uneven defense, with
  rigorous checks on user inputs but little coverage for tool
  outputs, retrieved external content, inter-agent messages,
  and memory reads, leaving the most commonly targeted vectors
  unprotected.
- Guardrails are treated as a one-time configuration rather
  than a tuning loop, so denied topic definitions, filter
  thresholds, and assessment modes decay as attack patterns
  and data classifications change.
- Guardrail and filtering decisions are not captured with
  enough context to tell when validation is degrading or which
  categories need retuning, so quality issues stay invisible
  until an incident surfaces them.
- Sensitive information controls lean on the model to
  self-censor rather than on enforced output filtering, so PII
  and credentials pulled in from tool outputs or retrieved
  documents flow through whenever the model repeats them.
- Filter rules are either overly broad, which erodes user
  trust and pushes teams to weaken or disable them, or overly
  narrow, which leaves gaps. Neither side has a feedback loop
  against annotated outcomes to calibrate strictness by risk
  scenario.

###### Best practices

- [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.md "agentsec08-bp01.md")
- [AGENTSEC08-BP02 Output filtering for sensitive information](agentsec08-bp02.md "agentsec08-bp02.md")
