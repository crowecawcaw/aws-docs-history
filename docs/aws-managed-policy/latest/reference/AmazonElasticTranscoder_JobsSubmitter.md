

# AmazonElasticTranscoder\_JobsSubmitter
<a name="AmazonElasticTranscoder_JobsSubmitter"></a>

**Description**: Grants users permission to change presets, submit jobs, and view Elastic Transcoder settings. This policy also grants some read-only access to some other services required to use the Elastic Transcode console, including S3, IAM, and SNS.

`AmazonElasticTranscoder_JobsSubmitter` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonElasticTranscoder_JobsSubmitter-how-to-use"></a>

You can attach `AmazonElasticTranscoder_JobsSubmitter` to your users, groups, and roles.

## Policy details
<a name="AmazonElasticTranscoder_JobsSubmitter-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 07, 2018, 21:12 UTC 
+ **Edited time:** June 10, 2019, 22:49 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonElasticTranscoder_JobsSubmitter`

## Policy version
<a name="AmazonElasticTranscoder_JobsSubmitter-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonElasticTranscoder_JobsSubmitter-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "elastictranscoder:Read*",
        "elastictranscoder:List*",
        "elastictranscoder:*Job",
        "elastictranscoder:*Preset",
        "s3:ListAllMyBuckets",
        "s3:ListBucket",
        "iam:ListRoles",
        "sns:ListTopics"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonElasticTranscoder_JobsSubmitter-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)