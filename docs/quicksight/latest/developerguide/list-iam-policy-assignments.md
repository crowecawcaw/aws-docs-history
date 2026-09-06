

# ListIAMPolicyAssignments
<a name="list-iam-policy-assignments"></a>

Use the `ListIAMPolicyAssignments` API operation to list IAM policy assignments in the current Amazon Quick Sight account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-iam-policy-assignments
    --aws-account-id {{AWSACCOUNTID}} 
    --assignment-status {{ENABLED}} 
    --namespace {{default}} 
    --max-results {{100}}
```

------

For more information about the `ListIAMPolicyAssignments` API operation, see [ListIAMPolicyAssignments](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIAMPolicyAssignments.html) in the *Amazon Quick Sight API Reference*.