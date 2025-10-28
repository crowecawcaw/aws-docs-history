# DeleteFolderMembership

Use the `DeleteFolderMembership` to delete an asset, such as a
dashboard, analysis, or dataset, from a folder. To use this operation, you need the
member ID of the asset that you want to add to a folder. The member ID is either the
dashboard, analysis, or dataset ID of the analysis, dashboard, or dataset that you
want to add to a folder. The member ID is part of the analysis, dashboard, or
dataset URL in Quick Sight. You can also use the `ListAnalyses`,
`ListDashboards`, or `ListDataSets` operations to get the
ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-folder-membership
    --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
    --member-id `444455556666`
    --member-type `DASHBOARD`
```

For more information about the `DeleteFolderMembership` operation, see [DeleteFolderMembership](../APIReference/API_DeleteFolderMembership.md "../APIReference/API_DeleteFolderMembership.md") in the _Quick Sight API Reference_.
