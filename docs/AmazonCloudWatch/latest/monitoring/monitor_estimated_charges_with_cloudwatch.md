# Create a billing alarm to monitor your estimated AWS charges

You can monitor your estimated AWS charges by using Amazon CloudWatch. When you enable the
monitoring of estimated charges for your AWS account, the estimated charges are calculated
and sent several times daily to CloudWatch as metric data.

Billing metric data is stored in the US East (N. Virginia) Region and
represents worldwide charges. This data includes the estimated charges for every service in
AWS that you use, in addition to the estimated overall total of your AWS charges.

The alarm triggers when your account billing exceeds the threshold you specify. It
triggers only when the current billing exceeds the threshold. It doesn't use projections
based on your usage so far in the month.

If you create a billing alarm at a time when your charges have already exceeded the
threshold, the alarm goes to the `ALARM` state immediately.

###### Note

For information about analyzing CloudWatch charges that you have already been billed for,
see [Analyzing, optimizing, and reducing CloudWatch costs](cloudwatch_billing.md "cloudwatch_billing.md").

###### Tasks

- [Enabling billing alerts](#turning_on_billing_metrics "#turning_on_billing_metrics")
- [Create a billing alarm](#creating_billing_alarm_with_wizard "#creating_billing_alarm_with_wizard")
- [Deleting a billing alarm](#deleting_billing_alarm "#deleting_billing_alarm")

## Enabling billing alerts

Before you can create an alarm for your estimated charges, you must enable billing
alerts, so that you can monitor your estimated AWS charges and create an alarm using
billing metric data. After you enable billing alerts, you can't disable data collection,
but you can delete any billing alarms that you created.

After you enable billing alerts for the first time, it takes about 15 minutes before
you can view billing data and set billing alarms.

###### Requirements

- You must be signed in using account root user credentials or as an IAM user that
  has been given permission to view billing information.
- For consolidated billing accounts, billing data for each linked account can be
  found by logging in as the paying account. You can view billing data for total
  estimated charges and estimated charges by service for each linked account, in
  addition to the consolidated account.
- In a consolidated billing account, member linked account metrics are captured only
  if the payer account enables the **Receive Billing Alerts**
  preference. If you change which account is your management/payer account, you must
  enable the billing alerts in the new management/payer account.
- The account must not be part of the Amazon Partner Network (APN) because billing
  metrics are not published to CloudWatch for APN accounts. For more information, see [AWS Partner Network](https://aws.amazon.com/partners/ "https://aws.amazon.com/partners/").

###### To enable the monitoring of estimated charges

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing Preferences**.
3. By **Alert preferences** choose **Edit**.
4. Choose **Receive CloudWatch Billing Alerts**.
5. Choose **Save preferences**.

## Create a billing alarm

###### Important

Before you create a billing alarm, you must set your Region to US East (N. Virginia).
Billing metric data is stored in this Region and represents worldwide charges. You also
must enable billing alerts for your account or in the management/payer account (if you
are using consolidated billing). For more information, see [Enabling billing alerts](#turning_on_billing_metrics "#turning_on_billing_metrics").

In this procedure, you create an alarm that sends a notification when your estimated
charges for AWS exceed a defined threshold.

###### To create a billing alarm using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then choose
   **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**. In **AWS
   Namespaces**, choose **Billing**, and then choose
   **Total Estimated Charge**.

###### Note

If you don't see the **Billing**/**Total Estimated
Charge** metric, enable billing alerts, and change your Region to
US East (N. Virginia). For more information, see [Enabling billing alerts](#turning_on_billing_metrics "#turning_on_billing_metrics"). 5. Select the box for the **EstimatedCharges** metric, and then
choose **Select metric**. 6. For **Statistic**, choose **Maximum**. 7. For **Period**, choose **6 hours**. 8. For **Threshold type**, choose **Static**. 9. For **Whenever EstimatedCharges is . . .**, choose
**Greater**. 10. For **than . . .**, define the value that you want to cause your
alarm to trigger. For example, `200` USD.

The **EstimatedCharges** metric values are only in US dollars
(USD), and the currency conversion is provided by Amazon Services LLC. For more
information, see [What is
AWS Billing?](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").

###### Note

After you define a threshold value, the preview graph displays your estimated
charges for the current month. 11. Choose **Additional Configuration** and do the following:

    * For **Datapoints to alarm**, specify **1 out of
     1**.
    * For **Missing data treatment**, choose **Treat
     missing data as missing**.

12. Choose **Next**.
13. Under **Notification**, ensure that **In
    alarm** is selected. Then specify an Amazon SNS topic to be notified when your
    alarm is in the `ALARM` state. The Amazon SNS topic can include your email
    address so that you receive email when the billing amount crosses the threshold that
    you specified.

You can select an existing Amazon SNS topic, create a new Amazon SNS topic, or use a topic
ARN to notify other account. If you want your alarm to send multiple notifications for
the same alarm state or for different alarm states, choose **Add
notification**. 14. Choose **Next**. 15. Under **Name and description**, enter a name for your alarm. The
name must contain only UTF-8 characters, and can't contain ASCII control characters.

    1. (Optional) Enter a description of your alarm. The description can include
     markdown formatting, which is displayed only in the alarm
     **Details** tab in the CloudWatch console. The markdown can be useful
     to add links to runbooks or other internal resources.

16. Choose **Next**.
17. Under **Preview and create**, make sure that your configuration
    is correct, and then choose **Create alarm**.

## Deleting a billing alarm

You can delete your billing alarm when you no longer need it.

###### To delete a billing alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the Region to US East (N. Virginia). Billing metric data is
   stored in this Region and reflects worldwide charges.
3. In the navigation pane, choose **Alarms**, **All
   alarms**.
4. Select the check box next to the alarm and choose **Actions**,
   **Delete**.
5. When prompted for confirmation, choose **Yes, Delete**.
