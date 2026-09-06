

# AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync"></a>

**Description**: Provides AWS BackupGateway permission to sync the metadata of Virtual Machines on your behalf

`AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync-how-to-use"></a>

You can attach `AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync` to your users, groups, and roles.

## Policy details
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: December 15, 2022, 19:43 UTC 
+ **Edited time:** December 15, 2022, 19:43 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync`

## Policy version
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ListVmTags",
      "Effect" : "Allow",
      "Action" : [
        "backup-gateway:ListTagsForResource"
      ],
      "Resource" : "arn:aws:backup-gateway:*:*:vm/*"
    },
    {
      "Sid" : "VMTagPermissions",
      "Effect" : "Allow",
      "Action" : [
        "backup-gateway:TagResource",
        "backup-gateway:UntagResource"
      ],
      "Resource" : "arn:aws:backup-gateway:*:*:vm/*"
    }
  ]
}
```

## Learn more
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)