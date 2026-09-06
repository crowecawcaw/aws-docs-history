

# AWSPanoramaSageMakerRolePolicy
<a name="AWSPanoramaSageMakerRolePolicy"></a>

**Description**: Allows Amazon SageMaker to manage objects in buckets created for use with AWS Panorama.

`AWSPanoramaSageMakerRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPanoramaSageMakerRolePolicy-how-to-use"></a>

You can attach `AWSPanoramaSageMakerRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSPanoramaSageMakerRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: December 01, 2020, 13:13 UTC 
+ **Edited time:** December 01, 2020, 13:13 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSPanoramaSageMakerRolePolicy`

## Policy version
<a name="AWSPanoramaSageMakerRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPanoramaSageMakerRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PanoramaSageMakerS3Access",
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject",
        "s3:PutObject",
        "s3:GetBucket*"
      ],
      "Resource" : [
        "arn:aws:s3:::*aws-panorama*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSPanoramaSageMakerRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)