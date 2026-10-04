

# Outbound messaging
<a name="nx-push-send-outbound"></a>

You send push notifications to specific device tokens or endpoints that your application has registered. When you send a message, you specify the application, the channel, the recipient, and the channel-specific payload.

## How push notifications are delivered
<a name="nx-push-send-how"></a>

Each push notification is delivered through the push notification service for the recipient platform: Apple Push Notification service (APNs) for iOS devices and the Safari browser on macOS, Firebase Cloud Messaging (FCM) for Android and web, Amazon Device Messaging (ADM) for Amazon devices, and Baidu Cloud Push. You must enable the channel and provide valid provider credentials for a service before AWS End User Messaging Push can deliver messages through it. For more information about enabling channels, see [How to get set up](nx-push-get-set-up.md).

The message payload that you send is specific to the target push notification service. Each service defines its own payload format and options, such as the notification title and body, and the settings that control how the notification is presented on the device. Construct the payload according to the requirements of the target service. For payload details, see the developer documentation for APNs, FCM, ADM, or Baidu Cloud Push.

## Send a push notification programmatically
<a name="nx-push-send-api"></a>

You can send push notifications programmatically using the AWS CLI or an AWS SDK. Direct messages are sent to specific device tokens or endpoints that your application has registered. When you send a message, you specify the application, the channel, the recipient, and the channel-specific payload.

**Note**  
The complete request syntax, parameters, and per-channel payload examples for sending push notifications are being added to this guide. In the meantime, refer to the API reference for the send operation and the developer documentation for each push notification service for the exact payload fields.