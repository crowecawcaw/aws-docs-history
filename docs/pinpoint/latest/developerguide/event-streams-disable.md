

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Delete an event stream from Amazon Pinpoint
<a name="event-streams-disable"></a>

If you assign a Kinesis stream to an application, you can disable event streaming for that application. Amazon Pinpoint stops streaming the events to Kinesis, but you can view event analytics by using the Amazon Pinpoint console.

## AWS CLI
<a name="event-streams-disable-cli"></a>

Use the [`delete-event-stream`](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/delete-event-stream.html) command:

```
aws pinpoint delete-event-stream --application-id {{application-id}}
```

## AWS SDK for Java
<a name="event-streams-disable-java"></a>

Use the [`deleteEventStream`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/pinpoint/model/DeleteEventStreamRequest.html) method of the Amazon Pinpoint client:

```
pinClient.deleteEventStream(new DeleteEventStreamRequest().withApplicationId(appId));
```