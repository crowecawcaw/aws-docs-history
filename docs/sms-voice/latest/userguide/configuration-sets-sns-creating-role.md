# Amazon SNS access policy

Access to an Amazon SNS topic is controlled by a _resource policy_
attached to the Amazon SNS topic, this is also called an _access
policy_. For more information about Amazon SNS _access
polices_, see [Identity and access management](../../../sns/latest/dg/security-iam.md "../../../sns/latest/dg/security-iam.md") in the
_Amazon SNS Developer Guide_.

###### Note

If your Amazon SNS topic has server-side encryption enabled with AWS Key Management Service then also add the policy to the associated [symmetric encryption customer](#configuration-sets-sns-creating-role-encrypted "#configuration-sets-sns-creating-role-encrypted") managed key.

Update the _access
policy_ with the following statement to permit AWS End User Messaging SMS to publish to the
Amazon SNS topic.

- Replace `111122223333` with the unique
  ID for your AWS account.
- Replace `TopicName` with the name of the Amazon SNS
  topic.
- Replace `Region` with the AWS Region that
  contains the Amazon SNS topic and configuration set.
- Replace `ConfigSetName` with the name of the
  configuration set.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sms-voice.amazonaws.com"
 },
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`TopicName`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "accountId"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sms-voice:`us-east-1`:`111122223333`:configuration-set/`ConfigSetName`"
 }
 }
 }
 ]
}`

```

## Access policy for encrypted Amazon SNS topics

If your Amazon SNS topic has server-side encryption enabled with AWS Key Management Service, add the following policy to the associated symmetric encryption customer managed key.
You must add the policy to a customer managed key because you cannot modify the AWS managed key for Amazon SNS.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "example-ID",
 "Statement": [
 {
 "Sid": "example-statement-ID",
 "Effect": "Allow",
 "Principal": {
 "Service": "sms-voice.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```
