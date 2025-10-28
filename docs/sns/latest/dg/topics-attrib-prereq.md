# Prerequisites for delivery status logging

This topic outlines the necessary IAM permissions for enabling Amazon SNS to write
delivery logs to CloudWatch and explains the default log group naming convention. This ensures
you have the correct setup and access to monitor and analyze message delivery logs in
CloudWatch logs.

**Required IAM permissions**

The IAM role attached for delivery status logging must include the following
permissions to enable Amazon SNS to write to CloudWatch Logs. You can use an existing role with these
permissions or create a new role during setup.

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
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:*"
 }
 ]
}`

```

**Log group naming convention**

By default, Amazon SNS creates CloudWatch log groups for delivery status logs using the following
naming convention. Log streams within this group correspond to the endpoint protocols
(for example, Lambda, Amazon SQS). Ensure you have permissions to view these logs in the CloudWatch Logs
console.

```
sns/<region>/<account-id>/<topic-name>
```
