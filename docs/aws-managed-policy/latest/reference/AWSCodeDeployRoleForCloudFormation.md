

# AWSCodeDeployRoleForCloudFormation
<a name="AWSCodeDeployRoleForCloudFormation"></a>

**Description**: Provides CodeDeploy service access to invoke Lambda function on your behalf to perform blue/green deployment through CloudFormation.

`AWSCodeDeployRoleForCloudFormation` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCodeDeployRoleForCloudFormation-how-to-use"></a>

You can attach `AWSCodeDeployRoleForCloudFormation` to your users, groups, and roles.

## Policy details
<a name="AWSCodeDeployRoleForCloudFormation-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: May 19, 2020, 17:12 UTC 
+ **Edited time:** May 19, 2020, 17:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSCodeDeployRoleForCloudFormation`

## Policy version
<a name="AWSCodeDeployRoleForCloudFormation-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCodeDeployRoleForCloudFormation-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
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
<a name="AWSCodeDeployRoleForCloudFormation-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)