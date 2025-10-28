# Create a storage throughput alarm that sends

email

You can set up an SNS notification and configure an alarm that is triggered when Amazon EBS
exceeds 100 MB throughput.

## Setting up a storage throughput alarm using the

AWS Management Console

Use these steps to use the AWS Management Console to create an alarm based on Amazon EBS
throughput.

###### To create a storage throughput alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
   Alarms**.
3. Choose **Create alarm**.
4. Under **EBS Metrics**, choose a metric category.
5. Select the row with the volume and the **VolumeWriteBytes**
   metric.
6. For the statistic, choose **Average**. For the period, choose
   **5 Minutes**. Choose **Next**.
7. Under **Alarm Threshold**, enter a unique name for the alarm (for
   example, `myHighWriteAlarm`) and a description of the alarm (for
   example, `VolumeWriteBytes exceeds 100,000 KiB/s`). The name must
   contain only UTF-8 characters, and can't contain ASCII control characters. The
   description can include markdown formatting, which is displayed only in the alarm
   **Details** tab in the CloudWatch console. The markdown can be useful to
   add links to runbooks or other internal resources.
8. Under **Whenever**, for **is**, choose
   **>** and enter `100000`. For
   **for**, enter `15` consecutive
   periods.

A graphical representation of the threshold is shown under **Alarm
Preview**. 9. Under **Additional settings**, for **Treat missing data
as**, choose **ignore (maintain alarm state)** so that
missing data points don't trigger alarm state changes. 10. Under **Actions**, for **Whenever this alarm**,
choose **State is ALARM**. For **Send notification
to**, choose an existing SNS topic or create one.

To create an SNS topic, choose **New list**. For **Send
notification to**, enter a name for the SNS topic (for example,
`myHighCpuAlarm`), and for **Email list**,
enter a comma-separated list of email addresses to be notified when the alarm changes
to the `ALARM` state. Each email address is sent a topic subscription
confirmation email. You must confirm the subscription before notifications can be sent
to an email address. 11. Choose **Create Alarm**.

## Setting up a storage throughput alarm using the

AWS CLI

Use these steps to use the AWS CLI to create an alarm based on Amazon EBS throughput.

###### To create a storage throughput alarm

1. Create an SNS topic. For more information, see [Setting up Amazon SNS notifications](Notify_Users_Alarm_Changes.md#US_SetupSNS "Notify_Users_Alarm_Changes.md#US_SetupSNS").
2. Create the alarm.

```
`aws cloudwatch put-metric-alarm --alarm-name `ebs-mon` --alarm-description "Alarm when EBS volume exceeds 100MB throughput" --metric-name VolumeReadBytes --namespace AWS/EBS --statistic Average --period 300 --threshold 100000000 --comparison-operator GreaterThanThreshold --dimensions Name=VolumeId,Value=`my-volume-id` --evaluation-periods 3 --alarm-actions arn:aws:sns:`us-east-1`:`111122223333`:`my-alarm-topic` --insufficient-data-actions arn:aws:sns:`us-east-1`:`111122223333`:`my-insufficient-data-topic``
```

3. Test the alarm by forcing an alarm state change using the [set-alarm-state](../../../cli/latest/reference/cloudwatch/set-alarm-state.md "../../../cli/latest/reference/cloudwatch/set-alarm-state.md")
   command.
   1. Change the alarm state from `INSUFFICIENT_DATA` to
      `OK`.

   ```
   `aws cloudwatch set-alarm-state --alarm-name `ebs-mon` --state-reason "initializing" --state-value OK`
   ```

   2. Change the alarm state from `OK` to `ALARM`.

   ```
   `aws cloudwatch set-alarm-state --alarm-name `ebs-mon` --state-reason "initializing" --state-value ALARM`
   ```

   3. Change the alarm state from `ALARM` to
      `INSUFFICIENT_DATA`.

   ```
   `aws cloudwatch set-alarm-state --alarm-name `ebs-mon` --state-reason "initializing" --state-value INSUFFICIENT_DATA`
   ```

   4. Check that you have received an email notification about the alarm.
