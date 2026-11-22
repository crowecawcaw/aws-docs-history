

# Get started with Performance Monitor

To help you get started, this section provides a high-level overview of the steps to configure and gain insights with Performance Monitor.

1. **Initialize Performance Monitor.** Creating the first monitor or adding accounts to the scope automatically creates the initial scope and the service-linked role in your AWS account. If you want to observe network performance for paths across multiple accounts, you must integrate with AWS Organizations by turning on trusted access on the **Account Configuration** page. For more information, see [Initialize Performance Monitor](CloudWatch-PerformanceMonitor-initialize.md).

1. **Create a monitor.** Select the VPCs whose network paths you want to monitor. For organizations, you can select VPCs from member accounts. For more information, see [Create a monitor in Performance Monitor](CloudWatch-PerformanceMonitor-monitors-create.md).

1. **Review top network paths.** The **Top network paths** view in your monitor shows paths ranked by impact score, with Availability Zone-level detail and subnet drill-down.

1. **(Optional) Add inter-Region scope.** If your traffic flows to other Regions, add destination account-Region pairs to your scope for full Availability Zone to Availability Zone granularity on inter-Region paths. Performance Monitor can recommend missing pairs based on detected traffic, or you can add them on the **Account Configuration** page. For more information, see [Add inter-Region scope](CloudWatch-PerformanceMonitor-monitors-scope.md).

1. **Set up alarms.** Create CloudWatch alarms on impact scores to get notified when degradation on any path in your monitor reaches High levels. For more information, see [Create alarms with Performance Monitor](CloudWatch-PerformanceMonitor-create-alarm.md).

1. **Review your monitors regularly.** Do the following:
   + Review the **Top network paths** view in your monitors to identify and troubleshoot network degradation.
   + Check for scope recommendations to help maintain complete path visibility.