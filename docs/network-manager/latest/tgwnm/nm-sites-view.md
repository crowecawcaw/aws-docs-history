# View site details using AWS Network Manager

View
details about a core network site using the Network Manager console.

###### To view details about a site

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Sites**.
5. Choose the link that you want to see site details for.
6. The **General details** page provides information about the site.
7. Choose the **Devices** tab. This page displays
   information about the devices that are connected to the site. If you don't
   see a device listed, you'll need to add it. For more information on adding
   devices, see [Add a device using AWS Network Manager](nm-devices-add.md "nm-devices-add.md").
8. Choose the **Links** tab. This page displays the links
   that represent a connection from a device. If you don't see a link listed,
   you'll need to create the link. For the steps to create a link, see [Add a link using AWS Network Manager](nm-site-link-add.md "nm-site-link-add.md").
9. Choose the **VPNs** tab. This page displays site-related
   VPN information.
10. Choose the **Monitoring** tab. This page displays
    **Data In** and **Data Out**
    information for your links.
11. From the dropdown list, choose the link that you want to view information
    for.
12. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.
