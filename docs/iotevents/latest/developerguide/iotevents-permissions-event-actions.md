End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Action permissions for AWS IoT Events

AWS IoT Events enables you to trigger actions which use other AWS services. To do so, you must
grant AWS IoT Events permission to perform these actions on your behalf. This section contains a list
of the actions and an example policy which grants permission to perform all these actions on
your resources. Change the `region` and
`account-id` references as required. When possible, you should
also change the wildcards (\*) to refer to specific resources that will be accessed. You can
use the IAM console to grant permission to AWS IoT Events to send an Amazon SNS alert that you have
defined.
.

AWS IoT Events supports the following actions that let you use a timer
or set a variable:

- [setTimer](built-in-actions.md#iotevents-set-timer "built-in-actions.md#iotevents-set-timer") to create a
  timer.
- [resetTimer](built-in-actions.md#iotevents-reset-timer "built-in-actions.md#iotevents-reset-timer") to reset the
  timer.
- [clearTimer](built-in-actions.md#iotevents-clear-timer "built-in-actions.md#iotevents-clear-timer") to delete the
  timer.
- [setVariable](built-in-actions.md#iotevents-set-variable "built-in-actions.md#iotevents-set-variable") to create a
  variable.
  AWS IoT Events supports the following actions that let you work
  with AWS services:

- [iotTopicPublish](iotevents-other-aws-services.md#iotevents-iotcore "iotevents-other-aws-services.md#iotevents-iotcore") to publish a
  message on an MQTT topic.
- [iotEvents](iotevents-other-aws-services.md#iotevents-iteinput "iotevents-other-aws-services.md#iotevents-iteinput") to send data to
  AWS IoT Events as an input value.
- [iotSiteWise](iotevents-other-aws-services.md#iotevents-iotsitewise "iotevents-other-aws-services.md#iotevents-iotsitewise") to send data
  to an asset property in AWS IoT SiteWise.
- [dynamoDB](iotevents-other-aws-services.md#iotevents-dynamodb "iotevents-other-aws-services.md#iotevents-dynamodb") to send data to an
  Amazon DynamoDB table.
- [dynamoDBv2](iotevents-other-aws-services.md#iotevents-dynamodbv2 "iotevents-other-aws-services.md#iotevents-dynamodbv2") to send data
  to an Amazon DynamoDB table.
- [firehose](iotevents-other-aws-services.md#iotevents-firehose "iotevents-other-aws-services.md#iotevents-firehose") to send data to an
  Amazon Data Firehose stream.
- [lambda](iotevents-other-aws-services.md#iotevents-lambda "iotevents-other-aws-services.md#iotevents-lambda") to invoke an AWS Lambda
  function.
- [sns](iotevents-other-aws-services.md#iotevents-sns "iotevents-other-aws-services.md#iotevents-sns") to send data as a push
  notification.
- [sqs](iotevents-other-aws-services.md#iotevents-sqs "iotevents-other-aws-services.md#iotevents-sqs") to send data to an Amazon SQS
  queue.

###### Example Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iot:Publish",
 "Resource": "arn:aws:iot:`us-east-1`:`123456789012`:topic/*"
 },
 {
 "Effect": "Allow",
 "Action": "iotevents:BatchPutMessage",
 "Resource": "arn:aws:iotevents:`us-east-1`:`123456789012`:input/*"
 },
 {
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "dynamodb:PutItem",
 "Resource": "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Resource": "arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/*"
 },
 {
 "Effect": "Allow",
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:*"
 },
 {
 "Effect": "Allow",
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`123456789012`:*"
 },
 {
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:`us-east-1`:`123456789012`:*"
 }
 ]
}`

```
