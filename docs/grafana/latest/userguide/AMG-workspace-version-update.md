# Update your workspace version

You can update your Amazon Managed Grafana workspace to a newer version of Grafana in the Amazon Managed Grafana
console in two ways.

###### Note

You can only update the version to a newer version of Grafana. You can't downgrade
to a previously released version of Grafana.

Updating your version of Grafana will not update the plugins that are installed in
your workspace. You might need to individually update any plugins that are not
compatible with the new version of Grafana. For details on viewing and managing
plugins, see [Find plugins with the plugin catalog](grafana-plugins.md#plugin-catalog "grafana-plugins.md#plugin-catalog"). For a
list of changes in each version, see [Differences between Grafana versions](version-differences.md "version-differences.md").

###### Option 1 - Update the version from the list of workspaces

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana](https://console.aws.amazon.com/grafana "https://console.aws.amazon.com/grafana").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. In the row containing the details for the workspace you want to update, choose
   **Update version**. Only workspaces that are eligible to be
   updated will include this option.

###### Warning

The update process is irreversible and can't be paused or canceled. We
recommend testing the newer version in a non-production environment before
updating a production workspace. During an update, you can't make changes to
the workspace. 5. Choose a version number from the dropdown on the **Update
version** screen and click **Update** to
confirm. 6. Periodically check the status of your update on the
**Workspaces** tab. The update process could take up to 10
minutes. During this process, the workspace will be in 'read only' mode. A
banner update will display to indicate if your workspace update succeeded or
failed. If your update failed, follow the action items outlined in the banner
and try again.

###### Option 2 - Update the version from the workspace summary page

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana](https://console.aws.amazon.com/grafana "https://console.aws.amazon.com/grafana").
2. In the left navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the hyperlinked **Workspace name** of the workspace
   you want to update. Only workspaces that are eligible to be updated will include
   this option.
5. Choose the **Update version** prompt in the
   **Summary** block.

###### Warning

The update process is irreversible and can't be paused or canceled. We
recommend testing the newer version in a non-production environment before
updating a production workspace. During an update, you can't make changes to
the workspace. 6. Choose a version number from the dropdown on the **Update
version** screen and click **Update** to
confirm. 7. Periodically check the status of your update on the
**Workspaces** tab. The update process could take up to 10
minutes. During this process, the workspace will be in 'read only' mode. A
banner update will display to indicate if your workspace update succeeded or
failed. If your update failed, follow the action items outlined in the banner
and try again.

###### Note

You can also update the version using the [UpdateWorkspaceConfiguration](../APIReference/API_UpdateWorkspaceConfiguration.md "../APIReference/API_UpdateWorkspaceConfiguration.md") operation in the Amazon Managed Grafana API.

If you run into issues with your updated workspace, see [Troubleshooting issues
with updated workspaces](AMG-workspace-version-update-troubleshoot.md "AMG-workspace-version-update-troubleshoot.md").
