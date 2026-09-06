

# AmazonRoute53ResolverReadOnlyAccess
<a name="AmazonRoute53ResolverReadOnlyAccess"></a>

**Description**: Read only policy for Route 53 Resolver

`AmazonRoute53ResolverReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonRoute53ResolverReadOnlyAccess-how-to-use"></a>

You can attach `AmazonRoute53ResolverReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonRoute53ResolverReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 30, 2019, 18:11 UTC 
+ **Edited time:** August 05, 2024, 18:54 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonRoute53ResolverReadOnlyAccess`

## Policy version
<a name="AmazonRoute53ResolverReadOnlyAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonRoute53ResolverReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AmazonRoute53ResolverReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "route53resolver:Get*",
        "route53resolver:List*",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonRoute53ResolverReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)