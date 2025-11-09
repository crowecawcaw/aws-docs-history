# Identity-based policy examples for

Amazon CloudFront

By default, users and roles don't have permission to create or modify CloudFront
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by CloudFront, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon CloudFront](../../../service-authorization/latest/reference/list_amazoncloudfront.md "../../../service-authorization/latest/reference/list_amazoncloudfront.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Permissions to access CloudFront programmatically](#security_iam_id-based-policy-examples-programmatic-access-all "#security_iam_id-based-policy-examples-programmatic-access-all")
- [Permissions required to use the CloudFront console](#security_iam_id-based-policy-examples-console-required-permissions "#security_iam_id-based-policy-examples-console-required-permissions")
- [Customer managed policy
  examples](#security_iam_id-based-policy-examples-sdk-cli "#security_iam_id-based-policy-examples-sdk-cli")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete CloudFront resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## Permissions to access CloudFront programmatically

The following shows a permissions policy. The `Sid`, or statement ID, is
optional.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAllCloudFrontPermissions",
 "Effect": "Allow",
 "Action": ["cloudfront:*"],
 "Resource": "*"
 }
 ]
}`

```

The policy grants permissions to perform all CloudFront operations, which is sufficient to
access CloudFront programmatically. If you're using the console to access CloudFront, see [Permissions required to use the CloudFront console](#security_iam_id-based-policy-examples-console-required-permissions "#security_iam_id-based-policy-examples-console-required-permissions").

For a list of actions and the ARN that you specify to grant or deny permission to use
each action, see [Actions, resources, and condition keys for Amazon CloudFront](../../../service-authorization/latest/reference/list_amazoncloudfront.md "../../../service-authorization/latest/reference/list_amazoncloudfront.md") in
the _Service Authorization Reference_.

## Permissions required to use the CloudFront console

To grant full access to the CloudFront console, you grant the permissions in the following
permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "acm:ListCertificates",
 "cloudfront:*",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:GetMetricStatistics",
 "elasticloadbalancing:DescribeLoadBalancers",
 "iam:ListServerCertificates",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics",
 "waf:GetWebACL",
 "waf:ListWebACLs"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ListAllMyBuckets",
 "s3:PutBucketPolicy"
 ],
 "Resource":"arn:aws:s3:::*"
 }
 ]
}`

```

Here's why the permissions are required:

**`acm:ListCertificates`**

When you're creating and updating distributions by using the CloudFront console
and you want to configure CloudFront to require HTTPS between the viewer and CloudFront or
between CloudFront and the origin, lets you view a list of ACM certificates.

This permission isn't required if you aren't using the CloudFront console.

**`cloudfront:*`**

Lets you perform all CloudFront actions.

**`cloudwatch:DescribeAlarms` and
`cloudwatch:PutMetricAlarm`**

Let you create and view CloudWatch alarms in the CloudFront console. See also
`sns:ListSubscriptionsByTopic` and
`sns:ListTopics`.

These permissions aren't required if you aren't using the CloudFront
console.

**`cloudwatch:GetMetricStatistics`**

Lets CloudFront render CloudWatch metrics in the CloudFront console.

This permission isn't required if you aren't using the CloudFront console.

**`elasticloadbalancing:DescribeLoadBalancers`**

When creating and updating distributions, lets you view a list of Elastic Load Balancing load
balancers in the list of available origins.

This permission isn't required if you aren't using the CloudFront console.

**`iam:ListServerCertificates`**

When you're creating and updating distributions by using the CloudFront console
and you want to configure CloudFront to require HTTPS between the viewer and CloudFront or
between CloudFront and the origin, lets you view a list of certificates in the IAM
certificate store.

This permission isn't required if you aren't using the CloudFront console.

**`s3:ListAllMyBuckets`**

When you're creating and updating distributions, lets you perform the
following operations:

- View a list of S3 buckets in the list of available origins
- View a list of S3 buckets that you can save access logs in

This permission isn't required if you aren't using the CloudFront console.

**`S3:PutBucketPolicy`**

When you're creating or updating distributions that restrict access to S3
buckets, lets a user update the bucket policy to grant access to the CloudFront
origin access identity. For more information, see [Use an origin access
identity (legacy, not recommended)](private-content-restricting-access-to-s3.md#private-content-restricting-access-to-s3-oai "private-content-restricting-access-to-s3.md#private-content-restricting-access-to-s3-oai").

This permission isn't required if you aren't using the CloudFront console.

**`sns:ListSubscriptionsByTopic` and
`sns:ListTopics`**

When you create CloudWatch alarms in the CloudFront console, lets you choose an SNS
topic for notifications.

These permissions aren't required if you aren't using the CloudFront
console.

**`waf:GetWebACL` and `waf:ListWebACLs`**

Lets you view a list of AWS WAF web ACLs in the CloudFront console.

These permissions aren't required if you aren't using the CloudFront
console.

### Permission-only actions for the CloudFront

console

You can perform the following CloudFront actions on the [CloudFront Security Savings
Bundle](https://console.aws.amazon.com/cloudfront/v3/home#/savings-bundle/overview "https://console.aws.amazon.com/cloudfront/v3/home#/savings-bundle/overview") page. The following API actions are not intended to be called by
your code, and are not included in the AWS CLI and AWS SDKs.

| Action              | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `CreateSavingsPlan` | Grants permission to create a new savings plan.                  |
| `GetSavingsPlan`    | Grants permission to get a savings plan.                         |
| `ListRateCards`     | Grants permission to list CloudFront rate cards for the account. |
| `ListSavingsPlans`  | Grants permission to list savings plans in the account.          |
| `ListUsages`        | Grants permission to list CloudFront usage.                      |
| `UpdateSavingsPlan` | Grants permission to update a savings plan.                      |

###### Notes

- For more information about CloudFront savings plans, see the CloudFront Security
  Savings Bundle section of the [Amazon CloudFront FAQs](https://aws.amazon.com/cloudfront/faqs/ "https://aws.amazon.com/cloudfront/faqs/").
- If you create a savings plan for CloudFront and then want to delete it later,
  contact [AWS Support](https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service "https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service").

## Customer managed policy

examples

You can create your own custom IAM policies to allow permissions for CloudFront API
actions. You can attach these custom policies to the IAM users or groups that require
the specified permissions. These policies work when you are using the CloudFront API, the
AWS SDKs, or the AWS CLI. The following examples show permissions for a few common use
cases. For the policy that grants a user full access to CloudFront, see [Permissions required to use the CloudFront console](#security_iam_id-based-policy-examples-console-required-permissions "#security_iam_id-based-policy-examples-console-required-permissions").

###### Examples

- [Example 1: Allow read access to all distributions](#security_iam_id-based-policy-examples-allow-read-all-distributions "#security_iam_id-based-policy-examples-allow-read-all-distributions")
- [Example 2: Allow creating, updating, and deleting distributions](#security_iam_id-based-policy-examples-allow-create-update-delete-distributions "#security_iam_id-based-policy-examples-allow-create-update-delete-distributions")
- [Example 3: Allow creating and listing invalidations](#security_iam_id-based-policy-examples-allow-create-list-invalidations "#security_iam_id-based-policy-examples-allow-create-list-invalidations")
- [Example 4: Allow creating a
  distribution](#create-distribution-iam-policy "#create-distribution-iam-policy")

### Example 1: Allow read access to all distributions

The following permissions policy grants the user permissions to view all
distributions in the CloudFront console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "acm:ListCertificates",
 "cloudfront:GetDistribution",
 "cloudfront:GetDistributionConfig",
 "cloudfront:ListDistributions",
 "cloudfront:ListCloudFrontOriginAccessIdentities",
 "elasticloadbalancing:DescribeLoadBalancers",
 "iam:ListServerCertificates",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics",
 "waf:GetWebACL",
 "waf:ListWebACLs"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ListAllMyBuckets"
 ],
 "Resource":"arn:aws:s3:::*"
 }
 ]
}`

```

### Example 2: Allow creating, updating, and deleting distributions

The following permissions policy allows users to create, update, and delete
distributions by using the CloudFront console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "acm:ListCertificates",
 "cloudfront:CreateDistribution",
 "cloudfront:DeleteDistribution",
 "cloudfront:GetDistribution",
 "cloudfront:GetDistributionConfig",
 "cloudfront:ListDistributions",
 "cloudfront:UpdateDistribution",
 "cloudfront:ListCloudFrontOriginAccessIdentities",
 "elasticloadbalancing:DescribeLoadBalancers",
 "iam:ListServerCertificates",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics",
 "waf:GetWebACL",
 "waf:ListWebACLs"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ListAllMyBuckets",
 "s3:PutBucketPolicy"
 ],
 "Resource":"arn:aws:s3:::*"
 }
 ]
}`

```

The `cloudfront:ListCloudFrontOriginAccessIdentities` permission allows
users to automatically grant to an existing origin access identity the permission to
access objects in an Amazon S3 bucket. If you also want users to be able to create origin
access identities, you also need to allow the
`cloudfront:CreateCloudFrontOriginAccessIdentity` permission.

### Example 3: Allow creating and listing invalidations

The following permissions policy allows users to create and list invalidations. It
includes read access to CloudFront distributions because you create and view invalidations
by first displaying settings for a distribution:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "acm:ListCertificates",
 "cloudfront:GetDistribution",
 "cloudfront:GetStreamingDistribution",
 "cloudfront:GetDistributionConfig",
 "cloudfront:ListDistributions",
 "cloudfront:ListCloudFrontOriginAccessIdentities",
 "cloudfront:CreateInvalidation",
 "cloudfront:GetInvalidation",
 "cloudfront:ListInvalidations",
 "elasticloadbalancing:DescribeLoadBalancers",
 "iam:ListServerCertificates",
 "sns:ListSubscriptionsByTopic",
 "sns:ListTopics",
 "waf:GetWebACL",
 "waf:ListWebACLs"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ListAllMyBuckets"
 ],
 "Resource":"arn:aws:s3:::*"
 }
 ]
}`

```

### Example 4: Allow creating a

distribution

The following permission policy grants the user permission to create and list
distributions in the CloudFront console. For the `CreateDistribution` action,
specify the wildcard (\*) character for the `Resource` instead of a
wildcard for the distribution ARN
(`arn:aws:cloudfront::123456789012:distribution/*`). For more
information about the `Resource` element, see [IAM JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the
_IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "cloudfront:CreateDistribution",
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": "cloudfront:ListDistributions",
 "Resource": "*"
 }
 ]
}`

```
