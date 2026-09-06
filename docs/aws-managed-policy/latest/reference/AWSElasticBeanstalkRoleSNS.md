

# AWSElasticBeanstalkRoleSNS
<a name="AWSElasticBeanstalkRoleSNS"></a>

**Description**: (Elastic Beanstalk operations role) Allows an environment to enable Amazon SNS topic integration.

`AWSElasticBeanstalkRoleSNS` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElasticBeanstalkRoleSNS-how-to-use"></a>

You can attach `AWSElasticBeanstalkRoleSNS` to your users, groups, and roles.

## Policy details
<a name="AWSElasticBeanstalkRoleSNS-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: June 05, 2020, 21:46 UTC 
+ **Edited time:** June 05, 2020, 21:46 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkRoleSNS`

## Policy version
<a name="AWSElasticBeanstalkRoleSNS-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElasticBeanstalkRoleSNS-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowBeanstalkManageSNS",
      "Effect" : "Allow",
      "Action" : [
        "sns:CreateTopic",
        "sns:SetTopicAttributes",
        "sns:DeleteTopic"
      ],
      "Resource" : [
        "arn:aws:sns:*:*:ElasticBeanstalkNotifications-*"
      ]
    },
    {
      "Sid" : "AllowSNSPublish",
      "Effect" : "Allow",
      "Action" : [
        "sns:GetTopicAttributes",
        "sns:Subscribe",
        "sns:Unsubscribe",
        "sns:Publish"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSElasticBeanstalkRoleSNS-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)