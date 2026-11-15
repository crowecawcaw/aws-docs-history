

# ADVREL05-BP02 Monitor Availability Zone-level health and detect asymmetric failures
<a name="advrel05-bp02"></a>

 Partial degradation (increased latency, packet loss, or intermittent errors in a single Availability Zone) can erode bid win rates without triggering a full failover. Use Availability Zone-aware monitoring to detect these conditions. 

 **Desired outcome:** 
+  Metrics carry an Availability Zone dimension so per-AZ health is visible side by side. 
+  Per-AZ alarms detect partial degradation (latency, error rate, asymmetric traffic) before it materially affects bid win rates. 
+  Synthetic bid probes surface Availability Zone-level impairment ahead of real-traffic impact. 

 **Common anti-patterns:** 
+  Treating Availability Zone health as binary and missing partial degradation such as elevated latency or packet loss. 
+  Aggregating metrics across Availability Zones, which masks a single degraded Availability Zone. 
+  Tagging metrics by Availability Zone instead of ID, so mapping is inconsistent across accounts. 

 **Benefits of establishing this best practice:** 
+  Early detection of partial Availability Zone impairment helps catch bid-win-rate erosion that would otherwise go undetected. 
+  Per-AZ visibility enables rapid triage and confident failover decisions during incidents. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Partial failure is more difficult to detect than total failure. For example, a zone can answer slowly, drop a fraction of packets, or return intermittent errors while displaying good system health. In a latency-sensitive auction, that degraded zone keeps accepting bids and loses them, so bid outcomes degrade before infrastructure signals display a problem. 

 Averaged metrics can obscure actually useful signals for your workload. When you sum or average across zones, a single degraded zone disappears into the healthy majority, and the dashboard shows that your operation is healthy despite a degrading win rate. Show each zone on its own to expose a single-zone fault. Apply the same per-zone view to traffic share, because a quiet zone is often the first sign of a problem in that zone. 

 Consistency across accounts depends on how you identify a zone. The friendly zone name maps to different physical zones in different accounts, so an alarm keyed to a name can watch one physical zone in one account and a different one elsewhere. Physical zone identifiers stay stable across accounts and remove that ambiguity. Cross-account correlation must rely on the stable identifier. 

 Use two complementary detection strategies. Passive alarms watch real traffic and react after bidders are already affected, which makes them accurate but late. Active probes send synthetic bid requests into each zone and can surface a fault before real traffic is affected, at the cost of traffic you generate yourself. Business signals lead the infrastructure metrics, because a zone often loses auctions before its network or error counters look abnormal. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Tag metrics with an Availability Zone dimension:** Instrument metrics with an Availability Zone dimension (for example, tag CloudWatch metrics by Availability Zone ID, not just name, to maintain consistency across accounts). 

1.  **Alarm on per-AZ infrastructure metrics:** Set CloudWatch alarms on per-AZ metrics: gateway connection counts, bid request error rates, response latency (p99), and throughput. 

1.  **Detect asymmetric traffic distribution:** Create alarms for asymmetric traffic distribution. If one Availability Zone is handling significantly less traffic than others, it may indicate partial Availability Zone degradation or unhealthy gateways. 

1.  **Monitor RTB business metrics per Availability Zone:** Monitor RTB-specific business metrics per Availability Zone: bid response timeouts, auction win rates, and no-bid rates. A spike in timeouts in one Availability Zone is an early signal of impairment. 

1.  **Build a per-AZ health dashboard:** Build a CloudWatch dashboard showing per-AZ health side by side for rapid visual triage during incidents. 

1.  **Run synthetic bid probes per Availability Zone:** Use synthetic bid request probes per Availability Zone to detect degradation before it affects real traffic. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 
+  [ADVREL05-BP01 Deploy partner-facing bid gateways across multiple Availability Zones](advrel05-bp01.md) 

 **Related documents:** 
+  [CloudWatch Cross-Account Cross-Region Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_crossaccount_dashboard.html) 
+  [Using AZ IDs for Consistent AZ Mapping](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudWatch Contributor Insights](https://aws.amazon.com/cloudwatch/features/) 