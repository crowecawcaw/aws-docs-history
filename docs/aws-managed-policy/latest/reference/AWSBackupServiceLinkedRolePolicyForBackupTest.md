

# AWSBackupServiceLinkedRolePolicyForBackupTest
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest"></a>

**Description**: Provides AWS Backup permission to create backups on your behalf across AWS services

`AWSBackupServiceLinkedRolePolicyForBackupTest` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: May 12, 2020, 17:37 UTC 
+ **Edited time:** May 12, 2020, 17:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSBackupServiceLinkedRolePolicyForBackupTest`

## Policy version
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "elasticfilesystem:Backup",
        "elasticfilesystem:DescribeTags"
      ],
      "Resource" : "arn:aws:elasticfilesystem:*:*:file-system/*",
      "Effect" : "Allow",
      "Condition" : {
        "StringLike" : {
          "aws:ResourceTag/aws:elasticfilesystem:default-backup" : "enabled"
        }
      }
    },
    {
      "Action" : [
        "tag:GetResources"
      ],
      "Resource" : "*",
      "Effect" : "Allow"
    }
  ]
}
```

## Learn more
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)