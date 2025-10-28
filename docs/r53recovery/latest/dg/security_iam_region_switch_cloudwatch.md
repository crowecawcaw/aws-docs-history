# CloudWatch alarms for application health permissions

The following is a sample policy to attach to access CloudWatch alarms for application health, which are used to help
determine actual recovery time.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": [
 "arn:aws:cloudwatch:us-east-1:123456789012:alarm:app-health-primary",
 "arn:aws:cloudwatch:us-west-2:123456789012:alarm:app-health-secondary"
 ]
 }
 ]
}`

```
