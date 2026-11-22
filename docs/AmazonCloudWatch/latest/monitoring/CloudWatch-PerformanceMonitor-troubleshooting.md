

# Troubleshoot issues in Performance Monitor

This section describes common issues and resolutions for Performance Monitor.

## No data appears after I create a monitor
<a name="CloudWatch-PerformanceMonitor-troubleshooting-no-data"></a>
+ Make sure that your VPCs have active traffic. Performance Monitor only shows paths with observed traffic.
+ Allow a few minutes for initial topology generation and data collection.
+ Verify that the service-linked role was created successfully.

## Inter-Region paths show only Region-to-Region detail
<a name="CloudWatch-PerformanceMonitor-troubleshooting-inter-region-detail"></a>

The destination account-Region pair isn't in your scope. Add it on the **Account Configuration** page, or act on the recommendation shown on the monitor details page.

## VPCs are missing from the selection list
<a name="CloudWatch-PerformanceMonitor-troubleshooting-missing-vpcs"></a>
+ For single-account users, only VPCs in the current Region are shown.
+ For multi-account users, make sure that your management or delegated administrator account has permissions to view resources in the member accounts. For more information, see [Set up permissions for multi-account resource access (console only)](CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.console-perms).
+ Verify that the service-linked role has the necessary Amazon EC2 read-only permissions in the member account.

## Impact scores seem inaccurate or diluted
<a name="CloudWatch-PerformanceMonitor-troubleshooting-impact-scores"></a>

Check whether you have incomplete scope coverage. Missing account-Region pairs can result in diluted impact scores because of incomplete topology information. Make sure that all relevant destination pairs are in scope.

## Scope limit reached
<a name="CloudWatch-PerformanceMonitor-troubleshooting-scope-limit"></a>

You've reached the maximum of 1,000 account-Region pairs per scope. Prioritize the most critical destination pairs for your workloads.