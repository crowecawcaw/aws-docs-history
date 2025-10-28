# DescribeFolder

Use the `DescribeFolder` operation to describe a folder. To use this
operation, you need the ID of the folder whose permissions you want to view. The folder
ID is part of the folder URL in Quick Sight. You can also use the `ListFolders`
operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-folder
    --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
```

For more information about the `DescribeFolder` operation, see [DescribeFolder](../APIReference/API_DescribeFolder.md "../APIReference/API_DescribeFolder.md") in the _Quick Sight API Reference_.
