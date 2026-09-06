

# Secure agent inputs and outputs
<a name="agentsec08"></a>

 Agents process inputs from users, tools, and other agents, and they generate outputs for downstream systems, memory stores, and end users. Without proper validation, adversarial inputs such as prompt injection can influence agent behavior, and agent outputs can inadvertently disclose sensitive information or generate harmful content. Multi-layer validation at both the input and output boundaries helps verify that agents operate safely within their intended scope. 


|  AGENTSEC08: How do you validate and secure agent inputs and outputs?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-7"></a>
+  Every agent input surface (direct user messages, tool outputs, inter-agent messages, retrieved external content, and memory reads) has validation appropriate to its risk profile, with no input reaching the agent's reasoning process unchecked. 
+  Indirect prompt injection through retrieved documents, web pages, and API responses is treated as a first-class risk and filtered with the same rigor applied to direct user inputs. 
+  Agent outputs are inspected for personally identifiable information (PII), credentials, and other sensitive data on every outbound path (user responses, inter-agent messages, memory writes, and audit logs), with consistent masking or blocking applied at each boundary. 
+  Validation strictness is calibrated to the likelihood and impact of each risk scenario rather than applied uniformly, and telemetry on confidence scores, blocked content, and false-positive rates drives continual tuning. 
+  Filtering and guardrail decisions are logged with enough context to support compliance auditing, to detect systemic data leakage patterns, and to feed periodic re-optimization of denied topics, sample prompts, and filter thresholds. 

## Maturity levels
<a name="maturity-levels-7"></a>

 These levels summarize what each stage of maturity looks like for secure agent inputs and outputs as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Input validation, if present, runs only on direct user messages. Retrieved external content, tool outputs, inter-agent messages, and memory reads are treated as trusted. Sensitive information in agent outputs is controlled, if at all, by asking the model to self-censor. Prompt injection and data leakage incidents are found by users or downstream systems rather than by controls.  | 
|  2  |  Emerging  |  [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) is deployed with [prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html) and basic [sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) covering common PII categories, primarily on user inputs and user-facing responses. Denied topics are defined but not tuned against representative data, and assessment modes use default settings. Inter-agent messages, memory writes, and tool outputs are covered inconsistently.  | 
|  3  |  Defined  |  Every agent has its input surfaces mapped and a validation control assigned to each, applied through the [ApplyGuardrail API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html) with prompt attack detection in block mode. Output filtering runs on every outbound path, including inter-agent messages, writes to [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html), and audit logs, with masking or blocking chosen per data classification. Guardrail telemetry captures per-filter confidence scores and blocked content in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for review.  | 
|  4  |  Proactive  |  Guardrails configuration is tuned periodically using the [Amazon Bedrock Guardrails Optimizer](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer) against annotated production samples. Denied topic definitions use the full character budget with representative sample prompts, and assessment modes are selected per filter category based on likelihood and impact. [Amazon Comprehend custom entity recognizers](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html) extend coverage to organization-specific data types, and filtering decisions feed alarms that detect systemic increases in sensitive-data generation or blocked-content volume. Compliance auditing is in place: guardrail and filtering decisions are written to tamper-evident storage with the input, output, intervention type, filter scores, and the originating agent and user identity, retention is aligned to the applicable regulatory framework, and standard audit queries support reporting against frameworks such as the EU AI Act, SOC 2, and HIPAA.  | 
|  5  |  Optimized  |  Input validation and output filtering are self-tuning: optimization runs on a schedule against fresh production samples, false-positive and false-negative rates are primary metrics, and validation telemetry is correlated with runtime threat detection and penetration-test findings to identify active exploitation. Content retrieval is restricted to approved sources with runtime attestation, and evolving attack patterns flow directly into updated guardrails, denied topics, and filter thresholds.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-7"></a>
+  Input and output boundaries receive uneven defense, with rigorous checks on user inputs but little coverage for tool outputs, retrieved external content, inter-agent messages, and memory reads, leaving the most commonly targeted vectors unprotected. 
+  Guardrails are treated as a one-time configuration rather than a tuning loop, so denied topic definitions, filter thresholds, and assessment modes decay as attack patterns and data classifications change. 
+  Guardrail and filtering decisions are not captured with enough context to tell when validation is degrading or which categories need retuning, so quality issues stay invisible until an incident surfaces them. 
+  Sensitive information controls lean on the model to self-censor rather than on enforced output filtering, so PII and credentials pulled in from tool outputs or retrieved documents flow through whenever the model repeats them. 
+  Filter rules are either overly broad, which erodes user trust and pushes teams to weaken or disable them, or overly narrow, which leaves gaps. Neither side has a feedback loop against annotated outcomes to calibrate strictness by risk scenario. 

**Topics**
+ [Capability intent](#capability-intent-7)
+ [Maturity levels](#maturity-levels-7)
+ [Common issues to watch for](#common-issues-to-watch-for-7)
+ [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.md)
+ [AGENTSEC08-BP02 Output filtering for sensitive information](agentsec08-bp02.md)