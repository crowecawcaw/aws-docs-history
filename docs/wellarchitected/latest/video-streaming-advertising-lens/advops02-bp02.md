

# ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns
<a name="advops02-bp02"></a>

 Advertising workloads spike in traffic and resource use, and both performance and yield vary with them. To keep observability across shifting workloads, collect granular, near-real-time metrics across every tier: infrastructure, application, partner connectivity, database, agentic AI, and (for publisher workloads) monetization, SGAI delivery, and FAST playout. Segment metrics by partner and adapter, apply anomaly detection, and tier alarms to business outcomes so issues surface before they hit bid win rate or campaign delivery. 

 **Desired outcome:** 
+  You collect granular (one-second granularity where cost-justified) metrics across every tier, with KPIs and SLOs defined for each tier. 
+  Visibility by adapter, partner, and content type supports targeted yield optimization rather than masking individual problems behind aggregate metrics. 
+  Anomaly detection and tiered alarms catch degradations by partner, agent, and adapter (distinguishing warning-level from critical failures that affect revenue) before they hit bid win rate or campaign delivery. 
+  Identity-signal pass-through rates are monitored across standardized frameworks (UID2, LiveRamp, ID5, publisher first-party, and no-ID) to surface identity-resilience issues. 

 **Common anti-patterns:** 
+  Treating all no-bids as a single metric, hiding whether the bidder chose not to bid or whether a traffic-management module filtered the request before it reached the application. 
+  Relying on default one-minute monitoring granularity for bid-path measurements that need one-second resolution. 
+  Setting uniform alarm thresholds without baselining each adapter. 
+  Monitoring only aggregate latency across all partners, hiding degradation at individual partners until it cascades into revenue loss. 
+  Deploying AI agents in the bid path without built-in agent metrics (invocation count, TTFT, token consumption, and model latency), leaving operations without a view into their behavior. 
+  Monitoring SGAI metrics only at aggregate level, without breakdown by content type or ad break, and lacking identity-signal pass-through monitoring across frameworks. 

 **Benefits of establishing this best practice:** 
+  Reliable, responsive advertising infrastructure even during high-demand periods, with detection of transient yield anomalies that coarse metrics miss. 
+  Layer-by-layer and adapter-level clarity that accelerates incident triage and shortens mean time to resolution. 
+  Tiered alarming that reduces alert fatigue while making sure critical issues that affect revenue receive immediate attention. 
+  Data-driven optimization that informs agent configurations, partner routing, and capacity decisions through measured behavior. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publisher and bid-path yield metrics need higher resolution and finer dimensionality than standard infrastructure metrics. Collect bid-path metrics at one-second granularity where cost permits: bid requests per second, bid response time (p50/p95/p99), bid win rate, and timeout rate. Segment by partner and adapter, plus region where topology matters, so degradation in one segment isn't averaged away by healthy segments. Distinguish no-bids by reason code (application-generated or filtered upstream by a traffic-management module), because the two have different owners and remedies. 

 Attribution depends on measuring at each layer of your architecture. A bid that misses its deadline looks identical to the application no matter which layer consumed the time, so an application-level timeout metric does not tell you where the problem exists. Measure each layer where the time is spent. A bid-path dashboard organized by layer, not by service, can help you answer root-cause questions. 

 Units and definitions vary between layers, and carrying a unit assumption across a layer boundary produces wrong conclusions. A latency figure reported in microseconds against a dashboard axis built for milliseconds understates the value by three orders of magnitude, which reads as a healthy system. Check the unit explicitly for each metric, because the same word means different things in different namespaces. 

 Managed inference reports on the agent layer (invocations, latency, throttles, tokens), but no service metric captures the quality of the agent's recommendation. Emit the business outcome yourself and join it to the service metric. This pair separates a resource-intensive agent producing poor recommendations from an expensive one producing high-quality recommendations. 

 Thresholds are hard to set for yield metrics, because the commercially important metrics are the ones that move for legitimate reasons. Fill rate and eCPM shift with daypart and seasonality, and with the demand mix behind them, so a single fixed bound doesn't fit. Each adapter is also its own population. One might time out on a tenth of requests while another treats that as an outage. Compare a partner against its own history, and set alarm tiers to match how the team responds, reserving immediate response for high-criticality alerts. Segment yield metrics by identity dimension, because a match-rate collapse in one framework on one partner is an integration failure, while the same drop across all frameworks is a marketplace condition. 

 High-cardinality, high-frequency metrics incur charges that scale with the volume of metrics and requests, so decide which signals justify the resolution. Beyond the cost, synchronous instrumentation in the bid path adds latency to the request it was meant to measure. Emit off the request path, and accept sampling for signals that don't page. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define KPIs and SLOs for each tier:** Document business-tied metrics and SLOs for infrastructure, application, connectivity, database, agent, and publisher yield layers, as the anchor for alarm design and dashboard layout. 

1.  **Instrument application-layer metrics for each partner with no-bid reason codes:** Emit bid request count, no-bid count (reason codes distinguishing application-generated from network-generated), timeout count, server-error count, throughput, and P90/P95/P99 response latency, tagged with partner identity, to Amazon CloudWatch. 

1.  **Baseline each adapter and content type, then tier alarms against the baseline:** Use at least two weeks of production data to baseline bid response rate, timeout rate, and eCPM contribution for each adapter, then set tiered alarms relative to that baseline (for example, twice the adapter's own baseline) so naturally higher-baseline adapters don't generate false positives. 

1.  **Collect connectivity metrics for each link:** For AWS RTB Fabric, subscribe to the AWS/RTBFabric namespace for each link, capturing the Link, HttpStatusCode, and Statistic dimensions needed for percentile alarms and anomaly detection. Account for the microsecond unit on latency metrics in dashboards and thresholds. 

1.  **Track database-tier latency in the bid path:** Monitor read and write latency, throughput, error rates, and connection counts for bid-path databases (Amazon DynamoDB, Amazon RDS) independently, so database saturation is attributed directly rather than appearing only as application timeouts. 

1.  **Instrument agent-layer metrics:** Enable the built-in AWS/Bedrock/Agents metrics (invocation count, TTFT, latency, token consumption, and error categories) by AgentAliasArn, and emit custom metrics by using PutMetricData for business outcomes Amazon Bedrock doesn't publish (bid win rate per agent recommendation, decision quality). 

1.  **Instrument publisher yield and identity-framework metrics:** Publish header-bidding timeout rates, request-to-response ratios, and eCPM contribution segmented by identity framework (UID2, LiveRamp, ID5, first-party, and no-ID), plus SGAI metrics by stage (manifest-generation error rate, ad break completion) broken out by content type. 

1.  **Apply anomaly detection and composite alarms:** Enable [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on variable metrics (eCPM, fill rate, link-level latency) with at least 14 days of training data, and keep static thresholds for invariant conditions (target-ip-count=0, manifest-generation errors). Create composite alarms that fire when a link-level latency anomaly AND an adapter timeout-rate spike occur together, for higher-confidence detection and fewer false positives. 

1.  **Build correlated dashboards, route alarms, and optimize cost:** Display infrastructure, application, connectivity, database, agent, and publisher metrics side by side. Route each alarm to its owning tier through [Amazon SNS](https://aws.amazon.com/sns/) (consider one topic for each tier), and review metric cardinality and emission frequency monthly, keeping critical bid-path metrics at high granularity while moving lower-urgency signals to longer intervals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack](advops02-bp01.md) 
+  [ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics](advops02-bp04.md) 
+  [ADVOPS02-BP05 Monitor partner connectivity health and traffic management effectiveness across your advertising network](advops02-bp05.md) 
+  [ADVOPS02-BP06 Implement distributed tracing for automated and agent-driven advertising operations](advops02-bp06.md) 

 **Related documents:** 
+  [RTB Fabric CloudWatch metrics reference](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-metrics.html) 
+  [Amazon Bedrock agent metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-cw.html) 
+  [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [Publishing custom metrics in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [Monitoring metrics in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 