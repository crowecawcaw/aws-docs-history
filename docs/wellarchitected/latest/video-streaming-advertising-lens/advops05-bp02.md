

# ADVOPS05-BP02 Implement observability for ad break orchestration across server and client
<a name="advops05-bp02"></a>

 Because SGAI is hybrid, failures can occur at the server manifest, CDN caching, or client ad fetch layer, so you need cross-component observability to distinguish between failure origins. To identify root causes quickly, maintain full visibility from server-side manifest generation through CDN-cached delivery to client-side personalized ad fetching. 

 **Desired outcome:** 
+  Full visibility into ad break orchestration (from server-side manifest generation through CDN delivery to client-side personalized ad fetching) with correlated tracing across all components. 
+  Ad break completion rate SLO is defined and monitored with automated alerting when completion drops below threshold. 
+  Player-side ad fetch timeouts are monitored with categorization of timeout causes (demand partner latency, network issues, manifest errors) to enable targeted remediation. 

 **Common anti-patterns:** 
+  You monitor only server-side manifest generation without visibility into CDN delivery or client-side ad fetch outcomes, and you treat ad break failures as client-only issues without investigating server-side root causes. 
+  You do not have correlated tracing across the server-CDN-client pipeline. 
+  Conflating hybrid SGAI operational patterns with personalized SGAI patterns. 

 **Benefits of establishing this best practice:** 
+  Full visibility enabling rapid root cause identification across pipeline layers. 
+  Reduced MTTR for ad break failures through pre-built cross-layer analysis capabilities. 
+  Data-driven SLO management for ad break completion rates. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In hybrid SGAI architectures, failures can originate in three distinct layers, and symptoms at one layer often have root causes at another. Without correlated tracing across components, incident responders waste time investigating the wrong layer, which extends MTTR. Those layers (and their failure profiles) are: 
+  **Server manifest generation layer:** Manifest generation latency spikes, SCTE-35 marker validation failures, manifest formatting errors. Failures here affect all concurrent viewers (CDN-cached manifests serve all viewers from a single copy). Detection requires server-side metrics: manifest generation error rate, validation failure rate by message type, manifest generation p99 latency. 
+  **CDN delivery layer:** Cache hit ratio drops, manifest distribution failures, CloudFront origin errors. Failures here affect all viewers served by the affected CDN PoP. Detection requires CloudFront metrics: cache hit ratio, origin error rate, and cache invalidation success and failure rates. 
+  **Client ad fetch layer:** Player-side VAST request timeouts, ad creative fetch failures, ad rendering errors. Failures here affect individual viewer sessions (session-scoped impact for personalized SGAI, may be broader for hybrid SGAI if a shared demand partner is degraded). Detection requires client-side telemetry aggregated server-side. 

 Correlating one failed ad break across these layers is hard because each layer records data in its own terms. The origin records requests, the CDN records URLs and edge locations, and the player records sessions and break positions. These are three identifier spaces with no natural intersection point and timestamped with separate clocks. 

 Sampling compounds the problem. When each layer independently decides which events to record, the traffic that survives every layer's decision shrinks to a fraction, and the rare failure worth investigating is often the trace missing a segment. The client is the only component that observes what the viewer actually saw, such as a pod that never rendered or a stall mid-break, but the information it reports is not always reliable. The same degraded network that broke the ad fetch also drops the telemetry signal that would report it, and sessions that crash never flush their final events. Because the failing population underreports itself, treat absence of client telemetry as evidence of a problem, not a sign of health. 

 Ad break completion rate is the primary health indicator because it captures the integrated outcome of all three layers. A drop in completion rate without a corresponding manifest generation error or CDN anomaly points to the client ad fetch layer as the root cause. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement AWS X-Ray distributed tracing across SGAI pipeline stages:** Instrument the manifest generation service with X-Ray custom subsegments. Pass the X-Ray trace ID as a response header to CloudFront, which includes it in access logs. Collect client-side ad fetch events (with trace ID where available) through Kinesis. This enables correlation between manifest generation timing, CDN delivery, and client-side ad fetch outcomes for the same ad break. 

1.  **Define ad break completion rate SLOs and configure CloudWatch alarms:** Establish ad break completion rate SLOs based on historical data (typically 95%\+ for established FAST channel deployments). Configure CloudWatch alarms that trigger when completion rates breach thresholds. Set the alarm evaluation period to 5 minutes to detect sustained degradation while filtering transient one-off failures. Route critical completion rate alarms to the on-call engineer with high-priority notification. 

1.  **Build a unified ad break lifecycle dashboard:** Create a CloudWatch dashboard that displays all three pipeline layers side-by-side: server-side (manifest generation latency, validation failure rate), CDN layer (cache hit ratio, origin error rate), and client-side (ad fetch success rate, timeout rate by cause). This unified view enables operators to identify which layer is degraded during an incident without navigating between multiple monitoring tools. 

1.  **Instrument player-side ad fetch timeout monitoring with cause categorization:** Deploy player-side event collection that categorizes ad fetch timeout causes: demand partner latency (VAST request timed out before receiving a response), network issues (connection establishment failed or connection dropped mid-request), and manifest errors (ad asset URL from manifest is malformed or unreachable). Aggregate these events through Kinesis with 1-minute resolution. Alert when any single cause category exceeds baseline rates. 

1.  **Establish weekly ad break health reviews:** Schedule weekly reviews of ad break completion rate trends, timeout patterns, and cross-layer failure correlations. Use these reviews to identify slowly degrading failure modes that individual alarms miss, a gradual 2% per week decline in completion rate that stays below alarm threshold but represents significant revenue leakage over a month. Produce action items for threshold adjustments, runbook updates, or architectural improvements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS05-BP01 Implement manifest generation observability with SCTE-35 marker validation](advops05-bp01.md) 
+  [ADVOPS05-BP03 Create SGAI-specific runbooks and playbooks for manifest and player failures](advops05-bp03.md) 

 **Related documents:** 
+  [AWS X-Ray distributed tracing documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [AWS Elemental MediaTailor monitoring documentation](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch.html) 

 **Related services:** 
+  [AWS X-Ray](https://aws.amazon.com/xray/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 