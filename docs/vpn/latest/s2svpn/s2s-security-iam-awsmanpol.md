

# AWS managed policies for Site-to-Site VPN
<a name="s2s-security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSVPCS2SVpnServiceRolePolicy
<a name="security-iam-AWSVPCS2SVpnServiceRolePolicy"></a>

You can attach the `AWSVPCS2SVpnServiceRolePolicy` policy to your IAM identities. This policy allows Site-to-Site VPN to manage an AWS Secrets Manager secret within Site-to-Site VPN. For more information, see [Using service-linked roles for Site-to-Site VPN](using-service-linked-roles.md).

To view the permissions for this policy, see [AWSVPCS2SVpnServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVPCS2SVpnServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Site-to-Site VPN updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Site-to-Site VPN since this service began tracking these changes in May 2025.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSVPCS2SVpnServiceRolePolicy](#security-iam-AWSVPCS2SVpnServiceRolePolicy) - Updated policy.  | New permissions added to the policy allowing Site-to-Site VPN to manage the VPN connection's AWS Secrets Manager s2svpn-managed secret. | May 14, 2025 | 