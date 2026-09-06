

# DescribeIAMPolicyAssignment
<a name="describe-iam-policy-assignment"></a>

Use the `DescribeIAMPolicyAssignment` API operation to describe an existing IAM policy assignment.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-iam-policy-assignment
    --aws-account-id {{AWSACCOUNTID}} 
    --assignment-name {{ASSIGNMENT}} 
    --namespace {{default}}
```

------

For more information about the `DescribeIAMPolicyAssignment` API operation, see [DescribeIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeIAMPolicyAssignment.html) in the *Amazon Quick Sight API Reference*.