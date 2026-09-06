

# AGENTSEC08-BP02 Output filtering for sensitive information
<a name="agentsec08-bp02"></a>

 Filtering user-facing responses leaves internal data paths (inter-agent messages, memory writes, audit logs) as open channels for PII and credentials to escape. Scanning every output path with a data classification policy keeps sensitive content inside the agent's authorized handling scope. 

 **Desired outcome:** 
+  You scan agent outputs for PII, credentials, and other sensitive data before returning them to users or downstream systems, with content masked or blocked based on data classification policies. 
+  Agent outputs containing credentials, private keys, or regulated PII are blocked or masked before they reach end users or external systems. 
+  You log output filtering decisions for compliance auditing. 

 **Common anti-patterns:** 
+  Relying on the model to self-censor sensitive information, when models do generate outputs containing PII or credentials (especially when that information is in the agent's context from tool outputs or retrieved documents). 
+  Applying output filtering only to user-facing responses while skipping filtering for outputs passed to other agents or stored in memory, creating data-leakage paths through internal communications. 
+  Using overly broad masking rules that mask legitimate content alongside sensitive data, degrading output quality to the point users work around the filter. 

 **Benefits of establishing this best practice:** 
+  Data classification enforcement at the agent boundary helps keep sensitive information within the agent's authorized data-handling scope regardless of what the model generates. 
+  Logged filtering decisions support compliance with data protection regulations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every output path is a potential exfiltration path. User-facing responses are the obvious one, but an agent also writes to memory, passes content to other agents, and emits logs. Filtering only the user-facing path leaves the others as open channels for sensitive data, and adversarial inputs designed to exfiltrate data don't consistently target the user-facing channel. The architectural requirement is that every output surface passes through the same filter, not just the ones users see. 

 [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) sensitive information filters cover the data types relevant to most use cases: 
+  PII categories (names, addresses, phone numbers, email addresses, SSNs, and financial account numbers) 
+  Credentials (API keys, passwords, and private keys) 
+  Custom entity types specific to your organization 

 Configure the filter action as MASK for most sensitive data types to preserve output utility while protecting sensitive content, and BLOCK for the most sensitive categories such as credentials and private keys where masking isn't enough. 

 Apply the filter as middleware in the agent output pipeline, so every output destination, user-facing responses, inter-agent messages, [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) writes through the create\_event API, and audit logs, flows through it. AgentCore Memory's built-in long-term memory strategies already filter PII from extracted long-term records by default, but short-term memory (raw events) retains original content, so compliance requirements that prohibit PII in any stored form require applying Guardrails sensitive information filters before writing events to short-term memory as well. 

 For organization-specific sensitive data types not covered by built-in categories, Amazon Comprehend custom entity recognizers extend coverage. Train recognizers on examples of your sensitive data types and integrate them into the output filtering pipeline through AWS Lambda functions that call the Amazon Comprehend API before returning outputs. 

 Logging every filtering decision (the type of sensitive data detected, the action taken (mask or block), the output destination) produces the data loss prevention report and catches patterns where the agent is systematically generating outputs containing sensitive data (a signal of prompt injection or data exfiltration). Amazon CloudWatch alarms on elevated detection rates turn that signal into an active alert. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure sensitive information filters:** Set up [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) with filters for all relevant PII and credential categories, choosing MASK or BLOCK per category based on data classification policy. 

1.  **Filter every output path:** Apply output filtering as a middleware layer for user-facing responses, inter-agent messages, memory writes, and audit logs. 

1.  **Filter before short-term memory writes when required:** For compliance requirements that prohibit PII in any stored form, apply Guardrails filtering before writing events to [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) short-term storage. 

1.  **Extend with Amazon Comprehend custom entities:** Train Amazon Comprehend custom entity recognizers for organization-specific sensitive data types and integrate them into the filtering pipeline. 

1.  **Log and alarm on detections:** Log all output filtering decisions with data type, action, and destination metadata, and configure Amazon CloudWatch alarms for elevated sensitive data detection rates. 

1.  **Review configurations periodically:** Adjust output filtering to match evolving data classification policies and new regulated data types. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 
+  [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) 
+  [Amazon Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) 
+  [Amazon Comprehend documentation](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon Comprehend](https://aws.amazon.com/comprehend/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 