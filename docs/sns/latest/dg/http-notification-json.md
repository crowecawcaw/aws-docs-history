# HTTP/HTTPS notification JSON format

When Amazon SNS sends a notification to a subscribed HTTP or HTTPS endpoint, the POST
message sent to the endpoint has a message body that contains a JSON document with the
following name-value pairs.

**`Type`**

The type of message. For a notification, the type is
`Notification`.

**`MessageId`**

A Universally Unique Identifier (UUID), unique for each message published.
For a notification that Amazon SNS resends during a retry, the message ID of the
original message is used.

**`TopicArn`**

The Amazon Resource Name (ARN) for the topic that this message was
published to.

**`Subject`**

The `Subject` parameter specified when the notification was
published to the topic.

###### Note

This is an optional parameter. If no `Subject` was
specified, then this name-value pair does not appear in this JSON
document.

**`Message`**

The `Message` value specified when the notification was
published to the topic.

**`Timestamp`**

The time (GMT) when the notification was published.

**`SignatureVersion`**

Version of the Amazon SNS signature used.

- If the `SignatureVersion` is **1**, `Signature` is a Base64-encoded
  `SHA1withRSA` signature of the `Message`,
  `MessageId`, `Subject` (if present),
  `Type`, `Timestamp`, and
  `TopicArn` values.
- If the `SignatureVersion` is **2**, `Signature` is a Base64-encoded
  `SHA256withRSA` signature of the
  `Message`, `MessageId`, `Subject`
  (if present), `Type`, `Timestamp`, and
  `TopicArn` values.

**`Signature`**

Base64-encoded `SHA1withRSA` or `SHA256withRSA`
signature of the `Message`, `MessageId`,
`Subject` (if present), `Type`,
`Timestamp`, and `TopicArn` values.

**`SigningCertURL`**

The URL to the certificate that was used to sign the message.

**`UnsubscribeURL`**

A URL that you can use to unsubscribe the endpoint from this topic. If you
visit this URL, Amazon SNS unsubscribes the endpoint and stops sending
notifications to this endpoint.

The following HTTP POST message is an example of a `Notification` message
to an HTTP endpoint.

```
POST / HTTP/1.1
x-amz-sns-message-type: Notification
x-amz-sns-message-id: 22b80b92-fdea-4c2c-8f9d-bdfb0c7bf324
x-amz-sns-topic-arn: arn:aws:sns:us-west-2:123456789012:MyTopic
x-amz-sns-subscription-arn: arn:aws:sns:us-west-2:123456789012:MyTopic:c9135db0-26c4-47ec-8998-413945fb5a96
Content-Length: 773
Content-Type: text/plain; charset=UTF-8
Host: myhost.example.com
Connection: Keep-Alive
User-Agent: Amazon Simple Notification Service Agent

{
  "Type" : "Notification",
  "MessageId" : "22b80b92-fdea-4c2c-8f9d-bdfb0c7bf324",
  "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
  "Subject" : "My First Message",
  "Message" : "Hello world!",
  "Timestamp" : "2012-05-02T00:54:06.655Z",
  "SignatureVersion" : "1",
  "Signature" : "EXAMPLEw6JRN...",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem",
  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:123456789012:MyTopic:c9135db0-26c4-47ec-8998-413945fb5a96"
  }
```
