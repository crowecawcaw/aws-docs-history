

# Migrating access control for AWS Billing
<a name="migrate-granularaccess-whatis"></a>

**Note**  
The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:  
`aws-portal` namespace
`purchase-orders:ViewPurchaseOrders`
`purchase-orders:ModifyPurchaseOrders`
If you're using AWS Organizations, you can use the [bulk policy migrator scripts](migrate-iam-permissions.md) or bulk policy migrator to update polices from your payer account. You can also use the [old to granular action mapping reference](migrate-granularaccess-iam-mapping-reference.md) to verify the IAM actions that need to be added.  
If you have an AWS account, or are a part of an AWS Organizations created on or after March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your organization.

You can use fine-grained access controls to provide individuals in your organization access to AWS Billing and Cost Management services. For example, you can provide access to Cost Explorer without providing access to the Billing and Cost Management console.

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
API access to AWS Cost Explorer, AWS Cost and Usage Reports, and AWS Budgets remains unaffected.  
[Activating access to the Billing and Cost Management console](control-access-billing.md#ControllingAccessWebsite-Activate) remain unchanged.

**Topics**
+ [Managing access permissions](#migrate-control-access-billing)
+ [Using the console to bulk migrate your policies](migrate-granularaccess-console.md)
+ [How to use the affected policies tool](migrate-security-iam-tool.md)
+ [Use scripts to bulk migrate your policies to use fine-grained IAM actions](migrate-iam-permissions.md)
+ [Mapping fine-grained IAM actions reference](migrate-granularaccess-iam-mapping-reference.md)

## Managing access permissions
<a name="migrate-control-access-billing"></a>

AWS Billing integrates with the AWS Identity and Access Management (IAM) service so that you can control who in your organization can access specific pages on the [Billing and Cost Management console](https://console.aws.amazon.com/billing/). This includes features like Payments, Billing, Credits, Free Tier, Payment preferences, Consolidated billing, Tax settings, and Account pages.

Use the following IAM permissions for granular control for the Billing and Cost Management console.

To provide fine-grained access, replace the `aws-portal` policy with `account`, `billing`, `payments`, `freetier`, `invoicing`, `tax`, and `consolidatedbilling`.

Additionally, replace `purchase-orders:ViewPurchaseOrders` and `purchase-orders:ModifyPurchaseOrders` with the fine-grained actions under `purchase-orders`, `account`, and `payments`.

### Using fine-grained AWS Billing actions
<a name="migrate-user-permissions"></a>

This table summarizes the permissions that allow or deny IAM users and roles access to your billing information. For examples of policies that use these permissions, see [AWS Billing policy examples](billing-example-policies.md). 

For a list of actions for the AWS Cost Management console, see [AWS Cost Management actions policies](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#user-permissions) in the *AWS Cost Management User Guide*.



- ** [Billing Home](https://console.aws.amazon.com/billing/home#/) **
  - **IAM action:** `account:GetAccountInformation`<br />`billing:Get*`<br />`payments:List*`<br />`tax:List*`
  - **Description:** Grants permission to view the **Home** page. These are read-only permissions.These are permissions for the console only. No API access is available for these permissions.

- ** [Bills](https://console.aws.amazon.com/billing/home#/bills) **
  - **IAM action:** `account:GetAccountInformation`<br />`billing:Get*`<br />`consolidatedbilling:Get*`<br />`consolidatedbilling:List*`<br />`invoicing:List*`<br />`payments:List*` / **Description:** Grants permission to view the **Bills** page. These are read-only permissions.These are permissions for the console only. No API access is available for these permissions.
  - **IAM action:** `invoicing:Get*` / **Description:** Grants permission to download invoices from the **Bills** page.This is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `cur:Get*` / **Description:** Grants permission to download CSV reports from the **Bills** page.This is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `billing:ListBillingViews` / **Description:** Grants permission to view the `ARN` and description of each AWS Billing Conductor billing group created. This is required to create a report preference for specific groups.This is a permission for the console only. No API access is available for this permission.

- ** [Payments](https://console.aws.amazon.com/billing/home#/paymentsoverview) **
  - **IAM action:** `account:GetAccountInformation`<br />`billing:Get*`<br />`payments:Get*`<br />`payments:List*` / **Description:** Grants permission to view the **Payments** page. These are read-only permissions to the **Payments due**, **Unapplied funds**, **Transaction**, and **Advance pay** tabs.These are permissions for the console only. No API access is available for these permissions.
  - **IAM action:** `invoicing:Get*` / **Description:** Grants permission to download an invoice from the **Transactions** tab.This is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `payments:Update*` / **Description:** Grants permission action required to use Advance Pay and set up payment details.
  - **IAM action:** `payments:Make*`<br />`invoicing:Get*` / **Description:** Grants permission to generate a funding request document for Advance Pay, and make a payment.

- ** [Credits](https://console.aws.amazon.com/billing/home#/credits) **
  - **IAM action:** `billing:Get*`<br />`account:GetAccountInformation` / **Description:** Grants permission to view the **Credits** page.
  - **IAM action:** `billing:RedeemCredits` / **Description:** Grants permission to redeem credits.

- ** [Purchase orders](https://console.aws.amazon.com/billing/home#/purchaseorders) **
  - **IAM action:** `account:GetAccountInformation`<br />`account:GetContactInformation`<br />`payments:Get*`<br />`payments:List*`<br />`purchase-orders:ListPurchaseOrders`<br />`purchase-orders:ListPurchaseOrderInvoices`<br />`tax:ListTaxRegistrations`<br />`consolidatedbilling:GetAccountBillingRole` / **Description:** Grants permission to view the **Purchase orders** page.
  - **IAM action:** `purchase-orders:GetPurchaseOrder` / **Description:** Grants permission to view details of a purchase order.
  - **IAM action:** `purchase-orders:AddPurchaseOrder` / **Description:** Grants permission to add a purchase order.
  - **IAM action:** `purchase-orders:DeletePurchaseOrder` / **Description:** Grants permission to delete a purchase order.
  - **IAM action:** `purchase-orders:UpdatePurchaseOrder`<br />`purchase-orders:UpdatePurchaseOrderStatus` / **Description:** Grants permission to update purchase orders and purchase order status.

- ** [AWS Cost and Usage Reports](https://console.aws.amazon.com/billing/home#/reports) **
  - **IAM action:** `cur:GetClassic*`<br />`cur:DescribeReportDefinitions` / **Description:** Grants permission to view a list of AWS CUR reports on the **AWS Cost and Usage Reports** page.`cur:GetClassic*` is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `billing:ListBillingViews` / **Description:** Grants permission to view the `ARN` and description of each billing group created in AWS Billing Conductor. This is required to create a report preference for specific groups.This is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `s3:ListAllMyBuckets`<br />`s3:CreateBucket`<br />`s3:PutBucketPolicy`<br />`s3:GetBucketLocation`<br />`cur:Validate*`<br />`cur:PutReportDefinition` / **Description:** Grants permission actions required to create a new AWS CUR report.`cur:Validate*` is a permission for the console only. No API access is available for these permissions.
  - **IAM action:** `cur:Validate*`<br />`s3:CreateBucket`<br />`s3:ListAllMyBuckets`<br />`s3:PutBucketPolicy`<br />`s3:GetBucketLocation`<br />`cur:ModifyReportDefinition` / **Description:** Grants permission to edit AWS CUR definition.`cur:Validate*` is a permission for the console only. No API access is available for these permissions.
  - **IAM action:** `cur:DeleteReportDefinition` / **Description:** Grants permission to delete AWS CUR reports.
  - **IAM action:** `cur:GetUsage*` / **Description:** Grants permission to download usage reports.
  - **IAM action:** `sustainability:GetCarbonFootprintSummary` / **Description:** Grants permission to view sustainability data for your AWS account.

- ** [Cost categories](https://console.aws.amazon.com/billing/home#/costcategories) **
  - **IAM action:** `account:GetAccountInformation`<br />`ce:ListCostCategoryDefinitions`<br />`ce:DescribeCostCategoryDefinition`<br />`ce:GetCostAndUsage`<br />`ce:ListTagsForResource`<br />`consolidatedbilling:GetAccountBillingRole` / **Description:** Grants permission to view cost categories.`account:GetAccountInformation` is a permission for the console only. No API access is available for these permissions.
  - **IAM action:** `billing:Get*`<br />`ce:TagResource`<br />`ce:ListCostAllocationTags`<br />`consolidatedbilling:List*`<br />`ce:CreateCostCategoryDefinition`<br />`pricing:DescribeServices`<br />`ce:GetDimensionValues`<br />`ce:GetTags` / **Description:** Grants permission to create cost categories.`billing:Get*` and `consolidatedbilling:List*` is a permission for the console only. No API access is available for these permissions.
  - **IAM action:** `ce:UpdateCostCategoryDefinition`<br />`ce:UntagResource` / **Description:** Grants permission to modify cost categories.
  - **IAM action:** `ce:DeleteCostCategoryDefinition` / **Description:** Grants permission to delete cost categories.

- ** [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) **
  - **IAM action:** `account:GetAccountInformation`<br />`ce:ListCostAllocationTags`<br />`consolidatedbilling:GetAccountBillingRole` / **Description:** Grants permission to view cost allocation tags.
  - **IAM action:** `ce:UpdateCostAllocationTagsStatus` / **Description:** Grants permission to activate or deactivate cost allocation tags.

- ** [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets) **
  - **IAM action:** `budgets:ViewBudget`<br />`budgets:DescribeBudgetActionsForBudget`<br />`budgets:DescribeBudgetAction`<br />`budgets:DescribeBudgetActionsForAccount`<br />`budgets:DescribeBudgetActionHistories` / **Description:** Grants permission to view the **Budgets** page.
  - **IAM action:** `budgets:CreateBudgetAction`<br />`budgets:ExecuteBudgetAction`<br />`budgets:DeleteBudgetAction`<br />`budgets:UpdateBudgetAction`<br />`budgets:ModifyBudget` / **Description:** Grants permission to create, delete, and modify Budgets and Budgets actions.

- ** [Free tier](https://console.aws.amazon.com/billing/home#/freetier) **
  - **IAM action:** `billing:Get*`<br />`freetier:Get*`
  - **Description:** Grants permission to view free tier usage limits and month to date usage status.

- ** [Billing preferences](https://console.aws.amazon.com/billing/home#/preferences) **
  - **IAM action:** `account:GetAccountInformation`<br />`billing:Get*`<br />`consolidatedbilling:Get*`<br />`consolidatedbilling:List*`<br />`cur:GetClassic*`<br />`cur:Validate*`<br />`freetier:Get*`<br />`invoicing:Get*` / **Description:** Grants permission actions required to view all sections on the **Billing preferences** page.These are permissions for the console only. No API access is available for these permissions.
  - **IAM action:** `billing:Update*`<br />`freetier:Put*`<br />`cur:PutClassic*`<br />`s3:ListAllMyBuckets`<br />`s3:CreateBucket`<br />`s3:PutBucketPolicy`<br />`s3:GetBucketLocation`<br />`invoicing:Put*` / **Description:** Grants permission to make the following changes in the **Billing preferences** page:+ Turn credit sharing to RI or Savings Plans discount sharing on or off<br />+ Set **Free Tier Usage Alert** preferences<br />+ Set **detailed billing reports** delivery settings and preferences<br />+ Set or update the **PDF invoice by email** preferences`billing:Update*`, `freetier:Put*`, `cur:PutClassic*` are permissions for the console only. No API access is available for these permissions.

- ** [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences) **
  - **IAM action:** `account:GetAccountInformation`<br />`billing:Get*`<br />`payments:GetPaymentInstrument`<br />`payments:List*`<br />`payments:GetPaymentStatus` / **Description:** Grants permission to view the **Payment preferences** page.These are permissions for the console only. No API access is available for these permissions.
  - **IAM action:** `payments:Update*`<br />`payments:Make*`<br />`payments:CreatePaymentInstrument`<br />`payments:DeletePaymentInstrument` / **Description:** Grants permission to create or update payment methods.`payments:Make*` is only required if a payment card requires multi-factor authentication (MFA).
  - **IAM action:** `tax:PutTaxRegistration`<br />`tax:Delete*`<br />`payments:UpdatePaymentPreferences`<br />`payments:CreatePaymentInstrument` / **Description:** Grants permission to update or delete tax registration numbers.
  - **IAM action:** `payments:Update*` / **Description:** Grants permission to update payment profiles.This is a permission for the console only. No API access is available for this permission.

- ** [Tax settings](https://console.aws.amazon.com/billing/home#/tax) **
  - **IAM action:** `tax:List*`<br />`tax:Get*` / **Description:** Grants permission to view tax settings.
  - **IAM action:** `tax:BatchPut*` / **Description:** Grants permission action required to update tax settings.
  - **IAM action:** `tax:Put*` / **Description:** Grants permission to set tax inheritance.
  - **IAM action:** `tax:UpdateExemptions`<br />`support:CreateCase`<br />`support:AddAttachmentsToSet` / **Description:** Grants permission to update tax exemption.

- ** [Account](https://console.aws.amazon.com/billing/home#/account) **
  - **IAM action:** `account:Get*`<br />`account:List*`<br />`billing:Get*`<br />`payments:List*` / **Description:** Grants permission to view **Account settings**.`billing:Get*` is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `account:CloseAccount` / **Description:** Grants permission to close AWS accounts.This is a permission for the console only. No API access is available for this permission.
  - **IAM action:** `account:DisableRegion` / **Description:** Grants permission to turn off an AWS Region on the **Account** page.
  - **IAM action:** `account:EnableRegion` / **Description:** Grants permission to turn on an AWS Region on the **Account** page.
  - **IAM action:** `account:PutAlternateContact` / **Description:** Grants permission to write alternate contacts for the account.
  - **IAM action:** `account:PutChallengeQuestions` / **Description:** Grants permission to set security challenge questions for the account.This permission is for the console only. No API access is available for this permission.
  - **IAM action:** `account:PutContactInformation` / **Description:** Grants permission action required to set or write main contact information, including address, for the account.
  - **IAM action:** `billing:PutContractInformation` / **Description:** Grants permission to set the account contract information, if the account is used to service public-sector customers. Information that can be pulled includes end user organization names, contract number, and PO numbers.This permission is for the console only. No API access is available for this permission.
  - **IAM action:** `billing:Update*` / **Description:** Grants permission action required to turn on or turn off the **Activate IAM Access** setting on the **Account** page.
  - **IAM action:** `payments:Update*` / **Description:** Grants permission to set advance pay, currency preference, billing contact details and address, and payment terms and conditions.

