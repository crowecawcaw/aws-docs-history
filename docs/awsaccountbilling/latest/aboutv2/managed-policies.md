

# AWS managed policies
<a name="managed-policies"></a>

Managed policies are standalone identity-based policies that you can attach to multiple users, groups, and roles in your AWS account. You can use AWS managed policies to control access in Billing.

An AWS managed policy is a standalone policy that's created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases. AWS managed policies make it easier for you to assign appropriate permissions to users, groups, and roles than if you had to write the policies yourself.

You can't change the permissions defined in AWS managed policies. AWS occasionally updates the permissions that are defined in an AWS managed policy. When this occurs, the update affects all principal entities (users, groups, and roles) that the policy is attached to.

Billing provides several AWS managed policies for common use cases.

**Topics**
+ [[`AWSPurchaseOrdersServiceRolePolicy`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPurchaseOrdersServiceRolePolicy.html)](#security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy)
+ [[`AWSBillingReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingReadOnlyAccess.html)](#security-iam-awsmanpol-AWSBillingReadOnlyAccess)
+ [[`Billing`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Billing.html)](#security-iam-awsmanpol-Billing)
+ [[`AWSAccountActivityAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountActivityAccess.html)](#security-iam-awsmanpol-AWSAccountActivityAccess)
+ [[`AWSPriceListServiceFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPriceListServiceFullAccess.html)](#security-iam-awsmanpol-AWSPriceListServiceFullAccess)
+ [Updates to AWS managed policies for AWS Billing](#security-iam-awsmanpol-updates)

## [`AWSPurchaseOrdersServiceRolePolicy`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPurchaseOrdersServiceRolePolicy.html)
<a name="security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy"></a>

This managed policy grants full access to the Billing and Cost Management console and to the purchase orders console. The policy allows the user to view, create, update, and delete the account's purchase orders.

To view the permissions for this policy, see [AWSPurchaseOrdersServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPurchaseOrdersServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## [`AWSBillingReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingReadOnlyAccess.html)
<a name="security-iam-awsmanpol-AWSBillingReadOnlyAccess"></a>

This managed policy grants users read-only access to features in the AWS Billing and Cost Management console.

### Permissions details
<a name="security-iam-awsmanpol-AWSBillingReadOnlyAccess-details"></a>

This policy includes the following permissions:
+ `account` – Retrieve information about their AWS account.
+ `aws-portal` – Grants users overall viewing permission to the Billing and Cost Management console pages.
+ `billing` – Retrieve comprehensive access to AWS billing information, such as billing preference, active contracts, credits or discounts applied, IAM preferences, seller of record, and a list of billing reports.
+ `budgets` – Retrieve information about actions set for the AWS Budgets feature.
+ `ce` – Retrieve cost and usage information, tags, and dimension values to view the AWS Cost Explorer feature.
+ `consolidatedbilling` – Retrieve roles and details about the AWS accounts configured using the consolidated billing feature.
+ `cur` – Retrieve information about their AWS Cost and Usage Report data.
+ `freetier` – Retrieve information about AWS Free Tier alert and usage preferences.
+ `invoicing` – Retrieve information about their invoice preferences.
+ `mapcredits` – Retrieve spends and credits related to the Migration Acceleration Program (MAP) 2.0 agreement.
+ `payments` – Retrieve financing, payment status, and payment instrument information.
+ `purchase-orders` – Retrieve information about invoices associated with their purchase orders.
+ `sustainability` – Retrieve carbon footprint information based on their AWS usage.
+ `tax` – Retrieve registered tax information from tax settings.

To view the permissions for this policy, see [AWSBillingReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## [`Billing`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Billing.html)
<a name="security-iam-awsmanpol-Billing"></a>

This managed policy grants users permission to view and edit the AWS Billing and Cost Management console. This includes viewing account usage, modifying budgets and payment methods.

To view the permissions for this policy, see [Billing](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Billing.html) in the *AWS Managed Policy Reference*.

## [`AWSAccountActivityAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountActivityAccess.html)
<a name="security-iam-awsmanpol-AWSAccountActivityAccess"></a>

This managed policy grants users permission to view the **Account activity** page.

To view the permissions for this policy, see [AWSAccountActivityAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountActivityAccess.html) in the *AWS Managed Policy Reference*.

## [`AWSPriceListServiceFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPriceListServiceFullAccess.html)
<a name="security-iam-awsmanpol-AWSPriceListServiceFullAccess"></a>

This managed policy grants users full access to the AWS Price List Service.

To view the permissions for this policy, see [AWSPriceListServiceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPriceListServiceFullAccess.html) in the *AWS Managed Policy Reference*.

## Updates to AWS managed policies for AWS Billing
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Billing since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Billing Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following invoicing permissions to `Billing`:+ `invoicing:ListProcurementPortals`<br />+ `invoicing:ListProcurementPortalSuppliers`<br />We added the following invoicing permissions to `AWSBillingReadOnlyAccess`:+ `invoicing:ListProcurementPortals`<br />+ `invoicing:ListProcurementPortalSuppliers` | July 31, 2026 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following cost categories permission to `Billing`:+ `ce:ListCostCategoryResourceAssociations`<br />We added the following cost categories permission to `AWSBillingReadOnlyAccess`:+ `ce:ListCostCategoryResourceAssociations` | April 08, 2026 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following invoicing permissions to `Billing`:+ `invoicing:CreateProcurementPortalPreference`<br />+ `invoicing:GetProcurementPortalPreference`<br />+ `invoicing:PutProcurementPortalPreference`<br />+ `invoicing:UpdateProcurementPortalPreferenceStatus`<br />+ `invoicing:ListProcurementPortalPreferences`<br />+ `invoicing:DeleteProcurementPortalPreference`<br />We added the following invoicing permissions to `AWSBillingReadOnlyAccess`:+ `invoicing:GetProcurementPortalPreference`<br />+ `invoicing:ListProcurementPortalPreferences` | November 19, 2025 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following invoicing permissions to `Billing`:+ `invoicing:StartInvoiceCorrection`<br />+ `invoicing:GetInvoiceCorrection`<br />+ `invoicing:ListInvoiceCorrections`<br />We added the following invoicing permissions to `AWSBillingReadOnlyAccess`:+ `invoicing:GetInvoiceCorrection`<br />+ `invoicing:ListInvoiceCorrections` | October 1, 2025 | 
| [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following permissions to `AWSBillingReadOnlyAccess`:+ `ce:GetCostAndUsageComparisons`<br />+ `ce:GetCostComparisonDrivers` | August 21, 2025 | 
| [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following AWS Free Tier permissions to `AWSBillingReadOnlyAccess`:+ `freetier:GetAccountPlanState`<br />+ `freetier:GetAccountActivity`<br />+ `freetier:ListAccountActivities` | July 09, 2025 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following MAP 2.0 permissions to `Billing` and `AWSBillingReadOnlyAccess`:+ `mapcredits:ListAssociatedPrograms`<br />+ `mapcredits:ListQuarterCredits`<br />+ `mapcredits:ListQuarterSpend`<br />+ `mapcredits:GetUniqueQuarterSpendSum` | March 27, 2025 | 
| [Billing](#security-iam-awsmanpol-Billing) – Update to existing policies | We added the following invoicing permissions to `Billing` :+ `billing:CreateBillingView`<br />+ `billing:DeleteBillingView`<br />+ `billing:GetBillingView`<br />+ `billing:GetResourcePolicy`<br />+ `billing:ListSourceViewsForBillingView`<br />+ `billing:ListTagsForResource`<br />+ `billing:TagResource`<br />+ `billing:UntagResource`<br />+ `billing:UpdateBillingView` | January 17, 2025 | 
| [AWSPurchaseOrdersServiceRolePolicy](#security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy), [Billing](#security-iam-awsmanpol-Billing), and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following invoicing permission to `AWSPurchaseOrdersServiceRolePolicy`:+ `invoicing:ListInvoiceUnits`<br />We added the following invoicing permissions to `AWSBillingReadOnlyAccess`:+ `invoicing:BatchGetInvoiceProfile`<br />+ `invoicing:GetInvoiceUnit`<br />+ `invoicing:ListInvoiceUnits`<br />+ `invoicing:ListTagsForResource`<br />We added the following invoicing permissions to `Billing`:+ `invoicing:BatchGetInvoiceProfile`<br />+ `invoicing:CreateInvoiceUnit`<br />+ `invoicing:DeleteInvoiceUnit`<br />+ `invoicing:GetInvoiceUnit`<br />+ `invoicing:ListInvoiceUnits`<br />+ `invoicing:ListTagsForResource`<br />+ `invoicing:TagResource`<br />+ `invoicing:UntagResource`<br />+ `invoicing:UpdateInvoiceUnit` | December 1, 2024 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following payments permissions to `Billing`:+  `payments:GetFinancingOption` <br />+  `payments:CreateFinancingApplication` <br />+  `payments:UpdateFinancingApplication` <br />+  `payments:GetFinancingApplication` <br />+  `payments:ListFinancingApplications` <br />+ `payments:ListFinancingLines`<br />+  `payments:GetFinancingLine` <br />+  `payments:ListFinancingLines` <br />+  `payments:GetFinancingLineWithdrawal` <br />+  `payments:ListFinancingLineWithdrawals` <br />+  `payments:ListPaymentProgramStatus` <br />+  `payments:ListPaymentProgramOptions` <br />We added the following payments permissions to `AWSBillingReadOnlyAccess`:+  `payments:GetFinancingOption` <br />+  `payments:GetFinancingApplication` <br />+  `payments:ListFinancingApplications` <br />+  `payments:GetFinancingLine` <br />+  `payments:ListFinancingLines` <br />+  `payments:GetFinancingLineWithdrawal` <br />+  `payments:ListFinancingLineWithdrawals` <br />+  `payments:ListPaymentProgramStatus` <br />+  `payments:ListPaymentProgramOptions`  | November 12, 2024 | 
| [AWSPriceListServiceFullAccess ](#security-iam-awsmanpol-AWSPriceListServiceFullAccess) – Updated policy | We added the documentation for `AWSPriceListServiceFullAccess` policy for the AWS Price List Service. The policy was initially launched in 2017. We updated `Sid": "AWSPriceListServiceFullAccess` to the existing policy. | July 2, 2024 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following cost allocation tag-related permissions to `Billing`:+  `payments:ListTagsForResource` <br />+  `payments:TagResource` <br />+  `payments:UntagResource` <br />+  `payments:ListPaymentInstruments` <br />+  `payments:UpdatePaymentInstrument` <br />We added the following tag-related permission to `AWSBillingReadOnlyAccess`:+  `payments:ListTagsForResource` <br />+  `payments:ListPaymentInstruments`  | May 31, 2024 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following cost allocation tag-related permissions to `Billing`:+  `ce:ListCostAllocationTagBackfillHistory` <br />+  `ce:StartCostAllocationTagBackfill` <br />+  `ce:GetTags` <br />+  `ce:GetDimensionValues` <br />We added the following cost allocation tag-related permission to `AWSBillingReadOnlyAccess`:+  `ce:ListCostAllocationTagBackfillHistory` <br />+  `ce:GetTags` <br />+  `ce:GetDimensionValues`  | March 25, 2024 | 
| [Billing](#security-iam-awsmanpol-Billing) and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following cost allocation tag-related permissions to `Billing`:+  `ce:ListCostAllocationTags` <br />+  `ce:UpdateCostAllocationTagsStatus` <br />We added the following cost allocation tag-related permission to `AWSBillingReadOnlyAccess`:+  `ce:ListCostAllocationTags`  | July 26, 2023 | 
| [AWSPurchaseOrdersServiceRolePolicy](#security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy), [Billing](#security-iam-awsmanpol-Billing), and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies | We added the following purchase order tag-related permissions to `Billing` and `AWSPurchaseOrdersServiceRolePolicy`:+  `purchase-orders:ListTagsForResource` <br />+  `purchase-orders:TagResource` <br />+   `purchase-orders:UntagResource` <br />We added the following tag-related permission to `AWSBillingReadOnlyAccess`:+  `purchase-orders:ListTagsForResource`  | July 17, 2023 | 
| [AWSPurchaseOrdersServiceRolePolicy](#security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy), [Billing](#security-iam-awsmanpol-Billing), and [AWSBillingReadOnlyAccess](#security-iam-awsmanpol-AWSBillingReadOnlyAccess) – Update to existing policies<br />[AWSAccountActivityAccess](#security-iam-awsmanpol-AWSAccountActivityAccess) – New AWS managed policy documented for AWS Billing | Added updated action set across all policies. | March 06, 2023 | 
| [AWSPurchaseOrdersServiceRolePolicy](#security-iam-awsmanpol-AWSPurchaseOrdersServiceRolePolicy) – Update to an existing policy | AWS Billing removed unnecessary permissions. | November 18, 2021 | 
| AWS Billing started tracking changes | AWS Billing started tracking changes for its AWS managed policies. | November 18, 2021 | 