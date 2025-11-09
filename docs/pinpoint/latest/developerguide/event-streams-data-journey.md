**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Journey event data from Amazon Pinpoint

When you publish a journey, Amazon Pinpoint can stream event data for email, SMS, push,
and custom messages that you send from the journey. After you set up event streaming,
Amazon Pinpoint retrieves the data from the destination that you specified during setup for you
to view. For detailed information about the data that Amazon Pinpoint streams for email and SMS
messages, see [Email event data stream from Amazon Pinpoint](event-streams-data-email.md "event-streams-data-email.md") and [SMS event data stream from Amazon Pinpoint](event-streams-data-sms.md "event-streams-data-sms.md").
For information about how to set up event streaming, see [Set up Amazon Pinpoint to stream app event data through Amazon Kinesis or Amazon Data Firehose](event-streams-setup.md "event-streams-setup.md") .

## Journey event example

The JSON object for a journey event contains the data shown in the following
sample.

```
{
   "event_type":"_journey.send",
   "event_timestamp":1572989078843,
   "arrival_timestamp":1572989078843,
   "event_version":"3.1",
   "application":{
      "app_id":"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
      "sdk":{

      }
   },
   "client":{
      "client_id":"d8dcf7c5-e81a-48ae-8313-f540cexample"
   },
   "device":{
      "platform":{

      }
   },
   "session":{

   },
   "attributes":{
      "journey_run_id":"edc9a0b577164d1daf72ebd15example",
      "journey_send_status":"SUCCESS",
      "journey_id":"546401670c5547b08811ac6a9example",
      "journey_activity_id":"0yKexample",
      "journey_activity_type": "EMAIL",
      "journey_send_status_message": "200",
      "journey_send_status_code": "200"
   },
   "client_context":{
      "custom":{
         "endpoint":"{\"ChannelType\":\"EMAIL\",\"EndpointStatus\":\"ACTIVE\",\"OptOut\":\"NONE\",\"Demographic\":{\"Timezone\":\"America/Los_Angeles\"}}"
      }
   },
   "awsAccountId":"123456789012"
}
```

## Journey event attributes

This section defines the attributes that are included in the event stream data that
Amazon Pinpoint generates for a journey.

| Attribute           | Description                                                                                                                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_type`        | The type of event. For journey events, the value for this<br>attribute is always `_journey.send`, which indicates that<br>Amazon Pinpoint executed the journey.                                                                                     |
| `event_timestamp`   | The time when the event was reported, shown as Unix time in<br>milliseconds.                                                                                                                                                                        |
| `arrival_timestamp` | The time when the event was received by Amazon Pinpoint, shown as<br>Unix time in milliseconds.                                                                                                                                                     |
| `event_version`     | The version of the event JSON schema.<br>TipCheck this version in your event-processing application so<br>that you know when to update the application in response to a<br>schema update.                                                           |
| `application`       | Information about the Amazon Pinpoint project that's associated with the event. For more information,<br>see the [Application](#event-streams-data-journey-attributes-application "#event-streams-data-journey-attributes-application") table.      |
| `client`            | Information about the endpoint that's associated with the event. For more information, see the<br>[Client](#event-streams-data-journey-attributes-client "#event-streams-data-journey-attributes-client") table.                                    |
| `device`            | Information about the device that reported the event. For<br>journeys, this object is empty.                                                                                                                                                        |
| `session`           | Information about the session that generated the event. For<br>journeys, this object is empty.                                                                                                                                                      |
| `attributes`        | Attributes that are associated with the journey and journey<br>activity that generated the event. For more information, see the<br>[Attributes](#event-streams-data-journey-attributes-attrs "#event-streams-data-journey-attributes-attrs") table. |
| `client_context`    | Contains a `custom` object, which contains an<br>`endpoint` property. The `endpoint` property<br>contains the contents of the endpoint record for the endpoint that's<br>associated with the event.                                                 |
| `awsAccountId`      | The ID of the AWS account that was used to execute the<br>journey.                                                                                                                                                                                  |

### Application

Includes information about the Amazon Pinpoint project that's associated with the
event.

| Attribute | Description                                                              |
| --------- | ------------------------------------------------------------------------ |
| `app_id`  | The unique ID of the Amazon Pinpoint project that reported the<br>event. |
| `sdk`     | The SDK that was used to report the event.                               |

### Client

Includes information about the endpoint that's associated with the event.

| Attribute   | Description             |
| ----------- | ----------------------- |
| `client_id` | The ID of the endpoint. |

### Attributes

Includes information about the journey that generated the event.

| Attribute                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `journey_run_id`              | The unique ID of the journey run that generated the event.<br>Amazon Pinpoint generates and assigns this ID automatically to each new<br>run of a journey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `journey_send_status`         | Indicates the delivery status of the message that's associated<br>with the event. Possible values include:<br>• **SUCCESS** – The<br>message was successfully sent to the endpoint.<br>• **FAILURE** – The<br>message wasn't sent to the endpoint because an error<br>occurred.<br>• **CUSTOM_DELIVERY_FAILURE** – Custom<br>delivery failed.<br>• **FAILURE_PERMANENT**<br>– A permanent failure occurred when sending to the<br>endpoint.<br>TipYou can filter on events with **FAILURE_PERMANENT\*<br>• status<br>and `journey_send_status_code` set to 403<br>to determine if there is an access policy and role<br>violation. For outbound campaigns with voice, these<br>exceptions are typical to instances when the connect<br>campaign execution role binding Amazon Pinpoint journeys to<br>Amazon Connect campaigns is inadvertently deleted for<br>in-flight journey executions.<br>• **THROTTLED** –<br>Sending was throttled.<br>• **UNSUPPORTED_CHANNEL**<br>– Channel is not supported.<br>• **DAILY_CAP** – The<br>message wasn't sent to the endpoint because sending the<br>message would exceed the maximum number of messages that<br>the journey or project can send to a single endpoint<br>during a 24-hour period.<br>• **QUIET_TIME** –<br>The message wasn't sent because of quiet-time<br>restrictions for the journey or project.<br>• **QUIET_TIME_MISSING_TIMEZONE\*\* – The<br>message wasn't sent because time zone estimation<br>couldn't estimate a time zone for the endpoint and<br>quiet-time is enabled. |
| `journey_id`                  | The unique ID of the journey that generated the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `journey_activity_id`         | The unique ID of the journey activity that generated the<br>event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `journey_activity_type`       | The event's journey activity type. This can be **EMAIL**, **SMS**, **PUSH**,<br>**CONTACT_CENTER**, or<br>**CUSTOM**.<br>Note**VOICE\*<br>• is not a supported journey<br>activity type.The `journey_activity_type` field is not present when<br>`journey_send_status` is set to<br>**QUIET_TIME_WAIT_FINISHED\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `journey_send_status_message` | The description of the status of the send event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `journey_send_status_code`    | The HTTP status code of the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
