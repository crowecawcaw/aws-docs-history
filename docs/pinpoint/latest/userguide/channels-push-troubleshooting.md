

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting the push channel
<a name="channels-push-troubleshooting"></a>

Verify that logging is turned on to assist in identifying the cause of failure. For more information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging). For transactional push notifications that are not sent via a Campaign or Journey, log [API response](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) to learn on [delivery status](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-messageresult). 

## Monitoring delivery issues
<a name="troubleshooting-push-delivery"></a>
+ For direct push notification messages sent through the SendMessages API, verify that you capture the API response to get insights on the delivery. To do so, review the StatusMessage attribute inside the [EndpointResult](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-messageresponse) object in the response. This attribute contains the [Platform response codes](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html#platform-returncodes) received from the Downstream Push Notification Service. 
+ For campaigns, verify that logging through Kinesis Data Streams is turned on. Review the [Platform response codes](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html#platform-returncodes) in the [\_campaign.send](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-campaign.html#event-streams-data-campaign-attributes) event for delivery outcome received by Amazon Pinpoint from the Downstream Push Notification Service. 

## Message not received
<a name="troubleshooting-push-message-not-received"></a>

****Issues and solutions****
+ Device connectivity issues – If the issue is only occurring on certain devices, verify that these devices aren't blocked from connecting to the push notification service endpoints. See [FCM ports and your firewall](https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall) and [If your Apple devices aren't getting Apple push notifications](https://support.apple.com/en-us/102266).
+ Endpoint **OptOut** attribute value – If an endpoint **OptOut** value is set to `ALL`, the endpoint will not receive notifications. Use the [get-endpoint](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-endpoint.html) CLI to confirm that the endpoint **OptOut** value is set to `NONE`. If the endpoint is opted out, messages sent through campaigns or journeys won't be delivered to the endpoint, and no logs will be generated. 
+ Token environment – Verify that the channel type for your Amazon Pinpoint endpoint matches the token generated for the device. For example, use GCM as a channel for an app token address with FCM integration and for APNs, APNS\_Sandbox for your app in sandbox, or APNS for app in production. 

  For insights on delivery attempts with a failure status, see the [Push Notification Response codes for the respective Push Channel](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html#platform-returncodes) used in the delivery attempt. 

## Messages are not displayed
<a name="troubleshooting-push-message-not-displayed"></a>
+ If the logs show a Successful Delivery and if messages are not displayed on the system notification tray, this indicates an issue with the notification being delivered to the device but not being handled appropriately in the client application. 
+ You might see that the Kinesis event logs show a **Successful Delivery** status, or that an issue only occurs with a particular request payload or message type. This issue might indicate that the notification is being delivered to the device, but not being displayed on the system notification tray. 

  This can occur with a particular request payload or Message type (E.g. Data for FCM, Silent for APNs). For example, if messages are received as alert/ notification payload but not as data/silent payload, check what the intended action is when a message type of data, notification, alert, or background is received on your application, and whether the application can handle the different message types.
+ To troubleshoot, incorporate log statements in your app’s message handler. For an example, see [FCM](https://firebase.google.com/docs/cloud-messaging/android/receive) and [APNs](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application). This will help determine whether the the notification is received by the device but not displayed in the system notifications tray. 