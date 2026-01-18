# Creating a custom

dashboard with Performance Insights

###### Important

AWS has announced the end-of-life date for Performance Insights: June 30, 2026. After this date, Amazon RDS will no longer support the Performance Insights console experience,
flexible retention periods (1-24 months), and their associated pricing. The Performance Insights API will continue to exist with no pricing changes. Costs for the
Performance Insights API will appear in your AWS bill with the cost of CloudWatch Database Insights.

We recommend that you upgrade any DB instances
using the paid tier of Performance Insights to the Advanced mode of Database Insights before June 30, 2026.
For information about upgrading to the Advanced mode of Database Insights, see
[Turning on the Advanced mode of Database Insights for Amazon RDS](USER_DatabaseInsights.md "USER_DatabaseInsights.md").

If you take no action, DB instances using Performance Insights
will default to using the Standard mode of Database Insights. With Standard mode of Database Insights, you might lose access to performance data history beyond 7 days and might not be able to use execution plans
and on-demand analysis features in the Amazon RDS console. After June 30, 2026 only the Advanced mode of Database Insights will support execution plans and on-demand analysis.

With CloudWatch Database Insights, you can monitor database load for your fleet of databases and analyze and troubleshoot performance at scale.
For more information about Database Insights, see [Monitoring Amazon RDS databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").
For pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

In the new monitoring view, you can create a custom dashboard with the metrics you
need to meet your analysis requirements.

You can create a custom dashboard by selecting Performance Insights and CloudWatch metrics for your DB instance.
You can use this custom dashboard for other DB instances of the same database
engine type in your AWS account.

###### Note

The customized dashboard supports up to 50 metrics.

Use the widget settings menu to edit or delete the dashboard, and move or resize the
widget window.

###### To create a custom dashboard with Performance Insights in the navigation pane

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance.
4. Scroll down to the **Metrics tab** in the window.
5. Select the custom dashboard from the drop down list. The following example
   shows the custom dashboard creation.

![Custom metrics dashboard with no widgets yet.](images/Monitoring_custmDashbrd_addWidget.png) 6. Choose **Add widget** to open the **Add
widget** window. You can open and view the available operating
system (OS) metrics, database metrics, and CloudWatch metrics in the window.

The following example shows the **Add widget** window with the metrics.

![The metrics options in the Add Widget window.](images/Monitoring_AddWidget.png) 7. Select the metrics that you want to view in the dashboard and choose
**Add widget**. You can use the search field to find a
specific metric.

The selected metrics appear on your dashboard. 8. (Optional) If you want to modify or delete your dashboard, choose the
settings icon on the upper right of the widget, and then select one of the following actions in the menu.

    * **Edit** – Modify the metrics list in the window. Choose
     **Update widget** after you select the metrics for
     your dashboard.
    * **Delete** – Deletes the widget. Choose
     **Delete** in the confirmation window.
