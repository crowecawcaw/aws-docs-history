

# AWSStepFunctionsFullAccess
<a name="AWSStepFunctionsFullAccess"></a>

**Description**: An access policy for providing a user/role/etc access to the AWS StepFunctions API. For full access, in addition to this policy, a user MUST have iam:PassRole permission on at least one IAM role that can be assumed by the service.

`AWSStepFunctionsFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSStepFunctionsFullAccess-how-to-use"></a>

You can attach `AWSStepFunctionsFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSStepFunctionsFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 11, 2017, 21:51 UTC 
+ **Edited time:** January 11, 2017, 21:51 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSStepFunctionsFullAccess`

## Policy version
<a name="AWSStepFunctionsFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSStepFunctionsFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "states:*",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSStepFunctionsFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)