

# AGENTSEC02-BP02 Validate tool inputs and outputs
<a name="agentsec02-bp02"></a>

 Agents generate tool parameters from model output, which means malformed or adversarial inputs can reach tools through ordinary reasoning, not just through unauthorized callers. Schema-driven validation on inputs and sanitization on outputs keep tools operating inside their intended parameter space and help prevent error messages from disclosing internal system details. 

 **Desired outcome:** 
+  You validate every parameter passed to tools against a defined schema before execution, and sanitize tool outputs before returning them to the agent. 
+  Injection through tool parameters is blocked, oversized inputs are prevented from exhausting resources, and error messages are sanitized to avoid leaking sensitive system information. 
+  Tool invocations operate predictably within defined boundaries, and validation failures are logged for security analysis. 

 **Common anti-patterns:** 
+  Passing raw agent-generated parameters directly to tools without type checking or range validation, letting malformed inputs cause unexpected behavior or injection. 
+  Returning raw tool error messages to the agent without sanitization, exposing internal system details, stack traces, or infrastructure information usable for further probing. 
+  Validating only user-provided inputs and skipping validation for parameters produced by the agent's reasoning, on the assumption the model can't generate malformed output. 

 **Benefits of establishing this best practice:** 
+  Schema-enforced input validation helps prevent tools from operating outside their intended parameter space. 
+  Sanitized error responses return failure categories without exposing internal system details. 
+  Timeout controls, memory limits, and output-size enforcement help prevent resource exhaustion from oversized or long-running tool invocations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Validation is more useful when it happens at several layers than when any single layer tries to do all the work. The cheapest and most specific layer is at the model itself. Amazon Bedrock structured outputs with strict tool use constrain the model's decoding so that generated tool parameters always conform to the defined input schema. Setting strict: true on the tool definition, together with additionalProperties: false and enum constraints on fields with a closed set of values, helps prevent malformed parameters as a class before they ever reach the tool. That doesn't replace application validation, but it removes a large chunk of the work from it. The [Structured outputs on Amazon Bedrock blog](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/) covers the parameter shapes and the model-level enforcement. 

 The next layer is schema validation in the tool invocation pipeline. For tools deployed as AWS Lambda functions, a JSON Schema check inside the Lambda handler, or a shared Lambda Layer, enforces type constraints, value ranges, string length limits, and format patterns before the function logic runs. This is the place to catch the edge cases strict tool use doesn't cover, anything involving relationships between fields, external-state constraints, or values the model can't know. 

 Policy in Amazon Bedrock AgentCore provides a third layer at the gateway. Cedar policies can evaluate conditions on tool input parameters through context.input, so business rules like "financial amount below an approved threshold" or "date parameter within an acceptable range" are enforced deterministically at the gateway before the call reaches the backend. The value of this layer is that the rules are auditable and managed independently of tool code. The value of keeping it separate from the first two layers is that changes to business rules don't require redeploying tools. 

 Logical constraints that are not expressible as schema or simple comparisons need a different mechanism. [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning checks verify that tool parameters conform to logical constraints, a date range with start before end, a set of values that must be mutually consistent. Apply Guardrails at the AWS Organization level where consistent policy enforcement is required across all agent deployments. 

 Resource protection and error sanitization complete the picture. AWS Lambda function timeout and memory limits, sized to each tool's measured execution profile, bound what any single call can consume, and Lambda reserved concurrency caps total parallel invocations. Tool outputs that return large datasets need size limits and pagination. Truncation events belong in the log so an agent doesn't silently reason on a partial response. Error handling catches exceptions and returns structured responses that describe the failure category without exposing internal details, stack traces, or infrastructure information. AWS WAF managed rule groups on API-based tool endpoints add a network-layer filter for common injection patterns before requests reach tool code. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Constrain parameters at the model layer:** Enable strict tool use (strict: true) on tool definitions in Amazon Bedrock, set additionalProperties: false on all input schemas, and define enum constraints for fields with a limited set of valid values to block malformed parameters at decoding. 

1.  **Enforce schemas in the invocation pipeline:** Define JSON Schema specifications for every tool and validate parameters as a middleware layer inside the Lambda handler or a shared Lambda Layer before the tool function runs. 

1.  **Add Cedar policy checks at the gateway:** Define policies in AgentCore Policy with conditions on context.input to enforce business rules and parameter constraints deterministically, complementing application-level schema validation. 

1.  **Use Automated Reasoning for logical constraints:** Configure [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning policies for tool inputs and outputs that require logical constraint validation beyond schema and Cedar rules. 

1.  **Right-size Lambda limits per tool:** Set AWS Lambda timeout and memory limits based on measured execution profiles, with conservative limits that help prevent resource exhaustion, and use reserved concurrency to cap parallel invocations. 

1.  **Sanitize errors:** Implement structured error handling in every tool that returns sanitized responses without internal system details, stack traces, or infrastructure information. 

1.  **Paginate and truncate large outputs:** Apply output size limits for tools that may return large datasets, truncate responses before returning them to the agent, and log every truncation event. 

1.  **Add AWS WAF in front of API-based tools:** Deploy AWS WAF with managed rule groups on API-based tool endpoints to filter common injection patterns at the network layer. 

1.  **Alarm on validation-failure rates:** Publish Amazon CloudWatch metrics for validation outcomes and configure alarms for elevated failure rates that suggest active injection attempts or misconfigured parameters. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC02-BP01 Implement tool authorization](agentsec02-bp01.html) 
+  [AGENTSEC02-BP03 Maintain approved tool registry with security assessments](agentsec02-bp03.html) 
+  [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](agentsec08-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails automated reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning.html) 
+  [Structured outputs on Amazon Bedrock: Schema-compliant AI responses](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/) 
+  [Secure AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) 
+  [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 