# Use Amazon SNS Topics for Data Labeling

You need to create an Amazon SNS input to create a streaming labeling job. Optionally,
you may provide an Amazon SNS output topic.

When you create an Amazon SNS topic to use in your streaming labeling job, note down the
topic Amazon Resource Name (ARN). The ARN will be the input values for the parameter
`SnsTopicArn` in `InputConfig` and `OutputConfig`
when you create a labeling job.

## Create an Input Topic

Your input topic is used to send new data objects to Ground Truth. To create an input
topic, follow the instructions in [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the
Amazon Simple Notification Service Developer Guide.

Note down your input topic ARN and use it as input for the
`CreateLabelingJob` parameter `SnsTopicArn` in
`InputConfig`.

## Create an Output Topic

If you provide an output topic, it is used to send notifications when a data
object is labeled. When you create a topic, you have the option to add an encryption
key. Use this option to add a AWS Key Management Service customer managed key to your topic to
encrypt the output data of your labeling job before it is published to your output
topic.

To create an output topic, follow the instructions in [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the
Amazon Simple Notification Service Developer Guide.

If you add encryption, you must attach additional permission to the topic.
See [Add Encryption to Your Output
Topic (Optional)](#sms-streaming-encryption "#sms-streaming-encryption").
for more information.

###### Important

To add a customer managed key to your output topic while creating a topic in the console,
do not use the **(Default) alias/aws/sns** option. Select a
customer managed key that you created.

Note down your input topic ARN and use it in your
`CreateLabelingJob` request in the parameter `SnsTopicArn`
in `OutputConfig`.

### Add Encryption to Your Output

Topic (Optional)

To encrypt messages published to your output topic, you need to provide an
AWS KMS customer managed key to your topic. Modify the following policy
and add it to your customer managed key to give Ground Truth permission to encrypt output data
before publishing it to your output topic.

Replace `<account_id>` with the
ID of the account that you are using to create your topic. To learn how to
find your AWS account ID, see [Finding Your AWS Account ID](../../../IAM/latest/UserGuide/console_account-alias.md#FindingYourAWSId "../../../IAM/latest/UserGuide/console_account-alias.md#FindingYourAWSId").

JSON

```
`{
 "Id": "key-console-policy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow access for Key Administrators",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/Admin"
 },
 "Action": [
 "kms:Create*",
 "kms:Describe*",
 "kms:Enable*",
 "kms:List*",
 "kms:Put*",
 "kms:Update*",
 "kms:Revoke*",
 "kms:Disable*",
 "kms:Get*",
 "kms:Delete*",
 "kms:TagResource",
 "kms:UntagResource",
 "kms:ScheduleKeyDeletion",
 "kms:CancelKeyDeletion"
 ],
 "Resource": "*"
 }
 ]
}`

```

Additionally, you must modify and add the following policy to the
execution role that you use to create your labeling job (the input value for
`RoleArn`).

Replace `<account_id>` with the
ID of the account that you are using to create your topic. Replace
`<region>` with the AWS
Region you are using to create your labeling job. Replace
`<key_id>` with your customer managed key
ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "sid1",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`your_key_id`"
 }
 ]
}`

```

For more information on creating and securing keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") and [Using Key
Policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the AWS Key Management Service Developer Guide.

## Subscribe an Endpoint to

Your Amazon SNS Output Topic

When a worker completes a labeling job task from a Ground Truth streaming labeling
job, Ground Truth uses your output topic to publish output data to one or more
endpoints that you specify. To receive notifications when a worker finishes a
labeling task, you must subscribe an endpoint to your Amazon SNS output topic.

To learn how to add endpoints to your output topic, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the
_Amazon Simple Notification Service Developer Guide_.

To learn more about the output data format that is published to these endpoints,
see [Labeling job output data](sms-data-output.md "sms-data-output.md").

###### Important

If you do not subscribe an endpoint to your Amazon SNS output topic, you will
not receive notifications when new data objects are labeled.
