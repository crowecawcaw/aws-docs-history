

# Create a monitor in Performance Monitor

**VPC selection**

VPC selection is limited to a single Region per monitor. You can select multiple VPCs within that Region, including VPCs from other accounts in your organization, if you're signed in with a management or delegated administrator account and have set up permissions to view resources in the member accounts. For more information, see [Set up permissions for multi-account resource access (console only)](CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.console-perms). The VPC selection interface provides the following:
+ A table view that can list up to 100 VPCs
+ Filtering by tags, account ID, and VPC name
+ Account ownership information for each VPC

**To create a monitor**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**.

1. On the **Monitors** tab, choose **Create Monitor**.

1. Enter a monitor name.

1. Select the VPCs to monitor. You can select VPCs from any account in your organization.
   + For management accounts, VPCs across all member accounts are visible. To view member-account VPCs, you must set up permissions. For more information, see [Set up permissions for multi-account resource access (console only)](CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.console-perms).
   + For member accounts, only VPCs in that account are visible.

1. Review your selections, and then choose **Create**.

After you create the monitor, Performance Monitor begins generating impact scores and path data for the selected VPCs. Initial data can take a few minutes to populate.