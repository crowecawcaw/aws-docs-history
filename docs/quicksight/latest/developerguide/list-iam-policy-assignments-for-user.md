

# ListIAMPolicyAssignmentsForUser
<a name="list-iam-policy-assignments-for-user"></a>

Use the `ListIAMPolicyAssignmentsForUser` API operation to list all the IAM policy assignments, including the Amazon Resource Names (ARNs), for the IAM policies assigned to the specified user and the groups that the user belongs to.

To find a user name, call the `ListUsers` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-iam-policy-assignments-for-user 
    --aws-account-id {{AWSACCOUNTID}} 
    --user-name {{USER}} 
    --max-results {{100}} 
    --namespace {{default}}
```

------

For more information about the `ListIAMPolicyAssignmentsForUser` API operation, see [ListIAMPolicyAssignmentsForUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIAMPolicyAssignmentsForUser.html) in the *Amazon Quick Sight API Reference*.