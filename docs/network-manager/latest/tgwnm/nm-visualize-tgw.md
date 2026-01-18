# Access transit gateway dashboards using AWS Network Manager

The AWS Network Manager console provides a group of dashboards for AWS Global Networks for Transit Gateways, allowing you to view
and monitor your transit gateways. Dashboards include information about network resources, their
geographic locations, the network topology, and the logical network associations. If you
want to view the dashboards for all transit gateways in your global network, see [Access transit gateway network dashboards using AWS Network Manager](nm-monitoring-console.md "nm-monitoring-console.md").

###### Topics

- [Overview](#tgw-visualize-overview "#tgw-visualize-overview")
- [Topology tree](#tgw-visualize-geography "#tgw-visualize-geography")
- [Events](#tgw-visualize-events "#tgw-visualize-events")
- [Monitoring](#cloudwan-tgw-monitoring "#cloudwan-tgw-monitoring")
- [On-premises associations](#tgws-on-premises "#tgws-on-premises")
- [Connect peer associations](#tgws-connect-peer "#tgws-connect-peer")

## Overview

###### To access the transit gateway resource inventory

1.  Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2.  Under **Connectivity** choose **Global Networks**.
3.  On the **Global networks** page, choose the global network ID.
4.  In the navigation pane, choose **Transit Gateway networks**.
5.  The **Transit gateways** page opens, showing a list of your transit gateways.
6.  Choose the **ID** of the transit gateway you want to see more information about.
7.  On the **Overview** page you can view the following
    information:

        * Your transit gateway details.
        * The transit gateway attachments, along with information about each of
         those attachments.

    Use the following legend to understand the icons on this page:

| Icon                                  | Description                                                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| AWS Cloud WAN VPCs                    | **VPC**<br>The total number of VPC attachments in your transit gateway network.                                |
| AWS Cloud WAN VPNs                    | \*_VPN_<br>• The total number of VPN<br>attachments in your transit gateway.                                   |
| AWS Cloud WAN Direct Connect gateways | **Direct Connect Gateway**<br>The total number of Direct Connect gateways attached to<br>your transit gateway. |
| AWS Cloud WAN Connect peers           | **Connect**<br>The total number of Connect peer attachments in your<br>transit gateway.                        |
| AWS Cloud WAN transit gateways        | **Transit Gateway**<br>The total number of Transit Gateways.                                                   |

8. The **Details** section shows information about your global
   network: the transit gateway **ID**, its **Name**, the
   **Region** where it's located, and the current
   **State** of the gateway.

###### Note

To see details about a different transit gateway, choose the dropdown list and then
choose the transit gateway. 9. The **Transit Gateway attachment** section displays details
about your attachments: the Transit Gateway **ID**, the
**Resource ID**, and the **Resource
Type**. 10. The **VPNs** section displays details about your VPN
attachments: the VPN **ID**, the **Device**
using the VPN attachment, and any **Link** associated with the
attachment. 11. The **Connect peers** section displays details about your
Connect peer attachments: the name of the **Connect peer** and
the **Device** using that Connect peer. 12. The **Network events summary** section shows the network
events for that transit gateway. You must first onboard to see network
events. Choose **Onboard CloudWatch Insights** to enable viewing
network events. 13. (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.

## Topology tree

The **Topology tree** page shows a logical diagram of your transit
gateways.

###### To view a transit gateway topology tree

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway networks**.
5. The **Transit gateways** page opens, showing a list of your transit gateways.
6. Choose the **ID** of the transit gateway you want to see more information about.
7. Choose the **Topology tree** tab.
8. By default, the **Topology tree** page displays all
   **Sites**, **Devices**, and**Customer Gateways** of your transit gateway and the logical
   relationships between them. You can filter the network tree to show specific
   resources types only to view information about the specific resource it
   represents. The line colors represent the state of the relationships between
   AWS and the on-premises resources.
9. In the **Topology tree**, choose a resource. The resource
   details display in the right pane.
10. If your global network is part of a multi-account environment, you can choose
    a **Resource ID** from a member account and view details about
    that attachment.

Viewing details about a member's resources prompts you to switch Network Manager
console roles to the member account where the resource is located.

###### Note

Switching roles logs you out of the current account and into the delegated
administrator account associated with the attachment.

###### To view resource details in a member account

1. When choosing a link to a member account, you're prompted to switch console roles:

![Switch roles dialog box](/images/network-manager/latest/tgwnm/images/nm-switchrole.png) 2. The following values populate the **Switch Role**
screen. Keep the following values:

    * **Account** — The account ID for the member account
     that the resource is associated with.
    * **Role** —
     `IAMRoleForAWSNetworkManagerCrossAccountResourceAccess`
     is the required IAM role for accessing resources across multiple
     accounts.

3. Choose **Switch Role**.

You're logged out of your current account and into that member
account. A new tab opens showing the details of the resource. For
example, if you choose a VPC resource, the VPC resource page opens for
the member account that owns the resource. 4. Depending on the delegated permission level assigned to the delegated
administrators and the management account when trusted access was
enabled, you can either view information (read-only permission) about the
resource or add/modify (administrator permission) the resource. 5. To return to the original member account, choose one
of the following:

    * On your current tab, choose the browser
     **Back** button. On the **Switch
     Role** login screen, enter the
     **Account** ID of the account you want, and
     then choose **Switch Role**.
    * If you haven't closed it, choose the tab for the account
     you've just logged out of, and then choose
     **Reload**.

## Events

Track your transit gateway events using Amazon EventBridge that delivers a near-real-time stream of
system events that describe changes in your resources. Using simple rules that you can
quickly set up, you can match events and route them to one or more target functions or
streams. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### To track transit gateway events

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway network**.
5. The **Overview** page opens by default, showing information about your transit gateways.
6. Choose the **Events** tab.

The **Events** section updates with the events
that occurred during the time frame.

(Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see
[Using
Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User
Guide_.

###### Note

The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.

## Monitoring

You can monitor your transit gateways using Amazon CloudWatch, which collects raw data and
processes it into readable, near-real-time metrics. These statistics are kept for 15
months, so that you can access historical information and gain a better perspective on
how your network is performing. You can also set alarms that watch for certain
thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

On the monitoring page you can view usage metrics for your transit gateways, filtering
by specific transit gateways.

###### To view transit monitoring details

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway networks**.
5. The **Transit gateways** page opens, showing a list of your transit gateways.
6. Choose the **ID** of the transit gateway you want to see more information about.
7. Choose the **Monitoring** tab.
8. If you want to choose a different transit gateway to monitor, choose that
   transit gateway from the list.
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
    Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the Amazon CloudWatchUser Guide.

###### Note

The **Add to dashboard** option only works if your
registered transit gateway is in the US West (Oregon) Region.

## On-premises associations

The **On-premises** page displays information about your on-premises
devices for this transit gateway. On this page you can associate or disassociate any of your
devices..

###### To view on-premises associations

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway networks**.
5. The **Transit gateways** page opens, showing a list of your transit gateways.
6. Choose the **ID** of the transit gateway you want to see more information about.
7. Choose the **On-premises associations** tab.
8. The **Transit Gateway** on-premises association page displays
   the **Customer gateway**, **Device**,
   **Link**, and **State** of the
   transit gateway.

###### To associate a device

1. Choose the **Customer gateway** you want to associate a
   device with.
2. Choose **Associate**.
3. On the **Edit on-premises association** page, choose the
   **Device** and optional **Link** for the
   association.
4. Choose **Edit on-premises association**.

###### To disassociate an on-premises device

1. Choose the **Customer gateway** you want to disassociate.
2. Choose **Disassociate**.

## Connect peer associations

The Connect peer associations page displays information about your Connect peers for
this transit gateway. You can also disassociate any of your devices.

###### To access Connect peer associations

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Transit Gateway networks**.
5. The **Transit gateways** page opens, showing a list of your transit gateways.
6. Choose the **ID** of the transit gateway you want to see more information about.
7. Choose the **Connect peer associations** tab.
8. The **Connect peer associations** page displays the
   **Connect peer**, **Device**,
   **Link**, and **State** of the
   transit gateway.

###### To disassociate a Connect peer device

1. Choose the **Connect peer** you want to disassociate.
2. Choose **Disassociate**.
