# Edit an Amazon SNS event destination in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to edit an Amazon SNS event destination.

Update an Amazon SNS event destination (Console)
To update an AWS End User Messaging SMS event destination using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Configuration sets**.
3. On the **Configuration sets** page, choose the
   configuration set to add an event destination to.
4. On the **Configuration sets** page, choose the
   configuration set to edit.
5. On the **Configuration set details** page, choose
   a Amazon SNS event destination and then **Edit**.
6. From the **Destination type** dropdown choose
   Amazon SNS.
   1. **New Amazon SNS topic** – Choose this
      option, AWS End User Messaging SMS creates a topic in your account. The topic is
      automatically created with all of the required permissions.
      For more information on Amazon SNS topics see [Configuring Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
   2. **Existing Amazon SNS topic** – Choose
      this option if you have an existing Amazon SNS topic in the
      **Topic arn** dropdown.

7. Under **Event types**, choose:
   - **All SMS events (Recommended)** –
     Choose this option to send all SMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom SMS events** – Choose this
     option choose specific SMS events to send to Amazon SNS. To edit
     the list of events choose **Edit SMS event
     selection**. On **Edit SMS event
     selection** check only the events you want to
     send to Amazon SNS. Choose **Save
     selection**.
   - **All voice events (Recommended)**
     – Choose this option to send all voice events listed
     in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom voice events** – Choose
     this option choose specific voice events to send to Amazon SNS.
     To edit the list of events choose **Edit voice event
     selection**. On **Edit voice event
     selection** check only the events you want to
     send to Amazon SNS. Choose **Save
     selection**.
   - **All MMS events (Recommended)** –
     Choose this option to send all MMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon SNS.
   - **Custom MMS events** – Choose this
     option choose specific MMS events to send to Amazon SNS. To edit
     the list of events choose **Edit MMS event
     selection**. On **Edit MMS event
     selection** check only the events you want to
     send to Amazon SNS. Choose **Save
     selection**.

8. Choose **Edit event**.

Update an Amazon SNS event destination (AWS CLI)
You can use the [update-event-destination](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md") command to update an event
destination.

The procedure for updating an Amazon SNS event destination is similar to the
process for creating an event destination.

###### To update an Amazon SNS event destination in the AWS CLI

- At the command line, run the following command:

```
`$` aws pinpoint-sms-voice-v2 update-event-destination \
`>` --event-destination-name `eventDestinationName` \
`>` --configuration-set-name `configurationSet` \
`>` --matching-event types `eventTypes` \
`>` --sns-destination TopicArn=arn:aws:sns:`us-east-1`:`111122223333`:`snsTopic`
```

In the preceding command, make the following changes:

    + Replace `eventDestinationName`
     with a name of the event destination that you want to
     modify.
    + Replace `configurationSet` with
     the name of the configuration set that you want to associate
     the event destination with. You can associate the event
     destination with a different configuration set.
    + Replace `eventTypes` with one or
     more of the event types listed in [Event types for SMS, MMS, and
     voice](configuration-sets-event-types.md "configuration-sets-event-types.md").
    + Replace the value of `TopicArn` with the Amazon
     Resource Name (ARN) of the Amazon SNS topic that you want to send
     events to.
