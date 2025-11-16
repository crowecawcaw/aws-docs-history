# Restore a backup by resource type

## How to restore

For console restore instructions and links to documentation for each AWS Backup-supported
resource type, see the links at the bottom of this page.

To restore a backup programmatically, use the [StartRestoreJob](API_StartRestoreJob.md "API_StartRestoreJob.md") API operation.

The configuration values ("restore metadata") that you need to restore your resource
varies depending on the resource that you want to restore. To get the configuration metadata
that your backup was created with, you can call [GetRecoveryPointRestoreMetadata](API_GetRecoveryPointRestoreMetadata.md "API_GetRecoveryPointRestoreMetadata.md"). Restore metadata examples are also
available in the links at the bottom of this page.

Restoring from cold storage typically takes 4 hours more than restoring from warm
storage.

For each restore, a restore job is created with a unique job ID—for example,
`1323657E-2AA4-1D94-2C48-5D7A423E7394`.

###### Note

AWS Backup does not provide any service-level agreements (SLAs) for a restore time. Restore
times can vary based upon system load and capacity, even for restores containing the same
resources.

## Non-destructive restores

When you use AWS Backup to restore a backup, it creates a new resource with the backup that
you are restoring. This is to protect your existing resources from being destroyed by your
restore activity.

## Restore testing

You can conduct tests on your resources to simulate a restore experience. This helps
determine if you meet your organizational Restore Time Objective (RTO) and helps prepare for
future restore needs.

For more information, see [Restore testing](restore-testing.md "restore-testing.md").

## Copy tags during a restore

###### Note

Restores of Amazon DynamoDB, Amazon S3, SAP HANA on Amazon EC2 instances, virtual machines, and
Amazon Timestream resources currently do not have this feature available.

### Introduction

You can copy tags as you restore a resource if the tags belonged to the protected
resource at the time of backup. Tags, which are labels containing a key and value pair,
can help you identify and search for resources. When you start a restore job, tags that
belonged to the original backed-up resources can be added to the resource being
restored.

When you choose to include tags during a restore job, this step can replace the
overhead and labor of manually applying tags to resources after a restore job is
completed. Note this is distinct from adding new tags to restored resources.

When you restore a backup in the console flow, your source tags will be copied by
default. In the console, uncheck the box if you wish to opt out of copying tags to a
restored resource

In the API operation `StartRestoreJob`, the parameter
`CopySourceTagsToRestoredResource` is set to `false` by default,
which will exclude the original source tags from the resource you are restoring. If you
wish to _include_ tags from the original source, set this to
`True`.

### Considerations

- A resource can have up to 50 tags, including restored resources. Please see [Tagging your
  AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") for more information about tag limits.
- Ensure the correct permissions are present in the role used for restores to copy
  tags. The default role for restores contains the necessary permissions. A custom role
  must include additional permissions to tag resources.
- The following resources are not currently supported for restore tag inclusion:
  VMware Cloud™ on AWS, VMware Cloud™ on AWS Outposts, on-premises systems, SAP HANA on
  Amazon EC2 instances, Timestream, DynamoDB, Advanced DynamoDB, and Amazon S3.
- For continuous backups, the tags on the original resource as of the most recent
  backup will be copied to the restored resource.
- Tags will not be copied for item-level restores.
- Tags that were added to a backup after the backup job was completed but were not
  present on the original resource prior to the backup will not be copied to the
  restored resource. Only Backups created after May 22, 2023 are eligible for tag copy
  on restore.

- **Amazon EC2**
  - Tags applied to restored **Amazon EC2** instances are also
    applied to the attached restored **Amazon EBS** volumes.
  - Tags applied to the EBS volumes attached to source instances are not copied
    to the volumes attached to restored instances. If you have IAM policies that
    allow or deny users access to EBS volumes based on their tags, you must manually
    reassign the required tags to the restored volumes to ensure your policies
    remain in effect.

- When you restore an **Amazon EFS** resource, it must be copied to a
  new file system. Restorations to an existing file system cannot have tags copied to
  it.
- **Amazon RDS**
  - If the RDS cluster that was backed up is still active, tags from this
    cluster will be copied.
  - If the original cluster is no longer active, tags from the snapshot of the
    cluster will be copied instead.
  - Tags which were present on the resource at the time of the backup will be
    copied during the restore regardless if the Boolean parameter for
    `CopySourceTagsToRestoredResource` is set to `True` or
    `False`. However, if the snapshot does not contain tags, then the
    above Boolean setting will be used.

- **Amazon Redshift** clusters, by default, always include tags during a
  restore job.

### Copy tags via the console

1. Open the [AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/")
2. In the navigation pane, choose **Protected resources**, and
   select the Amazon S3 resource ID that you want to restore.
3. On the **Resource details** page, you will see a list of recovery
   points for the selected resource ID. To restore a resource:
   1. In the **Backup** pane, choose the recovery point ID of the
      resource.
   2. In the upper-right corner of the pane, choose **Restore**
      (alternatively, you can go to the backup vault, find the recovery point, and then
      click **Actions** then click
      **Restore**).

4. On the **Restore backup page**, locate the panel named Restore
   with tags. To include all tags from the original resource, retain the check the box
   (note in the console this box is checked by default).
5. Click **Restore backup** after you have selected all your
   preferred settings and roles.

### To include tags programmatically

Use the API operation `StartRestoreJob` . Ensure the following Boolean
parameter is set to `True`:

```
CopySourceTagsToRestoredResource = true
```

If the boolean parameter `CopySourceTagsToRestoredResource` =
`True`, the restore job will copy the tags from the original resource(s) to
the restored material.

###### Important

The restore job will fail if this parameter is included for an unsupported resource
(VMware, AWS Outposts, on-premises systems, SAP HANA on EC2 instances, Timestream, DynamoDB,
Advanced DynamoDB, and Amazon S3).

```
{
    "RecoveryPointArn": "arn:aws:ec2:us-east-1::image/ami-1234567890a1b234",
    "Metadata": {
        "InstanceInitiatedShutdownBehavior": "stop",
        "DisableApiTermination": "false",
        "EbsOptimized": "false",
        "InstanceType": "t1.micro",
        "SubnetId": "subnet-123ab456cd7efgh89",
        "SecurityGroupIds": "[\"sg-0a1bc2d345ef67890\"]",
        "Placement": "{\"GroupName\":null,\"Tenancy\":\"default\"}",
        "HibernationOptions": "{\"Configured\":false}",
        "IamInstanceProfileName": "UseBackedUpValue",
        "aws:backup:request-id": "1a2345b6-cd78-90e1-2345-67f890g1h2ij"
    },
    "IamRoleArn": "arn:aws:iam::123456789012:role/EC2Restore",
    "ResourceType": "EC2",
    "IdempotencyToken": "34ab5678-9012-3c4d-5678-efg9h01f23i4",
    "CopySourceTagsToRestoredResource": true
}
```

### Troubleshoot tag restore issues

**ERROR:** Insufficient Permissions

**REMEDY:** Ensure you have the necessary permissions in your restore
role so you can include tags on your restored resource. The default [AWS
managed](security-iam-awsmanpol.md#aws-managed-policies "security-iam-awsmanpol.md#aws-managed-policies") service role policy for restores, [AWSBackupServiceRolePolicyForRestores](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores$jsonEditor"), contains the necessary permissions for
this task.

If you choose to use a custom role, ensure the following permissions are
present:

- `elasticfilesystem:TagResource`
- `storagegateway:AddTagsToResource`
- `rds:AddTagsToResource`
- `ec2:CreateTags`
- `cloudformation:TagResource`

For more information, see [API
permissions](access-control.md#backup-api-permissions-ref "access-control.md#backup-api-permissions-ref").

## Restore job statuses

You can view the status of a restore job on the **Jobs** page of the
AWS Backup console. Restore job statuses include **pending**,
**running**, **completed**,
**aborted**, and **failed**.

###### Topics

- [Restoring an Amazon Aurora cluster](restoring-aur.md "restoring-aur.md")
- [Amazon Aurora DSQL restore](restore-auroradsql.md "restore-auroradsql.md")
- [Restore CloudFormation stacks](restore-application-stacks.md "restore-application-stacks.md")
- [Restoring a DocumentDB cluster](restoring-docdb.md "restoring-docdb.md")
- [Restore a Amazon DynamoDB table](restoring-dynamodb.md "restoring-dynamodb.md")
- [Restore an Amazon EBS volume](restoring-ebs.md "restoring-ebs.md")
- [Restore an Amazon EC2 instance](restoring-ec2.md "restoring-ec2.md")
- [Restore an Amazon EFS file system](restoring-efs.md "restoring-efs.md")
- [Restore an Amazon EKS cluster](restoring-eks.md "restoring-eks.md")
- [Restore an FSx file system](restoring-fsx.md "restoring-fsx.md")
- [Restore a Neptune cluster](restoring-nep.md "restoring-nep.md")
- [Restore an RDS database](restoring-rds.md "restoring-rds.md")
- [Restore an Amazon Redshift cluster](redshift-restores.md "redshift-restores.md")
- [Amazon Redshift Serverless restore](redshift-serverless-restore.md "redshift-serverless-restore.md")
- [Restore an SAP HANA database on an Amazon EC2 instance](saphana-restore.md "saphana-restore.md")
- [Restore S3 data using AWS Backup](restoring-s3.md "restoring-s3.md")
- [Restore a Storage Gateway volume](restoring-storage-gateway.md "restoring-storage-gateway.md")
- [Restore an Amazon Timestream table](timestream-restore.md "timestream-restore.md")
- [Restore a virtual machine using AWS Backup](restoring-vm.md "restoring-vm.md")
