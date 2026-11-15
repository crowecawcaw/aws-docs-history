

# ADVOPS06-BP02 Implement observability for scheduling, ad fill, and playout health
<a name="advops06-bp02"></a>

 FAST channel operations require observability across scheduling accuracy (is content playing as scheduled), ad fill health (are ad pods being filled at expected rates), and playout continuity (is the stream available and playing without interruption). Each of these areas requires its own metrics and alerts, and correlating signals across the three areas identifies the root cause when problems occur. 

 **Desired outcome:** 
+  Real-time visibility into FAST channel scheduling accuracy, ad pod fill rates, and playout continuity, with automated alerting on anomalies. 
+  Automated content gap remediation reduces dead air incidents by detecting scheduling holes and inserting fallback content before gaps reach viewers. 
+  Dashboards present all three dimensions with drill-down capability to component-specific metrics for root cause investigation. 

 **Common anti-patterns:** 
+  Monitoring only infrastructure health metrics without tracking scheduling accuracy or ad fill rates. 
+  Lacking content gap detection until viewers experience dead air. Gaps discovered at playout time have 0 minutes for remediation, while gaps discovered 30 minutes before playout have time for automated or manual remediation. 
+  Treating ad pod under-fill as a business concern rather than an operational alert. 

 **Benefits of establishing this best practice:** 
+  Real-time detection of scheduling conflicts and ad fill failures before they impact viewers. 
+  Automated content gap remediation reduces dead air incidents from hours of MTTR to minutes of automated response. 
+  Data-driven optimization of channel programming and ad operations based on engagement metrics. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Unlike web application errors, which affect individual requests, a scheduling gap creates dead air for every concurrent viewer for the entire duration of the gap. A single 5-minute scheduling error during primetime can affect thousands of viewers and generate viewer complaints and churn that extend beyond the incident itself. 
+  **Scheduling accuracy:** Track schedule adherence (actual content start time compared to scheduled start time within 10-second tolerance), content transition success rates (successful transitions between program entries compared to failed transitions causing dead air), and EPG completeness for the next 2-hour window (percentage of upcoming slots with validated content and correct asset metadata). Scheduling accuracy failures often surface as dead air with no explicit error. A "content not found" error in MediaLive logs is the symptom, while a missing asset reference in the EPG is the root cause. 
+  **Ad fill health:** Track ad pod fill rate (percentage of ad break time filled with paid content compared to slate), fill rate by demand source (adapter-level breakdown to identify which demand source is underperforming), ad break completion rate (percentage of started ad breaks that complete successfully without early return to content), and real-time CPM trend (to detect fill rate drops that aren't yet visible in broader revenue reports). 
+  **Playout continuity:** Track MediaLive input and output video frame rates (zero output frame rate means dead air), MediaLive channel active alerts count, CDN cache hit ratio for content segments, and viewer engagement metrics (viewers staying through ad breaks compared to abandoning during breaks). 

 A Lambda function on a 15-minute schedule looks ahead at the next 30 minutes of EPG to identify gaps before they affect viewers. When a gap is detected, the function inserts fallback content from the slate pool to avoid dead air and notifies content operations to address the underlying scheduling error. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instrument the scheduling engine to emit metrics on schedule adherence and upcoming gap detection:** Deploy custom CloudWatch metrics from the scheduling service: schedule adherence rate (actual compared to scheduled start time within tolerance), content transition success rate, and upcoming gap count (gaps detected in the next 30-minute window by the pre-flight validation). Configure alarms: critical alarm on any content transition failure (immediate response), warning alarm on schedule adherence dropping below 95% (investigation required), informational alert on upcoming gaps detected more than 30 minutes before playout. 

1.  **Configure ad pod fill rate monitoring with tiered alerting thresholds:** Publish ad pod fill rate as a custom CloudWatch metric from the channel assembly service. Configure alarms: critical alarm when fill rate drops below 80% (triggered immediately, revenue impact is significant), warning alarm when fill rate drops below 90% (triggered after 5 consecutive minutes), informational tracking of fill rate trend against 7-day rolling average. Include fill rate by demand source as a dimension to enable targeted adapter-level investigation. 

1.  **Implement automated content gap remediation with fallback content insertion:** Deploy a Lambda function triggered every 15 minutes by EventBridge that scans the next 30 minutes of EPG for gaps. When a gap is detected, automatically insert fallback content from the configured slate pool to fill the gap duration. Send an SNS notification to content operations with the gap details. For gaps detected less than 5 minutes before playout (insufficient remediation time), escalate immediately to the on-call engineer through PagerDuty. 

1.  **Deploy MediaLive monitoring with composite health alarms:** Configure CloudWatch monitoring on MediaLive: InputVideoFrameRate (drops to zero = input failure), OutputVideoFrameRate (drops to zero = output failure), and ActiveAlerts count. Create a composite alarm that fires when OutputVideoFrameRate drops to zero AND ActiveAlerts count exceeds zero. This high-confidence combination reduces false positives from transient metric sampling without delaying response to genuine failures. 

1.  **Implement synthetic viewer probes for full-path health validation:** Deploy a Lambda function that periodically (every 5 minutes) requests the channel's HLS or DASH manifest and validates: HTTP 200 response, current segment timestamps (within expected range), segment URLs resolve successfully, and content segment duration matches expected values. Configure this synthetic probe to alert when 3 consecutive checks fail. A failure here indicates a viewer-facing issue even when all infrastructure metrics appear healthy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS06-BP01 Establish continual linear streaming operational readiness](advops06-bp01.md) 
+  [ADVOPS06-BP03 Establish FAST channel KPI dashboards and operational cadences](advops06-bp03.md) 

 **Related documents:** 
+  [AWS Elemental MediaLive monitoring documentation](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-with-cloudwatch.html) 

 **Related services:** 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 