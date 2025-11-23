# Using identity-based policies (IAM policies) for AWS Cost Management

###### Note

The following AWS Identity and Access Management (IAM) actions have
reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the [bulk policy migrator scripts](../../../awsaccountbilling/latest/aboutv2/migrate-iam-permissions.md "../../../awsaccountbilling/latest/aboutv2/migrate-iam-permissions.md") to update
  polices from your payer account. You can also use the [old to granular action
  mapping reference](../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.md "../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.md") to verify the IAM actions that need to be added.

For more information, see the [Changes to AWS Billing, AWS Cost Management, and Account Consoles Permission](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/")
blog.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

This topic provides examples of identity-based policies that demonstrate how an
account administrator can attach permissions policies to IAM identities (roles and
groups) and thereby grant permissions to perform operations on Billing and Cost Management resources.

For a full discussion of AWS accounts and users, see [What Is IAM?](../../../IAM/latest/UserGuide/IAM_Introduction.md "../../../IAM/latest/UserGuide/IAM_Introduction.md") in the
_IAM User Guide_.

For information on how you can update customer managed policies, see [Editing customer managed policies (console)](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-managed-policy-console") in the _IAM User Guide_.

###### Topics

- [Billing and Cost Management actions policies](#user-permissions "#user-permissions")
- [Billing and Cost Management recommended actions
  policies](#allows-recommended-actions-access "#allows-recommended-actions-access")
- [Managed policies](#managed-policies "#managed-policies")
- [AWS Cost Management updates to AWS managed policies](#updates-managedIAM "#updates-managedIAM")

## Billing and Cost Management actions policies

This table summarizes the permissions that allow or deny users access to your
billing information and tools. For examples of policies that use these permissions,
see [AWS Cost Management policy examples](billing-example-policies.md "billing-example-policies.md").

For a list of actions policies for the Billing console, see [Billing actions policies](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions") in the _Billing user
guide_.

| Permission name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws-portal:ViewBilling`              | Allow or deny users permission to view the Billing and Cost Management console pages.<br>For an example policy, see [Allow IAM users to view your billing information](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-billing-view-billing-only "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-billing-view-billing-only") in<br>the _Billing User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `aws-portal:ViewUsage`                | Allow or deny users permission to view AWS usage [Reports](https://portal.aws.amazon.com/billing/home#/reports "https://portal.aws.amazon.com/billing/home#/reports").<br>To allow users to view usage reports, you must allow both<br>`ViewUsage` and `ViewBilling`.<br>For an example policy, see [Allow IAM users to access the reports console<br>page](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-billing-view-reports "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-billing-view-reports") in the _Billing User<br>Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `aws-portal:ModifyBilling`            | Allow or deny users permission to modify the following Billing and Cost Management<br>console pages:<br>• [Budgets](https://portal.aws.amazon.com/billing/home#/budgets "https://portal.aws.amazon.com/billing/home#/budgets")<br>• [Consolidated Billing](https://portal.aws.amazon.com/billing/home#/consolidatedbilling "https://portal.aws.amazon.com/billing/home#/consolidatedbilling")<br>• [Billing preferences](https://portal.aws.amazon.com/billing/home#/preferences "https://portal.aws.amazon.com/billing/home#/preferences")<br>• [Credits](https://portal.aws.amazon.com/billing/home#/credits "https://portal.aws.amazon.com/billing/home#/credits")<br>• [Tax<br>settings](https://portal.aws.amazon.com/billing/home#/tax "https://portal.aws.amazon.com/billing/home#/tax")<br>• [Payment methods](https://portal.aws.amazon.com/billing/home#/paymentmethods "https://portal.aws.amazon.com/billing/home#/paymentmethods")<br>• [Purchase orders](https://portal.aws.amazon.com/billing/home#/purchaseorders "https://portal.aws.amazon.com/billing/home#/purchaseorders")<br>• [Cost Allocation Tags](https://portal.aws.amazon.com/billing/home#/tags "https://portal.aws.amazon.com/billing/home#/tags")<br>To allow users to modify these console pages, you must allow<br>both `ModifyBilling` and `ViewBilling`.<br>For an example policy, see [Allow users to modify billing<br>information](billing-example-policies.md#example-billing-deny-modifybilling "billing-example-policies.md#example-billing-deny-modifybilling"). |
| `aws-portal:ViewAccount`              | Allow or deny users permission to view the following Billing and Cost Management<br>console pages:<br>• Billing<br>Dashboard<br>• [Account Settings](https://portal.aws.amazon.com/billing/home#/account "https://portal.aws.amazon.com/billing/home#/account")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `aws-portal:ModifyAccount`            | Allow or deny users permission to modify [Account<br>Settings](https://portal.aws.amazon.com/billing/home#/account "https://portal.aws.amazon.com/billing/home#/account").<br>To allow users to modify account settings, you must allow both<br>`ModifyAccount` and<br>`ViewAccount`.<br>For an example of a policy that explicitly denies a user<br>access to the \*_Account Settings_<br>• console<br>page, see [Deny access to account settings, but allow full access to all other billing and usage information](billing-example-policies.md#example-billing-deny-modifyaccount "billing-example-policies.md#example-billing-deny-modifyaccount").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `budgets:ViewBudget`                  | Allow or deny users permission to view [Budgets](https://portal.aws.amazon.com/billing/home#/budgets "https://portal.aws.amazon.com/billing/home#/budgets").<br>To allow users to view budgets, you must also allow<br>`ViewBilling`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `budgets:ModifyBudget`                | Allow or deny users permission to modify [Budgets](https://portal.aws.amazon.com/billing/home#/budgets "https://portal.aws.amazon.com/billing/home#/budgets").<br>To allow users to view and modify budgets, you must also allow<br>`ViewBilling`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:GetPreferences`                   | Allow or deny users permissions to view the Cost Explorer preferences<br>page.<br>For an example policy, see [View and update the Cost Explorer preferences page](billing-example-policies.md#example-view-update-ce "billing-example-policies.md#example-view-update-ce").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `ce:UpdatePreferences`                | Allow or deny users permissions to update the Cost Explorer preferences<br>page.<br>For an example policy, see [View and update the Cost Explorer preferences page](billing-example-policies.md#example-view-update-ce "billing-example-policies.md#example-view-update-ce").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ce:DescribeReport`                   | Allow or deny users permissions to view the Cost Explorer reports<br>page.<br>For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports "billing-example-policies.md#example-view-ce-reports").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ce:CreateReport`                     | Allow or deny users permissions to create reports using the<br>Cost Explorer reports page.<br>For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports "billing-example-policies.md#example-view-ce-reports").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ce:UpdateReport`                     | Allow or deny users permissions to update using the Cost Explorer<br>reports page.<br>For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports "billing-example-policies.md#example-view-ce-reports").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ce:DeleteReport`                     | Allow or deny users permissions to delete reports using the<br>Cost Explorer reports page.<br>For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports "billing-example-policies.md#example-view-ce-reports").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ce:DescribeNotificationSubscription` | Allow or deny users permissions to view Cost Explorer reservation<br>expiration alerts in the reservation overview page.<br>For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration "billing-example-policies.md#example-view-ce-expiration").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ce:CreateNotificationSubscription`   | Allow or deny users permissions to create Cost Explorer reservation<br>expiration alerts in the reservation overview page.<br>For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration "billing-example-policies.md#example-view-ce-expiration").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:UpdateNotificationSubscription`   | Allow or deny users permissions to update Cost Explorer reservation<br>expiration alerts in the reservation overview page.<br>For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration "billing-example-policies.md#example-view-ce-expiration").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:DeleteNotificationSubscription`   | Allow or deny users permissions to delete Cost Explorer reservation<br>expiration alerts in the reservation overview page.<br>For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration "billing-example-policies.md#example-view-ce-expiration").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:CreateCostCategoryDefinition`     | Allow or deny users permissions to create cost<br>categories.<br>For an example policy, see [View and manage cost categories](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api") in the<br>_Billing User Guide_.<br>You can add resource tags to monitors during<br>`Create`. In order to create monitors with<br>resource tags, you need the `ce:TagResource`<br>permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `ce:DeleteCostCategoryDefinition`     | Allow or deny users permissions to delete cost<br>categories.<br>For an example policy, see [View and manage cost categories](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api") in the<br>_Billing User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ce:DescribeCostCategoryDefinition`   | Allow or deny users permissions to view cost<br>categories.<br>For an example policy, see [View and manage cost categories](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api") in the<br>_Billing User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ce:ListCostCategoryDefinitions`      | Allow or deny users permissions to list cost<br>categories.<br>For an example policy, see [View and manage cost categories](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api") in the<br>_Billing User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ce:ListTagsForResource`              | Allow or deny users permissions to list all resource tags for<br>a given resource. For a list of supported resources, see [ResourceTag](../../../aws-cost-management/latest/APIReference/API_ResourceTag.md "../../../aws-cost-management/latest/APIReference/API_ResourceTag.md") in the<br>_AWS Billing and Cost Management API Reference_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ce:UpdateCostCategoryDefinition`     | Allow or deny users permissions to update cost<br>categories.<br>For an example policy, see [View and manage cost categories](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md#example-policy-cc-api") in the<br>_Billing User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ce:CreateAnomalyMonitor`             | Allow or deny users permissions to create a<br>single [AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md") monitor. You<br>can add resource tags to monitors during `Create`. In<br>order to create monitors with resource tags, you need the<br>`ce:TagResource` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:GetAnomalyMonitors`               | Allow or deny users permissions to view all<br>[AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md") monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ce:UpdateAnomalyMonitor`             | Allow or deny users permissions to update<br>[AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md") monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ce:DeleteAnomalyMonitor`             | Allow or deny users permissions to delete<br>[AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md") monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ce:CreateAnomalySubscription`        | Allow or deny users permissions to create a<br>single subscription for [AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md"). You can add resource tags to subscriptions<br>during `Create`. In order to create subscriptions<br>with resource tags, you need the `ce:TagResource`<br>permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `ce:GetAnomalySubscriptions`          | Allow or deny users permissions to view all<br>subscriptions for [AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `ce:UpdateAnomalySubscription`        | Allow or deny users permissions to update<br>[AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md")<br>subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ce:DeleteAnomalySubscription`        | Allow or deny users permissions to delete<br>[AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md")<br>subscriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ce:GetAnomalies`                     | Allow or deny users permissions to view all<br>anomalies in [AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ce:ProvideAnomalyFeedback`           | Allow or deny users permissions to provide<br>feedback on a detected [AWS Cost Anomaly Detection](manage-ad.md "manage-ad.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `ce:TagResource`                      | Allow or deny users permissions to add resource tag key-value<br>pairs to a resource. For a list of supported resources, see<br>[ResourceTag](../../../aws-cost-management/latest/APIReference/API_ResourceTag.md "../../../aws-cost-management/latest/APIReference/API_ResourceTag.md") in the<br>_AWS Billing and Cost Management API Reference_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `ce:UntagResource`                    | Allow or deny users permissions to delete resource tags from a<br>resource. For a list of supported resources, see [ResourceTag](../../../aws-cost-management/latest/APIReference/API_ResourceTag.md "../../../aws-cost-management/latest/APIReference/API_ResourceTag.md") in the<br>_AWS Billing and Cost Management API Reference_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ce:GetCostAndUsageComparisons`       | Allow or deny users permissions to retrieve<br>cost and usage comparisons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ce:GetCostComparisonDrivers`         | Allow or deny users permissions to retrieve<br>cost drivers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Billing and Cost Management recommended actions

policies

To get started with recommended actions, you need to have the following core
permission:

- `bcm-recommended-actions:ListRecommendedActions`

Additional permissions are then required based on recommended action type. The
following table summarizes the different recommended action types and the
corresponding IAM policy permissions needed in order to see the recommended
actions.

###### Note

Even with a granted IAM policy permission, the corresponding recommended
action type is only seen if the recommended action actually applies.

| Recommended action type                    | Required permission name                                                                                                                                                                       | Description                                                   |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Expired payment method                     | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"payments:ListPaymentPreferences",<br>"payments:GetPaymentInstrument"<br>`                                                           | For payment-related recommended actions.                      |
| Invalid payment method                     | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"payments:ListPaymentPreferences",<br>"payments:GetPaymentInstrument"<br>`                                                           | For payment-related recommended actions.                      |
| Payments past due                          | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"payments:GetPaymentStatus"<br>`                                                                                                     | For payment-related recommended actions.                      |
| Payments due                               | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"payments:GetPaymentStatus"<br>`                                                                                                     | For payment-related recommended actions.                      |
| Fix tax registration information           | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"tax:GetTaxRegistration"<br>`                                                                                                        | For recommended actions related to tax settings.              |
| Update tax exemption certificate           | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"tax:GetExemptions"<br>`                                                                                                             | For recommended actions related to tax settings.              |
| Migrate to granular permissions            | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"aws-portal:GetConsoleActionSetEnforced",<br>"ce:GetConsoleActionSetEnforced",<br>"purchase-orders:GetConsoleActionSetEnforced"<br>` | For recommended actions related to IAM permissions.           |
| Review budget alerts                       | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"budgets:DescribeBudgetNotificationsForAccount",<br>"budgets:DescribeBudget"<br>`                                                    | For budget-related recommended actions.                       |
| Review budgets exceeded                    | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"budgets:DescribeBudgets"<br>`                                                                                                       | For budget-related recommended actions.                       |
| Review Free Tier usage alerts              | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"freetier:GetFreeTierUsage"<br>`                                                                                                     | For recommended actions related to Free Tier.                 |
| Review anomalies                           | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"ce:GetAnomalies"<br>`                                                                                                               | For recommended actions related to cost anomaly<br>detection. |
| Review expiring reservations               | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"ce:GetReservationUtilization"<br>`                                                                                                  | For recommended actions related to cost optimization.         |
| Review expiring Savings Plans              | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"ce:GetSavingsPlansUtilizationDetails"<br>`                                                                                          | For recommended actions related to cost optimization.         |
| Review savings opportunity recommendations | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"cost-optimization-hub:ListEnrollmentStatuses",<br>"cost-optimization-hub:ListRecommendationSummaries"<br>`                          | For recommended actions related to cost optimization.         |
| Enable Cost Optimization Hub               | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"cost-optimization-hub:ListEnrollmentStatuses"<br>`                                                                                  | For recommended actions related to cost optimization.         |
| Create a budget                            | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"budgets:DescribeBudgets"<br>`                                                                                                       | For budget-related recommended actions.                       |
| Create a reservation budget                | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"budgets:DescribeBudgets",<br>"ce:GetReservationUtilization"<br>`                                                                    | For budget-related recommended actions.                       |
| Create a Savings Plans budget              | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"budgets:DescribeBudgets",<br>"ce:GetSavingsPlansUtilizationDetails"<br>`                                                            | For budget-related recommended actions.                       |
| Add an alternate billing contact           | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"account:GetAlternateContact"<br>`                                                                                                   | For account-related recommended actions.                      |
| Create an anomaly monitor                  | `<br>"bcm-recommended-actions:ListRecommendedActions",<br>"ce:GetAnomalyMonitors"<br>`                                                                                                         | For recommended actions related to cost anomaly<br>detection. |

## Managed policies

###### Note

The following AWS Identity and Access Management (IAM) actions have
reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the [bulk policy migrator scripts](../../../awsaccountbilling/latest/aboutv2/migrate-iam-permissions.md "../../../awsaccountbilling/latest/aboutv2/migrate-iam-permissions.md") to update
  polices from your payer account. You can also use the [old to granular action
  mapping reference](../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.md "../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.md") to verify the IAM actions that need to be added.

For more information, see the [Changes to AWS Billing, AWS Cost Management, and Account Consoles Permission](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/")
blog.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

Managed policies are standalone identity-based policies that you can attach to
multiple users, groups, and roles in your AWS account. You can use AWS managed
policies to control access in Billing and Cost Management.

An AWS managed policy is a standalone policy that is created and administered by
AWS. AWS managed policies are designed to provide permissions for many common
use cases. AWS managed policies make it easier for you to assign appropriate
permissions to users, groups, and roles than if you had to write the policies
yourself.

You can't change the permissions defined in AWS managed policies. AWS
occasionally updates the permissions defined in an AWS managed policy. When this
occurs, the update affects all principal entities (users, groups, and roles) that
the policy is attached to.

Billing and Cost Management provides several AWS managed policies for common use cases.

###### Topics

- [Allows full access to AWS Budgets
  including budgets actions](#budget-managedIAM-full "#budget-managedIAM-full")
- [Allows read only access to
  AWS Budgets](#budget-managedIAM-read-only "#budget-managedIAM-read-only")
- [Allows AWS Budgets to call
  services required to verify billing view access](#budget-managedIAM-billing-view "#budget-managedIAM-billing-view")
- [Allows permission to control AWS
  resources](#budget-managedIAM-SSM "#budget-managedIAM-SSM")
- [Allows Cost Optimization Hub to call services
  required to make the service work](#cost-optimization-hub-managedIAM "#cost-optimization-hub-managedIAM")
- [Allows read-only access to
  Cost Optimization Hub](#cost-optimization-hub-read-only "#cost-optimization-hub-read-only")
- [Allows admin access to Cost Optimization Hub](#cost-optimization-hub-admin "#cost-optimization-hub-admin")
- [Allows split cost
  allocation data to call services required to make the service work](#split-cost-allocation-data-managedIAM "#split-cost-allocation-data-managedIAM")
- [Allows Data Exports to access other AWS
  services](#data-exports-managedIAM "#data-exports-managedIAM")

### Allows full access to AWS Budgets

including budgets actions

Managed policy name:
`AWSBudgetsActionsWithAWSResourceControlAccess`

This managed policy is focused on the user, ensuring that you have the proper
permissions to grant permission to AWS Budgets to run the defined actions.
This policy provides full access to AWS Budgets, including budgets actions, to
retrieve the status of your policies and run AWS resources using the
AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "budgets:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "budgets.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-portal:ModifyBilling",
 "ec2:DescribeInstances",
 "iam:ListGroups",
 "iam:ListPolicies",
 "iam:ListRoles",
 "iam:ListUsers",
 "organizations:ListAccounts",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListPolicies",
 "organizations:ListRoots",
 "rds:DescribeDBInstances",
 "sns:ListTopics"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Allows read only access to

AWS Budgets

Managed policy name: `AWSBudgetsReadOnlyAccess`

This managed policy allows read only access to AWS Budgets through the
AWS Management Console. The policy can be attached to your users, groups, and roles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid": "AWSBudgetsReadOnlyAccess",
 "Effect" : "Allow",
 "Action" : [
 "aws-portal:ViewBilling",
 "budgets:ViewBudget",
 "budgets:Describe*",
 "budgets:ListTagsForResource"
 ],
 "Resource" : "*"
 }
 ]
}`

```

### Allows AWS Budgets to call

services required to verify billing view access

Managed policy name: `BudgetsServiceRolePolicy`

Allows AWS Budgets to verify access to billing views shared across account
boundaries.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "billing:GetBillingViewData"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Service-linked roles for Budgets](budgets-SLR.md "budgets-SLR.md").

### Allows permission to control AWS

resources

Managed policy name:
`AWSBudgetsActions_RolePolicyForResourceAdministrationWithSSM`

This managed policy is focused on specific actions that AWS Budgets takes on
your behalf when completing a specific action. This policy gives permission to
control AWS resources. For example, starts and stops Amazon EC2 or Amazon RDS instances
by running AWS Systems Manager (SSM) scripts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstanceStatus",
 "ec2:StartInstances",
 "ec2:StopInstances",
 "rds:DescribeDBInstances",
 "rds:StartDBInstance",
 "rds:StopDBInstance"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "ssm.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:automation-definition/AWS-StartEC2Instance:*",
 "arn:aws:ssm:*:*:automation-definition/AWS-StopEC2Instance:*",
 "arn:aws:ssm:*:*:automation-definition/AWS-StartRdsInstance:*",
 "arn:aws:ssm:*:*:automation-definition/AWS-StopRdsInstance:*"
 ]
 }
 ]
}`

```

### Allows Cost Optimization Hub to call services

required to make the service work

Managed policy name: `CostOptimizationHubServiceRolePolicy`

Allows Cost Optimization Hub to retrieve organization information and collect
optimization-related data and metadata.

To view the permissions for this policy, see [CostOptimizationHubServiceRolePolicy](../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

For more information, see [Service-linked roles for Cost Optimization Hub](cost-optimization-hub-SLR.md "cost-optimization-hub-SLR.md").

### Allows read-only access to

Cost Optimization Hub

Managed policy name: `CostOptimizationHubReadOnlyAccess`

This managed policy provides read-only access to Cost Optimization Hub.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CostOptimizationHubReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "cost-optimization-hub:ListEnrollmentStatuses",
 "cost-optimization-hub:GetPreferences",
 "cost-optimization-hub:GetRecommendation",
 "cost-optimization-hub:ListRecommendations",
 "cost-optimization-hub:ListRecommendationSummaries"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Allows admin access to Cost Optimization Hub

Managed policy name: `CostOptimizationHubAdminAccess`

This managed policy provides admin access to Cost Optimization Hub.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CostOptimizationHubAdminAccess",
 "Effect": "Allow",
 "Action": [
 "cost-optimization-hub:ListEnrollmentStatuses",
 "cost-optimization-hub:UpdateEnrollmentStatus",
 "cost-optimization-hub:GetPreferences",
 "cost-optimization-hub:UpdatePreferences",
 "cost-optimization-hub:GetRecommendation",
 "cost-optimization-hub:ListRecommendations",
 "cost-optimization-hub:ListRecommendationSummaries",
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowCreationOfServiceLinkedRoleForCostOptimizationHub",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/cost-optimization-hub.bcm.amazonaws.com/AWSServiceRoleForCostOptimizationHub"
 ],
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "cost-optimization-hub.bcm.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowAWSServiceAccessForCostOptimizationHub",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "organizations:ServicePrincipal": [
 "cost-optimization-hub.bcm.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

### Allows split cost

allocation data to call services required to make the service work

Managed policy name:
`SplitCostAllocationDataServiceRolePolicy`

Allows split cost allocation data to retrieve AWS Organizations information,
if applicable, and collect telemetry data for the split cost allocation data
services that the customer has opted in to.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AwsOrganizationsAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListParents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonManagedServiceForPrometheusAccess",
 "Effect": "Allow",
 "Action": [
 "aps:ListWorkspaces",
 "aps:QueryMetrics"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Service-linked roles for split cost allocation
data](split-cost-allocation-data-SLR.md "split-cost-allocation-data-SLR.md").

### Allows Data Exports to access other AWS

services

Managed policy name: `AWSBCMDataExportsServiceRolePolicy`

Allows Data Exports to access other AWS services such as Cost Optimization Hub on your
behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CostOptimizationRecommendationAccess",
 "Effect": "Allow",
 "Action": [
 "cost-optimization-hub:ListEnrollmentStatuses",
 "cost-optimization-hub:ListRecommendations"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Service-linked roles for Data Exports](data-exports-SLR.md "data-exports-SLR.md").

## AWS Cost Management updates to AWS managed policies

View details about updates to AWS managed policies for AWS Cost Management since this service
began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the AWS Cost Management [Document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| Update to existing policies<br>[CostOptimizationHubReadOnlyAccess](billing-permissions-ref.md#cost-optimization-hub-read-only "billing-permissions-ref.md#cost-optimization-hub-read-only")<br>[CostOptimizationHubAdminAccess](billing-permissions-ref.md#cost-optimization-hub-admin "billing-permissions-ref.md#cost-optimization-hub-admin") | We updated the policy to add the<br>`"cost-optimization-hub:ListEfficiencyMetrics"` action.                                                                                                                                                                                                                                                                                                                                                                                                                  | 11/20/2025 |
| Addition of a new policy<br>[BudgetsServiceRolePolicy](billing-permissions-ref.md#budget-managedIAM-billing-view "billing-permissions-ref.md#budget-managedIAM-billing-view")                                                                                                                                                                    | Budgets added a new policy to be used with service-linked roles,<br>which enables access to AWS services and resources used or managed<br>by Budgets.                                                                                                                                                                                                                                                                                                                                                        | 08/06/2025 |
| Update to existing policy<br>[CostOptimizationHubServiceRolePolicy](billing-permissions-ref.md#cost-optimization-hub-managedIAM "billing-permissions-ref.md#cost-optimization-hub-managedIAM")                                                                                                                                                   | We updated the policy to add the<br>`ce:GetDimensionValues` action.                                                                                                                                                                                                                                                                                                                                                                                                                                          | 07/23/2025 |
| Update to existing policy<br>[CostOptimizationHubServiceRolePolicy](billing-permissions-ref.md#cost-optimization-hub-managedIAM "billing-permissions-ref.md#cost-optimization-hub-managedIAM")                                                                                                                                                   | We updated the policy to add the<br>`organizations:ListDelegatedAdministrators` and<br>`ce:GetCostAndUsage` actions.                                                                                                                                                                                                                                                                                                                                                                                         | 07/05/2024 |
| Update to existing policy<br>[AWSBudgetsReadOnlyAccess](billing-permissions-ref.md#budget-managedIAM-read-only "billing-permissions-ref.md#budget-managedIAM-read-only")                                                                                                                                                                         | We updated the policy to add the<br>`budgets:ListTagsForResource` action.                                                                                                                                                                                                                                                                                                                                                                                                                                    | 06/17/2024 |
| Addition of a new policy<br>[AWSBCMDataExportsServiceRolePolicy](billing-permissions-ref.md#data-exports-managedIAM "billing-permissions-ref.md#data-exports-managedIAM")                                                                                                                                                                        | Data Exports added a new policy to be used with service-linked<br>roles, which enables access to other AWS services such as<br>Cost Optimization Hub.                                                                                                                                                                                                                                                                                                                                                        | 06/10/2024 |
| Addition of a new policy<br>[SplitCostAllocationDataServiceRolePolicy](billing-permissions-ref.md#split-cost-allocation-data-managedIAM "billing-permissions-ref.md#split-cost-allocation-data-managedIAM")                                                                                                                                      | Split cost allocation data added a new policy to be used with<br>service-linked roles, which enables access to AWS services and<br>resources used or managed by split cost allocation data.                                                                                                                                                                                                                                                                                                                  | 04/16/2024 |
| Update to existing policy<br>[AWSBudgetsActions_RolePolicyForResourceAdministrationWithSSM](billing-permissions-ref.md#budget-managedIAM-SSM "billing-permissions-ref.md#budget-managedIAM-SSM")                                                                                                                                                 | We updated the policy with scoped down permissions. The<br>`ssm:StartAutomationExecution` action is only allowed<br>for specific resources used by Budget actions.                                                                                                                                                                                                                                                                                                                                           | 12/14/2023 |
| Update to existing policies<br>[CostOptimizationHubReadOnlyAccess](billing-permissions-ref.md#cost-optimization-hub-read-only "billing-permissions-ref.md#cost-optimization-hub-read-only")<br>[CostOptimizationHubAdminAccess](billing-permissions-ref.md#cost-optimization-hub-admin "billing-permissions-ref.md#cost-optimization-hub-admin") | Cost Optimization Hub updated the following two managed policies:<br>• `CostOptimizationHubReadOnlyAccess`: Fixed<br>typo in "GetRecommendation"; removed permissions covered<br>by the SLR policy.<br>• `CostOptimizationHubAdminAccess`: Fixed<br>typo in "GetRecommendation"; removed permissions covered<br>by the SLR policy; added permissions to enable service<br>access and to create the SLR, so that the policy<br>provides all necessary permissions to opt in and use<br>Cost Optimization Hub. | 12/14/2023 |
| Addition of a new policy<br>[CostOptimizationHubServiceRolePolicy](billing-permissions-ref.md#cost-optimization-hub-managedIAM "billing-permissions-ref.md#cost-optimization-hub-managedIAM")                                                                                                                                                    | Cost Optimization Hub added a new policy to be used with<br>service-linked roles, which enables access to AWS services and<br>resources used or managed by Cost Optimization Hub.                                                                                                                                                                                                                                                                                                                            | 11/02/2023 |
| AWS Cost Management started tracking changes                                                                                                                                                                                                                                                                                                     | AWS Cost Management started tracking changes for its AWS managed<br>policies                                                                                                                                                                                                                                                                                                                                                                                                                                 | 11/02/2023 |
