

# REL06-BP07 Monitor end-to-end tracing of requests through your system

 In a distributed system, a single request touches many components, and a failure or slowdown in any one of them affects the whole. Tracing follows each request across those components so you can pinpoint where errors and latency originate. This shortens root-cause discovery and reduces the mean time to resolve incidents. 

 **Desired outcome:** 
+  You trace requests across every component, from client to compute to storage. 
+  Your traces correlate with logs, metrics, and alarms so responders move from symptom to cause quickly. 
+  Your tracing includes synthetic canaries and real-user monitoring to capture client-side interaction and latency. 
+  You use a single, integrated tracing solution across cloud-native and third-party components. 

 **Common anti-patterns:** 
+  Teams trace some components but not all, so latency from an untraced component stays hidden. 
+  Teams omit synthetic canaries and real-user monitoring, which leaves client interaction out of the trace. 
+  Teams run cloud-native and third-party tracing tools without integrating them into one solution. 
+  Teams treat tracing as optional instrumentation and add it only after an incident exposes the gap. 

 **Benefits of establishing this best practice:** 
+  You see the full picture of component interactions when responding to an issue. 
+  You spend less time investigating because tracing makes root causes visible. 
+  You make better and faster decisions, such as when to invoke failover or where to add self-healing. 
+  You evaluate performance against service level agreements and objectives using client-side measurements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A *correlation identifier* travels with a request and ties together every operation on its behalf. With that identifier, a tracing tool collects the spans a request generates and assembles them into a *service map* that shows how components interact. A trace that covers the web tier but not the database leaves a blind spot where latency problems occur. Include every component in request traces: service clients, middleware gateways and event buses, compute, and storage such as key-value stores and databases. 

 When a component is uninstrumented, its latency does not disappear from the trace. It appears as time spent on neighboring components. A function with cold starts, for example, can make a downstream call appear slow when the delay is in the caller. Client-side behavior is the most commonly omitted segment. Add synthetic canaries and real-user monitoring to capture the interaction and latency remote clients experience. This is how you measure performance against customer-facing agreements. 

 When you run both cloud and third-party tracing tools, no single system holds all the traces, so you cannot correlate them into one view. Choose one primary tracing solution and integrate everything into it. If the primary solution is cloud-based, instrument components with their SDKs. If it is a third-party tool, configure it to ingest cloud-based trace telemetry. 

 [AWS X-Ray (part of Amazon CloudWatch)](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) collects application telemetry that you can visualize and filter across payloads, functions, traces, services, and APIs. You can turn on X-Ray for many components with no-code or low-code configuration. [Amazon CloudWatch application monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) combines traces with metrics, logs, and alarms in the X-Ray trace map. It also includes synthetics for endpoint monitoring and real-user monitoring for web clients. For open standards and mixed environments, use [AWS Distro for OpenTelemetry](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html) to instrument applications and feed X-Ray. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Turn on tracing for supported AWS services:** Enable [AWS X-Ray on native services](https://docs.aws.amazon.com/xray/latest/devguide/xray-services.html) such as Amazon S3, AWS Lambda, and Amazon API Gateway using configuration toggles in infrastructure as code, the AWS SDKs, or the console. 

1.  **Instrument your application code:** Instrument your components with [AWS Distro for OpenTelemetry and X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html) or a third-party collection agent. Follow the [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) for language-specific instructions on tracing HTTP requests, SQL queries, and other processes. 

1.  **Extend tracing to the client edge:** Use X-Ray tracing with [CloudWatch Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) and [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) so you can analyze the request path from the end-user client through downstream infrastructure. 

1.  **Correlate traces with alarms:** Configure CloudWatch metrics and alarms from resource health and canary telemetry so teams are alerted quickly, then use the X-Ray trace map to move from an alarm into the related traces. 

1.  **Integrate a third-party tracing tool if used:** If a third-party tool is your primary solution, enable its X-Ray integration, such as [Datadog](https://docs.datadoghq.com/tracing/guide/serverless_enable_aws_xray/), [New Relic](https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-x-ray-monitoring-integration/), or [Dynatrace](https://docs.dynatrace.com/docs/ingest-from/amazon-web-services-classic/integrate-with-aws/aws-all-services), so all trace telemetry lands in one place. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 

 **Related documents:** 
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) 
+  [Integrating AWS X-Ray with other AWS services](https://docs.aws.amazon.com/xray/latest/devguide/xray-services.html) 
+  [AWS Distro for OpenTelemetry and AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html) 
+  [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 
+  [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) 
+  [DevOps Monitoring Dashboard on AWS](https://docs.aws.amazon.com/solutions/latest/devops-monitoring-dashboard-on-aws/) 
+  [Reducing MTTR](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html) 
+  [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Observability for AI Agents and Traditional Workloads (COP335)](https://www.youtube.com/watch?v=oYpCvqZk9SQ) 

 **Related examples:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) 

 **Related services:** 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 
+  [Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 