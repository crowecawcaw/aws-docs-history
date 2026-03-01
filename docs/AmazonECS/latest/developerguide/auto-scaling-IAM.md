# IAM permissions required for Amazon ECS service auto scaling

Service Auto Scaling is made possible by a combination of the Amazon ECS, CloudWatch, and Application Auto Scaling
APIs. Services are created and updated with Amazon ECS, alarms are created with CloudWatch, and
scaling policies are created with Application Auto Scaling.

In addition to the standard IAM permissions for creating and updating services, the
following permissions are required to interact with Service Auto Scaling settings.

- `application-autoscaling:*`
- `ecs:DescribeServices`
- `ecs:UpdateService`
- `cloudwatch:DescribeAlarms`
- `cloudwatch:PutMetricAlarm`
- `cloudwatch:DeleteAlarms`
- `cloudwatch:DescribeAlarmHistory`
- `cloudwatch:DescribeAlarmsForMetric`
- `cloudwatch:GetMetricStatistics`
- `cloudwatch:ListMetrics`
- `cloudwatch:DisableAlarmActions`
- `cloudwatch:EnableAlarmActions`
- `iam:CreateServiceLinkedRole`
- `sns:CreateTopic`
- `sns:Subscribe`
- `sns:Get*`
- `sns:List*`
  The Application Auto Scaling service also needs permission to describe your Amazon ECS services and
  CloudWatch alarms, and permissions to modify your service's desired count on your behalf.
  The `sns:` permissions are for the notifications that CloudWatch sends to an
  Amazon SNS topic when a threshold has been exceeded. If you use automatic scaling for
  your Amazon ECS services, it creates a service-linked role named
  `AWSServiceRoleForApplicationAutoScaling_ECSService`. This
  service-linked role grants Application Auto Scaling permission to describe the alarms for your
  policies, to monitor the current running task count of the service, and to modify
  the desired count of the service. The original managed Amazon ECS role for Application Auto Scaling was
  `ecsAutoscaleRole`, but it is no longer required. The service-linked
  role is the default role for Application Auto Scaling. For more information, see [Service-linked roles for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md") in the
  _Application Auto Scaling User Guide_.

If you created your Amazon ECS container instance role before CloudWatch
metrics are available for Amazon ECS, you might need to add the
`ecs:StartTelemetrySession` permission. For more information, see
[Considerations](cloudwatch-metrics.md#enable_cloudwatch "cloudwatch-metrics.md#enable_cloudwatch").
