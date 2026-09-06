

# Option 1: Send all MediaLive events to an email address
<a name="option-1"></a>

This option shows how to set up to send all events to a single email address. The drawback of this setup is that the email account will receive a large volume of emails. Therefore, we recommend that you don't use this setup in a production environment. 

You must perform the following procedure in each Region where channels or multiplexes are running.

## Create a subscription
<a name="option-1-1"></a>

Create a subscription to set up a specific email address so that it automatically receives email notifications when any event occurs in MediaLive. You must identify an email recipient for the emails.

In the following procedure, we use the example of "MediaLive\_alert" as the subject line and "MediaLive" as the sender of the email. We create the subscription using the Amazon Simple Notification Service (Amazon SNS) console.

**To create a subscription for email notifications (Amazon SNS console)**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/v2/home](https://console.aws.amazon.com/sns/v2/home).

1. In the navigation pane, choose **Topics**, and then choose **Create new topic**.

1. In the **Create new topic** dialog box, for **Topic name**, type the name that you want for the subject line of the email, such as **MediaLive\_alert**.

1. For **Display name**, type the name that you want for the sender of the email, such as **MediaLive**.

1. Choose **Create topic**.

1. Amazon SNS creates the topic and displays the ARN in the list of topics. For example, `arn:aws:sns:us-west-2:111122223333:MediaLive`, where `111122223333` is your AWS account.

1. Copy this ARN to your clipboard. 

1. In the navigation pane, choose **Subscriptions**, and then choose **Create subscription**.

1. On the **Subscriptions** page, choose **Create subscription**.

1. In the **Create subscriptions** dialog box, for **Topic ARN**, type or paste the ARN.

1. For **Protocol**, choose **Email**.

1. For **Endpoint**, type the email address of the recipient. You must be able to log on to this email account because Amazon SNS sends a confirmation email to this address.

1. Choose **Create subscription**.

   Amazon SNS sends a confirmation email to the address that you specified. 

1. Log on to that email account, and display the email. Choose the "Confirm subscription" link in the email to enable the subscription. A confirmation window appears in a web browser. You can close this window.

## Create a rule
<a name="option-1-2"></a>

You now create a rule in Amazon EventBridge that says, "When EventBridge receives any event from `aws.medialive`, invoke the specified SNS topic." In other words, you create a rule that sends an email to the subscribed email address.

**To create a rule (EventBridge console)**

1. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Rules**, and then choose **Create rule**.

1. Enter a **Name** and optional description for the rule.

1. For **Event bus**, keep the default event bus selected.

1. For **Rule type**, choose **Rule with an event pattern**, and then choose **Next**.

1. For **Creation method**, choose **Custom pattern (JSON editor)**.

1. In the **Event pattern** box, enter the following:

   ```
   {
     "source": [
       "aws.medialive"
     ]
   }
   ```

1. Choose **Next**.

1. For **Target type**, choose **AWS service**.

1. For **Select a target**, choose **SNS topic**.

1. For **Topic**, choose the topic that you created, for example, **MediaLive\_alert**.

1. Choose **Next**, configure optional tags, and then choose **Next** again.

1. Review the rule details and choose **Create rule**.

Now, whenever an alert occurs in MediaLive, an event will be sent to EventBridge. This event will trigger the rule that sends an email to the email address that you specified in the SNS subscription.