

# Enable multipath resilience for a transit gateway peering attachment

Multipath resilience is a cross-Region feature for transit gateway peering attachments. When you enable multipath resilience, we replicate each packet across multiple paths on the AWS global network and de-duplicate the copies at the destination Region. Multipath resilience provides Daily Uptime of at least 99.999%, measured in Unavailable Seconds. For more information about the SLA, see [Multipath Resilience SLA](https://aws.amazon.com/vpc/features/vpc-multipath-resilience/sla) on the AWS website.

Multipath resilience has the following characteristics:
+ Multipath resilience applies to transit gateway peering attachments, not to VPC attachments or other attachment types.
+ Multipath resilience is available only when the two transit gateways are in different AWS Regions. At launch, the supported Regions are US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), and Europe (Ireland).
+ Both the requester and the accepter must enable multipath resilience on their side of the attachment before packet replication becomes active.

## Multipath resilience states
<a name="tgw-multipath-resilience-states"></a>

The following table describes the multipath resilience states on a transit gateway peering attachment.


| State | Description | 
| --- | --- | 
| Enabled | Both sides have enabled multipath resilience. Packet replication is active in both directions. | 
| Pending enablement | Multipath resilience was requested at creation time but at least one side has not yet enabled it. | 
| Disabled | Multipath resilience is not enabled, and packet replication is not active. | 

## Create a cross-Region transit gateway peering attachment with multipath resilience
<a name="tgw-create-peering-with-multipath-resilience"></a>

Enable multipath resilience when you create a cross-Region transit gateway peering attachment. The **Multipath resilience** field appears only after you choose **Another Region** for the accepter.

**To create a cross-Region transit gateway peering attachment with multipath resilience using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**, and then choose **Create transit gateway attachment**.

1. Under **Details**:

   1. In **Name tag**, enter an optional name.

   1. In **Transit gateway ID**, choose the requester transit gateway.

   1. In **Attachment type**, choose **Peering connection**.

1. Under **Peering connection attachment**:

   1. For **Account**, choose **My account** or **Other account**. If you choose **Other account**, enter the 12-digit **Account ID** for the accepter.

   1. For **Region**, choose **Another Region**, and then choose the accepter Region.

   1. In **Transit gateway (accepter)**, choose the transit gateway to peer with.

1. Under **Multipath resilience**, select **Enable multipath resilience**. Choose the **Info** link to open the help panel.

1. Choose **Create transit gateway attachment**.

What happens next depends on whether the accepter is in your account:
+ **My account**: The attachment becomes **Available**, and multipath resilience shows **Enabled** immediately.
+ **Other account**: The attachment moves to **Pending acceptance**, and multipath resilience is not active until the accepter accepts and enables it. For more information, see [Accept a cross-account peering attachment with multipath resilience](#tgw-accept-peering-multipath-resilience).

## View multipath resilience status for a transit gateway peering attachment
<a name="tgw-view-multipath-resilience"></a>

**To view multipath resilience status for a peering attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**, and then choose the attachment ID.

1. Review the alert banners at the top of the detail page for the current state.

1. Choose the **Multipath resilience** tab.

1. The **Multipath resilience** container shows the overall status and, for cross-account attachments, the per-side status for the **Requester** and **Accepter**. Choose the **Info** link to open the help panel.

To monitor the replicated traffic for the attachment, use the multipath resilience CloudWatch metrics. For more information, see [Multipath resilience metrics](transit-gateway-cloudwatch-metrics.md#transit-gateway-multipath-resilience-metrics).

## Accept a cross-account peering attachment with multipath resilience
<a name="tgw-accept-peering-multipath-resilience"></a>

If the requester created the attachment with multipath resilience enabled, the **Multipath resilience** row in the acceptance dialog reflects the requester's submission. You do not toggle it from the acceptance dialog.

**To accept a cross-account peering attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) using credentials for the accepter account.

1. In the navigation pane, choose **Transit gateway attachments**, and then choose the attachment ID.

1. Choose **Accept peering attachment** from the top alert or from the **Actions** menu.

1. In the **Accept transit gateway peering attachment** dialog, review the details. The **Multipath resilience** row shows **Enabled** or **Disabled** as submitted by the requester.

1. Choose **Accept attachment**.

After the attachment is accepted and both sides have enabled multipath resilience, packet replication is active in both directions. To change the per-side setting later, see [Modify multipath resilience on an existing transit gateway peering attachment](#tgw-modify-multipath-resilience).

## Modify multipath resilience on an existing transit gateway peering attachment
<a name="tgw-modify-multipath-resilience"></a>

Each side manages its own enablement. Multipath resilience activates only when both sides are enabled.

**To change the multipath resilience setting for your side using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**, and then choose the attachment ID.

1. Choose **Manage multipath resilience** from the **Multipath resilience** tab, or choose **Modify transit gateway attachment** on the **Actions** menu.

1. In the **Peering attachment** section, choose the **Info** link next to **Multipath resilience** to open the help panel, then select or clear **Multipath resilience** for your side.

1. Choose **Modify transit gateway attachment** or **Save changes**.

For cross-account attachments, the panel shows the peer's current setting. Both sides must be enabled for replication to activate.