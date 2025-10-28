# Fanout Amazon SNS notifications to Lambda functions for

automated processing

Amazon SNS integrates with AWS Lambda, allowing you to trigger Lambda functions in response to
Amazon SNS notifications. When a message is published to an SNS topic that has a Lambda function
subscribed to it, the Lambda function is invoked with the payload of the published message. The
Lambda function receives the message payload as an input parameter and can manipulate the
information in the message, publish the message to other SNS topics, or send the message to
other AWS services.

Amazon SNS also supports message delivery status attributes for message notifications sent to
Lambda endpoints. For more information, see [Amazon SNS message delivery status](sns-topic-attributes.md "sns-topic-attributes.md").

###### Topics

- [Prerequisites](lambda-prereq.md "lambda-prereq.md")
- [Subscribing a function to a topic](lambda-console.md "lambda-console.md")
