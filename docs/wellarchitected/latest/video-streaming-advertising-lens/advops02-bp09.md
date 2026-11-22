

# ADVOPS02-BP09 Implement centralized observability for campaign delivery pacing and fulfillment across linear and digital channels

 Deploy a unified observability stack that provides real-time visibility into campaign delivery, pacing, and fulfillment metrics across both linear TV schedules and digital programmatic pipelines. Use KPI-driven monitoring with anomaly detection to identify delivery issues before they impact campaign outcomes. 

 **Desired outcome:** 
+  Operations teams have a single, authoritative view of campaign health across all delivery channels. 
+  Alerts fire based on business-outcome deviations (delivery pacing, revenue fulfillment) rather than isolated infrastructure metrics. 
+  Cross-channel anomalies are detected automatically, which improves proactive remediation before campaigns miss fulfillment targets. 

 **Common anti-patterns:** 
+  Operating separate monitoring dashboards for linear NOC (focused on playout health) and digital ad ops (focused on ad server metrics) with no correlation between campaign delivery across channels. 
+  Alerting on infrastructure causes (CPU, memory, and disk) rather than business symptoms (delivery pacing deviation, fill rate drop). 
+  Using static thresholds for campaign pacing alerts instead of anomaly detection based on historical delivery patterns. 
+  Relying on batch-processed daily reports to identify under-delivery, which leaves insufficient time for remediation during short campaign flights. 

 **Benefits of establishing this best practice:** 
+  Centralized observability enables faster detection and resolution of delivery issues, reduces campaign under-delivery risk, and provides unified reporting for advertiser transparency. 
+  KPI-driven observability ties technical metrics to business objectives, which makes issues clearer than technical metrics alone. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A campaign sold across linear and digital channels is one commercial commitment, but linear and digital channels have distinct failure modes. 

 Linear delivery runs on a schedule. A spot either aired in its booked position or it did not, and operators track playout health and log discrepancies. 

 Digital delivery runs at a particular rate. Impressions accumulate continuously against a flight, and operators track fill rate and pacing. 

 Neither one of these distinct views informs on whether the campaign is being delivered. To determine this, both channels must report against the same contracted total. 

 Pacing provides these channels a shared measure in delivery completed as a proportion of delivery owed at this point in the flight. Infrastructure metrics are stateless, but pacing is cumulative. Under-delivery that begins early keeps compounding until the campaign team intervenes, and the remaining flight time determines whether recovery is still possible. A campaign discovered to be under-pacing on its final day can't be recovered. Batch reporting fails because reports arrive after the window when action was still possible. 

 In campaign flights, delivery is intentionally uneven. Dayparts, live events, and weekend patterns all produce swings that a fixed threshold could flag as failures. Because flights are short, there is rarely enough history within one campaign to establish a baseline. Baseline against comparable historical flights rather than the current one, to avoid missing under-delivery or constant alerting from tight thresholds. 

 Business-outcome alerts lag, and by the time pacing has degraded, the cause has been running for a while. Infrastructure alerts come first, but a fill-rate dip or a timeout spike alone can produce noise that leads to alert fatigue. 

 Requiring a business symptom and a plausible technical cause to coincide before paging makes the alert early, credible, and routed to the responsible team. 

 Tooling alone does not settle ownership. Linear and digital operations usually belong to separate reporting lines with separate incident processes, and a cross-channel pacing alarm belongs to neither by default. To make the organizational dashboard useful, assign one team accountability for the whole campaign. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy AWS Distro for OpenTelemetry across linear playout and digital ad serving systems:** Configure ADOT collectors as DaemonSets on EKS clusters and as ECS sidecar containers for containerized ad serving workloads. Configure collectors to receive metrics from linear playout infrastructure (MediaLive CloudWatch metrics, scheduling engine metrics) and digital ad serving (Prebid Server metrics, ad server impression counts) and export to Amazon Managed Service for Prometheus. 

1.  **Configure Amazon Managed Grafana as the unified visualization layer:** Add data sources for CloudWatch, Amazon Managed Service for Prometheus, Amazon OpenSearch Service, and AWS X-Ray. Configure AWS Organizations integration for multi-account cross-region access. Build the primary campaign health dashboard: top-level pacing (linear spot delivery percentage, digital impression delivery percentage), mid-level channel health (linear playout status, programmatic fill rate, SGAI ad break completion), and drill-down views by campaign, channel, and time period. 

1.  **Define custom CloudWatch metrics for cross-channel KPIs:** Publish custom metrics for: campaign delivery pacing (percentage of ordered delivery completed compared to flight schedule, updated every 15 minutes), fill rate by channel type (linear avails filled, digital impressions filled), and revenue fulfillment (billed value compared to contracted value). Enable CloudWatch Anomaly Detection on pacing metrics to detect delivery deviations that diverge from historical campaign patterns. 

1.  **Implement CloudWatch Composite Alarms for delivery health indicators:** Create composite alarms that combine multiple delivery signals: (digital fill rate alarm) AND (programmatic timeout rate alarm) fires a "demand-side degradation" composite alarm. (Linear spot delivery alarm) AND (scheduling engine health alarm) fires a "linear fulfillment risk" composite alarm. Configure composite alarms to route to the on-call campaign management team through EventBridge → SNS. 

1.  **Enable AWS X-Ray tracing across the ad decisioning pipeline:** Instrument the ad decisioning path from bid request receipt through creative selection to delivery confirmation with X-Ray. Use X-Ray service maps to visualize end-to-end latency distribution across the decisioning pipeline. Configure X-Ray Group rules that filter traces where end-to-end latency exceeds the campaign SLA budget, creating a dedicated trace group for slow-decisioning events that may indicate under-delivery risk. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack](advops02-bp01.md) 
+  [ADVOPS01-BP06 Implement a unified campaign management interface across linear and digital operations](advops01-bp06.md) 

 **Related documents:** 
+  [AWS Distro for OpenTelemetry documentation](https://aws-otel.github.io/) 
+  [Amazon Managed Grafana best practices](https://docs.aws.amazon.com/grafana/latest/userguide/best-practices.html) 
+  [CloudWatch Composite Alarms and Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) 

 **Related services:** 
+  [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) 
+  [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) 
+  [AWS X-Ray](https://aws.amazon.com/xray/) 