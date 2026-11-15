

# ADVREL04-BP03 Monitor and manage partner SLAs against actuals
<a name="advrel04-bp03"></a>

 External partners (such as DSPs, SSPs, DMPs, and measurement providers) operate under agreed service-level agreements. Continuously measure each partner's actual availability, latency, and error rates against their committed SLA. Detect, attribute, and act on degradation before it erodes auction performance or revenue. 

 **Desired outcome:** 
+  Each external partner integration has its committed SLA (availability, response latency, and error rate) recorded and continuously compared against measured actuals. 
+  SLA breaches are detected automatically and attributed to the specific partner, with alerting to the owning team. 
+  Partner performance trends inform routing, fallback, and commercial decisions rather than being discovered only during incidents or contract reviews. 

 **Common anti-patterns:** 
+  Treating a contractual SLA as a guarantee and never measuring the partner's actual availability, latency, or error rate. 
+  Aggregating partner metrics together, so one degraded partner is masked by the healthy others. 
+  Detecting partner degradation only through downstream auction symptoms (fill-rate or revenue drops) rather than at the integration boundary. 
+  Holding no historical record of partner performance, so SLA-breach disputes and routing decisions lack evidence. 

 **Benefits of establishing this best practice:** 
+  Partner degradation is detected and attributed at the integration boundary, before it cascades into auction or revenue impact. 
+  Historical data comparing each partner's SLA to its actuals supports routing decisions, fallback tuning, and commercial or contract conversations with partners. 
+  Per-partner visibility reveals slow degradation that never trips defensive automation, which acute failure detection alone would miss. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Circuit breakers and similar defensive patterns react to acute failure (for example, a partner that returns errors at a rate high enough to trip a threshold). Many forms of partner degradation are subtler, such as a DSP with p99 latency drifting upward over weeks or a DMP that intermittently times out during peak traffic. These gradual problems erode fill rates and revenue without triggering any automated response. Detection requires a continual measurement of actual partner behaior against their contract. 

 Attributing degradation to a specific partner is harder. Aggregate metrics across all partners mask individual degradation, because one struggling partner disappears into an average that still looks healthy. Include partner identity as a dimension on every SLA measurement. Without this granularity, degradation surfaces only through downstream symptoms (auction timeouts, fill-rate drops, and revenue anomalies), after impact has spread. 

 Use SLA data beyond incident detection. Routing decisions, fallback tuning, and contract negotiations need a historical record of partner performance data, which helps you avoid relying on anecdotal or memory-based evidence. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Record each partner's committed SLA as configuration:** Store per-partner SLA targets (availability %, p99 latency, and maximum error rate) in a configuration store (for example, AWS AppConfig or a DynamoDB table) rather than hard-coding them. This allows thresholds to track contract changes without code deployment. 

1.  **Instrument partner calls with a partner dimension:** Emit CloudWatch metrics for every external partner call tagged with the partner identity: request count, error count, and response latency. Per-partner dimensions keep one degraded partner from being masked by aggregate health. 

1.  **Alarm on SLA breaches per partner:** Create CloudWatch alarms that compare measured actuals against each partner's configured SLA (for example, p99 latency exceeding the committed value over a 5-minute window, or availability dropping below the committed percentage). Route alarms to the team that owns the partner relationship. 

1.  **Retain and report partner performance trends:** Persist per-partner performance data (for example, to Amazon S3 or Amazon Timestream) and produce periodic reports comparing SLA to actuals. Use these trends to inform routing weight, fallback configuration, and commercial reviews with partners. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL02-BP03 Avoid scale mismatch of both internal services and external partners](advrel02-bp03.md) 

 **Related documents:** 
+  [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) 
+  [AWS AppConfig - feature flags and configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/) 
+  [Amazon Timestream](https://aws.amazon.com/timestream/) 