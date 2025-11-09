# AWS managed policies for AWS Elemental MediaPackage

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

## AWS managed

policy: AWSElementalMediaPackageV2FullAccess

This policy grants contributor permissions that allow all actions on all live resources in
MediaPackage.

You can attach the `AWSElementalMediaPackageV2FullAccess` policy to your
IAM identities.

To view the permissions for this policy, see [AWSElementalMediaPackageV2FullAccess](../../../aws-managed-policy/latest/reference/AWSElementalMediaPackageV2FullAccess.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaPackageV2FullAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed

policy: AWSElementalMediaPackageV2ReadOnly

This policy grants contributor permissions that allow read-only actions on all live resources in
MediaPackage.

You can attach the `AWSElementalMediaPackageV2ReadOnly` policy to your
IAM identities.

To view the permissions for this policy, see [AWSElementalMediaPackageV2ReadOnly](../../../aws-managed-policy/latest/reference/AWSElementalMediaPackageV2ReadOnly.md "../../../aws-managed-policy/latest/reference/AWSElementalMediaPackageV2ReadOnly.md") in the _AWS Managed Policy Reference_.

## MediaPackage updates to AWS managed

policies

View details about updates to AWS managed policies for MediaPackage since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the MediaPackage [Document history](doc-history.md "doc-history.md")
page.

| Change                                                 | Description                                                                                                                                      | Date          |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `AWSElementalMediaPackageV2FullAccess` – New<br>policy | MediaPackage added a new full-access policy for live resources.<br>This policy allows all actions on all live resources in MediaPackage.         | July 25, 2023 |
| `AWSElementalMediaPackageV2ReadOnly` – New<br>policy   | MediaPackage added a new read-only pollicy for live resources.<br>This policy allows read-only actions on all live resources in<br>MediaPackage. | July 25, 2023 |
| MediaPackage started tracking changes                  | MediaPackage started tracking changes for its AWS managed policies.                                                                              | July 25, 2023 |
