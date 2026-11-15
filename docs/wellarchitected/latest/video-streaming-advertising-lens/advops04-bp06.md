

# ADVOPS04-BP06 Implement operational procedures based on data classification and latency requirements
<a name="advops04-bp06"></a>

 Establish tier-based procedures for low-latency data (bid requests), medium-latency data (campaign optimization), and high-latency data (historical analytics). Classify managed connectivity service metrics as low-latency operational data, and agentic AI agent traces as medium-latency operational data. 

 **Desired outcome:** 
+  Operational procedures for real-time bidding data include multi-AZ deployments, short monitoring evaluation periods, rapid-response procedures, and circuit breakers. 
+  Connectivity-layer metrics and logs from managed services are classified and monitored as low-latency operational data requiring real-time monitoring intervals. 
+  Agent traces and reasoning chains from agentic AI workflows are processed in micro-batches for medium-latency operational analysis, with retention policies that account for compliance requirements separate from standard operational log retention. 

 **Common anti-patterns:** 
+  Applying the same monitoring evaluation period to all advertising data types. 
+  Not classifying connectivity-layer metrics as low-latency operational data, which delays detection of partner connectivity issues that affect bid win rates. 
+  Managing agentic AI agent traces with the same retention policy as standard application logs, without accounting for the potentially sensitive campaign data and audience information they contain. 

 **Benefits of establishing this best practice:** 
+  Appropriately tiered operational procedures match the urgency of each data type, reducing both false positives (over-alerting on slow-changing data) and blind spots (under-alerting on fast-changing data). 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The three-tier latency classification from this lens maps directly to operational procedure requirements: 
+  **Low-latency data (real-time, milliseconds):** Bid data, user device data, ad impression data, real-time campaign performance. Operational requirements: multi-AZ deployments with automatic failover, short monitoring evaluation periods (1 minute or less), rapid-response procedures for critical alerts, circuit breakers in API calls, auto-scaling with aggressive scaling policies, and local caching. Connectivity-layer metrics from RTB Fabric are classified here. Monitor per-link request counts, latency percentiles, and status code distributions at 1-minute intervals, with immediate alerting when target-ip-count drops to zero. 
+  **Medium-latency data (near real-time to batch, minutes to hours):** User behavior data, audience segmentation, campaign optimization, attribution. Operational requirements: queue management with automated retry, monitoring with balanced evaluation periods, standard incident response procedures, data validation checks. Agentic AI agent traces are classified here. Monitor them in aggregate for performance trends (invocation rates, error rates, token consumption) in near real-time to detect model degradation before it affects campaign delivery. Analyze individual traces in batches. 
+  **High-latency data (batch, hours to days):** Historical campaign data, third-party data, ad creative assets. Operational requirements: off-peak processing schedules, cost-optimized storage, periodic health checks, lifecycle policies. Historical bid analytics, AB test results, and agent decision audit trails are classified here. 

 For connectivity-layer logs, process filter logs from RTB Fabric in 5–15-minute micro-batches to identify shifts in partner traffic quality or changes in the filtered-to-passed ratio. Error logs require immediate alarming (100% sampling, short evaluation periods). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify all advertising operational data by latency tier:** Create a data classification inventory that includes connectivity-layer metrics and agent traces in addition to standard advertising data. For each data type, document: latency tier, monitoring evaluation period, alarming thresholds, retention period, processing cadence, and the operational procedure to follow when anomalies are detected. 

1.  **Configure monitoring evaluation periods by data tier:** For low-latency operational data (RTB Fabric metrics, bid path latency, impression event rates), configure CloudWatch alarm evaluation periods of 1 minute or less. For medium-latency operational data (audience segmentation freshness, campaign pacing, agent performance trends), configure 5-minute evaluation periods. For high-latency operational data (historical analytics SLAs, archive job completion), configure daily health checks. Mismatched evaluation periods are a common source of delayed detection for latency-sensitive bid path issues. 

1.  **Implement micro-batch processing for agent traces:** Deploy an AWS Glue ETL job running on a 5–15-minute schedule that processes agent traces written to S3 by the trace capture pipeline. The job should compute: per-agent invocation rates, average iteration counts, model latency percentiles, and error rates. Publish these computed metrics as CloudWatch custom metrics. This provides near-real-time visibility into agent health without requiring individual trace analysis in the alarm evaluation path. 

1.  **Define separate retention policies for connectivity-layer logs by category:** Configure CloudWatch Logs retention periods separately for RTB Fabric error logs (90 days: used for partner dispute resolution and debugging) and RTB Fabric filter logs (30 days: high volume, short operational utility). For agent traces in S3, configure lifecycle rules: transition to S3 Glacier Instant Retrieval after 90 days for operational debugging, to S3 Glacier Deep Archive after the compliance retention period, and deletion after the maximum retention period required by applicable regulations. 

1.  **Configure auto-scaling for real-time bidding workloads with aggressive scaling policies:** For bid path services, set Auto Scaling target utilization at 60–65% CPU with scale-out cooldown of 60 seconds and scale-in cooldown of 300 seconds. For audience segmentation services, set target utilization at 70% with 3-minute scale-out cooldown. The asymmetry (faster scale-out for bid path, more conservative for batch workloads) reflects the different consequences of under-provisioning at each latency tier. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [RTB Fabric CloudWatch metrics reference](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-metrics.html) 
+  [Amazon Bedrock Agent Tracing documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 