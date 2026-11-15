

# ADVOPS02-BP08 Monitor server-side auction health and demand partner yield across your header bidding infrastructure
<a name="advops02-bp08"></a>

 Server-side header bidding runs a parallel auction among configured demand partners, replacing the sequential waterfall model with a single, instrumentable decision point. Monitor auction-level health and yield by demand partner to determine whether your demand configuration maximizes publisher revenue. 

 **Desired outcome:** 
+  You have real-time visibility into auction-level health metrics including bid density (bids received per auction) and auction completion latency at the p50, p95, and p99 percentiles. 
+  Your dashboards show yield metrics for each demand partner (win rate, average CPM by format and identity-signal type, and competitive pressure indicators) so you can make data-driven partner portfolio decisions. 
+  You can quantify the revenue impact of identity-signal adoption for each identity framework (UID2, LiveRamp, and ID5) and reconcile your server-side measurement against demand-partner reporting. 

 **Common anti-patterns:** 
+  Monitoring only aggregate auction revenue without breaking it down by adapter, which hides underperforming demand partners behind high-performing ones. 
+  Operating without identity-signal effectiveness metrics, which leaves no visibility into how UID2, LiveRamp, ID5, or other identity solutions affect bid density and CPM across partners. 
+  Relying on demand-partner self-reported metrics without independent server-side measurement, which creates reconciliation gaps between reported and observed bid behavior. 

 **Benefits of establishing this best practice:** 
+  Revenue optimization through yield visibility for each partner that enables targeted configuration improvements. 
+  Identity-signal ROI quantification by correlating identity-solution adoption with measurable CPM lift and bid-density improvements for each partner. 
+  Reconciliation confidence. Independent server-side measurement provides ground truth for demand-partner billing disputes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Server-side header bidding centralizes auction logic that is distributed and opaque in client-side or waterfall models, creating a single instrumentation point where every bid request, response, and no-bid reason is observable. A single auction involves many adapters with distinct latency profiles, identity-signal requirements, and bid behavior, so aggregate metrics such as total revenue or average CPM hide per-partner dynamics. 

 Monitor identity-signal effectiveness because much of your traffic no longer carries third-party cookie signals. Different demand partners bid at different rates on the same identity signal, so without metrics for each partner, you can't quantify identity-solution ROI. 

 [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) provides the metrics infrastructure. If you use [AWS RTB Fabric](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/what-is-rtb-fabric.html) as the connectivity layer, link network metrics complement application auction metrics. See ADVOPS02-BP02 for timeout tracking by adapter, ADVOPS02-BP05 for no-bid reason analysis and holdback measurement, and ADVOPS03-BP04 for integration health for each DSP. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your auction health and yield metric taxonomy:** Document metrics for auction completion latency (p50, p95, p99) and bid density (bids received per auction). For each adapter, capture win rate, average CPM, timeout rate, bid response rate, and identity-signal match rate by framework. Assign each metric a CloudWatch namespace, dimension structure, and update frequency. See [Publishing custom metrics to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html). 

1.  **Build identity-signal effectiveness dashboards:** For each identity solution (UID2, LiveRamp, ID5, and publisher first-party), show match rate (fraction of requests where the signal is present and valid), bid-density lift (bids per auction on identity-enriched compared to no-ID requests), and CPM differential (average CPM on identity-enriched compared to no-ID requests), segmented by demand partner, directly quantifying the revenue value of each framework for each partner. 

1.  **Establish demand-partner reconciliation monitoring:** Implement daily Amazon Athena queries against your bid event log in Amazon S3. For each demand partner, aggregate bid events and delivered impressions with associated spend, then compare against demand-partner invoices and self-reported metrics. Publish discrepancy metrics to CloudWatch and alarm when discrepancies exceed threshold (typically 2–5% for bid-level events, under 1–2% for impression-level events where discrepancies affect billing). Document the reconciliation SLA (for example, investigate within 24 hours of detection). 

1.  **Correlate auction health with adjacent operational layers:** Cross-reference adapter-level timeout instrumentation (ADVOPS02-BP02), no-bid attribution and holdback measurement (ADVOPS02-BP05), DSP integration health (ADVOPS03-BP04), and RTB Fabric network metrics for each link to isolate whether degradation is auction-orchestration, application, or network in origin. Cross-reference identity-signal match rates with upstream identity-resolution service health to distinguish identity-environment issues from adapter integration issues. 

1.  **Implement competitive pressure indicators for yield optimization:** Track bid-density trends over time and calculate the marginal yield contribution per additional bid (the incremental CPM lift from adding a competitor to the auction). Use this to identify adapter combinations where increased competition drives meaningful CPM lift (candidates for new adapter additions), adapters where high bid density doesn't drive proportional CPM improvement (a floor-price optimization opportunity), and adapters with improving or declining competitive pressure over time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns](advops02-bp02.md) 
+  [ADVOPS02-BP05 Monitor partner connectivity health and traffic management effectiveness across your advertising network](advops02-bp05.md) 
+  [ADVOPS03-BP04 Establish third-party DSP integration operations for Prebid Server](advops03-bp04.md) 

 **Related documents:** 
+  [Guidance for Deploying a Prebid Server on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-prebid-server-on-aws/) 
+  [Publishing custom metrics to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [Amazon CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 