

# Access AWS Cloud WAN transit gateway network dashboards
<a name="cloudwan-tgw-networks"></a>

View dashboard information about transit gateways registered registered in your AWS Cloud WAN global network. For more information about the Cloud WAN transit gateway dashboards see [Cloud WAN transit gateway network dashboards](cloudwan-visualize-tgw.md#cloudwan-dashboard-tgw-network).

**Topics**
+ [Overview](#cloudwan-tgw-overview)
+ [Geography](#cloudwan-tgw-geography)
+ [Topology tree](#cloudwan-tgw-topology)
+ [Events](#cloudwan-tgw-events)
+ [Monitoring](#cloudwan-tgw-monitoring)
+ [Route analyzer](#cloudwan-tgw-routes)

## Overview
<a name="cloudwan-tgw-overview"></a>

The **Overview** page displays details about your Cloud WAN transit gateways, VPN and Connect peer status, and any network events affecting your transit gateways.

**To access transit gateway details**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. On the **Overview** page, you can view the following information:
   + Your transit gateway **Inventory**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-tgw-networks.html)
   + **Transit gateways VPN status**:
     + **ID** — The ID of the transit gateway. Choose the link to open details about the transit gateway.
     + **Name** — The name of the transit gateway.
     + **Region** — The Region where the transit gateway is located.
     + **Down VPN** — The percentage of your total transit gateway VPNs that are down.
     + **Impaired VPN** —The percentage of your total transit gateways VPNs that are impaired.
     + **Up VPN** — The percentage of your total transit gateway VPNs that are up.
   + **Transit gateways connect peer status**:
     + **ID** — The ID of the transit gateway.
     + **Name** — The name of the transit gateway.
     + **Region** — The Region where the transit peer is located.
     + **Down Connect peer** — The percentage of your total transit gateway Connect peers that are down.
     + **Impaired Connect peer** — The percentage of your total transit gateway Connect peers that are impaired.
     + **Up VPN** — The percentage of your total transit gateway Connect peers that are up.
   + The **Network events summary** displays CloudWatch Events and the number of core network attachments per edge, shown as a stacked column chart. 

     (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

     Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**  
The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region. 

## Geography
<a name="cloudwan-tgw-geography"></a>

The **Geography** page displays a world map showing the locations of your transit gateways.

**To access transit gateway details**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. Choose the **Geography** tab.

   A world map displays, showing you the locations of the following:
   + **AWS** **TGWs** and **VPCs**.
   + The **Connectivity** of **VPNs**, **Direct Connects**, and **Connect peers**.
   + **On-premises ****Sites** and **Devices**.
   + **Not associated** **Sites** and **Devices**.

## Topology tree
<a name="cloudwan-tgw-topology"></a>

The **Topology tree** page shows a logical diagram of your transit gateways.

**To access the topology tree for a transit gateway**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. Choose the **Topology tree** tab. 

1. By default, the **Topology tree** page displays all **Sites**, **Devices**, and **Customer Gateways** of your transit gateway and the logical relationships between them. You can filter the network tree to show specific resource types to view information about the specific resource represented. The line colors represent the state of the relationships between AWS and the on-premises resources.

## Events
<a name="cloudwan-tgw-events"></a>

Track your transit gateway events by using Amazon EventBridge, which delivers a near-real-time stream of system events that describe changes in your resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

**To track transit gateway events**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. Choose the **Events** tab.

   The **Events** section updates with the transit gateway events that occurred during the time frame.

   (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

   Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**  
The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region. 

## Monitoring
<a name="cloudwan-tgw-monitoring"></a>

You can monitor your transit gateways using Amazon CloudWatch, which collects raw data and processes it into readable, near-real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your network is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

On the monitoring page you can view usage metrics for your transit gateways, filtering by specific transit gateways.

**To access transit monitoring details**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. Choose the **Monitoring** tab.

1. Choose a transit gateway that you want to monitor.

1. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

   Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**  
The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region. 

1. The page updates the following transit gateway monitors:
   + **Bytes in**
   + **Bytes out**
   + **Bytes dropped – black hole**
   + **Bytes dropped – no route**
   + **Packets in**
   + **Packets out**
   + **Packets dropped – black hole**
   + **Packets dropped – no route**

1. (Optional) Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**  
The **Add to dashboard** option works only if your registered transit gateway is in the US West (Oregon) Region.

## Route analyzer
<a name="cloudwan-tgw-routes"></a>

The Route Analyzer analyzes the routing path between a specified source and destination.

**Note**  
Route Analyzer checks the routes on Transit Gateway route tables only.

**To analyze route information**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways. 

1. Choose the **Route Analyzer** tab.

1. In the **Source** section, do the following:
   + Choose the source **Transit Gateway** for the route that you want to analyze.
   + Choose the source **Transit Gateway attachment** for the route.
   + Enter either the IPv4 or IPv6 **IP address**.
   + Clear the **Include return path in results** check box if you don't want to include a return path.
   + Indicate whether this is a **Middlebox appliance**. For more information on middlebox configurations, see [Route analysis with a middlebox configuration ](https://docs.aws.amazon.com/network-manager/latest/tgwnm/example-route-analyzer-middlebox.html). 

1. In the Destination section, do the following:
   + Choose the destination **Transit Gateway**.
   + Choose the destination **Transit Gateway attachment** for the route.
   + Enter either the IPv4 or IPv6 **IP address**.

1. Choose **Run route analysis**.

1. The Results of route analysis return the **Source** and **Destination** transit gateways and the current **Status**. An error message is returned if no information is found in the transit gateway route table. For more information on route tables, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html). 