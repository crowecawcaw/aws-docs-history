# Edit an Amazon Data Firehose event destination in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to edit an Amazon Data Firehose event destination.

Update Amazon Data Firehose event destination (Console)
To update an Amazon Data Firehose event destination using the AWS End User Messaging SMS console, follow
these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Configuration sets**.
3. On the **Configuration sets** page, choose the
   configuration set to add an event destination to.
4. On the **Configuration sets** page, choose the
   configuration set to edit.
5. On the **Configuration set details** page, choose
   a Amazon Data Firehose event destination and then
   **Edit**.
6. For **IAM role arn** enter the ARN of the IAM
   role. For more information on the IAM role arn, see [IAM policy for
   Amazon Data Firehose](configuration-sets-kinesis-creating-role.md "configuration-sets-kinesis-creating-role.md").
7. For **Delivery stream arn** enter the ARN of the
   Amazon Data Firehose log group to deliver the events to.
8. Under **Event types**, choose:
   - **All SMS events (Recommended)** –
     Choose this option to send all SMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon Data Firehose.
   - **Custom SMS events** – Choose this
     option choose specific SMS events to send to CloudWatch. To edit
     the list of events choose **Edit SMS event
     selection**. On **Edit SMS event
     selection** check only the events you want to
     send to Amazon Data Firehose. Choose **Save
     selection**.
   - **All voice events (Recommended)**
     – Choose this option to send all voice events listed
     in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon Data Firehose.
   - **Custom voice events** – Choose
     this option choose specific voice events to send to
     Amazon Data Firehose. To edit the list of events choose **Edit
     voice event selection**. On **Edit
     voice event selection** check only the events
     you want to send to Amazon Data Firehose. Choose **Save
     selection**.
   - **All MMS events (Recommended)** –
     Choose this option to send all MMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon Data Firehose.
   - **Custom MMS events** – Choose this
     option choose specific MMS events to send to CloudWatch. To edit
     the list of events choose **Edit MMS event
     selection**. On **Edit MMS event
     selection** check only the events you want to
     send to Amazon Data Firehose. Choose **Save
     selection**.

9. Choose **Edit event**.

Update Amazon Data Firehose event destination (AWS CLI)
You can use the [update-event-destination](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md") command to update an event
destination.

The procedure for updating a Amazon Data Firehose event destination is similar to the
process for creating an event destination.

```
`$` aws pinpoint-sms-voice-v2 create-event-destination \
`>` --event-destination-name `eventDestinationName` \
`>` --configuration-set-name `configurationSet` \
`>` --matching-event-types `eventTypes` \
`>` --kinesis-firehose-destination IamRoleArn=arn:aws:iam::`111122223333`:role/`AKFSMSRole`,DeliveryStreamArn=arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/`MyDeliveryStream`
```

In the preceding command, make the following changes:

- Replace `eventDestinationName` with a
  name of the event destination that you want to modify.
- Replace `configurationSet` with the name
  of the configuration set that you want to associate the event
  destination with. You can associate the event destination with a
  different configuration set.
- Replace `eventTypes` with one of the
  event types listed in [Event types for SMS, MMS, and
  voice](configuration-sets-event-types.md "configuration-sets-event-types.md").
- Replace the value of `IamRoleArn` with the Amazon
  Resource Name (ARN) of an IAM role that has the policies described
  in [IAM policy for
  Amazon Data Firehose](configuration-sets-kinesis-creating-role.md "configuration-sets-kinesis-creating-role.md").
- Replace the value of `DeliveryStreamArn` with the ARN
  of the Amazon Data Firehose stream that you want to send events to.
