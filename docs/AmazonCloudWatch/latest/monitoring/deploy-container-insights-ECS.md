

# Container Insights for Amazon ECS

Use CloudWatch Container Insights to collect, aggregate, and summarize metrics and logs from your Amazon ECS clusters, including clusters on AWS Fargate. Container Insights collects data as performance log events in [embedded metric format](CloudWatch_Embedded_Metric_Format.md), and creates aggregated CloudWatch metrics at the cluster, service, task, and container level from them. When you turn on Container Insights, it creates the log group for the performance log events. You can set CloudWatch alarms on the metrics that it collects, and use CloudWatch Logs Insights to analyze the raw performance log events. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) on the AWS website.

To monitor the applications that run in your tasks, see [Enable your applications on Amazon ECS](CloudWatch-Application-Signals-Enable-ECSMain.md).

You can use one or more of the following options to collect metrics from Amazon ECS clusters:
+ Use the AWS Management Console or the AWS CLI to turn on Container Insights. It collects cluster-level, task-level, and service-level metrics.
+ Run the OpenTelemetry Collector as a sidecar in your tasks. It collects task-level and container-level metrics and sends them to CloudWatch over OTLP, where you query them with PromQL.
+ Deploy the CloudWatch agent as a daemon service. It collects instance-level metrics on clusters that run on Amazon EC2 instances.

**Topics**
+ [Setting up Container Insights on Amazon ECS](deploy-container-insights-ECS-cluster.md)
+ [Collecting Amazon ECS metrics with the OpenTelemetry Collector](deploy-container-insights-ECS-otel-collector.md)
+ [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](deploy-container-insights-ECS-instancelevel.md)
+ [Set up FireLens to send logs to CloudWatch Logs](deploy-container-insights-ECS-logs.md)
+ [Amazon ECS Container Insights with enhanced observability metrics](Container-Insights-enhanced-observability-metrics-ECS.md)
+ [Amazon ECS Container Insights metrics](Container-Insights-metrics-ECS.md)
+ [Container Insights performance log events for Amazon ECS](Container-Insights-reference-performance-logs-ECS.md)
+ [Set up and configure Prometheus metrics collection on Amazon ECS clusters](ContainerInsights-Prometheus-Setup-ECS.md)
+ [Viewing Amazon ECS lifecycle events within Container Insights](container-insights-ECS-lifecycle-events.md)