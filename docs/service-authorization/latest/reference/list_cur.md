# Actions, resources, and condition keys for AWS Cost and Usage Report

AWS Cost and Usage Report (service prefix: `cur`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../cur/latest/userguide.md "../../../cur/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../aws-cost-management/latest/APIReference.md "../../../aws-cost-management/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../cur/latest/userguide/security.md "../../../cur/latest/userguide/security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/cur/cur.json "https://servicereference.us-east-1.amazonaws.com/v1/cur/cur.json") for this service.

###### Topics

- [API operations defined by AWS Cost and Usage Report](#list_cur-operations "#list_cur-operations")
- [Actions defined by AWS Cost and Usage Report](#list_cur-actions-as-permissions "#list_cur-actions-as-permissions")
- [Permission-only actions for AWS Cost and Usage Report](#list_cur-permission-only-actions "#list_cur-permission-only-actions")
- [Resource types defined by AWS Cost and Usage Report](#list_cur-resources-for-iam-policies "#list_cur-resources-for-iam-policies")
- [Condition keys for AWS Cost and Usage Report](#list_cur-policy-keys "#list_cur-policy-keys")

## API operations defined by AWS Cost and Usage Report

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cur-actions-as-permissions "#list_cur-actions-as-permissions").

| Operation                                                                      | IAM action                                                                                                               | Condition key | Possible value(s) | Access level   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | -------------- |
| DeleteReportDefinition                                                         | [cur:DeleteReportDefinition](#list_cur-action-DeleteReportDefinition "#list_cur-action-DeleteReportDefinition")          |               |                   | Write          |
| DescribeReportDefinitions                                                      | [cur:DescribeReportDefinitions](#list_cur-action-DescribeReportDefinitions "#list_cur-action-DescribeReportDefinitions") |               |                   | Read           |
| ListTagsForResource                                                            | [cur:ListTagsForResource](#list_cur-action-ListTagsForResource "#list_cur-action-ListTagsForResource")                   |               |                   | Read           |
| ModifyReportDefinition                                                         | [cur:ModifyReportDefinition](#list_cur-action-ModifyReportDefinition "#list_cur-action-ModifyReportDefinition")          |               |                   | Write          |
| PutReportDefinition                                                            | [cur:PutReportDefinition](#list_cur-action-PutReportDefinition "#list_cur-action-PutReportDefinition")                   |               |                   | Write          |
| [cur:TagResource](#list_cur-action-TagResource "#list_cur-action-TagResource") |                                                                                                                          |               | Tagging, Write    |
| TagResource                                                                    | [cur:TagResource](#list_cur-action-TagResource "#list_cur-action-TagResource")                                           |               |                   | Tagging, Write |
| UntagResource                                                                  | [cur:UntagResource](#list_cur-action-UntagResource "#list_cur-action-UntagResource")                                     |               |                   | Tagging, Write |

## Actions defined by AWS Cost and Usage Report

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                    | Description                                                  | Resource types (\*required)                              | Condition keys                                                                                                                                                                                                                                                                | Access level   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [DeleteReportDefinition](../../../aws-cost-management/latest/APIReference/API_cur_DeleteReportDefinition.md "../../../aws-cost-management/latest/APIReference/API_cur_DeleteReportDefinition.md")          | Grants permission to delete Cost and Usage Report Definition | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") |                                                                                                                                                                                                                                                                               | Write          |
| [DescribeReportDefinitions](../../../aws-cost-management/latest/APIReference/API_cur_DescribeReportDefinitions.md "../../../aws-cost-management/latest/APIReference/API_cur_DescribeReportDefinitions.md") | Grants permission to get Cost and Usage Report Definitions   |                                                          |                                                                                                                                                                                                                                                                               | Read           |
| [ListTagsForResource](../../../aws-cost-management/latest/APIReference/API_cur_ListTagsForResource.md "../../../aws-cost-management/latest/APIReference/API_cur_ListTagsForResource.md")                   | Grants permission to list tags for a resource                | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") | [aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_ "#list_cur-aws_ResourceTag___TagKey_")                                                                                                                                                                        | Read           |
| [ModifyReportDefinition](../../../aws-cost-management/latest/APIReference/API_cur_ModifyReportDefinition.md "../../../aws-cost-management/latest/APIReference/API_cur_ModifyReportDefinition.md")          | Grants permission to modify Cost and Usage Report Definition | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") |                                                                                                                                                                                                                                                                               | Write          |
| [PutReportDefinition](../../../aws-cost-management/latest/APIReference/API_cur_PutReportDefinition.md "../../../aws-cost-management/latest/APIReference/API_cur_PutReportDefinition.md")                   | Grants permission to write Cost and Usage Report Definition  | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") | [aws:RequestTag/${TagKey}](#list_cur-aws_RequestTag___TagKey_ "#list_cur-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_ "#list_cur-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_cur-aws_TagKeys "#list_cur-aws_TagKeys") | Write          |
| [TagResource](../../../aws-cost-management/latest/APIReference/API_cur_TagResource.md "../../../aws-cost-management/latest/APIReference/API_cur_TagResource.md")                                           | Grants permission to tag a resource                          | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") | [aws:RequestTag/${TagKey}](#list_cur-aws_RequestTag___TagKey_ "#list_cur-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_ "#list_cur-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_cur-aws_TagKeys "#list_cur-aws_TagKeys") | Tagging, Write |
| [UntagResource](../../../aws-cost-management/latest/APIReference/API_cur_UntagResource.md "../../../aws-cost-management/latest/APIReference/API_cur_UntagResource.md")                                     | Grants permission to untag a resource                        | [cur\*](#list_cur-resource-cur "#list_cur-resource-cur") | [aws:ResourceTag/${TagKey}](#list_cur-aws_ResourceTag___TagKey_ "#list_cur-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_cur-aws_TagKeys "#list_cur-aws_TagKeys")                                                                                                        | Tagging, Write |

## Permission-only actions for AWS Cost and Usage Report

The following actions are defined by AWS Cost and Usage Report but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                | Description                                                                                                                                           | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetClassicReport](../../../cur/latest/userguide/security.md#user-permissions "../../../cur/latest/userguide/security.md#user-permissions")            | Grants permission to get Bills CSV report                                                                                                             |                             |                | Read         |
| [GetClassicReportPreferences](../../../cur/latest/userguide/security.md#user-permissions "../../../cur/latest/userguide/security.md#user-permissions") | Grants permission to get the classic report enablement status for Usage Reports                                                                       |                             |                | Read         |
| [GetUsageReport](../../../cur/latest/userguide/security.md#user-permissions "../../../cur/latest/userguide/security.md#user-permissions")              | Grants permission to get list of AWS services, usage type and operation for the Usage Report workflow. Allows or denies download of usage reports too |                             |                | Read         |
| [PutClassicReportPreferences](../../../cur/latest/userguide/security.md#user-permissions "../../../cur/latest/userguide/security.md#user-permissions") | Grants permission to enable classic reports                                                                                                           |                             |                | Write        |
| [ValidateReportDestination](../../../cur/latest/userguide/security.md#user-permissions "../../../cur/latest/userguide/security.md#user-permissions")   | Grants permission to validates if the s3 bucket exists with appropriate permissions for CUR delivery                                                  |                             |                | Read         |

## Resource types defined by AWS Cost and Usage Report

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                     | ARN                                                                | Condition keys |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------- |
| [cur](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md") | arn:${Partition}:cur:${Region}:${Account}:definition/${ReportName} |                |

## Condition keys for AWS Cost and Usage Report

AWS Cost and Usage Report defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                             | Description                                                   | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters access by the tags that are passed in the request     | String        |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters access by the tags associated with the resource       | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters access by the tag keys that are passed in the request | ArrayOfString |
