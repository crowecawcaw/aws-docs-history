**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Identity-based policy examples for

AWS Shield

By default, users and roles don't have permission to create or modify Shield
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Shield, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Shield](../../../service-authorization/latest/reference/list_awsshield.md "../../../service-authorization/latest/reference/list_awsshield.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#shd-security_iam_service-with-iam-policy-best-practices "#shd-security_iam_service-with-iam-policy-best-practices")
- [Using the Shield
  console](#shd-security_iam_id-based-policy-examples-console "#shd-security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#shd-security_iam_id-based-policy-examples-view-own-permissions "#shd-security_iam_id-based-policy-examples-view-own-permissions")
- [Grant read access to your Shield Advanced protections](#shd-example0 "#shd-example0")
- [Grant read-only access to Shield, CloudFront, and CloudWatch](#shd-example1 "#shd-example1")
- [Grant full access to Shield, CloudFront, and
  CloudWatch](#shd-example2 "#shd-example2")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Shield resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the Shield

console

To access the AWS Shield console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Shield resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

Users who can access and use the AWS console can also access the
AWS Shield console. No additional permissions are required.

### Console-only APIs

You can access the following Distributed Denial of Service (DDoS) attack information in the console. Specify the following API permissions in an IAM policy to allow or deny specific actions.

| Action                       | Description                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `DescribeAttackContributors` | Grants permission to get detailed information about the<br>contributors to a specific DDoS attack.                       |
| `ListMitigations`            | Grants permission to retrieve a list of mitigation actions that<br>have been applied during DDoS attacks.                |
| `GetGlobalThreatData`        | Grants permission to retrieve global threat intelligence data and<br>trends from AWS Shield's threat monitoring systems. |

This example shows how you might create a policy that allows you to see DDoS
attack information in the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "shield:DescribeAttackContributors"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "shield:ListMitigations"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "shield:GetGlobalThreatData"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Grant read access to your Shield Advanced protections

AWS Shield allows cross-account resource access, but it doesn't allow you to create
cross-account resource protections. You can only create protections for resources from
within the account that owns those resources.

The following is an example policy that grants permissions for the
`shield:ListProtections` action on all resources. Shield doesn't
support identifying specific resources using the resource ARNs (also referred to as
resource-level permissions) for some of the API actions, so you specify a wildcard
character (\*). This only permits access to the resources that you can retrieve through
the action `ListProtections`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListProtections",
 "Effect": "Allow",
 "Action": [
 "shield:ListProtections"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Grant read-only access to Shield, CloudFront, and CloudWatch

The following policy grants users read-only access to Shield and associated
resources, including Amazon CloudFront resources, and Amazon CloudWatch metrics. It's useful for users who
need permission to view the settings in Shield protections and attacks and to
monitor metrics in CloudWatch. These users can't create, update, or delete Shield
resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ProtectedResourcesReadAccess",
 "Effect": "Allow",
 "Action": [
 "cloudfront:List*",
 "route53:List*",
 "cloudfront:Describe*",
 "elasticloadbalancing:Describe*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "cloudfront:GetDistribution*",
 "globalaccelerator:ListAccelerators",
 "globalaccelerator:DescribeAccelerator"
 ],
 "Resource": [
 "arn:aws:elasticloadbalancing:*:*:*",
 "arn:aws:cloudfront::*:*",
 "arn:aws:route53:::hostedzone/*",
 "arn:aws:cloudwatch:*:*:*:*",
 "arn:aws:globalaccelerator::*:*"
 ]
 },
 {
 "Sid": "ShieldReadOnly",
 "Effect": "Allow",
 "Action": [
 "shield:List*",
 "shield:Describe*",
 "shield:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Grant full access to Shield, CloudFront, and

CloudWatch

The following policy lets users perform any Shield operation, perform any operation on
CloudFront web distributions, and monitor metrics and a sample of requests in CloudWatch. It's useful
for users who are Shield administrators.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ProtectedResourcesReadAccess",
 "Effect": "Allow",
 "Action": [
 "cloudfront:List*",
 "route53:List*",
 "cloudfront:Describe*",
 "elasticloadbalancing:Describe*",
 "cloudwatch:Describe*",
 "cloudwatch:Get*",
 "cloudwatch:List*",
 "cloudfront:GetDistribution*",
 "globalaccelerator:ListAccelerators",
 "globalaccelerator:DescribeAccelerator"
 ],
 "Resource": [
 "arn:aws:elasticloadbalancing:*:*:*",
 "arn:aws:cloudfront::*:*",
 "arn:aws:route53:::hostedzone/*",
 "arn:aws:cloudwatch:*:*:*:*",
 "arn:aws:globalaccelerator::*:*"
 ]
 },
 {
 "Sid": "ShieldFullAccess",
 "Effect": "Allow",
 "Action": [
 "shield:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

We strongly recommend that you configure multi-factor authentication (MFA) for users
who have administrative permissions. For more information, see [Using Multi-Factor Authentication (MFA)
Devices with AWS](../../../IAM/latest/UserGuide/Using_ManagingMFA.md "../../../IAM/latest/UserGuide/Using_ManagingMFA.md") in the _IAM User Guide_.
