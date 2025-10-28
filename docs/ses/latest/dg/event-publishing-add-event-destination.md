# Step 2: Add an event

destination

Event destinations are places that you publish Amazon SES events to. Each event destination
that you set up belongs to one, and only one, configuration set. When you set up an event
destination with Amazon SES, you choose the AWS service destination, and you specify parameters
associated with that destination.

When you set up an event destination, you can choose to send events to one of the
following AWS services:

- Amazon CloudWatch
- Amazon Data Firehose
- Amazon EventBridge
- Amazon Pinpoint
- Amazon Simple Notification Service (Amazon SNS)
  The event destination that you choose depends on the level of detail you want about the
  events, and the way you want to receive the event information. If you simply want a running
  total of each type of event (for example, so that you can set an alarm when the total gets
  too high), you can use CloudWatch.

If you want detailed event records that you can output to another service such as Amazon OpenSearch Service
or Amazon Redshift for analysis, you can use Firehose.

If you want to receive notifications when certain events occur, you can use Amazon SNS.

###### This section contains the following topics

- [Set up a CloudWatch event
  destination for event publishing](event-publishing-add-event-destination-cloudwatch.md "event-publishing-add-event-destination-cloudwatch.md")
- [Set up a Data Firehose event
  destination for Amazon SES event publishing](event-publishing-add-event-destination-firehose.md "event-publishing-add-event-destination-firehose.md")
- [Set up an Amazon EventBridge
  destination for event publishing](event-publishing-add-event-destination-eventbridge.md "event-publishing-add-event-destination-eventbridge.md")
- [Set up an Amazon Pinpoint event
  destination for event publishing](event-publishing-add-event-destination-pinpoint.md "event-publishing-add-event-destination-pinpoint.md")
- [Set up an Amazon SNS event
  destination for event publishing](event-publishing-add-event-destination-sns.md "event-publishing-add-event-destination-sns.md")
