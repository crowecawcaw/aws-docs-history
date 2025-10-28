**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Troubleshooting the push channel

Verify that logging is turned on to assist in identifying the cause of failure. For more
information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging "troubleshooting.md#troubleshooting-logging"). For
transactional push notifications that are not sent via a Campaign or Journey, log
[API response](../developerguide/event-streams.md "../developerguide/event-streams.md") to learn on [delivery status](../apireference/apps-application-id-messages.md#apps-application-id-messages-model-messageresult "../apireference/apps-application-id-messages.md#apps-application-id-messages-model-messageresult").

## Monitoring delivery issues

- For direct push notification messages sent through the SendMessages API,
  verify that you capture the API response to get insights on the delivery. To do
  so, review the StatusMessage attribute inside the [EndpointResult](../apireference/apps-application-id-messages.md#apps-application-id-messages-model-messageresponse "../apireference/apps-application-id-messages.md#apps-application-id-messages-model-messageresponse") object in the response. This
  attribute contains the [Platform response codes](../../../sns/latest/dg/sns-msg-status.md#platform-returncodes "../../../sns/latest/dg/sns-msg-status.md#platform-returncodes") received from the
  Downstream Push Notification Service.
- For campaigns, verify that logging through Kinesis Data Streams is turned on. Review the
  [Platform response codes](../../../sns/latest/dg/sns-msg-status.md#platform-returncodes "../../../sns/latest/dg/sns-msg-status.md#platform-returncodes") in the [\_campaign.send](../developerguide/event-streams-data-campaign.md#event-streams-data-campaign-attributes "../developerguide/event-streams-data-campaign.md#event-streams-data-campaign-attributes") event for delivery outcome
  received by Amazon Pinpoint from the Downstream Push Notification Service.

## Message not

received

###### **Issues and solutions**

- Device connectivity issues – If the issue is only occurring on certain devices,
  verify that these devices aren't blocked from connecting to the push
  notification service endpoints. See [FCM ports and your firewall](https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall "https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall") and [If your Apple devices aren't
  getting Apple push notifications](https://support.apple.com/en-us/102266 "https://support.apple.com/en-us/102266").
- Endpoint **OptOut** attribute value – If an endpoint
  **OptOut** value is set to `ALL`, the endpoint
  will not receive notifications. Use the [get-endpoint](../../../cli/latest/reference/pinpoint/get-endpoint.md "../../../cli/latest/reference/pinpoint/get-endpoint.md") CLI to confirm that the endpoint
  **OptOut** value is set to `NONE`. If the
  endpoint is opted out, messages sent through campaigns or journeys won't be
  delivered to the endpoint, and no logs will be generated.
- Token environment – Verify that the channel type for your Amazon Pinpoint endpoint matches
  the token generated for the device. For example, use GCM as a channel for an app
  token address with FCM integration and for APNs, APNS_Sandbox for your app in
  sandbox, or APNS for app in production.

For insights on delivery attempts with a failure status, see the [Push Notification Response codes for the respective
Push Channel](../../../sns/latest/dg/sns-msg-status.md#platform-returncodes "../../../sns/latest/dg/sns-msg-status.md#platform-returncodes") used in the delivery attempt.

## Messages are not

displayed

- If the logs show a Successful Delivery and if messages are not displayed on the system notification tray, this indicates an issue with the notification being delivered to the device but not being handled appropriately in the client application.
- You might see that the Kinesis event logs show a **Successful
  Delivery** status, or that an issue only occurs with a particular
  request payload or message type. This issue might indicate that the notification
  is being delivered to the device, but not being displayed on the system
  notification tray.

This can occur with a particular request payload or Message type (E.g. Data
for FCM, Silent for APNs). For example, if messages are received as alert/
notification payload but not as data/silent payload, check what the intended
action is when a message type of data, notification, alert, or background is
received on your application, and whether the application can handle the
different message types.

- To troubleshoot, incorporate log statements in your app’s message handler. For an example, see
  [FCM](https://firebase.google.com/docs/cloud-messaging/android/receive "https://firebase.google.com/docs/cloud-messaging/android/receive") and [APNs](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application "https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application"). This will help determine whether the the notification is received by the device but not displayed in the system notifications tray.
