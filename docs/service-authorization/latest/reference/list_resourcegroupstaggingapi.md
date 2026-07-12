# Actions, resources, and condition keys for Amazon Resource Group Tagging API

Amazon Resource Group Tagging API (service prefix: `tag`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md").
- View a list of the [API operations available for
  this service](../../../resourcegroupstagging/latest/APIReference.md "../../../resourcegroupstagging/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../ARG/latest/userguide/gettingstarted-prereqs.md "../../../ARG/latest/userguide/gettingstarted-prereqs.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/tag/tag.json "https://servicereference.us-east-1.amazonaws.com/v1/tag/tag.json") for this service.

###### Topics

- [API operations defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-operations "#list_resourcegroupstaggingapi-operations")
- [Actions defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-actions-as-permissions "#list_resourcegroupstaggingapi-actions-as-permissions")
- [Resource types defined by Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-resources-for-iam-policies "#list_resourcegroupstaggingapi-resources-for-iam-policies")
- [Condition keys for Amazon Resource Group Tagging API](#list_resourcegroupstaggingapi-policy-keys "#list_resourcegroupstaggingapi-policy-keys")

## API operations defined by Amazon Resource Group Tagging API

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_resourcegroupstaggingapi-actions-as-permissions "#list_resourcegroupstaggingapi-actions-as-permissions").

| Operation              | IAM action                                                                                                                                                | Condition key | Possible value(s) | Access level   |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | -------------- |
| DescribeReportCreation | [tag:DescribeReportCreation](#list_resourcegroupstaggingapi-action-DescribeReportCreation "#list_resourcegroupstaggingapi-action-DescribeReportCreation") |               |                   | Read           |
| GetComplianceSummary   | [tag:GetComplianceSummary](#list_resourcegroupstaggingapi-action-GetComplianceSummary "#list_resourcegroupstaggingapi-action-GetComplianceSummary")       |               |                   | Read           |
| GetResources           | [tag:GetResources](#list_resourcegroupstaggingapi-action-GetResources "#list_resourcegroupstaggingapi-action-GetResources")                               |               |                   | Read           |
| GetTagKeys             | [tag:GetTagKeys](#list_resourcegroupstaggingapi-action-GetTagKeys "#list_resourcegroupstaggingapi-action-GetTagKeys")                                     |               |                   | Read           |
| GetTagValues           | [tag:GetTagValues](#list_resourcegroupstaggingapi-action-GetTagValues "#list_resourcegroupstaggingapi-action-GetTagValues")                               |               |                   | Read           |
| ListRequiredTags       | [tag:ListRequiredTags](#list_resourcegroupstaggingapi-action-ListRequiredTags "#list_resourcegroupstaggingapi-action-ListRequiredTags")                   |               |                   | List           |
| StartReportCreation    | [tag:StartReportCreation](#list_resourcegroupstaggingapi-action-StartReportCreation "#list_resourcegroupstaggingapi-action-StartReportCreation")          |               |                   | Write          |
| TagResources           | [tag:TagResources](#list_resourcegroupstaggingapi-action-TagResources "#list_resourcegroupstaggingapi-action-TagResources")                               |               |                   | Tagging, Write |
| UntagResources         | [tag:UntagResources](#list_resourcegroupstaggingapi-action-UntagResources "#list_resourcegroupstaggingapi-action-UntagResources")                         |               |                   | Tagging, Write |

## Actions defined by Amazon Resource Group Tagging API

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                       | Description                                                                                                                                                                            | Resource types (\*required) | Condition keys | Access level   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | -------------- |
| [DescribeReportCreation](../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md") | Grants permission to describe the status of the StartReportCreation operation                                                                                                          |                             |                | Read           |
| [GetComplianceSummary](../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md "../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md")       | Grants permission to retrieve a summary of how many resources are noncompliant with their effective tag policies                                                                       |                             |                | Read           |
| [GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md")                               | Grants permission to return tagged or previously tagged resources in the specified AWS Region for the calling account                                                                  |                             |                | Read           |
| [GetTagKeys](../../../resourcegroupstagging/latest/APIReference/API_GetTagKeys.md "../../../resourcegroupstagging/latest/APIReference/API_GetTagKeys.md")                                     | Grants permission to returns tag keys currently in use in the specified AWS Region for the calling account                                                                             |                             |                | Read           |
| [GetTagValues](../../../resourcegroupstagging/latest/APIReference/API_GetTagValues.md "../../../resourcegroupstagging/latest/APIReference/API_GetTagValues.md")                               | Grants permission to return tag values for the specified key that are used in the specified AWS Region for the calling account                                                         |                             |                | Read           |
| [ListRequiredTags](../../../resourcegroupstagging/latest/APIReference/API_ListRequiredTags.md "../../../resourcegroupstagging/latest/APIReference/API_ListRequiredTags.md")                   | Grants permission to list required tags for supported resource types in the calling account                                                                                            |                             |                | List           |
| [StartReportCreation](../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md")          | Grants permission to start generating a report listing all tagged resources in accounts across your organization, and whether each resource is compliant with the effective tag policy |                             |                | Write          |
| [TagResources](../../../resourcegroupstagging/latest/APIReference/API_TagResources.md "../../../resourcegroupstagging/latest/APIReference/API_TagResources.md")                               | Grants permission to apply one or more tags to the specified resources                                                                                                                 |                             |                | Tagging, Write |
| [UntagResources](../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md "../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md")                         | Grants permission to remove the specified tags from the specified resources                                                                                                            |                             |                | Tagging, Write |

## Resource types defined by Amazon Resource Group Tagging API

Amazon Resource Group Tagging API does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon Resource Group Tagging API

Amazon Resource Group Tagging API has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
