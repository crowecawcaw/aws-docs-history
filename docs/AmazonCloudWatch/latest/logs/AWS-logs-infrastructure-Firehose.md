# Logs sent to Firehose

This section applies when the types of logs listed in the table in the preceding
section are sent to Firehose:

**User permissions**

To be able to set up sending any of these types of logs to Firehose for the first
time, you must be logged into an account with the following permissions.

- `logs:CreateLogDelivery`
- `firehose:TagDeliveryStream`
- `iam:CreateServiceLinkedRole`
  If any of these types of logs is already being sent to Firehose, then to set up the
  sending of another one of these types of logs to Firehose you need to have only the
  `logs:CreateLogDelivery` and `firehose:TagDeliveryStream`
  permissions.

**IAM roles used for permissions**

Because Firehose does not use resource policies, AWS uses IAM roles when setting
up these logs to be sent to Firehose. AWS creates a service-linked role named
**AWSServiceRoleForLogDelivery**. This
service-linked role includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:ListTagsForDeliveryStream"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/LogDeliveryEnabled": "true"
 }
 },
 "Effect": "Allow"
 }
 ]
}`

```

This service-linked role grants permission for all Firehose delivery streams that
have the `LogDeliveryEnabled` tag set to `true`. AWS gives
this tag to the destination delivery stream when you set up the logging.

This service-linked role also has a trust policy that allows the
`delivery.logs.amazonaws.com` service principal to assume the needed
service-linked role. That trust policy is as follows:

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
