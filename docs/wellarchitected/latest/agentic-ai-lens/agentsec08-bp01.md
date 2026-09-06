

# AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense
<a name="agentsec08-bp01"></a>

 Agents take input from many surfaces and only one needs to be unvalidated for adversarial content to reach the agent's reasoning process. A layered validation architecture covers every surface, and in particular catches the indirect prompt injection embedded in retrieved external content. 

 **Desired outcome:** 
+  Every input surface has a validation layer appropriate to its risk profile, and no input reaches the agent's reasoning process without passing through at least one validation control. 
+  You specifically address indirect prompt injection through retrieved external content, which is the surface most commonly missed when validation is applied only to direct user inputs. 

 **Common anti-patterns:** 
+  Applying input validation only to direct user inputs while skipping validation for data retrieved from external sources, letting embedded instructions in web pages, documents, and API responses bypass user-facing validation. 
+  Validating at one input surface but not others (for example, validating user inputs with Guardrails but not validating tool outputs before they enter the agent's context), creating gaps that can be targeted. 
+  Defining denied topics with vague or overly broad descriptions that generate false positives on legitimate content, eroding trust and prompting teams to weaken or disable guardrails entirely. 

 **Benefits of establishing this best practice:** 
+  Defense-in-depth architecture where each input surface has validation appropriate to its risk profile helps cover every surface. 
+  Validation of external content before it enters the agent's context closes the most commonly missed gap: indirect prompt injection. 
+  Confidence-based assessment modes let organizations tune validation strictness per filter category based on the likelihood and impact of each risk scenario. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Input surfaces to an agent are not one thing. Direct user messages, tool outputs, inter-agent messages, retrieved external content (web pages, documents, API responses), and memory reads are all paths by which data reaches the agent's context, and each needs a validation control. Surface-specific guidance lives in AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool parameters), and AGENTSEC04-BP01 (goal alignment guardrails). This best practice is the architectural framing and focuses on the cross-cutting concern those others don't cover: indirect prompt injection through external content retrieval. 

 External content retrieval is the most commonly missed surface. When an agent uses RAG, web browsing, or API calls to gather information during task execution, the retrieved content becomes part of the agent's context, and adversarial instructions embedded in that content (indirect prompt injection) influence the agent's behavior as effectively as a direct user injection. Apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection to all retrieved content before it enters the agent's context, and implement content source validation that restricts the agent to retrieving content from approved domains or data sources where feasible. 

 Guardrails provides a unified validation mechanism that can be applied across multiple input surfaces through the ApplyGuardrail API. Configure a guardrail with prompt attack detection, denied topics, and word filters once, and apply it at each input boundary. That gives you consistent policy enforcement across surfaces with surface-specific tuning through guardrail versioning. 

 Two assessment modes matter: block mode returns a binary allow or deny decision, and detect mode returns confidence scores for each filter category without blocking the request. Use block mode for prompt attack detection, where even low-confidence matches warrant intervention given the severity of potential impact. For content safety filters on internal or lower-risk applications, detect mode lets the application make risk-proportionate decisions based on the confidence scores returned. Score each risk scenario by likelihood and impact to determine appropriate confidence thresholds per filter category rather than applying uniform thresholds. 

 Denied topics use probabilistic, LLM-based evaluation to determine whether content matches a topic definition, and definition quality drives accuracy. Use the full 1,000-character limit for each denied topic definition with specific and unambiguous descriptions, and populate all five sample prompt fields (up to 200 characters each) with representative examples that illustrate the boundary between restricted and permitted content. Vague or broad definitions inflate false positive rates, which erodes user trust and pressures teams to weaken or disable guardrails. 

 When using the ApplyGuardrail API directly (rather than through the Converse API or Amazon Bedrock Agents), guardrail assessment results are not automatically published to Amazon CloudWatch. You are responsible for the telemetry pipeline that captures assessment outcomes, confidence scores, and blocked content. Set the outputScope parameter to full on ApplyGuardrail API calls to receive complete assessment data including per-filter confidence scores, which are essential for adjusting thresholds and feeding the Guardrails Optimizer. Log both the request content and the assessment response for blocked items, this data is required for ongoing configuration refinement and false-positive analysis. 

 The Amazon Bedrock Guardrails Optimizer is a reference implementation on AWS Samples that automates guardrail configuration refinement. It uses a Strands Agent to iteratively adjust denied topic definitions, sample prompts, and filter thresholds based on annotated test data. As opposed to model fine-tuning, this is policy configuration optimization. The agent analyzes failed test cases, rewrites the guardrail configuration, re-evaluates against the test dataset, and repeats until target accuracy is reached. Prepare a representative dataset annotated with expected outcomes (allow or deny for each filter category), run the Optimizer during initial guardrail setup, and schedule periodic re-runs (monthly or quarterly) using samples from production traffic to adapt to evolving content patterns and reduce false positive rates over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map input surfaces and assign controls:** Identify all input surfaces for each agent and the validation control covering each surface, flagging any that are currently unvalidated. 

1.  **Validate retrieved external content:** Configure [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection and apply it to external content (RAG results, web content, API responses) before it enters the agent's context. 

1.  **Pick assessment mode by risk:** Use block mode for prompt attack detection filters and consider detect mode for content safety filters on lower-risk applications, implementing application-level logic to make risk-proportionate decisions based on returned confidence scores. 

1.  **Write precise denied topics:** Use the full 1,000-character limit for each denied topic definition and populate all five sample prompt fields with representative examples that illustrate the boundary between restricted and permitted content. 

1.  **Capture ApplyGuardrail telemetry:** Set outputScope to full on all ApplyGuardrail API calls and implement a telemetry pipeline to capture assessment outcomes, confidence scores, and blocked content in Amazon CloudWatch. 

1.  **Run the Guardrails Optimizer:** Run the Amazon Bedrock Guardrails Optimizer with an annotated test dataset during initial setup, then schedule periodic re-optimization (monthly or quarterly) using samples from production traffic. 

1.  **Restrict content sources where feasible:** Implement content source validation that restricts agents to retrieving content from approved domains or data sources. 

1.  **Verify surface-specific controls exist:** Confirm that the controls described in AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool parameters), and AGENTSEC04-BP01 (goal alignment guardrails) are implemented for each applicable agent. 

1.  **Log and review blocked inputs:** Log all blocked inputs across surfaces and review patterns periodically to identify new techniques and surfaces that may need additional coverage. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC01-BP02 Validate and sanitize memory inputs](agentsec01-bp02.html) 
+  [AGENTSEC02-BP02 Validate tool inputs and outputs](agentsec02-bp02.html) 
+  [AGENTSEC04-BP01 Implement guardrails and alignment controls](agentsec04-bp01.html) 
+  [AGENTSEC08-BP02 Output filtering for sensitive information](agentsec08-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html) 
+  [Amazon Bedrock Guardrails denied topics](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html) 
+  [Amazon Bedrock Guardrails ApplyGuardrail API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html) 
+  [Build responsible AI applications with Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/) 
+  [Best practices with Amazon Bedrock Guardrails filter configuration](https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails/) 
+  [Amazon Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) 

 **Related examples:** 
+  [Amazon Bedrock Guardrails Evaluation and Optimization Framework](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 