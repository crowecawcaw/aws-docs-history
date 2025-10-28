# Delete an

Amazon CloudWatch event destination in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to delete a CloudWatch event destination.

Delete an CloudWatch event destination (Console)
The process for deleting an event destination is the same regardless of the type of
event destination that you want to delete.

###### To delete an CloudWatch event destination in the Console

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Configuration sets**.
3. On the **Configuration sets** page, choose the
   configuration set to remove an event destination from.
4. In the **All destinations** section choose an event destination and then choose **Delete**.

Delete an CloudWatch event destination (AWS CLI)You can use the [delete-event-destination](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-event-destination.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-event-destination.md") command to delete an event destination.

The process for deleting an event destination is the same regardless of the type of
event destination that you want to delete.

###### To delete an CloudWatch event destination in the AWS CLI

- At the command line, run the following command:

```
`$` aws pinpoint-sms-voice-v2 delete-event-destination \
`>` --event-destination-name `eventDestinationName` \
`>` --configuration-set-name `configurationSetName`
```

In the preceding command, make the following changes:

    + Replace `eventDestinationName` with the name
     or Amazon Resource Name (ARN) of the event destination that you want to
     delete.
    + Replace `configurationSetName` with the name
     or ARN of the configuration set that the event destination is associated
     with.
