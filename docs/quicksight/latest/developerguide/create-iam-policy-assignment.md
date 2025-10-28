# CreateIAMPolicyAssignment

Use the `CreateIAMPolicyAssignment` API operation to create an
assignment with one specified IAM policy, identified by its Amazon Resource Name
(ARN). This policy assignment is attached to the specified groups or users of Amazon Quick Sight.
Assignment names are unique for each AWS account. To avoid overwriting rules in other
namespaces, use assignment names that are unique.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-iam-policy-assignment
    --aws-account-id `AWSACCOUNTID`
    --assignment-name `ASSIGNMENT`
    --assignment-status `ENABLED`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-iam-policy-assignment
    --cli-input-json file://`createiampolicyassignment`.json
```

For more information about the `CreateIAMPolicyAssignment` API operation, see [CreateIAMPolicyAssignment](../APIReference/API_CreateIAMPolicyAssignment.md "../APIReference/API_CreateIAMPolicyAssignment.md") in the _Amazon Quick Sight API Reference_.
