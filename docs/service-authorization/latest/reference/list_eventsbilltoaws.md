# Actions, resources, and condition keys for AWS reInvent event pass amount charge to customer AWS account

AWS reInvent event pass amount charge to customer AWS account (service prefix: `eventsbilltoaws`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.md "../../../eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.md").
- View a list of the [API operations available for
  this service](../../../eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.md "../../../eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../eventsbilltoaws/latest/reference/security-iam.md "../../../eventsbilltoaws/latest/reference/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/eventsbilltoaws/eventsbilltoaws.json "https://servicereference.us-east-1.amazonaws.com/v1/eventsbilltoaws/eventsbilltoaws.json") for this service.

###### Topics

- [Actions defined by AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-actions-as-permissions "#list_eventsbilltoaws-actions-as-permissions")
- [Resource types defined by AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-resources-for-iam-policies "#list_eventsbilltoaws-resources-for-iam-policies")
- [Condition keys for AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-policy-keys "#list_eventsbilltoaws-policy-keys")

## Actions defined by AWS reInvent event pass amount charge to customer AWS account

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                | Description                                                                  | Resource types (\*required) | Condition keys                                                                                                                                                                                                                                                                                                                                        | Access level |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [approve](../../../eventsbilltoaws/latest/reference.md "../../../eventsbilltoaws/latest/reference.md") | Grants permission to approve or deny the reinvent pass charge to AWS account |                             | [aws:RequestTag/${TagKey}](#list_eventsbilltoaws-aws_RequestTag___TagKey_ "#list_eventsbilltoaws-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_ "#list_eventsbilltoaws-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_eventsbilltoaws-aws_TagKeys "#list_eventsbilltoaws-aws_TagKeys") | Write        |
| [info](../../../eventsbilltoaws/latest/reference.md "../../../eventsbilltoaws/latest/reference.md")    | Grants permission to get the AWS reinvent pass purchase details              |                             | [aws:RequestTag/${TagKey}](#list_eventsbilltoaws-aws_RequestTag___TagKey_ "#list_eventsbilltoaws-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_ "#list_eventsbilltoaws-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_eventsbilltoaws-aws_TagKeys "#list_eventsbilltoaws-aws_TagKeys") | Read         |

## Resource types defined by AWS reInvent event pass amount charge to customer AWS account

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                   | ARN                                                                 | Condition keys                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [approve](../../../eventsbilltoaws/latest/reference/security-iam.md "../../../eventsbilltoaws/latest/reference/security-iam.md") | arn:${Partition}:eventsbilltoaws:${Region}:${Account}:${RelativeId} | [aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_ "#list_eventsbilltoaws-aws_ResourceTag___TagKey_") |
| [info](../../../eventsbilltoaws/latest/reference/security-iam.md "../../../eventsbilltoaws/latest/reference/security-iam.md")    | arn:${Partition}:eventsbilltoaws:${Region}:${Account}:${RelativeId} | [aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_ "#list_eventsbilltoaws-aws_ResourceTag___TagKey_") |

## Condition keys for AWS reInvent event pass amount charge to customer AWS account

AWS reInvent event pass amount charge to customer AWS account defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                         | Description                                                          | Type          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/condition-keys-requesttag.md "../../../IAM/latest/UserGuide/condition-keys-requesttag.md")    | Filters access by the presence of tag key-value pairs in the request | String        |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/condition-keys-resourcetag.md "../../../IAM/latest/UserGuide/condition-keys-resourcetag.md") | Filters access by tag key-value pairs attached to the resource       | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/condition-keys-tagkeys.md "../../../IAM/latest/UserGuide/condition-keys-tagkeys.md")                       | Filters access by a key that is present in the request               | ArrayOfString |
