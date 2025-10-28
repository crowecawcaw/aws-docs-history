End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Supported actions to receive data and trigger

actions in AWS IoT Events

AWS IoT Events can trigger actions when it detects a specified event or transition event. You can
define built-in actions to use a timer or set a variable, or send data to other AWS
resources. Learn how to configure and customize these actions to create automated responses
to your various IoT events.

###### Note

When you define an action in a detector model, you can use expressions for parameters
that are string data type. For more information, see [Expressions](iotevents-expressions.md "iotevents-expressions.md").

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
