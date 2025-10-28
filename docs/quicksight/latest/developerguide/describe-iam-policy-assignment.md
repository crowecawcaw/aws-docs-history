# DescribeIAMPolicyAssignment

Use the `DescribeIAMPolicyAssignment` API operation to describe an existing IAM policy assignment.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operation.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-iam-policy-assignment
    --aws-account-id `AWSACCOUNTID`
    --assignment-name `ASSIGNMENT`
    --namespace `default`
```

For more information about the `DescribeIAMPolicyAssignment` API operation, see [DescribeIAMPolicyAssignment](../APIReference/API_DescribeIAMPolicyAssignment.md "../APIReference/API_DescribeIAMPolicyAssignment.md") in the _Amazon Quick Sight API Reference_.
