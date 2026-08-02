# Actions, resources, and condition keys for AWS PricingPlanManager Service

AWS PricingPlanManager Service (service prefix: `pricingplanmanager`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../pricingplanmanager/userguide.md "../../../pricingplanmanager/userguide.md").
- View a list of the [API operations available for
  this service](../../../pricingplanmanager/userguide/security-pricing-plan.html..md "../../../pricingplanmanager/userguide/security-pricing-plan.html..md").
- Learn how to secure this service and its resources by
  [using IAM](../../../pricingplanmanager/userguide/security.md "../../../pricingplanmanager/userguide/security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/pricingplanmanager/pricingplanmanager.json "https://servicereference.us-east-1.amazonaws.com/v1/pricingplanmanager/pricingplanmanager.json") for this service.

###### Topics

- [API operations defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-operations "#list_pricing-plan-manager-operations")
- [Actions defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-actions-as-permissions "#list_pricing-plan-manager-actions-as-permissions")
- [Resource types defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-resources-for-iam-policies "#list_pricing-plan-manager-resources-for-iam-policies")
- [Condition keys for AWS PricingPlanManager Service](#list_pricing-plan-manager-policy-keys "#list_pricing-plan-manager-policy-keys")

## API operations defined by AWS PricingPlanManager Service

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pricing-plan-manager-actions-as-permissions "#list_pricing-plan-manager-actions-as-permissions").

| Operation                                                                                                                                            | IAM action                                                                                                                                                                                                    | Condition key | Possible value(s) | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| ApprovePaidSubscription                                                                                                                              | [pricingplanmanager:ApprovePaidSubscription](#list_pricing-plan-manager-action-ApprovePaidSubscription "#list_pricing-plan-manager-action-ApprovePaidSubscription")                                           |               |                   | Write        |
| AssociateResourcesToSubscription                                                                                                                     | [pricingplanmanager:AssociateResourcesToSubscription](#list_pricing-plan-manager-action-AssociateResourcesToSubscription "#list_pricing-plan-manager-action-AssociateResourcesToSubscription")                |               |                   | Write        |
| CancelSubscription                                                                                                                                   | [pricingplanmanager:CancelSubscription](#list_pricing-plan-manager-action-CancelSubscription "#list_pricing-plan-manager-action-CancelSubscription")                                                          |               |                   | Write        |
| CancelSubscriptionChange                                                                                                                             | [pricingplanmanager:CancelSubscriptionChange](#list_pricing-plan-manager-action-CancelSubscriptionChange "#list_pricing-plan-manager-action-CancelSubscriptionChange")                                        |               |                   | Write        |
| CreateSubscription                                                                                                                                   | [pricingplanmanager:ApprovePaidSubscription](#list_pricing-plan-manager-action-ApprovePaidSubscription "#list_pricing-plan-manager-action-ApprovePaidSubscription")                                           |               |                   | Write        |
| [pricingplanmanager:CreateSubscription](#list_pricing-plan-manager-action-CreateSubscription "#list_pricing-plan-manager-action-CreateSubscription") |                                                                                                                                                                                                               |               | Write             |
| DisassociateResourcesFromSubscription                                                                                                                | [pricingplanmanager:DisassociateResourcesFromSubscription](#list_pricing-plan-manager-action-DisassociateResourcesFromSubscription "#list_pricing-plan-manager-action-DisassociateResourcesFromSubscription") |               |                   | Write        |
| GetSubscription                                                                                                                                      | [pricingplanmanager:GetSubscription](#list_pricing-plan-manager-action-GetSubscription "#list_pricing-plan-manager-action-GetSubscription")                                                                   |               |                   | Read         |
| ListSubscriptions                                                                                                                                    | [pricingplanmanager:ListSubscriptions](#list_pricing-plan-manager-action-ListSubscriptions "#list_pricing-plan-manager-action-ListSubscriptions")                                                             |               |                   | Read         |
| UpdateSubscription                                                                                                                                   | [pricingplanmanager:UpdateSubscription](#list_pricing-plan-manager-action-UpdateSubscription "#list_pricing-plan-manager-action-UpdateSubscription")                                                          |               |                   | Write        |

## Actions defined by AWS PricingPlanManager Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                | Description                                                       | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ApprovePaidSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")               | Grants permission to approve paid subscription                    |                             |                | Write        |
| [AssociateResourcesToSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")      | Grants permission to associate resources with a subscription      |                             |                | Write        |
| [CancelSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to cancel a subscription                        |                             |                | Write        |
| [CancelSubscriptionChange](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")              | Grants permission to cancel a scheduled change for a subscription |                             |                | Write        |
| [CreateSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to create a subscription                        |                             |                | Write        |
| [DisassociateResourcesFromSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md") | Grants permission to disassociate resources from a subscription   |                             |                | Write        |
| [GetSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                       | Grants permission to get the details for a subscription           |                             |                | Read         |
| [ListSubscriptions](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                     | Grants permission to list subscriptions in your account           |                             |                | Read         |
| [UpdateSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to update a subscription                        |                             |                | Write        |

## Resource types defined by AWS PricingPlanManager Service

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                | ARN                                                                            | Condition keys |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- |
| [subscription](../../../pricingplanmanager/userguide/subscription.md "../../../pricingplanmanager/userguide/subscription.md") | arn:${Partition}:pricingplanmanager::${Account}:subscription/${SubscriptionId} |                |

## Condition keys for AWS PricingPlanManager Service

AWS PricingPlanManager Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
