# Change a pool's opt-out list in AWS End User Messaging SMS

An _opt-out list_ is list of destination phone numbers that should not
have messages sent to them. When you send SMS messages, destination identities are
automatically added to the opt-out list if they reply to your origination number with the
keyword STOP (unless you enable the self-managed opt-out option). If you attempt to send a
message to a destination number that is on an opt-out list, and the opt-out list is
associated with the pool used to send the message, AWS End User Messaging SMS doesn't attempt to send the
message.

By default, when a pool is created it is assigned to the _Default_
opt-out list. Pools can share the same opt-out list. When you change a pools opt-out
list any recipients who previously opt-out might not be in the new list and start to
receive messages. For more information on adding or removing destination phone numbers
from an opt-out list, see [Add a destination phone number to an opt-out list in AWS End User Messaging SMS](opt-out-list-add-phone-number.md "opt-out-list-add-phone-number.md").

Change opt-out list (Console)
To change the opt-out list using the AWS End User Messaging SMS console, follow these steps:

###### Change opt-out list

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone pools**.
3. On the **Phone Pools** page, choose the
   pool.
4. On the **Opt-out list** tab, choose
   **Edit settings**.
   - **Create a new opt-out list** – Create a new empty opt-out
     list and enter a friendly name.
   - **Choose an existing opt-out list**
     – Choose a previously created opt-out list from the
     dropdown.

5. (Optional) To enable self-managed opt-outs choose **Enable
   self-managed opt-out**.
6. Choose **Save changes**.

Change opt-out list (AWS CLI)
You can use the [update-pool](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-pool.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-pool.md") command to change the opt-out list used by the pool.

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 update-pool --pool-id `poolid` --opt-out-list-name `OptOutListName`
```

In the preceding command, make the following changes:

- Replace `poolid` with the poolID or
  Amazon Resource Name (ARN) of the pool.
- Replace `OptOutListName` with the Amazon Resource Name (ARN)
  or opt-out list name.
