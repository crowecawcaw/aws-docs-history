

# Initialize Performance Monitor for multiple accounts

To monitor VPCs across multiple accounts in your organization, you must turn on trusted access to grant CloudWatch permission to discover resources in your organization.

**To initialize Performance Monitor for multiple accounts**

1. Sign in with your management account or a delegated administrator account.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**.

1. On the **Account Configuration** page, choose **Turn on trusted access**.

1. Review the service-linked role permissions, and then choose **Accept**.

1. (Recommended) Register a delegated administrator account.

After configuration, the following applies:
+ When you create your first monitor, Performance Monitor creates a scope that includes all accounts in your organization. If you use a delegated administrator account, the scope excludes the management account.
+ You can select VPCs from any member account when you create monitors.
+ The scope expands cumulatively as you add accounts.
+ Performance Monitor automatically creates the service-linked role in each member account.

**Important**  
The service-linked role grants Amazon EC2 read-only access across member accounts. With this access, Performance Monitor can list VPCs, subnets, and instances for network topology mapping. It doesn't grant access to data within your instances or applications. We recommend that you sign in as the delegated administrator to add accounts. You can add and work with multiple accounts from the management account, but we don't recommend it.

For more information about configuring AWS Organizations for network monitoring, see [Configure AWS Organizations in CloudWatch](CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.config-orgs).