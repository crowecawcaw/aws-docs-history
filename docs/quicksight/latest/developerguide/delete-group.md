

# DeleteGroup
<a name="delete-group"></a>

Use the `DeleteGroup` API operation to remove a user group from Amazon Quick Sight. You can find a group name by calling the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-group 
    --group-name {{GROUPNAME}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{default}}
```

------

For more information about the `DeleteGroup` API operation, see [DeleteGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteGroup.html) in the *Amazon Quick Sight API Reference*.