# ListDashboardVersions

Use the `ListDashboardVersions` API operation to list all the versions of a dashboard in an AWS account. To use this operation, you need the ID of the dashboard that you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-dashboard-versions
    --aws-account-id `AWSACCOUNTID`
    --dashboard-id `DASHBOARD`
    --page-size `10`
    --max-items `100`
```

For more information about the `ListDashboardVersions` API operation, see [ListDashboardVersions](../APIReference/API_ListDashboardVersions.md "../APIReference/API_ListDashboardVersions.md") in the _Amazon Quick Sight API Reference_.
