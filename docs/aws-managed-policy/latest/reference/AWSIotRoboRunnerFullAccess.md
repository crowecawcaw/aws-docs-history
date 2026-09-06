

# AWSIotRoboRunnerFullAccess
<a name="AWSIotRoboRunnerFullAccess"></a>

**Description**: This policy grants permissions that allow full access to AWS Iot RoboRunner.

`AWSIotRoboRunnerFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIotRoboRunnerFullAccess-how-to-use"></a>

You can attach `AWSIotRoboRunnerFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSIotRoboRunnerFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 29, 2021, 03:54 UTC 
+ **Edited time:** February 23, 2023, 18:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSIotRoboRunnerFullAccess`

## Policy version
<a name="AWSIotRoboRunnerFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIotRoboRunnerFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "iotroborunner:*",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/iotroborunner.amazonaws.com/AWSServiceRoleForIoTRoboRunner",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "iotroborunner.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSIotRoboRunnerFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)