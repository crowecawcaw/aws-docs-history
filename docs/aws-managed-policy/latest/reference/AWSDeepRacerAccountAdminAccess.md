

# AWSDeepRacerAccountAdminAccess
<a name="AWSDeepRacerAccountAdminAccess"></a>

**Description**: DeepRacer admin access to all actions including toggling between multiuser and single user mode.

`AWSDeepRacerAccountAdminAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSDeepRacerAccountAdminAccess-how-to-use"></a>

You can attach `AWSDeepRacerAccountAdminAccess` to your users, groups, and roles.

## Policy details
<a name="AWSDeepRacerAccountAdminAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: October 28, 2021, 01:27 UTC 
+ **Edited time:** October 28, 2021, 01:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSDeepRacerAccountAdminAccess`

## Policy version
<a name="AWSDeepRacerAccountAdminAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSDeepRacerAccountAdminAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DeepRacerAdminAccessStatement",
      "Effect" : "Allow",
      "Action" : [
        "deepracer:*"
      ],
      "Resource" : [
        "*"
      ],
      "Condition" : {
        "Null" : {
          "deepracer:UserToken" : "true"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSDeepRacerAccountAdminAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)