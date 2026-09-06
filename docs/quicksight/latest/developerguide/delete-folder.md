

# DeleteFolder
<a name="delete-folder"></a>

Use the `DeleteFolder` operation to delete an empty folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-folder 
    --aws-account-id {{AWSACCOUNTID}} 
    --folder-id {{FOLDERID}}
```

------

For more information about the `DeleteFolder` operation, see [DeleteFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteFolder.html) in the *Quick Sight API Reference*.