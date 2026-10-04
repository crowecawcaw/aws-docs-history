

# Move out of the sandbox
<a name="nx-sms-scale-sandbox"></a>

New AWS End User Messaging accounts are placed into an SMS and MMS or voice sandbox. The sandbox protects both customers and recipients from fraud and abuse, and it creates a safe environment for test and development. While your account is in the sandbox, you have access to all of the features of AWS End User Messaging, with restrictions on the volume and destinations of the messages that you can send. To send unrestricted production traffic, you request production access.

**Topics**
+ [Sandbox restrictions](#nx-sms-scale-sandbox-restrictions)
+ [Move to production](#nx-sms-scale-sandbox-production)
+ [Set a spending limit](#nx-sms-scale-sandbox-spend-limit)
+ [Request a spending quota change](#nx-sms-scale-sandbox-spend-quota)

## Sandbox restrictions
<a name="nx-sms-scale-sandbox-restrictions"></a>

While your account is in the sandbox, you can use all of the SMS sending methods in the AWS End User Messaging console or the `SendTextMessage` API. To send an MMS message, you must use the `SendMediaMessage` API. The following restrictions are in place while your account is in the sandbox:
+ You have a monthly SMS spending limit of $1.00 (USD).
+ You have a monthly MMS spending limit of $1.00 (USD).
+ You can send SMS and MMS messages only to verified destination phone numbers. You can add up to 10 verified numbers.
+ The rules and restrictions for sending SMS and MMS messages to each destination country apply. For example, to send a message to a recipient in the United States, you must first request and register a US number.
+ To verify that you own a phone number, we send a verification code to that number. While the standard fees for each SMS message typically apply, we waive the fee for the first verification code for each phone number.
+ You can delete a destination phone number. However, you must wait 24 hours after adding a phone number before you can delete it.

The voice channel has its own sandbox restrictions. While your account is in the voice sandbox, you have a daily limit of 20 messages, you can send a maximum of five voice messages to a single recipient during a 24-hour period, you can send a maximum of five calls per minute, and the maximum voice message length is 30 seconds.

**Note**  
If your account is observed to be sending suspicious SMS or MMS traffic, your account's ability to send messages might be paused. If this occurs, request production access to regain the ability to send.

## Move to production
<a name="nx-sms-scale-sandbox-production"></a>

After you fully test your SMS and MMS environment in the sandbox, you can request to move to production. Moving from the SMS sandbox to production also applies to MMS capability.

**Note**  
If your account is in multiple AWS Regions, you must submit a support request for each AWS Region. Complete all fields in the support case, even if they are labeled as optional.

**To move to production from the sandbox**

1. Create a AWS Support case at [https://support.console.aws.amazon.com/support/home\#/case/create?issueType=service-limit-increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

1. On the **Create case** page, select **Account and Billing**, and for **Service**, choose **Service Quotas**. For **Category**, choose the SMS or voice option, depending on your request.

1. Under **Requests**, choose the AWS Region from which you will send messages, choose **General Limits** for the resource type, choose **SMS Production Access** for the quota, and enter 1 for the new quota value.

1. Under **Description**, for **Use case description**, provide a link to the site or app that will send messages, the type of messages you plan to send (one-time password, promotional, or transactional), the countries you plan to send to, your opt-in process, and the message template you plan to use.

1. Choose **Submit**.

After we receive your request, we provide an initial response within 24 hours. We might contact you to request additional information.

## Set a spending limit
<a name="nx-sms-scale-sandbox-spend-limit"></a>

In AWS End User Messaging there are spending limits for each messaging channel. The *account limit* is the maximum amount, in US dollars, that you can spend each month sending messages through a channel. When you reach your account limit, AWS End User Messaging stops sending your messages, and to send more messages that month you need to request a spending limit increase.

The *enforced limit* is an optional spending limit, in US dollars, between $1 and the account limit. If you don't specify an enforced limit, you can spend up to your account limit. When you reach your enforced limit, AWS End User Messaging stops sending your messages. You can adjust your enforced limit through the console or AWS CLI without contacting Support. The *remaining limit* is how much you have spent for the current month sending messages.

------
#### [ View your spending limits (console) ]

**View all of your spending limits**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. On the **Overview** page, navigate to **SMS Spending status**.

1. In the **SMS Spending status** pane, you can view your **Account limit**, **Enforced limit**, and **Remaining limit**.

------
#### [ Set enforced spending limit (AWS CLI) ]

You can use the `[set-text-message-spend-limit-override](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/set-text-message-spend-limit-override.html)` command to set the enforced limit for the SMS channel. For the voice channel, use the `[set-voice-message-spend-limit-override](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/set-voice-message-spend-limit-override.html)` command.

```
aws pinpoint-sms-voice-v2 set-text-message-spend-limit-override --monthly-limit {{NewEnforcedLimit}}
```

Replace {{NewEnforcedLimit}} with a value between one and the account limit of the SMS channel.

------

To set up billing alarms for your spending, see [Spending and cost](nx-sms-scale-spending.md).

## Request a spending quota change
<a name="nx-sms-scale-sandbox-spend-quota"></a>

Your spending quota determines how much money you can spend sending SMS, MMS, or voice messages through AWS End User Messaging each month. When AWS End User Messaging determines that sending a message would incur a cost that exceeds your spending quota for the current month, it stops publishing messages within minutes.

**Important**  
Because AWS End User Messaging is a distributed system, it stops sending messages within minutes of the spending quota being exceeded. During this period, if you continue to send messages, you might incur costs that exceed your quota.

We set the maximum spending quota for all accounts in the sandbox at $1.00 (USD) per month. Spending limits vary by AWS Region, so you must specify the AWS Regions where you require an increase.

**To request a spending limit increase**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS Services**.

1. Choose AWS End User Messaging from the list, or search for it in the search box.

1. Choose the applicable spending quota — **TextMessageMonthlySpend**, **VoiceMessageMonthlySpend**, or **MediaMessageMonthlySpend** — and then choose **Request increase at account level**.

1. For the increased quota value, enter the new value. The new value must be greater than the current value, and then choose **Request**.