

# AWSDiscoveryContinuousExportFirehosePolicy
<a name="AWSDiscoveryContinuousExportFirehosePolicy"></a>

**Description**: Provides write access to AWS resources required for AWS Discovery Continuous Export

`AWSDiscoveryContinuousExportFirehosePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSDiscoveryContinuousExportFirehosePolicy-how-to-use"></a>

You can attach `AWSDiscoveryContinuousExportFirehosePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSDiscoveryContinuousExportFirehosePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 09, 2018, 18:29 UTC 
+ **Edited time:** June 08, 2021, 17:32 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSDiscoveryContinuousExportFirehosePolicy`

## Policy version
<a name="AWSDiscoveryContinuousExportFirehosePolicy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSDiscoveryContinuousExportFirehosePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "glue:GetTableVersions"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:AbortMultipartUpload",
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:PutObject"
      ],
      "Resource" : [
        "arn:aws:s3:::aws-application-discovery-service-*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:PutLogEvents"
      ],
      "Resource" : [
        "arn:aws:logs:*:*:log-group:/aws/application-discovery-service/firehose:log-stream:*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSDiscoveryContinuousExportFirehosePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)