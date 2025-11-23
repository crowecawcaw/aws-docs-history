# Actions, resources, and condition keys for Amazon Resource Group Tagging API

Amazon Resource Group Tagging API (service prefix: `tag`) provides the following service-specific resources, actions, and condition context keys for use in IAM permission policies.

References:

- Learn how to [configure this service](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md").
- View a list of the [API operations available for this service](../../../resourcegroupstagging/latest/APIReference.md "../../../resourcegroupstagging/latest/APIReference.md").
- Learn how to secure this service and its resources by [using IAM](../../../ARG/latest/userguide/gettingstarted-prereqs.md "../../../ARG/latest/userguide/gettingstarted-prereqs.md") permission policies.

###### Topics

- [Actions defined by Amazon Resource Group Tagging API](#amazonresourcegrouptaggingapi-actions-as-permissions "#amazonresourcegrouptaggingapi-actions-as-permissions")
- [Resource types defined by Amazon Resource Group Tagging API](#amazonresourcegrouptaggingapi-resources-for-iam-policies "#amazonresourcegrouptaggingapi-resources-for-iam-policies")
- [Condition keys for Amazon Resource Group Tagging API](#amazonresourcegrouptaggingapi-policy-keys "#amazonresourcegrouptaggingapi-policy-keys")

## Actions defined by Amazon Resource Group Tagging API

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

The **Access level** column of the Actions table describes how the action is classified (List, Read, Permissions management, or Tagging). This classification can help you understand the level of access that an action grants when you use it in a policy. For more information about access levels, see [Access levels in policy summaries](../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md "../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md").

The **Resource types** column of the Actions table indicates whether each action supports resource-level permissions. If there is no value for this column, you must specify all resources ("\*") to which the policy applies in the `Resource` element of your policy statement. If the column includes a resource type, then you can specify an ARN of that type in a statement with that action. If the action has one or more required resources, the caller must have permission to use the action with those resources. Required resources are indicated in the table with an asterisk (\*). If you limit resource access with the `Resource` element in an IAM policy, you must include an ARN or pattern for each required resource type. Some actions support multiple resource types. If the resource type is optional (not indicated as required), then you can choose to use one of the optional resource types.

The **Condition keys** column of the Actions table includes keys that you can specify in a policy statement's `Condition` element. For more information on the condition keys that are associated with resources for the service, see the **Condition keys** column of the Resource types table.

The **Dependent actions** column of the Actions table shows additional permissions that may be required to successfully call an action. These permissions may be needed in addition to the permission for the action itself. When an action specifies dependent actions, those dependencies may apply to additional resources defined for that action, not only the first resource listed in the table.

###### Note

Resource condition keys are listed in the [Resource types](#amazonresourcegrouptaggingapi-resources-for-iam-policies "#amazonresourcegrouptaggingapi-resources-for-iam-policies") table. You can find a link to the resource type that applies to an action in the **Resource types (\*required)** column of the Actions table. The resource type in the Resource types table includes the **Condition keys** column, which are the resource condition keys that apply to an action in the Actions table.

For details about the columns in the following table, see [Actions table](reference_policies_actions-resources-contextkeys.md#actions_table "reference_policies_actions-resources-contextkeys.md#actions_table").

| Actions                                                                                                                                                                                       | Description                                                                                                                                                                            | Access level | Resource types (\*required) | Condition keys | Dependent actions |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------- | -------------- | ----------------- |
| [DescribeReportCreation](../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.md") | Grants permission to describe the status of the StartReportCreation operation                                                                                                          | Read         |                             |                |                   |
| [GetComplianceSummary](../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md "../../../resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.md")       | Grants permission to retrieve a summary of how many resources are noncompliant with their effective tag policies                                                                       | Read         |                             |                |                   |
| [GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md")                               | Grants permission to return tagged or previously tagged resources in the specified AWS Region for the calling account                                                                  | Read         |                             |                |                   |
| [GetTagKeys](../../../resourcegroupstagging/latest/APIReference/API_GetTagKeys.md "../../../resourcegroupstagging/latest/APIReference/API_GetTagKeys.md")                                     | Grants permission to returns tag keys currently in use in the specified AWS Region for the calling account                                                                             | Read         |                             |                |                   |
| [GetTagValues](../../../resourcegroupstagging/latest/APIReference/API_GetTagValues.md "../../../resourcegroupstagging/latest/APIReference/API_GetTagValues.md")                               | Grants permission to return tag values for the specified key that are used in the specified AWS Region for the calling account                                                         | Read         |                             |                |                   |
| [ListRequiredTags](../../../resourcegroupstagging/latest/APIReference/API_ListRequiredTags.md "../../../resourcegroupstagging/latest/APIReference/API_ListRequiredTags.md")                   | Grants permission to list required tags for supported resource types in the calling account                                                                                            | List         |                             |                |                   |
| [StartReportCreation](../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md "../../../resourcegroupstagging/latest/APIReference/API_StartReportCreation.md")          | Grants permission to start generating a report listing all tagged resources in accounts across your organization, and whether each resource is compliant with the effective tag policy | Write        |                             |                |                   |
| [TagResources](../../../resourcegroupstagging/latest/APIReference/API_TagResources.md "../../../resourcegroupstagging/latest/APIReference/API_TagResources.md")                               | Grants permission to apply one or more tags to the specified resources                                                                                                                 | Tagging      |                             |                |                   |
| [UntagResources](../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md "../../../resourcegroupstagging/latest/APIReference/API_UntagResources.md")                         | Grants permission to remove the specified tags from the specified resources                                                                                                            | Tagging      |                             |                |                   |

## Resource types defined by Amazon Resource Group Tagging API

Amazon Resource Group Tagging API does not support specifying a resource ARN in the `Resource` element of an IAM policy statement. To allow access to Amazon Resource Group Tagging API, specify `"Resource": "*"` in your policy.

## Condition keys for Amazon Resource Group Tagging API

Resource Group Tagging has no service-specific context keys that can be used in the `Condition` element of policy statements. For the list of the global context keys that are available to all services, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").
