# DescribeDashboardPermissions

Use the `DescribeDashboardPermissions` API operation to view the read and write permissions for a dashboard. To use this operation, you need the ID of the dashboard whose permissions you want to view. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-dashboard-permissions
    --aws-account-id `555555555555`
    --dashboard-id `111122223333`
```

For more information about the `DescribeDashboardPermissions` API operation, see [DescribeDashboardPermissions](../APIReference/API_DescribeDashboardPermissions.md "../APIReference/API_DescribeDashboardPermissions.md") in the _Amazon Quick Sight API Reference_.
