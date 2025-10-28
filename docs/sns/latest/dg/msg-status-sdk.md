# Configuring delivery status logging using the AWS SDKs

The AWS SDKs provide APIs in several languages to set topic attributes for message
delivery status logging. For example, use the [SetTopicAttributes](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md") API to
configure:

- `LambdaSuccessFeedbackRoleArn` – IAM role for successful
  message delivery to Lambda endpoints.
- `LambdaSuccessFeedbackSampleRate` – Sampling rate for
  successful messages to Lambda endpoints.
- `LambdaFailureFeedbackRoleArn` – IAM role for failed
  message delivery to Lambda endpoints.
  **Example AWS CLI command**

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:us-west-2:123456789012:MyTopic \
    --attribute-name LambdaSuccessFeedbackRoleArn \
    --attribute-value arn:aws:iam::123456789012:role/MyFeedbackRole
```

## Topic attributes

Use the following topic attribute name values for message delivery status:

**HTTP**

- `HTTPSuccessFeedbackRoleArn` – Successful message
  delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.
- `HTTPSuccessFeedbackSampleRate` – Percentage of
  successful messages to sample for an Amazon SNS topic that is subscribed to an
  HTTP endpoint.
- `HTTPFailureFeedbackRoleArn` – Failed message delivery
  status for an Amazon SNS topic that is subscribed to an HTTP endpoint.

**Amazon Data Firehose**

- `FirehoseSuccessFeedbackRoleArn` – Successful message
  delivery status for an Amazon SNS topic that is subscribed to an Amazon
  Data Firehose endpoint.
- `FirehoseSuccessFeedbackSampleRate` – Percentage of
  successful messages to sample for an Amazon SNS topic that is subscribed to an
  Amazon Data Firehose endpoint.
- `FirehoseFailureFeedbackRoleArn` – Failed message
  delivery status for an Amazon SNS topic that is subscribed to an Amazon
  Data Firehose endpoint.

**AWS Lambda**

- `LambdaSuccessFeedbackRoleArn` – Successful message
  delivery status for an Amazon SNS topic that is subscribed to an Lambda
  endpoint.
- `LambdaSuccessFeedbackSampleRate` – Percentage of
  successful messages to sample for an Amazon SNS topic that is subscribed to an
  Lambda endpoint.
- `LambdaFailureFeedbackRoleArn` – Failed message delivery
  status for an Amazon SNS topic that is subscribed to an Lambda endpoint.

**Platform application endpoints**

- `ApplicationSuccessFeedbackRoleArn` – Successful message
  delivery status for an Amazon SNS topic that is subscribed to an AWS application endpoint.
- `ApplicationSuccessFeedbackSampleRate` – Percentage of
  successful messages to sample for an Amazon SNS topic that is subscribed to an
  AWS application endpoint.
- `ApplicationFailureFeedbackRoleArn` – Failed message
  delivery status for an Amazon SNS topic that is subscribed to an AWS application endpoint.

###### Note

Additionally, you can configure application attributes to log delivery
status directly to push notification services. For more information, see
[Using Amazon SNS Application
Attributes for Message Delivery Status](sns-msg-status.md "sns-msg-status.md").

**Amazon SQS**

- `SQSSuccessFeedbackRoleArn` – Successful message
  delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.
- `SQSSuccessFeedbackSampleRate` – Percentage of
  successful messages to sample for an Amazon SNS topic that is subscribed to an
  Amazon SQS endpoint.
- `SQSFailureFeedbackRoleArn` – Failed message delivery
  status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint.

Logs for platform application endpoints are written to the same CloudWatch Logs group as
other endpoints.

###### Note

The `<ENDPOINT>SuccessFeedbackRoleArn` and
`<ENDPOINT>FailureFeedbackRoleArn` attributes are used to
give Amazon SNS write access to use CloudWatch Logs on your behalf. The
`<ENDPOINT>SuccessFeedbackSampleRate` attribute is for
specifying the sample rate percentage (0-100) of successfully delivered
messages. After you configure the
`<ENDPOINT>FailureFeedbackRoleArn` attribute, then all
failed message deliveries generate CloudWatch Logs.
