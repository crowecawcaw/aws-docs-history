# Service Quotas and Amazon CloudWatch alarms

You can create Amazon CloudWatch alarms to notify you when you're close to a quota value threshold.
Setting an alarm can help alert you if you need to request a quota increase.

###### To create a CloudWatch alarm for a quota

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").
2. In the navigation pane, choose **AWS services** and then select
   a service.
3. Select a quota that supports CloudWatch alarms.

If you actively use the quota, utilization appears beneath the quota description.
If CloudWatch alarms are supported, the CloudWatch alarms section appears at the bottom of the
page. 4. In **Amazon CloudWatch alarms**, choose
**Create**. 5. For **Alarm threshold**, choose a threshold. 6. For **Alarm name**, enter a name for the alarm. This name must be
unique within the AWS account. 7. Choose **Create**.

###### Note

To add a notification to the CloudWatch alarm, see [Creating a CloudWatch
alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
_Amazon CloudWatch User Guide_.

###### To delete a CloudWatch alarm

1. Choose the service quota with the alarm.
2. Select the alarm.
3. Choose **Delete**.
