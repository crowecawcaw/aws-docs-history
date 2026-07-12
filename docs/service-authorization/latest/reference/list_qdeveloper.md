# Actions, resources, and condition keys for Amazon Q Developer

Amazon Q Developer (service prefix: `qdeveloper`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md").
- View a list of the [API operations available for
  this service](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/qdeveloper/qdeveloper.json "https://servicereference.us-east-1.amazonaws.com/v1/qdeveloper/qdeveloper.json") for this service.

###### Topics

- [Actions defined by Amazon Q Developer](#list_qdeveloper-actions-as-permissions "#list_qdeveloper-actions-as-permissions")
- [Permission-only actions for Amazon Q Developer](#list_qdeveloper-permission-only-actions "#list_qdeveloper-permission-only-actions")
- [Resource types defined by Amazon Q Developer](#list_qdeveloper-resources-for-iam-policies "#list_qdeveloper-resources-for-iam-policies")
- [Condition keys for Amazon Q Developer](#list_qdeveloper-policy-keys "#list_qdeveloper-policy-keys")

## Actions defined by Amazon Q Developer

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                    | Description                                                                 | Resource types (\*required)                                                                                       | Condition keys                                                                                                                                                                                  | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [ExportArtifact](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")    | Grants permission to export artifacts from Amazon Q Developer               | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")                                                                            | Write        |
| [ImportArtifact](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")    | Grants permission to import artifacts to Amazon Q Developer                 | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")                                                                            | Write        |
| [StartAgentSession](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md") | Grants permission to start an agent session with Amazon Q Developer         |                                                                                                                   | [aws:RequestTag/${TagKey}](#list_qdeveloper-aws_RequestTag___TagKey_ "#list_qdeveloper-aws_RequestTag___TagKey_")<br>[aws:TagKeys](#list_qdeveloper-aws_TagKeys "#list_qdeveloper-aws_TagKeys") | Write        |
| [TransformCode](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")     | Grants permission to transform code with Amazon Q Developer Transform Agent | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")                                                                            | Write        |

## Permission-only actions for Amazon Q Developer

The following actions are defined by Amazon Q Developer but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                      | Description                                                                       | Resource types (\*required)                                                                                       | Condition keys                                                                                                                                                                                                                                                                                                          | Access level   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [ListTagsForResource](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md") | Grants permission to list all tags associated with an Amazon Q Developer resource | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")                                                                                                                                                                                                    | List           |
| [TagResource](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")         | Grants permission to associate tags with an Amazon Q Developer resource           | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:RequestTag/${TagKey}](#list_qdeveloper-aws_RequestTag___TagKey_ "#list_qdeveloper-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_qdeveloper-aws_TagKeys "#list_qdeveloper-aws_TagKeys") | Tagging, Write |
| [UntagResource](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")       | Grants permission to remove tags associated with an Amazon Q Developer resource   | [codeTransformation](#list_qdeveloper-resource-codeTransformation "#list_qdeveloper-resource-codeTransformation") | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_qdeveloper-aws_TagKeys "#list_qdeveloper-aws_TagKeys")                                                                                                                      | Tagging, Write |

## Resource types defined by Amazon Q Developer

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                  | ARN                                                                               | Condition keys                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [codeTransformation](../../../amazonq/latest/qdeveloper-ug/codeTransformation.md "../../../amazonq/latest/qdeveloper-ug/codeTransformation.md") | arn:${Partition}:qdeveloper:${Region}:${Account}:codeTransformation/${Identifier} | [aws:ResourceTag/${TagKey}](#list_qdeveloper-aws_ResourceTag___TagKey_ "#list_qdeveloper-aws_ResourceTag___TagKey_") |

## Condition keys for Amazon Q Developer

Amazon Q Developer defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                               | Description                                                                | Type          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md")  | Filters access by the tags that are passed in the request                  | String        |
| [aws:ResourceTag/${TagKey}](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md") | Filters access by the tags associated with the Amazon Q Developer resource | String        |
| [aws:TagKeys](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md")               | Filters access by the tag keys that are passed in the request              | ArrayOfString |
