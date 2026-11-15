

# ADVOPS06-BP03 Establish FAST channel KPI dashboards and operational cadences
<a name="advops06-bp03"></a>

 Without dedicated KPI tracking and regular operational reviews, FAST channel performance degrades undetected until revenue drops or viewers churn. Dedicated dashboards and weekly cross-functional reviews create the visibility and accountability to maintain monetization health across continual linear streaming operations. 

 **Desired outcome:** 
+  Dedicated FAST channel dashboards provide real-time and trend visibility into channel uptime, ad monetization, and viewer engagement. 
+  KPIs are reviewed in regular cross-functional operational cadences involving engineering, content, and ad operations teams. 
+  Performance targets are defined for each KPI, with automated alerting when metrics breach target thresholds. 

 **Common anti-patterns:** 
+  Operating FAST channels without dedicated KPI dashboards, relying instead on periodic manual reporting from ad servers and play logs. 
+  Lacking regular cross-functional reviews where engineering, content, and ad operations jointly analyze channel performance. 
+  Not defining uptime or fill rate targets, which makes it difficult to determine whether observed performance is acceptable or requires intervention. 

 **Benefits of establishing this best practice:** 
+  Early detection of performance degradation through trend analysis before it becomes a revenue crisis. 
+  Cross-functional alignment on channel health priorities. 
+  Data-driven decision-making for programming and ad operations optimization. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 No single metric captures a FAST channel's health, because availability, monetization, and audience engagement change independently. A channel can maintain perfect uptime and still lose revenue when inventory goes unsold. It can fill every ad break and still lose viewers to weak programming. Each dimension needs its own metric, because a problem in one dimension can otherwise stay hidden behind a healthy reading in another. 

 A useful metric points to the team that can act on the problem. Declining viewership during otherwise stable operations indicates a content problem, so paging an engineer accomplishes nothing. Assign each metric a clear owner, because a metric with no owner generates alerts that go unresolved. 

 Real-time views catch a fault while an operator can still act on it, and trend views expose the slow decline that no single moment reveals. Set thresholds tight enough to catch a real decline and loose enough that the team does not suffer from alert fatigue. Genre also affects what counts as normal, so a news channel and a niche channel can't share a single target. Threshold calibration remains an ongoing task as the audience grows. 

 Content teams report viewer growth while fill rate slips, and ad operations defends monetization while uptime erodes. The whole channel's state only becomes visible when these teams meet. An around-the-clock channel degrades slowly, and slow problems rarely get attention until revenue has already dropped. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define FAST channel operational KPIs with performance targets:** Document the complete KPI list: channel uptime, target: 99.9% uptime (approximately 8.7 hours of downtime per year). Monitor as a calculated metric: uptime percentage = (total minutes in period − minutes with OutputVideoFrameRate = 0) / total minutes in period. ad pod fill rate (target varies by channel, establish based on first 4 weeks of operation), viewer hours per channel per day (track trend, set target based on launch benchmark), content rotation effectiveness (percentage of content library that plays in a 7-day window), and revenue per viewer hour. Establish measurement methodology for each metric before building dashboards. 

1.  **Build real-time operational dashboards in CloudWatch and trend dashboards in Quick:** Create CloudWatch dashboards with real-time KPI gauges (current values against targets) for the on-call and ad operations teams. Create Quick dashboards with trend visualizations (13-week time series for each KPI, anomaly detection overlays) for the weekly operational review. Make sure both dashboard sets use the same underlying data sources so there is a single version of KPI truth. 

1.  **Establish weekly cross-functional FAST channel operational reviews:** Schedule weekly 30-minute reviews with mandatory attendance from engineering, content, and ad operations. Standing agenda: (1) KPI review: current week compared to 4-week average for all KPIs, (2) incident review: all incidents from the previous week with status and action items, (3) forward-looking risks: upcoming programming changes, live events, planned maintenance, (4) action item review: completion status of items from previous meeting. Produce brief written notes with action items, owners, and due dates. 

1.  **Configure automated alerting for KPI threshold breaches:** For each KPI, configure CloudWatch alarms at two levels: a "warning" level that triggers investigation (fill rate below 85% for 15 consecutive minutes) and a "critical" level that triggers immediate response (fill rate below 75% for 5 consecutive minutes). Route critical alarms to the on-call rotation through PagerDuty. Route warning alarms to the ad operations team Slack channel for awareness and investigation. 

1.  **Conduct monthly KPI framework reviews to refine thresholds and add new indicators:** Schedule monthly reviews specifically focused on the KPI framework itself (separate from the weekly operational review). Review: are current thresholds generating appropriate alert volumes (not too many false positives, not missing real issues), are there new KPIs to add based on operational experience (for example, ad pod completion by demand source if a specific adapter is consistently underperforming), and are target levels still aligned with business expectations (targets should evolve as the channel matures and audience grows). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS06-BP01 Establish continual linear streaming operational readiness](advops06-bp01.md) 
+  [ADVOPS06-BP02 Implement observability for scheduling, ad fill, and playout health](advops06-bp02.md) 

 **Related documents:** 
+  [Quick dashboard documentation](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html) 
+  [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 

 **Related services:** 
+  [Quick](https://aws.amazon.com/quicksight/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 