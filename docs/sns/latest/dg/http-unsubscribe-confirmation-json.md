# HTTP/HTTPS unsubscribe confirmation

JSON format

After an HTTP/HTTPS endpoint is unsubscribed from a topic, Amazon SNS sends an unsubscribe
confirmation message to the endpoint.

The unsubscribe confirmation message is a POST message with a message body that
contains a JSON document with the following name-value pairs.

**`Type`**

The type of message. For a unsubscribe confirmation, the type is
`UnsubscribeConfirmation`.

**`MessageId`**

A Universally Unique Identifier (UUID), unique for each message published.
For a message that Amazon SNS resends during a retry, the message ID of the
original message is used.

**`Token`**

A value you can use with the [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md") action to re-confirm the
subscription. Alternatively, you can simply visit the
`SubscribeURL`.

**`TopicArn`**

The Amazon Resource Name (ARN) for the topic that this endpoint has been
unsubscribed from.

**`Message`**

A string that describes the message. For unsubscribe confirmation, this
string looks like this:

```
You have chosen to deactivate subscription arn:aws:sns:us-east-2:123456789012:MyTopic:2bcfbf39-05c3-41de-beaa-fcfcc21c8f55.\nTo cancel this operation and restore the subscription, visit the SubscribeURL included in this message.
```

**`SubscribeURL`**

The URL that you must visit in order to re-confirm the subscription.
Alternatively, you can instead use the `Token` with the [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md") action to re-confirm the
subscription.

**`Timestamp`**

The time (GMT) when the unsubscribe confirmation was sent.

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
`UnsubscribeConfirmation` message to an HTTP endpoint.

```
POST / HTTP/1.1
x-amz-sns-message-type: UnsubscribeConfirmation
x-amz-sns-message-id: 47138184-6831-46b8-8f7c-afc488602d7d
x-amz-sns-topic-arn: arn:aws:sns:us-west-2:123456789012:MyTopic
x-amz-sns-subscription-arn: arn:aws:sns:us-west-2:123456789012:MyTopic:2bcfbf39-05c3-41de-beaa-fcfcc21c8f55
Content-Length: 1399
Content-Type: text/plain; charset=UTF-8
Host: myhost.example.com
Connection: Keep-Alive
User-Agent: Amazon Simple Notification Service Agent

{
  "Type" : "UnsubscribeConfirmation",
  "MessageId" : "47138184-6831-46b8-8f7c-afc488602d7d",
  "Token" : "2336412f37...",
  "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
  "Message" : "You have chosen to deactivate subscription arn:aws:sns:us-west-2:123456789012:MyTopic:2bcfbf39-05c3-41de-beaa-fcfcc21c8f55.\nTo cancel this operation and restore the subscription, visit the SubscribeURL included in this message.",
  "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37fb6...",
  "Timestamp" : "2012-04-26T20:06:41.581Z",
  "SignatureVersion" : "1",
  "Signature" : "EXAMPLEHXgJm...",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
}
```
