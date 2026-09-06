

# AWSElementalMediaConvertFullAccess
<a name="AWSElementalMediaConvertFullAccess"></a>

**Description**: Provides full access to AWS Elemental MediaConvert via the AWS Management Console and SDK.

`AWSElementalMediaConvertFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElementalMediaConvertFullAccess-how-to-use"></a>

You can attach `AWSElementalMediaConvertFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSElementalMediaConvertFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 25, 2018, 19:25 UTC 
+ **Edited time:** June 10, 2019, 22:52 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSElementalMediaConvertFullAccess`

## Policy version
<a name="AWSElementalMediaConvertFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElementalMediaConvertFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "mediaconvert:*",
        "s3:ListAllMyBuckets",
        "s3:ListBucket"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:PassRole"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringLike" : {
          "iam:PassedToService" : [
            "mediaconvert.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSElementalMediaConvertFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)