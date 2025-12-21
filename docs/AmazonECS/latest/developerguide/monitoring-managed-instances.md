# Monitoring Amazon ECS Managed Instances

Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon ECS Managed Instances workloads. AWS provides several tools and services to help you monitor your containerized applications and infrastructure.

## Container Insights monitoring

CloudWatch Container Insights provides comprehensive monitoring for your containerized applications and microservices. Container Insights automatically collects, aggregates, and summarizes metrics and logs from your containerized applications and microservices running on Amazon ECS Managed Instances.

Container Insights collects metrics at the cluster, service, and task level, providing visibility into:

- CPU and memory utilization
- Network performance metrics
- Storage utilization
- Task and service performance

The metrics are available in CloudWatch dashboards and can be used to create alarms and automated responses to performance issues. Container Insights also provides enhanced monitoring capabilities that help you identify and troubleshoot issues quickly.

###### Note

Container Insights comes at an additional cost. For more information about pricing, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Instance monitoring

For monitoring the underlying infrastructure that supports your Amazon ECS Managed Instances workloads,
you can use Amazon EC2 metrics available through CloudWatch.

Amazon ECS Managed Instances come with two Amazon EBS volumes:

- Root volume used for the OS filesystem
- Data volume used by the applications

When Container Insights is enabled, Amazon ECS automatically publishes instance-level OS and data filesystem utilization metrics.

Available metrics for Amazon ECS Managed Instances include:

- Amazon EC2 metrics: CPU utilization, network performance, disk operations, and status checks. For more information, see
  [Monitor your instances using CloudWatch](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md")
- Amazon ECS metrics (when Container Insights is enabled): OS and data volume file system utilization. For more information, see
  [Amazon ECS Container Insights metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md")
- Amazon EBS metrics: IOPS, throughput, read and write latency. For more information, see [Amazon EBS CloudWatch metrics](../../../ebs/latest/userguide/using_cloudwatch_ebs.md "../../../ebs/latest/userguide/using_cloudwatch_ebs.md")

###### Note

The CloudWatch agent cannot be run as a daemon because daemons are not supported on Amazon ECS Managed Instances.
This means additional system-level metrics that require the CloudWatch agent running as a daemon are not available.

These metrics are automatically available without manual agent installation.

### Detailed monitoring for Amazon ECS Managed Instances

CloudWatch provides two categories of monitoring: _basic monitoring_
and _detailed monitoring_. By default, your managed instance is configured for
basic monitoring. You can optionally enable detailed monitoring to help you more quickly
identify and act on operational issues. You can turn on or off detailed monitoring when you create or update a Amazon ECS Managed Instances capacity provider.

Enabling detailed monitoring on a managed instance does not affect the monitoring of its
attached Amazon EBS volumes.

The following table highlights the differences between basic monitoring and detailed
monitoring for your managed instances.

| Monitoring type         | Description                                                                                                                                                                                                                                                                                                                    | Charges                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic monitoring**    | Status check metrics are available in 1-minute periods.<br>All other metrics are available in 5-minute periods.                                                                                                                                                                                                                | No charge.                                                                                                                                                                                                                                                                                                                                              |
| **Detailed monitoring** | All metrics, including status check metrics, are available in 1-minute periods.<br>To get this level of data, you must specifically enable it for the managed instance. For the<br>managed instances where you've enabled detailed monitoring, you can also get aggregated data<br>across groups of similar managed instances. | You are charged per metric that Amazon ECS Managed Instances sends to CloudWatch. You are not charged for<br>data storage. For more information, see **Paid tier**<br>and \*_Example 1<br>• EC2 Detailed Monitoring_<br>• on the<br>[CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). |

#### Required permissions

To enable detailed monitoring for a managed instance, your user must
have permission to use the `MonitorInstances`
API action. To turn off detailed monitoring for a managed instance, your
user must have permission to use the `UnmonitorInstances`
API action.
