

# Collecting Amazon ECS metrics with the OpenTelemetry Collector

You can use the OpenTelemetry Collector to collect task-level and container-level metrics from your Amazon ECS tasks. The collector sends them to CloudWatch over OpenTelemetry Protocol (OTLP), and you query them with PromQL. This works on AWS Fargate, Amazon EC2, and Amazon ECS Managed Instances.

The collector runs as a sidecar container in each task. Its `awsecscontainermetrics` receiver reads the [Amazon ECS task metadata endpoint version 4](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4.html) of the task it runs in. It publishes CPU, memory, network, and storage metrics for the task and for each container in it.

Metrics sent this way use OpenTelemetry metrics pricing. You pay per GB ingested, and there's no charge per metric or per label combination. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

**Note**  
This pipeline doesn't populate the Container Insights console pages for Amazon ECS, and existing metric alarms don't apply to these metrics. Use PromQL queries, dashboards, and alarms instead. For more information about the Container Insights console, see [Setting up Container Insights on Amazon ECS](deploy-container-insights-ECS-cluster.md).