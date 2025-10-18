# Monitor AWS Cloud WAN with Amazon CloudWatch Events
 metrics

You can monitor your core network and core network attachments using Amazon CloudWatch under the
  `AWS/NetworkManager` namespace, which collects raw data and processes it into readable,
 near-real-time metrics. These statistics are kept for 15 months, so that you can access
 historical information and gain a better perspective on how your network is performing. You
 can also set alarms that watch for certain thresholds, and send notifications or take
 actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Note

 CloudWatch metrics in the `AWS/NetworkManager` namespace are available only in the
 following Regions:


* US West (Oregon) for all Regions except AWS GovCloud (US)
* AWS GovCloud (US-West) for AWS GovCloud (US-West) and AWS GovCloud (US-East)
You can view usage metrics for any of your core network edge locations.


## View usage metrics for an edge location


View usage metrics for a specific core network edge.


###### To access usage metrics for a core network edge location

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Core networks**, and then
 choose the **Monitoring** tab.
5. On the **Core network** page, choose the **Show
 metrics** dropdown list, and then choose
 **Usage**.
6. From the **Core network edge** dropdown list, choose the edge
 location that you want to see metrics for.
7. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.


Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
 [Using
 Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the *Amazon CloudWatch User
 Guide*.


###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.
8. The Metrics page displays the usage metrics for the specified edge location
 during the chosen time frame. For more information about these metrics, see [Cloud WAN metrics and dimensions](cloudwan-metrics.md#cloudwan-metrics-tbl "cloudwan-metrics.md#cloudwan-metrics-tbl").
