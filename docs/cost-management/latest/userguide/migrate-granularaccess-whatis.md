

# Migrating access control for AWS Cost Management
<a name="migrate-granularaccess-whatis"></a>

**Note**  
The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:  
`aws-portal` namespace
`purchase-orders:ViewPurchaseOrders`
`purchase-orders:ModifyPurchaseOrders`
If you're using AWS Organizations, you can use the [bulk policy migrator scripts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-iam-permissions.html) to update polices from your payer account. You can also use the [old to granular action mapping reference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.html) to verify the IAM actions that need to be added.  
For more information, see the [Changes to AWS Billing, AWS Cost Management, and Account Consoles Permission](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/) blog.  
If you have an AWS account, or are a part of an AWS Organizations created on or after March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your organization.

You can use fine-grained access controls to provide individuals in your organization access to AWS Billing and Cost Management services. For example, you can provide access to Cost Explorer without providing access to the AWS Billing console.

To use the fine-grained access controls, you'll need to migrate your policies from under `aws-portal` to the new IAM actions.

The following IAM actions in your permission policies or service control policies (SCP) require updating with this migration:
+ `aws-portal:ViewAccount`
+ `aws-portal:ViewBilling`
+ `aws-portal:ViewPaymentMethods`
+ `aws-portal:ViewUsage`
+ `aws-portal:ModifyAccount`
+ `aws-portal:ModifyBilling`
+ `aws-portal:ModifyPaymentMethods`
+ `purchase-orders:ViewPurchaseOrders`
+ `purchase-orders:ModifyPurchaseOrders`

To learn how to use the **Affected policies** tool to identify your impacted IAM policies, see [How to use the affected policies tool](migrate-security-iam-tool.md).

**Note**  
Programmatic requests to AWS Cost Explorer, AWS Cost and Usage Reports, and AWS Budgets remains unaffected.  
[Activating access to the Billing and Cost Management console](control-access-billing.md#ControllingAccessWebsite-Activate) remain unchanged.

**Topics**
+ [Managing access permissions](#migrate-control-access-CMG)
+ [How to use the affected policies tool](migrate-security-iam-tool.md)

## Managing access permissions
<a name="migrate-control-access-CMG"></a>

AWS Cost Management integrates with the AWS Identity and Access Management (IAM) service so that you can control who in your organization has access to specific pages on the [AWS Cost Management console](https://console.aws.amazon.com/cost-management/). You can control access to AWS Cost Management features. For example, AWS Cost Explorer, Savings Plans, and reservation recommendations, Savings Plans and reservations utilization and coverage reports.

Use the following IAM permissions for granular control for the AWS Cost Management console.

### Using fine-grained AWS Cost Management actions
<a name="migrate-user-permissions"></a>

This table summarizes the permissions that allow or deny IAM users and roles access to your cost and usage information. For examples of policies that use these permissions, see [AWS Cost Management policy examples](billing-example-policies.md).

For a list of actions for the AWS Billing console, see [AWS Billing actions policies](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions) in the *AWS Billing user guide*.



- ** [AWS Cost Management Home](https://console.aws.amazon.com/cost-management/home#/) **
  - **IAM action:** `ce:GetCostAndUsage`<br />`ce:GetDimensionValues`<br />`ce:GetCostForecast`<br />`ce:GetReservationUtilization`<br />`ce:GetReservationPurchaseRecommendation`<br />`ce:DescribeReport`
  - **Description:** Allow or deny users permission to view the **AWS Cost Management Home** page. All IAM actions are required to view the page.

- ** [AWS Cost Explorer](https://console.aws.amazon.com/cost-management/home#/cost-explorer) **
  - **IAM action:** `ce:GetCostCategories`<br />`ce:GetDimensionValues`<br />`ce:GetCostAndUsageWithResources`<br />`ce:GetCostAndUsage`<br />`ce:GetCostForecast`<br />`ce:GetTags`<br />`ce:GetUsageForecast`<br />`ce:DescribeReport` / **Description:** Allow or deny users permission to view the **AWS Cost Explorer** page.
  - **IAM action:** `ce:CreateReport` / **Description:** Allow or deny users permission to save Cost Explorer reports.

- ** [Reports](https://console.aws.amazon.com/cost-management/home#/reports) **
  - **IAM action:** `ce:DescribeReport` / **Description:** Allow or deny users permission to view a list of saved reports.
  - **IAM action:** `ce:DeleteReport` / **Description:** Allow or deny users permission to delete a saved report.

- ** [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets) **
  - **IAM action:** `budgets:ViewBudget`<br />`budgets:DescribeBudgetActionsForBudget`<br />`budgets:DescribeBudgetAction`<br />`budgets:DescribeBudgetActionsForAccount`<br />`budgets:DescribeBudgetActionHistories` / **Description:** Allow or deny users permission to view the **Budgets** page.
  - **IAM action:** `budgets:CreateBudgetAction`<br />`budgets:ExecuteBudgetAction`<br />`budgets:DeleteBudgetAction`<br />`budgets:UpdateBudgetAction`<br />`budgets:ModifyBudget` / **Description:** Allow or deny users permission to create, delete, and modify Budgets and Budgets actions.

- ** [AWS Cost Anomaly Detection](https://console.aws.amazon.com/cost-management/home#/anomaly-detection) **
  - **IAM action:** `ce:GetDimensionValues`<br />`ce:GetCostAndUsage`<br />`ce:CreateAnomalyMonitor`<br />`ce:GetAnomalyMonitors`<br />`ce:UpdateAnomalyMonitor`<br />`ce:DeleteAnomalyMonitor`<br />`ce:CreateAnomalySubscription`<br />`ce:GetAnomalySubscriptions`<br />`ce:UpdateAnomalySubscription`<br />`ce:DeleteAnomalySubscription`<br />`ce:GetAnomalies`<br />`ce:ProvideAnomalyFeedback`
  - **Description:** Allow or deny users permission to view, create, delete, and update on the **Cost Anomaly Detection** page.

- ** [Rightsizing recommendations](https://console.aws.amazon.com/cost-management/home#/rightsizing) **
  - **IAM action:** `ce:GetDimensionValues`<br />`ce:GetTags`<br />`ce:GetRightsizingRecommendation`
  - **Description:** Allow or deny users permission to view the **Savings Plans Overview** page.

- **[Savings Plans overview](https://console.aws.amazon.com/cost-management/home#/savings-plans/overview)**
  - **IAM action:** `ce:GetSavingsPlansUtilizationDetails`<br />`ce:GetSavingsPlansPurchaseRecommendation` / **Description:** 
  - **IAM action:** `ce:DescribeNotificationSubscription` / **Description:** Allow or deny users permission to view the existing notification settings for expiring and queued Savings Plans alerts.
  - **IAM action:** `ce:CreateNotificationSubscription`<br />`ce:UpdateNotificationSubscription`<br />`ce:DeleteNotificationSubscription` / **Description:** Allow or deny users permission to update the existing notification settings for expiring and queued Savings Plans alerts.

- **[Savings Plans inventory](https://console.aws.amazon.com/cost-management/home#/savings-plans/inventory)**
  - **IAM action:** `savingsplans:DescribeSavingsPlans`<br />`ce:GetSavingsPlansUtilizationDetails` / **Description:** Allow or deny users permissions to view purchased Savings Plans.
  - **IAM action:** `savingsplans:DescribeSavingsPlansOfferings` / **Description:** Allow or deny users permissions to add the Savings Plans they wish to renew to the cart.

- ** [Savings Plans recommendations](https://console.aws.amazon.com/cost-management/home#/savings-plans/recommendations) **
  - **IAM action:** `ce:GetSavingsPlansPurchaseRecommendation`<br />`ce:ListSavingsPlansPurchaseRecommendationGeneration` / **Description:** Allow or deny users permission to view generated Savings Plans recommendations.
  - **IAM action:** `ce:StartSavingsPlansPurchaseRecommendationGeneration` / **Description:** Allow or deny users permission to calculate a new set of recommendations based on the latest usage and Savings Plans inventory.

- ** [Purchase Savings Plans](https://console.aws.amazon.com/cost-management/home#/savings-plans/purchase) **
  - **IAM action:** `savingsplans:DescribeSavingsPlansOfferings`
  - **Description:** Allow or deny users permission to add Savings Plans to the cart.

- ** [Savings Plans utilization report](https://console.aws.amazon.com/cost-management/home#/savings-plans/utilization) **
  - **IAM action:** `ce:DescribeReport`<br />`ce:GetSavingsPlansUtilization`<br />`ce:GetSavingsPlansUtilizationDetails`<br />`ce:GetDimensionValues` / **Description:** Allow or deny users permission to view utilization of your existing Savings Plans.
  - **IAM action:** `savingsplans:DescribeSavingsPlanRates` / **Description:** Allow or deny users permission to view the Savings Plans rate.

- ** [Savings Plans coverage report](https://console.aws.amazon.com/cost-management/home#/savings-plans/coverage) **
  - **IAM action:** `ce:GetDimensionValues`<br />`ce:GetSavingsPlansCoverage`<br />`ce:GetCostCategories`<br />`ce:DescribeReport`<br />`ce:GetSavingsPlansPurchaseRecommendation`
  - **Description:** Allow or deny users permission to view the eligible spends covered by Savings Plans.

- ** [Savings Plans cart](https://console.aws.amazon.com/cost-management/home#/savings-plans/cart) **
  - **IAM action:** `savingsplans:DescribeSavingsPlansOfferings`<br />`savingsplans:DescribeSavingsPlans` / **Description:** Allow or deny users permission to purchase Savings Plans.
  - **IAM action:** `savingsplans:CreateSavingsPlan` / **Description:** 

- ** [Reservations overview](https://console.aws.amazon.com/cost-management/home#/ri/dashboard) **
  - **IAM action:** `ce:GetReservationUtilization`<br />`ce:GetReservationCoverage`<br />`ce:GetReservationPurchaseRecommendation`<br />`ce:DescribeReport` / **Description:** Allow or deny users permission to view the **Reservations Overview** page.
  - **IAM action:** `ce:DescribeNotificationSubscription` / **Description:** Allow or deny users permission to view existing notification settings for expiring reserved instances (RI) alerts.
  - **IAM action:** `ce:CreateNotificationSubscription`<br />`ce:UpdateNotificationSubscription`<br />`ce:DeleteNotificationSubscription` / **Description:** Allow or deny users permission to update notification settings for expiring RI alerts.

- ** [Reservations recommendations](https://console.aws.amazon.com/cost-management/home#/ri/recommendations) **
  - **IAM action:** `ce:GetReservationPurchaseRecommendation`<br />`ce:GetDimensionValues`
  - **Description:** Allow or deny users permission to view reservations recommendations.

- ** [Reservations utilization reports](https://console.aws.amazon.com/cost-management/home#/ri/utilization) **
  - **IAM action:** `ce:GetDimensionValues`<br />`ce:GetReservationUtilization`<br />`ce:DescribeReport` / **Description:** Allow or deny users permission to view utilization of your existing RI.
  - **IAM action:** `ce:CreateReport` / **Description:** Allow or deny users permission to save RI reports.

- ** [Reservations coverage report ](https://console.aws.amazon.com/cost-management/home#/ri/coverage) **
  - **IAM action:** `ce:GetReservationCoverage`<br />`ce:GetReservationPurchaseRecommendation`<br />`ce:DescribeReport`<br />`ce:GetDimensionValues`<br />`ce:GetCostCategories` / **Description:** Allow or deny users permission to view eligible spends covered by Reservations (RIs).
  - **IAM action:** `ce:CreateReport` / **Description:** Allow or deny users permission to save RI coverage reports.

- ** [Preferences](https://console.aws.amazon.com/cost-management/home#/settings) **
  - **IAM action:** `ce:GetPreferences` / **Description:** Allow or deny users permission to view AWS Cost Management preferences.
  - **IAM action:** `ce:UpdatePreferences` / **Description:** Allow or deny users permission to update AWS Cost Management preferences.

