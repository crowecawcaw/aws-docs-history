

# Viewing Amazon Q Developer user activity on the dashboard
<a name="dashboard"></a>

Available only for Amazon Q Developer administrators, the Amazon Q Developer dashboard summarizes useful data about how your Pro tier subscribers use the service.

![The Amazon Q dashboard that shows total subscriptions, active subscriptions, pending subscriptions, a suggested lines of code widget, an active users widget, and filters.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/q-dev-dashboard.png)


Amazon Q generates and displays new metrics on an hourly basis for the most part. The only section that is not updated hourly is the **Active users** widget, which is updated daily according to the coordinated universal time (UTC) clock.

The dashboard shows metrics collected from users who are subscribed in:
+ the AWS account that you're currently signed into

  *and*
+ member accounts, if you're signed in to a management account for which [organization-wide visibility of subscriptions](subscribe-visibility.md) has been enabled.
**Note**  
The **Active users** widget only displays information from the account that you're currently signed into.

**To view and filter the dashboard**

1. Sign in to the AWS Management Console.

1. Switch to the Amazon Q Developer console.

1. From the navigation pane, choose **Dashboard**.

1. (Optional) Filter the information by date range, programming language, customization, or integrated development environment (IDE) vendor.

**Notes**:
+ If the **Dashboard** link is not available in the navigation pane, see [Troubleshooting the dashboard](dashboard-troubleshooting.md).
+ If you’d like to send user metrics to a daily report with a per-user breakdown of their Amazon Q Developer usage, see [Viewing the activity of specific users in Amazon Q Developer](q-admin-user-telemetry.md).
+ For information about specific metrics, see [Descriptions of Amazon Q Developer dashboard usage metrics](dashboard-metrics-descriptions.md) or choose the help link (![The help link.](http://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/images/help-icon.png)) on the dashboard page.