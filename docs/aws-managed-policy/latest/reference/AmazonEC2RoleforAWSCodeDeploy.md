

# AmazonEC2RoleforAWSCodeDeploy
<a name="AmazonEC2RoleforAWSCodeDeploy"></a>

**Description**: Provides EC2 access to S3 bucket to download revision. This role is needed by the CodeDeploy agent on EC2 instances.

`AmazonEC2RoleforAWSCodeDeploy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonEC2RoleforAWSCodeDeploy-how-to-use"></a>

You can attach `AmazonEC2RoleforAWSCodeDeploy` to your users, groups, and roles.

## Policy details
<a name="AmazonEC2RoleforAWSCodeDeploy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: May 19, 2015, 18:10 UTC 
+ **Edited time:** March 20, 2017, 17:14 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforAWSCodeDeploy`

## Policy version
<a name="AmazonEC2RoleforAWSCodeDeploy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonEC2RoleforAWSCodeDeploy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonEC2RoleforAWSCodeDeploy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)