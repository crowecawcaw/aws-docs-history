# Agent observability and non-repudiation

Without proper logging and traceability, agent actions can't be
investigated or attributed. Agents operate autonomously across
multiple services, tools, and data sources, generating complex
interaction chains that are difficult to reconstruct after the
fact. Observability through logging, distributed tracing, and
decision artifact storage supports security investigations,
compliance reporting, and continuous improvement of agent
behavior.

Two decisions drive this question. First, what record of agent
behavior you keep, where it lives, and how it is protected against
tampering by the agent itself. Second, how you follow a single
request across agents, tools, and asynchronous boundaries so that
any action can be reconstructed end-to-end.

| AGENTSEC05: How do you implement observability and prevent<br>repudiation? |
| -------------------------------------------------------------------------- |
|                                                                            |

## Capability intent

- Agent decisions, reasoning chains, tool invocations, and
  intermediate steps are captured to tamper-evident, queryable
  storage that sits outside the agent's own operational scope.
- Every logged action carries the initiating source that
  caused the agent to act, whether a human user session, an
  upstream event, a schedule, or another agent, so logged
  actions can typically be traced back to what triggered them.
- A single correlation identifier, independent of the tracing
  system's trace ID, survives asynchronous boundaries and
  connects every span, log, and decision artifact generated
  during a request.
- Sensitive fields are masked or redacted before logs reach
  long-term storage, so completeness of behavioral records
  doesn't conflict with data protection obligations.
- Security investigators can reconstruct the complete chain of
  agent interactions for past requests, without relying on the
  agent's own account of its reasoning.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent observability and non-repudiation as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Only final agent outputs are captured, typically to<br>application logs that share credentials and lifetime<br>with the agent itself. Intermediate reasoning, tool<br>invocations, and trigger attribution are lost. Logs are<br>mutable, sensitive data is unmasked, and there is no<br>practical way to reconstruct how the agent reached a<br>given conclusion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2     | Emerging  | [Amazon<br>Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md") is turned on,<br>delivering prompts and responses to a single destination<br>chosen based on access and retention needs:<br>[Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") for operational visibility or<br>[Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") for retention.<br>[AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") is turned on across agent accounts.<br>Trace IDs are generated within each service, but<br>correlation across asynchronous boundaries is partial,<br>and sensitive data protection is inconsistent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 3     | Defined   | Decision artifacts and CloudTrail logs are delivered to<br>a dedicated<br>[Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket in a separate Log Archive account,<br>aligned with the<br>[AWS Security Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md"), with<br>[versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md")<br>turned on and bucket policies that deny delete and<br>overwrite.<br>[CloudTrail<br>log file validation](../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md "../../../awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.md") is on.<br>[Amazon CloudWatch Logs data protection](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md") masks common<br>sensitive patterns.<br>[AWS Distro for OpenTelemetry](https://aws-otel.github.io/ "https://aws-otel.github.io/") instruments agent code,<br>correlation IDs are propagated through<br>[Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.md#sqs-message-attributes "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.md#sqs-message-attributes") and<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md"), and<br>[AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") produces end-to-end traces. |
| 4     | Proactive | [Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability-telemetry.md "../../../bedrock-agentcore/latest/devguide/observability-telemetry.md") captures session,<br>trace, and span hierarchies that include agent<br>reasoning, tool calls, and memory operations.<br>[AgentCore<br>Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") continuously scores correctness,<br>helpfulness, tool selection accuracy, and safety, with<br>alarms on score drift. Tamper-evident retention is<br>achieved through bucket policies that deny delete and<br>overwrite, MFA delete, and (where compliance<br>requirements call for it)<br>[S3<br>Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") in governance mode after careful<br>review of the operational implications.<br>[Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") with<br>[AWS Glue Data Catalog](../../../glue/latest/dg/components-overview.md#data-catalog-intro "../../../glue/latest/dg/components-overview.md#data-catalog-intro") makes the artifact store<br>queryable, and standard investigation queries are<br>documented.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 5     | Optimized | Tiered retention moves artifacts from<br>[CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md "../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md") through<br>[Amazon S3 Standard](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") to<br>[Amazon Glacier](../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-glacier "../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-glacier") with automated<br>[S3<br>Lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") transitions tied to data classification<br>tags.<br>[AWS KMS customer-managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") with automatic rotation<br>protect all log destinations. Investigation-time queries<br>return answers within a target investigation window<br>defined for each customer based on data volume and<br>incident-response objectives, anomaly detection runs on<br>the artifact index, and the observability data feeds<br>back into evaluation and guardrail tuning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Common issues to watch for

- Only final outputs are captured, so incident responders can
  see what the agent did but not why it did it, which is the
  first question asked in nearly every investigation.
- Decision artifacts share the credentials and lifetime of the
  agent that generated them, which means an affected agent can
  modify or delete its own record of what happened.
- Trace context is re-generated at every asynchronous boundary
  without a complementary correlation identifier, breaking the
  chain exactly where investigations need it most.
- Sensitive data protection applied at inference time but not
  at logging time, so prompts and responses containing PII,
  secrets, or regulated fields end up unmasked in long-term
  storage. CloudWatch Logs has built-in data protection
  policies that mask known sensitive types in place. For S3
  destinations, masking has to be applied at write time before
  the object lands in the bucket, and any retroactive
  remediation requires re-processing existing objects. Plan
  the masking strategy per destination rather than assuming
  one control covers both.
- Artifacts are retained indefinitely without a queryable
  index, producing petabytes of S3 objects that are
  technically complete but practically unsearchable during a
  time-sensitive incident.

###### Best practices

- [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.md "agentsec05-bp01.md")
- [AGENTSEC05-BP02 Implement distributed tracing for agent interactions](agentsec05-bp02.md "agentsec05-bp02.md")
