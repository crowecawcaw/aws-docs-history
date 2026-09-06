

# AmazonElasticFileSystemClientFullAccess
<a name="AmazonElasticFileSystemClientFullAccess"></a>

**Description**: Provides root client access to an Amazon EFS file system

`AmazonElasticFileSystemClientFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonElasticFileSystemClientFullAccess-how-to-use"></a>

You can attach `AmazonElasticFileSystemClientFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonElasticFileSystemClientFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 13, 2020, 16:27 UTC 
+ **Edited time:** January 13, 2020, 16:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonElasticFileSystemClientFullAccess`

## Policy version
<a name="AmazonElasticFileSystemClientFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonElasticFileSystemClientFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "elasticfilesystem:ClientMount",
        "elasticfilesystem:ClientRootAccess",
        "elasticfilesystem:ClientWrite",
        "elasticfilesystem:DescribeMountTargets"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonElasticFileSystemClientFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)