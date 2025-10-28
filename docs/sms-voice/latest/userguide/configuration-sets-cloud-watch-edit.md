# Edit an

Amazon CloudWatch event destination in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to edit a CloudWatch event destination.

Update event destination (Console)
To update an event destination using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Configuration sets**.
3. On the **Configuration sets** page, choose the
   configuration set to edit.
4. On the **Event settings** tab, choose a Amazon CloudWatch
   event destination and then **Edit**.
5. For **IAM role arn** enter the ARN of the IAM
   role. For more information about the IAM role arn, see [IAM policy for
   Amazon CloudWatch](configuration-sets-cloud-watch-creating-role.md "configuration-sets-cloud-watch-creating-role.md").
6. For **Log group arn** enter the ARN of the
   Amazon CloudWatch log group to deliver the events to.
7. Under **Event types**, choose:
   - **All SMS events (Recommended)** –
     Choose this option to send all SMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon CloudWatch.
   - **Custom SMS events** – Choose this
     option choose specific SMS events to send to CloudWatch. To edit
     the list of events choose **Edit SMS event
     selection**. On **Edit SMS event
     selection** check only the events you want to
     send to Amazon CloudWatch. Choose **Save
     selection**.
   - **All voice events (Recommended)**
     – Choose this option to send all voice events listed
     in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon CloudWatch.
   - **Custom voice events** – Choose
     this option choose specific voice events to send to CloudWatch. To
     edit the list of events choose **Edit voice event
     selection**. On **Edit voice event
     selection** check only the events you want to
     send to Amazon CloudWatch. Choose **Save
     selection**.
   - **All MMS events (Recommended)** –
     Choose this option to send all MMS events listed in [Event types](configuration-sets-event-types.md "configuration-sets-event-types.md") to
     Amazon CloudWatch.
   - **Custom MMS events** – Choose this
     option choose specific MMS events to send to CloudWatch. To edit
     the list of events choose **Edit MMS event
     selection**. On **Edit MMS event
     selection** check only the events you want to
     send to Amazon CloudWatch. Choose **Save
     selection**.

8. Choose **Edit event**.

Update event destination AWS CLI)
You can use the [update-event-destination](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-event-destination.md") command to update an event
destination.

The procedure for updating a CloudWatch event destination is similar to the
process for creating an event destination. At the command line, run the
following command:

```
`$` aws pinpoint-sms-voice-v2 update-event-destination \
`>` --event-destination-name `eventDestinationName` \
`>` --configuration-set-name `configurationSet` \
`>` --matching-event types `eventTypes` \
`>` --cloud-watch-logs-destination IamRoleArn=arn:aws:iam::`111122223333`:role/`CWLSMSRole`,LogGroupArn=arn:aws:logs:`us-east-1`:`111122223333`:log-group:`MyCWLLogGroup`
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
  in [Event types for SMS, MMS, and
  voice](configuration-sets-event-types.md "configuration-sets-event-types.md").
- Replace the value of `LogGroupArn` with the ARN of the
  CloudWatch group that you want to send events to.
