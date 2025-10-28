# Manage permissions for data sources

and notification channels

Your Amazon Managed Grafana workspace must have permission to access AWS data sources for your
metrics and notification channels for your alerts. You can use the Amazon Managed Grafana console to
have Amazon Managed Grafana automatically create AWS Identity and Access Management (IAM) policies and permissions for the
AWS data sources and notification channels that you want to use in the Amazon Managed Grafana
workspace.

###### To manage permissions and policies for data sources and notification

channels

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace that you want to manage.
5. To switch between using **Service managed** and
   **Customer managed** permissions, choose the edit icon for
   **IAM role** and then make your selection. For more
   information, see [Amazon Managed Grafana permissions and policies for AWS data
   sources](AMG-manage-permissions.md "AMG-manage-permissions.md").

If you change from **Service managed** permissions to
**Customer managed** permissions, the roles and policies
that Amazon Managed Grafana created for you are not deleted in the current account. If you
were using **Service managed** permissions for an organization,
the roles and policies in other accounts in the organization are deleted. 6. Choose the **Data sources** tab. 7. If you are using **Service managed** permissions, you can
choose **Edit** next to **IAM permission access
settings** to change whether your **Service
managed** permissions apply to only the current account or to an
entire organization. For more information, see [Amazon Managed Grafana permissions and policies for AWS data
sources](AMG-manage-permissions.md "AMG-manage-permissions.md").

Under **Data sources**, select the AWS data sources that
you want to query in this workspace. Selecting data sources enables Amazon Managed Grafana to
create the IAM roles and permissions that allow Amazon Managed Grafana to read data from
these sources. You must still add the data sources in the Grafana workspace
console.

To manage AWS services that can be used as notification channels, choose
**Notification channels**.

Select the AWS notification channel that you want to use in this workspace.
Selecting a notification channel enables Amazon Managed Grafana to create IAM roles and
permissions that allow Amazon Managed Grafana to use these services. You must still add the
notification channels in the Grafana workspace console.

###### Note

For more information about using notifications, see [Manage your alert
notifications](v9-alerting-managenotifications.md "v9-alerting-managenotifications.md").
