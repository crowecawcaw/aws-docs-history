

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting journeys
<a name="journeys-troubleshooting"></a>

Verify that logging is turned on to assist in identifying the cause of failure. For more information on logging, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging) and [Journey events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-journey.html).

## Event based journey isn't triggered when using a PutEvents request
<a name="troubleshooting-journey-event"></a>

****Issues and solutions****
+ Verify that the configured **Journey limits** are not being exceeded:
  + **Maximum daily messages per endpoint**
  + **Maximum number of messages an endpoint can receive from the journey**
  +  **Maximum number of journey messages per second**
  + **Maximum entries per endpoint** 
+ Ensure that the active number of event triggered journeys does not exceed the provisioned threshold. For more information, see [Quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html). 
+ Verify that all components of the [PutEvents](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html) API request are complete, including [Event Component](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html#apps-application-id-events-model-event) and [Endpoint Component](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-events.html#apps-application-id-events-model-publicendpoint).
+ Verify that the specific journey is in the same application as the one in the PutEvent request. 
+ Verify that the correct event is configured to activate your journey. You can confirm this configuration in the [Journey entry condition](https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-entry-activity.html#journeys-entry-activity-event-triggered).
+ Event-driven journeys are not conducive to Contact Center use cases because of the limited life span for dial operations is 3 minutes.
+ You can use the following example request to activate a journey using “TestEvent” as the entry condition.

  ```
  aws pinpoint put-events --application-id 7149cbb8XXXXXXXX --events-request file://PutEvents.json
  file://PutEvents.json 
  {
      "BatchItem": {
          "ExampleEndpointID": {
              "Endpoint": {
                  "User": {
                      "UserId": "10107"
                  }, 
                  "ChannelType": "EMAIL",
                  "Address": "johndoe@example.com"
                     
              },
              "Events": {
                  "JourneyEvent": {
                      "EventType": "TestEvent",
                      "Timestamp": "2019-02-10T19:48:57+00:00"
                  }
              }
          }
      }
  }
  ```

## All journey participants go through ‘No’ branch during ‘Yes/No’ split activity
<a name="troubleshooting-journey-split"></a>

****Issues and solutions****
+ This error can occur when no wait time is configured. Send events are evaluated immediately, which results in moving all participants to the 'No' branch. 
  + To resolve this issue, verify that some wait time is configured after the condition evaluation.
+ Yes/No splits based on an event criterion and following custom AWS Lambda activities have an implicit wait time of 15 minutes to accrue and process the event outcomes.
+ Yes/No splits based on an event criterion and following channel activities (SMS, EMAIL, PNS) have a wait time of 1 hour to accrue and process the delivery event statuses for channel message deliveries.
+ Only standard events specific to channel delivery statuses are supported for Yes/No splits.