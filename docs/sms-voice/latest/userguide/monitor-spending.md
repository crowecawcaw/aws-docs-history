# Monitoring SMS, MMS, and voice spending activity with

AWS End User Messaging SMS

This topic provides information about viewing SMS, MMS, and voice spending metrics in
Amazon CloudWatch. It also explains how to set up a CloudWatch alarm that sends you a notification when
your monthly SMS, MMS, or voice spending exceeds a certain amount.

If you only want to view your monthly charges for using AWS End User Messaging SMS, including the amount of
money you've spent, you should use the AWS Billing and Cost Management console. The Billing and Cost Management console provides an
estimate of your bill for the current month, and your final charges for previous months. For
more information, see [Viewing your monthly
charges](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the _AWS Billing User Guide_.

###### Important

You must create a [service-linked role](using-service-linked-roles.md#using-service-linked-roles.title "using-service-linked-roles.md#using-service-linked-roles.title") for CloudWatch metrics to be collected.

## View your monthly SMS, MMS, and voice

spending by using CloudWatch

To quickly determine how much money you've spent sending SMS, MMS, and voice messages
during the current month, you can use the Metrics section of the CloudWatch console. CloudWatch
retains metrics data for 15 months, so you can view real-time data and analyze
historical trends.

For more information about viewing metrics in CloudWatch, see [Using Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the
_Amazon CloudWatch User Guide_.

###### To view SMS, MMS, and voice spending metrics in CloudWatch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose
   **SMSVoice**.
4. Choose **Account Metrics**.
5. Select from options **TextMessageMonthlySpend**,
   **MediaMessageMonthlySpend**, and **VoiceMessageMonthlySpend**. Based on your selection,
   the graph updates to display the amount of money spent during the current month
   by using AWS End User Messaging SMS.

###### Note

The **TextMessageMonthlySpend**, **MediaMessageMonthlySpend**, and **VoiceMessageMonthlySpend** metrics don't appear
until you send at least one message using AWS End User Messaging SMS.

## Create an SMS, MMS, or voice spending alarm by

using CloudWatch

In addition to viewing your monthly SMS, MMS, and voice spending metrics, you can
create CloudWatch alarms that notify you when your SMS, MMS, or voice spending exceeds a
certain amount. You can set up CloudWatch to deliver these notifications to you by sending
them to an Amazon SNS topic.

For more information about creating alarms in CloudWatch, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
_Amazon CloudWatch User Guide_.

###### To create an SMS or voice spending alarm in CloudWatch

1. If you haven't already done so, create an Amazon SNS topic and subscribe an
   endpoint to it. The endpoint that you subscribe to the topic should be the
   location where you want to receive spending notifications. For example, if you
   want to receive spending notifications by email, subscribe your email address to
   the Amazon SNS topic. If you want to receive spending notifications by text message,
   subscribe an SMS endpoint to the topic.

For information about creating and subscribing to topics, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in
the _Amazon Simple Notification Service Developer Guide_. 2. Open the CloudWatch console at
[https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). 3. ###### Important

Before you create a billing alarm, you must set your AWS Region to US East (N. Virginia). Billing metric data is stored in this AWS Region and represents
worldwide charges. You also must enable billing alerts for your account or
in the management/payer account (if you are using consolidated billing). For
more information, see [Enabling billing alerts](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md#turning_on_billing_metrics "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md#turning_on_billing_metrics").

In the navigation pane, under **Alarms**, choose
**Billing**. 4. Next to **Billing alarms**, choose **Create
alarm**. 5. Choose **Select metric**. 6. On the **All metrics** tab, choose
**SMSVoice**, and then choose **Account
Metrics**. 7. Select either **TextMessageMonthlySpend**,
**MediaMessageMonthlySpend**, or **VoiceMessageMonthlySpend**.

###### Note

The **TextMessageMonthlySpend**, **MediaMessageMonthlySpend**, and **VoiceMessageMonthlySpend** metrics don't appear
until you send at least one message through AWS End User Messaging SMS. 8. Choose the **Graphed metrics** tab, and then complete the
following steps:

    * Under **Statistic**, choose the statistic or
     predefined percentile that you want to monitor, or specify a custom
     percentile—for example, **p99** or
     **p45**.
    * Under **Period**, choose the evaluation period for
     the alarm. When evaluating the alarm, each period is aggregated into one
     datapoint.

9. Choose **Select metric**. The **Specify metric and
   conditions** page appears, showing a graph and other information
   about the metric and statistic for the alarm.
10. Under **Conditions**, complete the following steps:
    - For **Threshold type**, choose
      **Static**.
    - For **Whenever (**TextMessageMonthlySpend**, **MediaMessageMonthlySpend**, or **VoiceMessageMonthlySpend**) is**, specify
      whether you want the metric to be greater than, greater than or equal
      to, or equal to the threshold in order to trigger the alarm. Then, under
      **than**, enter the threshold value, which is the
      dollar amount (in US Dollars) that you want to trigger the alarm.

11. Under **Additional configuration**, complete the
    following steps:
    - For **Datapoints to alarm**, enter the number of
      evaluation periods (datapoints) during which the spending amount must
      exceed the threshold to trigger the alarm.
    - For **Missing data treatment**, choose
      **Treat missing data as ignore (maintain the alarm
      state)**.

12. Choose **Next**.
13. Under **Notification**, complete the following steps:
    - For **Whenever this alarm state is**, choose
      **in Alarm**.
    - For **Select an SNS topic**, choose the Amazon SNS topic
      that you want the alarm notification to be sent to.

14. Choose **Next**.
15. Enter a name and, optionally, a description for the alarm, and then choose
    **Next**.
16. Under **Preview and create**, review and confirm that the
    alarm settings are what you want, and then choose **Create
    alarm**.
