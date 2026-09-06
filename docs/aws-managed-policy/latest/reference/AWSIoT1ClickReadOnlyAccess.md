

# AWSIoT1ClickReadOnlyAccess
<a name="AWSIoT1ClickReadOnlyAccess"></a>

**Description**: Provides read only access to AWS IoT 1-Click.

`AWSIoT1ClickReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoT1ClickReadOnlyAccess-how-to-use"></a>

You can attach `AWSIoT1ClickReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSIoT1ClickReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 11, 2018, 21:49 UTC 
+ **Edited time:** May 11, 2018, 21:49 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSIoT1ClickReadOnlyAccess`

## Policy version
<a name="AWSIoT1ClickReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoT1ClickReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "iot1click:Describe*",
        "iot1click:Get*",
        "iot1click:List*"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSIoT1ClickReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)