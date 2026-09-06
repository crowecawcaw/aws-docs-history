

# ListGroupMemberships
<a name="list-group-memberships"></a>

Use the `ListGroupMemberships` API operation to list member users in a group. To view a list of user groups in Amazon Quick Sight, call the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-group-memberships 
    --group-name {{GROUPNAME}} 
    --max-results {{100}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --namespace {{NAMESPACE}}
```

------

For more information about the `ListGroupMemberships` API operation, see [ListGroupMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListGroupMemberships.html) in the *Amazon Quick Sight API Reference*.