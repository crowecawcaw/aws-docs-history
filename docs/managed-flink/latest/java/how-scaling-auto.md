Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use automatic scaling in Managed Service for Apache Flink

Managed Service for Apache Flink elastically scales your application’s parallelism to accommodate the data
throughput of your source and your operator complexity for most scenarios. Automatic
scaling is enabled by default. Managed Service for Apache Flink monitors the resource (CPU) usage of your
application, and elastically scales your application's parallelism up or down
accordingly:

- Your application scales up (increases parallelism) if CloudWatch metric maximum
  `containerCPUUtilization` is larger than 75 percent or above for
  15 minutes. That means the `ScaleUp` action is initiated when there
  are 15 consecutive datapoints with 1 minute period equal to or over 75 percent.
  A `ScaleUp` action doubles the `CurrentParallelism` of
  your application. `ParallelismPerKPU` is not modified. As a
  consequence, the number of allocated KPUs also doubles.
- Your application scales down (decreases parallelism) when your CPU usage remains below 10
  percent for six hours. That means the `ScaleDown` action is initiated
  when there are 360 consecutive datapoints with 1 minute period less than 10
  percent. A `ScaleDown` action halves (rounded up) the parallelism of
  the application. `ParallelismPerKPU` is not modified, and the number
  of allocated KPUs also halves (rounded up).

###### Note

Max of `containerCPUUtilization` over 1 minute period can be referenced to find the
correlation with a datapoint used for Scaling action, but it’s not necessary to
reflect the exact moment when the action is initialized.

Managed Service for Apache Flink will
not reduce your application's `CurrentParallelism` value to less than your application's
`Parallelism` setting.

When the Managed Service for Apache Flink service is scaling your application, it will be in the `AUTOSCALING`
status. You can check your current application status using the
[DescribeApplication](../apiv2/API_DescribeApplication.md "../apiv2/API_DescribeApplication.md") or
[ListApplications](../apiv2/API_ListApplications.md "../apiv2/API_ListApplications.md") actions. While the service is scaling your application,
the only valid API action you can use is [StopApplication](../apiv2/API_ListApplications.md "../apiv2/API_ListApplications.md") with the `Force` parameter set to `true`.

You can use
the `AutoScalingEnabled` property (part of [`FlinkApplicationConfiguration`](../../../managed-service-for-apache-flink/latest/apiv2/API_FlinkApplicationConfiguration.md "../../../managed-service-for-apache-flink/latest/apiv2/API_FlinkApplicationConfiguration.md")
) to enable or disable auto scaling behavior. Your AWS account is charged for KPUs that Managed Service for Apache Flink provisions which is a function of your application's `parallelism`
and `parallelismPerKPU` settings. An activity
spike increases your Managed Service for Apache Flink costs.

For information about pricing, see [Amazon Managed Service for Apache Flink
pricing](https://aws.amazon.com/kinesis/data-analytics/pricing/ "https://aws.amazon.com/kinesis/data-analytics/pricing/").

Note the following about application scaling:

- Automatic scaling is enabled by default.
- Scaling doesn't apply to Studio notebooks. However, if you deploy a Studio notebook as an application with durable state, then scaling will apply to the deployed application.
- Your application has a default limit of 64 KPUs. For more information, see [Managed Service for Apache Flink and Studio notebook quota](limits.md "limits.md").
- When autoscaling updates application parallelism, the application experiences downtime. To avoid this downtime, do the following:
  - Disable automatic scaling
  - Configure your application's `parallelism` and `parallelismPerKPU` with
    the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action. For more information about
    setting your application's parallelism settings, see [Update your application's parallelism](how-scaling.md#how-scaling-howto "how-scaling.md#how-scaling-howto").
  - Periodically monitor your application's resource usage to verify that your application has the correct parallelism settings for its workload. For information about
    monitoring allocation resource usage, see [Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md "metrics-dimensions.md").

## Implement custom autoscaling

If you want finer grained control on autoscaling or use trigger metrics other than
`containerCPUUtilization`, you can use this example:

- [AutoScaling](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/AutoScaling "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/AutoScaling")

This examples illustrates how to scale your Managed Service for Apache Flink application using a
different CloudWatch metric from the Apache Flink application, including metrics from
Amazon MSK and Amazon Kinesis Data Streams, used as sources or sink.

For additional information, see [Enhanced monitoring and automatic scaling for Apache Flink](https://aws.amazon.com/blogs/big-data/enhanced-monitoring-and-automatic-scaling-for-apache-flink/ "https://aws.amazon.com/blogs/big-data/enhanced-monitoring-and-automatic-scaling-for-apache-flink/").

## Implement scheduled autoscaling

If your workload follows a predictable profile over time, you might prefer to
scale your Apache Flink application preemptively. This scales your application at a
scheduled time, as opposed to scaling reactively based on a metric. To set up
scaling up and down at fixed hours of the day, you can use this example:

- [ScheduledScaling](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/ScheduledScaling "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/infrastructure/ScheduledScaling")
