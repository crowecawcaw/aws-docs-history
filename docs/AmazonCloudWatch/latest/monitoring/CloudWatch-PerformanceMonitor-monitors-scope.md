

# Add inter-Region scope

To get full Availability Zone to Availability Zone granularity for inter-Region paths, add the missing destination account-Region pairs to your scope.

**To add an account-Region pair to your scope**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**.

1. Choose **Account Configuration**.

1. In the **Accounts in scope** section, choose **Manage Scope**.

1. Choose the destination accounts and their Regions, and then choose **Add to selection**.

1. Choose **Confirm**.

After you add account-Region pairs, Performance Monitor updates its topology and begins providing full Availability Zone to Availability Zone detail for paths to that destination. This process can take a few minutes.

After you make a change to your scope, you must wait about 20 minutes before you can make another change to the scope. This delay is because Performance Monitor requires time to update its topology information.

**Scope recommendations**

After your monitor is active, Performance Monitor analyzes traffic flows to identify destinations that aren't in your scope. When missing account-Region pairs are detected, a recommendation appears on the monitor details page. You can act on recommendations directly from the monitor details page.