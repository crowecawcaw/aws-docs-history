

# AmazonDMSRedshiftS3Role
<a name="AmazonDMSRedshiftS3Role"></a>

**Description**: Provides access to manage S3 settings for Redshift endpoints for DMS.

`AmazonDMSRedshiftS3Role` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonDMSRedshiftS3Role-how-to-use"></a>

You can attach `AmazonDMSRedshiftS3Role` to your users, groups, and roles.

## Policy details
<a name="AmazonDMSRedshiftS3Role-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: April 20, 2016, 17:05 UTC 
+ **Edited time:** July 08, 2019, 18:19 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonDMSRedshiftS3Role`

## Policy version
<a name="AmazonDMSRedshiftS3Role-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonDMSRedshiftS3Role-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:CreateBucket",
        "s3:ListBucket",
        "s3:DeleteBucket",
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:GetObjectVersion",
        "s3:GetBucketPolicy",
        "s3:PutBucketPolicy",
        "s3:GetBucketAcl",
        "s3:PutBucketVersioning",
        "s3:GetBucketVersioning",
        "s3:PutLifecycleConfiguration",
        "s3:GetLifecycleConfiguration",
        "s3:DeleteBucketPolicy"
      ],
      "Resource" : "arn:aws:s3:::dms-*"
    }
  ]
}
```

## Learn more
<a name="AmazonDMSRedshiftS3Role-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)