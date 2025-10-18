# Customer managed policy examples

In this section, you can find example user policies that grant permissions for various
 CloudWatch actions. These policies work when you are using the CloudWatch API, AWS SDKs, or the
 AWS CLI.

###### Examples

* [Example 1: Allow user full access to
 CloudWatch](#full-access-example-cw "#full-access-example-cw")
* [Example 2: Allow read-only access to
 CloudWatch](#read-only-access-example-cw "#read-only-access-example-cw")
* [Example 3: Stop or terminate an Amazon EC2
 instance](#stop-terminate-example-cw "#stop-terminate-example-cw")

## Example 1: Allow user full access to
 CloudWatch


To grant a user full access to CloudWatch, you can use grant them the
 **CloudWatchFullAccess** managed policy instead of creating a
 customer-managed policy. The contents of the
 **CloudWatchFullAccess** are listed in [CloudWatchFullAccess](managed-policies-cloudwatch.md#managed-policies-cloudwatch-CloudWatchFullAccess "managed-policies-cloudwatch.md#managed-policies-cloudwatch-CloudWatchFullAccess").


## Example 2: Allow read-only access to
 CloudWatch


The following policy allows a user read-only access to CloudWatch and view Amazon EC2 Auto Scaling
 actions, CloudWatch metrics, CloudWatch Logs data, and alarm-related Amazon SNS data.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "autoscaling:Describe*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "logs:Get*",
 "logs:Describe*",
 "logs:StartQuery",
 "logs:StopQuery",
 "logs:TestMetricFilter",
 "logs:FilterLogEvents",
 "logs:StartLiveTail",
 "logs:StopLiveTail",
 "sns:Get*",
 "sns:List*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```





## Example 3: Stop or terminate an Amazon EC2
 instance


The following policy allows an CloudWatch alarm action to stop or terminate an EC2
 instance. In the sample below, the GetMetricData, ListMetrics, and DescribeAlarms
 actions are optional. It is recommended that you include these actions to ensure
 that you have correctly stopped or terminated the instance.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Action": [
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "ec2:DescribeInstanceStatus",
 "ec2:DescribeInstances",
 "ec2:StopInstances",
 "ec2:TerminateInstances"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```
