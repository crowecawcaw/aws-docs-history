

# Amazon ECS
<a name="deploy-container-insights-ECS"></a>

You can use one or more of the following options to collect metrics from Amazon ECS clusters:
+ Use the AWS Management Console or the AWS CLI to turn on Container Insights. It collects cluster-level, task-level, and service-level metrics.
+ Run the OpenTelemetry Collector as a sidecar in your tasks. It collects task-level and container-level metrics and sends them to CloudWatch over OTLP, where you query them with PromQL.
+ Deploy the CloudWatch agent as a daemon service. It collects instance-level metrics on clusters that run on Amazon EC2 instances.

**Topics**
+ [Setting up Container Insights on Amazon ECS](deploy-container-insights-ECS-cluster.md)
+ [Collecting Amazon ECS metrics with the OpenTelemetry Collector](deploy-container-insights-ECS-otel-collector.md)
+ [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](deploy-container-insights-ECS-instancelevel.md)
+ [Set up FireLens to send logs to CloudWatch Logs](deploy-container-insights-ECS-logs.md)