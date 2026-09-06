

# AGENTSEC04-BP01 Implement guardrails and alignment controls
<a name="agentsec04-bp01"></a>

 Instruction-following alone doesn't provide reliable enforcement. Layered controls (deterministic where possible, probabilistic where necessary) help keep agents inside operational boundaries even when prompts are adversarial and model behavior is unpredictable. 

 **Desired outcome:** 
+  You define agent operational and policy boundaries up front and enforce them through layered controls, with deterministic controls (IAM, schema validation, technical policy checks) handling what is expressible deterministically and probabilistic controls (content filters, behavioral evaluation) handling what isn't. 
+  Multiple validation layers at different stages of the agent call chain can reduce the likelihood that a single control failure results in a boundary violation. 
+  You log, alert on, and periodically review guardrail interventions, policy violations, and behavioral evaluation results to tune the controls and surface emerging patterns. 

 **Common anti-patterns:** 
+  Relying on a single guardrail configuration for all agent use cases, applying the same constraints to low-risk informational agents and high-risk operational agents. 
+  Applying content filtering only to model outputs without validating inputs first, letting adversarial content reach the model before any check runs. 
+  Defining operational boundaries in natural-language system prompts alone, relying on the model's instruction-following as the sole constraint, which can be bypassed through prompt injection or adversarial framing. 

 **Benefits of establishing this best practice:** 
+  Deterministic technical controls (IAM, schema validation) combined with probabilistic content controls (Guardrails) at distinct stages reduce reliance on instruction-following alone. 
+  Layered validation catches policy violations at multiple stages, so a bypass at one layer is less likely to result in an unchecked boundary violation. 
+  Logged guardrail interventions and evaluation results feed policy updates as new patterns emerge, keeping boundaries current with evolving use cases. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Operational boundaries written only in system prompts typically don't provide reliable enforcement. A prompt can be overridden by adversarial framing, prompt injection, or the model's own creative reinterpretation, and none of those failure modes produces an audit signal before the boundary has already been crossed. The design pattern is layered. Express what can be expressed deterministically as hard checks: 
+  IAM scoping 
+  Schema validation 
+  Cedar policies 
+  Permission boundaries 

 Use probabilistic controls (content filters, behavioral evaluation) to cover the content-shaped risks that determinism can't reach. 

 [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) is the probabilistic layer. Configure a base guardrail with universal constraints (no generation of harmful content, no disclosure of system prompts), then overlay use-case-specific configurations for each agent's operational context. Content filter strengths need calibration to use case sensitivity: HIGH strength for consumer-facing agents handling categories like hate speech, violence, and sexual content, MEDIUM strength for internal enterprise agents, and custom thresholds for specialized domains (medical, legal) with their own content norms. Content moderation needs to apply to every output path, including outputs used in internal agent workflows and inter-agent messages, not just user-facing responses. Use Guardrails versioning for change management with rollback. 

 Pre-execution validation matters for two reasons. Applying Guardrails to user inputs before they reach the model blocks adversarial content before it influences reasoning, and it rejects bad inputs before they consume inference capacity. When an agent invokes an Amazon Bedrock model with a guardrail attached, the check runs automatically on inputs and outputs. The ApplyGuardrail API runs the same policy independently when the automatic path doesn't apply, agents that invoke non-Amazon Bedrock models (third-party APIs, self-hosted models), pipelines that need to filter content before deciding whether to invoke a model at all (for example, checking retrieved content before it enters the prompt), or additional validation checkpoints beyond the model invocation. 

 Monitoring closes the feedback loop. The [Amazon Bedrock Guardrails CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html) include InvocationsIntervened, broken down by Operation (ApplyGuardrail) and GuardrailContentSource (Input / Output) so input-side and output-side interventions are visible separately. Amazon CloudWatch alarms on intervention rates route through Amazon SNS to the security team. For the detail (what was blocked, which policy triggered, which part of the content was affected), enable Amazon Bedrock model invocation logging, which captures the full guardrail trace for each call. Analyze intervention patterns over time to find emerging techniques that require policy updates and to catch filter categories generating excessive false positives or false negatives. 

 [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) assesses goal attainment correctness and tracks whether agents are achieving their intended objectives rather than drifting into misaligned goals. Built-in evaluators cover correctness, helpfulness, tool selection accuracy, and safety. Custom model-based evaluators extend coverage to organization-specific alignment requirements. Run evaluations on a regular cadence and after any significant change to agent prompts, tools, or guardrail configurations. Results publish to Amazon CloudWatch alongside AgentCore Observability insights for a unified view, and CloudWatch alarms on evaluation scores catch behavioral drift outside acceptable thresholds. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map ethical constraints to guardrail categories:** Define organizational ethical constraints and operational boundaries per agent use case and map them to guardrail policy categories with risk-appropriate differentiation. 

1.  **Build tiered guardrail configurations:** Create base and use-case-specific [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) configurations, apply them to all deployments, and use versioning for rollback capability. 

1.  **Validate inputs before inference:** Call the ApplyGuardrail API on inputs before they reach the model, checking against denied topics, word filters, and sensitive information patterns. 

1.  **Alarm on intervention metrics:** Configure Amazon CloudWatch alarms on Guardrails metrics (especially InvocationsIntervened), route alerts through Amazon SNS, and enable Amazon Bedrock model invocation logging for detailed intervention records. 

1.  **Deploy AgentCore Evaluations with drift alarms:** Deploy [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with built-in and custom evaluators, and configure Amazon CloudWatch alarms on evaluation scores to detect behavioral drift. 

1.  **Review intervention logs monthly:** Establish a monthly review of guardrail intervention logs to identify emerging patterns and update policies accordingly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](agentsec04-bp02.html) 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 
+  [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) 
+  [Amazon Bedrock Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filter.html) 
+  [Build responsible AI applications with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/) 
+  [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Amazon Bedrock AgentCore adds quality evaluations and policy controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) 
+  [AI agents in enterprises: Best practices with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 