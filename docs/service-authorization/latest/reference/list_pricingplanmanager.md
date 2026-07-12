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

- [Actions defined by AWS PricingPlanManager Service](#list_pricingplanmanager-actions-as-permissions "#list_pricingplanmanager-actions-as-permissions")
- [Resource types defined by AWS PricingPlanManager Service](#list_pricingplanmanager-resources-for-iam-policies "#list_pricingplanmanager-resources-for-iam-policies")
- [Condition keys for AWS PricingPlanManager Service](#list_pricingplanmanager-policy-keys "#list_pricingplanmanager-policy-keys")

## Actions defined by AWS PricingPlanManager Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                | Description                                                       | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AssociateResourcesToSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")      | Grants permission to associate resources with a subscription      |                             |                | Write        |
| [CancelSubscription](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")                    | Grants permission to cancel a subscription                        |                             |                | Write        |
| [CancelSubscriptionChange](../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md "../../../PricingPlanManager/latest/UserGuide/security-pricing-plan.md")              | Grants permission to cancel a pending a change for a subscription |                             |                | Write        |
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
