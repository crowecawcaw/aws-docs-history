# Stop rule set action

The **Stop** action terminates the evaluation of the receipt rule set
and, optionally, notifies you through Amazon SNS. This action has the following options.

- SNS Topic—The name or ARN of the Amazon SNS topic
  to notify when the Stop action is performed. An example of an Amazon SNS topic ARN is
  _arn:aws:sns:us-east-1:123456789012:MyTopic_. You can also
  create an Amazon SNS topic when you set up your action by choosing **Create SNS
  Topic**. For more information about Amazon SNS topics, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg/CreateTopic.md "../../../sns/latest/dg/CreateTopic.md").

###### Note

The Amazon SNS topic you choose must be in the same AWS Region as the Amazon SES
endpoint you use to receive email.
