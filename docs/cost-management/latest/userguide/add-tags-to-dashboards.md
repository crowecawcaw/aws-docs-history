# Adding tags to dashboards

Tags help you identify, organize, and manage your dashboards by adding descriptive labels.
You might tag your dashboards to identify which department created them, track them by project
or initiative, label their purpose, or mark them for different environments. For example, you
could use tags like Department = Marketing or Project = Cost-Optimization-2025 to categorize
your dashboards.

When you have many dashboards across your organization, tags become particularly valuable.
They allow you to filter and search for specific dashboards, control access through IAM
policies based on tag values, and track dashboards that serve similar purposes across
different teams. If you use the AWS CLI or SDK, tags also help you manage related dashboards
as a group.

###### To add tags to a dashboard

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Dashboards**.
3. Select the dashboard you want to tag.
4. Choose **Actions**, and then choose **Manage tags**
   from the dropdown list.
5. Choose **Add new tag**.
6. Enter the key and value (optional) for the tag.
7. Choose **Add new tag** to add additional tags. The maximum number of
   tags that you can add is 50
8. Choose **Save changes**.
   After you save changes, the tags are applied to your dashboard and can be used for
   filtering and access control.
