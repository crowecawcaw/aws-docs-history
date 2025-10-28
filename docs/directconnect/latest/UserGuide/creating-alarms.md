# Create Amazon CloudWatch alarms to monitor AWS Direct Connect connections

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes
state. An alarm watches a single metric over a time period that you specify. It
sends a notification to an Amazon SNS topic based on the value of the metric relative to
a given threshold over a number of time periods.

For example, you can create an alarm that monitors the state of an AWS Direct Connect
connection. It sends a notification when the connection state is **down** for five consecutive 1-minute periods. For details
on what to know for creating an alarm and for more information on creating an alarm,
see [Using Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
in the _Amazon CloudWatch User Guide_.

###### To create a CloudWatch alarm.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then
   choose **All alarms**.
3. Choose **Create Alarm**.
4. Choose **Select metric**, and then choose
   **DX** .
5. Choose the **Connection Metrics** metric.
6. Select the AWS Direct Connect connection, and then choose the **Select
   metric** metric.
7. On the **Specify metric and conditions** page, configure
   the parameters for the alarm. For more specifying metrics and conditions,
   see [Using Amazon CloudWatch
   Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.
8. Choose **Next**.
9. Configure the alarm actions on the **Configure actions**
   page. For more information on configuring alarm actions, see [Alarm
   actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions") in the _Amazon CloudWatch User Guide_.
10. Choose **Next**.
11. On the **Add name and description** page, enter a
    **Name** and an optional **Alarm
    description** to describe this alarm, and then choose
    **Next**.
12. Verify the proposed alarm on the **Preview and create**
    page.
13. If needed choose **Edit** to change any information, and
    then choose **Create alarm**.

The **Alarms** page displays a new row with information
about the new alarm. The **Actions** status displays
**Actions enabled**, indicating that the alarm is
active.
