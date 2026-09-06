

# AWSAppRunnerReadOnlyAccess
<a name="AWSAppRunnerReadOnlyAccess"></a>

**Description**: Grants permissions to list and view details about App Runner resources.

`AWSAppRunnerReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAppRunnerReadOnlyAccess-how-to-use"></a>

You can attach `AWSAppRunnerReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSAppRunnerReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 24, 2022, 21:24 UTC 
+ **Edited time:** February 24, 2022, 21:24 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSAppRunnerReadOnlyAccess`

## Policy version
<a name="AWSAppRunnerReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAppRunnerReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "apprunner:List*",
        "apprunner:Describe*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSAppRunnerReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)