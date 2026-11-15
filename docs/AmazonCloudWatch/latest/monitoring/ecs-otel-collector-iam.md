

# Step 1: Grant the task role permission to publish metrics
<a name="ecs-otel-collector-iam"></a>

The collector signs requests to CloudWatch with the credentials of the task's IAM role (`taskRoleArn`), not the task execution role. Add the following policy to the task role.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*"
    }
  ]
}
```

`cloudwatch:PutMetricData` doesn't support resource-level permissions, so the policy specifies `"*"` as the resource.

The task execution role still needs its usual permissions to pull the collector image and to write the collector's logs, for example `AmazonECSTaskExecutionRolePolicy`.