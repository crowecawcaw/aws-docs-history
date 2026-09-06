

# AWSIoTDataAccess
<a name="AWSIoTDataAccess"></a>

**Description**: This policy gives full access to the AWS IoT messaging actions

`AWSIoTDataAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIoTDataAccess-how-to-use"></a>

You can attach `AWSIoTDataAccess` to your users, groups, and roles.

## Policy details
<a name="AWSIoTDataAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 27, 2015, 21:51 UTC 
+ **Edited time:** June 23, 2021, 21:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSIoTDataAccess`

## Policy version
<a name="AWSIoTDataAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIoTDataAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "iot:Connect",
        "iot:Publish",
        "iot:Subscribe",
        "iot:Receive",
        "iot:GetThingShadow",
        "iot:UpdateThingShadow",
        "iot:DeleteThingShadow",
        "iot:ListNamedShadowsForThing"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSIoTDataAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)