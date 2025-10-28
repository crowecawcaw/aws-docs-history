# Amazon ECS service scaling execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon ECS service scaling.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:DescribeServices",
 "ecs:UpdateService"
 ],
 "Resource": [
 "arn:aws:ecs:us-east-1:123456789012:service/app-cluster-primary/app-service",
 "arn:aws:ecs:us-west-2:123456789012:service/app-cluster-secondary/app-service"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecs:DescribeClusters"
 ],
 "Resource": [
 "arn:aws:ecs:us-east-1:123456789012:cluster/app-cluster-primary",
 "arn:aws:ecs:us-west-2:123456789012:cluster/app-cluster-secondary"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecs:ListServices"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:DescribeScalableTargets",
 "application-autoscaling:RegisterScalableTarget"
 ],
 "Resource": "*"
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
