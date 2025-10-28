# Create CloudWatch alarms to monitor a NAT gateway

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes
state. An alarm watches a single metric over a time period that you specify. It sends a
notification to an Amazon SNS topic based on the value of the metric relative to a given
threshold over a number of time periods.

For example, you can create an alarm that monitors the amount of traffic coming in
or leaving the NAT gateway. The following alarm monitors the amount of outbound traffic
from clients in your VPC through the NAT gateway to the internet. It sends a
notification when the number of bytes reaches a threshold of 5,000,000 during a
15-minute period.

###### To create an alarm for outbound traffic through the NAT gateway

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**,
   **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose the **NATGateway** metric namespace and then choose
   a metric dimension. When you get to the metrics, select the check box next to
   the **BytesOutToDestination** metric for the NAT gateway, and
   then choose **Select metric**.
6. Configure the alarm as follows, and then choose **Next**:
   - For **Statistic**, choose **Sum**.
   - For **Period**, choose **15 minutes**.
   - For **Whenever**, choose **Greater/Equal**
     and enter `5000000` for the threshold.

7. For **Notification**, select an existing SNS topic or choose
   **Create new topic** to create a new one. Choose **Next**.
8. Enter a name and description for the alarm and choose
   **Next**.
9. When you done configuring the alarm, choose **Create
   alarm**.
   As another example, you can create an alarm that monitors port allocation errors and
   sends a notification when the value is greater than zero (0) for three consecutive
   5-minute periods.

###### To create an alarm to monitor port allocation errors

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**,
   **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose the **NATGateway** metric namespace and then choose
   a metric dimension. When you get to the metrics, select the check box next
   to the **ErrorPortAllocation** metric for the NAT gateway,
   and then choose **Select metric**.
6. Configure the alarm as follows, and then choose **Next**:
   - For **Statistic**, choose **Maximum**.
   - For **Period**, choose **5 minutes**.
   - For **Whenever**, choose **Greater**
     and enter 0 for the threshold.
   - For **Additional configuration**, **Datapoints
     to alarm**, enter 3.

7. For **Notification**, select an existing SNS topic or choose
   **Create new topic** to create a new one. Choose **Next**.
8. Enter a name and description for the alarm and choose
   **Next**.
9. When you are done configuring the alarm, choose **Create
   alarm**.
   For more information, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in
   the _Amazon CloudWatch User Guide_.
