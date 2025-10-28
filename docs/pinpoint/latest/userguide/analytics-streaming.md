**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Streaming events with Amazon Pinpoint

Amazon Pinpoint can stream engagement and application usage data, known as _event
data_, to supported AWS services that provide more options for analysis and
storage. _Event data_ can be used to troubleshoot issues by viewing
individual events or to view individual customer events, see [Streaming
Amazon Pinpoint events to Kinesis](../developerguide/event-streams.md "../developerguide/event-streams.md") in the _Amazon Pinpoint Developer Guide_.

After you integrate your application with Amazon Pinpoint, it reports events, such as the number
of sessions started by users. Amazon Pinpoint provides this data in the analytics charts and metrics
for that application in the console. The analytics data also shows campaign events generated
by Amazon Pinpoint, such as the number of devices that a campaign sent messages to.

Amazon Pinpoint retains this data for 90 days. To keep this data for an indefinite period of time
or to analyze it with custom queries and tools, you can configure Amazon Pinpoint to send event data
to Amazon Kinesis.

###### Topics in this section:

- [About Amazon Kinesis](#analytics-streaming-about-kinesis "#analytics-streaming-about-kinesis")
- [Streaming Amazon Pinpoint events to Kinesis](#analytics-streaming-kinesis "#analytics-streaming-kinesis")

## About Amazon Kinesis

The Kinesis platform offers services that you can use to load and analyze streaming data on
AWS. You can configure Amazon Pinpoint to send application, campaign, and journey events to
Amazon Kinesis Data Streams or Amazon Data Firehose. By streaming your events, you enable more flexible options for data
analysis, such as:

- Converging the events from multiple applications into one stream so that you can
  analyze this data as a collection.
- Analyzing events with AWS query services. For example, you can use Amazon Managed Service for Apache Flink to
  run SQL queries against streaming data.

### About Amazon Kinesis Data Streams

Amazon Kinesis Data Streams is a service that you can use to build custom applications that process or
analyze your streaming data. For example, streaming your events to Kinesis Data Streams is useful if
you want to use event data in custom dashboards, generate alerts based on events, or
dynamically respond to events.

For more information, see the [Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev.md "../../../streams/latest/dev.md").

### About Amazon Data Firehose

Amazon Data Firehose is a service that you can use to deliver your streaming data to AWS data
stores, including Amazon Simple Storage Service (Amazon S3), Amazon Redshift, or Amazon OpenSearch Service (OpenSearch Service). For example, streaming your
events to Firehose is useful if you want to:

- Use your own analytics applications and tools to analyze events in Amazon S3, Amazon Redshift,
  or OpenSearch Service.
- Send your events to Amazon S3 so that you can write SQL queries on this data with
  Amazon Athena.
- Back up your event data for long-term storage in Amazon S3.

For more information, see the [Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md").

## Streaming Amazon Pinpoint events to Kinesis

The Kinesis platform offers services that you can use to load and analyze streaming data on
AWS. You can configure Amazon Pinpoint to send application, campaign, and journey events to
Amazon Kinesis Data Streams for processing by external applications or third-party analytics tools. You can
also configure Amazon Pinpoint to stream this event data to AWS data stores (such as Amazon Redshift) using
Amazon Data Firehose.

### Prerequisites

Before you complete the procedure in this section, create an Amazon Kinesis stream or a
Firehose delivery stream in the same account in which you use Amazon Pinpoint. To learn more about
creating Kinesis streams, see [Creating and updating data streams](../../../streams/latest/dev/working-with-streams.md "../../../streams/latest/dev/working-with-streams.md") in the
_Amazon Kinesis Data Streams Developer Guide_. To learn more about creating Firehose delivery
streams, see [Creating an Amazon Data Firehose delivery
stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the _Amazon Data Firehose Developer Guide_.

You can optionally create an IAM role that grants permission to send data to your
stream. If you don't create this role, Amazon Pinpoint can create one for you. For more
information about creating this policy manually, see [IAM role for streaming events to
Kinesis](../developerguide/permissions-streams.md "../developerguide/permissions-streams.md") in the _Amazon Pinpoint Developer Guide_.

### Setting up event streaming

Complete the following steps in Amazon Pinpoint to set up event streaming.

###### Note

If you haven't already created an Amazon Kinesis stream, go to the Amazon Kinesis console
at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis"). For more information about creating streams, see the
[Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev.md "../../../streams/latest/dev.md") or the [Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md").

Verify you have the permissions to setup and send to the stream. For more information about permissions see [IAM role for streaming events to Kinesis](../developerguide/permissions-streams.md "../developerguide/permissions-streams.md")

###### To set up event streaming

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you want to set up data streaming for.
3. In the navigation pane, under **Settings**, choose
   **Event stream**.
4. In the **Services** section, choose
   **Edit**.
5. Choose **Stream to Amazon Kinesis**.
6. Under **Choose a stream type**, choose one of the following options:
   - **Send events to an Amazon Kinesis Data Stream** – Choose this
     option if you want to send Amazon Pinpoint event data to an external application for
     analysis.
   - **Send events to an Amazon Data Firehose stream** –
     Choose this option if you want to send event data to an AWS data store,
     such as Amazon Redshift.

7. For **Amazon Kinesis stream**, choose the Amazon Kinesis stream that you want to use to export the
   data.

###### Note

If you haven't already created an Amazon Kinesis stream, go to the Amazon Kinesis console
at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis"). For more information about creating streams, see the
[Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev.md "../../../streams/latest/dev.md") or the [Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md"). 8. Under **IAM role**, choose one of the following options:

    * **Use an existing role** – Choose this option to
     have Amazon Pinpoint assume an IAM role that already exists in your account. The
     role that you select must allow the `firehose:PutRecordBatch` action.
     For an example of a policy that allows this action, see [Permissions Policies](../developerguide/permissions-streams.md#permissions-streams-permissionspolicies "../developerguide/permissions-streams.md#permissions-streams-permissionspolicies") in the
     *Amazon Pinpoint Developer Guide*.
    * **Automatically create a role** – Choose this
     option to automatically create an IAM role with the required permissions.
     This role authorizes Amazon Pinpoint to send data to the stream that you chose in step
     7.

9. Choose **Save**.

As Amazon Pinpoint receives events for your project, it sends this
data to your Kinesis stream. For information about the data that Amazon Pinpoint sends for an
event, see [Streaming Amazon Pinpoint Events to Kinesis](../developerguide/event-streams.md "../developerguide/event-streams.md") in the _Amazon Pinpoint Developer Guide_.
