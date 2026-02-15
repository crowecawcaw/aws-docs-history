# AWS managed policies for AWS Local Zones

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

## AWS managed policy: AWSZoneGroupAccessManagementServiceRolePolicy

The `AWSZoneGroupAccessManagementServiceRolePolicy` policy is attached to the
`AWSServiceRoleForZoneGroupAccessManagement` service-linked role that allows
an administrator to enable Zone Groups on behalf of their entire organization,
automatically opting-in all existing member accounts and new accounts joining the
organization. You cannot attach this policy to your users, groups, or roles.

**Permissions details**

This policy includes the following permissions.

- `DescribeOrganization` – View organization details.
- `DescribeOrganizationalUnit` – View organizational unit
  information.
- `DescribeAccount` – View account details.
- `ListAccounts` – List all accounts in the organization.
- `ListParents` – List parent containers.
- `ListAWSServiceAccessForOrganization` – List AWS service
  access status.
- `ListChildren` – List child resources.
- `ListDelegatedAdministrators` – List delegated
  administrators.

To view details for this policy, see [AWSZoneGroupAccessManagementServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSZoneGroupAccessManagementServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSZoneGroupAccessManagementServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## AWS Local Zones updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Local Zones since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Local Zones Document history page.

| Change                                                     | Description                                                                                                                                                                                                                        | Date          |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| AWSZoneGroupAccessManagementServiceRolePolicy – New policy | Added a new AWS managed policy that allows<br>an administrator to enable Zone Groups on behalf of their entire organization,<br>automatically opting-in all existing member accounts and new accounts joining the<br>organization. | June 30, 2025 |
