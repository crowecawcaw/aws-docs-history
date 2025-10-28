# DeleteUser

Use the `DeleteUser` operation to delete the Quick Sight user that is associated
with the identity of the IAM user or role that's making the call. The
IAM user isn't deleted as a result of this call. To use this operation, you need the
ID of the user that you want to delete. You can also use the `ListUsers`
operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-user
    --user-name `USERNAME`
    --aws-account-id `AWSACCOUNTID`
    --namespace `default`
```

For more information about the `DeleteUser` operation, see [DeleteUser](../APIReference/API_DeleteUser.md "../APIReference/API_DeleteUser.md") in the _Quick Sight API Reference_.
