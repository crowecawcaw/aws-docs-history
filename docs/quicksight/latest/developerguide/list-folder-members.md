

# ListFolderMembers
<a name="list-folder-members"></a>

Use the `ListFolderMembers` operation to list all assets (`DASHBOARD`, `ANALYSIS`, and `DATASET`) that are in a folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-folder-members 
    --aws-account-id {{AWSACCOUNTID}} 
    --folder-id {{FOLDERID}}
    --page-size {{10}} 
    --max-items {{100}}
```

------

For more information about the `ListFolderMembers` operation, see [ListFolderMembers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListFolderMembers.html) in the *Quick Sight API Reference*.