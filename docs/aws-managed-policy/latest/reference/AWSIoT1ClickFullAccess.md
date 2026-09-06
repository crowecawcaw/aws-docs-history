

# AWSIoT1ClickFullAccess
<a name="AWSIoT1ClickFullAccess"></a>

**Description**: Provides full access to AWS IoT 1-Click.

`AWSIoT1ClickFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoT1ClickFullAccess-how-to-use"></a>

You can attach `AWSIoT1ClickFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSIoT1ClickFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 11, 2018, 22:10 UTC 
+ **Edited time:** May 11, 2018, 22:10 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSIoT1ClickFullAccess`

## Policy version
<a name="AWSIoT1ClickFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoT1ClickFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "iot1click:*"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSIoT1ClickFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)