# Amazon SNS message attributes

Amazon SNS supports delivery of message attributes, which let you provide structured metadata
items (such as timestamps, geospatial data, signatures, and identifiers) about the message.
For SQS subscriptions, a maximum of 10 message attributes can be sent when [Raw Message Delivery](sns-large-payload-raw-message-delivery.md "sns-large-payload-raw-message-delivery.md") is enabled.
To send more than 10 message attributes, Raw Message Delivery must be disabled. Messages
with more than 10 message attributes directed towards Raw Message Delivery enabled Amazon SQS
subscriptions will be discarded as client side errors.

Message attributes are optional and separate from—but are sent together
with—the message body. The receiver can use this information to decide how to handle
the message without having to process the message body first.

For information about sending messages with attributes using the AWS Management Console or the
AWS SDK for Java, see the [To publish messages to Amazon SNS topics using the
AWS Management Console](sns-publishing.md#sns-publishing-messages "sns-publishing.md#sns-publishing-messages") tutorial.

###### Note

Message attributes are sent only when the message structure is String, not
JSON.

You can also use message attributes to help structure the push notification message for
mobile endpoints. In this scenario, the message attributes are used only to help structure
the push notification message. The attributes are not delivered to the endpoint as they are
when sending messages with message attributes to Amazon SQS endpoints.

You can also use message attributes to make your messages filterable using subscription
filter policies. You can apply filter policies to topic subscriptions. When a filter policy
is applied with filter policy scope set to `MessageAttributes` (default), a
subscription receives only those messages that have attributes that the policy accepts. For
more information, see [Amazon SNS message filtering](sns-message-filtering.md "sns-message-filtering.md").

###### Note

When message attributes are used for filtering, the value must be a valid JSON string.
Doing this ensures that the message is delivered to a subscription with message
attributes filtering enabled.

## Message attribute items and validation

Each message attribute consists of the following items:

- **Name** – The message attribute name can
  contain the following characters: A-Z, a-z, 0-9, underscore(\_), hyphen(-), and
  period (.). The name must not start or end with a period, and it should not have
  successive periods. The name is case-sensitive and must be unique among all
  attribute names for the message. The name can be up to 256 characters long. The
  name cannot start with `AWS.` or `Amazon.` (or any
  variations in casing) because these prefixes are reserved for use by
  Amazon Web Services.
- **Type** – The supported message attribute
  data types are `String`, `String.Array`,
  `Number`, and `Binary`. The data type has the same
  restrictions on the content as the message body. For more information, see the
  [Message attribute data types and
  validation](#SNSMessageAttributes.DataTypes "#SNSMessageAttributes.DataTypes") section.
- **Value** – The user-specified message
  attribute value. For string data types, the value attribute must follow the same
  content restrictions as the message body. However, if the message attribute is
  used for filtering, the value must be a valid JSON string to ensure
  compatibility with Amazon SNS subscription filter policies. For more
  information, see the [Publish](../api/API_Publish.md "../api/API_Publish.md")
  action in the _Amazon Simple Notification Service API Reference_.

Name, type, and value must not be empty or null. In addition, the message body should
not be empty or null. All parts of the message attribute, including name, type, and
value, are included in the message size restriction, which is 256 KB.

## Message attribute data types and

validation

Message attribute data types identify how the message attribute values are handled by
Amazon SNS. For example, if the type is a number, Amazon SNS validates that it's a number.

Amazon SNS supports the following logical data types for all endpoints except as
noted:

- **String** – Strings are Unicode with
  UTF-8 binary encoding. For a list of code values, see [http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters "http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters").

###### Note

Surrogate values are not supported in the message attributes. For example,
using a surrogate value to represent an emoji will give you the following
error: `Invalid attribute value was passed in for message
 attribute`.

- **String.Array** – An array, formatted as
  a string, that can contain multiple values. The values can be strings, numbers,
  or the keywords `true`, `false`, and `null`. A
  String.Array of number or boolean type does not require quotes. Multiple
  String.Array values are separated by commas.

This data type isn't supported for AWS Lambda subscriptions. If you specify
this data type for Lambda endpoints, it's passed as the `String` data
type in the JSON payload that Amazon SNS delivers to Lambda.

- **Number** – Numbers are positive or
  negative integers or floating-point numbers. Numbers have sufficient range and
  precision to encompass most of the possible values that integers, floats, and
  doubles typically support. A number can have a value from
  -109 to 109, with 5
  digits of accuracy after the decimal point. Leading and trailing zeroes are
  trimmed.

This data type isn't supported for AWS Lambda subscriptions. If you specify
this data type for Lambda endpoints, it's passed as the `String` data
type in the JSON payload that Amazon SNS delivers to Lambda.

- **Binary** – Binary type attributes can
  store any binary data; for example, compressed data, encrypted data, or
  images.

## Reserved message attributes for mobile push

notifications

The following table lists the reserved message attributes for mobile push notification
services that you can use to structure your push notification message:

| Push notification service                  | Reserved message attribute              |
| ------------------------------------------ | --------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ADM                                        | `AWS.SNS.MOBILE.ADM.TTL`                |
| APNs1                                      | `AWS.SNS.MOBILE.APNS_MDM.TTL`           |
| `AWS.SNS.MOBILE.APNS_MDM_SANDBOX.TTL`      |                                         | `AWS.SNS.MOBILE.APNS_PASSBOOK.TTL`     |
| `AWS.SNS.MOBILE.APNS_PASSBOOK_SANDBOX.TTL` |                                         | `AWS.SNS.MOBILE.APNS_SANDBOX.TTL`      |
| `AWS.SNS.MOBILE.APNS_VOIP.TTL`             |                                         | `AWS.SNS.MOBILE.APNS_VOIP_SANDBOX.TTL` |
| `AWS.SNS.MOBILE.APNS.COLLAPSE_ID`          |                                         | `AWS.SNS.MOBILE.APNS.PRIORITY`         |
| `AWS.SNS.MOBILE.APNS.PUSH_TYPE`            |                                         | `AWS.SNS.MOBILE.APNS.TOPIC`            |
| `AWS.SNS.MOBILE.APNS.TTL`                  |
| Baidu                                      | `AWS.SNS.MOBILE.BAIDU.DeployStatus`     |
| `AWS.SNS.MOBILE.BAIDU.MessageKey`          |                                         | `AWS.SNS.MOBILE.BAIDU.MessageType`     |
| `AWS.SNS.MOBILE.BAIDU.TTL`                 |
| FCM                                        | `AWS.SNS.MOBILE.FCM.TTL`                |
| `AWS.SNS.MOBILE.GCM.TTL`                   |
| macOS                                      | `AWS.SNS.MOBILE.MACOS_SANDBOX.TTL`      |
| `AWS.SNS.MOBILE.MACOS.TTL`                 |
| MPNS                                       | `AWS.SNS.MOBILE.MPNS.NotificationClass` |
| `AWS.SNS.MOBILE.MPNS.TTL`                  |                                         | `AWS.SNS.MOBILE.MPNS.Type`             |
| WNS                                        | `AWS.SNS.MOBILE.WNS.CachePolicy`        |
| `AWS.SNS.MOBILE.WNS.Group`                 |                                         | `AWS.SNS.MOBILE.WNS.Match`             |
| `AWS.SNS.MOBILE.WNS.SuppressPopup`         |                                         | `AWS.SNS.MOBILE.WNS.Tag`               |
| `AWS.SNS.MOBILE.WNS.TTL`                   |                                         | `AWS.SNS.MOBILE.WNS.Type`              | 1 Apple will reject Amazon SNS notifications if message attributes do not meet their requirements. For additional details, see [Sending Notification Requests to APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns") on the Apple Developer website. |
