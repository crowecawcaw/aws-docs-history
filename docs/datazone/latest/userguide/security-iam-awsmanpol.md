# AWS managed policies for Amazon DataZone

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

###### Contents

- [AWS managed
  policy: AmazonDataZoneFullAccess](security-iam-awsmanpol-AmazonDataZoneFullAccess.md "security-iam-awsmanpol-AmazonDataZoneFullAccess.md")
- [AWS managed
  policy: AmazonDataZoneFullUserAccess](security-iam-awsmanpol-AmazonDataZoneFullUserAccess.md "security-iam-awsmanpol-AmazonDataZoneFullUserAccess.md")
- [AWS managed policy:
  AmazonDataZoneEnvironmentRolePermissionsBoundary](security-iam-awsmanpol-AmazonDataZoneEnvironmentRolePermissionsBoundary.md "security-iam-awsmanpol-AmazonDataZoneEnvironmentRolePermissionsBoundary.md")
- [AWS managed policy:
  AmazonDataZoneRedshiftGlueProvisioningPolicy](security-iam-awsmanpol-AmazonDataZoneRedshiftGlueProvisioningPolicy.md "security-iam-awsmanpol-AmazonDataZoneRedshiftGlueProvisioningPolicy.md")
- [AWS managed policy:
  AmazonDataZoneGlueManageAccessRolePolicy](security-iam-awsmanpol-AmazonDataZoneGlueManageAccessRolePolicy.md "security-iam-awsmanpol-AmazonDataZoneGlueManageAccessRolePolicy.md")
- [AWS managed policy:
  AmazonDataZoneRedshiftManageAccessRolePolicy](security-iam-awsmanpol-AmazonDataZoneRedshiftManageAccessRolePolicy.md "security-iam-awsmanpol-AmazonDataZoneRedshiftManageAccessRolePolicy.md")
- [AWS managed policy:
  AmazonDataZoneDomainExecutionRolePolicy](security-iam-awsmanpol-AmazonDataZoneDomainExecutionRolePolicy.md "security-iam-awsmanpol-AmazonDataZoneDomainExecutionRolePolicy.md")
- [AWS managed policy:
  AmazonDataZoneSageMakerProvisioningRolePolicy](security-iam-awsmanpol-AmazonDataZoneSageMakerProvisioningRolePolicy.md "security-iam-awsmanpol-AmazonDataZoneSageMakerProvisioningRolePolicy.md")
- [AWS managed policy:
  AmazonDataZoneSageMakerManageAccessRolePolicy](security-iam-awsmanpol-AmazonDataZoneSageMakerManageAccessRolePolicy.md "security-iam-awsmanpol-AmazonDataZoneSageMakerManageAccessRolePolicy.md")
- [AWS managed policy:
  AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary](security-iam-awsmanpol-AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary.md "security-iam-awsmanpol-AmazonDataZoneSageMakerEnvironmentRolePermissionsBoundary.md")
- [Amazon DataZone updates to AWS managed
  policies](security-iam-awsmanpol-updates.md "security-iam-awsmanpol-updates.md")
