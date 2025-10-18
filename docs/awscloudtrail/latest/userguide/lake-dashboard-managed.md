# View a managed dashboard with the CloudTrail
 console

CloudTrail Lake provides managed dashboards that show event trends for event data stores
 that collect management events, data events, and Insights events. These dashboards are managed by
 CloudTrail Lake. You cannot modify, add, or remove the widgets for these dashboards, however,
 you can save a managed dashboard as a custom dashboard if you want to modify the widgets
 or set a refresh schedule.

###### Note

You can only view managed dashboards for event data stores that exist in your account.

###### To view a managed dashboard

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
 **Dashboard**.
3. Choose the **Managed and custom dashboards** tab.
4. From **Managed dashboards**, choose the dashboard you
 want to view. For more information, see [Available managed dashboards](lake-managed-dashboards.md "lake-managed-dashboards.md").


###### Note

The dropdown shows only relevant event data stores for the selected
 dashboard. For example, if you choose dashboards focused on data events,
 like S3 data events, the dropdown will only show event data stores that are
 configured to collect data events.
5. Choose the event data store for the dashboard. CloudTrail will run queries on this
 dashboard when the dashboard is refreshed.
6. To view the query for a widget, choose **View and edit
 query** at the bottom of the widget.
7. Choose to filter the dashboard data by an **Absolute range**
 or **Relative range**. Choose **Absolute
 range** to select a specific date and time range. Choose
 **Relative range** to select a predefined time range or a
 custom range. By default, the dashboard displays event data for the past 24
 hours.


###### Note

CloudTrail Lake queries incur costs based upon the amount of data scanned. To
 help control costs, you can filter on a narrower time range. For more
 information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
8. Choose the refresh icon to populate the graphics for the dashboard's
 widgets. Each widget indicates the status of the refresh.

## Save a managed dashboard as a custom
 dashboard


You cannot modify a managed dashboard, but you can save a copy as a custom
 dashboard. This allows you to set a refresh schedule for the dashboard and modify
 the widgets.


###### To save a managed dashboard as a custom dashboard

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
 **Dashboard**.
3. Choose the **Managed and custom dashboards** tab.
4. Choose the managed dashboard that you want to create a copy of.
5. Choose **Save as new dashboard**.
6. Provide a name to identify the dashboard.
7. (Optional) In the **Tags** section, you can add up to 50
 tag key pairs to help you identify and sort your dashboards. For more
 information about how you can use tags in AWS, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html") in the *Tagging AWS
 Resources User Guide*.
8. For **Permissions**, choose the event data stores that
 you want to apply permissions to. Because CloudTrail runs queries to populate data
 for the widgets on a dashboard, CloudTrail requires permissions to run queries on
 the event data store associated with the dashboard's widgets. For each event
 data store selected in this step, CloudTrail attaches a resource-based policy to
 the event data store that allows CloudTrail to run queries. You can deselect an
 event data store if you do not want to allow permissions.
9. Choose **Create dashboard**.

After you create the custom dashboard, you can [add widgets](lake-dashboard-custom-widgets.md "lake-dashboard-custom-widgets.md"), [remove widgets](lake-dashboard-custom-widgets-remove.md "lake-dashboard-custom-widgets-remove.md"), and [set a refresh schedule](lake-dashboard-refresh.md "lake-dashboard-refresh.md") for the
 dashboard.
