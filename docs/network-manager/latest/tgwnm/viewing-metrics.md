# View global network CloudWatch metrics

There are various options for viewing CloudWatch metrics for your global network,
including the following:

- Viewing metrics for the global network and filtering by transit
  gateway
- Viewing metrics for a specific transit gateway and its attachments

###### To view metrics for your global network and filter by transit gateway

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Global networks**, and
   choose the ID for your global network.
3. In the navigation pane, choose **Transit gateway
   network**.
4. Choose **Monitoring**. On this page, you can filter by
   transit gateway to view metrics for that transit gateway.

###### To view metrics for a specific transit gateway and its attachments

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Global networks**, and
   choose the ID for your global network.
3. In the navigation pane, choose **Transit gateways**, and
   choose the ID for your transit gateway.
4. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.
