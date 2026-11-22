

# Delete the scope in Performance Monitor

Before you can delete your scope, you must delete all of your Performance Monitor and Network Flow Monitor monitors. It can take about 15 minutes to complete removing monitors after you request to delete them. For more information, see [Delete a monitor in Performance Monitor](CloudWatch-PerformanceMonitor-monitors-delete.md).

**To delete your scope**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**.

1. Choose **Account Configuration**.

1. Choose **Delete scope**.

1. Confirm the deletion.

Deleting your scope removes all account-Region pairs and turns off monitoring. You must initialize Performance Monitor again to use it.