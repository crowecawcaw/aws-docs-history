# AWS managed policies for Site-to-Site VPN

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't break
your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed

policy: AWSVPCS2SVpnServiceRolePolicy

You can attach the `AWSVPCS2SVpnServiceRolePolicy` policy to your IAM
identities. This policy allows Site-to-Site VPN to manage an AWS Secrets Manager secret within Site-to-Site VPN. For more
information, see [Using service-linked roles for
Site-to-Site VPN](using-service-linked-roles.md "using-service-linked-roles.md").

To view the permissions for this policy, see [AWSVPCS2SVpnServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVPCS2SVpnServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVPCS2SVpnServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## Site-to-Site VPN updates to AWS managed

policies

View details about updates to AWS managed policies for Site-to-Site VPN since this service began
tracking these changes in May 2025.

| Change                                                                                                                                          | Description                                                                                                                                  | Date         |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [AWSVPCS2SVpnServiceRolePolicy](#security-iam-AWSVPCS2SVpnServiceRolePolicy "#security-iam-AWSVPCS2SVpnServiceRolePolicy")<br>• Updated policy. | New permissions added to the policy allowing Site-to-Site VPN to manage the VPN<br>connection's AWS Secrets Manager `s2svpn`-managed secret. | May 14, 2025 |
