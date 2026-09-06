

# AWSCloudFormationFullAccess
<a name="AWSCloudFormationFullAccess"></a>

**Description**: Provides full access to AWS CloudFormation.

`AWSCloudFormationFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCloudFormationFullAccess-how-to-use"></a>

You can attach `AWSCloudFormationFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSCloudFormationFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 26, 2019, 21:50 UTC 
+ **Edited time:** July 26, 2019, 21:50 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCloudFormationFullAccess`

## Policy version
<a name="AWSCloudFormationFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCloudFormationFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSCloudFormationFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)