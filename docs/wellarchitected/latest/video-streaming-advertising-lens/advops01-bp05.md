

# ADVOPS01-BP05 Foster a publisher operations culture that prioritizes yield reliability
<a name="advops01-bp05"></a>

 Build a culture that treats yield reliability with the same urgency as system availability. This best practice addresses how teams proactively monitor monetization health and treat revenue-impacting incidents with defined severity classifications, using shared dashboards visible to both engineering and ad operations, and escalation paths that mirror infrastructure incident severity levels. 

 **Desired outcome:** 
+  Publisher operations teams participate in regular yield review meetings, maintain shared dashboards visible to both engineering and ad operations, and have defined escalation paths for yield anomalies. 
+  Yield degradation is treated as an operational incident, not a business-only concern, with severity classifications that trigger defined response procedures. 
+  Mean time to detect (MTTD) for yield anomalies that affect revenue is measured and continuously improved. 

 **Common anti-patterns:** 
+  Treating yield degradation as a business-only concern rather than an operational incident, leading to delayed detection and response. 
+  Ad operations and engineering teams operating in silos without shared dashboards. Ad operations sees revenue dropping but can't correlate it to infrastructure events, while engineering sees healthy infrastructure metrics but is unaware of yield impact. 
+  No defined severity levels for anomalies that affect revenue. Every yield issue gets the same (slow) response regardless of magnitude. 

 **Benefits of establishing this best practice:** 
+  Faster detection and resolution of issues that affect yield. 
+  Shared accountability between engineering and ad operations. 
+  Reduced sustained monetization losses from prolonged undetected yield degradation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A stream can serve every request and render every frame while revenue drops. Latency and error rates do not tell you whether inventory is converting. Mean time to detect (MTTD) measures how long yield degradation goes unnoticed. 

 Ad demand swings with auction timing, seasonality, and demand partner behavior. A useful threshold separates normal noise from a signal worth paging the on-call. 

 This practice usually breaks on ownership, because engineers treat revenue metrics as a business concern and resist being on-call for them. Ad operations can see revenue dropping but can't inspect infrastructure to explain it. The two teams end up with different views. Detection and resolution need named owners before any tooling helps. You can assign these roles to different people, but neither role can be implicit. 

 On-call engineers already follow an incident process for outages. A parallel process creates confusion about which one applies. Route yield events through the escalation process the team already trusts, because teams often skip separate processes under pressure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define yield anomaly severity classifications:** Document severity levels for events that affect yield with specific thresholds: Sev-1 (sustained eCPM drop >15% or fill rate drop >20% over 10 minutes), Sev-2 (sustained eCPM drop >5% or fill rate drop >10% over 30 minutes), Sev-3 (eCPM declining trend >3% over 24 hours). Align these thresholds with estimated revenue impact. Obtain sign-off from engineering and ad operations leadership to make the severity classifications official policy. 

1.  **Build shared yield dashboards in Amazon CloudWatch and Quick:** Create Amazon CloudWatch dashboards displaying real-time yield KPIs (eCPM, fill rate by demand partner, ad break completion rate) alongside infrastructure health metrics (latency, error rates). Build Quick dashboards for trend analysis accessible to business stakeholders. Confirm both dashboards use the same underlying data sources so there is a single version of the truth. 

1.  **Establish a weekly yield review cadence:** Schedule a weekly cross-functional yield review meeting with a defined standing agenda: eCPM trend analysis (current week compared to previous 4-week average), fill rate patterns by demand partner and ad format, open incidents that affect yield and their status, and forward-looking risks (planned infrastructure changes, upcoming campaign launches). Document action items with owners and due dates. 

1.  **Configure automated alerting for yield anomaly severity breaches:** Set up CloudWatch Alarms on yield metrics with thresholds matching the severity classifications from step 1. Route Sev-1 and Sev-2 alarms to the on-call rotation through Amazon SNS and your incident management system (PagerDuty, OpsGenie). Confirm the on-call rotation for ad operations and engineering covers yield metric alerts, not just infrastructure alerts. 

1.  **Conduct quarterly retrospectives on yield culture maturity:** Measure improvements in MTTD for anomalies that affect revenue over time using CloudWatch metrics and incident logs. Track: average time from yield degradation onset to first alarm, average time from first alarm to incident declaration, and average time from incident declaration to resolution. Set quarterly improvement targets and report results to leadership as evidence of cultural maturity progress. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS01-BP03 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)](advops01-bp03.md) 
+  [ADVOPS07-BP04 Conduct post-incident reviews for revenue-affecting events](advops07-bp04.md) 

 **Related documents:** 
+  [Amazon CloudWatch dashboards documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Quick embedded analytics](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Quick](https://aws.amazon.com/quicksight/) 