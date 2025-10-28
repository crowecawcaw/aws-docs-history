# AWS Transit Gateway Flow Logs records in Amazon CloudWatch Logs

Flow logs can publish flow log data directly to Amazon CloudWatch.

When published to CloudWatch Logs, the flow log data is published to a log group, and each transit gateway
has a unique log stream in the log group. Log streams contain flow log records. You can
create multiple flow logs that publish data to the same log group. If the same transit gateway is
present in one or more flow logs in the same log group, it has one combined log stream.
If you've specified that one flow log should capture rejected traffic, and the other
flow log should capture accepted traffic, then the combined log stream captures all
traffic.

Data ingestion and archival charges for vended logs apply when you publish flow logs
to CloudWatch Logs. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

In CloudWatch Logs, the **timestamp** field corresponds to the start time
that's captured in the flow log record. The **ingestionTime** field
provides the date and time when the flow log record was received by CloudWatch Logs. The timestamp
is later than the end time that's captured in the flow log
record.

For more information about CloudWatch Logs, see [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL") in the _Amazon CloudWatch Logs User
Guide_.

###### Contents

- [IAM roles for publishing flow logs to
  CloudWatch Logs](#flow-logs-iam "#flow-logs-iam")
- [Permissions for IAM users to pass a
  role](#flow-logs-iam-user "#flow-logs-iam-user")
- [Create a Flow Log that publishes
  to CloudWatch Logs](flow-logs-cwl-create-flow-log.md "flow-logs-cwl-create-flow-log.md")
- [View Flow Logs records](view-flow-log-records.md "view-flow-log-records.md")
- [Process Flow Log records](process-records-cwl.md "process-records-cwl.md")

## IAM roles for publishing flow logs to

CloudWatch Logs

The IAM role that's associated with your flow log must have sufficient
permissions to publish flow logs to the specified log group in CloudWatch Logs. The IAM role
must belong to your AWS account.

The IAM policy that's attached to your IAM role must include at least the
following permissions.

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
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": "*"
 }
 ]
}`

```

Also ensure that your role has a trust relationship that allows the flow logs
service to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "vpc-flow-logs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

We recommend that you use the `aws:SourceAccount` and
`aws:SourceArn` condition keys to protect yourself against [the confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").
For example, you could add the following condition block to the previous trust
policy. The source account is the owner of the flow log and the source ARN is the
flow log ARN. If you don't know the flow log ID, you can replace that portion of the
ARN with a wildcard (\*) and then update the policy after you create the flow
log.

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account_id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:ec2:`region`:`account_id`:vpc-flow-log/`flow-log-id`"
    }
}
```

## Permissions for IAM users to pass a

role

Users must also have permissions to use the `iam:PassRole` action for
the IAM role that's associated with the flow log.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`flow-log-role-name`"
 }
 ]
}`

```
