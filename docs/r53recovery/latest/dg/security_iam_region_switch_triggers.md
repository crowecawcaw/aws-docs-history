

# Plan execution trigger permissions

 If your plan has triggers, Region switch uses the plan's execution role to read the CloudWatch alarms that the triggers use and to start the plan execution. The execution role needs the following permissions: 
+ `cloudwatch:DescribeAlarms` and `cloudwatch:DescribeAlarmHistory` on `arn:aws:cloudwatch:{{region}}:{{account-id}}:alarm:*` for each Region that has trigger alarms.
+ `arc-region-switch:StartPlanExecution` on the plan.

 The following is a sample policy to attach to the plan's execution role if you configure triggers. 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:DescribeAlarms",
        "cloudwatch:DescribeAlarmHistory"
      ],
      "Resource": [
        "arn:aws:cloudwatch:us-east-1:111122223333:alarm:*",
        "arn:aws:cloudwatch:us-west-2:111122223333:alarm:*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "arc-region-switch:StartPlanExecution",
      "Resource": "arn:aws:arc-region-switch::111122223333:plan/example-plan:abcde1"
    }
  ]
}
```

 The alarm resources must use a wildcard, even for metric alarms, because Region switch requests composite alarm information, and CloudWatch requires a wildcard resource to return it. For more information, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html#cw-permissions-table) in the *Amazon CloudWatch User Guide*. 