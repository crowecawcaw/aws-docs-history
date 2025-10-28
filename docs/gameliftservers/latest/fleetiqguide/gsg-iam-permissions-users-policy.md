# Reference: Amazon GameLift Servers FleetIQ_policy

The following is an example of the Amazon GameLift Servers FleetIQ_policy for your reference:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition":
 {
 "StringEquals":
 {
 "iam:PassedToService": "gamelift.amazonaws.com"
 }
 }
 },
 {
 "Action":
 [
 "iam:CreateServiceLinkedRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:*:iam::*:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
 },
 {
 "Action":
 [
 "autoscaling:CreateAutoScalingGroup",
 "autoscaling:CreateOrUpdateTags",
 "autoscaling:DescribeAutoScalingGroups",
 "autoscaling:ExitStandby",
 "autoscaling:PutLifecycleHook",
 "autoscaling:PutScalingPolicy",
 "autoscaling:ResumeProcesses",
 "autoscaling:SetInstanceProtection",
 "autoscaling:UpdateAutoScalingGroup",
 "autoscaling:DeleteAutoScalingGroup"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action":
 [
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSubnets",
 "ec2:RunInstances",
 "ec2:CreateTags"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action":
 [
 "events:PutRule",
 "events:PutTargets"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```
