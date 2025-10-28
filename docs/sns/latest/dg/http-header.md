# HTTP/HTTPS headers

When Amazon SNS sends a subscription confirmation, notification, or unsubscribe
confirmation message to HTTP/HTTPS endpoints, it sends a POST message with a number of
Amazon SNS-specific header values. You can use header values for such tasks as identifying
the message type without having to parse the JSON message body to read the
`Type` value. By default, Amazon SNS sends all the notification to HTTP/S
endpoints with `Content-Type` set to `text/plain; charset=UTF-8`.
To choose a `Content-Type` other than text/plain (default), see
`headerContentType` in [Creating an HTTP/S delivery policy](sns-message-delivery-retries.md#creating-delivery-policy "sns-message-delivery-retries.md#creating-delivery-policy").

**`x-amz-sns-message-type`**

The type of message. The possible values are
`SubscriptionConfirmation`, `Notification`, and
`UnsubscribeConfirmation`.

**`x-amz-sns-message-id`**

A Universally Unique Identifier (UUID), unique for each message published.
For a notification that Amazon SNS resends during a retry, the message ID of the
original message is used.

**`x-amz-sns-topic-arn`**

The Amazon Resource Name (ARN) for the topic that this message was
published to.

**`x-amz-sns-subscription-arn`**

The ARN for the subscription to this endpoint.

The following HTTP POST header is an example of a header for a
`Notification` message to an HTTP endpoint.

```
POST / HTTP/1.1
x-amz-sns-message-type: Notification
x-amz-sns-message-id: 165545c9-2a5c-472c-8df2-7ff2be2b3b1b
x-amz-sns-topic-arn: arn:aws:sns:us-west-2:123456789012:MyTopic
x-amz-sns-subscription-arn: arn:aws:sns:us-west-2:123456789012:MyTopic:2bcfbf39-05c3-41de-beaa-fcfcc21c8f55
Content-Length: 1336
Content-Type: text/plain; charset=UTF-8
Host: myhost.example.com
Connection: Keep-Alive
User-Agent: Amazon Simple Notification Service Agent
```
