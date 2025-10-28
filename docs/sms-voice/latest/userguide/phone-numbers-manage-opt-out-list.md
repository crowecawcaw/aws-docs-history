# Change a phone number's opt-out list in AWS End User Messaging SMS

An _opt-out list_ is list of destination phone numbers that should not
have messages sent to them. When you send SMS or MMS messages, destination identities are
automatically added to the opt-out list if they reply to your origination number with the
keyword STOP (unless you enable the self-managed opt-out option). If you attempt to send a
message to a destination number that is on an opt-out list, and the opt-out list is
associated with the phone number used to send the message, AWS End User Messaging SMS doesn't attempt to send the
message.

By default, when a phone number is created it is assigned to the
_Default_ opt-out list. For more information on adding a destination phone numbers from an opt-out list, see [Add a destination phone number to an opt-out list in AWS End User Messaging SMS](opt-out-list-add-phone-number.md "opt-out-list-add-phone-number.md").

Create or change opt-out list (Console)
To change the opt-out list using the AWS End User Messaging SMS console, follow these
steps:

###### Create or change an opt-out list

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone numbers**.
3. On the **Phone numbers** page, choose the phone
   number.
4. On the **Opt-out list** tab, choose the
   **Edit settings** button.
5. For **Opt-out list**, choose either:
   - **Create a new opt-out list** –
     Create a new empty opt-out list. In **List
     name** enter a name for the opt-out
     list.
   - **Choose an existing opt-out list**
     – Choose a previously created opt-out list from the
     dropdown.

6. Choose **Save changes**.

Change an opt-out list (AWS CLI)
You can use the [update-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md") command to change the opt-out list
used by the phone number.

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 update-phone-number --phone-number-id `PhoneNumberid` --opt-out-list-name `OptOutListName`
```

In the preceding command, make the following changes:

- Replace `PhoneNumberid` with the
  PhoneNumberId or Amazon Resource Name (ARN) of the phone
  number.
- Replace `OptOutListName` with the Amazon
  Resource Name (ARN) or opt-out list name.
