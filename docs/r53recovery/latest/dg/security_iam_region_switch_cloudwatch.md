

# CloudWatch alarms for application health permissions

 The following is a sample policy to attach to access CloudWatch alarms for application health, which are used to help determine actual recovery time. 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:DescribeAlarmHistory",
        "cloudwatch:DescribeAlarms"
      ],
      "Resource": [
        "arn:aws:cloudwatch:us-east-1:123456789012:alarm:*",
        "arn:aws:cloudwatch:us-west-2:123456789012:alarm:*"
      ]
    }
  ]
}
```

 The alarm resources must use a wildcard, even for metric alarms, because Region switch requests composite alarm information, and CloudWatch requires a wildcard resource to return it. For more information, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html#cw-permissions-table) in the *Amazon CloudWatch User Guide*. 