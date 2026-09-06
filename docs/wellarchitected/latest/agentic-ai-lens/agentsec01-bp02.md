

# AGENTSEC01-BP02 Validate and sanitize memory inputs
<a name="agentsec01-bp02"></a>

 Unvalidated writes into agent memory let adversarial content persist and influence every subsequent session that reads the same context. Layered validation at ingestion keeps the memory store free of injection payloads, policy-violating content, and context inconsistent with the current task. 

 **Desired outcome:** 
+  You validate all data entering agent memory for type, format, and content before storage, and reject or quarantine policy-violating inputs before they influence agent behavior. 
+  You detect and block injection attempts at the memory ingestion layer and route suspicious inputs to human review. 
+  Your memory store contains only schema-conformant, sanitized data that downstream agents can consume safely. 

 **Common anti-patterns:** 
+  Storing raw, unvalidated user inputs directly into agent memory, letting prompt injection payloads persist and influence future sessions as agents build reasoning chains on top of affected context. 
+  Validating only at the public API boundary while skipping validation for content that enters memory from other write paths, including tool outputs, inter-agent messages, and memory consolidation. 
+  Failing to scan for encoded or obfuscated injection payloads, missing base64-encoded instructions, Unicode homoglyph substitutions, and other obfuscation that bypasses keyword-based filters but is still interpreted by downstream models. 

 **Benefits of establishing this best practice:** 
+  Multi-layer validation catches issues at syntactic, semantic, and contextual levels before data reaches the memory store. 
+  Blocking adversarial content at the ingestion boundary helps prevent it from influencing agent reasoning or propagating to downstream agents. 
+  Validation metrics surface trends in rejection rates and issue patterns, turning ingestion controls into operational signal. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every write into agent memory is a trust decision. Raw user inputs are the obvious write path, but they are not the only one. Tool outputs arrive from search APIs, databases, and third-party services the agent queries. Inter-agent messages carry content one agent wrote into another's scope, and memory consolidation generates long-term records by summarizing or merging existing events. Each of these is a distinct ingestion path, and each needs the same validation treatment. Validating only at the public API boundary leaves the other three open. 

 A layered pipeline gives each category of issue somewhere to be caught. Syntactic validation against a JSON Schema rejects wrong types, over-long strings, and missing fields before anything semantic happens. Semantic validation with [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) detects prompt injection attempts, denied topics, and content that violates organizational guidelines through the ApplyGuardrail API, which evaluates content independently of model invocations so you can run it at any point in the pipeline. Contextual validation checks whether an input is consistent with the current task and flags anomalies for review. 

 [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) gives this pipeline a natural integration point. Because long-term memory extraction runs asynchronously from event ingestion, running Guardrails before events are written through the create\_event API blocks harmful content from entering the extraction pipeline, and running Guardrails again before consolidation catches anything that made it past the first check. The built-in memory strategies already filter PII from long-term records by default, but that isn't a substitute for injection and policy enforcement, which must be added on top. 

 The shared responsibility model matters here. AWS is responsible for the AgentCore Memory infrastructure. You are responsible for secure application development, input validation, and helping prevent prompt injection in the memory extraction service. The [AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) specifically recommend sanitizing user input with guardrails before persisting through CreateEvent. If your memory writes originate from HTTP APIs you already operate, AWS WAF in front of those APIs adds a network-layer tier, and Amazon API Gateway request validation enforces schema constraints at the same layer. For writes that happen entirely in agent code through direct SDK calls, validating in the agent code before create\_event is the simpler path. 

 Failed inputs need a tiered response. Clearly harmful inputs are blocked and logged. Ambiguous inputs go to an Amazon SQS quarantine queue for human review, stored with enough context (agent ID, session ID, timestamp, and source) to support investigation. All validation failures emit Amazon CloudWatch metrics so rejection-rate trends become visible and configurable into alarms when something changes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define JSON schemas for every memory input type:** Specify field types, length limits, allowed values, and required fields so the first validation layer can reject malformed inputs deterministically. 

1.  **Configure Guardrails for semantic validation:** Configure [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with denied topics, word filters, and sensitive information filters tuned to your security policies, and use the ApplyGuardrail API so validation is independent of model invocations. 

1.  **Validate every write path, not just user input:** Apply Guardrails to tool outputs and inter-agent messages as well as user-provided content before any of them reach the memory store. 

1.  **Validate before create\_event:** Run validation on events before they enter [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) short-term storage through create\_event, so harmful content doesn't enter the asynchronous long-term extraction pipeline. 

1.  **Add AWS WAF on API-fronted memory writes:** Deploy AWS WAF managed rule groups on Amazon API Gateway endpoints that accept memory inputs, enforcing network-layer injection filtering before requests reach application code. 

1.  **Quarantine ambiguous inputs for review:** Route failures into an Amazon SQS queue with agent ID, session ID, timestamp, and source, so humans can review without blocking the pipeline. 

1.  **Emit validation telemetry:** Publish Amazon CloudWatch metrics for every validation outcome (pass, block, or quarantine) and alarm on elevated rejection rates that suggest an active issue. 

1.  **Review quarantined inputs regularly:** Use the quarantine queue to identify new attack patterns, update Guardrail configurations, and refine validation rules over time. 

1.  **Test for injection continually:** Apply penetration testing, static code analysis, and dynamic application security testing (DAST) to the memory write paths as part of regular security validation. 

1.  **Enforce IAM conditions on CreateEvent:** Use IAM Access Analyzer to validate that memory resource policies follow least privilege, and add policy conditions that restrict which roles can call the CreateEvent API for specific AgentCore Memory resources. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC01-BP01 Implement memory isolation and integrity controls](agentsec01-bp01.html) 
+  [AGENTSEC01-BP03 Monitor for hallucination propagation](agentsec01-bp03.html) 
+  [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) 
+  [Amazon Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) 
+  [Amazon Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/) 
+  [AWS WAF developer guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 