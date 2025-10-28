# Delete a Amazon Managed Grafana workspace

If you delete an Amazon Managed Grafana workspace, all the configuration data for that workspace is
also deleted. This includes dashboards, data source configuration, alerts, and
snapshots.

###### To delete an Amazon Managed Grafana workspace

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace that you want to delete.
5. Choose **Delete**.
6. To confirm the deletion, enter the name of the workspace and choose
   **Delete**.

###### Note

This procedure deletes a workspace. Other resources may not be deleted. For
example, IAM roles that were in use by the workspace are not deleted (but may be
unlocked if they are no longer in use).
