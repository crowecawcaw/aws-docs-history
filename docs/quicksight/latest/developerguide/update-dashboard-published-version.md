

# UpdateDashboardPublishedVersion
<a name="update-dashboard-published-version"></a>

Use the `UpdateDashboardPublishedVersion` API operation to update the published version of a dashboard. To use this operation, you need the ID of the published dashboard that you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-dashboard-published-version 
    --aws-account-id {{555555555555}} 
    --dashboard-id {{DASHBOARDID}} 
    --dashboard-version-number {{VERSION}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-dashboard-published-version
    --cli-input-json file://{{updatedashboardpublishedversion}}.json
```

------

For more information about the `UpdateDashboardPublishedVersion` API operation, see [UpdateDashboardPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPublishedVersion.html) in the *Amazon Quick Sight API Reference*.