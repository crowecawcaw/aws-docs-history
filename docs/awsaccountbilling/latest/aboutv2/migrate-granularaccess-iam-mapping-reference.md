# Mapping fine-grained IAM

actions reference

###### Note

The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the [bulk policy migrator scripts](migrate-iam-permissions.md "migrate-iam-permissions.md") or bulk policy migrator to update
  polices from your payer account. You can also use the old to granular action
  mapping reference to verify the IAM actions that need to be added.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

You will need to migrate the following IAM actions in your permission policies or service
control policies (SCP):

- `aws-portal:ViewAccount`
- `aws-portal:ViewBilling`
- `aws-portal:ViewPaymentMethods`
- `aws-portal:ViewUsage`
- `aws-portal:ModifyAccount`
- `aws-portal:ModifyBilling`
- `aws-portal:ModifyPaymentMethods`
- `purchase-orders:ViewPurchaseOrders`
- `purchase-orders:ModifyPurchaseOrders`
  You can use this topic to view the mapping of the old to new fine-grained actions for each
  IAM action that we're retiring.

###### Overview

1. Review your affected IAM policies in your AWS account. To do so, follow the steps in
   the **Affected policies** tool to identify your affected IAM policies.
   See [How to use the affected policies
   tool](migrate-security-iam-tool.md "migrate-security-iam-tool.md").
2. Use the IAM console to add the new granular permissions to your policy. For example,
   if your policy allows the `purchase-orders:ModifyPurchaseOrders` permission, you
   will need to add each action in the [Mapping for
   purchase-orders:ModifyPurchaseOrders](#mapping-for-purchase-ordersmodifypurchaseorders "#mapping-for-purchase-ordersmodifypurchaseorders") table.

**Old policy**

The following policy allows a user to add, delete, or modify any purchase order in the
account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "purchase-orders:ModifyPurchaseOrders",
 "Resource": "arn:aws:purchase-orders::123456789012:purchase-order/*"
 }
 ]
}`

```

**New policy**

The following policy also allows a user to add, delete, or modify any purchase order in
the account. Note that each granular permission appears after the old
`purchase-orders:ModifyPurchaseOrders` permission. These permissions give you
more control over what actions you want to allow or deny.

###### Tip

We recommend that you keep the old permissions to ensure that you don't lose
permissions until this migration is complete.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "purchase-orders:ModifyPurchaseOrders",
 "purchase-orders:AddPurchaseOrder",
 "purchase-orders:DeletePurchaseOrder",
 "purchase-orders:UpdatePurchaseOrder",
 "purchase-orders:UpdatePurchaseOrderStatus"
 ],
 "Resource": "arn:aws:purchase-orders::123456789012:purchase-order/*"
 }
 ]
}`

```

3. Save your changes.

###### Notes

- To edit policies manually in the IAM console, see [Editing customer managed policies (console)](../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-inline-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-edit.md#edit-inline-policy-console") in the
  _IAM User Guide_.
- To bulk migrate your IAM policies to use fine-grained actions (new actions), see
  [Use scripts to bulk migrate your policies to use
  fine-grained IAM actions](migrate-iam-permissions.md "migrate-iam-permissions.md").

###### Contents

- [Mapping for
  aws-portal:ViewAccount](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewaccount "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewaccount")
- [Mapping for
  aws-portal:ViewBilling](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewbilling "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewbilling")
- [Mapping for
  aws-portal:ViewPaymentMethods](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewpaymentmethods "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewpaymentmethods")
- [Mapping for
  aws-portal:ViewUsage](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewusage "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalviewusage")
- [Mapping for
  aws-portal:ModifyAccount](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifyaccount "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifyaccount")
- [Mapping for
  aws-portal:ModifyBilling](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifybilling "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifybilling")
- [Mapping for
  aws-portal:ModifyPaymentMethods](migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifypaymentmethods "migrate-granularaccess-iam-mapping-reference.md#mapping-for-aws-portalmodifypaymentmethods")
- [Mapping for
  purchase-orders:ViewPurchaseOrders](migrate-granularaccess-iam-mapping-reference.md#mapping-for-purchase-ordersviewpurchaseorders "migrate-granularaccess-iam-mapping-reference.md#mapping-for-purchase-ordersviewpurchaseorders")
- [Mapping for
  purchase-orders:ModifyPurchaseOrders](migrate-granularaccess-iam-mapping-reference.md#mapping-for-purchase-ordersmodifypurchaseorders "migrate-granularaccess-iam-mapping-reference.md#mapping-for-purchase-ordersmodifypurchaseorders")

## Mapping for

aws-portal:ViewAccount

| New action                        | Description                                                                                                                                                                                                          | Access level |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `account:GetAccountInformation`   | Grants permission to retrieve the account information for an account                                                                                                                                                 | Read         |
| `account:GetAlternateContact`     | Grants permission to retrieve the alternate contacts for an account                                                                                                                                                  | Read         |
| `account:GetContactInformation`   | Grants permission to retrieve the primary contact information for an account                                                                                                                                         | Read         |
| `billing:GetContractInformation`  | Grants permission to view the account's contract information including the<br>contract number, end-user organization names, purchase order numbers, and if the<br>account is used to service public-sector customers | Read         |
| `billing:GetIAMAccessPreference`  | Grants permission to retrieve the state of the \*_Allow IAM<br>Access_<br>• billing preference                                                                                                                       | Read         |
| `billing:GetSellerOfRecord`       | Grants permission to retrieve the account's default seller of record                                                                                                                                                 | Read         |
| `payments:ListPaymentPreferences` | Grants permission to get payment preferences (for example, preferred payment<br>currency, preferred payment method)                                                                                                  | Read         |

## Mapping for

aws-portal:ViewBilling

| New action                                            | Description                                                                                                                                                                                                          | Access level |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `account:GetAccountInformation`                       | Grants permission to retrieve the account information for an account                                                                                                                                                 | Read         |
| `billing:GetBillingData`                              | Grants permission to perform queries on billing information                                                                                                                                                          | Read         |
| `billing:GetBillingDetails`                           | Grants permission to view detailed line item billing information                                                                                                                                                     | Read         |
| `billing:GetBillingNotifications`                     | Grants permission to view notifications sent by AWS related to your accounts<br>billing information                                                                                                                  | Read         |
| `billing:GetBillingPreferences`                       | Grants permission to view billing preferences such as Reserved Instances, Savings Plans,<br>and credits sharing                                                                                                      | Read         |
| `billing:GetContractInformation`                      | Grants permission to view the account's contract information including the<br>contract number, end-user organization names, purchase order numbers, and if the<br>account is used to service public-sector customers | Read         |
| `billing:GetCredits`                                  | Grants permission to view credits that have been redeemed                                                                                                                                                            | Read         |
| `billing:GetIAMAccessPreference`                      | Grants permission to retrieve the state of the \*_Allow IAM<br>Access_<br>• billing preference                                                                                                                       | Read         |
| `billing:GetSellerOfRecord`                           | Grants permission to retrieve the account's default seller of record                                                                                                                                                 | Read         |
| `billing:ListBillingViews`                            | Grants permission to get billing information for your proforma billing<br>groups                                                                                                                                     | List         |
| `ce:DescribeNotificationSubscription`                 | Grants permission to view reservation expiration alerts                                                                                                                                                              | Read         |
| `ce:DescribeReport`                                   | Grants permission to view Cost Explorer reports page                                                                                                                                                                 | Read         |
| `ce:GetAnomalies`                                     | Grants permission to retrieve anomalies                                                                                                                                                                              | Read         |
| `ce:GetAnomalyMonitors`                               | Grants permission to query anomaly monitors                                                                                                                                                                          | Read         |
| `ce:GetAnomalySubscriptions`                          | Grants permission to query anomaly subscriptions                                                                                                                                                                     | Read         |
| `ce:GetCostAndUsage`                                  | Grants permission to retrieve the cost and usage metrics for your account                                                                                                                                            | Read         |
| `ce:GetCostAndUsageWithResources`                     | Grants permission to retrieve the cost and usage metrics with resources for your<br>account                                                                                                                          | Read         |
| `ce:GetCostCategories`                                | Grants permission to query cost category names and values for a specified<br>time period                                                                                                                             | Read         |
| `ce:GetCostForecast`                                  | Grants permission to retrieve a cost forecast for a forecast time period                                                                                                                                             | Read         |
| `ce:GetDimensionValues`                               | Grants permission to retrieve all available filter values for a filter for a<br>period of time                                                                                                                       | Read         |
| `ce:GetPreferences`                                   | Grants permission to view the Cost Explorer preferences page                                                                                                                                                         | Read         |
| `ce:GetReservationCoverage`                           | Grants permission to retrieve the reservation coverage for your account                                                                                                                                              | Read         |
| `ce:GetReservationPurchaseRecommendation`             | Grants permission to retrieve the reservation recommendations for your account                                                                                                                                       | Read         |
| `ce:GetReservationUtilization`                        | Grants permission to retrieve the reservation utilization for your account                                                                                                                                           | Read         |
| `ce:GetRightsizingRecommendation`                     | Grants permission to retrieve the rightsizing recommendations for your account                                                                                                                                       | Read         |
| `ce:GetSavingsPlansCoverage`                          | Grants permission to retrieve the Savings Plans coverage for your account                                                                                                                                            | Read         |
| `ce:GetSavingsPlansPurchaseRecommendation`            | Grants permission to retrieve the Savings Plans recommendations for your account                                                                                                                                     | Read         |
| `ce:GetSavingsPlansUtilization`                       | Grants permission to retrieve the Savings Plans utilization for your account                                                                                                                                         | Read         |
| `ce:GetSavingsPlansUtilizationDetails`                | Grants permission to retrieve the Savings Plans utilization details for your account                                                                                                                                 | Read         |
| `ce:GetTags`                                          | Grants permission to query tags for a specified time period                                                                                                                                                          | Read         |
| `ce:GetUsageForecast`                                 | Grants permission to retrieve a usage forecast for a forecast time period                                                                                                                                            | Read         |
| `ce:ListCostAllocationTags`                           | Grants permission to list cost allocation tags                                                                                                                                                                       | List         |
| `ce:ListSavingsPlansPurchaseRecommendationGeneration` | Grants permission to retrieve a list of your historical recommendation<br>generations                                                                                                                                | Read         |
| `consolidatedbilling:GetAccountBillingRole`           | Grants permission to get account role (payer, linked, regular)                                                                                                                                                       | Read         |
| `consolidatedbilling:ListLinkedAccounts`              | Grants permission to get list of member and linked accounts                                                                                                                                                          | List         |
| `cur:GetClassicReport`                                | Grants permission to get the CSV report for your bill                                                                                                                                                                | Read         |
| `cur:GetClassicReportPreferences`                     | Grants permission to get the classic report enablement status for usage reports                                                                                                                                      | Read         |
| `cur:ValidateReportDestination`                       | Grants permission to validates if the Amazon S3 bucket exists with appropriate<br>permissions for AWS CUR delivery                                                                                                   | Read         |
| `freetier:GetFreeTierAlertPreference`                 | Grants permission to get AWS Free Tier alert preference (by email address)                                                                                                                                           | Read         |
| `freetier:GetFreeTierUsage`                           | Grants permission to get AWS Free Tier usage limits and month-to-date (MTD) usage<br>status                                                                                                                          | Read         |
| `invoicing:GetInvoiceEmailDeliveryPreferences`        | Grants permission to get invoice email delivery preferences                                                                                                                                                          | Read         |
| `invoicing:GetInvoicePDF`                             | Grants permission to get the invoice PDF                                                                                                                                                                             | Read         |
| `invoicing:ListInvoiceSummaries`                      | Grants permission to get invoice summary information for your account or linked<br>account                                                                                                                           | List         |
| `payments:GetPaymentInstrument`                       | Grants permission to get information about a payment instrument                                                                                                                                                      | Read         |
| `payments:GetPaymentStatus`                           | Grants permission to get payment status of invoices                                                                                                                                                                  | Read         |
| `payments:ListPaymentPreferences`                     | Grants permission to get payment preferences (for example, preferred payment<br>currency, preferred payment method)                                                                                                  | Read         |
| `tax:GetTaxInheritance`                               | Grants permission to view tax inheritance status                                                                                                                                                                     | Read         |
| `tax:GetTaxRegistrationDocument`                      | Grants permission to download tax registration documents                                                                                                                                                             | Read         |
| `tax:ListTaxRegistrations`                            | Grants permission to view tax registration                                                                                                                                                                           | Read         |

## Mapping for

aws-portal:ViewPaymentMethods

| New action                        | Description                                                                                                         | Access level |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| `account:GetAccountInformation`   | Grants permission to retrieve the account information for an account                                                | Read         |
| `invoicing:GetInvoicePDF`         | Grants permission to get the invoice PDF                                                                            | Read         |
| `payments:GetPaymentInstrument`   | Grants permission to get information about a payment instrument                                                     | Read         |
| `payments:GetPaymentStatus`       | Grants permission to get payment status of invoices                                                                 | Read         |
| `payments:ListPaymentPreferences` | Grants permission to get payment preferences (for example, preferred payment<br>currency, preferred payment method) | List         |

## Mapping for

aws-portal:ViewUsage

| New action           | Description                                                                                                                                   | Access level |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `cur:GetUsageReport` | Grants permission to get a list of AWS services, the usage type and operation<br>for the usage report workflow, and to download usage reports | Read         |

## Mapping for

aws-portal:ModifyAccount

| New action                          | Description                                                                                                                                              | Access level |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `account:CloseAccount`              | Grants permission to close an account                                                                                                                    | Write        |
| `account:DeleteAlternateContact`    | Grants permission to delete the alternate contacts for an account                                                                                        | Write        |
| `account:PutAlternateContact`       | Grants permission to modify the alternate contacts for an account                                                                                        | Write        |
| `account:PutChallengeQuestions`     | Grants permission to modify the challenge questions for an account                                                                                       | Write        |
| `account:PutContactInformation`     | Grants permission to update the primary contact information for an account                                                                               | Write        |
| `billing:PutContractInformation`    | Grants permission to set the account's contract information end-user<br>organization names and if the account is used to service public-sector customers | Write        |
| `billing:UpdateIAMAccessPreference` | Grants permission to update the \*_Allow IAM Access_<br>• billing<br>preference                                                                          | Write        |
| `payments:UpdatePaymentPreferences` | Grants permission to update payment preferences (for example, preferred payment<br>currency, preferred payment method)                                   | Write        |

## Mapping for

aws-portal:ModifyBilling

| New action                                             | Description                                                                                                                                              | Access level |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `billing:PutContractInformation`                       | Grants permission to set the account's contract information end-user<br>organization names and if the account is used to service public-sector customers | Write        |
| `billing:RedeemCredits`                                | Grants permission to redeem an AWS credit                                                                                                                | Write        |
| `billing:UpdateBillingPreferences`                     | Grants permission to update billing preferences such as Reserved Instances,<br>Savings Plans, and credits sharing                                        | Write        |
| `ce:CreateAnomalyMonitor`                              | Grants permission to create a new anomaly monitor                                                                                                        | Write        |
| `ce:CreateAnomalySubscription`                         | Grants permission to create a new anomaly subscription                                                                                                   | Write        |
| `ce:CreateNotificationSubscription`                    | Grants permission to create reservation expiration alerts                                                                                                | Write        |
| `ce:CreateReport`                                      | Grants permission to create Cost Explorer reports                                                                                                        | Write        |
| `ce:DeleteAnomalyMonitor`                              | Grants permission to delete an anomaly monitor                                                                                                           | Write        |
| `ce:DeleteAnomalySubscription`                         | Grants permission to delete an anomaly subscription                                                                                                      | Write        |
| `ce:DeleteNotificationSubscription`                    | Grants permission to delete reservation expiration alerts                                                                                                | Write        |
| `ce:DeleteReport`                                      | Grants permission to delete Cost Explorer reports                                                                                                        | Write        |
| `ce:ProvideAnomalyFeedback`                            | Grants permission to provide feedback on detected anomalies                                                                                              | Write        |
| `ce:StartSavingsPlansPurchaseRecommendationGeneration` | Grants permission to request a Savings Plans recommendation generation                                                                                   | Write        |
| `ce:UpdateAnomalyMonitor`                              | Grants permission to update an existing anomaly monitor                                                                                                  | Write        |
| `ce:UpdateAnomalySubscription`                         | Grants permission to update an existing anomaly subscription                                                                                             | Write        |
| `ce:UpdateCostAllocationTagsStatus`                    | Grants permission to update existing cost allocation tags status                                                                                         | Write        |
| `ce:UpdateNotificationSubscription`                    | Grants permission to update reservation expiration alerts                                                                                                | Write        |
| `ce:UpdatePreferences`                                 | Grants permission to edit the Cost Explorer preferences page                                                                                             | Write        |
| `cur:PutClassicReportPreferences`                      | Grants permission to enable classic reports                                                                                                              | Write        |
| `freetier:PutFreeTierAlertPreference`                  | Grants permission to set AWS Free Tier alert preference (by email address)                                                                               | Write        |
| `invoicing:PutInvoiceEmailDeliveryPreferences`         | Grants permission to update invoice email delivery preferences                                                                                           | Write        |
| `payments:CreatePaymentInstrument`                     | Grants permission to create a payment instrument                                                                                                         | Write        |
| `payments:DeletePaymentInstrument`                     | Grants permission to delete a payment instrument                                                                                                         | Write        |
| `payments:MakePayment`                                 | Grants permission to make a payment, authenticate a payment, verify a payment<br>method, and generate a funding request document for Advance Pay         | Write        |
| `payments:UpdatePaymentPreferences`                    | Grants permission to update payment preferences (for example, preferred payment<br>currency, preferred payment method)                                   | Write        |
| `tax:BatchPutTaxRegistration`                          | Grants permission to batch update tax registrations                                                                                                      | Write        |
| `tax:DeleteTaxRegistration`                            | Grants permission to delete tax registration data                                                                                                        | Write        |
| `tax:PutTaxInheritance`                                | Grants permission to set tax inheritance                                                                                                                 | Write        |

## Mapping for

aws-portal:ModifyPaymentMethods

| New action                          | Description                                                                                                                                      | Access level |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `account:GetAccountInformation`     | Grants permission to retrieve the account information for an account                                                                             | Read         |
| `payments:DeletePaymentInstrument`  | Grants permission to delete a payment instrument                                                                                                 | Write        |
| `payments:CreatePaymentInstrument`  | Grants permission to create a payment instrument                                                                                                 | Write        |
| `payments:MakePayment`              | Grants permission to make a payment, authenticate a payment, verify a payment<br>method, and generate a funding request document for Advance Pay | Write        |
| `payments:UpdatePaymentPreferences` | Grants permission to update payment preferences (for example, preferred payment<br>currency, preferred payment method)                           | Write        |

## Mapping for

purchase-orders:ViewPurchaseOrders

| New action                                  | Description                                                                                                         | Access level |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| `invoicing:GetInvoicePDF`                   | Grants permission to get invoice PDF                                                                                | Get          |
| `payments:ListPaymentPreferences`           | Grants permission to get payment preferences (for example, preferred payment<br>currency, preferred payment method) | List         |
| `purchase-orders:GetPurchaseOrder`          | Grants permission to get a purchase order                                                                           | Read         |
| `purchase-orders:ListPurchaseOrderInvoices` | Grants permission to view purchase orders and details                                                               | List         |
| `purchase-orders:ListPurchaseOrders`        | Grants permission to get all available purchase orders                                                              | List         |

## Mapping for

purchase-orders:ModifyPurchaseOrders

| New action                                  | Description                                            | Access level |
| ------------------------------------------- | ------------------------------------------------------ | ------------ |
| `purchase-orders:AddPurchaseOrder`          | Grants permission to add a purchase order              | Write        |
| `purchase-orders:DeletePurchaseOrder`       | Grants permission to delete a purchase order.          | Write        |
| `purchase-orders:UpdatePurchaseOrder`       | Grants permission to update an existing purchase order | Write        |
| `purchase-orders:UpdatePurchaseOrderStatus` | Grants permission to set purchase order status         | Write        |
