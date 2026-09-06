

# Create Amazon CloudWatch alarms to monitor Direct Connect connections
<a name="creating-alarms"></a>

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period that you specify. It sends a notification to an Amazon SNS topic based on the value of the metric relative to a given threshold over a number of time periods. 

For example, you can create an alarm that monitors the state of a Direct Connect connection. It sends a notification when the connection state is **down** for five consecutive 1-minute periods. For details on what to know for creating an alarm and for more information on creating an alarm, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*. 

**To create a CloudWatch alarm.**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, and then choose **All alarms**.

1. Choose **Create Alarm**.

1. Choose **Select metric**, and then choose **DX** .

1. Choose the **Connection Metrics** metric.

1. Select the Direct Connect connection, and then choose the **Select metric** metric.

1. On the** Specify metric and conditions** page, configure the parameters for the alarm. For more specifying metrics and conditions, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

1. Choose **Next**.

1. Configure the alarm actions on the **Configure actions** page. For more information on configuring alarm actions, see [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions) in the *Amazon CloudWatch User Guide*.

1. Choose **Next**. 

1. On the **Add name and description** page, enter a **Name** and an optional **Alarm description** to describe this alarm, and then choose **Next**.

1. Verify the proposed alarm on the **Preview and create** page. 

1. If needed choose **Edit** to change any information, and then choose **Create alarm**.

   The **Alarms** page displays a new row with information about the new alarm. The **Actions** status displays **Actions enabled**, indicating that the alarm is active.