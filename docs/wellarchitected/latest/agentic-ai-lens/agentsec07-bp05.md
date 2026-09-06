

# AGENTSEC07-BP05 Regular security assessments and red teaming
<a name="agentsec07-bp05"></a>

 Untested security controls degrade quietly as techniques evolve and configurations drift. A combination of continuous automated scanning and periodic human-led red team exercises validates that guardrails, detection rules, and response procedures still work against current attacks. 

 **Desired outcome:** 
+  You run automated security scanning continuously against agent deployments (on each deploy and on schedule) and conduct human-led red team exercises on a regular cadence with scenarios targeting agent manipulation, including prompt injection, goal hijacking, and tool misuse. 
+  You document findings, track them to remediation, and use them to update security controls and detection rules. 

 **Common anti-patterns:** 
+  Conducting generic application security assessments without agent-specific scenarios, missing prompt injection, memory poisoning, and multi-agent coordination issues that traditional testing doesn't cover. 
+  Performing red team exercises only at initial deployment without scheduling regular assessments, missing techniques that emerge as the threat environment evolves. 
+  Not tracking findings to remediation, letting identified issues persist so the assessment produces work but no posture improvement. 
+  Conducting red team and blue team activities in isolation without purple team collaboration, limiting the knowledge transfer that improves detection and response. 

 **Benefits of establishing this best practice:** 
+  Realistic testing confirms guardrails, detection rules, and response procedures work against current techniques. 
+  Assessment findings drive updates to guardrail configurations, permission boundaries, and detection rules in a continuous feedback loop. 
+  Purple team activities transfer knowledge from red to blue teams, improving the organization's ability to detect and respond to agent-specific issues. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The assessment cadence needs to match the risk level of each agent deployment. Automated scanning runs continuously, and manual red team exercises run on a schedule. For automated agentic testing, [AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing that executes attack chains adapted to the target application, covering prompt injection, jailbreaking, goal hijacking, and related patterns (see AGENTSEC09-BP02 for integrating it into broader penetration testing workflows). Supplement automated testing with manual exercises that explore novel scenarios specific to your agent architecture. 

 Red team scenarios need structure. The [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) covers agent manipulation risks specifically, prompt injection, tool misuse, identity and privilege abuse, and agent behavior hijacking, and the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) covers model-level risks that still apply. Build a scenario library that covers multi-agent coordination issues, memory poisoning, tool misuse, and human-in-the-loop bypass techniques, and document each scenario with description, expected detection mechanism, and success criteria. 

 [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) supports the assessment process by providing a continuous quality baseline. Running evaluations before and after red team exercises measures whether the exercise exposed quality degradation that the existing evaluators did not catch, and the results refine custom evaluator prompts and scoring thresholds. 

 Durable, versioned storage keeps the historical record intact. Store scenarios, execution results, and remediation tracking in Amazon S3 with versioning enabled, or in a dedicated test management system that maintains change history. Map red team findings to your compliance control framework so assessment results produce audit evidence consistent with your regulatory requirements. 

 Purple team activities close the loop. Bringing red team and blue team together to review scenarios and detection responses updates Amazon CloudWatch alarms, Guardrails configurations, and incident response runbooks based on observed patterns. Tracking improvements in detection time and response effectiveness across cycles demonstrates the program's value. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish an assessment schedule:** Set a cadence appropriate for each agent deployment's risk level. 

1.  **Build a scenario library:** Develop red team scenarios based on the OWASP Top 10 for Agentic Applications (primary) and the OWASP Top 10 for LLM Applications (supplementary), covering prompt injection, memory poisoning, tool misuse, and HITL bypass. 

1.  **Integrate automated agentic testing:** Deploy agentic AI red teaming tools and include them in the assessment workflow for automated coverage of common patterns. 

1.  **Measure quality impact before and after:** Run [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) before and after red team exercises to measure quality impact and refine evaluator configurations. 

1.  **Persist and map findings:** Store scenarios, results, and remediation tracking in durable, versioned storage (Amazon S3 with versioning enabled), and map findings to your compliance control framework for audit evidence. 

1.  **Run purple team sessions:** Update detection rules, guardrail configurations, and incident response runbooks based on each assessment cycle's findings. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC04-BP01 Implement guardrails and alignment controls](agentsec04-bp01.html) 
+  [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.html) 
+  [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.html) 

 **Related documents:** 
+  [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) 
+  [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) 
+  [AWS Security Agent](https://aws.amazon.com/security-agent/) 
+  [Responsible AI in action: How Data Reply red teaming supports generative AI safety on AWS](https://aws.amazon.com/blogs/machine-learning/responsible-ai-in-action-how-data-reply-red-teaming-supports-generative-ai-safety-on-aws/) 
+  [Protect DeepSeek model deployments with Protect AI and Amazon Bedrock](https://aws.amazon.com/blogs/apn/protect-deepseek-model-deployments-with-protect-ai-and-amazon-bedrock/) 
+  [Amazon Bedrock AgentCore adds quality evaluations and policy controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 