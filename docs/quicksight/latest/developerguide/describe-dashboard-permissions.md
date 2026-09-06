

# DescribeDashboardPermissions
<a name="describe-dashboard-permissions"></a>

Use the `DescribeDashboardPermissions` API operation to view the read and write permissions for a dashboard. To use this operation, you need the ID of the dashboard whose permissions you want to view. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-dashboard-permissions
    --aws-account-id {{555555555555}}
    --dashboard-id {{111122223333}}
```

------

For more information about the `DescribeDashboardPermissions` API operation, see [DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardPermissions.html) in the *Amazon Quick Sight API Reference*.