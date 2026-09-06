

# QuickSightAccessForS3StorageManagementAnalyticsReadOnly
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly"></a>

**Description**: Policy used by QuickSight team to access customer data produced by S3 Storage Management Analytics.

`QuickSightAccessForS3StorageManagementAnalyticsReadOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly-how-to-use"></a>

You can attach `QuickSightAccessForS3StorageManagementAnalyticsReadOnly` to your users, groups, and roles.

## Policy details
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: June 12, 2017, 18:18 UTC 
+ **Edited time:** October 08, 2019, 23:53 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/QuickSightAccessForS3StorageManagementAnalyticsReadOnly`

## Policy version
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject"
      ],
      "Resource" : [
        "arn:aws:s3:::s3-analytics-export-shared-*"
      ]
    },
    {
      "Action" : [
        "s3:GetAnalyticsConfiguration",
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="QuickSightAccessForS3StorageManagementAnalyticsReadOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)