# AWS managed policies for Amazon S3 on Outposts

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

## AWS managed policy: AWSS3OnOutpostsServiceRolePolicy

Helps manage network resources for you as part of the service-linked role
`AWSServiceRoleForS3OnOutposts`.

To view the permissions for this policy, see [AWSS3OnOutpostsServiceRolePolicy](S3OutpostsServiceLinkedRoles.md "S3OutpostsServiceLinkedRoles.md").

## S3 on Outposts updates to AWS managed policies

View details about updates to AWS managed policies for S3 on Outposts since this
service began tracking these changes.

| Change                                                     | Description                                                                                                                                                                        | Date            |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| S3 on Outposts added<br>`AWSS3OnOutpostsServiceRolePolicy` | S3 on Outposts added `AWSS3OnOutpostsServiceRolePolicy`<br>as part of the service-linked role<br>`AWSServiceRoleForS3OnOutposts`, which helps manage<br>network resources for you. | October 3, 2023 |
| S3 on Outposts started tracking changes                    | S3 on Outposts started tracking changes for its AWS managed<br>policies.                                                                                                           | October 3, 2023 |
