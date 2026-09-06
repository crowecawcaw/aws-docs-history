

# Actions, resources, and condition keys for AWS PricingPlanManager Service
<a name="list_pricing-plan-manager"></a>

AWS PricingPlanManager Service (service prefix: `pricingplanmanager`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pricingplanmanager/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pricingplanmanager/userguide/security-pricing-plan.html.).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/pricingplanmanager/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pricingplanmanager/pricingplanmanager.json) for this service.

**Topics**
+ [API operations defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-operations)
+ [Actions defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-actions-as-permissions)
+ [Resource types defined by AWS PricingPlanManager Service](#list_pricing-plan-manager-resources-for-iam-policies)
+ [Condition keys for AWS PricingPlanManager Service](#list_pricing-plan-manager-policy-keys)

## API operations defined by AWS PricingPlanManager Service
<a name="list_pricing-plan-manager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pricing-plan-manager-actions-as-permissions).




- **   ApprovePaidSubscription  **
  - **IAM action:**  [pricingplanmanager:ApprovePaidSubscription](#list_pricing-plan-manager-action-ApprovePaidSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateResourcesToSubscription  **
  - **IAM action:**  [pricingplanmanager:AssociateResourcesToSubscription](#list_pricing-plan-manager-action-AssociateResourcesToSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelSubscription  **
  - **IAM action:**  [pricingplanmanager:CancelSubscription](#list_pricing-plan-manager-action-CancelSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelSubscriptionChange  **
  - **IAM action:**  [pricingplanmanager:CancelSubscriptionChange](#list_pricing-plan-manager-action-CancelSubscriptionChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubscription  **
  - **IAM action:**  [pricingplanmanager:ApprovePaidSubscription](#list_pricing-plan-manager-action-ApprovePaidSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pricingplanmanager:CreateSubscription](#list_pricing-plan-manager-action-CreateSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DisassociateResourcesFromSubscription  **
  - **IAM action:**  [pricingplanmanager:DisassociateResourcesFromSubscription](#list_pricing-plan-manager-action-DisassociateResourcesFromSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSubscription  **
  - **IAM action:**  [pricingplanmanager:GetSubscription](#list_pricing-plan-manager-action-GetSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSubscriptions  **
  - **IAM action:**  [pricingplanmanager:ListSubscriptions](#list_pricing-plan-manager-action-ListSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateSubscription  **
  - **IAM action:**  [pricingplanmanager:UpdateSubscription](#list_pricing-plan-manager-action-UpdateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS PricingPlanManager Service
<a name="list_pricing-plan-manager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [ApprovePaidSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to approve paid subscription |  |   | Write | 
|   [AssociateResourcesToSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to associate resources with a subscription |  |   | Write | 
|   [CancelSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to cancel a subscription |  |   | Write | 
|   [CancelSubscriptionChange](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to cancel a scheduled change for a subscription |  |   | Write | 
|   [CreateSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to create a subscription |  |   | Write | 
|   [DisassociateResourcesFromSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to disassociate resources from a subscription |  |   | Write | 
|   [GetSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to get the details for a subscription |  |   | Read | 
|   [ListSubscriptions](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to list subscriptions in your account |  |   | Read | 
|   [UpdateSubscription](https://docs.aws.amazon.com/PricingPlanManager/latest/UserGuide/security-pricing-plan.html)  | Grants permission to update a subscription |  |   | Write | 

## Resource types defined by AWS PricingPlanManager Service
<a name="list_pricing-plan-manager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [subscription](https://docs.aws.amazon.com/pricingplanmanager/userguide/subscription.html)  | arn:${Partition}:pricingplanmanager::${Account}:subscription/${SubscriptionId} |   | 

## Condition keys for AWS PricingPlanManager Service
<a name="list_pricing-plan-manager-policy-keys"></a>

AWS PricingPlanManager Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.