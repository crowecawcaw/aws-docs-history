

# Actions, resources, and condition keys for AWS Free Tier
<a name="list_freetier"></a>

AWS Free Tier (service prefix: `freetier`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/freetier/freetier.json) for this service.

**Topics**
+ [API operations defined by AWS Free Tier](#list_freetier-operations)
+ [Actions defined by AWS Free Tier](#list_freetier-actions-as-permissions)
+ [Permission-only actions for AWS Free Tier](#list_freetier-permission-only-actions)
+ [Resource types defined by AWS Free Tier](#list_freetier-resources-for-iam-policies)
+ [Condition keys for AWS Free Tier](#list_freetier-policy-keys)

## API operations defined by AWS Free Tier
<a name="list_freetier-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_freetier-actions-as-permissions).




- **   GetAccountActivity  **
  - **IAM action:**  [freetier:GetAccountActivity](#list_freetier-action-GetAccountActivity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAccountPlanState  **
  - **IAM action:**  [freetier:GetAccountPlanState](#list_freetier-action-GetAccountPlanState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFreeTierUsage  **
  - **IAM action:**  [freetier:GetFreeTierUsage](#list_freetier-action-GetFreeTierUsage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAccountActivities  **
  - **IAM action:**  [freetier:ListAccountActivities](#list_freetier-action-ListAccountActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpgradeAccountPlan  **
  - **IAM action:**  [freetier:UpgradeAccountPlan](#list_freetier-action-UpgradeAccountPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Free Tier
<a name="list_freetier-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetAccountActivity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountActivity.html)  | Grants permission to get a specific activity record |  |   | Read | 
|   [GetAccountPlanState](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountPlanState.html)  | Grants permission to get all of the information related to the state of the account plan related to Free Tier |  |   | Read | 
|   [GetFreeTierUsage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html)  | Grants permission to get free tier usage limits and MTD usage status |  |   | Read | 
|   [ListAccountActivities](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ListAccountActivities.html)  | Grants permission to list available activities |  |   | List | 
|   [UpgradeAccountPlan](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_UpgradeAccountPlan.html)  | Grants permission to trigger an upgrade of account plan |  |   | Write | 

## Permission-only actions for AWS Free Tier
<a name="list_freetier-permission-only-actions"></a>

The following actions are defined by AWS Free Tier but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetFreeTierAlertPreference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html)  | Grants permission to get free tier alert preference (email address) |  |   | Read | 
|   [PutFreeTierAlertPreference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html)  | Grants permission to set free tier alert preference (email address) |  |   | Write | 

## Resource types defined by AWS Free Tier
<a name="list_freetier-resources-for-iam-policies"></a>

AWS Free Tier does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Free Tier
<a name="list_freetier-policy-keys"></a>

AWS Free Tier has no service-specific condition keys that can be used in the `Condition` element of policy statements.