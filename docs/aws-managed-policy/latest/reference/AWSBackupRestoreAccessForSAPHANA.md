

# AWSBackupRestoreAccessForSAPHANA
<a name="AWSBackupRestoreAccessForSAPHANA"></a>

**Description**: Provides AWS Backup permission to restore a backup of SAP HANA on Amazon EC2

`AWSBackupRestoreAccessForSAPHANA` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSBackupRestoreAccessForSAPHANA-how-to-use"></a>

You can attach `AWSBackupRestoreAccessForSAPHANA` to your users, groups, and roles.

## Policy details
<a name="AWSBackupRestoreAccessForSAPHANA-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 10, 2022, 22:43 UTC 
+ **Edited time:** November 10, 2022, 22:43 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSBackupRestoreAccessForSAPHANA`

## Policy version
<a name="AWSBackupRestoreAccessForSAPHANA-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSBackupRestoreAccessForSAPHANA-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "backup:Get*",
        "backup:List*",
        "backup:Describe*",
        "backup:StartBackupJob",
        "backup:StartRestoreJob"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ssm-sap:GetOperation",
        "ssm-sap:ListDatabases"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ssm-sap:BackupDatabase",
        "ssm-sap:RestoreDatabase",
        "ssm-sap:UpdateHanaBackupSettings",
        "ssm-sap:GetDatabase",
        "ssm-sap:ListTagsForResource"
      ],
      "Resource" : "arn:aws:ssm-sap:*:*:*"
    }
  ]
}
```

## Learn more
<a name="AWSBackupRestoreAccessForSAPHANA-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)