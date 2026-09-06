

# DescribeFolderResolvedPermissions
<a name="describe-folder-resolved-permissions"></a>

Use the `DescribeFolderResolvedPermissions` operation to describe the resolved permissions of a folder. Permissions consist of both folder direct permissions and the inherited permissions from the ancestor folders. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-folder-resolved-permissions 
    --aws-account-id {{AWSACCOUNTID}} 
    --folder-id {{FOLDERID}}
```

------

For more information about the `DescribeFolderResolvedPermissions` operation, see [DescribeFolderResolvedPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolderResolvedPermissions.html) in the *Quick Sight API Reference*.