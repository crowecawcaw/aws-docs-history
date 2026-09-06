

# AWSElementalMediaTailorReadOnly
<a name="AWSElementalMediaTailorReadOnly"></a>

**Description**: Provides read only access to AWS Elemental MediaTailor resources

`AWSElementalMediaTailorReadOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElementalMediaTailorReadOnly-how-to-use"></a>

You can attach `AWSElementalMediaTailorReadOnly` to your users, groups, and roles.

## Policy details
<a name="AWSElementalMediaTailorReadOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 23, 2021, 00:05 UTC 
+ **Edited time:** November 23, 2021, 00:05 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSElementalMediaTailorReadOnly`

## Policy version
<a name="AWSElementalMediaTailorReadOnly-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElementalMediaTailorReadOnly-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : [
      "mediatailor:List*",
      "mediatailor:Describe*",
      "mediatailor:Get*"
    ],
    "Resource" : "*"
  }
}
```

## Learn more
<a name="AWSElementalMediaTailorReadOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)