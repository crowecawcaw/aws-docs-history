

# REL06-BP01 Monitor all components for the workload (Generation)

 Collect telemetry from each tier so you can detect degradation early and confirm that the workload delivers its intended business outcomes. Without broad instrumentation, failures surface first as customer complaints. 

 **Desired outcome:** 
+  You collect metrics and logs from every tier of the workload, including front end, business logic, and storage. 
+  Your monitoring includes business-outcome metrics, such as orders processed per minute, alongside technical metrics. 
+  You monitor external endpoints independently of your own components so you can verify the customer experience even with no live traffic. 
+  Your critical signals have defined thresholds that invoke alarms and recovery workflows. 

 **Common anti-patterns:** 
+  Teams monitor only the external interfaces to a workload and stay blind to internal component health. 
+  Teams rely on the default metrics that AWS services emit and generate no workload-specific metrics. 
+  Teams track technical metrics only and ignore the business outcomes the workload supports. 
+  Teams depend on production traffic and simple health checks to judge workload state. 

 **Benefits of establishing this best practice:** 
+  You anticipate and resolve problems faster because you see the health of every component. 
+  You detect business-impacting issues sooner, because outcome metrics often move before technical metrics do. 
+  You catch endpoint failures before customers do through synthetic monitoring. 
+  You reduce mean time to detection, which shortens the path to recovery. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Aggregation, alarming, automated response, and analysis can only work with the signals you generate at this stage. You cannot alarm on a metric you never collected or investigate a failure in a component that produces no logs. 

 Not all metrics have the same diagnostic value. Technical metrics such as CPU utilization, network I/O, and disk I/O tell you how infrastructure behaves, but they often lag the signals that matter to the business. A metric tied to a business outcome, such as successful checkouts per minute, can reveal trouble while CPU and memory graphs still show as healthy. Combine both classes of signal. 

 External endpoints require separate monitoring because their health is independent of your internal implementation. A component can report healthy while the path a customer travels is broken by a DNS problem, a certificate expiry, or a misconfigured load balancer. *Synthetic transactions*, sometimes called user canaries, address this by periodically running the common tasks a real client performs. They verify the customer experience continually, even during quiet periods with no organic traffic. Keep these tasks short and lightweight so they do not add meaningful load to the workload they observe. Do not confuse user canaries with canary deployments, which are a release technique. 

 [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) accounts for seasonality and trend so that expected daily and weekly patterns do not generate false alarms. [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) creates the canaries that monitor endpoints and APIs. Combine canary results with [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) to pinpoint which paths experience errors, faults, or throttling. For the health of the AWS services your resources depend on, the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) gives a personalized view. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Turn on logging across all components:** Obtain monitoring data from every tier of the workload. Turn on service logs such as Amazon S3 server access logs and load balancer access logs, and permit your application to emit workload-specific data. Collect infrastructure metrics for compute, network, and disk from the services you run. See [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) for the services that emit metrics automatically. 

1.  **Review default metrics and find collection gaps:** Every service emits default metrics that help you understand the dependencies between components. Review them, then identify what they do not cover. Where a gap exists, add instrumentation to emit the missing data, including business-outcome metrics that reflect what the workload delivers. For guidance on calculating aggregate metrics and choosing dimensions, see [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md). 

1.  **Select the signals worth alarming on:** Evaluate the metrics for each service in your workload and choose the subset with the largest impact on reliability. Focusing on a small set of critical signals and their thresholds reduces alert noise and lowers the rate of false positives. 

1.  **Define alarms and their recovery paths:** For each critical signal, create an alarm and document the response that follows it. Use [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) to notify responders and to invoke automated recovery workflows that help you meet your recovery time objective. 

1.  **Add synthetic transactions for external endpoints:** Configure [synthetic canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) that follow the same routes and perform the same actions as a customer. They verify the experience continuously and surface endpoint problems before customers report them. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL06-BP02 Define and calculate metrics (Aggregation)](rel06-bp02.md) 
+  [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel06-bp07.md) 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 

 **Related documents:** 
+  [Getting started with your AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) 
+  [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) 
+  [Access logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) 
+  [Access logs for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html) 
+  [Sending Lambda function logs to CloudWatch Logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) 
+  [Logging requests with server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) 
+  [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) 
+  [Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) 
+  [Publish custom metrics (PutMetricData / EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Metrics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 
+  [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) 
+  [Collect metrics, logs, and traces using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) 
+  [Monitoring tools for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-automated-manual.html) 
+  [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 
+  [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html) 

 **Related examples:** 
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) 