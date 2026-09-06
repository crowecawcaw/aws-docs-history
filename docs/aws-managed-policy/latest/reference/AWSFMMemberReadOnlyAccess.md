

# AWSFMMemberReadOnlyAccess
<a name="AWSFMMemberReadOnlyAccess"></a>

**Description**: Provides read only access to AWS WAF actions for AWS Firewall Manager member accounts

`AWSFMMemberReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSFMMemberReadOnlyAccess-how-to-use"></a>

You can attach `AWSFMMemberReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSFMMemberReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 09, 2018, 21:05 UTC 
+ **Edited time:** May 09, 2018, 21:05 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSFMMemberReadOnlyAccess`

## Policy version
<a name="AWSFMMemberReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSFMMemberReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "fms:GetAdminAccount",
        "waf:Get*",
        "waf:List*",
        "waf-regional:Get*",
        "waf-regional:List*",
        "organizations:DescribeOrganization"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSFMMemberReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)