# Creating a CloudWatch cross-account cross-Region dashboard with the
 AWS Management Console

You can create *cross-account cross-Region dashboards*, which
 summarize your CloudWatch data from multiple AWS accounts and multiple Regions into one
 dashboard. From this high-level dashboard you can get a view of your entire application,
 and also drill down into more specific dashboards without having to sign in and out of
 accounts or switch Regions.


###### Prerequisite


Before you can create a cross-account cross-Region dashboard, you must enable at least one
 sharing account and at least one monitoring account. Additionally, to be able to use the
 CloudWatch console to create a cross-account dashboard, you must enable the console for
 cross-account functionality. For more information, see [Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md").


###### To create a cross-account cross-Region dashboard

1. Sign in to the monitoring account.
2. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Dashboards**.
4. Choose a dashboard, or create a new one.
5. At the top of the screen, you can switch between accounts and Regions.
 As you create your dashboard, you can include widgets from multiple
 accounts and Regions. Widgets include graphs, alarms, and CloudWatch Logs Insights
 widgets.
