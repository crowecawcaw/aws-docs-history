# Perform a route analysis

Perform a route analysis of your AWS global network. You can only use Route Analyzer using the AWS Global Networks for Transit Gateways console.

###### To analyze your routes

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway network**.
5. The **Overview** page opens by default, showing information about your transit gateways.
6. Choose the **Route Analyzer** tab.
7. Under **Source**, do the following:
   - Choose the transit gateway and the transit gateway attachment.
   - For **IP address**, enter a source IPv4 or IPv6
     address.

8. Under **Destination**, do the following:
   - Choose the transit gateway and the transit gateway attachment.
   - For **IP address**, enter a target IPv4 or IPv6
     address.

9. (Optional) To analyze the return path, ensure that you enable
   **Include return path in results**. If enabled, you must
   specify an IP address under **Source**.
10. To specify middlebox appliances in the routing path, choose
    **Middlebox appliance?**. We store this information for use
    in future analyses. You can update your middlebox appliances later on as needed.
11. Choose **Run route analysis**.
12. The results are displayed under **Results of route
    analysis**. If you specified **Middlebox appliance?**,
    choose **Yes** or **No** for each of the
    attachments to indicate the location of the appliances and to complete the route
    analysis.

You can choose the ID of any of the resources in the path to view more
information about the resources.
