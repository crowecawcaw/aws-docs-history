

# Initialize Performance Monitor

Before you can use Performance Monitor, you must initialize it for your account. Initialization sets up the required permissions and creates the monitoring scope. Creating the initial topology and completing initialization can take 20 to 30 minutes.

Creating the first monitor or adding accounts to the scope automatically creates the initial scope and the service-linked role in your AWS account. The scope is shared between Performance Monitor and Network Flow Monitor. Any changes that you make to the scope, such as adding or removing accounts, apply to both.

When you initialize Performance Monitor, Performance Monitor automatically does the following:

1. **Service-linked role creation** – Performance Monitor uses the Network Flow Monitor service-linked role, `AWSServiceRoleForNetworkFlowMonitor`, with the minimum permissions needed to publish metrics and generate topology snapshots. For more information, see [Service-linked roles for Network Flow Monitor](using-service-linked-roles-network-flow-monitor.md).

1. **Scope creation** – Performance Monitor creates a monitoring scope for your account, or uses your existing Network Flow Monitor scope. For a standalone account or a member account, the scope initially contains only your current account and Region. For a management account, the scope includes all accounts in your organization. For a delegated administrator account, the scope includes all accounts in your organization except the management account.

1. **Topology generation** – Performance Monitor generates a topology of network resources within your scope to map network paths.

You don't need to modify your existing resources. Initialization is a one-time setup per account.

**Topics**
+ [Initialize Performance Monitor for a single account](CloudWatch-PerformanceMonitor-single-account.md)
+ [Initialize Performance Monitor for multiple accounts](CloudWatch-PerformanceMonitor-multi-account.md)