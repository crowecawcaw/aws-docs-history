**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Delete an event stream from Amazon Pinpoint

If you assign a Kinesis stream to an application, you can disable event streaming for
that application. Amazon Pinpoint stops streaming the events to Kinesis, but you can view event
analytics by using the Amazon Pinpoint console.

## AWS CLI

Use the [`delete-event-stream`](../../../cli/latest/reference/pinpoint/delete-event-stream.md "../../../cli/latest/reference/pinpoint/delete-event-stream.md") command:

```
aws pinpoint delete-event-stream --application-id `application-id`
```

## AWS SDK for Java

Use the [`deleteEventStream`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/pinpoint/model/DeleteEventStreamRequest.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/pinpoint/model/DeleteEventStreamRequest.html") method of the Amazon Pinpoint client:

```
pinClient.deleteEventStream(new DeleteEventStreamRequest().withApplicationId(appId));
```
