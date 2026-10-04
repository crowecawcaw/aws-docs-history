

# Send a message
<a name="nx-push-send"></a>

After you create an application and enable one or more push channels, you can send push notifications to the devices registered with your app. You send a push notification through the channel that matches the recipient device, and AWS End User Messaging Push forwards the message to the corresponding push notification service – Apple Push Notification service (APNs), Firebase Cloud Messaging (FCM), Amazon Device Messaging (ADM), or Baidu Cloud Push – which delivers it to the device.

## API operations
<a name="nx-push-send-operations"></a>

Push notifications are sent with the Amazon Pinpoint API (the `mobiletargeting` namespace). Use the following API operation to send push notifications.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendMessages` | Sends a push notification to the registered device endpoints for your application. | All outbound push. | 

## In this section
<a name="nx-push-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-push-send-outbound.md) | Send push notifications to registered device endpoints, including how each push notification service delivers the message. | 