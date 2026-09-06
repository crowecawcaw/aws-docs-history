

# DescribeDashboard
<a name="describe-dashboard"></a>

Use the `DescribeDashboard` API operation to view the summary of a dashboard. To use this operation, you need the ID of the dashboard that you want to view. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-dashboard 
    --aws-account-id {{555555555555}} 
    --dashboard-id {{DASHBOARDID}}
```

------

For more information about the `DescribeDashboard` API operation, see [DescribeDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboard.html) in the *Amazon Quick Sight API Reference*.