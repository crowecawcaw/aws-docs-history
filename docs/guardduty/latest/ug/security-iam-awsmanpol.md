# AWS managed policies for Amazon GuardDuty

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

The `Version` policy element specifies the language syntax rules that are to be
used to process a policy. The following policies include the current version that IAM
supports. For more information, see [IAM JSON policy
elements: Version](../../../IAM/latest/UserGuide/reference_policies_elements_version.md "../../../IAM/latest/UserGuide/reference_policies_elements_version.md").

## AWS managed policy:

AmazonGuardDutyFullAccess_v2 (recommended)

You can attach the AmazonGuardDutyFullAccess_v2 policy to your IAM
identities. This policy will allow a user full access to perform all GuardDuty actions and access
required resources. Between AmazonGuardDutyFullAccess_v2 and AmazonGuardDutyFullAccess, GuardDuty recommends
attaching AmazonGuardDutyFullAccess_v2 because it offers enhanced security and restricts administrative actions
to GuardDuty service principals.

### Permission details

The AmazonGuardDutyFullAccess_v2 policy includes the following permissions:

- `GuardDuty` – Allows users full access to all GuardDuty
  actions.
- `IAM`:
  - Allows users to create GuardDuty service-linked role.
  - Allows viewing and managing IAM roles and their policies for GuardDuty.
  - Allows users to pass a role to GuardDuty that uses this role to enable the
    GuardDuty Malware Protection for S3 feature. This is regardless of how you enable Malware Protection for S3
  * within the GuardDuty service or independently.
  - The permission to perform an `iam:GetRole` action on
    `AWSServiceRoleForAmazonGuardDutyMalwareProtection` establishes if the
    service-linked role (SLR) for Malware Protection for EC2 exists in an account.

- `Organizations`:
  - Allow users to read (view) GuardDuty organization structure and accounts.
  - Allows users to designate a delegated administrator
    and manage members for a GuardDuty organization.

To review the permissions for this policy, see [AmazonGuardDutyFullAccess_v2](../../../aws-managed-policy/latest/reference/AmazonGuardDutyFullAccess_v2.md "../../../aws-managed-policy/latest/reference/AmazonGuardDutyFullAccess_v2.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

AmazonGuardDutyFullAccess

You can attach the `AmazonGuardDutyFullAccess` policy to your IAM
identities.

###### Important

For enhanced security and restrictive permissions to GuardDuty service principals,
we recommend you to use [AWS managed policy:
AmazonGuardDutyFullAccess_v2 (recommended)](#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2 "#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2").

This policy grants administrative permissions that allow a user full access to perform all
GuardDuty actions and resources.

### Permission details

This policy includes the following permissions.

- `GuardDuty` – Allows users full access to all GuardDuty
  actions.
- `IAM`:
  - Allows users to create the GuardDuty service-linked role.
  - Allows an administrator account to enable GuardDuty for member accounts.
  - Allows users to pass a role to GuardDuty that uses this role to enable the
    GuardDuty Malware Protection for S3 feature. This is regardless of how you enable Malware Protection for S3
  * within the GuardDuty service or independently.

- `Organizations` – Allows users to designate a delegated administrator
  and manage members for a GuardDuty organization.

The permission to perform an `iam:GetRole` action on
`AWSServiceRoleForAmazonGuardDutyMalwareProtection` establishes if the
service-linked role (SLR) for Malware Protection for EC2 exists in an account.

To review the permissions for this policy, see [AmazonGuardDutyFullAccess](../../../aws-managed-policy/latest/reference/AmazonGuardDutyFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonGuardDutyFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed

policy: AmazonGuardDutyReadOnlyAccess

You can attach the `AmazonGuardDutyReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only permissions that allow a user to view GuardDuty findings and
details of your GuardDuty organization.

**Permissions details**

This policy includes the following permissions.

- `GuardDuty` – Allows users to view GuardDuty findings and perform
  API operations that start with `Get`, `List`, or
  `Describe`.
- `Organizations` – Allows users to retrieve information about your
  GuardDuty organization configuration, including details of the delegated
  administrator account.

To review the permissions for this policy, see [AmazonGuardDutyReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonGuardDutyReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonGuardDutyReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed

policy: AmazonGuardDutyServiceRolePolicy

You can't attach `AmazonGuardDutyServiceRolePolicy` to your IAM entities.
This AWS managed policy is attached to a service-linked role that allows GuardDuty to
perform actions on your behalf. For more information, see [Service-linked role permissions for GuardDuty](slr-permissions.md "slr-permissions.md").

## GuardDuty updates to AWS managed

policies

View details about updates to AWS managed policies for GuardDuty since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the GuardDuty Document history page.

| Change                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonGuardDutyFullAccess_v2](#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2 "#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2") – Added a new policy                          | Added a new AmazonGuardDutyFullAccess_v2 policy. This is recommended because<br>its permissions enhance security by restricting administrative actions to GuardDuty<br>service principals based on IAM roles and policies, and AWS Organizations integration.                                                                                                                                                                                                                                                                                                                            | June 04, 2025     |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md") – Update to an<br>existing policy                                                                             | Added the `ec2:DescribeVpcs` permission. This allows<br>GuardDuty to track VPC updates, such as retrieving the VPC CIDR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | August 22, 2024   |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md") – Update to an<br>existing policy                                                                             | Added permission that allows you to pass an IAM role to GuardDuty<br>when you enable Malware Protection for S3.<br>`<br>{<br>"Sid": "AllowPassRoleToMalwareProtectionPlan",<br>"Effect": "Allow",<br>"Action": [<br>"iam:PassRole"<br>],<br>"Resource": "arn:aws:iam::*:role/*",<br>"Condition": {<br>"StringEquals": {<br>"iam:PassedToService": "guardduty.amazonaws.com"<br>}<br>}<br>}<br>`                                                                                                                                                                                          | June 10, 2024     |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md") – Update to an<br>existing policy.                                                                            | Use AWS Systems Manager actions to manage SSM associations on Amazon EC2<br>instances when you enable GuardDuty Runtime Monitoring with automated agent for<br>Amazon EC2. When GuardDuty automated agent configuration is disabled, GuardDuty<br>considers only those EC2 instances that have an inclusion tag<br>(`GuardDutyManaged`:`true`).                                                                                                                                                                                                                                          | March 26, 2024    |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md") – Update to an<br>existing policy.                                                                            | GuardDuty has added a new permission -<br>`organization:DescribeOrganization` to retrieve the<br>organization ID of the shared Amazon VPC account and set the Amazon VPC<br>endpoint policy with organization ID.                                                                                                                                                                                                                                                                                                                                                                        | February 9, 2024  |
| [AmazonGuardDutyMalwareProtectionServiceRolePolicy](slr-permissions-malware-protection.md "slr-permissions-malware-protection.md")<br>– Update to an existing policy.                     | Malware Protection for EC2 has added two permissions -<br>`GetSnapshotBlock` and<br>`ListSnapshotBlocks` to fetch the snapshot of an EBS<br>volume (encrypted using AWS managed key) from your AWS account<br>and copy it to the GuardDuty service account before starting the malware<br>scan.                                                                                                                                                                                                                                                                                          | Jan 25, 2024      |
| [AmazonGuardDutyServiceRolePolicy](#security-iam-awsmanpol-AmazonGuardDutyServiceRolePolicy "#security-iam-awsmanpol-AmazonGuardDutyServiceRolePolicy") – Update to an<br>existing policy | Added new permissions to allow GuardDuty to add<br>`guarddutyActivate` Amazon ECS account setting, and<br>perform list and describe operations on Amazon ECS clusters.                                                                                                                                                                                                                                                                                                                                                                                                                   | Nov 26, 2023      |
| [AmazonGuardDutyReadOnlyAccess](#security-iam-awsmanpol-AmazonGuardDutyReadOnlyAccess "#security-iam-awsmanpol-AmazonGuardDutyReadOnlyAccess") – Update to an existing policy             | GuardDuty added a new policy for `organizations` to<br>`ListAccounts`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | November 16, 2023 |
| [AmazonGuardDutyFullAccess](#security-iam-awsmanpol-AmazonGuardDutyFullAccess "#security-iam-awsmanpol-AmazonGuardDutyFullAccess")<br>– Update to an existing policy                      | GuardDuty added a new policy for `organizations` to<br>`ListAccounts`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | November 16, 2023 |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md")<br>– Update to an existing policy                                                                             | GuardDuty added new permissions to support the upcoming GuardDuty<br>EKS Runtime Monitoring feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | March 8, 2023     |
| [AmazonGuardDutyServiceRolePolicy](#security-iam-awsmanpol-AmazonGuardDutyServiceRolePolicy "#security-iam-awsmanpol-AmazonGuardDutyServiceRolePolicy") – Update to an<br>existing policy | GuardDuty has added new permissions to allow GuardDuty to create [Service-linked role for Malware Protection for EC2](slr-permissions-malware-protection.md "slr-permissions-malware-protection.md"). This will help GuardDuty<br>streamline the process of enabling Malware Protection for EC2.<br>GuardDuty can now perform the following IAM action:<br>`<br>{<br>"Effect": "Allow",<br>"Action": "iam:CreateServiceLinkedRole",<br>"Resource": "*",<br>"Condition": {<br>"StringEquals": {<br>"iam:AWSServiceName": "malware-protection.guardduty.amazonaws.com"<br>}<br>}<br>}<br>` | Feb 21, 2023      |
| [AmazonGuardDutyFullAccess](#security-iam-awsmanpol-AmazonGuardDutyFullAccess "#security-iam-awsmanpol-AmazonGuardDutyFullAccess")<br>– Update to an existing policy                      | GuardDuty updated ARN for `iam:GetRole` to<br>`*AWSServiceRoleForAmazonGuardDutyMalwareProtection`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Jul 26, 2022      |
| [AmazonGuardDutyFullAccess](#security-iam-awsmanpol-AmazonGuardDutyFullAccess "#security-iam-awsmanpol-AmazonGuardDutyFullAccess")<br>– Update to an existing policy                      | GuardDuty added a new `AWSServiceName` to allow the<br>creation of service-linked role using<br>`iam:CreateServiceLinkedRole` for GuardDuty Malware Protection for EC2<br>service.<br>GuardDuty can now perform the `iam:GetRole` action to gain<br>information for `AWSServiceRole`.                                                                                                                                                                                                                                                                                                    | Jul 26, 2022      |
| [AmazonGuardDutyServiceRolePolicy](slr-permissions.md "slr-permissions.md")<br>– Update to an existing policy                                                                             | GuardDuty added new permissions to allow GuardDuty to use Amazon EC2 networking<br>actions to improve findings.<br>GuardDuty can now perform the following EC2 actions to gain<br>information about how your EC2 instances are communicating. This<br>information is used to improve finding accuracy.<br>• `ec2:DescribeVpcEndpoints`<br>• `ec2:DescribeSubnets`<br>• `ec2:DescribeVpcPeeringConnections`<br>• `ec2:DescribeTransitGatewayAttachments`                                                                                                                                  | Aug 3, 2021       |
| GuardDuty started tracking<br>changes                                                                                                                                                     | GuardDuty started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Aug 3, 2021       |
