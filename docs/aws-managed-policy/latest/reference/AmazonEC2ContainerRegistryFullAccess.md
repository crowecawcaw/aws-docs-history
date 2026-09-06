

# AmazonEC2ContainerRegistryFullAccess
<a name="AmazonEC2ContainerRegistryFullAccess"></a>

**Description**: Provides administrative access to Amazon ECR resources

`AmazonEC2ContainerRegistryFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEC2ContainerRegistryFullAccess-how-to-use"></a>

You can attach `AmazonEC2ContainerRegistryFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonEC2ContainerRegistryFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 21, 2015, 17:06 UTC 
+ **Edited time:** December 05, 2020, 00:04 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess`

## Policy version
<a name="AmazonEC2ContainerRegistryFullAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEC2ContainerRegistryFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr:*",
        "cloudtrail:LookupEvents"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : [
            "replication.ecr.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonEC2ContainerRegistryFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)