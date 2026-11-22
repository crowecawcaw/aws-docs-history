

# REL06-BP02 Define and calculate metrics (Aggregation)

 Raw telemetry from individual components rarely answers the questions that matter during an incident. Aggregation turns scattered logs and metrics into a coherent view of how the workload behaves. When you calculate metrics that span components and enrich them with context, you can detect anomalies, correlate failures, and find the cause of a problem faster. 

 **Desired outcome:** 
+  You collect logs from your workload components and service dependencies and publish them to a central location for access and processing. 
+  Your logs carry high-fidelity timestamps and processing context, such as a trace identifier, user or account identifier, and remote IP address. 
+  You calculate aggregate metrics from your logs that represent workload behavior at a high level. 
+  You can query aggregated logs to gain deep insights and identify actual and potential problems. 

 **Common anti-patterns:** 
+  Teams collect no logs or metrics from the compute their workloads run on or the cloud services they use. 
+  Teams overlook logs and metrics tied to business key performance indicators. 
+  Teams analyze telemetry in isolation, without aggregation or correlation across components. 
+  Teams expire metrics and logs too quickly, which prevents trend analysis and recurring-issue identification. 

 **Benefits of establishing this best practice:** 
+  You detect more anomalies and correlate events and metrics across components. 
+  You gain insights from log detail that metrics alone do not capture. 
+  You determine causes of failure more quickly by querying logs at scale. 
+  You reveal behavioral patterns that would stay hidden in per-component data. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Observability draws from every component, the cloud services those components depend on, and well-structured logs. Metrics tell you that a value crossed a line, and logs tell you what happened and in what context. Aggregation combines these resources into signals about the whole workload. 

 Logs often carry detail that no metric exposes. A web server typically records each request with a timestamp, processing latency, user ID, remote IP address, path, and query string. You can use log detail to compute metrics after the fact, even ones you didn't emit directly, and reconstruct how each request was handled. Collect logs even from components that emit metrics. 

 Adding *dimensions* to telemetry lets you explore behavior along axes that expose correlated problems. Useful dimensions include Availability Zone, instance ID, and container task or Pod ID. With them, you can see that errors cluster in a single Availability Zone, or that latency spikes track one deployment. Without them, an aggregate metric averages the problem away. A dashboard shows a healthy mean while a subset of requests fails consistently. 

 Historical logs reveal long-term usage patterns, regressions, and performance changes. Once deleted, they can never be analyzed again. But log value diminishes with age, and storage costs money. Choose a retention policy that balances analytical value against storage cost and meets legal or contractual requirements. Prepare and save the queries you'll need during an incident to speed up investigation start times. 

 An agent such as the [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) collects logs from Amazon EC2 instances and publishes them to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html). Managed services such as AWS Lambda and Amazon ECS publish logs automatically. To calculate aggregate metrics, [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) derives custom metrics from application logs, [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) queries metrics at scale, and Container and Lambda Insights summarize telemetry for those runtimes. For petabyte-scale queries across many sources, [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-aws-service-logs.html) queries logs directly. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose your observability mechanisms:** Decide how you will collect, store, analyze, and display telemetry data across the workload. Confirm the choice covers both metric sources and log sources, including managed services that emit logs on your behalf. 

1.  **Install and configure collectors:** Deploy metric and log collectors on the appropriate components, such as Amazon EC2 instances and sidecar containers. Configure collectors to restart automatically if they stop, and turn on disk or memory buffering so that temporary publication failures do not affect applications or lose data. 

1.  **Turn on logging for AWS service dependencies:** Turn on logging for the AWS services your workload uses, such as [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html), Amazon S3, Elastic Load Balancing, and Amazon API Gateway. Forward those logs to your central storage location where needed. 

1.  **Enrich telemetry with dimensions:** Add [dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) such as Availability Zone, instance ID, and task or Pod ID so you can observe behavior at a finer grain and detect correlated failures. 

1.  **Define and calculate operational metrics:** Identify the metrics that reflect workload behavior, including business KPI metrics and aggregate calculations such as sums, rates, percentiles, and histograms. Calculate them with your log analyzer, scan for anomalous patterns with [CloudWatch Logs anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html), and place the results on dashboards. 

1.  **Prepare queries and set retention:** Write and save the queries you will need to analyze components, requests, and transactions during an incident. Define a log retention policy that balances analytical value against cost, and delete logs when they exceed the policy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP03 Send notifications with real-time processing and alarming](rel06-bp03.md) 
+  [REL06-BP05 Analyze logs](rel06-bp05.md) 
+  [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel06-bp07.md) 

 **Related documents:** 
+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) 
+  [What is Amazon Managed Service for Prometheus?](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) 
+  [What is Amazon Managed Grafana?](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) 
+  [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) 
+  [Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html) 
+  [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) 
+  [Query your CloudWatch metrics with CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) 
+  [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) 
+  [Sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) 
+  [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) 
+  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/) 
+  [Query AWS service logs](https://docs.aws.amazon.com/athena/latest/ug/querying-aws-service-logs.html) 
+  [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html)) 

 **Related examples:** 
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/) 

 **Related tools:** 
+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) 