# UpdateFolder

Use the `UpdateFolder` operation to update the name of a folder. To use
this operation, you need the ID of the folder whose permissions you want to view. The
folder ID is part of the folder URL in Quick Sight. You can also use the
`ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-folder
    --aws-account-id `AWSACCOUNTID`
    --folder-id `FOLDERID`
    --name `NAME`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-folder
    --cli-input-json file://`updatefolder`.json
```

For more information about the `UpdateFolder` operation, see [UpdateFolder](../APIReference/API_UpdateFolder.md "../APIReference/API_UpdateFolder.md") in the _Quick Sight API Reference_.
