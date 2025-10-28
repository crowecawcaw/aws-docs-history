# Create an Amazon SNS event destination in AWS End User Messaging SMS

Before you can create an Amazon SNS event destination, you must first create an Amazon SNS
topic. For more information about creating Amazon SNS topics, see [Creating a topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the
_Amazon Simple Notification Service Developer Guide_.

You must also have already setup a configuration set to associate the event
destinations with, see [Configuration sets in AWS End User Messaging SMS](configuration-sets.md "configuration-sets.md").

Create an Amazon SNS event destination (Console)
To create an Amazon SNS event destination using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Configuration sets**.
3. On the **Configuration sets** page, choose the
   configuration set to add an event destination to.
4. On the **Configuration set details** page, choose
   **Add destination event**.
5. Under the **Event details** section, enter a
   name.
6. From the **Destination type** dropdown choose
   Amazon SNS.
   1. **New Amazon SNS topic** – Choose this
      option, for AWS End User Messaging SMS to create a topic in your account. The
      topic is automatically created with all of the required
      permissions. For more information on Amazon SNS topics see [Configuring Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
   2. **Existing Amazon SNS topic** – Choose this
      option if you have an existing Amazon SNS topic in the
      **Topic arn** dropdown.

7. Under **Event types**, choose:
   - **All SMS events (Recommended)** –
     Choose this option to send all SMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom SMS events** – Choose t
     specific SMS events to send to Amazon SNS. To edit the list of
     events choose **Edit SMS event selection**.
     On **Edit SMS event selection** check only
     the events you want to send to Amazon SNS. Choose **Save
     selection**.
   - **All voice events (Recommended)**
     – Choose this option to send all voice events listed
     in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom voice events** – Choose t
     specific voice events to send to Amazon SNS. To edit the list of
     events choose **Edit voice event
     selection**. On **Edit voice event
     selection** check only the events you want to
     send to Amazon SNS. Choose **Save
     selection**.
   - **All MMS events (Recommended)** –
     Choose this option to send all MMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom MMS events** – Choose
     specific MMS events to send to Amazon SNS. To edit the list of
     events choose **Edit MMS event selection**.
     On **Edit MMS event selection** check only
     the events you want to send to Amazon SNS. Choose **Save
     selection**.

8. Choose **Create event**.

Create an Amazon SNS event destination (AWS CLI)
You can use the [create-event-destination](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-event-destination.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-event-destination.md") command to create an event
destination.

```
`$` aws pinpoint-sms-voice-v2 create-event-destination \
`>` --event-destination-name `eventDestinationName` \
`>` --configuration-set-name `configurationSet` \
`>` --matching-event-types `eventTypes` \
`>` --sns-destination TopicArn=arn:aws:sns:`us-east-1`:`111122223333`:`snsTopic`
```

In the preceding command, make the following changes:

- Replace `eventDestinationName` with a
  descriptive name for the event destination.
- Replace `configurationSet` with the name
  of the configuration set that you want to associate the event
  destination with.
- Replace `eventTypes` with one of the
  event types listed in [Event types for SMS, MMS, and
  voice](configuration-sets-event-types.md "configuration-sets-event-types.md").
- Replace the value of `TopicArn` with the Amazon
  Resource Name (ARN) of the Amazon SNS topic that you want to send events
  to.
