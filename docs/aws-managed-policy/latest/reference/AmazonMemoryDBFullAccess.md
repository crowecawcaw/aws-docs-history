

# AmazonMemoryDBFullAccess
<a name="AmazonMemoryDBFullAccess"></a>

**Description**: Provides full access to Amazon MemoryDB via the AWS Management Console.

`AmazonMemoryDBFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonMemoryDBFullAccess-how-to-use"></a>

You can attach `AmazonMemoryDBFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonMemoryDBFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 08, 2021, 19:24 UTC 
+ **Edited time:** October 08, 2021, 19:24 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonMemoryDBFullAccess`

## Policy version
<a name="AmazonMemoryDBFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonMemoryDBFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "memorydb:*",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/memorydb.amazonaws.com/AWSServiceRoleForMemoryDB",
      "Condition" : {
        "StringLike" : {
          "iam:AWSServiceName" : "memorydb.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonMemoryDBFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)