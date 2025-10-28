# Add a destination phone number to an opt-out list in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to add a destination phone number to an opt-out list. When
you add a phone number to an opt-out list that phone number will no longer receive messages
sent from an origination identity that is linked to the opt-out list.

Add a destination number (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Opt-out lists**.
3. On the **Opt-out lists** page, choose an opt-out
   list.
4. On the **Opted-out numbers** tab, choose
   **Add number**.
5. On the **Add opt-out number** page, for
   **Destination number** enter in the phone number to
   add to the opt-out list. The phone number must be in E.164 format, for
   example +12065550150.
6. Choose **Add number**

Add a destination number (AWS CLI)
You can use the [put-opted-out-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-opted-out-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-opted-out-number.md") command add a phone number to an opt-out
list.

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 put-opted-out-number \
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
