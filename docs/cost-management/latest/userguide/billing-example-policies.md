# AWS Cost Management policy examples

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

This topic contains example policies that you can attach to your IAM role or group to
control access to your account's billing information and tools. The following basic
rules apply to IAM policies for Billing and Cost Management:

- `Version` is always `2012-10-17`.
- `Effect` is always `Allow` or `Deny`.
- `Action` is the name of the action or a wildcard (`*`).

The action prefix is `budgets` for AWS Budgets, `cur` for AWS Cost and Usage Reports, `aws-portal` for AWS Billing, or `ce` for Cost Explorer.

- `Resource` is always `*` for AWS Billing.

For actions performed on a `budget` resource, specify the budget Amazon Resource Name (ARN).

- It's possible to have multiple statements in one policy.
  For a list of policy examples for the Billing console, see [Billing policy examples](../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md "../../../awsaccountbilling/latest/aboutv2/billing-example-policies.md") in the _Billing user guide_.

###### Note

These policies require that you activate user access to the Billing and Cost Management console on the [Account Settings](https://portal.aws.amazon.com/billing/home#/account "https://portal.aws.amazon.com/billing/home#/account") console
page. For more information, see [Activating access to the Billing and Cost Management
console](control-access-billing.md#ControllingAccessWebsite-Activate "control-access-billing.md#ControllingAccessWebsite-Activate").

###### Topics

- [Deny users access to the Billing and Cost Management console](#example-billing-deny-all "#example-billing-deny-all")
- [Deny AWS Console cost and usage widget access for member accounts](#example-billing-deny-widget "#example-billing-deny-widget")
- [Deny AWS Console cost and usage widget
  access for specific users and roles](#example-billing-deny-ce "#example-billing-deny-ce")
- [Allow full access to AWS services but deny users
  access to the Billing and Cost Management console](#ExampleAllowAllDenyBilling "#ExampleAllowAllDenyBilling")
- [Allow users to view the Billing and Cost Management console except for
  account settings](#example-billing-read-only "#example-billing-read-only")
- [Allow users to modify billing
  information](#example-billing-deny-modifybilling "#example-billing-deny-modifybilling")
- [Allow users to create budgets](#example-billing-allow-createbudgets "#example-billing-allow-createbudgets")
- [Deny access to account settings, but allow full access to all other billing and usage information](#example-billing-deny-modifyaccount "#example-billing-deny-modifyaccount")
- [Deposit reports into an Amazon S3 bucket](#example-billing-s3-bucket "#example-billing-s3-bucket")
- [View costs and usage](#example-policy-ce-api "#example-policy-ce-api")
- [Enable and disable AWS Regions](#enable-disable-regions "#enable-disable-regions")
- [View and update the Cost Explorer preferences page](#example-view-update-ce "#example-view-update-ce")
- [View, create, update, and delete using the Cost Explorer reports page](#example-view-ce-reports "#example-view-ce-reports")
- [View, create, update, and delete reservation and Savings Plans alerts](#example-view-ce-expiration "#example-view-ce-expiration")
- [Allow read-only access to AWS Cost Anomaly Detection](#example-policy-ce-ad "#example-policy-ce-ad")
- [Allow AWS Budgets to apply
  IAM policies and SCPs](#example-budgets-IAM-SCP "#example-budgets-IAM-SCP")
- [Allow AWS Budgets to apply
  IAM policies and SCPs and target EC2 and RDS instances](#example-budgets-applySCP "#example-budgets-applySCP")
- [Allow users to create, list, and
  add usage to workload estimates in Pricing Calculator](#example-pc-create-list-estimates "#example-pc-create-list-estimates")
- [Allow users to create, list, and
  add usage and commitments to bill scenarios in Pricing Calculator](#example-pc-create-list-scenario "#example-pc-create-list-scenario")
- [Allow users to create a bill
  estimate in Pricing Calculator](#example-pc-create-bill-estimate "#example-pc-create-bill-estimate")
- [Allow users to create preferences in
  Pricing Calculator](#example-pc-create-preferences "#example-pc-create-preferences")
- [Allow users to create, manage, and share
  custom billing views](#example-billing-view "#example-billing-view")
- [Allow users to access Cost Explorer
  when accessing a specific custom billing view](#example-custom-billing-view "#example-custom-billing-view")

## Deny users access to the Billing and Cost Management console

To explicitly deny a user access to the all Billing and Cost Management console pages, use a policy similar to
this example policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "aws-portal:*",
 "Resource": "*"
 }
 ]
}`

```

## Deny AWS Console cost and usage widget access for member accounts

To restrict member (linked) account access to cost and usage data, use your
management (payer) account to access the Cost Explorer preferences tab and uncheck
**Linked Account Access**. This will deny access to cost and
usage data from the Cost Explorer (AWS Cost Management) console, Cost Explorer API, and AWS
Console Home page's cost and usage widget regardless of the IAM actions a member
account’s user or role has.

## Deny AWS Console cost and usage widget

access for specific users and roles

To deny AWS Console cost and usage widget access for specific users and roles,
use the permissions policy below.

###### Note

Adding this policy to a user or role will deny users access to Cost Explorer (AWS Cost Management) console
and Cost Explorer APIs as well.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ce:*",
 "Resource": "*"
 }
 ]
}`

```

## Allow full access to AWS services but deny users

access to the Billing and Cost Management console

To deny users access to everything on the Billing and Cost Management console, use the following policy. In this
case, you should also deny user access to AWS Identity and Access Management (IAM) so that the users can't
access the policies that control access to billing information and tools.

###### Important

This policy doesn't allow any actions. Use this policy in combination with other policies that allow specific actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "aws-portal:*",
 "iam:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to view the Billing and Cost Management console except for

account settings

This policy allows read-only access to all of the Billing and Cost Management console, including the **Payments Method** and **Reports** console pages, but denies access to the **Account Settings** page, thus protecting the account password, contact information, and security questions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "aws-portal:View*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "aws-portal:*Account",
 "Resource": "*"
 }
 ]
}`

```

## Allow users to modify billing

information

To allow users to modify account billing information in the Billing and Cost Management console, you must also
allow users to view your billing information. The following policy example allows a
user to modify the **Consolidated Billing**,
**Preferences**, and **Credits** console
pages. It also allows a user to view the following Billing and Cost Management console pages:

- **Dashboard**
- **Cost Explorer**
- **Bills**
- **Orders and invoices**
- **Advance Payment**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "aws-portal:*Billing",
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create budgets

To allow users to create budgets in the Billing and Cost Management console, you must also allow users to view
your billing information, create CloudWatch alarms, and create Amazon SNS notifications. The
following policy example allows a user to modify the **Budget**
console page.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1435216493000",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling",
 "aws-portal:ModifyBilling",
 "budgets:ViewBudget",
 "budgets:ModifyBudget"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Stmt1435216514000",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "Stmt1435216552000",
 "Effect": "Allow",
 "Action": [
 "sns:*"
 ],
 "Resource": [
 "arn:aws:sns:us-east-1::"
 ]
 }
 ]
}`

```

## Deny access to account settings, but allow full access to all other billing and usage information

To protect your account password, contact information, and security questions, you can deny
user access to **Account Settings** while still enabling full
access to the rest of the functionality in the Billing and Cost Management console, as shown in the
following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-portal:*Billing",
 "aws-portal:*Usage",
 "aws-portal:*PaymentMethods"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "aws-portal:*Account",
 "Resource": "*"
 }
 ]
}`

```

## Deposit reports into an Amazon S3 bucket

The following policy allows Billing and Cost Management to save your detailed AWS bills to an Amazon S3 bucket, as
long as you own both the AWS account and the Amazon S3 bucket. Note that this policy
must be applied to the Amazon S3 bucket, instead of to a user. That is, it's a
resource-based policy, not a user-based policy. You should deny user access to the
bucket for users who don't need access to your bills.

Replace `bucketname` with the name of your bucket.

For more information, see [Using Bucket
Policies and User Policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md") in the _Amazon Simple Storage Service User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "billingreports.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketAcl",
 "s3:GetBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::`bucketname`"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "billingreports.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`bucketname`/*"
 }
 ]
}`

```

## View costs and usage

To allow users to use the AWS Cost Explorer API, use the following policy to grant them
access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ce:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Enable and disable AWS Regions

For an example IAM policy that allows users to enable and disable Regions, see [AWS: Allows Enabling and Disabling AWS Regions](../../../IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws-enable-disable-regions.md") in the _IAM User Guide_.

## View and update the Cost Explorer preferences page

This policy allows a user to view and update using the **Cost Explorer preferences
page**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling",
 "ce:UpdatePreferences"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but deny permission to view or edit the
**Preferences** page.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "ce:GetPreferences",
 "ce:UpdatePreferences"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but deny permission to edit the
**Preferences** page.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "ce:UpdatePreferences"
 ],
 "Resource": "*"
 }
 ]
}`

```

## View, create, update, and delete using the Cost Explorer reports page

This policy allows a user to view, create, update, and delete using the
**Cost Explorer reports page**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling",
 "ce:CreateReport",
 "ce:UpdateReport",
 "ce:DeleteReport"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but deny permission to view or edit the
**Reports** page.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "ce:DescribeReport",
 "ce:CreateReport",
 "ce:UpdateReport",
 "ce:DeleteReport"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but deny permission to edit the
**Reports** page.

## View, create, update, and delete reservation and Savings Plans alerts

This policy allows a user to view, create, update, and delete [reservation expiration alerts](../../../awsaccountbilling/latest/aboutv2/ce-ris.md "../../../awsaccountbilling/latest/aboutv2/ce-ris.md") and [Savings Plans
alerts](../../../savingsplans/latest/userguide/sp-overview.md#sp-alert "../../../savingsplans/latest/userguide/sp-overview.md#sp-alert"). To edit reservation expiration alerts or Savings Plans alerts, a user
needs all three granular actions: `ce:CreateNotificationSubscription`,
`ce:UpdateNotificationSubscription`, and
`ce:DeleteNotificationSubscription`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling",
 "ce:CreateNotificationSubscription",
 "ce:UpdateNotificationSubscription",
 "ce:DeleteNotificationSubscription"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but denies permission to view or
edit the **Reservation Expiration Alerts** and **Savings Plans
alert** pages.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "ce:DescribeNotificationSubscription",
 "ce:CreateNotificationSubscription",
 "ce:UpdateNotificationSubscription",
 "ce:DeleteNotificationSubscription"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy allows users to view Cost Explorer, but denies permission to edit the
**Reservation Expiration Alerts** and **Savings Plans
alert** pages.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "ce:CreateNotificationSubscription",
 "ce:UpdateNotificationSubscription",
 "ce:DeleteNotificationSubscription"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow read-only access to AWS Cost Anomaly Detection

To allow users read-only access to AWS Cost Anomaly Detection, use the following policy to grant
them access. `ce:ProvideAnomalyFeedback` is optional as a part of the
read-only access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ce:Get*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Allow AWS Budgets to apply

IAM policies and SCPs

This policy allows AWS Budgets to apply IAM policies and service control
policies (SCPs) on behalf of the user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachGroupPolicy",
 "iam:AttachRolePolicy",
 "iam:AttachUserPolicy",
 "iam:DetachGroupPolicy",
 "iam:DetachRolePolicy",
 "iam:DetachUserPolicy",
 "organizations:AttachPolicy",
 "organizations:DetachPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow AWS Budgets to apply

IAM policies and SCPs and target EC2 and RDS instances

This policy allows AWS Budgets to apply IAM policies and service control
policies (SCPs), and to target Amazon EC2 and Amazon RDS instances on behalf of the user.

Trust policy

###### Note

This trust policy allows AWS Budgets to assume a role that can call other services on your behalf. For more information on the best practices for cross-service permissions like this, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "budgets.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:budgets::123456789012:budget/*"
 },
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 }
 }
 }
]
}`

```

Permissions policy

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
 "iam:AttachGroupPolicy",
 "iam:AttachRolePolicy",
 "iam:AttachUserPolicy",
 "iam:DetachGroupPolicy",
 "iam:DetachRolePolicy",
 "iam:DetachUserPolicy",
 "organizations:AttachPolicy",
 "organizations:DetachPolicy",
 "rds:DescribeDBInstances",
 "rds:StartDBInstance",
 "rds:StopDBInstance",
 "ssm:StartAutomationExecution"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create, list, and

add usage to workload estimates in Pricing Calculator

This policy allows IAM users to create,
list, and add usage to workload estimates, along
with permissions to query Cost Explorer data to get historical cost and
usage data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "WorkloadEstimate",
 "Effect": "Allow",
 "Action": [
 "ce:GetCostCategories",
 "ce:GetDimensionValues",
 "ce:GetCostAndUsage",
 "ce:GetTags",
 "bcm-pricing-calculator:GetWorkloadEstimate",
 "bcm-pricing-calculator:ListWorkloadEstimateUsage",
 "bcm-pricing-calculator:CreateWorkloadEstimate",
 "bcm-pricing-calculator:ListWorkloadEstimates",
 "bcm-pricing-calculator:CreateWorkloadEstimateUsage",
 "bcm-pricing-calculator:UpdateWorkloadEstimateUsage"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create, list, and

add usage and commitments to bill scenarios in Pricing Calculator

This policy allows IAM users to create, list, and add usage and commitments to
bill scenarios. Cost Explorer permissions aren't added, so you won't be able to load
historical data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BillScenario",
 "Effect": "Allow",
 "Action": [
 "bcm-pricing-calculator:CreateBillScenario",
 "bcm-pricing-calculator:GetBillScenario",
 "bcm-pricing-calculator:ListBillScenarios",
 "bcm-pricing-calculator:CreateBillScenarioUsageModification",
 "bcm-pricing-calculator:UpdateBillScenarioUsageModification",
 "bcm-pricing-calculator:ListBillScenarioUsageModifications",

 "bcm-pricing-calculator:ListBillScenarioCommitmentModifications"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create a bill

estimate in Pricing Calculator

This policy allows IAM users to create bill estimate and list bill
estimate line items.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BillEstimate",
 "Effect": "Allow",
 "Action": [
 "bcm-pricing-calculator:CreateBillEstimate",
 "bcm-pricing-calculator:GetBillEstimate",
 "bcm-pricing-calculator:UpdateBillEstimate",
 "bcm-pricing-calculator:ListBillEstimates",
 "bcm-pricing-calculator:ListBillEstimateLineItems",
 "bcm-pricing-calculator:ListBillEstimateCommitments",
 "bcm-pricing-calculator:ListBillEstimateInputUsageModifications",
 "bcm-pricing-calculator:ListBillEstimateInputCommitmentModifications"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create preferences in

Pricing Calculator

This policy allows IAM users to create and get rate preferences.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RatePreferences",
 "Effect": "Allow",
 "Action": [
 "bcm-pricing-calculator:GetPreferences",
 "bcm-pricing-calculator:UpdatePreferences"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to create, manage, and share

custom billing views

This policy allows IAM users to create, manage, and share custom billing views.
They will need the ability to create and manage custom billing views using Billing
View, and the ability to create and associate resource shares using AWS Resource
Access Manager (AWS RAM).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "billing:CreateBillingView",
 "billing:UpdateBillingView",
 "billing:DeleteBillingView",
 "billing:GetBillingView",
 "billing:ListBillingViews",
 "billing:ListTagsForResource",
 "billing:PutResourcePolicy",
 "ce:GetCostAndUsage",
 "ce:GetTags",
 "organizations:ListAccounts",
 "ram:ListResources",
 "ram:ListPermissions",
 "ram:CreateResourceShare",
 "ram:AssociateResourceShare",
 "ram:GetResourceShares",
 "ram:GetResourceShareAssociations",
 "ram:ListResourceSharePermissions",
 "ram:ListResourceTypes",
 "ram:ListPrincipals",
 "ram:DisassociateResourceShare"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users to access Cost Explorer

when accessing a specific custom billing view

This policy allows IAM users to access Cost Explorer when accessing a specific
custom billing view (`custom-1a2b3c4d`). Replace
`123456789012` with the 12-digit AWS account ID and
`1a2b3c4d` with the unique identifier of the custom billing
view.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ce:GetDimensionValues",
 "ce:GetCostAndUsageWithResources",
 "ce:GetCostAndUsage",
 "ce:GetCostForecast",
 "ce:GetTags",
 "ce:GetUsageForecast",
 "ce:GetCostCategories"
 ],
 "Resource": [
 "arn:aws:billing::123456789012:billingview/custom-1a2b3c4d"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "billing:ListBillingViews",
 "billing:GetBillingView"
 ],
 "Resource": "*"
 }
 ]
}`

```
