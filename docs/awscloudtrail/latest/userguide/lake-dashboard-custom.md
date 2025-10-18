# Create a custom dashboard with the CloudTrail
 console

You can create custom dashboards and add up to 10 widgets to each custom dashboard.
 You can choose to add sample widgets or create new widgets from SQL queries.

After you're done adding widgets, you can manually refresh the dashboard or set a
 refresh schedule.

###### To create a custom dashboard

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
 **Dashboard**.
3. Choose the **Managed and custom dashboards** tab.
4. Choose **Build my own dashboard**.
5. Provide a dashboard name to identify your dashboard.
6. For **Permissions**, choose the event data stores that you
 want to apply permissions to. Because CloudTrail runs queries to populate data for the
 widgets on a dashboard, CloudTrail requires permissions to run queries on the event
 data stores associated with the dashboard's widgets. For each event data store
 selected in this step, CloudTrail attaches a resource-based policy to the event data
 store that allows CloudTrail to run queries on the event data store for this
 dashboard.
7. (Optional) In the **Tags** section, you can add up to 50 tag
 key pairs to help you identify and sort your dashboards. For more information
 about how you can use tags in AWS, see [Tagging
 AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html "https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html") in the *Tagging AWS Resources User
 Guide*.
8. Choose **Create dashboard**.


Next, you can add widgets and [set a
 refresh schedule](lake-dashboard-refresh.md "lake-dashboard-refresh.md").
###### Topics

* [Add a sample widget with the CloudTrail
 console](lake-dashboard-custom-widgets.md "lake-dashboard-custom-widgets.md")
* [Create a new widget from a SQL
 query with the CloudTrail console](lake-dashboard-custom-widgets-new.md "lake-dashboard-custom-widgets-new.md")
* [Remove a widget from a
 dashboard with the CloudTrail console](lake-dashboard-custom-widgets-remove.md "lake-dashboard-custom-widgets-remove.md")
