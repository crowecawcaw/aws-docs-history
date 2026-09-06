

# AWSCodeDeployRoleForLambdaLimited
<a name="AWSCodeDeployRoleForLambdaLimited"></a>

**Description**: Provides CodeDeploy service limited access to perform a Lambda deployment on your behalf.

`AWSCodeDeployRoleForLambdaLimited` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCodeDeployRoleForLambdaLimited-how-to-use"></a>

You can attach `AWSCodeDeployRoleForLambdaLimited` to your users, groups, and roles.

## Policy details
<a name="AWSCodeDeployRoleForLambdaLimited-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: August 17, 2020, 17:14 UTC 
+ **Edited time:** August 17, 2020, 17:14 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSCodeDeployRoleForLambdaLimited`

## Policy version
<a name="AWSCodeDeployRoleForLambdaLimited-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCodeDeployRoleForLambdaLimited-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "cloudwatch:DescribeAlarms",
        "lambda:UpdateAlias",
        "lambda:GetAlias",
        "lambda:GetProvisionedConcurrencyConfig"
      ],
      "Resource" : "*",
      "Effect" : "Allow"
    },
    {
      "Action" : [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource" : "arn:aws:s3:::*/CodeDeploy/*",
      "Effect" : "Allow"
    },
    {
      "Action" : [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "s3:ExistingObjectTag/UseWithCodeDeploy" : "true"
        }
      },
      "Effect" : "Allow"
    },
    {
      "Action" : [
        "lambda:InvokeFunction"
      ],
      "Resource" : "arn:aws:lambda:*:*:function:CodeDeployHook_*",
      "Effect" : "Allow"
    }
  ]
}
```

## Learn more
<a name="AWSCodeDeployRoleForLambdaLimited-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)