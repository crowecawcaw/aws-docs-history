# Access AWS Cloud WAN transit gateway dashboards

View dashboard information about transit gateways registered in your AWS Cloud WAN global
network. For more information about the Cloud WAN transit gateway dashboards see [Cloud WAN transit gateway dashboards](cloudwan-visualize-tgw.md#cloudwan-dashboard-tgw "cloudwan-visualize-tgw.md#cloudwan-dashboard-tgw").

###### Transit gateway dashboards

- [Overview](#cloudwan-tgws-overview "#cloudwan-tgws-overview")
- [Topology tree](#cloudwan-tgws-topolgy-tree "#cloudwan-tgws-topolgy-tree")
- [Events](#cloudwan-tgws-events "#cloudwan-tgws-events")
- [Monitoring](#cloudwan-tgws-monitoring "#cloudwan-tgws-monitoring")
- [On-premises associations](#cloudwan-tgws-on-premises "#cloudwan-tgws-on-premises")
- [Connect peer](#cloudwan-tgws-connect-peer "#cloudwan-tgws-connect-peer")

## Overview

The **Overview** page displays details about your transit gateways, their VPN,
their Connect peer status, and any network events affecting the transit gateway.

###### To view transit gateway details

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. On the **Overview** page, you can view the following sections:
   - The **Transit Gateway** details section displays the transit gateway
     **ID**, **Name**,
     **Region**, and **State**. Choose
     a different transit gateway to view those details.
   - The **Attachments** section shows the number of each
     resource attached to the transit gateway. The following legend describes the
     attachments:

   | Icon                                  | Description                                                                                                    |
   | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
   | The icon for VPCs.                    | **VPC**<br>The total number of VPCs attached to your transit gateway.                                          |
   | The icon for VPN connections.         | **VPN**<br>The total number of VPNs attached to your transit gateway.                                          |
   | The icon for Direct Connect Gateways. | **Direct Connect Gateways**The<br>total number of Direct Connect Gateways attached to<br>your transit gateway. |
   | The icon for Connect attachments.     | **Connect**The total number of<br>Connect attachments on your transit gateway.                                 |
   | The icon for transit gateways.        | **Transit Gateway**The total number of<br>transit gateways.                                                    |
   - The **VPNs** section displays the VPN
     **ID**, **Device**,
     **Link**, **VPN status**, and
     **Tunnel status**.
   - The **Connect peers** section displays the Connect
     peer **ID**, **Device**,
     **Link**, **Status**, and
     **BGP status**.
   - The **Network events summary** displays events and the
     number of core network attachments per edge, shown as a stacked column
     chart.

   (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

   Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
   [Using
   Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
   Guide_.

   ###### Note

   The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.

## Topology tree

The **Topology tree** page shows a logical diagram of each
AWS Transit Gateway.

###### To access the topology tree for a transit gateway

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. Choose the **Topology tree** tab.
8. By default, the **Topology tree** page displays the
   **Sites**, **Devices**, and
   **Customer Gateways** of the chosen transit gateway and the
   logical relationships between them. You can filter the network tree to show
   specific resources types to view information about the specific resource
   represented. The line colors represent the state of the relationships between
   AWS and the on-premises resources.

## Events

Track your transit gateway **Events** using Amazon EventBridge, which delivers a
near-real-time stream of system events that describe changes in your resources. Using
simple rules that you can quickly set up, you can match events and route them to one or
more target functions or streams. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### To track transit gateway events

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. Choose the **Events** tab.

The **Events** section updates with the events
that occurred during the time frame for the chosen transit gateway.

(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.

## Monitoring

On the **Monitor** page, monitor your transit gateways using Amazon CloudWatch, which
collects raw data and processes it into readable, near-real-time metrics. These
statistics are kept for 15 months, so that you can access historical information and
gain a better perspective on how your network is performing. You can also set alarms
that watch for certain thresholds, and send notifications or take actions when those
thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

On the monitoring page, you can view usage metrics for your transit gateways,
filtering by specific transit gateways.

###### To access transit monitoring details

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. Choose the **Monitoring** tab.
8. Monitoring statistics display for the chosen transit gateway. Choose a
   different transit gateway to see those monitoring statistics.
9. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region. 10. The page updates the following transit gateway monitors:

    * **Bytes in**
    * **Bytes out**
    * **Bytes dropped – black hole**
    * **Bytes dropped – no route**
    * **Packets in**
    * **Packets out**
    * **Packets dropped – black hole**
    * **Packets dropped – no route**

11. (Optional) Choose **Add to dashboard** to add this metric to
    your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
    [Using
    Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User Guide_.

###### Note

The **Add to dashboard** option works only if your
registered transit gateway is in the US West (Oregon) Region.

## On-premises associations

The **On-premises** page displays information about your on-premises
devices for this transit gateway. On this page, you can associate or disassociate any of your
devices.

###### To access transit gateway on-premises associations

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. Choose the **On-premises associations** tab.
8. The **Transit Gateway** on-premises association page displays
   the **Customer gateway**, **Device**,
   **Link**, and **State** of the
   transit gateway.

###### To associate a device

1. Choose the **Customer gateway** that you want to associate a
   device with.
2. Choose **Associate**.
3. On the **Edit on-premises association** page, choose the
   **Device** and optional **Link** for the
   association.
4. Choose **Edit on-premises association**.

###### To disassociate an on-premises device

1. Choose the **Customer gateway** that you want to
   disassociate.
2. Choose **Disassociate**.

## Connect peer

The Connect peer page displays information about your associated Connect peers for
this transit gateway. On this page you can disassociate any of your devices.

###### To access on-premises associations

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link.
4. In the navigation pane, choose **Transit Gateways**.
5. On the **Transit gateways** page, choose the **ID** link that you want to view the dashboard for.
6. The **Overview** page opens by default.
7. Choose the **Connect peer associations** tab.
8. The **Connect peer associations** page displays the
   **Connect peer**, **Device**,
   **Link**, and **State** of the
   transit gateway.

###### To disassociate a Connect peer device

1. Choose the **Connect peer** that you want to
   disassociate.
2. Choose **Disassociate**.
