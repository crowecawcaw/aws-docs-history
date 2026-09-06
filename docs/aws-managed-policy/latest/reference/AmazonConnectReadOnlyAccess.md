

# AmazonConnectReadOnlyAccess
<a name="AmazonConnectReadOnlyAccess"></a>

**Description**: Grants permission to view the Amazon Connect instances in your AWS account.

`AmazonConnectReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonConnectReadOnlyAccess-how-to-use"></a>

You can attach `AmazonConnectReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonConnectReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 17, 2018, 21:00 UTC 
+ **Edited time:** June 19, 2024, 15:15 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonConnectReadOnlyAccess`

## Policy version
<a name="AmazonConnectReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonConnectReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowConnectReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "connect:Get*",
        "connect:Describe*",
        "connect:List*",
        "ds:DescribeDirectories"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "DenyConnectEmergencyAccess",
      "Effect" : "Deny",
      "Action" : "connect:AdminGetEmergencyAccessToken",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonConnectReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)