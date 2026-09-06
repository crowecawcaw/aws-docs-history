

# UpdateUser
<a name="update-user"></a>

Use the `UpdateUser` operation to update an Quick Sight user. To use this operation, you need the ID of the user that you want to delete. You can use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-user
    --aws-account-id {{555555555555}}
    --username {{USERNAME}}
    --namespace {{NAMESPACE}}
    --email {{johndoe@example.com}}
    --role {{ROLE}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-user 
    --cli-input-json file://{{updateuser}}.json
```

------

For more information about `UpdateUser` operation, see [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html)in the *Quick Sight API Reference*.