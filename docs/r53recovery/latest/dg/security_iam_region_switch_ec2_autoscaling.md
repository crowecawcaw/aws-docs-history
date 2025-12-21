# EC2 Auto Scaling execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for EC2 Auto Scaling groups.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "autoscaling:DescribeAutoScalingGroups"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "autoscaling:UpdateAutoScalingGroup"
 ],
 "Resource": [
 "arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:123d456e-123e-1111-abcd-EXAMPLE22222:autoScalingGroupName/app-asg-primary",
 "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1234a321-123e-1234-aabb-EXAMPLE33333:autoScalingGroupName/app-asg-secondary"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": "*"
 }
 ]
}`

```
