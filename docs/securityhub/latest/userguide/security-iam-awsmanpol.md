# AWS managed policies for Security Hub

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

AWSSecurityHubFullAccess

You can attach the `AWSSecurityHubFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow a principal full access to all
Security Hub CSPM actions. This policy must be attached to a principal before they enable Security Hub CSPM
manually for their account. For example, principals with these permissions can both view
and update the status of findings. They can also configure custom insights, enable
integrations, and enable and disable standards and controls. Principals for an
administrator account can also manage member accounts.

**Permissions details**

This policy includes the following permissions:

- `securityhub` – Allows principals full access to all Security Hub CSPM
  actions.
- `guardduty` – Allows principals perform full lifecycle management of a detector, organization admin management, member account mnagement, and organiation-wide configuration in Amazon GuardDuty.
  This includes API actions: GetDetector, ListDetector, CreateDetector, UpdateDetector, DeleteDetector,
  EnableOrganizationAdminAccount, ListOrganizationAdminAccounts,
  CreateMembers, UpdateOrganizationConfiguration, DescribeOrganizationConfiguration.
- `iam` – Allows principals to create a service-linked role for Security Hub CSPM and Security Hub and to get roles, policies, and policy versions.
- `inspector` – Allows principals to get information about account status, enable or disable, delegate admin management, and perform organization configuration management in Amazon Inspector.
  This includes API actions: BatchGetAccountStatus, Enable, Disable,
  EnableDelegatedAdminAccount, DisableDelegatedAdminAccount, ListDelegatedAdminAccounts,
  UpdateOrganizationConfiguration, DescribeOrganizationConfiguration.
- `pricing` – Allows principals to get a price list of AWS services and products.
- `account` – Allows principals to get information about account Regions to support Region management in Security Hub.

To review the permissions for this policy, see [AWSSecurityHubFullAccess](../../../aws-managed-policy/latest/reference/AWSSecurityHubFullAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityHubFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

AWSSecurityHubReadOnlyAccess

You can attach the `AWSSecurityHubReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only permissions that allow users to view information in Security Hub CSPM.
Principals with this policy attached cannot make any updates in Security Hub CSPM. For example,
principals with these permissions can view the list of findings associated with their
account, but cannot change the status of a finding. They can view the results of insights,
but cannot create or configure custom insights. They cannot configure controls or product
integrations.

**Permissions details**

This policy includes the following permissions:

- `securityhub` – Allows users to perform actions that return a
  list of items or details about an item. This includes API operations that start
  with `Get`, `List`, or `Describe`.

To review the permissions for this policy, see [AWSSecurityHubReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSSecurityHubReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityHubReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed

policy: AWSSecurityHubOrganizationsAccess

You can attach the `AWSSecurityHubOrganizationsAccess` policy to your IAM identities.

This policy grants administrative permissions to enable and manage Security Hub, Security Hub CSPM, Amazon GuardDuty and Amazon Inspector for an organization in AWS Organizations.
The permissions for this policy allow the organization management account to designate the delegated administrator account for Security Hub, Security Hub CSPM, Amazon GuardDuty and Amazon Inspector.
They also allow the delegated administrator account to enable organization accounts as member accounts.

This policy only provides permissions for AWS Organizations. The organization management account
and delegated administrator account also require permissions for associated actions.
These permissions can be granted using the `AWSSecurityHubFullAccess` managed
policy.

Creating or updating a delegated administrator policy in a management account requires additional permissions that are not provided in this policy.
To perform these actions is is recommended to add permissions for `organizations:PutResourcePolicy` or attach the AWSOrganizationsFullAccess policy.

**Permissions details**

This policy includes the following permissions:

- `organizations:ListAccounts` – Allows principals to retrieve the
  list of accounts that are part of an organization.
- `organizations:DescribeOrganization` – Allows principals to
  retrieve information about the organization.
- `organizations:ListRoots` – Allows principals to
  list the root of an organization.
- `organizations:ListDelegatedAdministrators` – Allows principals to
  list the delegated administrator of an organization.
- `organizations:ListAWSServiceAccessForOrganization` – Allows principals to list the AWS services that an
  organization uses.
- `organizations:ListOrganizationalUnitsForParent` – Allows principals to list the child organizational units (OU) of
  a parent OU.
- `organizations:ListAccountsForParent` – Allows principals to list the child accounts of a parent OU.
- `organizations:ListParents` – Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account.
- `organizations:DescribeAccount` – Allows principals to
  retrieve information about an account in the organization.
- `organizations:DescribeOrganizationalUnit` – Allows principals to
  retrieve information about an OU in the organization.
- `organizations:ListPolicies` – Retrieves the list of all policies in an organization of a specified type.
- `organizations:ListPoliciesForTarget` – Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account.
- `organizations:ListTargetsForPolicy` – Lists all the roots, organizational units (OUs), and accounts that the specified policy is attached to.
- `organizations:EnableAWSServiceAccess` – Allows principals to
  enable the integration with Organizations.
- `organizations:RegisterDelegatedAdministrator` – Allows
  principals to designate the delegated administrator account.
- `organizations:DeregisterDelegatedAdministrator` – Allows
  principals to remove the delegated administrator account.
- `organizations:DescribePolicy` – Retrieves information about a policy.
- `organizations:DescribeEffectivePolicy` – Returns the contents of the effective policy for specified policy type and account.
- `organizations:CreatePolicy` – Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.
- `organizations:UpdatePolicy` – Updates an existing policy with a new name, description, or content.
- `organizations:DeletePolicy` – Deletes the specified policy from your organization.
- `organizations:AttachPolicy` – Attaches a policy to a root, an organizational unit (OU), or an individual account.
- `organizations:DetachPolicy` – Detaches a policy from a target root, organizational unit (OU), or account.
- `organizations:EnablePolicyType` – Enables a policy type in a root.
- `organizations:DisablePolicyType` – Disables an organizational policy type in a root.
- `organizations:TagResource` – Adds one or more tags to a specified resource.
- `organizations:UntagResource` – Removes any tags with the specified keys from a specified resource.
- `organizations:ListTagsForResource` – Lists tags that are attached to a specified resource.
- `organizations:DescribeResourcePolicy` – Retrieves information about a resource policy.

To review the permissions for this policy, see [AWSSecurityHubOrganizationsAccess](../../../aws-managed-policy/latest/reference/AWSSecurityHubOrganizationsAccess.md "../../../aws-managed-policy/latest/reference/AWSSecurityHubOrganizationsAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed

policy: AWSSecurityHubServiceRolePolicy

You can't attach `AWSSecurityHubServiceRolePolicy` to your IAM entities.
This policy is attached to a service-linked role that allows Security Hub CSPM to perform actions on
your behalf. For more information, see [Service-linked roles for AWS Security Hub](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allow the service-linked role to
perform tasks such as run security checks for Security Hub CSPM controls.

**Permissions details**

This policy includes the following permissions:

- `cloudtrail` – Retrieve information about CloudTrail trails.
- `cloudwatch` – Retrieve current CloudWatch alarms.
- `logs` – Retrieve metric filters for CloudWatch logs.
- `sns` – Retrieve the list of subscriptions to an SNS
  topic.
- `config` – Retrieve information about configuration recorders,
  resources, and AWS Config rules. Also allows the service-linked role to create and delete
  AWS Config rules, and to run evaluations against the rules.
- `iam` – Retrieve and generate credential reports for
  accounts.
- `organizations` – Retrieve account and organizational unit (OU) information for an
  organization.
- `securityhub` – Retrieve information about how the Security Hub CSPM service, standards, and controls
  are configured.
- `tag` – Retrieve information about resource tags.

To review the permissions for this policy, see [AWSSecurityHubServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSecurityHubServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSecurityHubServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AWSSecurityHubV2ServiceRolePolicy

###### Note

Security Hub is in preview release and subject to change.

This policy allows Security Hub to manage AWS Config rules and Security Hub resources for your
organization and on your behalf. This policy is attached to a service-linked role that
allows the service to perform actions on your behalf. You cannot attach this policy to
your IAM identities. For more information, see [Service-linked roles for AWS Security Hub](using-service-linked-roles.md "using-service-linked-roles.md").

###### Permissions details

This policy includes the following permissions:

- `cloudwatch` – Retrieve metrics data to support metering capabilities for Security Hub resources.
- `config` – Manage service-linked configuration recorders for
  Security Hub resources, including support for global Config recorders.
- `ecr` – Retrieve information about Amazon Elastic Container Registry images and repositories to support metering capabilities.
- `iam` – Create the service-linked role for AWS Config and retrieve account information to support metering capabilities.
- `lambda` – Retrieve AWS Lambda function information to support metering capabilities.
- `organizations` – Retrieve account and organizational unit
  (OU) information for an organization.
- `securityhub` – Manage the Security Hub configuration.
- `tag` – Retrieve information about resource tags.

To review the permissions for this policy, see [AWSSecurityHubV2ServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSecurityHubV2ServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSecurityHubV2ServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## Security Hub updates to AWS managed

policies

The following table provides details about updates to AWS managed policies for
AWS Security Hub and Security Hub CSPM since this service began tracking these changes. For automatic
alerts about updates to the policies, subscribe to the RSS feed on the [Security Hub document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                          | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| [AWSSecurityHubOrganizationsAccess](#security-iam-awsmanpol-awssecurityhuborganizationsaccess "#security-iam-awsmanpol-awssecurityhuborganizationsaccess") – Updated policy                     | Security Hub updated the policy to add permissions to describe resource policies to support Security Hub features. Security Hub is in preview release and subject to change.                                                                                                                                                         | November 12, 2025  |
| [AWSSecurityHubFullAccess](#security-iam-awsmanpol-awssecurityhubfullaccess "#security-iam-awsmanpol-awssecurityhubfullaccess") – Updated policy                                                | Security Hub updated the policy to add capabilities around managing GuardDuty, Amazon Inspector, and account management to support Security Hub features. Security Hub is in preview release and subject to change.                                                                                                                  | November 17, 2025  |
| [AWSSecurityHubV2ServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") – Updated policy                     | Security Hub updated the policy to add metering capabilities for Amazon Elastic Container Registry, AWS Lambda, Amazon CloudWatch, and AWS Identity and Access Management to support Security Hub features. The update also added support for global AWS Config recorders. Security Hub is in preview release and subject to change. | November 5, 2025   |
| [AWSSecurityHubOrganizationsAccess](#security-iam-awsmanpol-awssecurityhuborganizationsaccess "#security-iam-awsmanpol-awssecurityhuborganizationsaccess") – Update to an<br>existing policy    | Security Hub added new permissions to the policy. The permissions allow the<br>organization management to enable and manage Security Hub and Security Hub CSPM for an<br>organization.                                                                                                                                               | June 17, 2025      |
| [AWSSecurityHubFullAccess](#security-iam-awsmanpol-awssecurityhubfullaccess "#security-iam-awsmanpol-awssecurityhubfullaccess") – Update to an existing policy                                  | Security Hub CSPM added new permissions that allow principals to create a<br>service-linked role for Security Hub.                                                                                                                                                                                                                   | June 17, 2025      |
| [AWSSecurityHubFullAccess](#security-iam-awsmanpol-awssecurityhubfullaccess "#security-iam-awsmanpol-awssecurityhubfullaccess") – Update to an existing policy                                  | Security Hub CSPM updated the policy to get pricing details for AWS services and products.                                                                                                                                                                                                                                           | April 24, 2024     |
| [AWSSecurityHubReadOnlyAccess](#security-iam-awsmanpol-awssecurityhubreadonlyaccess "#security-iam-awsmanpol-awssecurityhubreadonlyaccess") – Update to an existing policy                      | Security Hub CSPM updated this managed policy by adding a `Sid` field.                                                                                                                                                                                                                                                               | February 22, 2024  |
| [AWSSecurityHubFullAccess](#security-iam-awsmanpol-awssecurityhubfullaccess "#security-iam-awsmanpol-awssecurityhubfullaccess") – Update to an existing policy                                  | Security Hub CSPM updated the policy so it can determine if Amazon GuardDuty and Amazon Inspector are enabled in an account.<br>This helps customers bring together security-related information from multiple AWS services.                                                                                                         | November 16, 2023  |
| [AWSSecurityHubOrganizationsAccess](#security-iam-awsmanpol-awssecurityhuborganizationsaccess "#security-iam-awsmanpol-awssecurityhuborganizationsaccess") – Update to an existing policy       | Security Hub CSPM updated the policy to grant additional permissions to allow read-only access to AWS Organizations<br>delegated administrator functionality. This includes details like the root, organizational units (OUs),<br>accounts, organizational structure, and service access.                                            | November 16, 2023  |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM added the `BatchGetSecurityControls`, `DisassociateFromAdministratorAccount`, and<br>`UpdateSecurityControl` permissions to read and update customizable security control properties.                                                                                                                              | November 26, 2023  |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM added the `tag:GetResources` permission to read resource tags related to findings.                                                                                                                                                                                                                                 | November 7, 2023   |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM added the `BatchGetStandardsControlAssociations` permission to get information about the<br>enablement status of a control in a standard.                                                                                                                                                                          | September 27, 2023 |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM added new permissions to get AWS Organizations data and read and update Security Hub CSPM configurations, including<br>standards and controls.                                                                                                                                                                     | September 20, 2023 |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM moved the existing `config:DescribeConfigRuleEvaluationStatus` permission to<br>a different statement within the policy. The `config:DescribeConfigRuleEvaluationStatus` permission is now applied to all<br>resources.                                                                                            | March 17, 2023     |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update to an<br>existing policy          | Security Hub CSPM moved the existing `config:PutEvaluations` permission to<br>a different statement within the policy. The `config:PutEvaluations` permission<br>is now applied to all resources.                                                                                                                                    | July 14, 2021      |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Update<br>to an existing policy          | Security Hub CSPM added a new permission to allow the service-linked role to deliver<br>evaluation results to AWS Config.                                                                                                                                                                                                            | June 29, 2021      |
| [AWSSecurityHubServiceRolePolicy](#security-iam-awsmanpol-awssecurityhubservicerolepolicy "#security-iam-awsmanpol-awssecurityhubservicerolepolicy") – Added to<br>the list of managed policies | Added information about the managed policy<br>AWSSecurityHubServiceRolePolicy, which is used by the Security Hub CSPM<br>service-linked role.                                                                                                                                                                                        | June 11, 2021      |
| [AWSSecurityHubOrganizationsAccess](#security-iam-awsmanpol-awssecurityhuborganizationsaccess "#security-iam-awsmanpol-awssecurityhuborganizationsaccess") – New policy                         | Security Hub CSPM added a new policy that grants permissions that are needed for the<br>Security Hub CSPM integration with Organizations.                                                                                                                                                                                            | March 15, 2021     |
| Security Hub CSPM started tracking changes                                                                                                                                                      | Security Hub CSPM started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                             | March 15, 2021     |
