

# AmazonEC2RoleforAWSCodeDeployLimited
<a name="AmazonEC2RoleforAWSCodeDeployLimited"></a>

**Description**: Provides EC2 limited access to S3 bucket to download revision. This role is needed by the CodeDeploy agent on EC2 instances. 

`AmazonEC2RoleforAWSCodeDeployLimited` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEC2RoleforAWSCodeDeployLimited-how-to-use"></a>

You can attach `AmazonEC2RoleforAWSCodeDeployLimited` to your users, groups, and roles.

## Policy details
<a name="AmazonEC2RoleforAWSCodeDeployLimited-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 24, 2020, 17:55 UTC 
+ **Edited time:** January 20, 2022, 21:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforAWSCodeDeployLimited`

## Policy version
<a name="AmazonEC2RoleforAWSCodeDeployLimited-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEC2RoleforAWSCodeDeployLimited-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket"
      ],
      "Resource" : "arn:aws:s3:::*/CodeDeploy/*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "s3:ExistingObjectTag/UseWithCodeDeploy" : "true"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonEC2RoleforAWSCodeDeployLimited-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)