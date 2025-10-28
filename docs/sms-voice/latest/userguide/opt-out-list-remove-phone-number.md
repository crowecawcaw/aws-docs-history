# Remove a destination phone number from an opt-out list in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to remove destination phone numbers from an opt-out list.
When you remove a phone number that phone number will receive messages
sent from an origination identity that is linked to the opt-out list.

Remove a destination number (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Opt-out lists**.
3. On the **Opt-out lists** page, choose an opt-out list.
4. On the **Opted-out numbers** tab enter the phone
   number to remove and then **Search**.
5. If the phone number is found use it can be removed from the opt-out list by using **Remove number**.
6. In the **Remove opted-out number** window enter `release` and then **Remove number**.

Remove a destination number (AWS CLI)
You can use the [delete-opted-out-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-opted-out-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-opted-out-number.md") command remove a phone number to an opt-out list.

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 delete-opted-out-number \
`>` --opt-out-list-name `optOutListName` \
`>` --opted-out-number `+12065550123`
```

In the preceding example, make the following changes:

- Replace `optOutListName` with the name or
  Amazon Resource Name (ARN) of the opt-out list that you want to add the
  destination identity to.
- Replace `+12065550123` with phone number that
  you want to add to the opt-out list. The phone number must be formatted
  in E.164 format.
