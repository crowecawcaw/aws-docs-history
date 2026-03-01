# Granting permissions to publish event notification messages to a destination

You must grant the Amazon S3 principal the necessary permissions to call the relevant
API to publish messages to an SNS topic, an SQS queue, or a Lambda function. This is
so that Amazon S3 can publish event notification messages to a destination.

To troubleshoot publishing event notification messages to a destination, see [Troubleshoot to publish Amazon S3 event notifications to an Amazon Simple Notification Service topic](https://repost.aws/knowledge-center/sns-not-receiving-s3-event-notifications "https://repost.aws/knowledge-center/sns-not-receiving-s3-event-notifications") .

###### Topics

- [Granting permissions to invoke an AWS Lambda function](#grant-lambda-invoke-permission-to-s3 "#grant-lambda-invoke-permission-to-s3")
- [Granting permissions to publish messages to an SNS topic or an SQS queue](#grant-sns-sqs-permission-for-s3 "#grant-sns-sqs-permission-for-s3")

## Granting permissions to invoke an AWS Lambda function

Amazon S3 publishes event messages to AWS Lambda by invoking a Lambda function and
providing the event message as an argument.

When you use the Amazon S3 console to configure event notifications on an Amazon S3
bucket for a Lambda function, the console sets up the necessary permissions on
the Lambda function. This is so that Amazon S3 has permissions to invoke the function
from the bucket. For more information, see [Enabling and configuring event notifications using the Amazon S3 console](enable-event-notifications.md "enable-event-notifications.md").

You can also grant Amazon S3 permissions from AWS Lambda to invoke your Lambda function.
For more information, see [Tutorial:
Using AWS Lambda with Amazon S3](../../../lambda/latest/dg/with-s3-example.md "../../../lambda/latest/dg/with-s3-example.md") in the
_AWS Lambda Developer Guide_.

## Granting permissions to publish messages to an SNS topic or an SQS queue

To grant Amazon S3 permissions to publish messages to the SNS topic or SQS queue,
attach an AWS Identity and Access Management (IAM) policy to the destination SNS topic or SQS queue.

For an example of how to attach a policy to an SNS topic or an SQS queue, see
[Walkthrough: Configuring a bucket for notifications (SNS topic or SQS queue)](ways-to-add-notification-config-to-bucket.md "ways-to-add-notification-config-to-bucket.md"). For more
information about permissions, see the following topics:

- [Example
  cases for Amazon SNS access control](../../../sns/latest/dg/AccessPolicyLanguage_UseCases_Sns.md "../../../sns/latest/dg/AccessPolicyLanguage_UseCases_Sns.md") in the
  _Amazon Simple Notification Service Developer Guide_
- [Identity and access management in
  Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/UsingIAM.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/UsingIAM.md") in the _Amazon Simple Queue Service Developer Guide_

### IAM policy for a destination SNS topic

The following is an example of an AWS Identity and Access Management (IAM) policy that you attach
to the destination SNS topic. For instructions on how to use this policy to
set up a destination Amazon SNS topic for event notifications, see [Walkthrough: Configuring a bucket for notifications (SNS topic or SQS queue)](ways-to-add-notification-config-to-bucket.md "ways-to-add-notification-config-to-bucket.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "example-ID",
 "Statement": [
 {
 "Sid": "Example SNS topic policy",
 "Effect": "Allow",
 "Principal": {
 "Service": "s3.amazonaws.com"
 },
 "Action": [
 "SNS:Publish"
 ],
 "Resource": "arn:aws:sns:us-east-1:`111122223333`:`example-sns-topic`",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`bucket-owner-123456789012`"
 }
 }
 }
 ]
}`

```

### IAM policy for a destination SQS queue

The following is an example of an IAM policy that you attach to the
destination SQS queue. For instructions on how to use this policy to set up
a destination Amazon SQS queue for event notifications, see [Walkthrough: Configuring a bucket for notifications (SNS topic or SQS queue)](ways-to-add-notification-config-to-bucket.md "ways-to-add-notification-config-to-bucket.md").

To use this policy, you must update the Amazon SQS queue ARN, bucket name, and
bucket owner's AWS account ID.

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
 "Service": "s3.amazonaws.com"
 },
 "Action": [
 "SQS:SendMessage"
 ],
 "Resource": "arn:aws:sqs:`us-east-1`:`111122223333`:`queue-name`",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:s3:*:*:`amzn-s3-demo-bucket`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`bucket-owner-123456789012`"
 }
 }
 }
 ]
}`

```

For both the Amazon SNS and Amazon SQS IAM policies, you can specify the
`StringLike` condition in the policy instead of the `ArnLike`
condition.

When `ArnLike` is used, the partition, service, account ID, resource
type, and partial resource ID portions of the ARN must exactly match to the ARN in the request
context. Only the Region and resource path allow partial matching.

When `StringLike` is used instead of `ArnLike`, matching
ignores the ARN structure and allows partial matching, regardless of the portion that's replaced
by the wildcard character. For more information, see [IAM JSON policy
elements](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") in the _IAM User Guide_.

```
"Condition": {         
  "StringLike": { "aws:SourceArn": "arn:aws:s3:*:*:``amzn-s3-demo-bucket``" }
  }
```

### AWS KMS key policy

If the SQS queue or SNS topics are encrypted with an AWS Key Management Service (AWS KMS)
customer managed key, you must grant the Amazon S3 service
principal permission to work with the encrypted topics or queue. To grant the
Amazon S3 service principal permission, add the following statement to the key policy
for the customer managed key.

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
 "Service": "s3.amazonaws.com"
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

For more information about AWS KMS key policies, see [Using key policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

For more information about using server-side encryption with AWS KMS for Amazon SQS
and Amazon SNS, see the following:

- [Key management](../../../sns/latest/dg/sns-key-management.md "../../../sns/latest/dg/sns-key-management.md")
  in the _Amazon Simple Notification Service Developer Guide_.
- [Key management](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.md") in the
  _Amazon Simple Queue Service Developer Guide_.
- [Encrypting messages published to Amazon SNS with AWS KMS](https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/ "https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/") in the
  _AWS Compute Blog_.
