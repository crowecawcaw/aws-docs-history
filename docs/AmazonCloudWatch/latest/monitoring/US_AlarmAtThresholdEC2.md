# Create a CPU usage alarm

You can create an CloudWatch alarm that sends a notification using Amazon SNS when the alarm
changes state from `OK` to `ALARM`.

The alarm changes to the `ALARM` state when the average CPU use of an EC2
instance exceeds a specified threshold for consecutive specified periods.

## Setting up a CPU usage alarm using the

AWS Management Console

Use these steps to use the AWS Management Console to create a CPU usage alarm.

###### To create an alarm based on CPU usage

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
   Alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. In the **All metrics** tab, choose **EC2
   metrics**.
6. Choose a metric category (for example, **Per-Instance
   Metrics**).
7. Find the row with the instance that you want listed in the
   **InstanceId** column and **CPUUtilization** in
   the **Metric Name** column. Select the check box next to this row,
   and choose **Select metric**.
8. Under **Specify metric and conditions**, for
   **Statistic** choose **Average**, choose one of
   the predefined percentiles, or specify a custom percentile (for example,
   `p95.45`).
9. Choose a period (for example, `5 minutes`).
10. Under **Conditions**, specify the following:
    1. For **Threshold type**, choose
       **Static**.
    2. For **Whenever CPUUtilization is**, specify
       **Greater**. Under **than...**, specify the
       threshold that is to trigger the alarm to go to ALARM state if the CPU utilization
       exceeds this percentage. For example, 70.
    3. Choose **Additional configuration**. For **Datapoints
       to alarm**, specify how many evaluation periods (data points) must be
       in the `ALARM` state to trigger the alarm. If the two values here
       match, you create an alarm that goes to `ALARM` state if that many
       consecutive periods are breaching.

    To create an M out of N alarm, specify a lower number for the first value than
    you specify for the second value. For more information, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md"). 4. For **Missing data treatment**, choose how to have the alarm
    behave when some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing
    data](alarms-and-missing-data.md "alarms-and-missing-data.md"). 5. If the alarm uses a percentile as the monitored statistic, a
    **Percentiles with low samples** box appears. Use it to choose
    whether to evaluate or ignore cases with low sample rates. If you choose
    **ignore (maintain alarm state)**, the current alarm state is
    always maintained when the sample size is too low. For more information, see [Percentile-based alarms and low data
    samples](percentiles-with-low-samples.md "percentiles-with-low-samples.md").

11. Choose **Next**.
12. Under **Notification**, choose **In alarm** and
    select an SNS topic to notify when the alarm is in `ALARM` state

To have the alarm send multiple notifications for the same alarm state or for
different alarm states, choose **Add notification**.

To have the alarm not send notifications, choose
**Remove**. 13. When finished, choose **Next**. 14. Enter a name and description for the alarm. Then choose
**Next**.

The name must contain only UTF-8 characters, and can't contain ASCII control
characters. The description can include markdown formatting, which is displayed only
in the alarm **Details** tab in the CloudWatch console. The markdown can be
useful to add links to runbooks or other internal resources. 15. Under **Preview and create**, confirm that the information and
conditions are what you want, then choose **Create alarm**.

## Setting up a CPU usage alarm using the AWS CLI

Use these steps to use the AWS CLI to create a CPU usage alarm.

###### To create an alarm based on CPU usage

1. Set up an SNS topic. For more information, see [Setting up Amazon SNS notifications](Notify_Users_Alarm_Changes.md#US_SetupSNS "Notify_Users_Alarm_Changes.md#US_SetupSNS").
2. Create an alarm using the [put-metric-alarm](../../../cli/latest/reference/cloudwatch/put-metric-alarm.md "../../../cli/latest/reference/cloudwatch/put-metric-alarm.md") command
   as follows.

```
`aws cloudwatch put-metric-alarm --alarm-name `cpu-mon` --alarm-description "Alarm when CPU exceeds 70%" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period `300` --threshold `70` --comparison-operator GreaterThanThreshold --dimensions Name=InstanceId,Value=`i-12345678` --evaluation-periods `2` --alarm-actions arn:aws:sns:`us-east-1`:`111122223333`:`my-topic` --unit Percent`
```

3. Test the alarm by forcing an alarm state change using the [set-alarm-state](../../../cli/latest/reference/cloudwatch/set-alarm-state.md "../../../cli/latest/reference/cloudwatch/set-alarm-state.md")
   command.
   1. Change the alarm state from `INSUFFICIENT_DATA` to
      `OK`.

   ```
   `aws cloudwatch set-alarm-state --alarm-name `cpu-mon` --state-reason "initializing" --state-value OK`
   ```

   2. Change the alarm state from `OK` to `ALARM`.

   ```
   `aws cloudwatch set-alarm-state --alarm-name `cpu-mon` --state-reason "initializing" --state-value ALARM`
   ```

   3. Check that you have received a notification about the alarm.
