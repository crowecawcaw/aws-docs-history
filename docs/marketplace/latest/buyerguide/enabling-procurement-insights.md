# Enabling the Procurement insights dashboard

The following sections explain how to meet the general prerequisites for enabling the **Procurement insights** dashboard, and how to activate it.

If you need assistance with any part of this section, contact your AWS administrator.

###### Topics

- [Dashboard prerequisites](#dashboard-prereqs "#dashboard-prereqs")
- [Activating the dashboard](#integrate-dashboard "#integrate-dashboard")
- [For administrators: example policy](#procurement-sec-policy "#procurement-sec-policy")

## Dashboard prerequisites

To set up and enable the **Procurement insights** dashboard, you must have the
following prerequisites:

- All features enabled for your organization. For more information, see
  [Enabling all features for an organization with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"),
  in the _AWS Organizations User Guide_.
- Create the service-linked role and enable **Trusted access** in AWS Marketplace settings.
- The following enablement permissions are required to enable the dashboards:
  - `iam:CreateServiceLinkedRole`
  - `organizations:DescribeOrganization`
  - `organizations:EnableAWSServiceAccess`
  - `organizations:ListAWSServiceAccessForOrganization`
  - `organizations:DeregisterDelegatedAdministrator`(Required to manage delegated admins)
  - `organizations:ListDelegatedAdministrators`(Required to manage delegated admins)
  - `organizations:RegisterDelegatedAdministrator`(Required to manage delegated admins)

- The following permissions are required to view and interact with the dashboards:
  - `aws-marketplace:GetBuyerDashboard`
  - `organizations:DescribeOrganization`

###### Note

If you need help getting these permissions, contact your AWS administrator.

## Activating the dashboard

To activate dashboards, you must sign in to the AWS organization's management account with all features enabled. Your IAM user or role must have the permissions specified in
[Dashboard prerequisites](enabling-procurement-insights.md#dashboard-prereqs "enabling-procurement-insights.md#dashboard-prereqs").

###### Important

You or your AWS administrator must have a full-featured organization, and you must belong to an AWS Organizations management account to complete the following steps. For more information, see
[Tutorial: Creating and configuring an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md")
and [Managing the management account with AWS Organizations](../../../organizations/latest/userguide/orgs-manage_accounts_management.md "../../../organizations/latest/userguide/orgs-manage_accounts_management.md"), both in the
_AWS Organizations User Guide_.

###### To activate the dashboard

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. In the navigation pane, choose **Settings**.
3. Under **AWS Marketplace procurement insights**, choose **Enable trusted access**.
4. Select both checkboxes, **Enable trusted access across your organization**, and **Create a service-linked role for your organization**.
5. Choose **Create integration**.

Once you create the integration, the system creates the following service-linked roles and AWS managed policies:

- [AWSServiceRoleForProcurementInsightsPolicy](buyer-service-linked-role-procurement.md "buyer-service-linked-role-procurement.md") (later in this guide)
- [AWS managed policy:
  AWSServiceRoleForProcurementInsightsPolicy](../../../aws-managed-policy/latest/reference/AWSServiceRoleForProcurementInsightsPolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForProcurementInsightsPolicy.md") (_AWS Managed Policy Reference_)

###### Important

If you use the AWS command line interface (CLI) to active the dashboard, you must create the
service-liked roles listed above before you enable trusted access. Otherwise, the activation
process fails.

## For administrators: example policy

This example policy contains the permissions described in [Dashboard prerequisites](#dashboard-prereqs "#dashboard-prereqs"), earlier in this section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "CreateServiceLinkedRoleForProcurementInsights",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/procurement-insights.marketplace.amazonaws.com/AWSServiceRoleForProcurementInsights*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "procurement-insights.marketplace.amazonaws.com"
 }
 }
 },
 {
 "Sid": "EnableAWSServiceAccessForProcurementInsights",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "organizations:ServicePrincipal": "procurement-insights.marketplace.amazonaws.com"
 }
 }
 },
 {
 "Sid": "ManageDelegatedAdministrators",
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators",
 "organizations:DeregisterDelegatedAdministrator",
 "organizations:RegisterDelegatedAdministrator"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "organizations:ServicePrincipal": "procurement-insights.marketplace.amazonaws.com"
 }
 }
 },
 {
 "Sid": "GetBuyerDashboardStatement",
 "Effect": "Allow",
 "Action": "aws-marketplace:GetBuyerDashboard",
 "Resource": "*"
 },
 {
 "Sid": "ViewOrganizationDetails",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about creating policies, see
[Policies and permissions in AWS Identity and Access Management](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md"),
in the _IAM User Guide_.
