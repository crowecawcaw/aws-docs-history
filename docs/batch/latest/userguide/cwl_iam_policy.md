# Tutorial: Add a CloudWatch Logs IAM policy

Before your jobs can send log data and detailed metrics to CloudWatch Logs, you must create an IAM
policy that uses the CloudWatch Logs APIs. After you create the IAM policy, attach it to the
`ecsInstanceRole` role.

###### Note

If the `ECS-CloudWatchLogs` policy isn't attached to the
`ecsInstanceRole` role, basic metrics can still be sent to CloudWatch Logs. However, the
basic metrics don't include log data or detailed metrics such as free disk space.

AWS Batch compute environments use Amazon EC2 resources. When you create a compute environment
using the AWS Batch first-run wizard, AWS Batch creates the `ecsInstanceRole` role and
configures the environment with it.

If you aren't using the first-run wizard, you can specify the `ecsInstanceRole`
role when you create a compute environment in the AWS Command Line Interface or AWS Batch API. For more
information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md") or [AWS Batch API
Reference](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md").

###### To create the `ECS-CloudWatchLogs` IAM policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. Choose **JSON**, then enter the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:*"
 ]
 }
 ]
}`

```

5. Choose **Next: Tags**.
6. (Optional) For **Add tags**, choose **Add tag** to
   add a tag to the policy.
7. Choose **Next: Review**.
8. On the **Review policy** page, for **Name**, enter
   `ECS-CloudWatchLogs`, and then enter an optional
   **Description**.
9. Choose **Create policy**.

###### To attach the `ECS-CloudWatchLogs` policy to `ecsInstanceRole`

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose `ecsInstanceRole`. If the role doesn't exist, follow the procedures
   in [Amazon ECS instance role](instance_IAM_role.md "instance_IAM_role.md") to create the
   role.
4. Choose **Add Permissions**, then choose **Attach
   policies**.
5. Choose the **ECS-CloudWatchLogs** policy and then choose
   **Attach policy**.
