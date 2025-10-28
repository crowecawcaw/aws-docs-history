# Best practices for managing Amazon SNS

mobile push notifications

This section describes best practices that might help you improve your customer
engagement.

## Endpoint

management

Delivery issues might occur in situations were device tokens change due to a user’s
action on the device (for example, an app is re-installed on the device), or [certificate updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns") affecting devices running on a particular iOS version.
It is a recommended best practice by Apple to [register](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/HandlingRemoteNotifications.html#:~:text=Registering%20to%20Receive%20Remote%20Notifications "https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/HandlingRemoteNotifications.html#:~:text=Registering%20to%20Receive%20Remote%20Notifications") with APNs each time your app launches.

Since the device token won’t change each time an app is opened by a user, the
idempotent [`CreatePlatformEndpoint`](../api/API_CreatePlatformEndpoint.md "../api/API_CreatePlatformEndpoint.md") API can be used. However, this can
introduce duplicates for the same device in cases where the token itself is invalid, or
if the endpoint is valid but disabled (for example, a mismatch of production and sandbox
environments).

A device token management mechanism such as the one in the [pseudo code](mobile-platform-endpoint.md#mobile-platform-endpoint-pseudo-code "mobile-platform-endpoint.md#mobile-platform-endpoint-pseudo-code") can be
used.

For information on managing and maintaining FCM v1 device tokens, see [Amazon SNS management of Firebase Cloud Messaging
endpoints](sns-fcm-endpoint-management.md "sns-fcm-endpoint-management.md").

## Delivery status

logging

To monitor push notification delivery status, we recommended you enable delivery
status logging for your Amazon SNS platform application. This helps you troubleshoot delivery
failures because the logs contain provider [response
codes](sns-msg-status.md#platform-returncodes "sns-msg-status.md#platform-returncodes") returned from the push platform service. For details on enabling
delivery status logging, see [How do I access Amazon SNS topic delivery logs for push notifications?](https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-failed-sns-deliveries/ "https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-failed-sns-deliveries/").

## Event

notifications

For managing endpoints in an event driven fashion, you can make use of the [event notifications](application-event-notifications.md#application-event-notifications-sdk "application-event-notifications.md#application-event-notifications-sdk")
functionality. This allows the configured Amazon SNS topic to fanout events to the
subscribers such as a Lambda function, for platform application events of endpoint
creation, deletion, updates, and delivery failures.
