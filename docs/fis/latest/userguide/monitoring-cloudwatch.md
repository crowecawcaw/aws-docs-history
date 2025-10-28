# Monitor AWS FIS usage metrics using Amazon CloudWatch

You can use Amazon CloudWatch to monitor the impact of AWS FIS experiments on targets. You
can also monitor your AWS FIS usage.

For more information about viewing the state of an experiment, see [View your experiments](view-experiment-progress.md "view-experiment-progress.md").

## Monitor AWS FIS experiments

As you plan your AWS FIS experiments, identify the CloudWatch metrics that you can
use to identify the baseline or "steady state" for the target resource types
for the experiment. After you start an experiment, you can monitor those CloudWatch
metrics for the targets selected through the experiment template.

For more information about the available CloudWatch metrics for a target resource
type supported by AWS FIS, see the following:

- [Monitor your instances using CloudWatch](../../../AWSEC2/latest/UserGuide/using-cloudwatch.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch.md")
- [Amazon ECS CloudWatch metrics](../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md "../../../AmazonECS/latest/developerguide/cloudwatch-metrics.md")
- [Monitoring Amazon RDS metrics using CloudWatch](../../../AmazonRDS/latest/UserGuide/monitoring-cloudwatch.md "../../../AmazonRDS/latest/UserGuide/monitoring-cloudwatch.md")
- [Monitoring Run Command metrics using CloudWatch](../../../systems-manager/latest/userguide/monitoring-cloudwatch-metrics.md "../../../systems-manager/latest/userguide/monitoring-cloudwatch-metrics.md")

## AWS FIS usage metrics

You can use CloudWatch usage metrics to provide visibility into your account's usage of resources.
Use these metrics to visualize your current service usage on CloudWatch graphs and dashboards.

AWS FIS usage metrics correspond to AWS service quotas. You can configure alarms that alert
you when your usage approaches a service quota. For more information about CloudWatch alarms, see
the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS FIS publishes the following metric in the **AWS/Usage** namespace.

| Metric          | Description                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `ResourceCount` | The total number of the specified resource running on your account. The resource is defined by the dimensions associated with the metric.                     | The following dimensions are used to refine the usage metrics that are published by AWS FIS. |
| Dimension       | Description                                                                                                                                                   |
| ---             | ---                                                                                                                                                           |
| `Service`       | The name of the AWS service containing the resource. For AWS FIS usage metrics, the value for this dimension is `FIS`.                                        |
| `Type`          | The type of entity that is being reported. Currently, the only valid value for AWS FIS usage metrics is `Resource`.                                           |
| `Resource`      | The type of resource that is running. The possible values are `ExperimentTemplates` for experiment templates, and `ActiveExperiments` for active experiments. |
| `Class`         | This dimension is reserved for future use.                                                                                                                    |
