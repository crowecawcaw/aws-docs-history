# AWS Transit Gateway,Flow Logs records in Amazon Data Firehose

###### Topics

- [IAM roles for cross account delivery](#flow-logs-kinesis-iam "#flow-logs-kinesis-iam")
- [Create the source account role](flowlog-fh-create-source.md "flowlog-fh-create-source.md")
- [Create the destination account role](flowlog-fh-create-destination.md "flowlog-fh-create-destination.md")
- [Create a Flow Log that
  publishes to Firehose](flow-logs-kinesis-create.md "flow-logs-kinesis-create.md")
  Flow logs can publish flow log data directly to Firehose. You can choose to publish flow
  logs to the same account as the resource monitor or to a different account.

**Prerequisities**

When publishing to Firehose, flow log data is published to a Firehose delivery stream, in
plain text format. You must first have created a Firehose delivery stream. For the steps to
create a delivery stream, see [Creating an Amazon Data Firehose Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the _Amazon Data Firehose Developer Guide_.

**Pricing**

Standard ingestion and delivery charges apply. For more information, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"),
select **Logs** and find **Vended
Logs**.

## IAM roles for cross account delivery

When you publish to Kinesis Data Firehose, you can choose a delivery stream that's
in the same account as the resource to monitor (the source account), or in a
different account (the destination account). To enable cross account delivery of
flow logs to Firehose, you must create an IAM role in the source account and an IAM
role in the destination account.

###### Roles

- [Source account role](#flow-logs-kinesis-iam-role-source "#flow-logs-kinesis-iam-role-source")
- [Destination account role](#flow-logs-kinesis-iam-role-destination "#flow-logs-kinesis-iam-role-destination")

### Source account role

In the source account, create a role that grants the following permissions. In
this example, the name of the role is `mySourceRole`, but you can choose
a different name for this role. The last statement allows the role in the
destination account to assume this role. The condition statements ensure that this
role is passed only to the log delivery service, and only when monitoring the
specified resource. When you create your policy, specify the VPCs, network
interfaces, or subnets that you're monitoring with the condition key
`iam:AssociatedResourceARN`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/mySourceRole",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "delivery.logs.amazonaws.com"
 },
 "StringLike": {
 "iam:AssociatedResourceARN": [
 "arn:aws:ec2:us-east-1:source-account:transit-gateway/tgw-0fb8421e2da853bf"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:GetLogDelivery"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/AWSLogDeliveryFirehoseCrossAccountRole"
 }
 ]
}`

```

Ensure that this role has the following trust policy, which allows the log delivery service to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### Destination account role

In the destination account, create a role with a name that starts with
**AWSLogDeliveryFirehoseCrossAccountRole**. This role must
grant the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "firehose:TagDeliveryStream"
 ],
 "Resource": "*"
 }
 ]
}`

```

Ensure that this role has the following trust policy, which allows the role
that you created in the source account to assume this role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/mySourceRole"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
