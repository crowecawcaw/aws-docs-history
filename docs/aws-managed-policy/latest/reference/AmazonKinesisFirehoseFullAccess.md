

# AmazonKinesisFirehoseFullAccess
<a name="AmazonKinesisFirehoseFullAccess"></a>

**Description**: Provides full access to all Amazon Kinesis Firehose Delivery Streams.

`AmazonKinesisFirehoseFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonKinesisFirehoseFullAccess-how-to-use"></a>

You can attach `AmazonKinesisFirehoseFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonKinesisFirehoseFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 07, 2015, 18:45 UTC 
+ **Edited time:** October 07, 2015, 18:45 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonKinesisFirehoseFullAccess`

## Policy version
<a name="AmazonKinesisFirehoseFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonKinesisFirehoseFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "firehose:*"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonKinesisFirehoseFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)