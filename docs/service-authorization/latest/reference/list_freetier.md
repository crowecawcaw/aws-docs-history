# Actions, resources, and condition keys for AWS Free Tier

AWS Free Tier (service prefix: `freetier`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- View a list of the [API operations available for
  this service](../../../aws-cost-management/latest/APIReference.md "../../../aws-cost-management/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/freetier/freetier.json "https://servicereference.us-east-1.amazonaws.com/v1/freetier/freetier.json") for this service.

###### Topics

- [API operations defined by AWS Free Tier](#list_freetier-operations "#list_freetier-operations")
- [Actions defined by AWS Free Tier](#list_freetier-actions-as-permissions "#list_freetier-actions-as-permissions")
- [Permission-only actions for AWS Free Tier](#list_freetier-permission-only-actions "#list_freetier-permission-only-actions")
- [Resource types defined by AWS Free Tier](#list_freetier-resources-for-iam-policies "#list_freetier-resources-for-iam-policies")
- [Condition keys for AWS Free Tier](#list_freetier-policy-keys "#list_freetier-policy-keys")

## API operations defined by AWS Free Tier

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_freetier-actions-as-permissions "#list_freetier-actions-as-permissions").

| Operation                                                                                                                                                                                               | IAM action                                                                                                                  | Condition key | Possible value(s) | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetAccountActivity                                                                                                                                                                                      | [freetier:GetAccountActivity](#list_freetier-action-GetAccountActivity "#list_freetier-action-GetAccountActivity")          |               |                   | Read         |
| GetAccountPlanState                                                                                                                                                                                     | [freetier:GetAccountPlanState](#list_freetier-action-GetAccountPlanState "#list_freetier-action-GetAccountPlanState")       |               |                   | Read         |
| GetFreeTierUsage                                                                                                                                                                                        | [freetier:GetFreeTierUsage](#list_freetier-action-GetFreeTierUsage "#list_freetier-action-GetFreeTierUsage")                |               |                   | Read         |
| [aws-portal:ViewBilling](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions") |                                                                                                                             |               | Read              |
| ListAccountActivities                                                                                                                                                                                   | [freetier:ListAccountActivities](#list_freetier-action-ListAccountActivities "#list_freetier-action-ListAccountActivities") |               |                   | List         |
| UpgradeAccountPlan                                                                                                                                                                                      | [freetier:UpgradeAccountPlan](#list_freetier-action-UpgradeAccountPlan "#list_freetier-action-UpgradeAccountPlan")          |               |                   | Write        |

## Actions defined by AWS Free Tier

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                  | Description                                                                                                   | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetAccountActivity](../../../aws-cost-management/latest/APIReference/API_freetier_GetAccountActivity.md "../../../aws-cost-management/latest/APIReference/API_freetier_GetAccountActivity.md")          | Grants permission to get a specific activity record                                                           |                             |                | Read         |
| [GetAccountPlanState](../../../aws-cost-management/latest/APIReference/API_freetier_GetAccountPlanState.md "../../../aws-cost-management/latest/APIReference/API_freetier_GetAccountPlanState.md")       | Grants permission to get all of the information related to the state of the account plan related to Free Tier |                             |                | Read         |
| [GetFreeTierUsage](../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md "../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md")                                        | Grants permission to get free tier usage limits and MTD usage status                                          |                             |                | Read         |
| [ListAccountActivities](../../../aws-cost-management/latest/APIReference/API_freetier_ListAccountActivities.md "../../../aws-cost-management/latest/APIReference/API_freetier_ListAccountActivities.md") | Grants permission to list available activities                                                                |                             |                | List         |
| [UpgradeAccountPlan](../../../aws-cost-management/latest/APIReference/API_freetier_UpgradeAccountPlan.md "../../../aws-cost-management/latest/APIReference/API_freetier_UpgradeAccountPlan.md")          | Grants permission to trigger an upgrade of account plan                                                       |                             |                | Write        |

## Permission-only actions for AWS Free Tier

The following actions are defined by AWS Free Tier but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                     | Description                                                         | Resource types (\*required) | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetFreeTierAlertPreference](../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md "../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md") | Grants permission to get free tier alert preference (email address) |                             |                | Read         |
| [PutFreeTierAlertPreference](../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md "../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md") | Grants permission to set free tier alert preference (email address) |                             |                | Write        |

## Resource types defined by AWS Free Tier

AWS Free Tier does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Free Tier

AWS Free Tier has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
