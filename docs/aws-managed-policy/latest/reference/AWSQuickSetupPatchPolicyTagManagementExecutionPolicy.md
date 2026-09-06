

# AWSQuickSetupPatchPolicyTagManagementExecutionPolicy
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy"></a>

**Description**: Grants permissions to track which instances are managed by Quick Setup patch policy configurations through automated tagging and inventory collection.

`AWSQuickSetupPatchPolicyTagManagementExecutionPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy-how-to-use"></a>

You can attach `AWSQuickSetupPatchPolicyTagManagementExecutionPolicy` to your users, groups, and roles.

## Policy details
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 03, 2026, 14:12 UTC 
+ **Edited time:** June 03, 2026, 14:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSQuickSetupPatchPolicyTagManagementExecutionPolicy`

## Policy version
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "GetSSMInventory",
      "Effect" : "Allow",
      "Action" : [
        "ssm:GetInventory"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ManageSSMManagedInstanceTags",
      "Effect" : "Allow",
      "Action" : [
        "ssm:AddTagsToResource",
        "ssm:RemoveTagsFromResource"
      ],
      "Resource" : "arn:aws:ssm:*:*:managed-instance/*",
      "Condition" : {
        "ForAllValues:StringLike" : {
          "aws:TagKeys" : "QSConfigName-*"
        },
        "ForAnyValue:StringLike" : {
          "aws:TagKeys" : "QSConfigName-*"
        }
      }
    },
    {
      "Sid" : "ManageEC2InstanceTags",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateTags",
        "ec2:DeleteTags"
      ],
      "Resource" : "arn:aws:ec2:*:*:instance/*",
      "Condition" : {
        "ForAllValues:StringLike" : {
          "aws:TagKeys" : "QSConfigName-*"
        },
        "ForAnyValue:StringLike" : {
          "aws:TagKeys" : "QSConfigName-*"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSQuickSetupPatchPolicyTagManagementExecutionPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)