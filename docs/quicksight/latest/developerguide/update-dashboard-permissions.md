# UpdateDashboardPermissions

Use the `UpdateDashboardPermissions` API operation to update read and write permissions for a dashboard. You can grant or revoke permissions in the same command. To use this operation, you need the ID of the dashboard whose permissions you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-dashboard-permissions
    --aws-account-id `555555555555`
    --dashboard-id `DASHBOARDID`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`555555555555`:user/default/`USERNAME`,Actions=quicksight:DescribeDashboard,quicksight:QueryDashboard,quicksight:ListDashboardVersions
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`555555555555`:user/default/`USERNAME`,Actions=quicksight:DescribeDashboard,quicksight:QueryDashboard,quicksight:ListDashboardVersions
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-dashboard-permisisons
    --cli-input-json file://`updatedashboardpermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDashboardPermissions` API operation, see [UpdateDashboardPermissions](../APIReference/API_UpdateDashboardPermissions.md "../APIReference/API_UpdateDashboardPermissions.md") in the _Amazon Quick Sight API Reference_.
