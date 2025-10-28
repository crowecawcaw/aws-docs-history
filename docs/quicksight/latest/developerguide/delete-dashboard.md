# DeleteDashboard

Use the `DeleteDashboard` API operation to delete a dashboard. To use this operation, you need the ID of the dashboard that you want to delete. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

You can add a `VersionNumber` parameter to this operation to only delete the specified version of the dashboard.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-dashboard
    --aws-account-id `555555555555`
    --dashboard-id `DASHBOARDID`
```

For more information about the `DeleteDashboard` API operation, see [DeleteDashboard](../APIReference/API_DeleteDashboard.md "../APIReference/API_DeleteDashboard.md") in the _Amazon Quick Sight API Reference_.
