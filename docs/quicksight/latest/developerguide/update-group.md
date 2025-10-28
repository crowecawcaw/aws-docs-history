# UpdateGroup

Use the `UpdateGroup` API operation to change a group description. You can find a group name by calling the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-group
    --group-name `GROUPNAME`
    --description "`NEW DESCRIPTION`"
    --aws-account-id `AWSACCOUNTID`
    --namespace `default`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-group
    --cli-input-json file://`updategroup`.json
```

For more information about the `UpdateGroup` API operation, see [UpdateGroup](../APIReference/API_UpdateGroup.md "../APIReference/API_UpdateGroup.md") in the _Amazon Quick Sight API Reference_.
