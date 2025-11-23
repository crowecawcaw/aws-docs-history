# Actions, resources, and condition keys for AWS PricingPlanManager Service

AWS PricingPlanManager Service (service prefix: `pricingplanmanager`) provides the following service-specific resources, actions, and condition context keys for use in IAM permission policies.

References:

- Learn how to [configure this service](../../../pricingplanmanager/userguide.md "../../../pricingplanmanager/userguide.md").
- View a list of the [API operations available for this service](../../../pricingplanmanager/userguide/security-pricing-plan.html..md "../../../pricingplanmanager/userguide/security-pricing-plan.html..md").
- Learn how to secure this service and its resources by [using IAM](../../../pricingplanmanager/userguide/security.md "../../../pricingplanmanager/userguide/security.md") permission policies.

###### Topics

- [Actions defined by AWS PricingPlanManager Service](#awspricingplanmanagerservice-actions-as-permissions "#awspricingplanmanagerservice-actions-as-permissions")
- [Resource types defined by AWS PricingPlanManager Service](#awspricingplanmanagerservice-resources-for-iam-policies "#awspricingplanmanagerservice-resources-for-iam-policies")
- [Condition keys for AWS PricingPlanManager Service](#awspricingplanmanagerservice-policy-keys "#awspricingplanmanagerservice-policy-keys")

## Actions defined by AWS PricingPlanManager Service

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

The **Access level** column of the Actions table describes how the action is classified (List, Read, Permissions management, or Tagging). This classification can help you understand the level of access that an action grants when you use it in a policy. For more information about access levels, see [Access levels in policy summaries](../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md "../../../IAM/latest/UserGuide/access_policies_understand-policy-summary-access-level-summaries.md").

The **Resource types** column of the Actions table indicates whether each action supports resource-level permissions. If there is no value for this column, you must specify all resources ("\*") to which the policy applies in the `Resource` element of your policy statement. If the column includes a resource type, then you can specify an ARN of that type in a statement with that action. If the action has one or more required resources, the caller must have permission to use the action with those resources. Required resources are indicated in the table with an asterisk (\*). If you limit resource access with the `Resource` element in an IAM policy, you must include an ARN or pattern for each required resource type. Some actions support multiple resource types. If the resource type is optional (not indicated as required), then you can choose to use one of the optional resource types.

The **Condition keys** column of the Actions table includes keys that you can specify in a policy statement's `Condition` element. For more information on the condition keys that are associated with resources for the service, see the **Condition keys** column of the Resource types table.

The **Dependent actions** column of the Actions table shows additional permissions that may be required to successfully call an action. These permissions may be needed in addition to the permission for the action itself. When an action specifies dependent actions, those dependencies may apply to additional resources defined for that action, not only the first resource listed in the table.

###### Note

Resource condition keys are listed in the [Resource types](#awspricingplanmanagerservice-resources-for-iam-policies "#awspricingplanmanagerservice-resources-for-iam-policies") table. You can find a link to the resource type that applies to an action in the **Resource types (\*required)** column of the Actions table. The resource type in the Resource types table includes the **Condition keys** column, which are the resource condition keys that apply to an action in the Actions table.

For details about the columns in the following table, see [Actions table](reference_policies_actions-resources-contextkeys.md#actions_table "reference_policies_actions-resources-contextkeys.md#actions_table").

| Actions                                                                                                                                                                                | Description                                                       | Access level | Resource types (\*required) | Condition keys | Dependent actions |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------ | --------------------------- | -------------- | ----------------- |
| [AssociateResourcesToSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")      | Grants permission to associate resources with a subscription      | Write        |                             |                |                   |
| [CancelSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to cancel a subscription                        | Write        |                             |                |                   |
| [CancelSubscriptionChange](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")              | Grants permission to cancel a pending a change for a subscription | Write        |                             |                |                   |
| [CreateSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to create a subscription                        | Write        |                             |                |                   |
| [DisassociateResourcesFromSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md") | Grants permission to disassociate resources from a subscription   | Write        |                             |                |                   |
| [GetSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                       | Grants permission to get the details for a subscription           | Read         |                             |                |                   |
| [ListSubscriptions](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                     | Grants permission to list subscriptions in your account           | Read         |                             |                |                   |
| [UpdateSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to update a subscription                        | Write        |                             |                |                   |

## Resource types defined by AWS PricingPlanManager Service

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements. Each action in the [Actions table](#awspricingplanmanagerservice-actions-as-permissions "#awspricingplanmanagerservice-actions-as-permissions") identifies the resource types that can be specified with that action. A resource type can also define which condition keys you can include in a policy. These keys are displayed in the last column of the Resource types table. For details about the columns in the following table, see [Resource types table](reference_policies_actions-resources-contextkeys.md#resources_table "reference_policies_actions-resources-contextkeys.md#resources_table").

| Resource types                                                                                                                | ARN                                                                              | Condition keys |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------- |
| [subscription](../../../pricingplanmanager/userguide/subscription.md "../../../pricingplanmanager/userguide/subscription.md") | `arn:${Partition}:pricingplanmanager::${Account}:subscription/${SubscriptionId}` |                |

## Condition keys for AWS PricingPlanManager Service

PricingPlanManager has no service-specific context keys that can be used in the `Condition` element of policy statements. For the list of the global context keys that are available to all services, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").
