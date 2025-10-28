# ListUserGroups

Use the `ListUserGroups` operation to list the Quick Sight groups that an Quick Sight user is a member of. To use this operation, you need the ID of the user whose group memberships you want to know. You can use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight list-user-groups
    --user-name `USERNAME`
    --aws-account-id `AWSACCOUNTID`
    --namespace `default`
    --max-results `100`
```

For more information about `ListUserGroups` operation, see [ListUserGroups](../APIReference/API_ListUserGroups.md "../APIReference/API_ListUserGroups.md")in the _Quick Sight API Reference_.
