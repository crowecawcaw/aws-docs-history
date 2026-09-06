

# AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage
<a name="agentsec05-bp01"></a>

 Agent decisions are only auditable if the reasoning behind them is captured, preserved intact, and reachable at the speed investigations actually move. Tamper-evident artifact storage, attribution to the original trigger, and a queryable index turn raw log volume into forensic capability. 

 **Desired outcome:** 
+  You capture every agent decision, action, and reasoning step in tamper-evident, queryable storage, producing a complete and verifiable record of agent behavior. 
+  Each logged action includes attribution to the initiating source (a human user session, an upstream event, a schedule, or another agent), so logged actions can typically be traced back to what triggered them. 
+  You can reconstruct the full decision-making process for any agent action from stored artifacts, independent of the agent's own account of its reasoning. 
+  Cryptographic validation verifies log integrity, the agent's operational IAM role can't modify or delete its own decision history, and sensitive data (PII, secrets, regulated fields) is masked or redacted before logs are written to long-term storage. 

 **Common anti-patterns:** 
+  Logging only final agent outputs without intermediate reasoning, tool invocations, or decision points, making incident reconstruction impossible. 
+  Storing logs and decision artifacts in mutable storage without write-once protection, so logs can be deleted or modified after the fact. 
+  Storing decision artifacts in the same account and with the same permissions as the agent's operational resources, letting an affected agent modify or delete its own history. 
+  Retaining artifacts without a queryable index, so scanning raw S3 objects becomes impractical during time-sensitive investigations. 

 **Benefits of establishing this best practice:** 
+  Detailed logging of reasoning chains, tool invocations, and intermediate steps, stored independently from the agent's operational resources, supports reconstruction of agent behavior during investigations. 
+  Amazon S3 Object Lock and AWS CloudTrail log file validation provide cryptographic proof of log integrity for compliance and forensic purposes. 
+  Queryable artifact stores support retrospective behavioral analysis that surfaces patterns missed by real-time alerts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Logging for agents has three hard requirements that ordinary application logging doesn't: 
+  Completeness (the reasoning chain, not just the outputs) 
+  Immutability (the agent whose behavior you are investigating can't be the entity that controls its own logs) 
+  Queryability at investigation speed (S3 scans are not fast enough when minutes matter) 

 Each of those requirements shapes a different piece of the architecture. 

 Start with the model invocation layer. Enable Amazon Bedrock model invocation logging to capture all inference requests and responses (input prompts, model outputs, token counts, latency metrics) with delivery to Amazon CloudWatch Logs for operational monitoring and Amazon S3 for long-term retention. Because agent prompts and model outputs often contain PII, secrets, or regulated data, apply data protection before content lands in long-term storage. [Amazon CloudWatch Logs data protection policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) automatically detect and mask sensitive types (credentials, personal identifiers, financial data) in log events. [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters anonymize or redact PII in input prompts and model responses at inference time, but that is distinct from what the logs capture. Verify masking behavior across each destination in use (Amazon Bedrock Model Invocation Logs, AgentCore Observability, CloudWatch Logs, the S3 artifact store) and add write-time masking in agent code wherever the source doesn't mask on its own. 

 Decision artifacts require a separate trust boundary. Create a dedicated S3 bucket in a separate AWS account with versioning enabled, and use bucket policies that allow write from the agent account but deny delete and overwrite operations. That gives you an append-only artifact store the agent's operational IAM role can't tamper with. A consistent key schema (agent ID, session ID, timestamp, decision type) makes retrieval predictable during investigations. Capture the initiator on every decision. An agent can be invoked by: 
+  A human user session 
+  An Amazon EventBridge event 
+  An Amazon SQS message 
+  An Amazon CloudWatch alarm 
+  A scheduled rule 
+  Another agent 

 Log the identifiers that describe the trigger (IAM session or Amazon Cognito user for human requests, event source and event ID for events, alarm ARN for alarms, calling agent and session IDs for inter-agent calls) as structured fields so investigation queries can filter by trigger source. 

 For tamper-evidence on the bucket itself, default to bucket policies that deny delete and overwrite, MFA delete on the bucket, and versioning. Where compliance requirements call for stronger guarantees, consider enabling Amazon S3 Object Lock in governance mode, which allows users with specific IAM permissions to override retention settings when needed. Compliance mode helps prevent any user (including the root account) from deleting or shortening retention periods for the duration of the lock. Once configured, this mode is irreversible, and a misconfiguration of the retention period or scope can leave a customer unable to delete data they need to delete (for example, to meet right-to-be-forgotten requests). Use compliance mode only when there is a specific regulatory requirement for it, and validate the retention configuration against representative test data before applying it broadly. 

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) captures agent reasoning chains, tool invocations, and decision artifacts automatically for agents running on AgentCore Runtime. The session, trace, and span hierarchy records reasoning steps, tool calls with inputs and outputs, and memory operations. AgentCore outputs span data for memory resources by default and publishes session-level metrics viewable on the Amazon CloudWatch generative AI observability page. For artifacts that need retention beyond the default observability window or specific compliance controls, write the full decision context to the dedicated S3 artifact store at each significant decision point. AWS Distro for OpenTelemetry (ADOT) extends coverage with custom metrics, logs, and spans in agent code. 

 [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) complements logging by continually scoring agent behavior on correctness, helpfulness, tool selection accuracy, and safety. Results publish to Amazon CloudWatch alongside observability data for a unified view, and Amazon CloudWatch alarms on evaluation scores detect behavioral drift outside acceptable thresholds. 

 Tamper-evidence at the audit-trail level uses AWS CloudTrail with log file validation across all accounts and regions where agents operate. Log file validation produces SHA-256 hashes and RSA signatures in a digest file that verifies log files have not been modified, deleted, or forged after delivery. A dedicated S3 bucket with cross-account access controls helps prevent the agent's own IAM role from modifying or deleting logs. 

 Amazon Athena with AWS Glue Data Catalog makes the decision artifact store queryable: an AWS Glue crawler scans the S3 artifact bucket and creates tables in the Data Catalog based on the artifact schema, and Athena runs SQL queries directly against S3 without loading data into a separate database. Investigation queries such as "find all decisions made by agent X that involved tool Y between dates A and B" become cheap to run. Document standard investigation queries for common security scenarios so investigators can work immediately during an incident. This pattern (logs to Amazon S3, cataloged by AWS Glue, queried with Amazon Athena) is an established forensic log analytics approach recommended in the AWS Well-Architected Security Pillar. 

 A lifecycle policy keeps storage costs proportional to access patterns. Hot logs live in Amazon CloudWatch Logs for operational monitoring (30 to 90 days), transition to Amazon S3 Standard for medium-term retention (1 to 2 years), and archive to Amazon Glacier for long-term compliance retention (7\+ years). Tag objects with data classification and retention policy metadata so lifecycle transitions are automated. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable Amazon Bedrock model invocation logging:** Turn on Amazon Bedrock model invocation logging and deliver to both Amazon CloudWatch Logs and Amazon S3. 

1.  **Mask sensitive data before it lands in long-term storage:** Configure Amazon CloudWatch Logs data protection policies, verify masking behavior across every logging destination in use, and add write-time masking in agent code where the destination doesn't mask on its own. 

1.  **Create a dedicated, append-only artifact bucket in a Log Archive account:** Create an Amazon S3 bucket in a separate Log Archive account, aligned with the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html), with versioning enabled and cross-account access controls that allow agent write access but deny delete and overwrite operations. 

1.  **Choose a retention-protection model:** Default to bucket-policy-based protection (deny delete, deny overwrite, MFA delete, versioning). Evaluate Amazon S3 Object Lock in governance mode where compliance requires stronger guarantees, and reserve compliance mode for cases where there is a specific regulatory requirement for it after validating the retention scope and duration against representative test data. 

1.  **Capture full traces through AgentCore Observability:** Use [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) to capture full agent execution traces, and for artifacts needing longer retention or compliance controls, write the full decision context to the dedicated S3 artifact store at each significant decision point. 

1.  **Record initiator attributes on every artifact:** Capture human session, event source and event ID, alarm ARN, schedule rule ARN, calling agent ID, and similar identifiers as structured fields on decision artifacts and log entries. 

1.  **Apply a consistent artifact key schema:** Use `agentId`, `sessionId`, `timestamp`, and `decisionType` as the key schema for efficient retrieval during investigations. 

1.  **Deploy AgentCore Evaluations with drift alarms:** Deploy [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with built-in and custom evaluators, publish results to Amazon CloudWatch, and configure alarms on evaluation scores to detect behavioral drift. 

1.  **Enable CloudTrail log file validation:** Turn on AWS CloudTrail with log file validation across all accounts and regions, storing logs in a dedicated S3 bucket with cross-account access controls. 

1.  **Make artifacts queryable with Athena and AWS Glue:** Set up an AWS Glue crawler to scan the S3 artifact bucket and create tables in the Data Catalog, use Amazon Athena to query artifacts directly in S3, and document standard investigation queries for common security scenarios. 

1.  **Implement tiered retention with automation:** Define retention tiers (CloudWatch Logs for operational monitoring, S3 Standard for medium-term, Amazon Glacier for long-term compliance) with automated lifecycle transitions and data classification tagging. 

1.  **Encrypt all log and artifact storage:** Use customer-managed AWS KMS keys with key rotation enabled on every logging destination. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC03-BP02 Separate agent and human user permission](agentsec03-bp02.html) 
+  [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](agentsec04-bp02.html) 
+  [AGENTSEC05-BP02 Implement distributed tracing for agent interactions](agentsec05-bp02.html) 
+  [AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery](agentrel07-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) 
+  [AgentCore Observability: Sessions, traces, and spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) 
+  [Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Amazon Bedrock AgentCore adds quality evaluations and policy controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) 
+  [AWS CloudTrail log file validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) 
+  [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) 
+  [Amazon CloudWatch Logs data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) 
+  [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) 
+  [Querying AWS service logs with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-aws-service-logs.html) 
+  [Create a customizable cross-company log lake for compliance (AWS Big Data Blog)](https://aws.amazon.com/blogs/big-data/create-a-customizable-cross-company-log-lake-part-ii-build-and-add-amazon-bedrock/) 
+  [AWS Well-Architected Security Pillar SEC04-BP01: Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_detect_investigate_events_app_service_logging.html) 
+  [Considerations for addressing the core dimensions of responsible AI for Amazon Bedrock applications](https://aws.amazon.com/blogs/machine-learning/considerations-for-addressing-the-core-dimensions-of-responsible-ai-for-amazon-bedrock-applications/) 
+  [Security reference architecture for generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 