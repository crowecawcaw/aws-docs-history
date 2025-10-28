# CreateFolderMembership

Use the `CreateFolderMembership` to add an asset, such as a dashboard,
analysis, or dataset, to a folder. To use this operation, you need the member ID of
the asset that you want to add to a folder. The member ID is either the dashboard,
analysis, or dataset ID of the analysis, dashboard, or dataset that you want to add
to a folder. The member ID is part of the analysis, dashboard, or dataset URL in
Quick Sight. You can also use the `ListAnalyses`, `ListDashboards`,
or `ListDataSets` operations to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-folder-membership
    --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
    --member-id `444455556666`
    --member-type `DASHBOARD`
```

You can also make this command using a CLI skeleton file with the following command.
For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-folder-membership
    --cli-input-json file://`createfoldermembership`.json
```

For more information about the `CreateFolderMembership`
operation, see [CreateFolderMembership](../APIReference/API_CreateFolderMembership.md "../APIReference/API_CreateFolderMembership.md") in the _Quick Sight API Reference_.
