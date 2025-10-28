# DeleteIAMPolicyAssignment

Use the `DeleteIAMPolicyAssignment` API operation to delete an existing IAM policy assignment.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operation.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-iam-policy-assignment
    --aws-account-id `AWSACCOUNTID`
    --assignment-name `ASSIGNMENT`
    --namespace `default`
```

For more information about the `DeleteIAMPolicyAssignment` API operation, see [DeleteIAMPolicyAssignment](../APIReference/API_DeleteIAMPolicyAssignment.md "../APIReference/API_DeleteIAMPolicyAssignment.md") in the _Amazon Quick Sight API Reference_.
