# AWS managed policies for AWS Support

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

###### Topics

- [AWS managed policies for
  AWS Support](aws-managed-policies-aws-support.md "aws-managed-policies-aws-support.md")
- [AWS managed policies for
  AWS Support App in Slack](support-app-managed-policies.md "support-app-managed-policies.md")
- [AWS managed policies for
  AWS Trusted Advisor](aws-managed-policies-for-trusted-advisor.md "aws-managed-policies-for-trusted-advisor.md")
- [AWS managed policies for
  AWS Support Plans](managed-policies-aws-support-plans.md "managed-policies-aws-support-plans.md")
- [AWS managed policies for AWS Partner-Led Support](managed-policies-partner-led-support.md "managed-policies-partner-led-support.md")
