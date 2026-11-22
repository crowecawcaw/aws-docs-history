

# PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical

 Workload components contribute unequally to the customer experience, user-perceived latency, and operating cost. Instrument the workload to reveal those pressure points, and focus optimization on them. 

 **Desired outcome:** 
+  You have instrumentation across the performance-relevant paths of the workload, from client sessions through application code to data stores. 
+  Your metrics, traces, and logs are correlated so a single slow request is traceable across component boundaries. 
+  You know which components sit on the critical path for customer-facing latency and cost. 
+  Your dashboards show performance against business KPIs, not just raw resource counters. 
+  Your team reviews performance data continuously, not only when an incident occurs. 

 **Common anti-patterns:** 
+  Teams rely only on the default metrics emitted by their monitoring tool and never add workload-specific instrumentation. 
+  Teams review metrics only when something breaks, so they have no baseline to compare against. 
+  Developers instrument code without reference to the KPIs the workload is measured on. 
+  Teams collect metrics but build no dashboards that relate them to business outcomes. 
+  Teams select monitoring tools that are expensive to run and hard to maintain. 
+  Teams treat each component in isolation and never correlate signals across layers to explain a system-wide slowdown. 
+  Teams treat AI-generated investigation hypotheses as confirmed root causes without validating them against telemetry or subsequent tests. 

 **Benefits of establishing this best practice:** 
+  You spend optimization effort where it changes the customer experience, not on components that are already fast enough. 
+  You detect bottlenecks during traffic growth, before users report degradation. 
+  You explain the root cause of a slowdown faster because signals from different layers line up. 
+  You justify performance work with data that ties back to business KPIs. 
+  You keep monitoring cost proportional to the value it delivers by instrumenting deliberately. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Monitor to find the components with the greatest effect before your customers do. Instrumentation must reveal the *critical path*: the sequence of calls a user request travels, and the point on that path where time accumulates. Default metrics like CPU and memory show resource activity. They do not indicate whether a resource is on the critical path between a customer and the response they are waiting for. 

 Observability has three signal types. Metrics tell you *that* something is slow. Traces tell you *where* the time went across services. Logs tell you *why* a request behaved as it did. Metrics without traces surface a spike without its downstream cause. Traces without logs surface a slow database call without the query behind it. A shared request identifier links the spike, the span, and the log line. 

 Sampling, aggregation, and retention balance detail against cost. Decide up front which questions the data must answer. 

 Normal traffic does not reveal every bottleneck. Load testing and synthetic monitoring generate traffic on demand, so scaling limits and slow paths surface under controlled conditions before a real peak. Synthetic canaries also produce a consistent baseline for comparison with real user behavior. 

 Once you see the critical path, choose the statistics you track on it. Averages and P99 miss the small number of extreme outliers that take much longer than the rest. Some operations depend on a predictable completion time, such as a clone, backup, or provisioning step. For those, monitor the maximum or P100 alongside average and P99. Define an evaluation window and minimum sample count so a single outlier does not create a misleading alarm. Investigate extreme values separately from improvements to typical latency. 

 AWS provides monitoring capabilities for each performance-relevant layer of a workload. [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) captures performance from real client-side sessions. [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) provides application performance monitoring, service maps, correlated telemetry, and service level objectives. Instrument applications with [OpenTelemetry](https://opentelemetry.io/) or [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) and send traces to supported backends such as [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html). X-Ray remains supported, but its SDKs and daemon are in maintenance mode. Migrate application instrumentation to OpenTelemetry. [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) and [RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) expose database and operating-system performance. 

 For generative AI and agentic workloads, collect model, retrieval, memory, and tool-call spans alongside infrastructure metrics. Track signals such as time to first token, output token throughput, quota pressure, end-to-end completion time, and task success. [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) provides model and agent views with prompt tracing, latency, token usage, and error telemetry. [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) and [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) correlate telemetry, code, and deployment changes to surface bottleneck and root-cause hypotheses. Validate agent-generated findings against the underlying telemetry and confirm improvements with subsequent measurements or tests. [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) collects metrics from applications and containers, and [Amazon Managed Grafana](https://aws.amazon.com/grafana/) visualizes them alongside business KPIs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map the critical performance paths:** Trace how a customer request flows through the workload and identify the components on that path that most affect latency, cost, or customer experience. Rank these areas so instrumentation and later optimization focus on the parts that matter most. 

1.  **Instrument each performance-relevant layer of the workload:** Use [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) for client sessions, [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) with OpenTelemetry or [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) for application services and traces, and [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) with [RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) for data stores. For generative AI and agentic paths, include model, retrieval, memory, and tool calls and collect latency, token, quota, error, and task-success signals. 

1.  **Generate traffic to expose bottlenecks:** Set up [Amazon CloudWatch Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to replay browser activity on a schedule and produce a consistent baseline. Use [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) to drive peak and growth-rate traffic and find where the workload stops scaling linearly. 

1.  **Correlate, visualize, and investigate the signals:** Bring metrics, traces, logs, and deployment events together so a single request is traceable across layers. Use Application Signals or build dashboards in [Amazon Managed Grafana](https://aws.amazon.com/grafana/) to show performance against business KPIs. Use [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) or [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) to accelerate analysis of unfamiliar bottlenecks, and validate their hypotheses against the source telemetry. 

1.  **Prioritize improvements and measure them:** Review the instrumented critical areas with your team, agree on the highest-impact fixes, and apply changes one at a time. Measure each change against the baseline so you keep only the improvements the data confirms. 

1.  **Target tail and worst-case latency on predictability-sensitive operations:** Monitor P99 together with the maximum or P100 for operations where customers depend on a consistent completion time. Choose an evaluation window and minimum sample count based on request volume and the review cadence. Use CloudWatch percentile statistics for P100 and the Maximum statistic where each is supported, and treat extreme outliers as a distinct investigation from improving average or P99 latency. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 
+  [PERF02-BP02 Collect compute-related metrics](perf02-bp02.md) 
+  [PERF03-BP03 Collect and record data store performance metrics](perf03-bp03.md) 
+  [PERF04-BP07 Optimize network configuration based on metrics](perf04-bp07.md) 

 **Related documents:** 
+  [Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 
+  [Strategic instrumentation](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/strategic-instrumentation.html) 
+  [Application performance monitoring (APM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) 
+  [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) 
+  [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html) 
+  [Generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) 
+  [Diagnose InvocationLatency increases using output tokens per second (OTPS)](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-otps.html) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [What is AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Troubleshooting database performance issues at scale](https://www.youtube.com/watch?v=2O08fPo3uYY) 
+  [AWS re:Invent 2025 - Implementing observability at scale: A blueprint for success](https://www.youtube.com/watch?v=GxZ2c4XsXOw) 
+  [AWS re:Invent 2025 - Elevate application and generative AI observability](https://www.youtube.com/watch?v=vxzq8GthOLs) 
+  [AWS re:Invent 2025 - AI-Native Era of Observability: How You Can Get Started Today](https://www.youtube.com/watch?v=y7fuAOIVEGw) 
+  [AIOps for AWS Observability Strategy](https://aws.amazon.com/video/watch/6b95b13df68/) 
+  [Amazon's Observability Best Practices Revealed](https://aws.amazon.com/video/watch/1a569f79ca0/) 

 **Related examples:** 
+  [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance) 
+  [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web) 
+  [Amazon CloudWatch generative AI observability sample](https://github.com/aws-samples/sample-amazon-cloudwatch-generative-ai-observability) 
+  [EKS investigation with AWS DevOps Agent](https://github.com/aws-samples/sample-aws-genai-ops-demos/blob/main/observability/eks-investigation-devops-agent/README.md) 
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 
+  [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) 