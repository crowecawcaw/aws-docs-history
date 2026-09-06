

# DescribeUser
<a name="describe-user"></a>

Use the `DescribeUser` operation to return information about a user, given the user name. Following is an example AWS CLI command for this operation. To use this operation, you need the ID of the user that you want to describe. You can also use the `ListUsers` operation to list all users and their corresponding user IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-user 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{default}}
```

------

For more information about the `DescribeUser` operation, see [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html) in the *Quick Sight API Reference*.