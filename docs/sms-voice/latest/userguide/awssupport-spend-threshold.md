# Requesting an SMS, MMS, or voice spending quota

change for AWS End User Messaging SMS

Your spending quota determines how much money you can spend sending SMS, MMS, or voice
messages through AWS End User Messaging SMS each month. When AWS End User Messaging SMS determines that sending an SMS, MMS, or voice
message would incur a cost that exceeds your spending quota for the current month, it stops
publishing SMS, MMS, or voice messages within minutes.

###### Important

Because AWS End User Messaging SMS is a distributed system, it stops sending SMS, MMS, or voice messages
within minutes of the spending quota being exceeded. During this period, if you continue
to send SMS, MMS, or voice messages, you might incur costs that exceed your
quota.

We set the maximum spending quota for all accounts in the Sandbox at $1.00 (USD) per
month. This quota is intended to let you test the message-sending capabilities of AWS End User Messaging SMS.
This quota also reduces the risk of sending large amounts of messages before you're ready to
use AWS End User Messaging SMS for your production workloads and is necessary to prevent malicious users from
abusing AWS End User Messaging SMS.

You can request an increase to the SMS, MMS, or voice spending quota for your account by
opening a quota increase case in the AWS Support Center. Spending limits vary by region.
Because of this you must specify the AWS Regions where you require an increase.

## Change your spending threshold

You can request an increase to your maximum monthly spending quota by using the
**AWS Service Quotas.**

###### To request a spending limit increase

1.  Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2.  In the Navigation pane, choose **AWS Services**.
3.  Choose **AWS End User Messaging** from the list, or search for
    **AWS End User Messaging** in the search box.
4.  Choose the applicable spending quota

        * **TextMessageMonthlySpend**
        * **VoiceMessageMonthlySpend**
        * **MediaMessageMonthlySpend**

    and then choose **Request increase at account level**.

5.  For increased quota value, enter the new value. The new value must be greater
    than the current value.
6.  Choose **Request**.
7.  To view any pending or recently resolved requests in the console, navigate to
    the **Request history** tab from the service's details page or
    choose **Dashboard** from the navigation pane. For pending
    requests, choose the status of the request to open the request receipt. The
    initial status of a request is **Pending**. After the status
    changes to **Quota requested**, the Support case number is
    shown. Choose the case number to open the ticket for your request.

The AWS Support team provides an initial response to your request within 24 hours.

In order to prevent our systems from being used to send unsolicited or malicious content, we have to
consider each request carefully. If we’re able to do so, we'll grant your request within this 24-hour
period. However, if we need to obtain additional information from you, it might take longer to resolve your
request.

We might not be able to grant your request if your use case doesn’t align with our policies.
