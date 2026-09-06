

# UpdateIAMPolicyAssignment
<a name="update-iam-policy-assignment"></a>

Use the `UpdateIAMPolicyAssignment` API operation to update an existing IAM policy assignment. This operation updates only the optional parameters that are specified in the request. It overwrites all of the users included in `Identities`.

To find a policy assignment name, call the `ListIAMPolicyAssignments` or `ListIAMPolicyAssignmentsForUser` API operations.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-iam-policy-assignment
    --aws-account-id {{AWSACCOUNTID}} 
    --assignment-name {{NAME}} 
    --namespace {{default}}
    --assignment-status {{ENABLED}} 
    --policy-arn {{222244446666}} 
    --identities KEY={{VALUE}},{{VALUE}},KEY={{VALUE}},{{VALUE}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-iam-policy-assignment 
    --cli-input-json file://{{updateiampolicyassignment}}.json
```

------

For more information about the `UpdateIAMPolicyAssignment` API operation, see [UpdateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIAMPolicyAssignment.html) in the *Amazon Quick Sight API Reference*.