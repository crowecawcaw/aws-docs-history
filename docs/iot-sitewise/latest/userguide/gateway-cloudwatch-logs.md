

# Use Amazon CloudWatch Logs
<a name="gateway-cloudwatch-logs"></a>

You can configure your SiteWise Edge gateway to send logs to CloudWatch Logs. For more information, see [Enable logging for CloudWatch Logs](https://docs.aws.amazon.com/greengrass/v2/developerguide/monitor-logs.html#enable-cloudwatch-logs) in the *AWS IoT Greengrass Version 2 Developer Guide*.

**To configure and access CloudWatch Logs (Console)**

1. Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log groups**.

1. You can find the AWS IoT SiteWise component logs in the following log groups:
   + `/aws/greengrass/UserComponent/{{region}}/aws.iot.SiteWiseEdgeCollectorOpcua` – The logs for the SiteWise Edge gateway's component that collects data from the SiteWise Edge gateway's OPC UA sources.
   + `/aws/greengrass/UserComponent/{{region}}/aws.iot.SiteWiseEdgePublisher` – The logs for the SiteWise Edge gateway's component that publishes OPC UA data streams to AWS IoT SiteWise.

   Choose the log group for the function to debug.

1. Choose a log stream that has a name that ends with the name of your AWS IoT Greengrass group. By default, CloudWatch displays the most recent log stream first.  
![CloudWatch Logs "Log groups" page screenshot.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/gateway-view-cloudwatch-logs-console.png)

1. To show logs from the last 5 minutes, do the following:

   1. Choose **custom** in the upper-right corner.

   1. Choose **Relative**.

   1. Choose **5** minutes.

   1. Choose **Apply**.  
![CloudWatch "Logs" page screenshot.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/gateway-filter-cloudwatch-logs-console.png)

1. (Optional) To see fewer logs, you can choose **1m** from the upper-right corner.

1. Scroll to the bottom of the log entries to show the most recent logs.