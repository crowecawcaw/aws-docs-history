# AWS Billing Conductor identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
Billing Conductor resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Billing Conductor identity-based policy examples](#security_policy-examples "#security_policy-examples")
- [AWS managed policies for AWS Billing Conductor](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [AWS Billing Conductor
  resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md")
- [Troubleshooting AWS Billing Conductor identity
  and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Billing Conductor resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Billing Conductor identity-based policy examples

This topic contains example policies that you can attach to your IAM user or group to control access to your account's information and tools.

###### Topics

- [Granting full access to the Billing Conductor console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Granting full access
  to the Billing Conductor API](#security_iam_id-based-policy-examples-fullAPI "#security_iam_id-based-policy-examples-fullAPI")
- [Granting read-only
  access to the Billing Conductor console](#security_iam_id-based-policy-examples-readonly "#security_iam_id-based-policy-examples-readonly")
- [Granting
  Billing Conductor access through the Billing console](#security_iam_id-based-policy-examples-ABCthroughbilling "#security_iam_id-based-policy-examples-ABCthroughbilling")
- [Granting Billing Conductor
  access through AWS Cost and Usage Reports](#security_iam_id-based-policy-examples-ABCthroughCUR "#security_iam_id-based-policy-examples-ABCthroughCUR")
- [Granting Billing Conductor
  access to the import organizational unit feature](#security_iam_id-based-policy-examples-ABCaccessOU "#security_iam_id-based-policy-examples-ABCaccessOU")
- [Denying Billing and Cost Explorer access to
  services and features that don't support pro forma costs](#deny-access-proforma-costs "#deny-access-proforma-costs")
- [Creating a pro forma CUR by billing group](#allow-legacy-cur "#allow-legacy-cur")

### Granting full access to the Billing Conductor console

To access the Billing Conductor console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the Billing Conductor
resources in your AWS account. If you create an identity-based policy that is more
restrictive than the minimum required permissions, the console won't function as
intended for entities (IAM users or roles) with that policy.

To ensure that those entities can still use the Billing Conductor console, also
attach the following AWS managed policy to the entities. For more information, see
[Adding Permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_:

In addition to the `billingconductor:*` permissions, `pricing:DescribeServices` is required for pricing rule creation, and `organizations:ListAccounts` is required to list linked accounts that are linked to the payer account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "billingconductor:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccounts",
 "organizations:DescribeAccount"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "pricing:DescribeServices",
 "Resource": "*"
 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.

### Granting full access

to the Billing Conductor API

In this example, you grant an IAM entity full access to the Billing Conductor API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "billingconductor:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "organizations:ListAccounts",
 "Resource": "*"
 }
 ]
}`

```

### Granting read-only

access to the Billing Conductor console

In this example, you grant an IAM entity read-only access to the Billing Conductor console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "billingconductor:List*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "organizations:ListAccounts",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "pricing:DescribeServices",
 "Resource": "*"
 }
 ]
}`

```

### Granting

Billing Conductor access through the Billing console

In this example, IAM entities can toggle and view pro forma billing data through the bills
page in their Billing console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "billing:ListBillingViews",
 "aws-portal:ViewBilling"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Granting Billing Conductor

access through AWS Cost and Usage Reports

In this example, IAM entities can toggle and view pro forma billing data through the
Cost and Usage Reports page in their Billing console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "billing:ListBillingViews",
 "aws-portal:ViewBilling",
 "cur:DescribeReportDefinitions"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Granting Billing Conductor

access to the import organizational unit feature

In this example, IAM entities have read-only access to the specific AWS Organizations API operations
that are required to import your organizational unit (OU) accounts when you're
creating a billing group. The import OU feature is on the AWS Billing Conductor console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListRoots",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListChildren"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Denying Billing and Cost Explorer access to

services and features that don't support pro forma costs

In this example, IAM entities are denied access to services and features that
don't support pro forma costs. This policy includes a list of actions that are
possible within the management account and individual member accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Deny",
 "Action": [
 "aws-portal:ModifyAccount",
 "aws-portal:ModifyBilling",
 "aws-portal:ModifyPaymentMethods",
 "aws-portal:ViewPaymentMethods",
 "aws-portal:ViewAccount",
 "cur:GetClassic*",
 "cur:Validate*",
 "tax:List*",
 "tax:Get*",
 "tax:Put*",
 "tax:ListTaxRegistrations",
 "tax:BatchPut*",
 "tax:UpdateExemptions",
 "freetier:Get*",
 "payments:Get*",
 "payments:List*",
 "payments:Update*",
 "payments:GetPaymentInstrument",
 "payments:GetPaymentStatus",
 "purchase-orders:ListPurchaseOrders",
 "purchase-orders:ListPurchaseOrderInvoices",
 "consolidatedbilling:GetAccountBillingRole",
 "consolidatedbilling:Get*",
 "consolidatedbilling:List*",
 "invoicing:List*",
 "invoicing:Get*",
 "account:Get*",
 "account:List*",
 "account:CloseAccount",
 "account:DisableRegion",
 "account:EnableRegion",
 "account:GetContactInformation",
 "account:GetAccountInformation",
 "account:PutContactInformation",
 "billing:GetBillingPreferences",
 "billing:GetContractInformation",
 "billing:GetCredits",
 "billing:RedeemCredits",
 "billing:Update*",
 "ce:GetPreferences",
 "ce:UpdatePreferences",
 "ce:GetReservationCoverage",
 "ce:GetReservationPurchaseRecommendation",
 "ce:GetReservationUtilization",
 "ce:GetSavingsPlansCoverage",
 "ce:GetSavingsPlansPurchaseRecommendation",
 "ce:GetSavingsPlansUtilization",
 "ce:GetSavingsPlansUtilizationDetails",
 "ce:ListSavingsPlansPurchaseRecommendationGeneration",
 "ce:StartSavingsPlansPurchaseRecommendationGeneration",
 "ce:UpdateNotificationSubscription"
 ],
 "Resource": "*"
 }]
}`

```

For more information, see [AWS services that support pro forma
costs](service-integrations-support-proforma.md "service-integrations-support-proforma.md").

### Creating a pro forma CUR by billing group

Step 1: Allow IAM users to have full access to legacy CUR and billing group billing view.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "CurDataAccess",
        "Effect": "Allow",
        "Action": "cur:PutReportDefinition",
        "Resource": [
            "arn:*:cur:*:*:definition/*",
            "arn:aws:billing::*:billingview/*"
        ]
      }
    ]
}
```

Step 2: To assign IAM roles to have access to specific billing groups, add the billing view ARN the user can access.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CurDataAccess",
            "Effect": "Allow",
            "Action": "cur:PutReportDefinition",
            "Resource":[
                "arn:aws:cur:us-east-1:123456789012:definition/*",
                "arn:aws:billing::`AWS-account-ID`:billingview/billing-group-$`billinggroup-primary-account-ID`"
                ]
        }
    ]
}
```

For more information, see [Configuring Cost and Usage Reports by billing group](configuring-abc.md "configuring-abc.md").
