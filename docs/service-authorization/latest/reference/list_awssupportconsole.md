# Actions, resources, and condition keys for AWS Support Console

AWS Support Console (service prefix: `support-console`) provides the following service-specific resources, actions, and condition context keys for use in IAM permission policies.

References:

- Learn how to [configure this service](../../../awssupport/latest/user/aws-support-console.md "../../../awssupport/latest/user/aws-support-console.md").
- View a list of the [API operations available for this service](../../../awssupport/latest/user/support-console-access-control.md "../../../awssupport/latest/user/support-console-access-control.md").
- Learn how to secure this service and its resources by [using IAM](../../../awssupport/latest/user/support-console-access-control.md "../../../awssupport/latest/user/support-console-access-control.md") permission policies.

###### Topics

- [Actions defined by AWS Support Console](#awssupportconsole-actions-as-permissions "#awssupportconsole-actions-as-permissions")
- [Resource types defined by AWS Support Console](#awssupportconsole-resources-for-iam-policies "#awssupportconsole-resources-for-iam-policies")
- [Condition keys for AWS Support Console](#awssupportconsole-policy-keys "#awssupportconsole-policy-keys")

## Actions defined by AWS Support Console

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

The **Access level** column of the Actions table describes how the action is classified (List, Read, Permissions management, or Tagging). This classification can help you understand the level of access that an action grants when you use it in a policy. For more information about access levels, see [Access levels in policy summaries](../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md "../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md").

The **Resource types** column of the Actions table indicates whether each action supports resource-level permissions. If there is no value for this column, you must specify all resources ("\*") to which the policy applies in the `Resource` element of your policy statement. If the column includes a resource type, then you can specify an ARN of that type in a statement with that action. If the action has one or more required resources, the caller must have permission to use the action with those resources. Required resources are indicated in the table with an asterisk (\*). If you limit resource access with the `Resource` element in an IAM policy, you must include an ARN or pattern for each required resource type. Some actions support multiple resource types. If the resource type is optional (not indicated as required), then you can choose to use one of the optional resource types.

The **Condition keys** column of the Actions table includes keys that you can specify in a policy statement's `Condition` element. For more information on the condition keys that are associated with resources for the service, see the **Condition keys** column of the Resource types table.

The **Dependent actions** column of the Actions table shows additional permissions that may be required to successfully call an action. These permissions may be needed in addition to the permission for the action itself. When an action specifies dependent actions, those dependencies may apply to additional resources defined for that action, not only the first resource listed in the table.

###### Note

Resource condition keys are listed in the [Resource types](#awssupportconsole-resources-for-iam-policies "#awssupportconsole-resources-for-iam-policies") table. You can find a link to the resource type that applies to an action in the **Resource types (\*required)** column of the Actions table. The resource type in the Resource types table includes the **Condition keys** column, which are the resource condition keys that apply to an action in the Actions table.

For details about the columns in the following table, see [Actions table](reference_policies_actions-resources-contextkeys.md#actions_table "reference_policies_actions-resources-contextkeys.md#actions_table").

| Actions                                                                                        | Description                                                                     | Access level | Resource types (\*required) | Condition keys | Dependent actions |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ | --------------------------- | -------------- | ----------------- |
| [CheckSubscription](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                 | Grants permission to check whether the account has access to given product      | Read         |                             |                |                   |
| [CreateCaseDraft](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                   | Grants permission to create or update case draft for the given case type        | Write        |                             |                |                   |
| [CreateContact](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                     | Grants permission to create an authenticated contact for the given contact type | Write        |                             |                |                   |
| [DeleteCaseDraft](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                   | Grants permission to delete a case draft for the given case type                | Write        |                             |                |                   |
| [DescribeDynamicHelp](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]               | Grants permission to get dynamic help resources for given service and category  | Read         |                             |                |                   |
| [GetAccountGovCloudEnabled](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]         | Grants permission to determines whether the calling account is GovCloud enabled | Read         |                             |                |                   |
| [GetAccountState](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                   | Grants permission to get the state of the calling account                       | Read         |                             |                |                   |
| [GetBanner](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                         | Grants permission to get the support banner information                         | Read         |                             |                |                   |
| [GetCaseDraft](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                      | Grants permission to get a case draft for given case type                       | Read         |                             |                |                   |
| [GetIssueClassificationPredictions](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only] | Grants permission to get classification predictions of an issue                 | Read         |                             |                |                   |
| [GetIssueTextSummary](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]               | Grants permission to get a generated text summary of an issue                   | Read         |                             |                |                   |
| [GetQuestionnaire](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                  | Grants permission to get a feedback questionnaire                               | Read         |                             |                |                   |
| [SaveFeedback](${AuthZDocPage}.md "${AuthZDocPage}.md") [permission only]                      | Grants permission to save questionnaire feedback                                | Write        |                             |                |                   |

## Resource types defined by AWS Support Console

AWS Support Console does not support specifying a resource ARN in the `Resource` element of an IAM policy statement. To allow access to AWS Support Console, specify `"Resource": "*"` in your policy.

## Condition keys for AWS Support Console

Support Console has no service-specific context keys that can be used in the `Condition` element of policy statements. For the list of the global context keys that are available to all services, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").
