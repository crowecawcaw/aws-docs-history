# Internet Monitor cross-account observability

With Internet Monitor cross-account observability, you can monitor your applications that span multiple AWS accounts within a single AWS Region.

You can use Amazon CloudWatch Observability Access Manager to set up one or more of your AWS accounts as a monitoring account. You’ll provide
the monitoring account with the ability to view data in your source account by creating a _sink_ in your monitoring account.
A sink is a resource that represents an attachment point in a monitoring account. For Internet Monitor, the resource attachment point is a monitor.
You use the sink to create a link from your source account to your monitoring account. For more information, see
[CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

###### Required resources

For proper functionality of CloudWatch Application Insights cross-account observability, ensure that the following telemetry types are shared through the CloudWatch Observability Access Manager.

- Monitors in Internet Monitor
- Metrics in Amazon CloudWatch
- Log groups in Amazon CloudWatch Logs
