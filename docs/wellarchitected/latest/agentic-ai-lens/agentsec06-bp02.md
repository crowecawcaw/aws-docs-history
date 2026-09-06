

# AGENTSEC06-BP02 Implement workflow orchestration security controls
<a name="agentsec06-bp02"></a>

 The orchestration layer is where a single weak check cascades into a system-wide failure. Access controls on state machines, input validation on transitions, and circuit breakers on agent tasks keep multi-agent workflows on approved execution paths instead of unexpected ones. 

 **Desired outcome:** 
+  The workflow orchestration layer enforces strict access controls that help prevent unauthorized modification of workflow definitions or execution state. 
+  State machine validation helps keep workflows on expected execution patterns, and circuit breakers are designed to stop failures in one agent from cascading through the entire workflow. 
+  You log all workflow executions with enough detail to reconstruct the execution path for security investigations. 

 **Common anti-patterns:** 
+  Granting broad IAM permissions to start, stop, or modify Step Functions workflows without restricting access to specific state machines, letting any principal with workflow permissions modify or trigger any workflow in the account. 
+  Not implementing input validation in state machine definitions, letting crafted input payloads direct workflows into unexpected execution paths. 
+  Failing to implement circuit breakers, so a single failing agent cascades failures through the entire workflow with no automatic mechanism to stop retrying a broken step. 
+  Using overly permissive retry configurations, letting an agent repeatedly attempt the same operation before any circuit breaker triggers and potentially amplifying the original issue. 

 **Benefits of establishing this best practice:** 
+  State validation and input schema enforcement keep workflows within defined boundaries. 
+  Circuit breakers automatically stop cascading failures and route affected executions to quarantine paths for investigation. 
+  AWS Step Functions logging captures every state transition, input, output, and error event for full execution reconstructability. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Two orchestration patterns are in scope here. AWS Step Functions state machines handle deterministic workflows where the execution path is defined in JSON and the orchestrator enforces sequencing. [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) with the A2A protocol handles agent-delegated workflows where an orchestrator agent dynamically decides which sub-agents to invoke. Most of the controls below apply to both, and the differences are called out inline. 

 Start with IAM. Configure policies for AWS Step Functions that restrict workflow start, stop, and modification permissions to specific principals and state machines, use resource-based policies on state machine definitions to help prevent unauthorized modification, and implement IAM Conditions that restrict execution to approved input schemas. Manage state machine definitions as infrastructure as code through AWS CloudFormation or AWS CDK, which helps prevent informal modifications and provides version-controlled change history. 

 Input validation belongs inside the state machine definition, not outside it. With Step Functions' built-in JSONPath filtering and AWS Lambda validation functions, you can validate that workflow inputs conform to expected schemas before passing them to agent tasks, rejecting inputs that deviate from expected patterns. Step Functions' error handling catches and logs validation failures without exposing error details to callers. 

 Circuit breakers use Step Functions' error handling and retry logic. Set conservative retry limits with exponential backoff for agent task failures, and implement catch states that route failed executions to a quarantine path rather than retrying indefinitely. Amazon EventBridge emits circuit breaker events when failure thresholds are exceeded, triggering alerts and automated remediation. For multi-agent workflows using the A2A protocol on AgentCore Runtime, the structured request lifecycle (agent card discovery, task delegation, result collection) provides natural points to validate inputs, check authorization, and apply circuit breaker logic before proceeding. 

 Execution logging makes the orchestration auditable. Enable Step Functions execution logging to Amazon CloudWatch Logs at the ALL level to capture all state transitions, input/output data, and error events. Configure log retention policies aligned with compliance requirements and create Amazon CloudWatch Logs Insights queries for common investigation scenarios such as identifying workflows that took unexpected execution paths or triggered circuit breakers. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Scope Step Functions IAM to specific state machines:** Configure IAM policies with least-privilege access scoped to specific state machines and execution operations. 

1.  **Manage state machines as IaC:** Use AWS CloudFormation or AWS CDK for state machine definitions to help prevent unauthorized modifications and keep version history. 

1.  **Validate inputs inside state machines:** Implement input validation in state machine definitions using JSONPath filtering and AWS Lambda validation functions, rejecting inputs that deviate from expected schemas. 

1.  **Configure circuit breakers with catch states:** Set conservative retry limits and implement catch states that route failures to quarantine paths rather than retrying indefinitely. 

1.  **Log every execution at the ALL level:** Enable Step Functions execution logging to Amazon CloudWatch Logs at the ALL level with retention policies aligned to compliance requirements. 

1.  **Alarm on circuit breaker events:** Create Amazon CloudWatch alarms for circuit breaker triggers and Amazon EventBridge rules to route workflow security events to the monitoring pipeline. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](agentsec04-bp02.html) 
+  [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.html) 
+  [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.html) 
+  [AGENTREL07-BP01 Design workflows in stages with incremental recovery](agentrel07-bp01.html) 
+  [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](agentrel07-bp02.html) 

 **Related documents:** 
+  [AWS Step Functions security documentation](https://docs.aws.amazon.com/step-functions/latest/dg/security.html) 
+  [Step Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) 
+  [Using the circuit breaker pattern with Step Functions and DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/) 
+  [AWS Prescriptive Guidance: Circuit breaker pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) 
+  [Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) 

 **Related services:** 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 