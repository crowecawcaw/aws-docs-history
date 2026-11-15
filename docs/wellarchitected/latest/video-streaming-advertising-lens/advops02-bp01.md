

# ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack
<a name="advops02-bp01"></a>

 Operational excellence in advertising workloads requires monitoring across ad-serving infrastructure, data pipelines, application performance, user experience, partner connectivity, and agentic AI. For publisher workloads, this includes sell-side monitoring on monetization, content delivery pipeline (SGAI), playout health (FAST), and rendering health for innovative ad formats. With a multi-layered approach, you can detect and resolve problems before they affect revenue or the viewer. You can also correlate signals across tiers. 

 **Desired outcome:** 
+  You have observability coverage across the requisite layers in your workload. Every layer has defined KPIs and SLOs. 
+  Operators correlate signals across layers to identify which tier caused an incident. They triage quickly instead of working backward from a vague symptom like slow-loading ads. 
+  Each layer emits structured logs with correlation IDs for cross-layer trace analysis. 
+  Dashboards present layer health hierarchically, from top-level revenue impact down to component-level metrics. Operators drill from symptom to root cause without switching tools. 

 **Common anti-patterns:** 
+  You treat infrastructure monitoring as complete when CPU, memory, and disk are tracked. You skip the higher tiers: application behavior, partner connectivity, agent reasoning, and a dedicated monetization layer. 
+  You rely on a single aggregate latency metric across all partners. This masks degradation for each partner until it cascades. 
+  You deploy AI agents in the bid path without dedicated observability for invocation rates, iteration counts, or tool-call health. 
+  You treat SGAI observability as a single metric (ad break completion). You do not decompose it into manifest generation, CDN delivery, and client-side fetch stages. 
+  You operate separate dashboards for linear NOC and digital ad ops with no correlation between the two systems. 
+  You alert on causes (CPU spikes) instead of symptoms (yield degradation). This produces alert fatigue without business context you can act on. 

 **Benefits of establishing this best practice:** 
+  Faster root cause analysis when incidents cross layers. Infrastructure, application, connectivity, agent, and (for publishers) monetization, SGAI, and FAST signals arrive in a single correlated view. 
+  Lower mean time to detect and resolve, because operators know which tier to investigate first. 
+  Clear operational ownership. Each layer has named metrics, alarms, and runbooks. 
+  Protection against revenue impact from degradations that otherwise appear only after traffic shifts away. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 *Observability* is a deep understanding of a system through its metrics, logs, and traces. With observability, you explore and resolve symptoms through concrete data: CDN cache-hit ratios, SCTE-35 marker validation results, and ad decision server latency. 

 The advertising stack has buy-side and connectivity tiers that require more than application-level monitoring. When partner traffic flows through a managed connectivity service, treat that connectivity layer as a distinct tier with its own failure modes: connection rejections, forwarding delays, and degradation for a specific partner. For workloads on [AWS RTB Fabric](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/what-is-rtb-fabric.html), monitor the AWS/RTBFabric [CloudWatch namespace](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-metrics.html) for gateway and link-level metrics. For workloads with agent orchestration on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/), treat the agent layer as an additional application tier. This tier needs its own monitoring for invocation rates, decision quality, and tool-integration health. 

 Publisher workloads add four sell-side aspects: 

1.  *Monetization* tracks real-time metrics that affect revenue: eCPM trends, fill rate by demand partner, ad break completion, and identity-signal match rate. This layer belongs at the top of every publisher operations dashboard. 

1.  The *content delivery pipeline (SGAI)* tracks manifest generation latency, SCTE-35 marker validation failures, CDN cache-hit ratios, and client-side ad-fetch success. A failure at any stage affects all concurrent viewers. 

1.  *Playout health (FAST)* tracks channel status and scheduling health for channels that run continuously and have no natural recovery window. 

1.  *Rendering health* tracks whether innovative formats (overlays, squeezebacks, pause ads, and shoppable ads) render correctly across targeted device and player combinations. 

 Unify these tiers behind a single visualization. Warner Bros. Discovery does this by converging streaming and linear observability on AWS Distro for OpenTelemetry (ADOT) with Amazon Managed Grafana. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map every layer of your advertising stack and define the metrics that signal health for each:** Cover infrastructure, application, user experience, partner connectivity, agentic AI, and the publisher layers (monetization, SGAI, FAST playout, and rendering). For each metric, document the data source, update frequency, CloudWatch namespace and metric name, alert thresholds, and the responsible team. Use this inventory as the acceptance criterion for observability-completeness reviews. 

1.  **Instrument the infrastructure, application, and user-experience tiers with built-in primitives:** Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics and alarms for infrastructure. Use application logs and custom metrics for bid volume, no-bid rate, and latency percentiles. Use Real User Monitoring or synthetic probes for ad load time, viewability, and playback quality. 

1.  **Instrument the partner connectivity tier:** For RTB Fabric, collect gateway and link-level metrics from the AWS/RTBFabric namespace. Deliver application logs for each link with appropriate sampling. Follow ADVOPS02-BP05 for connectivity observability depth by partner. 

1.  **Instrument the agentic AI tier:** Turn on Amazon Bedrock agent tracing. Publish agent-level custom metrics (invocation rate, iteration count, tool-call health) to CloudWatch with PutMetricData. Follow ADVOPS02-BP06 for distributed tracing patterns across the application and agent tiers. 

1.  **Instrument the monetization layer with real-time revenue-impact metrics:** Deploy custom CloudWatch metrics for eCPM, fill rate by demand partner, ad break completion rate, and identity-signal match rate by framework. Use CloudWatch Contributor Insights to surface the top contributors to fill-rate drops by adapter, content type, and geography. 

1.  **Instrument the publisher delivery tiers (SGAI, FAST, and rendering):** Emit SGAI metrics for each stage: manifest generation latency, SCTE-35 validation failure rate, CDN cache-hit ratio, and client-side fetch success. Carry correlation IDs across the stages. Emit FAST playout metrics from AWS Elemental MediaLive: channel active alerts, input and output frame rates, schedule adherence, and ad pod fill. Emit rendering metrics for innovative formats: success rate, completion, and matching-pipeline latency. 

1.  **Build unified hierarchical dashboards and route alarms to the responsible tier:** Configure Amazon Managed Grafana over CloudWatch, Amazon Managed Service for Prometheus, Amazon OpenSearch Service, and AWS X-Ray. Build three view levels: top-level revenue impact, mid-level layer health, and component-level drill-down. Apply RED (Rate, Errors, and Duration) to delivery services. Apply USE (Utilization, Saturation, and Errors) to infrastructure. Route each alarm to its owning team through [Amazon SNS](https://aws.amazon.com/sns/) and runbooks. Validate cross-layer correlation during game days by injecting controlled failures. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns](advops02-bp02.md) 
+  [ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics](advops02-bp04.md) 
+  [ADVOPS02-BP05 Monitor partner connectivity health and traffic management effectiveness across your advertising network](advops02-bp05.md) 
+  [ADVOPS02-BP06 Implement distributed tracing for automated and agent-driven advertising operations](advops02-bp06.md) 

 **Related documents:** 
+  [Monitoring RTB Fabric with Amazon CloudWatch](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch-metrics.html) 
+  [Amazon Bedrock agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) 
+  [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/) 
+  [Guidance for Advertising Agents on AWS](https://aws.amazon.com/solutions/guidance/advertising-agents-on-aws/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 