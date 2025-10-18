# Monitor devices in an AWS Cloud WAN global network

Monitor device Amazon CloudWatch events on the AWS Cloud WAN Monitoring page. 

###### To monitor devices

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the **Monitoring** tab.
6. The **Monitoring** page displays data for the
 following:




	* **Data In**
	* **Data Out**
	* **Tunnel down count Average**
(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.


Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
 [Using
 Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the *Amazon CloudWatch User
 Guide*.


###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.
