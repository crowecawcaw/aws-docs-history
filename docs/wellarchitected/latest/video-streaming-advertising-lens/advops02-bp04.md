

# ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics

 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics. Operations teams can then see into every tier of the ad-serving stack. Structured instrumentation helps teams detect and resolve issues quickly, and scales with complex systems such as managed connectivity and agent-based decision-making. Extend instrumentation to capture the correlation between network events and application outcomes. 

 **Desired outcome:** 
+  All advertising services emit structured JSON logs with correlation IDs that link events across service boundaries, covering infrastructure, application, partner connectivity, and agent tiers. 
+  Managed connectivity traffic is correlated with bid outcome data using the link ID as the join key, so an operator can follow a single bid request across the full request path. 
+  Agentic AI workflows emit trace data capturing reasoning chains, tool invocations, and downstream API calls linked by trace IDs, persisted beyond the ephemeral response. 
+  Instrumentation emits business-relevant structured fields (partner link ID, agent ID, campaign ID, decision rationale) alongside standard telemetry, and log sampling captures all error conditions while managing volume on high-frequency categories. 

 **Common anti-patterns:** 
+  Emitting unstructured (plain-text) logs that require regex parsing, break cross-service correlation, and can't be joined on business fields like partner identity. 
+  Logging bid outcomes without the link identifier or partner ID, making per-partner root cause analysis impossible. 
+  Not correlating connectivity-layer events with bid outcomes. 
+  Capturing agent reasoning chains in ephemeral API responses without persisting them. 
+  Setting log sampling rates uniformly across error and success paths, diluting signal on the error conditions that matter most. 

 **Benefits of establishing this best practice:** 
+  Structured logs with correlation IDs enable automated root cause analysis across service boundaries. 
+  Connectivity-layer and application-layer correlation enables precise diagnosis of whether bid latency originates in the network path, at the partner endpoint, or within bidder application logic. 
+  Shared correlation identifiers (link ID, trace ID, agent ID) let operators join across data sources without manual reconstruction. 
+  Persisted agent traces support compliance, debugging, and ongoing optimization of agent workflows. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 You can query a structured log line without parsing it. Text written for humans requires pattern-matching at read time. This couples the query to the message format and breaks whenever someone rewords the message. A typed event with a stable set of fields moves that cost to write time, and the query becomes a property of the schema. Enforce the schema in shared code, not by convention. 

 Cross-tier questions require a shared identifier that survives every boundary. Per-tier instrumentation alone does not provide one. Create the identifier at the edge and propagate it, including across boundaries the team does not own. Propagation fails more often than emission. Test this by following one real request through its full lifecycle, not by checking that each service logs correctly. 

 Connectivity behavior, such as a rejected connection or forwarding delay, does not appear in application logs. A latency spike from there looks like an unexplained application slowdown. Without a connectivity-side signal keyed to a value the application also records, you cannot distinguish the two. Agent reasoning exists only inside the response and is destroyed when the response closes. Capturing it is a write-time decision, not a retention decision. The loss is unrecoverable. If you cannot reconstruct an agent action, you cannot explain it to an advertiser, audit it, or debug it. 

 The dimensions that make a metric diagnostic (partner, campaign, adapter, and agent) have unbounded value sets. Their instrumentation cost grows the fastest and eventually forces throttling. Deciding which dimensions to keep is an ongoing judgment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Standardize a structured JSON log schema across all advertising services:** Define required fields: timestamp (ISO 8601), service\_name, log\_level, correlation\_id, request\_id, partner\_id/link ID, agent\_id (if applicable), campaign\_id, outcome code, and a payload object. Enforce the schema in a shared logging library so every service in the bid path emits joinable logs. 

1.  **Instrument application metrics:** Emit custom metrics for per-partner bid volume, no-bid reason codes (distinguishing application- from network-generated), timeout counts, and response-latency percentiles by using Amazon CloudWatch PutMetricData, keeping dimensions bounded to avoid high-cardinality explosion. 

1.  **Configure RTB Fabric application log delivery with sampling:** Enable per-link delivery to CloudWatch Logs with errorLog at 100 percent and filterLog calibrated to volume and cost. Include the link ID in the structured log record so filter-log events join with bidder application logs during analysis. 

1.  **Instrument agentic AI workflows with trace IDs spanning the full decision chain:** Assign a trace\_id per agent workflow invocation (campaign planning, brand-safety assessment, creative selection) and propagate it through all tool calls, sub-agent invocations, and downstream API calls in Lambda action-group handlers, enabling cross-service trace reconstruction. 

1.  **Capture and persist Amazon Bedrock agent traces from the streaming response:** In the InvokeAgent handler, extract TracePart objects from the stream, buffer them, and write the complete trace to Amazon S3 when the stream closes, using trace\_id, agent\_id, session\_id, and timestamp as partition keys for efficient retrieval. Don't rely on the ephemeral response buffer. 

1.  **Deploy AWS X-Ray distributed tracing across services:** Instrument services with the X-Ray SDK, propagate trace context across every boundary, and build service maps spanning API Gateway, Lambda, Bedrock, ElastiCache, DynamoDB, and external partner APIs. Add X-Ray annotations for bid-specific metadata (partner ID, auction outcome, creative format) to enable advertising-dimension filtering. 

1.  **Centralize logs in CloudWatch Logs:** Route logs from application services, infrastructure, managed connectivity, and agent runtimes into a common log-group structure, and use subscription filters to pipe high-value signals (errors and anomalies) to downstream analytics. 

1.  **Validate log joinability across all tiers:** Pick a recent bid request and trace it from ingress through connectivity, application, database, and agent reasoning to response. If you can't follow it without gaps, the instrumentation has missing tiers. Fix before treating instrumentation as complete. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack](advops02-bp01.md) 
+  [ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns](advops02-bp02.md) 
+  [ADVOPS02-BP05 Monitor partner connectivity health and traffic management effectiveness across your advertising network](advops02-bp05.md) 
+  [ADVOPS02-BP06 Implement distributed tracing for automated and agent-driven advertising operations](advops02-bp06.md) 

 **Related documents:** 
+  [Configuring RTB Fabric logs with Amazon CloudWatch Logs](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-logs.html) 
+  [Amazon Bedrock agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) 
+  [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/features/) 
+  [AWS X-Ray](https://aws.amazon.com/xray/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 