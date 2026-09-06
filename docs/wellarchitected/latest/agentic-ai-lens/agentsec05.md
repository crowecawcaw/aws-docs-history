

# Agent observability and non-repudiation
<a name="agentsec05"></a>

 Without proper logging and traceability, agent actions can't be investigated or attributed. Agents operate autonomously across multiple services, tools, and data sources, generating complex interaction chains that are difficult to reconstruct after the fact. Observability through logging, distributed tracing, and decision artifact storage supports security investigations, compliance reporting, and continuous improvement of agent behavior. 

 Two decisions drive this question. First, what record of agent behavior you keep, where it lives, and how it is protected against tampering by the agent itself. Second, how you follow a single request across agents, tools, and asynchronous boundaries so that any action can be reconstructed end-to-end. 


|  AGENTSEC05: How do you implement observability and prevent repudiation?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-4"></a>
+  Agent decisions, reasoning chains, tool invocations, and intermediate steps are captured to tamper-evident, queryable storage that sits outside the agent's own operational scope. 
+  Every logged action carries the initiating source that caused the agent to act, whether a human user session, an upstream event, a schedule, or another agent, so logged actions can typically be traced back to what triggered them. 
+  A single correlation identifier, independent of the tracing system's trace ID, survives asynchronous boundaries and connects every span, log, and decision artifact generated during a request. 
+  Sensitive fields are masked or redacted before logs reach long-term storage, so completeness of behavioral records doesn't conflict with data protection obligations. 
+  Security investigators can reconstruct the complete chain of agent interactions for past requests, without relying on the agent's own account of its reasoning. 

## Maturity levels
<a name="maturity-levels-4"></a>

 These levels summarize what each stage of maturity looks like for agent observability and non-repudiation as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Only final agent outputs are captured, typically to application logs that share credentials and lifetime with the agent itself. Intermediate reasoning, tool invocations, and trigger attribution are lost. Logs are mutable, sensitive data is unmasked, and there is no practical way to reconstruct how the agent reached a given conclusion.  | 
|  2  |  Emerging  |  [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) is turned on, delivering prompts and responses to a single destination chosen based on access and retention needs: [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) for operational visibility or [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for retention. [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) is turned on across agent accounts. Trace IDs are generated within each service, but correlation across asynchronous boundaries is partial, and sensitive data protection is inconsistent.  | 
|  3  |  Defined  |  Decision artifacts and CloudTrail logs are delivered to a dedicated [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket in a separate Log Archive account, aligned with the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html), with [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) turned on and bucket policies that deny delete and overwrite. [CloudTrail log file validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) is on. [Amazon CloudWatch Logs data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) masks common sensitive patterns. [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) instruments agent code, correlation IDs are propagated through [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html), and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) produces end-to-end traces.  | 
|  4  |  Proactive  |  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) captures session, trace, and span hierarchies that include agent reasoning, tool calls, and memory operations. [AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) continuously scores correctness, helpfulness, tool selection accuracy, and safety, with alarms on score drift. Tamper-evident retention is achieved through bucket policies that deny delete and overwrite, MFA delete, and (where compliance requirements call for it) [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in governance mode after careful review of the operational implications. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) with [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) makes the artifact store queryable, and standard investigation queries are documented.  | 
|  5  |  Optimized  |  Tiered retention moves artifacts from [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SettingLogRetention.html) through [Amazon S3 Standard](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) to [Amazon Glacier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-glacier) with automated [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) transitions tied to data classification tags. [AWS KMS customer-managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) with automatic rotation protect all log destinations. Investigation-time queries return answers within a target investigation window defined for each customer based on data volume and incident-response objectives, anomaly detection runs on the artifact index, and the observability data feeds back into evaluation and guardrail tuning.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-4"></a>
+  Only final outputs are captured, so incident responders can see what the agent did but not why it did it, which is the first question asked in nearly every investigation. 
+  Decision artifacts share the credentials and lifetime of the agent that generated them, which means an affected agent can modify or delete its own record of what happened. 
+  Trace context is re-generated at every asynchronous boundary without a complementary correlation identifier, breaking the chain exactly where investigations need it most. 
+  Sensitive data protection applied at inference time but not at logging time, so prompts and responses containing PII, secrets, or regulated fields end up unmasked in long-term storage. CloudWatch Logs has built-in data protection policies that mask known sensitive types in place. For S3 destinations, masking has to be applied at write time before the object lands in the bucket, and any retroactive remediation requires re-processing existing objects. Plan the masking strategy per destination rather than assuming one control covers both. 
+  Artifacts are retained indefinitely without a queryable index, producing petabytes of S3 objects that are technically complete but practically unsearchable during a time-sensitive incident. 

**Topics**
+ [Capability intent](#capability-intent-4)
+ [Maturity levels](#maturity-levels-4)
+ [Common issues to watch for](#common-issues-to-watch-for-4)
+ [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.md)
+ [AGENTSEC05-BP02 Implement distributed tracing for agent interactions](agentsec05-bp02.md)