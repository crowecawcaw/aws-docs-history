

# ADVOPS02-BP03 Implement centralized logging to aggregate logs from all components of your advertising stack

 Aggregate logs from every component of your advertising stack into a centralized store. Aggregate logs from components such as third-party integrations, custom applications, managed connectivity services, and agentic AI workflows. 

 **Desired outcome:** 
+  Logs from all advertising stack components flow into a centralized, searchable store with a consistent schema. 
+  Structured logs with correlation IDs enable cross-component trace analysis, following a bid request from SSP ingestion through auction evaluation to creative delivery. 
+  Log retention periods are aligned with compliance requirements and operational needs per data type. 

 **Common anti-patterns:** 
+  Operating separate log repositories for different teams (infrastructure logs in CloudWatch, application logs in S3, analytics logs in Amazon Redshift) with no unified search capability. 
+  Collecting unstructured text logs that can't be parsed and queried for specific events. 
+  Setting uniform retention periods for all log types regardless of compliance requirements. Bid request logs with user data may require shorter retention than infrastructure audit logs. 

 **Benefits of establishing this best practice:** 
+  Consolidated view of logs across the advertising environment, which improves issue detection and resolution. 
+  Cross-component correlation enables root cause analysis that spans infrastructure and application boundaries. 
+  Unified log governance simplifies compliance auditing. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising platforms generate logs ad serving infrastructure (Amazon ECS and Amazon EKS containers), managed connectivity (RTB Fabric application logs), ad decision services, VAST response caches, SGAI manifest generation services, FAST channel playout infrastructure, and agentic AI agent traces. Without centralization, incident investigation requires logging into multiple systems, switching between query tools, and correlating timestamps manually, which extends MTTD and MTTR. 

 Amazon OpenSearch Service scales log aggregation and supports full-text and structured queries across components. Use OpenSearch to trace a bid request from SSP ingestion through auction evaluation to creative delivery in a single query. Use Amazon CloudWatch Logs Insights when you only need single-service analysis. 

 At auction volume, log storage becomes a material cost line, so you must decide what to sample. Error events are rare, and dropping one may discard the only record of an incident. Routine events have low individual value but in aggregate establish your system's baseline before an incident. Set the sampling rate separately for each category to keep incident evidence and control storage cost. 

 Cross-system correlation depends on a join key that exists at every boundary, and centralization often fails at this junction. Aggregating logs into one store makes them searchable but not joinable. If a connectivity-layer event and an application event share no identifier, they might be in the same index but still cannot be connected. An operator then correlates by timestamp. Every system in the path must include an identifier that can be matched upstream. 

 Some observability data is lost unless you capture it deliberately. For example, in agent reasoning, the response includes the model's decision chain, but no other system stores this data. Unlike infrastructure logs, there is no retroactive retrieval and no default retention. For most systems, you decide how long to retain logs that already exist. For agent traces, you decide whether to capture them at all. Without captured traces, you cannot reconstruct or explain an agent decision to an advertiser or regulator. 

 Retention is also a per-category judgment. Logs that contain viewer signals are subject to deletion obligations that do not apply to infrastructure logs. Separate the categories whose obligations differ. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Amazon OpenSearch Service as the centralized log aggregation backend:** Configure an OpenSearch domain sized for your daily log volume. Deploy Amazon Data Firehose delivery streams that receive logs from CloudWatch Logs Subscription Filters and write to OpenSearch with structured JSON documents. Define index templates that enforce a consistent log schema with required fields: timestamp, service, correlation\_id, severity, and service-specific data fields. 

1.  **Configure structured logging with correlation IDs across all services:** Update all advertising services to emit structured JSON logs with a correlation\_id field populated from the request context (bid request ID, session ID, or generated UUID). This field is the key that enables cross-service trace reconstruction. Enforce the schema using a log validation layer that rejects logs missing required fields, to avoid schema drift that breaks cross-component queries. 

1.  **Configure RTB Fabric log delivery with appropriate sampling rates:** Enable RTB Fabric application log delivery per link to CloudWatch Logs. Set errorLog sampling to 100% (all error conditions) and filterLog sampling based on volume and cost tolerance. Configure CloudWatch Logs subscription filters that forward RTB Fabric logs to the centralized OpenSearch domain. Create an index template that preserves the link ID field for correlation with bidder application logs. 

1.  **Capture and persist Amazon Bedrock agent traces to Amazon S3:** Implement agent trace capture in your InvokeAgent call handlers. Extract TracePart objects from the streaming response and write them to an S3 bucket with a structured prefix (year=YYYY/month=MM/day=DD/agent\_id=XXX/). Include the inputTokens and outputTokens counts from ModelInvocationOutput.metadata.usage so the archive supports per-agent cost attribution. Use AWS Glue to catalog the S3 trace archive and Amazon Athena for analysis. Configure S3 lifecycle policies to transition traces to S3 Glacier Flexible Retrieval after the operational retention period and delete after the compliance retention period. 

1.  **Define retention policies by log category:** Configure CloudWatch Logs retention periods and S3 lifecycle policies per log category: bid request and response logs (30 days, then delete: may contain user data), infrastructure audit logs (1 year: compliance requirement), RTB Fabric error logs (90 days: operational debugging), RTB Fabric filter logs (30 days: high volume, short operational utility), Bedrock agent traces (90 days operational, configurable compliance extension). Document these policies in your data governance inventory. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS01-BP04 Establish data governance and compliance operations](advops01-bp04.md) 
+  [ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics](advops02-bp04.md) 

 **Related documents:** 
+  [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) 
+  [Configuring RTB Fabric logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-logs.html) 

 **Related services:** 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon Data Firehose](https://aws.amazon.com/firehose/) 
+  [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/) 