**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

#

Set up Amazon Pinpoint to stream app event data through Amazon Kinesis or Amazon Data Firehose

You can set up Amazon Pinpoint to send event data to an Amazon Kinesis stream or an Amazon Data Firehose delivery
stream. Amazon Pinpoint can send event data for campaigns, journeys, and transactional email and SMS
messages.

This section includes information about setting up event streaming programmatically. You
can also use the Amazon Pinpoint console to set up event streaming. For information about setting up
event streaming by using the Amazon Pinpoint console, see [Event stream settings](../userguide/settings-event-streams.md "../userguide/settings-event-streams.md") in the
_Amazon Pinpoint User Guide_.

## Prerequisites

The examples in this section require the following input:

- The application ID of an application that's integrated with Amazon Pinpoint and
  reporting events. For information about how to integrate, see [Integrate Amazon Pinpoint with your application](integrate.md "integrate.md").
- The Amazon Resource Name (ARN) of a Kinesis stream or Firehose delivery stream in
  your AWS account. For information about creating these resources, see [Creating and Managing Streams](../../../streams/latest/dev/working-with-streams.md "../../../streams/latest/dev/working-with-streams.md") in the _Amazon Kinesis Data Streams Developer Guide_ or
  [Creating an Amazon Data Firehose delivery
  stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the _Amazon Data Firehose Developer Guide_.
- The ARN of an AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to send data to the
  stream. For information about creating a role, see [IAM role for streaming events to Kinesis](permissions-streams.md "permissions-streams.md").

## AWS CLI

The following AWS CLI example uses the [put-event-stream](../../../cli/latest/reference/pinpoint/put-event-stream.md "../../../cli/latest/reference/pinpoint/put-event-stream.md") command. This
command configures Amazon Pinpoint to send events to a Kinesis stream:

```
aws pinpoint put-event-stream \
--application-id `projectId` \
--write-event-stream DestinationStreamArn=`streamArn`,RoleArn=`roleArn`
```

## AWS SDK for Java

The following Java example configures Amazon Pinpoint to send events to a Kinesis stream:

```
public PutEventStreamResult createEventStream(AmazonPinpoint pinClient,
        String appId, String streamArn, String roleArn) {

    WriteEventStream stream = new WriteEventStream()
            .withDestinationStreamArn(streamArn)
            .withRoleArn(roleArn);

    PutEventStreamRequest request = new PutEventStreamRequest()
            .withApplicationId(appId)
            .withWriteEventStream(stream);

    return pinClient.putEventStream(request);
}
```

This example constructs a `WriteEventStream` object that stores the ARNs of the Kinesis
stream and the IAM role. The `WriteEventStream` object is passed to a
`PutEventStreamRequest` object to configure Amazon Pinpoint to stream
events for a specific application. The `PutEventStreamRequest` object is
passed to the `putEventStream` method of the Amazon Pinpoint client.

You can assign a Kinesis stream to multiple applications. If you do this, Amazon Pinpoint sends
event data encoded in base64 from each application to the stream, which enables you to
analyze the data as a collection. The following example method accepts a list of
application (app) IDs, and it uses the previous example method,
`createEventStream`, to assign a stream to each application:

```
public List<PutEventStreamResult> createEventStreamFromAppList(
        AmazonPinpoint pinClient, List<String> appIDs,
        String streamArn, String roleArn) {

    return appIDs.stream()
            .map(appId -> createEventStream(pinClient, appId, streamArn,
                    roleArn))
            .collect(Collectors.toList());
}
```

Although you can assign one stream to multiple applications, you can't assign multiple
streams to one application.
