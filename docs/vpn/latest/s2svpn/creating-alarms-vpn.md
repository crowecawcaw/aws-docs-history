

# Create Amazon CloudWatch alarms to monitor AWS Site-to-Site VPN tunnels
<a name="creating-alarms-vpn"></a>

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period you specify, and sends a notification to an Amazon SNS topic based on the value of the metric relative to a given threshold over a number of time periods. 

For example, you can create an alarm that monitors the state of a single VPN tunnel, and sends a notification when the tunnel state is DOWN for 3 datapoints within 15 minutes.

**To create an alarm for a single tunnel state**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, expand **Alarms**, then choose **All alarms**.

1. Choose **Create alarm**, then choose **Select metric**.

1. Choose **VPN**, then **VPN Tunnel Metrics**.

1. Select the IP address of the desired tunnel, on the same line with the **TunnelState** metric. Choose **Select metric**.

1. For **Whenever TunnelState is...**, select **Lower**, and then enter "1" in the input field under **than...**.

1. Under **Additional configuration**, set the inputs to "3 out of 3" for **Datapoints to alarm**.

1. Choose **Next**.

1. Under **Send a notification to the following SNS topic**, select an existing notification list or create a new one.

1. Choose **Next**.

1. Enter a name for your alarm. Choose **Next**. 

1. Check the settings for your alarm, and then choose **Create alarm**.

You can create an alarm that monitors the state of the Site-to-Site VPN connection. For example, you can create an alarm that sends a notification when the status of one or both tunnels is DOWN for one 5-minute period.

**To create an alarm for Site-to-Site VPN connection state**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, expand **Alarms**, then choose **All alarms**.

1. Choose **Create alarm**, then choose **Select metric**.

1. Choose **VPN**, then choose **VPN Connection Metrics**.

1. Select your Site-to-Site VPN connection and the **TunnelState** metric. Choose **Select metric**.

1. For **Statistic**, specify **Maximum**.

   Alternatively, if you've configured your Site-to-Site VPN connection so that both tunnels are up, you can specify a statistic of **Minimum** to send a notification when at least one tunnel is down.

1. For **Whenever**, choose **Lower/Equal** (**<=**) and enter **0** (or **0.5** for when at least one tunnel is down). Choose **Next**.

1. Under **Select an SNS topic**, select an existing notification list or choose **New list** to create a new one. Choose **Next**.

1. Enter a name and description for your alarm. Choose **Next**. 

1. Check the settings for your alarm, and then choose **Create alarm**.

You can also create alarms that monitor the amount of traffic coming in or leaving the VPN tunnel. For example, the following alarm monitors the amount of traffic coming into the VPN tunnel from your network, and sends a notification when the number of bytes reaches a threshold of 5,000,000 during a 15 minute period.

**To create an alarm for incoming network traffic**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, expand **Alarms**, then choose **All alarms**.

1. Choose **Create alarm**, then choose **Select metric**.

1. Choose **VPN**, then choose **VPN Tunnel Metrics**.

1. Select the IP address of the VPN tunnel and the **TunnelDataIn** metric. Choose **Select metric**.

1. For **Statistic**, specify **Sum**. 

1. For **Period**, select **15 minutes**.

1. For **Whenever**, choose **Greater/Equal**(**>=**) and enter **5000000**. Choose **Next**.

1. Under **Select an SNS topic**, select an existing notification list or choose **New list** to create a new one. Choose **Next**.

1. Enter a name and description for your alarm. Choose **Next**. 

1. Check the settings for your alarm, and then choose **Create alarm**.

The following alarm monitors the amount of traffic leaving the VPN tunnel to your network, and sends a notification when the number of bytes is less than 1,000,000 during a 15 minute period.

**To create an alarm for outgoing network traffic**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, expand **Alarms**, then choose **All alarms**.

1. Choose **Create alarm**, then choose **Select metric**.

1. Choose **VPN**, then choose **VPN Tunnel Metrics**.

1. Select the IP address of the VPN tunnel and the **TunnelDataOut** metric. Choose **Select metric**.

1. For **Statistic**, specify **Sum**. 

1. For **Period**, select **15 minutes**.

1. For **Whenever**, choose **Lower/Equal** (**<=**) and enter `1000000`. Choose **Next**.

1. Under **Select an SNS topic**, select an existing notification list or choose **New list** to create a new one. Choose **Next**.

1. Enter a name and description for your alarm. Choose **Next**. 

1. Check the settings for your alarm, and then choose **Create alarm**.

For more examples of creating alarms, see [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.