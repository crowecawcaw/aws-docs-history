# UpdateFolderPermissions

Use the `UpdateFolderPermissions` operation to update the permissions of a folder. You can grant or revoke permissions in the same command. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-folder-permissions --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USER`NAME``,Actions=quicksight:CreateFolder,quicksight:DescribeFolder,quicksight:UpdateFolder,quicksight:DeleteFolder,quicksight:CreateFolderMembership,quicksight:DeleteFolderMembership,quicksight:DescribeFolderPermissions,quicksight:UpdateFolderPermissions
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:CreateFolder,quicksight:DescribeFolder,quicksight:UpdateFolder,quicksight:DeleteFolder,quicksight:CreateFolderMembership,quicksight:DeleteFolderMembership,quicksight:DescribeFolderPermissions,quicksight:UpdateFolderPermissions
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-folder-permissions
    --cli-input-json file://`updatefolderpermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information on the `UpdateFolderPermissions` operation, see [UpdateFolderPermissions](../APIReference/API_UpdateFolderPermissions.md "../APIReference/API_UpdateFolderPermissions.md") in the _Quick Sight API Reference_.
