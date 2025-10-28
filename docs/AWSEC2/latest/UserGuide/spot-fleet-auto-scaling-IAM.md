# IAM permissions required for Spot Fleet

automatic scaling

Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2,
Amazon CloudWatch, and Application Auto Scaling APIs. Spot Fleet requests are created with Amazon EC2, alarms are
created with CloudWatch, and scaling policies are created with Application Auto Scaling. In addition to
the [IAM permissions required for using
Spot Fleet](spot-fleet-prerequisites.md#spot-fleet-iam-users "spot-fleet-prerequisites.md#spot-fleet-iam-users") and Amazon EC2, the user that accesses the fleet scaling settings must
have the appropriate permissions for the services that support automatic
scaling.

To use automatic scaling for Spot Fleet, users must have permissions to use the actions
shown in the following example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:*",
 "ec2:DescribeSpotFleetRequests",
 "ec2:ModifySpotFleetRequest",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:DisableAlarmActions",
 "cloudwatch:EnableAlarmActions",
 "iam:CreateServiceLinkedRole",
 "sns:CreateTopic",
 "sns:Subscribe",
 "sns:Get*",
 "sns:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can also create your own IAM policies that allow more fine-grained
permissions for calls to the Application Auto Scaling API. For more information, see [Identity
and Access Management for Application Auto Scaling](../../../autoscaling/application/userguide/auth-and-access-control.md "../../../autoscaling/application/userguide/auth-and-access-control.md") in the _Application Auto Scaling User
Guide_.

The Application Auto Scaling service also needs permission to describe your Spot Fleet and CloudWatch alarms,
and permissions to modify your Spot Fleet target capacity on your behalf. If you enable
automatic scaling for your Spot Fleet, it creates a service-linked role named
`AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`. This
service-linked role grants Application Auto Scaling permission to describe the alarms for your
policies, to monitor the current capacity of the fleet, and to modify the capacity
of the fleet. The original managed Spot Fleet role for Application Auto Scaling was
`aws-ec2-spot-fleet-autoscale-role`, but it is no longer required.
The service-linked role is the default role for Application Auto Scaling. For more information, see
[Service-linked roles for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md "../../../autoscaling/application/userguide/application-auto-scaling-service-linked-roles.md") in the _Application Auto Scaling User
Guide_.
