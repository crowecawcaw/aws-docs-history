

# AWSIoTRuleActions
<a name="AWSIoTRuleActions"></a>

**Description**: Allows access to all AWS services supported in AWS IoT Rule Actions

`AWSIoTRuleActions` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoTRuleActions-how-to-use"></a>

You can attach `AWSIoTRuleActions` to your users, groups, and roles.

## Policy details
<a name="AWSIoTRuleActions-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: October 08, 2015, 15:14 UTC 
+ **Edited time:** January 16, 2018, 19:28 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSIoTRuleActions`

## Policy version
<a name="AWSIoTRuleActions-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoTRuleActions-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : {
    "Effect" : "Allow",
    "Action" : [
      "dynamodb:PutItem",
      "kinesis:PutRecord",
      "iot:Publish",
      "s3:PutObject",
      "sns:Publish",
      "sqs:SendMessage*",
      "cloudwatch:SetAlarmState",
      "cloudwatch:PutMetricData",
      "es:ESHttpPut",
      "firehose:PutRecord"
    ],
    "Resource" : "*"
  }
}
```

## Learn more
<a name="AWSIoTRuleActions-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)