# Using the Amazon SNS time to live message attribute for mobile push

notifications

Amazon Simple Notification Service (Amazon SNS) provides support for setting a _Time To Live (TTL)_
message attribute for mobile push notifications messages. This is in addition to the
existing capability of setting TTL within the Amazon SNS message body for the mobile push
notification services that support this, such as Amazon Device Messaging (ADM) and Firebase Cloud Messaging (FCM)
when sending to Android.

The TTL message attribute is used to specify expiration metadata about a message. This
allows you to specify the amount of time that the push notification service, such as
Apple Push Notification Service (APNs) or FCM, has to deliver the message to the endpoint. If for some reason
(such as the mobile device has been turned off) the message is not deliverable within the
specified TTL, then the message will be dropped and no further attempts to deliver it will
be made. To specify TTL within message attributes, you can use the AWS Management Console, AWS software
development kits (SDKs), or query API.

## TTL message attributes for push notification

services

The following is a list of the TTL message attributes for push notification services
that you can use to set when using the AWS SDKs or query API:

| Push notification service                              | TTL message attribute             |
| ------------------------------------------------------ | --------------------------------- |
| Amazon Device Messaging (ADM)                          | `AWS.SNS.MOBILE.ADM.TTL`          |
| Apple Push Notification Service (APNs)                 | `AWS.SNS.MOBILE.APNS.TTL`         |
| Apple Push Notification Service Sandbox (APNs_SANDBOX) | `AWS.SNS.MOBILE.APNS_SANDBOX.TTL` |
| Baidu Cloud Push (Baidu)                               | `AWS.SNS.MOBILE.BAIDU.TTL`        |
| Firebase Cloud Messaging (FCM when sending to Android) | `AWS.SNS.MOBILE.FCM.TTL`          |
| Windows Push Notification Services (WNS)               | `AWS.SNS.MOBILE.WNS.TTL`          |

Each of the push notification services handle TTL differently. Amazon SNS provides an
abstract view of TTL over all the push notification services, which makes it easier to
specify TTL. When you use the AWS Management Console to specify TTL (in seconds), you only have to
enter the TTL value once and Amazon SNS will then calculate the TTL for each of the selected
push notification services when publishing the message.

TTL is relative to the publish time. Before handing off a push notification message
to a specific push notification service, Amazon SNS computes the dwell time (the time between
the publish timestamp and just before handing off to a push notification service) for
the push notification and passes the remaining TTL to the specific push notification
service. If TTL is shorter than the dwell time, Amazon SNS won't attempt to publish.

If you specify a TTL for a push notification message, then the TTL value must be a
positive integer, unless the value of `0` has a specific meaning for the push
notification service—such as with APNs and FCM (when sending to Android). If
the TTL value is set to `0` and the push notification service does not have a
specific meaning for `0`, then Amazon SNS will drop the message. For more
information about the TTL parameter set to `0` when using APNs, see
_Table A-3 Item identifiers for remote notifications_ in the
[Binary Provider API](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/BinaryProviderAPI.html "https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/BinaryProviderAPI.html") documentation.

## Precedence order for determining TTL

The precedence that Amazon SNS uses to determine the TTL for a push notification message is
based on the following order, where the lowest number has the highest priority:

1. Message attribute TTL
2. Message body TTL
3. Push notification service default TTL (varies per service)
4. Amazon SNS default TTL (4 weeks)

If you set different TTL values (one in message attributes and another in the message
body) for the same message, then Amazon SNS will modify the TTL in the message body to match
the TTL specified in the message attribute.

## Specifying TTL using the AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Mobile**, **Push
   notifications**.
3. On the **Mobile push notifications** page, in the
   **Platform applications** section, choose an
   application.
4. On the `**MyApplication**` page, in
   the **Endpoints** section, choose an application endpoint and
   then choose **Publish message**.
5. In the **Message details** section, enter the TTL (the number
   of seconds that the push notification service has to deliver the message to the
   endpoint).
6. Choose **Publish message**.
