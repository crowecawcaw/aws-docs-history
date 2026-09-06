

# AmazonRoute53AutoNamingFullAccess
<a name="AmazonRoute53AutoNamingFullAccess"></a>

**Description**: Provides full access to all Route 53 Auto Naming actions.

`AmazonRoute53AutoNamingFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonRoute53AutoNamingFullAccess-how-to-use"></a>

You can attach `AmazonRoute53AutoNamingFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonRoute53AutoNamingFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 18, 2018, 18:40 UTC 
+ **Edited time:** January 18, 2018, 18:40 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonRoute53AutoNamingFullAccess`

## Policy version
<a name="AmazonRoute53AutoNamingFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonRoute53AutoNamingFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "route53:GetHostedZone",
        "route53:ListHostedZonesByName",
        "route53:CreateHostedZone",
        "route53:DeleteHostedZone",
        "route53:ChangeResourceRecordSets",
        "route53:CreateHealthCheck",
        "route53:GetHealthCheck",
        "route53:DeleteHealthCheck",
        "route53:UpdateHealthCheck",
        "ec2:DescribeVpcs",
        "ec2:DescribeRegions",
        "servicediscovery:*"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonRoute53AutoNamingFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)