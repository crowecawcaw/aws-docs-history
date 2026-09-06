

# AWSManagedServiceAccessManagementAccess
<a name="AWSManagedServiceAccessManagementAccess"></a>

**Description**: Grants permissions to manage Service Control Policies (SCPs) in AWS Organizations for the AWS Managed Service Access Management service. Includes permissions to list, create, update, and attach SCPs scoped to policies tagged with ManagedBy=service-access.

`AWSManagedServiceAccessManagementAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSManagedServiceAccessManagementAccess-how-to-use"></a>

You can attach `AWSManagedServiceAccessManagementAccess` to your users, groups, and roles.

## Policy details
<a name="AWSManagedServiceAccessManagementAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: July 21, 2026, 17:57 UTC 
+ **Edited time:** July 21, 2026, 17:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSManagedServiceAccessManagementAccess`

## Policy version
<a name="AWSManagedServiceAccessManagementAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSManagedServiceAccessManagementAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowListRoots",
      "Effect" : "Allow",
      "Action" : "organizations:ListRoots",
      "Resource" : "*"
    },
    {
      "Sid" : "AllowSCPList",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListPolicies",
        "organizations:ListPoliciesForTarget"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY"
        }
      }
    },
    {
      "Sid" : "AllowSCPCreateWithTag",
      "Effect" : "Allow",
      "Action" : [
        "organizations:CreatePolicy",
        "organizations:TagResource"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY",
          "aws:RequestTag/ManagedBy" : "service-access"
        }
      }
    },
    {
      "Sid" : "AllowSCPUpdateTagged",
      "Effect" : "Allow",
      "Action" : "organizations:UpdatePolicy",
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedBy" : "service-access"
        }
      }
    },
    {
      "Sid" : "AllowSCPAttachTaggedPolicy",
      "Effect" : "Allow",
      "Action" : "organizations:AttachPolicy",
      "Resource" : "arn:aws:organizations::*:policy/*/service_control_policy/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedBy" : "service-access"
        }
      }
    },
    {
      "Sid" : "AllowSCPAttachRoot",
      "Effect" : "Allow",
      "Action" : "organizations:AttachPolicy",
      "Resource" : "arn:aws:organizations::*:root/*"
    }
  ]
}
```

## Learn more
<a name="AWSManagedServiceAccessManagementAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)