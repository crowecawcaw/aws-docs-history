

# AWSElasticBeanstalkRoleWorkerTier
<a name="AWSElasticBeanstalkRoleWorkerTier"></a>

**Description**: (Elastic Beanstalk operations role) Allows a worker environment tier to create an Amazon DynamoDB table and an Amazon SQS queue.

`AWSElasticBeanstalkRoleWorkerTier` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSElasticBeanstalkRoleWorkerTier-how-to-use"></a>

You can attach `AWSElasticBeanstalkRoleWorkerTier` to your users, groups, and roles.

## Policy details
<a name="AWSElasticBeanstalkRoleWorkerTier-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: June 05, 2020, 21:43 UTC 
+ **Edited time:** June 05, 2020, 21:43 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkRoleWorkerTier`

## Policy version
<a name="AWSElasticBeanstalkRoleWorkerTier-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSElasticBeanstalkRoleWorkerTier-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowSQS",
      "Effect" : "Allow",
      "Action" : [
        "sqs:TagQueue",
        "sqs:DeleteQueue",
        "sqs:GetQueueAttributes",
        "sqs:CreateQueue"
      ],
      "Resource" : "arn:aws:sqs:*:*:awseb-e-*"
    },
    {
      "Sid" : "AllowDDB",
      "Effect" : "Allow",
      "Action" : [
        "dynamodb:CreateTable",
        "dynamodb:TagResource",
        "dynamodb:DescribeTable",
        "dynamodb:DeleteTable"
      ],
      "Resource" : "arn:aws:dynamodb:*:*:table/awseb-e-*"
    }
  ]
}
```

## Learn more
<a name="AWSElasticBeanstalkRoleWorkerTier-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)