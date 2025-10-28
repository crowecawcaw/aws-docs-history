# Logs sent to CloudWatch Logs

###### Important

When you set up the log types in the following list to be sent to CloudWatch Logs, AWS
creates or changes the resource policies associated with the log group receiving
the logs, if needed. Continue reading this section to see the details.

This section applies when the types of logs listed in the table in the preceding
section are sent to CloudWatch Logs:

**User permissions**

To be able to set up sending any of these types of logs to CloudWatch Logs for the first
time, you must be logged into an account with the following permissions.

- `logs:CreateLogDelivery`
- `logs:PutResourcePolicy`
- `logs:DescribeResourcePolicies`
- `logs:DescribeLogGroups`

###### Note

When you specify the `logs:DescribeLogGroups`,
`logs:DescribeResourcePolicies`, or
`logs:PutResourcePolicy` permission, be sure to set the
ARN of its `Resource` line to use a `*` wildcard,
instead of specifying only a single log group name. For example,
`"Resource":
 "arn:aws:logs:us-east-1:111122223333:log-group:*"`
If any of these types of logs is already being sent to a log group in CloudWatch Logs, then
to set up the sending of another one of these types of logs to that same log group,
you only need the `logs:CreateLogDelivery` permission.

**Log group resource policy**

The log group where the logs are being sent must have a resource policy that
includes certain permissions. If the log group currently does not have a resource
policy, and the user setting up the logging has the
`logs:PutResourcePolicy`, `logs:DescribeResourcePolicies`,
and `logs:DescribeLogGroups` permissions for the log group, then AWS
automatically creates the following policy for it when you begin sending the logs to
CloudWatch Logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite20150319",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "delivery.logs.amazonaws.com"
 ]
 },
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`my-log-group`:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`0123456789`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`111122223333`:*"
 ]
 }
 }
 }
 ]
}`

```

If the log group does have a resource policy but that policy doesn't contain the
statement shown in the previous policy, and the user setting up the logging has the
`logs:PutResourcePolicy`, `logs:DescribeResourcePolicies`,
and `logs:DescribeLogGroups` permissions for the log group, that
statement is appended to the log group's resource policy.
