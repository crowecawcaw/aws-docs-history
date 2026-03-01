# DynamoDB API permissions: Actions, resources, and conditions reference

When you are setting up
[Identity and Access Management for Amazon DynamoDB](security-iam.md "security-iam.md") and writing a permissions policy that you can attach to an IAM identity
(identity-based policies), you can use the list of [Actions,
resources, and condition keys for Amazon DynamoDB](../../../service-authorization/latest/reference/list_amazondynamodb.md "../../../service-authorization/latest/reference/list_amazondynamodb.md") in the
_IAM User Guide_ as a reference. The page lists each
DynamoDB API operation, the corresponding actions for which you can grant
permissions to perform the action, and the AWS resource for which you can grant the
permissions. You specify the actions in the policy's `Action` field, and you
specify the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your DynamoDB policies to express
conditions. For a complete list of AWS-wide keys, see the [IAM JSON policy
elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

In addition to the AWS-wide condition keys, DynamoDB has its own specific keys that you
can use in conditions. For more information, see [Using IAM policy conditions for fine-grained access control](specifying-conditions.md "specifying-conditions.md").

## Related topics

- [Identity and Access Management for Amazon DynamoDB](security-iam.md "security-iam.md")
- [Using IAM policy conditions for fine-grained access control](specifying-conditions.md "specifying-conditions.md")
