

# AWSXrayFullAccess
<a name="AWSXrayFullAccess"></a>

**Description**: AWS X-Ray full access managed policy

`AWSXrayFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSXrayFullAccess-how-to-use"></a>

You can attach `AWSXrayFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSXrayFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: December 01, 2016, 18:30 UTC 
+ **Edited time:** April 11, 2024, 17:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSXrayFullAccess`

## Policy version
<a name="AWSXrayFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSXrayFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AWSXrayFullAccess",
      "Effect" : "Allow",
      "Action" : [
        "xray:*"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSXrayFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)