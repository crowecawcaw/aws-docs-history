

# AGENTOPS05-BP03 Implement structured logging and comprehensive audit trails
<a name="agentops05-bp03"></a>

 Free-text logs look useful until someone tries to query them at scale. Structured logs, immutable audit trails, and defined retention policies make your logs an active operational tool that provides evidence for compliance. 

 **Desired outcome:** 
+  All agent decisions, actions, and interactions are captured in structured, queryable logs. 
+  Audit trails are immutable and tamper-evident, providing a trustworthy record for regulatory and governance purposes. 
+  Log retention policies balance operational and compliance needs with storage cost. 
+  Authorized teams query log data efficiently through defined interfaces. 

 **Common anti-patterns:** 
+  Using unstructured free-text logging that can't be efficiently queried or parsed at scale. 
+  Logging only errors and exceptions without capturing successful operations, producing an incomplete picture that reduces the ability to reconstruct the full sequence. 
+  Storing logs in mutable storage without integrity controls, creating audit trails that could be altered and therefore can't be relied upon for compliance. 
+  Logging sensitive information, personally identifiable information (PII) or credentials, in agent reasoning traces, creating compliance and security risk. 
+  Operating without retention policies, producing unbounded log volumes that become expensive to store and difficult to search. 

 **Benefits of establishing this best practice:** 
+  Immutable, structured audit trails provide the evidentiary foundation for regulatory compliance and demonstrate that agents operated within authorized boundaries. 
+  Structured logging with efficient query interfaces turns log data from a passive record into an active operational tool, enabling rapid incident investigation and pattern extraction. 
+  PII redaction at write time helps prevent sensitive information from reaching log storage, reducing data protection risk. 
+  Tiered retention keeps compliance-relevant logs available for years while retiring short-term debug logs that would otherwise accumulate cost. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Structured logging is a format discipline that verifies that your other logging practices work correctly. Your JSON should have a standardized schema to make it queryable, including: 
+  Timestamp 
+  Trace ID 
+  Agent ID 
+  Session ID 
+  Operation type 
+  Decision rationale 
+  Outcome 

 Free-text logs require regex searches to answer simple questions, while structured logs answer them through [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/) Insights queries against named fields. Enforce the schema, even if it is simple. 

 Your retention policy should depend on the purpose of the logs. 
+  Operational logs (30–90 days) support incident investigation and recent trend analysis. 
+  Compliance logs (1–7 years depending on regulatory requirements) support audits and legal discovery. 
+  Debug logs (7–14 days) support development and are expensive to keep beyond that. 

 Applying different retention policies to different log streams, rather than one policy to everything, cuts storage cost substantially without losing important log information. 

 PII redaction should happen before logs reach storage. [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters detect and redact PII at write time, which is the only reliable place to do it. Once PII is in the log, every downstream access becomes a data protection concern. 

 For compliance-critical logs, [Amazon S3](https://aws.amazon.com/s3/) with Object Lock in Compliance mode provides immutable storage that supports regulatory requirements for tamper-evident audit trails. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) captures API-level agent actions as an infrastructure complement, and [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures agent reasoning chains, tool invocations, and decision artifacts automatically for agents on AgentCore Runtime. 

 Establish saved query templates to reduce investigation latency. For security-focused immutable audit logs with cryptographic integrity, see [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a JSON log schema:** Cover trace ID, operation type, decision rationale, and outcome as standard fields for every agent operation. 

1.  **Configure tiered retention:** Separate operational (30–90 days), compliance (1–7 years), and debug (7–14 days) log streams. 

1.  **Redact PII before write:** Integrate [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters into the logging pipeline. 

1.  **Use immutable storage for compliance logs:** Write audit trails to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) with Object Lock in Compliance mode. 

1.  **Create saved query templates:** Cover common operational analysis patterns so incident response doesn't start from a blank screen. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations](agentops05-bp01.html) 
+  [AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies](agentops05-bp02.html) 
+  [AGENTOPS04-BP02 Establish standardized tool integration protocols (MCP, A2A)](agentops04-bp02.html) 
+  [AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery](agentrel07-bp03.html) 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Observing agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/) 
+  [Getting started with Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) 
+  [Advancing AI agent governance with Boomi and AWS](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 