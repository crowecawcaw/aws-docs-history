

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Campaign event data stream from Amazon Pinpoint
<a name="event-streams-data-campaign"></a>

If you use Amazon Pinpoint to send campaigns through a channel, Amazon Pinpoint can stream event data about those campaigns. After you set up event streaming, Amazon Pinpoint retrieves your app's event data for email or SMS messages that you send from a campaign from the destination that you specified during setup for you to view. For detailed information about the data that Amazon Pinpoint streams for email and SMS messages, see [Email event data stream from Amazon Pinpoint](event-streams-data-email.md) and [SMS event data stream from Amazon Pinpoint](event-streams-data-sms.md). For information about how to set up event streaming, see [Set up Amazon Pinpoint to stream app event data through Amazon Kinesis or Amazon Data Firehose](event-streams-setup.md). 

## Campaign event example
<a name="event-streams-data-campaign-example"></a>

The JSON object for a campaign event contains the data shown in the following example.

```
{
  "event_type": "_campaign.send",
  "event_timestamp": 1562109497426,
  "arrival_timestamp": 1562109497494,
  "event_version": "3.1",
  "application": {
    "app_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "sdk": {}
  },
  "client": {
    "client_id": "d8dcf7c5-e81a-48ae-8313-f540cexample"
  },
  "device": {
    "platform": {}
  },
  "session": {},
  "attributes": {
    "treatment_id": "0",
    "campaign_activity_id": "5473285727f04865bc673e527example",
    "delivery_type": "GCM",
    "campaign_id": "4f8d6097c2e8400fa3081d875example",
    "campaign_send_status": "SUCCESS"
  },
  "client_context": {
    "custom": {
      "endpoint": "{\"ChannelType\":\"GCM\",\"EndpointStatus\":\"ACTIVE\",
          ↳\"OptOut\":\"NONE\",\"RequestId\":\"ec229696-9d1e-11e9-8bf1-85d0aexample\",
          ↳\"EffectiveDate\":\"2019-07-02T23:12:54.836Z\",\"User\":{}}"
    }
  },
  "awsAccountId": "123456789012"
}
```

## Campaign event attributes
<a name="event-streams-data-campaign-attributes"></a>

This section defines the attributes that are included in the campaign event stream.


| Attribute | Description | 
| --- | --- | 
| event\_type | The type of event. Possible values are:+  **\_campaign.send** – Amazon Pinpoint executed the campaign. <br />+  **\_campaign.opened\_notification** – For push notification campaigns, this event type indicates that the recipient tapped the notification to open it. <br />+  **\_campaign.received\_foreground** – For push notification campaigns, this event type indicates that the recipient received the message as a foreground notification. <br />+  **\_campaign.received\_background** – For push notification campaigns, this event type indicates that the recipient received the message as a background notification.  **\_campaign.opened\_notification**, **\_campaign.received\_foreground**, and **\_campaign.received\_background** are returned only if you use AWS Amplify. For more information on integrating your app with AWS Amplify. See [Connect your frontend application to Amazon Pinpoint using AWS Amplify](integrate-sdk.md).   | 
| event\_timestamp | The time when the event was reported, shown as Unix time in milliseconds. | 
| arrival\_timestamp | The time when the event was received by Amazon Pinpoint, shown as Unix time in milliseconds. | 
| event\_version | The version of the event JSON schema. Check this version in your event-processing application so that you know when to update the application in response to a schema update.  | 
| application | Information about the Amazon Pinpoint project that's associated with the event. For more information, see the [Application](#event-streams-data-campaign-attributes-application) table. | 
| client | Information about the endpoint that the event is associated with. For more information, see the [Client](#event-streams-data-campaign-attributes-client) table. | 
| device | Information about the device that reported the event. For campaign and transactional messages, this object is empty. | 
| session | Information about the session that generated the event. For campaigns, this object is empty. | 
| attributes | Attributes that are associated with the event. For events that are reported by one of your apps, this object can include custom attributes that are defined by the app. For events that are created when you send a campaign, this object contains attributes that are associated with the campaign. For events that are generated when you send transactional messages, this object contains information that's related to the message itself.<br />For more information, see the [Attributes](#event-streams-data-campaign-attributes-attrs) table. | 
| client\_context | Contains a custom object, which contains an endpoint property. The endpoint property contains the contents of the endpoint record for the endpoint that the campaign was sent to. | 
| awsAccountId | The ID of the AWS account that was used to send the message. | 

### Application
<a name="event-streams-data-campaign-attributes-application"></a>

Includes information about the Amazon Pinpoint project that the event is associated with.


| Attribute | Description | 
| --- | --- | 
| app\_id | The unique ID of the Amazon Pinpoint project that reported the event. | 
| sdk | The SDK that was used to report the event.  | 

### Attributes
<a name="event-streams-data-campaign-attributes-attrs"></a>

Includes information about the campaign that produced the event.


| Attribute | Description | 
| --- | --- | 
| treatment\_id | If the message was sent using an A/B test campaign, this value represents the treatment number of the message. For standard campaigns, this value is `0`. | 
| campaign\_activity\_id | The unique ID that Amazon Pinpoint generates when the event occurs. | 
| delivery\_type | The delivery method for the campaign. Don't confuse this attribute with the `ChannelType` field specified under the `endpoint` property of `client_context`. The `ChannelType` field is typically based on the endpoint that the message is being sent to.<br />For channels that support only one endpoint type, the `delivery_type` and `ChannelType` fields have the same value. For example, for the email channel, the `delivery_type` and `ChannelType` fields have the same value of EMAIL. <br />However, this condition isn't always true for channels that support different endpoint types, such as custom channels. You can use a custom channel for different endpoints, such as EMAIL, SMS, CUSTOM, and so on. In this case, the `delivery_type` identifies a custom delivery event, CUSTOM, and the `ChannelType` specifies the type of endpoint that the campaign was sent to, such as EMAIL, SMS, CUSTOM, and so on. For more information on creating custom channels, see [Create a custom channel in Amazon Pinpoint using a webhook or Lambda function](channels-custom.md).<br />Possible values are:+  **EMAIL** <br />+  ** SMS** <br />+  **ADM** <br />+  **APNS** <br />+  **APNS\_SANDBOX** <br />+  **APNS\_VOIP** <br />+  **APNS\_VOIP\_SANDBOX** <br />+  **VOICE** <br />+  **GCM** <br />+  **BAIDU** <br />+  **PUSH** <br />+  **CUSTOM**  | 
| campaign\_id | The unique ID of the campaign that the message was sent from. | 
| campaign\_send\_status | Indicates the status of the campaign for the target endpoint. Possible values include:+  **SUCCESS** – The campaign was successfully sent to the endpoint.  <br />+  **FAILURE** – The campaign wasn't sent to the endpoint. <br />+  **DAILY\_CAP** – The campaign wasn't sent to the endpoint because the maximum number of daily messages have already been sent to the endpoint. <br />+  **EXPIRED** – The campaign wasn’t sent to the endpoint because sending it would exceed the maximum duration or sending rate settings for the campaign.  <br />+  **QUIET\_TIME** – The campaign wasn't sent to the endpoint because of quiet time restrictions.  <br />+  **HOLDOUT** – The campaign wasn't sent to the endpoint because the endpoint was a member of the holdout group. <br />+  **DUPLICATE\_ADDRESS** – There are duplicate endpoint addresses in the segment. The campaign was sent once to the endpoint address. <br />+  **QUIET\_TIME** – The campaign wasn't sent to the endpoint because of quiet time restrictions. <br />+  **CAMPAIGN\_CAP** – The campaign wasn't sent to the endpoint because the maximum number of messages have already been sent to the endpoint from this campaign. <br />+  **FAILURE\_PERMANENT** – A permanent failure occurred when sending to the endpoint. <br />+  **TRANSIENT\_FAILURE** – A transient failure occurred when sending to the endpoint. <br />+  **THROTTLED** – Sending was throttled. <br />+  **UNKNOWN** – Unknown failure. <br />+  **HOOK\_FAILURE** – Campaign hook failed. <br />+  **CUSTOM\_DELIVERY\_FAILURE** – Custom delivery failed. <br />+  **RECOMMENDATION\_FAILURE** – Recommender failed. <br />+  **UNSUPPORTED\_CHANNEL** – Channel is not supported.   | 

### Client
<a name="event-streams-data-campaign-attributes-client"></a>

Includes information about the endpoint that was targeted by the campaign.


| Attribute | Description | 
| --- | --- | 
| client\_id | The ID of the endpoint that the campaign was sent to. | 