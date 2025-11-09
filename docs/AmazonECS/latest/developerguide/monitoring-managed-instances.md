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

For detailed monitoring of the underlying infrastructure that supports your
Amazon ECS Managed Instances workloads, you can install the CloudWatch agent on your Amazon ECS Managed Instances. The CloudWatch agent
provides additional system-level metrics and logs that complement the container-level
monitoring provided by Container Insights.

The CloudWatch agent can collect:

- System-level metrics such as disk usage, memory utilization, and network statistics
- Custom application metrics
- Log files from your applications and system
- Performance counters and other system information

For information about how to install and configure the CloudWatch agent on your Amazon ECS Managed Instances, see [Installing the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the _CloudWatch User Guide_.

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
