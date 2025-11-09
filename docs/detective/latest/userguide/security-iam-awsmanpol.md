# AWS managed policies for Amazon Detective

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy:

AmazonDetectiveFullAccess

You can attach the `AmazonDetectiveFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow a principal full access to all
Amazon Detective actions. You can attach this policy to a principal before they enable Detective for
their account. It must also be attached to the role that is used to run the Detective Python
scripts to create and manage a behavior graph.

Principals with these permissions can manage member accounts, add tags to their behavior
graph, and use Detective for investigation. They can also archive GuardDuty findings. The policy
provides permissions that the Detective console needs to display account names for accounts
that are in AWS Organizations.

**Permissions details**

This policy includes the following permissions:

- `detective` – Allows principals full access to all Detective
  actions.
- `organizations` – Allows principals to retrieve from AWS Organizations
  information about the accounts in an organization. If an account belongs to an
  organization, these permissions allow the Detective console to display account names in
  addition to account numbers.
- `guardduty` – Allows principals to get and archive GuardDuty
  findings from within Detective.
- `securityhub` – Allows principals to get Security Hub findings from
  within Detective.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "detective:*",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "guardduty:ArchiveFindings"
 ],
 "Resource": "arn:aws:guardduty:*:*:detector/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "guardduty:GetFindings",
 "guardduty:ListDetectors"

 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "securityHub:GetFindings"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AmazonDetectiveMemberAccess

You can attach the `AmazonDetectiveMemberAccess` policy to your IAM
entities.

This policy provides member access to Amazon Detective and scoped access to the console.

With this policy, you can:

- View invitations to Detective graph membership and accept or reject those
  invitations.
- View how your activity in Detective contributes to the cost of using this service on
  the **Usage** page.
- Resign from your membership in a graph.

This policy grants read-only permissions that allow scoped access to the Detective 
console.

**Permissions details**

This policy includes the following permissions:

- `detective` – Allows member access to Detective.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "detective:AcceptInvitation",
 "detective:BatchGetMembershipDatasources",
 "detective:DisassociateMembership",
 "detective:GetFreeTrialEligibility",
 "detective:GetPricingInformation",
 "detective:GetUsageInformation",
 "detective:ListInvitations",
 "detective:RejectInvitation"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AmazonDetectiveInvestigatorAccess

You can attach the `AmazonDetectiveInvestigatorAccess` policy to your IAM
entities.

This policy provides investigator access to the Detective service and scoped access to the
Detective console UI dependencies. This policy grants permissions to enable Detective
investigations in Detective for IAM users and IAM roles. You can investigate to identify
indicators of compromise such as findings using an investigation report, which provides analysis and
insights about security indicators. The report is ranked by severity, which is determined
using Detective’s behavioral analysis and machine learning. You can use the report to prioritize remediation of
resources.

**Permissions details**

This policy includes the following permissions:

- `detective` – Allows principals investigator access to Detective
  actions, to enable Detective investigations, and to enable finding groups summary.
- `guardduty` – Allows principals to get and archive GuardDuty
  findings from within Detective.
- `securityhub` – Allows principals to get Security Hub findings from within
  Detective.
- `organizations` – Allows principals to retrieve information
  about the accounts in an organization from AWS Organizations. If an account belongs to an
  organization, then these permissions allow the Detective console to display account names
  in addition to account numbers.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DetectivePermissions",
 "Effect": "Allow",
 "Action": [
 "detective:BatchGetGraphMemberDatasources",
 "detective:BatchGetMembershipDatasources",
 "detective:DescribeOrganizationConfiguration",
 "detective:GetFreeTrialEligibility",
 "detective:GetGraphIngestState",
 "detective:GetMembers",
 "detective:GetPricingInformation",
 "detective:GetUsageInformation",
 "detective:ListDatasourcePackages",
 "detective:ListGraphs",
 "detective:ListHighDegreeEntities",
 "detective:ListInvitations",
 "detective:ListMembers",
 "detective:ListOrganizationAdminAccount",
 "detective:ListTagsForResource",
 "detective:SearchGraph",
 "detective:StartInvestigation",
 "detective:GetInvestigation",
 "detective:ListInvestigations",
 "detective:UpdateInvestigationState",
 "detective:ListIndicators",
 "detective:InvokeAssistant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrganizationsPermissions",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GuardDutyPermissions",
 "Effect": "Allow",
 "Action": [
 "guardduty:ArchiveFindings",
 "guardduty:GetFindings",
 "guardduty:ListDetectors"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SecurityHubPermissions",
 "Effect": "Allow",
 "Action": [
 "securityHub:GetFindings"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AmazonDetectiveOrganizationsAccess

You can attach the `AmazonDetectiveOrganizationsAccess` policy to your IAM
entities.

This policy grants permission to enable and manage Amazon Detective within an organization. You
can enable Detective across the organization and determine the delegated administrator account
for Detective.

**Permissions details**

This policy includes the following permissions:

- `detective` – Allows principals access to Detective actions.
- `iam` – Specifies that a service linked role is created when
  Detective calls `EnableOrganizationAdminAccount`.
- `organizations` – Allows principals to retrieve information
  about the accounts in an organization from AWS Organizations. If an account belongs to an
  organization, then these permissions allow the Detective console to display account names
  in addition to account numbers. Enables the integration of an AWS service, allows
  register and deregister of the specified member account as a Delegated administrator,
  and allows principals to retrieve Delegated administrator accounts in other security
  services like Amazon Detective, Amazon GuardDuty, Amazon Macie, and AWS Security Hub.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "detective:DisableOrganizationAdminAccount",
 "detective:EnableOrganizationAdminAccount",
 "detective:ListOrganizationAdminAccount"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "detective.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:RegisterDelegatedAdministrator",
 "organizations:DeregisterDelegatedAdministrator"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "detective.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "detective.amazonaws.com",
 "guardduty.amazonaws.com",
 "macie.amazonaws.com",
 "securityhub.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AmazonDetectiveServiceLinkedRole

You can't attach the `AmazonDetectiveServiceLinkedRole` policy to your IAM
entities. This policy is attached to a service-linked role that allows Detective to perform
actions on your behalf. For more information, see [Using service-linked roles for
Detective](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allow the service-linked role to
retrieve account information for an organization.

**Permissions details**

This policy includes the following permissions:

- `organizations` – Retrieves account information for an
  organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:ListAccounts"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Detective updates to AWS managed

policies

View details about updates to AWS managed policies for Detective since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the [Document history page](doc-history.md "doc-history.md").

| Change                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                     | Date              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonDetectiveInvestigatorAccess](#security-iam-awsmanpol-amazondetectiveinvestigatoraccesspolicy "#security-iam-awsmanpol-amazondetectiveinvestigatoraccesspolicy") – Updates to existing policies                                                                                                                                          | Added Detective investigations and finding groups summary<br>actions to the `AmazonDetectiveInvestigatorAccess` policy.<br>These actions allow starting, retrieving, and updating Detective investigations; and<br>obtaining a summary of finding groups from within Detective. | November 26, 2023 |
| [AmazonDetectiveFullAccess](#security-iam-awsmanpol-amazondetectivefullaccess "#security-iam-awsmanpol-amazondetectivefullaccess") and [AmazonDetectiveInvestigatorAccess](#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy "#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy") – Updates to existing policies | Detective added Security Hub `GetFindings` actions to the<br>`AmazonDetectiveFullAccess` and `AmazonDetectiveInvestigatorAccess` policies.<br>These actions allow getting Security Hub findings from within Detective.                                                          | May 16, 2023      |
| [AmazonDetectiveOrganizationsAccess](#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy "#security-iam-awsmanpol-amazondetectiveorganizationsaccesspolicy") – New<br>policy                                                                                                                                                      | Detective added `AmazonDetectiveOrganizationsAccess` policy.<br>This policy grants permission to enable and manage Detective within an<br>organization                                                                                                                          | March 02, 2023    |
| [AmazonDetectiveMemberAccess](#security-iam-awsmanpol-amazondetectivememberaccess "#security-iam-awsmanpol-amazondetectivememberaccess") – New<br>policy                                                                                                                                                                                       | Detective added the `AmazonDetectiveMemberAccess` policy.<br>This policy provides member access to Detective and scoped access to the<br>console UI dependencies.                                                                                                               | January 17, 2023  |
| [AmazonDetectiveFullAccess](#security-iam-awsmanpol-amazondetectivefullaccess "#security-iam-awsmanpol-amazondetectivefullaccess") – Updates to<br>an existing policy                                                                                                                                                                          | Detective added GuardDuty `GetFindings` actions to the<br>`AmazonDetectiveFullAccess` policy.<br>These actions allow getting GuardDuty findings from within Detective.                                                                                                          | January 17, 2023  |
| [AmazonDetectiveInvestigatorAccess](#security-iam-awsmanpol-amazondetectiveinvestigatoraccesspolicy "#security-iam-awsmanpol-amazondetectiveinvestigatoraccesspolicy") – New<br>policy                                                                                                                                                         | Detective added the `AmazonDetectiveInvestigatorAccess` policy.<br>This policy allows the principal to conduct investigations in<br>Detective.                                                                                                                                  | January 17, 2023  |
| [AmazonDetectiveServiceLinkedRole](#security-iam-awsmanpol-amazondetectiveservicelinkedrolepolicy "#security-iam-awsmanpol-amazondetectiveservicelinkedrolepolicy") – New<br>policy                                                                                                                                                            | Detective added a new policy for its service-linked role.<br>The policy allows the service-linked role to retrieve information about<br>the accounts in an organization.                                                                                                        | December 16, 2021 |
| Detective started to track changes                                                                                                                                                                                                                                                                                                             | Detective started to track changes for its AWS managed policies.                                                                                                                                                                                                                | May 10, 2021      |
