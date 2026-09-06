

# DeleteUserByPrincipalTitle
<a name="delete-user-by-principal-title"></a>

The `DeleteUserByPrincipalTitle` operation deletes a user identified by a principal ID. Following is an example AWS CLI command for this operation. To use this operation, you need the ID of the user that you want to delete. You can also use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-user-by-principal-id 
    --principal-id {{PRINCIPALID}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{default}}
```

------

For more information about the `DeleteUserByPrincipalTitle` operation, see [DeleteUserByPrincipalTitle](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUserByPrincipalTitle.html) in the *Quick Sight API Reference*.