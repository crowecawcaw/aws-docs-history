

# AmazonESReadOnlyAccess
<a name="AmazonESReadOnlyAccess"></a>

**Description**: Provides read-only access to the Amazon ES configuration service.

`AmazonESReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonESReadOnlyAccess-how-to-use"></a>

You can attach `AmazonESReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonESReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 01, 2015, 19:18 UTC 
+ **Edited time:** October 03, 2018, 03:32 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonESReadOnlyAccess`

## Policy version
<a name="AmazonESReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonESReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "es:Describe*",
        "es:List*",
        "es:Get*"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonESReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)