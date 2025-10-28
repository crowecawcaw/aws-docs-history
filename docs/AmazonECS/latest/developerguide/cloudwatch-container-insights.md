# Monitor Amazon ECS containers using Container Insights with

enhanced observability

Container Insights collects, aggregates, and summarizes metrics and logs from your containerized
applications and microservices. Container Insights with enhanced observability provides all the Container Insights metrics, plus additional
task and container metrics.

Container Insights discovers all the running containers in a cluster and collects performance data at
every layer of the performance stack. Operational data is collected as performance log
events. These are entries that use a structured JSON schema for high-cardinality data to be
ingested and stored at scale. From this data, CloudWatch creates higher-level aggregated metrics
at the cluster, service, and task level as CloudWatch metrics. The metrics include utilization for
resources such as CPU, memory, disk, and network. The metrics are available in CloudWatch
automatic dashboards.

The metrics only reflect the resources with running tasks during the specified time range.
For example, if you have a cluster with one service in it but that service has no tasks in a
`RUNNING` state, there will be no metrics sent to CloudWatch. If you have two
services and one of them has running tasks and the other doesn't, only the metrics for the
service with running tasks will be sent.

On December 2, 2024, AWS released Container Insights with enhanced observability for
Amazon ECS. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and
Fargates. After you configure Container Insights with enhanced observability on
Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster
level down to the container level in your environment and displays these critical
performance data in curated dashboards removing the heavy lifting in observability set-up.
For information about how to set up Container Insights with enhanced observability, see
[Container Insights with
enhanced observability](ecs-account-settings.md#container-insights-setting-enhanced "ecs-account-settings.md#container-insights-setting-enhanced").

We recommend that you use Container Insights with enhanced observability instead of
Container Insights because it provides detailed visibility in your container environment,
reducing the mean time to resolution. For more information, see [Amazon ECS Container Insights with enhanced observability metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.md") in the _Amazon CloudWatch User Guide_.

The events that you can view are the ones that Amazon ECS sends to Amazon EventBridge. For more
information, see [Amazon ECS events](ecs_cwe_events.md "ecs_cwe_events.md").

###### Important

Metrics collected by CloudWatch Container Insights are charged as custom metrics. For more information
about CloudWatch pricing, see [CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
