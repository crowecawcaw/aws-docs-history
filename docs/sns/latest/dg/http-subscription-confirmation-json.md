# HTTP/HTTPS subscription

confirmation JSON format

After you subscribe an HTTP/HTTPS endpoint, Amazon SNS sends a subscription confirmation
message to the HTTP/HTTPS endpoint. This message contains a `SubscribeURL`
value that you must visit to confirm the subscription (alternatively, you can use the
`Token` value with the [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md")).

###### Note

Amazon SNS doesn't send notifications to this endpoint until the subscription is
confirmed

The subscription confirmation message is a POST message with a message body that
contains a JSON document with the following name-value pairs.

**`Type`**

The type of message. For a subscription confirmation, the type is
`SubscriptionConfirmation`.

**`MessageId`**

A Universally Unique Identifier (UUID), unique for each message published.
For a message that Amazon SNS resends during a retry, the message ID of the
original message is used.

**`Token`**

A value you can use with the [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md") action to confirm the
subscription. Alternatively, you can simply visit the
`SubscribeURL`.

**`TopicArn`**

The Amazon Resource Name (ARN) for the topic that this endpoint is
subscribed to.

**`Message`**

A string that describes the message. For subscription confirmation, this
string looks like this:

```
You have chosen to subscribe to the topic arn:aws:sns:us-east-2:123456789012:MyTopic.\nTo confirm the subscription, visit the SubscribeURL included in this message.
```

**`SubscribeURL`**

The URL that you must visit in order to confirm the subscription.
Alternatively, you can instead use the `Token` with the [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md") action to confirm the
subscription.

**`Timestamp`**

The time (GMT) when the subscription confirmation was sent.

**`SignatureVersion`**

Version of the Amazon SNS signature used.

- If the `SignatureVersion` is **1**, `Signature` is a Base64-encoded
  `SHA1withRSA` signature of the `Message`,
  `MessageId`, `Type`,
  `Timestamp`, and `TopicArn` values.
- If the `SignatureVersion` is **2**, `Signature` is a Base64-encoded
  `SHA256withRSA` signature of the
  `Message`, `MessageId`, `Type`,
  `Timestamp`, and `TopicArn` values.

**`Signature`**

Base64-encoded `SHA1withRSA` or `SHA256withRSA`
signature of the `Message`, `MessageId`,
`Type`, `Timestamp`, and `TopicArn`
values.

**`SigningCertURL`**

The URL to the certificate that was used to sign the message.

The following HTTP POST message is an example of a
`SubscriptionConfirmation` message to an HTTP endpoint.

```
POST / HTTP/1.1
x-amz-sns-message-type: SubscriptionConfirmation
x-amz-sns-message-id: 165545c9-2a5c-472c-8df2-7ff2be2b3b1b
x-amz-sns-topic-arn: arn:aws:sns:us-west-2:123456789012:MyTopic
Content-Length: 1336
Content-Type: text/plain; charset=UTF-8
Host: myhost.example.com
Connection: Keep-Alive
User-Agent: Amazon Simple Notification Service Agent

{
  "Type" : "SubscriptionConfirmation",
  "MessageId" : "165545c9-2a5c-472c-8df2-7ff2be2b3b1b",
  "Token" : "2336412f37...",
  "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
  "Message" : "You have chosen to subscribe to the topic arn:aws:sns:us-west-2:123456789012:MyTopic.\nTo confirm the subscription, visit the SubscribeURL included in this message.",
  "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37...",
  "Timestamp" : "2012-04-26T20:45:04.751Z",
  "SignatureVersion" : "1",
  "Signature" : "EXAMPLEpH+DcEwjAPg8O9mY8dReBSwksfg2S7WKQcikcNKWLQjwu6A4VbeS0QHVCkhRS7fUQvi2egU3N858fiTDN6bkkOxYDVrY0Ad8L10Hs3zH81mtnPk5uvvolIC1CXGu43obcgFxeL3khZl8IKvO61GWB6jI9b5+gLPoBc1Q=",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
}
```
