

# Monitor devices using AWS Network Manager
<a name="nm-devices-monitoring"></a>

Monitor device Amazon CloudWatch events on the Network Manager Monitoring page. 

**To monitor devices**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the **Monitoring** tab.

1. The **Monitoring** page displays data for the following:
   + **Data In**
   + **Data Out**
   + **Tunnel down count Average**

   (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

   Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**  
The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region. 