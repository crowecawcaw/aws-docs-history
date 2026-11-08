

# AWSCODAPermissionsBoundary
<a name="AWSCODAPermissionsBoundary"></a>

**Description**: AWS CODA creates IAM roles for delegations, and uses this policy when creating these roles to define the boundary of their permissions.

`AWSCODAPermissionsBoundary` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCODAPermissionsBoundary-how-to-use"></a>

You can attach `AWSCODAPermissionsBoundary` to your users, groups, and roles.

## Policy details
<a name="AWSCODAPermissionsBoundary-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 06, 2026, 18:07 UTC 
+ **Edited time:** November 06, 2026, 18:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCODAPermissionsBoundary`

## Policy version
<a name="AWSCODAPermissionsBoundary-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCODAPermissionsBoundary-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "NotAction" : [
        "iam:CreateRole",
        "iam:CreateUser",
        "iam:DeleteRolePermissionsBoundary",
        "iam:PutRolePermissionsBoundary",
        "sts:AssumeRoot"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateRole",
        "iam:CreateUser",
        "iam:PutRolePermissionsBoundary"
      ],
      "Resource" : "*",
      "Condition" : {
        "ArnLike" : {
          "iam:PermissionsBoundary" : "arn:*:iam::aws:policy/AWSCODAPermissionsBoundary"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSCODAPermissionsBoundary-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)