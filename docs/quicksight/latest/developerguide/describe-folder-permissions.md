# DescribeFolderPermissions

Use the `DescribeFolderPermissions` operation to describe the permissions of a folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-folder-permissions
    --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
```

You can find the folder ID by using a `ListFolders` operation or through the URL in the Quick Sight user interface.

For more information about the `DescribeFolderPermissions` operation, see [DescribeFolderPermissions](../APIReference/API_DescribeFolderPermissions.md "../APIReference/API_DescribeFolderPermissions.md") in the _Quick Sight API Reference_.
