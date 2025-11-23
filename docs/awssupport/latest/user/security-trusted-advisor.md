# Manage access to AWS Trusted Advisor

You can access AWS Trusted Advisor from the AWS Management Console. All AWS accounts have access to a
select core [Trusted Advisor
checks](https://aws.amazon.com//premiumsupport/faqs/#TaFree "https://aws.amazon.com//premiumsupport/faqs/#TaFree"). If you have a Business, Enterprise On-Ramp, or Enterprise Support plan, you can access all checks. for more
information, see [AWS Trusted Advisor check reference](trusted-advisor-check-reference.md "trusted-advisor-check-reference.md").

You can use AWS Identity and Access Management (IAM) to control access to Trusted Advisor.

###### Topics

- [Permissions for the Trusted Advisor
  console](#using-the-trusted-advisor-console "#using-the-trusted-advisor-console")
- [Trusted Advisor actions](#trusted-advisor-operations "#trusted-advisor-operations")
- [IAM policy examples](#iam-policy-examples-trusted-advisor "#iam-policy-examples-trusted-advisor")
- [See also](#see-also-security-trusted-advisor "#see-also-security-trusted-advisor")

## Permissions for the Trusted Advisor

console

To access the Trusted Advisor console, a user must have a minimum set of permissions. These
permissions must allow the user to list and view details about the Trusted Advisor resources in
your AWS account.

You can use the following options to control access to Trusted Advisor:

- Use the tag filter feature of the Trusted Advisor console. The user or role must have
  permissions associated with the tags.

You can use AWS managed policies or custom policies to assign permissions by
tags. For more information, see [Controlling access to and for IAM users and roles using tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md").

- Create an IAM policy with the `trustedadvisor` namespace. You can
  use this policy to specify permissions for actions and resources.

When you create a policy, you can specify the namespace of the service to allow or
deny an action. The namespace for Trusted Advisor is `trustedadvisor`. However, you
can't use the `trustedadvisor` namespace to allow or deny Trusted Advisor API
operations in the Support API. You must use the `support` namespace for Support
instead.

###### Note

If you have permissions to the [AWS Support](../APIReference.md "../APIReference.md") API,
the Trusted Advisor widget in the AWS Management Console shows a summary view of your Trusted Advisor results.
To view your results in the Trusted Advisor console, you must have permission to the
`trustedadvisor` namespace.

## Trusted Advisor actions

You can perform the following Trusted Advisor actions in the console. You can also specify
these Trusted Advisor actions in an IAM policy to allow or deny specific actions.

| Action                              | Description                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------ |
| `DescribeAccount`                   | Grants permission to view the Support plan and various Trusted Advisor<br>preferences.     |
| `DescribeAccountAccess`             | Grants permission to view if the AWS account has enabled or<br>disabled Trusted Advisor.   |
| `DescribeCheckItems`                | Grants permission to view details for the check items.                                     |
| `DescribeCheckRefreshStatuses`      | Grants permission to view the refresh statuses for Trusted Advisor<br>checks.              |
| `DescribeCheckSummaries`            | Grants permission to view Trusted Advisor check summaries.                                 |
| `DescribeChecks`                    | Grants permission to view details for Trusted Advisor checks.                              |
| `DescribeNotificationPreferences`   | Grants permission to view the notification preferences for the<br>AWS account.             |
| `ExcludeCheckItems`                 | Grants permission to exclude recommendations for Trusted Advisor<br>checks.                |
| `IncludeCheckItems`                 | Grants permission to include recommendations for Trusted Advisor<br>checks.                |
| `RefreshCheck`                      | Grants permission to refresh a Trusted Advisor check.                                      |
| `SetAccountAccess`                  | Grants permission to enable or disable Trusted Advisor for the<br>account.                 |
| `UpdateNotificationPreferences`     | Grants permission to update notification preferences for<br>Trusted Advisor.               |
| `DescribeCheckStatusHistoryChanges` | Grants permission to view the results and changed statuses for checks in the last 30 days. |

### Trusted Advisor actions for

organizational view

The following Trusted Advisor actions are for the organizational view feature. For more
information, see [Organizational view for AWS Trusted Advisor](organizational-view.md "organizational-view.md").

| Action                             | Description                                                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DescribeOrganization`             | Grants permission to view if the AWS account meets the<br>requirements to enable the organizational view feature.                                                     |
| `DescribeOrganizationAccounts`     | Grants permission to view the linked AWS accounts that are<br>in the organization.                                                                                    |
| `DescribeReports`                  | Grants permission to view details for organizational view<br>reports, such as the report name, runtime, date created, status,<br>and format.                          |
| `DescribeServiceMetadata`          | Grants permission to view information about organizational<br>view reports, such as the AWS Regions, check categories, check<br>names, and resource statuses.         |
| `GenerateReport`                   | Grants permission to create a report for Trusted Advisor checks in<br>your organization.                                                                              |
| `ListAccountsForParent`            | Grants permission to view, in the Trusted Advisor console, all of the<br>accounts in an AWS organization that are contained by a root<br>or organizational unit (OU). |
| `ListOrganizationalUnitsForParent` | Grants permission to view, in the Trusted Advisor console, all of the<br>organizational units (OUs) in a parent organizational unit or<br>root.                       |
| `ListRoots`                        | Grants permission to view, in the Trusted Advisor console, all of the<br>roots that are defined in an AWS organization.                                               |
| `SetOrganizationAccess`            | Grants permission to enable the organizational view feature<br>for Trusted Advisor.                                                                                   |

### Trusted Advisor Priority actions

If
you have Trusted Advisor Priority enabled for your account, you can perform the following
Trusted Advisor actions in the console. You can also add these Trusted Advisor
actions in an IAM policy to allow or deny specific actions. For more information,
see [Example IAM policies for
Trusted Advisor Priority](#trusted-advisor-priority-policies "#trusted-advisor-priority-policies").

###### Note

The risks that appear in Trusted Advisor Priority are recommendations that your technical
account manager (TAM) has identified for your account. Recommendations from a
service, such as a Trusted Advisor check, are created for you automatically.
Recommendations from your TAM are created for you manually. Next, your TAM sends
these recommendations so that they appear in Trusted Advisor Priority for your
account.

For more information, see [Get started with AWS Trusted Advisor Priority](trusted-advisor-priority.md "trusted-advisor-priority.md").

| Action                                             | Description                                                                                                                                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DescribeRisks`                                    | Grants permission to view risks in Trusted Advisor Priority.                                                                                                                 |
| `DescribeRisk`                                     | Grants permission to view risk details in Trusted Advisor Priority.                                                                                                          |
| `DescribeRiskResources`                            | Grants permission to view affected resources for a risk in<br>Trusted Advisor Priority.                                                                                      |
| `DownloadRisk`                                     | Grants permission to download a file that contains details<br>about the risk in Trusted Advisor Priority.                                                                    |
| `UpdateRiskStatus`                                 | Grants permission to update the risk status in<br>Trusted Advisor Priority.                                                                                                  |
| `DescribeNotificationConfigurations`               | Grants permission to get your email notification preferences<br>for Trusted Advisor Priority.                                                                                |
| `UpdateNotificationConfigurations`                 | Grants permission to create or update your email notification preferences for<br>Trusted Advisor Priority.                                                                   |
| `DeleteNotificationConfigurationForDelegatedAdmin` | Grants permission to the organization management account to<br>delete email notification preferences from a delegated<br>administrator account for Trusted Advisor Priority. |

## IAM policy examples

The following policies show you how to allow and deny access to Trusted Advisor. You can use
one of the following policies to create a _customer managed policy_
in the IAM console. For example, you can copy an example policy, and then paste it
into the [JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") of the IAM console. Then, you attach the
policy to your IAM user, group, or role.

For more information about how to create an IAM policy, see [Creating IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

###### Examples

- [Full access to Trusted Advisor](#full-access-trusted-advisor "#full-access-trusted-advisor")
- [Read-only access to
  Trusted Advisor](#read-only-access-trusted-advisor "#read-only-access-trusted-advisor")
- [Deny access to Trusted Advisor](#no-access-trusted-advisor "#no-access-trusted-advisor")
- [Allow and deny specific
  actions](#allow-specific-actions-trusted-advisor "#allow-specific-actions-trusted-advisor")
- [Control access to
  the Support API operations for Trusted Advisor](#control-access-to-trusted-advisor-deny-support "#control-access-to-trusted-advisor-deny-support")
- [Example IAM policies for
  Trusted Advisor Priority](#trusted-advisor-priority-policies "#trusted-advisor-priority-policies")
- [Example IAM policies for
  Trusted Advisor Engage](#trusted-advisor-engage-policies "#trusted-advisor-engage-policies")

### Full access to Trusted Advisor

The following policy allows users to view and take all actions on all Trusted Advisor
checks in the Trusted Advisor console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "trustedadvisor:*",
 "Resource": "*"
 }
 ]
}`

```

### Read-only access to

Trusted Advisor

The following policy allows users read-only access to the Trusted Advisor console. Users
can't make changes, such as refresh checks or change notification
preferences.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:Describe*",
 "trustedadvisor:Get*",
 "trustedadvisor:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Deny access to Trusted Advisor

The following policy doesn't allow users to view or take actions for Trusted Advisor
checks in the Trusted Advisor console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "trustedadvisor:*",
 "Resource": "*"
 }
 ]
}`

```

### Allow and deny specific

actions

The following policy allows users to view all Trusted Advisor checks in the Trusted Advisor
console, but doesn't allow them to refresh any checks.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "trustedadvisor:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "trustedadvisor:RefreshCheck",
 "Resource": "*"
 }
 ]
}`

```

### Control access to

the Support API operations for Trusted Advisor

In the AWS Management Console, a separate `trustedadvisor` IAM namespace controls
access to Trusted Advisor. You can't use the `trustedadvisor` namespace to allow
or deny Trusted Advisor API operations in the Support API. Instead, you use the
`support` namespace. You must have permissions to the Support API to
call Trusted Advisor programmatically.

For example, if you want to call the [RefreshTrustedAdvisorCheck](../APIReference/API_RefreshTrustedAdvisorCheck.md "../APIReference/API_RefreshTrustedAdvisorCheck.md") operation, you must have
permissions to this action in the policy.

###### Example : Allow Trusted Advisor API operations only

The following policy allows users access to the Support API operations for
Trusted Advisor, but not the rest of the Support API operations. For example, users can
use the API to view and refresh checks. They can't create, view, update, or
resolve AWS Support cases.

You can use this policy to call the Trusted Advisor API operations programmatically,
but you can't use this policy to view or refresh checks in the Trusted Advisor
console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "support:DescribeTrustedAdvisorCheckRefreshStatuses",
 "support:DescribeTrustedAdvisorCheckResult",
 "support:DescribeTrustedAdvisorChecks",
 "support:DescribeTrustedAdvisorCheckSummaries",
 "support:RefreshTrustedAdvisorCheck",
 "trustedadvisor:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "support:AddAttachmentsToSet",
 "support:AddCommunicationToCase",
 "support:CreateCase",
 "support:DescribeAttachment",
 "support:DescribeCases",
 "support:DescribeCommunications",
 "support:DescribeServices",
 "support:DescribeSeverityLevels",
 "support:ResolveCase"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about how IAM works with Support and Trusted Advisor, see [Actions](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions").

### Example IAM policies for

Trusted Advisor Priority

You can use the following AWS managed policies to control access to
Trusted Advisor Priority. For more information, see [AWS managed policies for
AWS Trusted Advisor](aws-managed-policies-for-trusted-advisor.md "aws-managed-policies-for-trusted-advisor.md") and [Get started with AWS Trusted Advisor Priority](trusted-advisor-priority.md "trusted-advisor-priority.md").

### Example IAM policies for

Trusted Advisor Engage

###### Note

Trusted Advisor Engage is in preview release and does not currently have any AWS managed
policies. You can use one of the following policies to create a _customer
managed policy_ in the IAM console.

An example policy that grants read and write access in Trusted Advisor Engage:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:CreateEngagement*",
 "trustedadvisor:DescribeAccount*",
 "trustedadvisor:GetEngagement*",
 "trustedadvisor:ListEngagement*",
 "trustedadvisor:UpdateEngagement*"
 ],
 "Resource": "*"
 }
 ]
}`

```

An example policy that grants read-only access in Trusted Advisor Engage:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:DescribeAccount*",
 "trustedadvisor:GetEngagement*",
 "trustedadvisor:ListEngagement*"
 ],
 "Resource": "*"
 }
 ]
}`

```

An example policy that grants read and write access in Trusted Advisor Engage and the ability
to enable trusted access to Trusted Advisor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization",
 "trustedadvisor:CreateEngagement*",
 "trustedadvisor:DescribeAccount*",
 "trustedadvisor:DescribeOrganization",
 "trustedadvisor:GetEngagement*",
 "trustedadvisor:ListEngagement*",
 "trustedadvisor:SetOrganizationAccess",
 "trustedadvisor:UpdateEngagement*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "reporting.trustedadvisor.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/reporting.trustedadvisor.amazonaws.com/AWSServiceRoleForTrustedAdvisorReporting",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "reporting.trustedadvisor.amazonaws.com"
 }
 }
 }
 ]
}`

```

## See also

For more information about Trusted Advisor permissions, see the following resources:

- [Actions defined by AWS Trusted Advisor](../../../IAM/latest/UserGuide/list_awstrustedadvisor.md#awstrustedadvisor-actions-as-permissions "../../../IAM/latest/UserGuide/list_awstrustedadvisor.md#awstrustedadvisor-actions-as-permissions") in the
  _IAM User Guide_.
- [Controlling Access to the
  Trusted Advisor Console](https://aws.amazon.com/premiumsupport/ta-iam/ "https://aws.amazon.com/premiumsupport/ta-iam/")
