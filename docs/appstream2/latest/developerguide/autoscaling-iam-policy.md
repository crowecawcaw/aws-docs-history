# Using IAM Policies to Manage Administrator Access to Application Auto Scaling

Automatic scaling for fleets is made possible by a combination of the AppStream 2.0,
Amazon CloudWatch, and Application Auto Scaling APIs. AppStream 2.0 fleets are created with AppStream 2.0, alarms are created
with CloudWatch, and scaling policies are created with Application Auto Scaling.

In addition to having the permissions defined in the [AmazonAppStreamFullAccess](managed-policies-required-to-access-appstream-resources.md "managed-policies-required-to-access-appstream-resources.md") policy,
the IAM user that accesses fleet scaling settings must have the required
permissions for the services that support dynamic scaling. IAM users must have
permissions to use the actions shown in the following example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "appstream:*",
 "application-autoscaling:*",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:DisableAlarmActions",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:EnableAlarmActions",
 "cloudwatch:ListMetrics",
 "cloudwatch:PutMetricAlarm",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "application-autoscaling.amazonaws.com"
 }
 }
 }
 ]
}`

```

You can also create your own IAM policies to set more specific permissions for calls
to the Application Auto Scaling API. For more information, see [Authentication
and Access Control](../../../autoscaling/application/userguide/auth-and-access-control.md "../../../autoscaling/application/userguide/auth-and-access-control.md") in the _Application Auto Scaling User Guide_.
