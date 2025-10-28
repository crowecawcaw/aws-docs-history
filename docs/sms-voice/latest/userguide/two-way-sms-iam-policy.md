# IAM policies for Amazon SNS topics

If you want AWS End User Messaging SMS to use an existing IAM role or if you create a new role, attach the
following policies to that role so that AWS End User Messaging SMS can assume it. For information about how to
modify the trust relationship of a role, see [Modifying a
Role](../../../IAM/latest/UserGuide/id_roles_manage.md "../../../IAM/latest/UserGuide/id_roles_manage.md") in the [_IAM user guide_](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

The following is the **trust policy** for the IAM role. In
the following IAM policy, make the following changes:

- Replace `accountId` with the unique ID for your AWS
  account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SMSVoice",
 "Effect": "Allow",
 "Principal": {
 "Service": "sms-voice.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`accountId`"
 }
 }
 }
 ]
}`

```

The following is the **permission policy** for the IAM
role. The `SMSVoiceAllowSNSPublish` Sid is a permission policy to allow for
publishing to Amazon SNS topics and the `SMSVoiceAllowEncryptedSNSTopics` Sid is an
option for encrypted Amazon SNS topics.

In the following IAM permission policy, make the following changes:

- Replace `partition` with the AWS partition that you use
  AWS End User Messaging SMS in.
- Replace `region` with the AWS Region that you use AWS End User Messaging SMS
  in.
- Replace `accountId` with the unique ID for your
  AWS account.
- Replace `snsTopicArn` with the Amazon SNS topics that will
  receive messages.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SMSVoiceAllowSNSPublish",
 "Effect": "Allow",
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`snsTopicArn`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Sid": "SMSVoiceAllowEncryptedSNSTopics",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:aws:sns:topicArn": "arn:aws:sns:`us-east-1`:`111122223333`:`snsTopicArn`",
 "aws:CalledViaLast": "sns.amazonaws.com"
 }
 }
 }
 ]
}`

```
