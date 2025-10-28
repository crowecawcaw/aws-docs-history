# Set an SMS, MMS or voice spending limit in AWS End User Messaging SMS

In AWS End User Messaging SMS there are spending limits for each messaging channel.

The _account limit_ is the maximum amount, in US dollars,
that you can spend each month sending messages through a channel. When you reach your
account limit, AWS End User Messaging SMS stops sending your messages and, to send more messages that month,
you need to request a spending limit increase. When you request a spending limit change to
either your SMS or MMS _account limit_ both your SMS and
MMS _account limit_ are set to the new requested limit. MMS
and SMS have separate _enforced limit_. For example you
could set you MMS _enforced limit_ to $10 and SMS _enforced limit_ to $5. To change your _account limit_, see [Requesting a spending quota
change](awssupport-spend-threshold.md "awssupport-spend-threshold.md").

The _enforced limit_ is an optional spending limit, in US
dollars, between $1 and the account limit. If you don't specify an enforced limit, you can
spend up to your account limit. When you reach your enforced limit, AWS End User Messaging SMS stops sending
your messages. To resume sending messages, you can adjust your enforced limit through the
console or AWS CLI. For example, if you set your SMS account limit to $100 and your enforced
limit to $50, then once you've spent $50, AWS End User Messaging SMS stops sending your messages until you
raise your enforced limit.

The _remaining limit_ is how much you have spent for the
current month sending messages.

You can adjust your enforced limit to increase or decrease your spending without having to
contact Support.

To set up billing alarms for your spending, see [Monitoring spending](monitor-spending.md "monitor-spending.md"). For more
information about configuring the AWS CLI, see [Configure the
AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For more information about SMS, MMS, or origination identity pricing, see [AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

View your spending limits (console)

###### View all of your spending limits

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. On the **Overview** page, navigate to **SMS
   Spending status**.
3. In the **SMS Spending status** pane, you can view
   your **Account limit**, **Enforced
   limit**, and **Remaining limit**.

If your **Enforced limit** displays a
`–`, it means the limit is not set.

View your enforced spending limit (AWS CLI)
You can use the `describe-spend-limits` command to view all of your
channel spending limits.

```
aws pinpoint-sms-voice-v2 describe-spend-limits
```

When the command completes, it returns the **Account limit**
and **Enforced limit** for each channel.

Change your enforced spending limit (Console)

###### Change a spending limit

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. On the **Overview** page, navigate to **SMS
   Spending status**.
3. In the **SMS Spending status** pane, choose
   **Edit** for the channel for which you want to
   change the **Enforced limit**.
4. In the **Edit spending limits** window,
   choose:
   - **Update enforced spend limit** – Enter
     a new **Enforced limit** between one and your
     account limit.
   - **Default to the max send limit** –
     Choose this option to adjust your enforced limit to your account
     limit.

5. Choose **Save changes**.

Set enforced spending limit (AWS CLI)
You can use the `set-text-message-spend-limit-override` command to set the
enforced limit for the SMS channel. For the voice channel, use the `set-voice-message-spend-limit-override` command.

The following command shows how to increase the enforced limit for the SMS
channel.

```
aws pinpoint-sms-voice-v2 set-text-message-spend-limit-override --monthly-limit `NewEnforcedLimit`
```

Replace `NewEnforcedLimit` with a value between one
and the account limit of the SMS channel.

When the command completes, it returns the value of your new set limit.

Remove an enforced spending limit (AWS CLI)
You can use the `delete-text-message-spend-limit-override` command to set
your enforced limit to the account limit for the SMS channel. For the voice
channel, use the `delete-voice-message-spend-limit-override`
command.

The following command shows how to remove the enforced limit for the SMS
channel.

```
aws pinpoint-sms-voice-v2 delete-text-message-spend-limit-override
```

When the command completes, it returns the value of your enforced
limit.
