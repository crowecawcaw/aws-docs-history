# REL11-BP01 Monitor all components of the workload to detect

failures

Continually monitor the health of your workload so that you and your
automated systems are aware of failures or degradations as soon as
they occur. Monitor for key performance indicators (KPIs) based on
business value.

All recovery and healing mechanisms must start with the ability to
detect problems quickly. Technical failures should be detected first
so that they can be resolved. However, availability is based on the
ability of your workload to deliver business value, so key
performance indicators (KPIs) that measure this need to be a part of
your detection and remediation strategy.

**Desired outcome:** Essential components of a workload are monitored independently to
detect and alert on failures when and where they happen.

**Common anti-patterns:**

- No alarms have been configured, so outages occur without
  notification.
- Alarms exist, but at thresholds that don't provide adequate time
  to react.
- Metrics are not collected often enough to meet the recovery time
  objective (RTO).
- Only the customer facing interfaces of the workload are actively
  monitored.
- Only collecting technical metrics, no business function metrics.
- No metrics measuring the user experience of the workload.
- Too many monitors are created.

**Benefits of establishing this best
practice:** Having appropriate monitoring at all layers allows you to reduce
recovery time by reducing time to detection.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Identify all workloads that will be reviewed for monitoring. Once
you have identified all components of the workload that will need
to monitored, you will now need to determine the monitoring
interval. The monitoring interval will have a direct impact on how
fast recovery can be initiated based on the time it takes to
detect a failure. The mean time to detection (MTTD) is the amount
of time between a failure occurring and when repair operations
begin. The list of services should be extensive and complete.

Monitoring must cover all layers of the application stack
including application, platform, infrastructure, and network.

Your monitoring strategy should consider the impact of
_gray failures_. For more detail on gray
failures, see
[Gray failures](../../../whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.md "../../../whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.md") in the Advanced Multi-AZ Resilience Patterns whitepaper.

### Implementation steps

- Your monitoring interval is dependent on how quickly you
  must recover. Your recovery time is driven by the time it
  takes to recover, so you must determine the frequency of
  collection by accounting for this time and your recovery
  time objective (RTO).
- Configure detailed monitoring for components and managed
  services.
  - Determine if
    [detailed
    monitoring for EC2 instances](../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md") and
    [Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/as-instance-monitoring.md "../../../autoscaling/ec2/userguide/as-instance-monitoring.md") is necessary. Detailed monitoring
    provides one minute interval metrics, and default
    monitoring provides five minute interval metrics.
  - Determine if
    [enhanced
    monitoring](../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md "../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md") for RDS is necessary. Enhanced
    monitoring uses an agent on RDS instances to get useful
    information about different process or threads.
  - Determine the monitoring requirements of critical
    serverless components for
    [Lambda](../../../lambda/latest/dg/monitoring-metrics.md "../../../lambda/latest/dg/monitoring-metrics.md"),
    [API Gateway](../../../apigateway/latest/developerguide/monitoring_automated_manual.md "../../../apigateway/latest/developerguide/monitoring_automated_manual.md"),
    [Amazon EKS](../../../eks/latest/userguide/eks-observe.md "../../../eks/latest/userguide/eks-observe.md"),
    [Amazon ECS](https://catalog.workshops.aws/observability/en-US/aws-managed-oss/amp/ecs "https://catalog.workshops.aws/observability/en-US/aws-managed-oss/amp/ecs"),
    and all types of
    [load
    balancers](../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md "../../../elasticloadbalancing/latest/application/load-balancer-monitoring.md").
  - Determine the monitoring requirements of storage
    components for
    [Amazon S3](../../../AmazonS3/latest/userguide/monitoring-overview.md "../../../AmazonS3/latest/userguide/monitoring-overview.md"),
    [Amazon FSx](../../../fsx/latest/WindowsGuide/monitoring_overview.md "../../../fsx/latest/WindowsGuide/monitoring_overview.md"),
    [Amazon EFS](../../../efs/latest/ug/monitoring_overview.md "../../../efs/latest/ug/monitoring_overview.md"),
    and
    [Amazon EBS](../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md "../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md").

- Create
  [custom
  metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") to measure business key performance
  indicators (KPIs). Workloads implement key business
  functions, which should be used as KPIs that help identify
  when an indirect problem happens.
- Monitor the user experience for failures using user
  canaries.
  [Synthetic
  transaction testing](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") (also known as canary testing,
  but not to be confused with canary deployments) that can run
  and simulate customer behavior is among the most important
  testing processes. Run these tests constantly against your
  workload endpoints from diverse remote locations.
- Create
  [custom
  metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") that track the user's experience. If you can
  instrument the experience of the customer, you can determine
  when the consumer experience degrades.
- [Set
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") to detect when any part of your workload is
  not working properly and to indicate when to automatically
  scale resources. Alarms can be visually displayed on
  dashboards, send alerts through Amazon SNS or email, and
  work with Amazon EC2 Auto Scaling to scale workload resources up or
  down.
- Create
  [dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
  to visualize your metrics. Dashboards can be used to
  visually see trends, outliers, and other indicators of
  potential problems or to provide an indication of problems
  you may want to investigate.
- Create
  [distributed
  tracing monitoring](https://aws.amazon.com/xray/faqs/ "https://aws.amazon.com/xray/faqs/") for your services. With
  distributed monitoring, you can understand how your
  application and its underlying services are performing to
  identify and troubleshoot the root cause of performance
  issues and errors.
- Create monitoring systems (using
  [CloudWatch](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_xaxr_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_xaxr_dashboard.md")
  or
  [X-Ray](https://aws.amazon.com/xray/faqs/ "https://aws.amazon.com/xray/faqs/"))
  dashboards and data collection in a separate Region and
  account.
- Stay informed about service degradations with [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/ "https://aws.amazon.com/premiumsupport/technology/aws-health/"). [Create purpose-fit AWS Health event notifications](../../../health/latest/ug/user-notifications.md "../../../health/latest/ug/user-notifications.md") to e-mail and chat channels through [AWS User Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md") and integrate programmatically with [your monitoring and alerting tools through Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md").

## Resources

**Related best practices:**

- [Availability
  Definition](availability.md "availability.md")
- [REL11-BP06
  Send Notifications when events impact availability](rel_withstand_component_failures_notifications_sent_system.md "rel_withstand_component_failures_notifications_sent_system.md")

**Related documents:**

- [Amazon CloudWatch Synthetics enables you to create user
  canaries](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")
- [Enable
  or Disable Detailed Monitoring for Your Instance](../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md")
- [Enhanced
  Monitoring](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md")
- [Monitoring
  Your Amazon EC2 Auto Scaling Groups and Instances Using Amazon CloudWatch](../../../autoscaling/ec2/userguide/as-instance-monitoring.md "../../../autoscaling/ec2/userguide/as-instance-monitoring.md")
- [Publishing
  Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")
- [Using
  Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [Using
  CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
- [Using
  Cross Region Cross Account CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_xaxr_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_xaxr_dashboard.md")
- [Using
  Cross Region Cross Account X-Ray Tracing](https://aws.amazon.com/xray/faqs/ "https://aws.amazon.com/xray/faqs/")
- [Understanding
  availability](../../../whitepapers/latest/availability-and-beyond-improving-resilience/understanding-availability.md "../../../whitepapers/latest/availability-and-beyond-improving-resilience/understanding-availability.md")

**Related videos:**

- [Mitigating
  gray failures](../../../whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.md "../../../whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.md")

**Related examples:**

- [One
  Observability Workshop: Explore X-Ray](https://catalog.workshops.aws/observability/en-US/aws-native/xray/explore-xray "https://catalog.workshops.aws/observability/en-US/aws-native/xray/explore-xray")

**Related tools:**

- [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [CloudWatch
  X-Ray](../../../xray/latest/devguide/security-logging-monitoring.md "../../../xray/latest/devguide/security-logging-monitoring.md")
