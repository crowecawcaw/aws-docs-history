

# AWSCloudMapRegisterInstanceAccess
<a name="AWSCloudMapRegisterInstanceAccess"></a>

**Description**: Provides registrant level access to AWS Cloud Map actions.

`AWSCloudMapRegisterInstanceAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCloudMapRegisterInstanceAccess-how-to-use"></a>

You can attach `AWSCloudMapRegisterInstanceAccess` to your users, groups, and roles.

## Policy details
<a name="AWSCloudMapRegisterInstanceAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 29, 2018, 00:04 UTC 
+ **Edited time:** September 20, 2023, 21:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCloudMapRegisterInstanceAccess`

## Policy version
<a name="AWSCloudMapRegisterInstanceAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCloudMapRegisterInstanceAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "route53:GetHostedZone",
        "route53:ListHostedZonesByName",
        "route53:ChangeResourceRecordSets",
        "route53:CreateHealthCheck",
        "route53:GetHealthCheck",
        "route53:DeleteHealthCheck",
        "route53:UpdateHealthCheck",
        "servicediscovery:Get*",
        "servicediscovery:List*",
        "servicediscovery:RegisterInstance",
        "servicediscovery:DeregisterInstance",
        "servicediscovery:DiscoverInstances",
        "servicediscovery:DiscoverInstancesRevision",
        "ec2:DescribeInstances"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSCloudMapRegisterInstanceAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)