# Monitor Amazon ECS using CloudWatch

You can monitor your Amazon ECS resources using Amazon CloudWatch, which collects and processes raw data
from Amazon ECS into readable, near real-time metrics. These statistics are recorded for a period
of two weeks so that you can access historical information and gain a better perspective on
how your clusters or services are performing. Amazon ECS metric data is automatically sent to
CloudWatch in 1-minute periods. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

Amazon ECS provides free metrics for clusters and services. For an additional cost, you can
turn on Amazon ECS CloudWatch Container Insights for your cluster for per-task metrics, including CPU, memory, and
EBS filesystem utilization. For more information about Container Insights, see [Monitor Amazon ECS containers using Container Insights with
enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").

## Considerations

The following should be considered when using Amazon ECS CloudWatch metrics.

- Any Amazon ECS service hosted on Fargate has CloudWatch CPU and memory
  utilization metrics automatically, so you don't need to take any manual
  steps.
- For any Amazon ECS task or service hosted on Amazon EC2 instances, the Amazon EC2 instance
  requires version `1.4.0` or later (Linux) or `1.0.0` or
  later (Windows) of the container agent for CloudWatch metrics to be generated.
  However, we recommend using the latest container agent version. For information
  about checking your agent version and updating to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
- The minimum Docker version for reliable CloudWatch metrics is Docker version
  `20.10.13` and newer.
- Your Amazon EC2 instances also require the `ecs:StartTelemetrySession`
  permission on the IAM role that you launch your Amazon EC2 instances with. If you
  created your Amazon ECS container instance IAM role before CloudWatch metrics were
  available for Amazon ECS, you might need to add this permission. For information
  about the container instance IAM role and attaching the
  managed IAM policy for container instances, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
- You can disable CloudWatch metrics collection on your Amazon EC2 instances by setting
  `ECS_DISABLE_METRICS=true` in your Amazon ECS container agent
  configuration. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

## Recommended metrics

Amazon ECS provides free CloudWatch metrics you can use to monitor your resources. The CPU and
memory reservation and the CPU, memory, and EBS filesystem utilization across your
cluster as a whole, and the CPU, memory, and EBS filesystem utilization on the services
in your clusters can be measured using these metrics. For your GPU workloads, you can
measure your GPU reservation across your cluster.

The infrastructure your Amazon ECS tasks are hosted on in your clusters determines which
metrics are available. For tasks hosted on Fargate infrastructure, Amazon ECS
provides CPU, memory, and EBS filesystem utilization metrics to assist in
the monitoring of your services. For tasks hosted on EC2 instances, Amazon ECS
provides CPU, memory, and GPU reservation metrics and CPU and memory utilization metrics
at the cluster and service level. You need to monitor the Amazon EC2 instances that make your
underlying infrastructure separately. For more information about monitoring your Amazon EC2
instances, see [Monitoring Amazon EC2](../../../AWSEC2/latest/UserGuide/monitoring_ec2.md "../../../AWSEC2/latest/UserGuide/monitoring_ec2.md") in the
_Amazon EC2 User Guide_.

For information about the recommended alarms to use with Amazon ECS, see one of the
following in the _Amazon CloudWatch Logs User Guide_:

- [Amazon ECS](../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#ECS "../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#ECS")
- [Amazon ECS with Container Insights](../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#ECS-ContainerInsights "../../../AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.md#ECS-ContainerInsights")
