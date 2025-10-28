# DeleteGroupMembership

Use the `DeleteGroupMembership` API operation to remove a user from a group
so that the user is no longer a member of the group. You can find users in a certain group by calling the `ListGroups` API operation, and then the `ListGroupMemberships` operation on the group that you choose.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-group-membership
    --member-name `USERNAME`
    --group-name `GROUPNAME`
    --aws-account-id `AWSACCOUNTID`
    --namespace `NAMESPACE`
```

For more information about the `DeleteGroupMembership` API operation, see [DeleteGroupMembership](../APIReference/API_DeleteGroupMembership.md "../APIReference/API_DeleteGroupMembership.md") in the _Amazon Quick Sight API Reference_.
