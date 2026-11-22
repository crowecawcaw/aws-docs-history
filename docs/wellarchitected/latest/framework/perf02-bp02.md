

# PERF02-BP02 Collect compute-related metrics

 Compute metrics show how hard your resources work and where they stall. Collect them continuously to spot bottlenecks and idle capacity before they affect users or budgets. Right-sizing and scaling decisions depend on these metrics. 

 **Desired outcome:** 
+  You collect compute metrics continuously in a central system, covering both resource utilization and application behavior. 
+  Your metric set goes beyond service defaults to include the signals your workload actually depends on, such as memory use or queue depth. 
+  Your metrics carry retention policies that match your operational and cost goals. 
+  Your alarms notify the right teams when a metric crosses a threshold, so you respond before users are affected. 

 **Common anti-patterns:** 
+  Teams search log files by hand to reconstruct what happened instead of tracking metrics over time. 
+  Teams rely only on the default metrics their monitoring tool records and miss workload-specific signals. 
+  Teams look at metrics only when an incident is already underway. 
+  Teams collect metrics but set no alarms, so a threshold breach goes unnoticed until users report it. 
+  Teams keep every metric at full resolution forever, driving up storage cost without operational value. 

 **Benefits of establishing this best practice:** 
+  Performance issues surface early because trends are visible before they become incidents. 
+  Right-sizing and scaling decisions rest on measured behavior rather than assumptions. 
+  Application performance can be tied back to business requirements, confirming the workload meets its goals. 
+  Storage cost stays controlled because retention matches the value of each metric. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Collect two groups of metrics: resource and application. Resource metrics show how busy the infrastructure is: CPU utilization, memory utilization, disk I/O, and network throughput. Application metrics show how the workload serves its purpose: response time, request rate, error rate, and throughput. You need both groups, because a service can show low CPU while response times climb, or run at high CPU while users see no impact. 

 Default metrics are a starting point. Services publish a baseline set automatically, but some useful signals are not visible from outside the instance. Memory utilization and disk-space consumption require an agent that runs inside the guest operating system. Workload-specific signals such as processing-queue depth never appear in a generic metric set at all. 

 Retention trades storage cost against the long history you need to investigate rare events or reveal seasonal trends. Set retention per metric: keep detailed data for signals that drive capacity planning or long-term trending, and expire or aggregate the metrics you act on in real time. Set alarms on the metrics that require action, and pair static thresholds with anomaly detection to catch both predictable limits and unexpected deviations. 

 On AWS, [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) provides default compute metrics, custom metrics, dashboards, and alarms in one place. The [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) collects in-guest signals such as memory and disk that the hypervisor cannot see. For open standards and multi-source telemetry, use [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) and [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) to collect and store metrics from containerized and hybrid workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the metrics that matter for your workload:** List the resource utilization metrics and the application metrics that reflect how your workload performs, such as response time and throughput. Start from the service defaults, then add the signals your workload depends on. Reference the default metrics for your compute type: [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html), [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html), [Amazon EKS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html). 

1.  **Choose a monitoring and observability solution:** Select a solution that centralizes collection and supports the metric types you identified. Options include [AWS native observability](https://catalog.workshops.aws/observability/en-US/aws-native), [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/), and [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html). 

1.  **Define filters and aggregation:** Set the aggregation windows and dimensions that make each metric meaningful for your workload. Use [CloudWatch Logs metric filters](https://aws.amazon.com/blogs/mt/quantify-custom-application-metrics-with-amazon-cloudwatch-logs-and-metric-filters/) to derive metrics from log data, and apply consistent naming so metrics correlate across services. 

1.  **Set retention policies:** Configure retention per metric to match operational and cost goals, keeping detailed history only where you need it. Review the defaults for [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) and [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) before overriding them. 

1.  **Create alarms and notifications:** Define alarms on the thresholds that require action, and route notifications to the teams that own the affected resources. Add [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to catch deviations you did not set an explicit threshold for. 

1.  **Automate agent deployment:** Deploy metric and log agents through automation so coverage stays consistent as instances launch and retire. Use [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) or the [OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector) to enroll new resources without manual steps. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 

 **Related documents:** 
+  [Monitoring and observability on AWS](https://aws.amazon.com/cloudops/monitoring-and-observability/) 
+  [Best practices for implementing observability with AWS](https://aws.amazon.com/blogs/mt/best-practices-implementing-observability-with-aws/) 
+  [Amazon CloudWatch documentation](https://docs.aws.amazon.com/cloudwatch/) 
+  [Install the CloudWatch agent on EC2 instances and on-premises servers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) 
+  [Access CloudWatch Logs for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) 
+  [Use CloudWatch Logs with container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-automated-manual.html) 
+  [Publish custom metrics to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) 

 **Related examples:** 
+  [Amazon CloudWatch immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US/300-cloudwatch) 
+  [Amazon EKS workshop](https://www.eksworkshop.com/) 