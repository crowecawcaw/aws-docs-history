

# DeleteIAMPolicyAssignment
<a name="delete-iam-policy-assignment"></a>

Use the `DeleteIAMPolicyAssignment` API operation to delete an existing IAM policy assignment.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-iam-policy-assignment
    --aws-account-id {{AWSACCOUNTID}} 
    --assignment-name {{ASSIGNMENT}} 
    --namespace {{default}}
```

------

For more information about the `DeleteIAMPolicyAssignment` API operation, see [DeleteIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteIAMPolicyAssignment.html) in the *Amazon Quick Sight API Reference*.