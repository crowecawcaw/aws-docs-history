

# What is Performance Monitor?

Performance Monitor is a feature of Amazon CloudWatch Network Monitoring. Performance Monitors monitor the traffic of the VPCs that you select to determine whether the AWS network is causing issues for your workloads. Using Performance Monitor, you can identify network degradation across paths between Availability Zones and across Regions. Performance Monitor uses an impact score, which maps to an impact level of None, Low, Medium, or High, to indicate how much a network path is experiencing unusual degradation relative to its normal behavior and the broader network.

**Key features of Performance Monitor**
+ With Performance Monitor, you receive near-real-time health and latency metrics for AWS network paths serving your VPCs, so that you can quickly identify whether an AWS infrastructure issue is affecting your workloads.
+ To start monitoring, you select the VPCs to monitor. Performance Monitor automatically provides visibility into the network paths your traffic uses.
+ When your workloads experience network degradation, Performance Monitor helps you determine whether the issue is caused by an AWS infrastructure event or is isolated to a specific path segment. You can then focus troubleshooting on the appropriate area.
+ Performance Monitor supports cross-account and cross-Region visibility across your organization in AWS Organizations. From a management account or delegated administrator account, you can monitor VPCs across member accounts, and network paths across Regions, providing centralized network health visibility.

**How to use Performance Monitor**

With Performance Monitor, you create a monitor by selecting VPCs from your accounts. For organizations, you can select VPCs from any member account within your organization. Performance Monitor then provides visibility into the network paths your traffic uses, including paths between Availability Zones within a Region, paths across Regions (when destination account-Region pairs are in scope), and paths to AWS services such as Amazon S3, Amazon DynamoDB, and Amazon EC2.

When you create your first monitor, Performance Monitor automatically creates a scope for your account. The scope defines which account-Region pairs are included in monitoring, and it is shared with Network Flow Monitor. When you add VPCs from additional accounts, the scope expands cumulatively. You don't need to configure the scope separately. You can also add accounts and account-Region pairs to your scope manually on the **Account Configuration** page.

Performance Monitor also automatically creates a service-linked role on your behalf. This role grants Performance Monitor the permissions that it needs to access network telemetry for the VPCs in your scope.

Performance Monitor calculates an impact score for each network path. The impact score reflects degradation observed on the network paths that your traffic uses. Performance Monitor identifies these paths from your VPC traffic, and measures degradation at the path level, not for individual connections. It doesn't confirm that your workloads were affected, only that degradation was detected on a path your traffic uses. To confirm impact on your workloads, check your application's own health and performance metrics, for example by using Network Flow Monitor. For more information, see [Using Network Flow Monitor](CloudWatch-NetworkFlowMonitor.md).

Performance Monitor calculates the impact score by comparing recent packet loss and traffic on a path against other paths in the network and against that path's own recent history. A higher score means more degradation than what's typically observed for that path.
+ **High impact** – High AWS network degradation detected on this path. Your applications using this path might be affected. Check your application health.
+ **Medium impact** – AWS network degradation above normal levels. Keep watching; no immediate action is needed unless your applications report issues.
+ **Low impact** – Normal variation. Traffic is flowing normally. No action is needed.
+ **None** – No significant impact detected on this path. No action is needed.

The **Top network paths** view on the monitor details page shows your network paths ranked by impact score. Each path displays at the Availability Zone level (for example, `us-east-1a` to `us-west-2b`), with the ability to drill down into subnet-level flows. For each path, you can view the impact score, p95 latency, traffic volume, bytes transferred, associated VPCs, and account information.

You can set CloudWatch alarms on impact scores to get notified when degradation reaches Medium or High levels, for a specific path or for any path in a monitor.

**Topics**
+ [Supported Regions](CloudWatch-PerformanceMonitor-Regions.md)
+ [Components and features](CloudWatch-PerformanceMonitor-components.md)
+ [How it works](CloudWatch-PerformanceMonitor-how-it-works.md)
+ [Pricing](CloudWatch-PerformanceMonitor.pricing.md)