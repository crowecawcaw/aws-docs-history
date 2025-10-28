# Refine permissions in AWS using last

accessed information

As an administrator, you might grant permissions to IAM resources (roles, users, user
groups, or policies) beyond what they require. IAM provides last accessed information to
help you identify unused permissions so that you can remove them. You can use last accessed
information to refine your policies and allow access to only the services and actions that
your IAM identities and policies use. This helps you to better adhere to the [best practice of least
privilege.](best-practices.md#grant-least-privilege "best-practices.md#grant-least-privilege") You can view last accessed information for identities or policies that
exist in IAM or AWS Organizations.

You can continuously monitor last accessed information with unused access analyzers. For
more information, see [Findings for external and unused
access](access-analyzer-findings.md "access-analyzer-findings.md").

###### Topics

- [Last accessed information types
  for IAM](#access_policies_last-accessed-data-types "#access_policies_last-accessed-data-types")
- [Last accessed information for
  AWS Organizations](#access_policies_last-accessed-orgs "#access_policies_last-accessed-orgs")
- [Things to know about last accessed
  information](#access_policies_last-accessed-know "#access_policies_last-accessed-know")
- [Permissions required](#access_policies_last-accessed-permissions "#access_policies_last-accessed-permissions")
- [Troubleshoot activity for
  IAM and AWS Organizations entities](#access_policies_last-accessed-troubleshooting "#access_policies_last-accessed-troubleshooting")
- [Where AWS tracks last accessed
  information](#last-accessed_tracking-period "#last-accessed_tracking-period")
- [View last accessed information for
  IAM](access_policies_last-accessed-view-data.md "access_policies_last-accessed-view-data.md")
- [View last accessed information
  for AWS Organizations](access_policies_last-accessed-view-data-orgs.md "access_policies_last-accessed-view-data-orgs.md")
- [Example scenarios for using
  last accessed information](access_policies_last-accessed-example-scenarios.md "access_policies_last-accessed-example-scenarios.md")
- [IAM action last
  accessed information services and actions](access_policies_last-accessed-action-last-accessed.md "access_policies_last-accessed-action-last-accessed.md")

## Last accessed information types

for IAM

You can view two types of last accessed information for IAM identities: allowed AWS
service information and allowed action information. The information includes the date and
time when the attempt to access an AWS API was made. For actions, last accessed
information reports service management actions. Management actions include creation,
deletion, and modification actions. To learn more about how to view last accessed
information for IAM, see [View last accessed information for
IAM](access_policies_last-accessed-view-data.md "access_policies_last-accessed-view-data.md").

For example scenarios for using last accessed information to make decisions about the
permissions that you grant to your IAM identities, see [Example scenarios for using
last accessed information](access_policies_last-accessed-example-scenarios.md "access_policies_last-accessed-example-scenarios.md").

To learn more about how the information for management actions is provided, see [Things to know about last accessed
information](#access_policies_last-accessed-know "#access_policies_last-accessed-know").

## Last accessed information for

AWS Organizations

If you sign in using management account credentials, you can view service last accessed
information for an AWS Organizations entity or policy in your organization. AWS Organizations entities
include the organization root, organizational units (OUs), or accounts. Last accessed
information for AWS Organizations includes information about services that are allowed by a service
control policy (SCP). The information indicates which principals (root user, IAM user, or
role) in an organization or account last attempted to access the service and when. To learn
more about the report and how to view last accessed information for AWS Organizations, see [View last accessed information
for AWS Organizations](access_policies_last-accessed-view-data-orgs.md "access_policies_last-accessed-view-data-orgs.md").

For example scenarios for using last accessed information to make decisions about the
permissions that you grant to your AWS Organizations entities, see [Example scenarios for using
last accessed information](access_policies_last-accessed-example-scenarios.md "access_policies_last-accessed-example-scenarios.md").

## Things to know about last accessed

information

Before you use last accessed information from a report to change the permissions for an
IAM identity or AWS Organizations entity, review the following details about the information.

- **Tracking period** – Recent activity appears in the IAM console
  within four hours. The tracking period for service information is at least 400 days
  depending on when the service started tracking actions information. The tracking
  period for Amazon S3 actions information began on April, 12, 2020. The tracking period for
  Amazon EC2, IAM, and Lambda actions began on April 7, 2021. The tracking period for all
  other services began on May 23, 2023. For a list of services for which action last
  accessed information is available, see [IAM action last
  accessed information services and actions](access_policies_last-accessed-action-last-accessed.md "access_policies_last-accessed-action-last-accessed.md"). For more
  information on which Regions action last accessed information is available in, see
  [Where AWS tracks last accessed
  information](#last-accessed_tracking-period "#last-accessed_tracking-period").
- **Attempts reported** – The service last
  accessed data includes all attempts to access an AWS API, not just the successful
  attempts. This includes all attempts that were made using the AWS Management Console, the AWS
  API through any of the SDKs, or any of the command line tools. An unexpected entry in
  the service last accessed data does not mean that your account has been compromised,
  because the request might have been denied. Refer to your CloudTrail logs as the
  authoritative source for information about all API calls and whether they were
  successful or denied access.
- **PassRole** – The `iam:PassRole`
  action is not tracked and is not included in IAM action last accessed
  information.
- **Action last accessed information** – Action
  last accessed information is available for service management actions accessed by
  IAM identities. See the [list of services and their actions](access_policies_last-accessed-action-last-accessed.md#access_policies_last-accessed-action-last-accessed-supported-actions "access_policies_last-accessed-action-last-accessed.md#access_policies_last-accessed-action-last-accessed-supported-actions") for which action last accessed reports
  information.

###### Note

Action last accessed information is not available for any data plane
event.

- **Management events** – IAM provides action
  information for service management events that are logged by CloudTrail. Sometimes, CloudTrail
  management events are also called control plane operations or control plane events.
  Management events provide visibility into administrative operations that are
  performed on resources in your AWS account. To learn more about management events
  in CloudTrail, see [Logging management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md") in the
  _AWS CloudTrail User Guide_.
- **Report owner** – Only the principal that
  generates a report can view the report details. This means that when you view the
  information in the AWS Management Console, you might have to wait for it to generate and load. If
  you use the AWS CLI or AWS API to get report details, your credentials must match the
  credentials of the principal that generated the report. If you use temporary
  credentials for a role or AWS STS federated user principal, you must generate and retrieve the report
  during the same session. For more information about assumed-role session principals,
  see [AWS JSON policy elements:
  Principal](reference_policies_elements_principal.md "reference_policies_elements_principal.md").
- **IAM resources** – The last accessed
  information for IAM includes IAM resources (roles, users, IAM groups, and
  policies) in your account. Last accessed information for AWS Organizations includes principals
  (IAM users, IAM roles, or the AWS account root user) in the specified AWS Organizations entity. The last
  accessed information does not include unauthenticated attempts.
- **IAM policy types** – The last accessed
  information for IAM includes services that are allowed by an IAM identity's
  policies. These are policies attached to a role or attached to a user directly or
  through a group. Access allowed by other policy types is not included in your report.
  The excluded policy types include resource-based policies, access control lists,
  AWS Organizations SCPs, IAM permissions boundaries, and session policies. Permissions that
  are provided by service-linked roles are defined by the service that they are linked
  to and can't be modified in IAM. To learn more about service-linked roles, see
  [Create a service-linked role](id_roles_create-service-linked-role.md "id_roles_create-service-linked-role.md") To learn how the different
  policy types are evaluated to allow or deny access, see [Policy evaluation logic](reference_policies_evaluation-logic.md "reference_policies_evaluation-logic.md").
- **AWS Organizations policy types** – The information for
  AWS Organizations includes only services that are allowed by an AWS Organizations entity's inherited
  service control policies (SCPs). SCPs are policies attached to a root, OU, or
  account. Access allowed by other policy types is not included in your report. The
  excluded policy types include identity-based policies, resource-based policies,
  access control lists, IAM permissions boundaries, and session policies. To learn
  how the different policy types are evaluated to allow or deny access, see [Policy evaluation logic](reference_policies_evaluation-logic.md "reference_policies_evaluation-logic.md").
- **Specifying a policy ID** – When you use the
  AWS CLI or AWS API to generate a report for last accessed information in AWS Organizations, you
  can optionally specify a policy ID. The resulting report includes information for the
  services that are allowed by only that policy. The information includes the most
  recent account activity in the specified AWS Organizations entity or the entity's children. For
  more information, see [aws iam
  generate-organizations-access-report](../../../cli/latest/reference/iam/generate-organizations-access-report.md "../../../cli/latest/reference/iam/generate-organizations-access-report.md") or [GenerateOrganizationsAccessReport](../APIReference/API_GenerateOrganizationsAccessReport.md "../APIReference/API_GenerateOrganizationsAccessReport.md").
- **AWS Organizations management account** – You must sign in
  to your organization's management account to view service last accessed information.
  You can choose to view information for the management account using the IAM console,
  the AWS CLI, or the AWS API. The resulting report lists all AWS services, because
  the management account is not limited by SCPs. If you specify a policy ID in the CLI
  or API, the policy is ignored. For each service, the report includes information for
  only the management account. However, reports for other AWS Organizations entities do not return
  information for activity in the management account.
- **AWS Organizations settings** – An administrator must
  [enable
  SCPs in your organization root](../../../organizations/latest/userguide/orgs_manage_policies.md#enable_policies_on_root "../../../organizations/latest/userguide/orgs_manage_policies.md#enable_policies_on_root") before you can generate data for
  AWS Organizations.

## Permissions required

To view the last accessed information in the AWS Management Console, you must have a policy that
grants the necessary permissions.

### Permissions for IAM

information

To use the IAM console to view the last accessed information for an IAM user,
role, or policy, you must have a policy that includes the following actions:

- `iam:GenerateServiceLastAccessedDetails`
- `iam:Get*`
- `iam:List*`

These permissions allow a user to see the following:

- Which users, groups, or roles are attached to a [managed policy](../../../glossary/latest/reference/glos-chap.md#managed_policy "../../../glossary/latest/reference/glos-chap.md#managed_policy")
- Which services a user or role can access
- The last time they accessed the service
- The last time they attempted to use a specific Amazon EC2, IAM, Lambda, or Amazon S3
  action

To use the AWS CLI or AWS API to view last accessed information for IAM, you must
have permissions that match the operation you want to use:

- `iam:GenerateServiceLastAccessedDetails`
- `iam:GetServiceLastAccessedDetails`
- `iam:GetServiceLastAccessedDetailsWithEntities`
- `iam:ListPoliciesGrantingServiceAccess`

This example shows how you might create an identity-based policy that allows viewing IAM last accessed information. Additionally,
it allows read-only access to all of IAM. This policy defines permissions for programmatic and console access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "iam:GenerateServiceLastAccessedDetails",
 "iam:Get*",
 "iam:List*"
 ],
 "Resource": "*"
 }
}`

```

### Permissions for

AWS Organizations information

To use the IAM console to view a report for the root, OU, or account entities in
AWS Organizations, you must have a policy that includes the following actions:

- `iam:GenerateOrganizationsAccessReport`
- `iam:GetOrganizationsAccessReport`
- `organizations:DescribeAccount`
- `organizations:DescribeOrganization`
- `organizations:DescribeOrganizationalUnit`
- `organizations:DescribePolicy`
- `organizations:ListChildren`
- `organizations:ListParents`
- `organizations:ListPoliciesForTarget`
- `organizations:ListRoots`
- `organizations:ListTargetsForPolicy`

To use the AWS CLI or AWS API to view service last accessed information for AWS Organizations, you
must have a policy that includes the following actions:

- `iam:GenerateOrganizationsAccessReport`
- `iam:GetOrganizationsAccessReport`
- `organizations:DescribePolicy`
- `organizations:ListChildren`
- `organizations:ListParents`
- `organizations:ListPoliciesForTarget`
- `organizations:ListRoots`
- `organizations:ListTargetsForPolicy`

This example shows how you might create an identity-based policy that allows viewing service last accessed information for AWS Organizations.
Additionally, it allows read-only access to all of AWS Organizations. This policy defines permissions for programmatic and console access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "iam:GenerateOrganizationsAccessReport",
 "iam:GetOrganizationsAccessReport",
 "organizations:Describe*",
 "organizations:List*"
 ],
 "Resource": "*"
 }
}`

```

You can also use the [iam:OrganizationsPolicyId](reference_policies_iam-condition-keys.md#ck_OrganizationsPolicyId "reference_policies_iam-condition-keys.md#ck_OrganizationsPolicyId") condition key to allow generating a report only for
a specific AWS Organizations policy. For an example policy, see [IAM: View
service last accessed information for an AWS Organizations policy](reference_policies_examples_iam_service-accessed-data-orgs.md "reference_policies_examples_iam_service-accessed-data-orgs.md").

## Troubleshoot activity for

IAM and AWS Organizations entities

In some cases, your AWS Management Console last accessed information table might be empty. Or perhaps
your AWS CLI or AWS API request returns an empty set of information or a null field. In
these cases, review the following issues:

- For action last accessed information, an action that you are expecting to see
  might not be returned in the list. This can happen either because the IAM identity
  does not have permissions for the action, or AWS does not yet track the action for
  last accessed information.
- For an IAM user, make sure that the user has at least one inline or managed
  policy attached, either directly or through group memberships.
- For an IAM group, verify that the group has at least one inline or managed
  policy attached.
- For an IAM group, the report returns only the service last accessed information
  for members that used the group's policies to access a service. To learn whether a
  member used other policies, review the last accessed information for that
  user.
- For an IAM role, verify that the role has at least one inline or managed policy
  attached.
- For an IAM entity (user or role), review other policy types that might affect
  the permissions of that entity. These include resource-based policies, access control
  lists, AWS Organizations policies, IAM permissions boundaries, or session policies. For more
  information, see [Policy types](access_policies.md#access_policy-types "access_policies.md#access_policy-types") or [Policy evaluation
  for requests within a single account](reference_policies_evaluation-logic_policy-eval-basics.md "reference_policies_evaluation-logic_policy-eval-basics.md").
- For an IAM policy, make sure that the specified managed policy is attached to at
  least one user, group with members, or role.
- For an AWS Organizations entity (root, OU, or account), make sure that you are signed using
  AWS Organizations management account credentials.
- Verify that [SCPs are
  enabled in your organization root](../../../organizations/latest/userguide/orgs_manage_policies.md#enable_policies_on_root "../../../organizations/latest/userguide/orgs_manage_policies.md#enable_policies_on_root").
- Action last accessed information is only available for the actions listed in [IAM action last
  accessed information services and actions](access_policies_last-accessed-action-last-accessed.md "access_policies_last-accessed-action-last-accessed.md").

When you make changes, wait at least four hours for activity to appear in your IAM
console report. If you use the AWS CLI or AWS API, you must generate a new report to view
the updated information.

## Where AWS tracks last accessed

information

AWS collects last accessed information for the standard AWS Regions. When AWS adds
additional Regions, those Regions are added to the following table, including the date that
AWS started tracking information in each Region.

- **Service information** – The tracking period
  for services is at least 400 days, or less if your Region began tracking this feature
  within the last 400 days.
- **Actions information** – The tracking period
  for Amazon S3 management actions began on April, 12, 2020. The tracking period for Amazon EC2,
  IAM, and Lambda management actions began on April 7, 2021. The tracking period for
  management actions of all other services began on May 23, 2023. If a Region's
  tracking date is later than May 23, 2023, then action last accessed information from
  that Region will start at the later date.

| Region name               | Region         | Tracking start date |
| ------------------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)            | us-east-2      | October 27, 2017    |
| US East (N. Virginia)     | us-east-1      | October 1, 2015     |
| US West (N. California)   | us-west-1      | October 1, 2015     |
| US West (Oregon)          | us-west-2      | October 1, 2015     |
| Africa (Cape Town)        | af-south-1     | April 22, 2020      |
| Asia Pacific (Hong Kong)  | ap-east-1      | April 24, 2019      |
| Asia Pacific (Hyderabad)  | ap-south-2     | November 22, 2022   |
| Asia Pacific (Jakarta)    | ap-southeast-3 | December 13, 2021   |
| Asia Pacific (Melbourne)  | ap-southeast-4 | January 23, 2023    |
| Asia Pacific (Mumbai)     | ap-south-1     | June 27, 2016       |
| Asia Pacific (Osaka)      | ap-northeast-3 | February 11, 2018   |
| Asia Pacific (Seoul)      | ap-northeast-2 | January 6, 2016     |
| Asia Pacific (Singapore)  | ap-southeast-1 | October 1, 2015     |
| Asia Pacific (Sydney)     | ap-southeast-2 | October 1, 2015     |
| Asia Pacific (Tokyo)      | ap-northeast-1 | October 1, 2015     |
| Canada (Central)          | ca-central-1   | October 28, 2017    |
| Europe (Frankfurt)        | eu-central-1   | October 1, 2015     |
| Europe (Ireland)          | eu-west-1      | October 1, 2015     |
| Europe (London)           | eu-west-2      | October 28, 2017    |
| Europe (Milan)            | eu-south-1     | April 28, 2020      |
| Europe (Paris)            | eu-west-3      | December 18, 2017   |
| Europe (Spain)            | eu-south-2     | November 15, 2022   |
| Europe (Stockholm)        | eu-north-1     | December 12, 2018   |
| Europe (Zurich)           | eu-central-2   | November 8, 2022    |
| Israel (Tel Aviv)         | il-central-1   | August 1, 2023      |
| Middle East (Bahrain)     | me-south-1     | July 29, 2019       |
| Middle East (UAE)         | me-central-1   | August 30, 2022     |
| South America (São Paulo) | sa-east-1      | December 11, 2015   |
| AWS GovCloud (US-East)    | us-gov-east-1  | July 1, 2023        |
| AWS GovCloud (US-West)    | us-gov-west-1  | July 1, 2023        | If a Region is not listed in the previous table, then that Region does not yet provide last accessed information. An AWS Region is a collection of AWS resources in a geographic area. Regions are grouped into partitions. The standard Regions are the Regions that belong to the `aws` partition. For more information about the different partitions, see [Amazon Resource Names (ARNs) Format](../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax "../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax") in the AWS General Reference. For more information about Regions, see [About AWS Regions](../../../general/latest/gr/rande-manage.md#region-what-is "../../../general/latest/gr/rande-manage.md#region-what-is") also in the AWS General Reference. |
