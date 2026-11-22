

# Enable multipath resilience for a VPC peering connection

Multipath resilience for Amazon VPC peering connections replicates packets across multiple paths on the AWS global network and de-duplicates the copies at the destination Region, so the application receives each packet once. You enable multipath resilience on both sides of a cross-Region peering connection.

Multipath resilience has the following characteristics:
+ **Cross-Region only.** Multipath resilience is available only when the requester and the accepter VPCs are in different AWS Regions. At launch, the supported Regions are US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland).
+ **Bilateral consent.** Both the requester and the accepter must enable multipath resilience on their side of the connection before packet replication becomes active.
+ **Reversible.** Either side can disable multipath resilience on its side at any time.

## Multipath resilience states
<a name="multipath-resilience-states"></a>

The following table describes the multipath resilience states on a VPC peering connection.


| State | Description | 
| --- | --- | 
| Enabled | Both sides have enabled multipath resilience. Packet replication is active in both directions. | 
| Pending enablement | Multipath resilience was requested at creation time but at least one side has not yet enabled it. | 
| Disabled | Multipath resilience is not enabled, and packet replication is not active. | 

## Create a cross-Region VPC peering connection with multipath resilience
<a name="create-peering-with-multipath-resilience"></a>

Enable multipath resilience when you create a cross-Region VPC peering connection. The **Multipath resilience** field appears only after you choose **Another Region** for the accepter.

**To create a cross-Region VPC peering connection with multipath resilience using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**, and then choose **Create peering connection**.

1. Under **Peering connection settings**, in **Name** enter an optional name, and in **VPC ID (Requester)** select the VPC in your account to peer from.

1. Under **Select another VPC to peer with**, do the following:

   1. For **Account**, choose **My account** or **Another account**. If you choose **Another account**, enter the 12-digit **Account ID** for the accepter.

   1. For **Region**, choose **Another Region**, and then choose the accepter Region. Multipath resilience is available only for cross-Region connections.

   1. In **VPC ID (Accepter)**, select or enter the accepter VPC.

1. Under **Multipath resilience**, select **Enable multipath resilience**. Choose the **Info** link to open the help panel.

1. (Optional) Expand **Tags** and add tags to the connection.

1. Choose **Create peering connection**.

What happens next depends on whether the peer VPC is in your account:
+ **Same account:** The connection moves to **Provisioning**, and multipath resilience shows **Enabled** immediately because both sides are you.
+ **Cross-account:** The connection moves to **Pending acceptance**, and multipath resilience is not active until the accepter accepts and enables it. For more information, see [Accept a cross-account peering request with multipath resilience](#accept-peering-multipath-resilience).

## View multipath resilience status for a VPC peering connection
<a name="view-multipath-resilience-peering"></a>

**To view the multipath resilience status for a peering connection using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Choose the ID of the peering connection to open its detail page.

1. Review the alert banners at the top of the detail page for the current state.

1. Choose the **Multipath resilience** tab.

1. The **Multipath resilience** container shows the overall status, and for cross-account connections, the per-side status for the **Requester** and **Accepter**. Choose the **Info** link to open the help panel.

To monitor the replicated traffic for the connection, use the multipath resilience CloudWatch metrics. For more information, see [Multipath resilience metrics and dimensions](multipath-resilience-metrics-peering.md).

## Accept a cross-account peering request with multipath resilience
<a name="accept-peering-multipath-resilience"></a>

If the requester created the connection with multipath resilience enabled, the **Multipath resilience** row in the acceptance dialog reflects the requester's submission. You do not toggle it from the acceptance dialog.

**To accept a cross-account peering request using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) using credentials for the accepter account.

1. In the navigation pane, choose **Peering connections**.

1. You can accept the request from either the list page or the detail page:

   1. On the **Peering connections** list page, select the peering connection, and then choose **Accept peering request** from the **Actions** menu.

   1. Or, open the peering connection detail page, and then choose **Accept peering request** from the top alert or from the **Actions** menu.

1. In the **Accept VPC peering connection request** dialog, review the details. The **Multipath resilience** row shows **Enabled** or **Disabled** as submitted by the requester.

1. Choose **Accept peering request**.

After the connection is accepted and both sides have enabled multipath resilience, packet replication is active in both directions. If the accepter has not yet enabled it on their side, see [Enable or disable multipath resilience on an existing VPC peering connection](#modify-multipath-resilience-peering).

## Enable or disable multipath resilience on an existing VPC peering connection
<a name="modify-multipath-resilience-peering"></a>

Each side manages its own enablement. Multipath resilience activates only when both sides are enabled.

**To change the multipath resilience setting for your side using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**, and then choose the peering connection ID.

1. Choose **Manage multipath resilience** from the **Multipath resilience** tab or from the **Actions** menu.

1. Select or clear **Enable multipath resilience**. For cross-account connections, the panel shows the peer's current setting; both sides must be enabled for replication to activate.

1. Choose **Save changes**. A confirmation notification appears, and the detail page reopens with the **Multipath resilience** tab selected.