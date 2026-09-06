

# Managed policies for AWS Backup
<a name="security-iam-awsmanpol"></a>

Managed policies are standalone identity-based policies that you can attach to multiple users, groups, and roles in your AWS account. When you attach a policy to a principal entity, you give the entity the permissions that are defined in the policy.

*AWS managed policies* are created and administered by AWS. You can't change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to.

*Customer managed policies* give you fine-grained controls to set access to backups in AWS Backup. For example, you can use them to give your database backup administrator access to Amazon RDS backups but not Amazon EFS ones.

For more information, see [Managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.

## AWS managed policies
<a name="aws-managed-policies"></a>

AWS Backup provides the following AWS managed policies for common use cases. These policies make it easier to define the right permissions and control access to your backups. There are two types of managed policies. One type is designed to be assigned to users to control their access to AWS Backup. The other type of managed policy is designed to be attached to roles that you pass to AWS Backup. The following table lists all the managed policies that AWS Backup provides and describes how they are defined. You can find these managed policies in the **Policies** section of the IAM console.

**Topics**
+ [AWSBackupAuditAccess](#AWSBackupAuditAccess)
+ [AWSBackupAccessPointOperatorAccess](#AWSBackupAccessPointOperatorAccess)
+ [AWSBackupDataTransferAccess](#AWSBackupDataTransferAccess)
+ [AWSBackupFullAccess](#AWSBackupFullAccess)
+ [AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync](#AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync)
+ [AWSBackupGuardDutyRolePolicyForScans](#AWSBackupGuardDutyRolePolicyForScans)
+ [AWSBackupOperatorAccess](#AWSBackupOperatorAccess)
+ [AWSBackupOrganizationAdminAccess](#AWSBackupOrganizationAdminAccess)
+ [AWSBackupRestoreAccessForSAPHANA](#AWSBackupRestoreAccessForSAPHANA)
+ [AWSBackupSearchOperatorAccess](#AWSBackupSearchOperatorAccess)
+ [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup)
+ [AWSBackupServiceLinkedRolePolicyForBackupTest](#AWSBackupServiceLinkedRolePolicyForBackupTest)
+ [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup)
+ [AWSBackupServiceRolePolicyForItemRestores](#AWSBackupServiceRolePolicyForItemRestores)
+ [AWSBackupServiceRolePolicyForIndexing](#AWSBackupServiceRolePolicyForIndexing)
+ [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores)
+ [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup)
+ [AWSBackupServiceRolePolicyForS3Restore](#AWSBackupServiceRolePolicyForS3Restore)
+ [AWSBackupServiceRolePolicyForScans](#AWSBackupServiceRolePolicyForScans)
+ [AWSServiceRolePolicyForBackupReports](#AWSServiceRolePolicyForBackupReports)
+ [AWSServiceRolePolicyForBackupRestoreTesting](#AWSServiceRolePolicyForBackupRestoreTesting)

### AWSBackupAuditAccess
<a name="AWSBackupAuditAccess"></a>

This policy grants permissions for users to create controls and frameworks that define their expectations for AWS Backup resources and activities, and to audit AWS Backup resources and activities against their defined controls and frameworks. This policy grants permissions to AWS Config and similar services to describe user expectations perform the audits.

This policy also grants permissions to deliver audit reports to Amazon S3 and similar services, and enables users to find and open their audit reports.

To view the permissions for this policy, see [AWSBackupAuditAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupAuditAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupAccessPointOperatorAccess
<a name="AWSBackupAccessPointOperatorAccess"></a>

Access point operators are users who need to access backup data in recovery points without performing a full restore. Access point operators have permissions to create, describe, delete, and list backup access points.

This policy contains the necessary permissions for those functions.

To view the permissions for this policy, see [AWSBackupAccessPointOperatorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupAccessPointOperatorAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupDataTransferAccess
<a name="AWSBackupDataTransferAccess"></a>

This policy provides permissions for the AWS Backup storage plane data transfer APIs, allowing the AWS Backint agent to complete backup data transfer with the AWS Backup storage plane. You can attach this policy to roles assumed by Amazon EC2 instances running SAP HANA with the Backint agent.

To view the permissions for this policy, see [AWSBackupDataTransferAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupDataTransferAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupFullAccess
<a name="AWSBackupFullAccess"></a>

The backup administrator has full access to AWS Backup operations, including creating or editing backup plans, assigning AWS resources to backup plans, and restoring backups. Backup administrators are responsible for determining and enforcing backup compliance by defining backup plans that meet their organization's business and regulatory requirements. Backup administrators also ensure that their organization's AWS resources are assigned to the appropriate plan.

To view the permissions for this policy, see [AWSBackupFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupFullAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync
<a name="AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync"></a>

This policy provides Backup gateway permission to sync the metadata of Virtual Machines on your behalf

To view the permissions for this policy, see [AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync.html) in the *AWS Managed Policy Reference*.

### AWSBackupGuardDutyRolePolicyForScans
<a name="AWSBackupGuardDutyRolePolicyForScans"></a>

This policy must be added to a new scanning role that grants Amazon GuardDuty permission to read and scan your backups. You'll need to attach this scanning role to your backup plan within the malware protection or scan settings. When AWS Backup initiates a scan, it passes this scanning role to Amazon GuardDuty.

To view the permissions for this policy, see [AWSBackupGuardDutyRolePolicyForScans](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupGuardDutyRolePolicyForScans.html) in the *AWS Managed Policy Reference*.

### AWSBackupOperatorAccess
<a name="AWSBackupOperatorAccess"></a>

Backup operators are users that are responsible for ensuring the resources that they are responsible for are properly backed up. Backup operators have permissions to assign AWS resources to the backup plans that the backup administrator creates. They also have permissions to create on-demand backups of their AWS resources and to configure the retention period of on-demand backups. Backup operators do not have permissions to create or edit backup plans or to delete scheduled backups after they are created. Backup operators can restore backups. You can limit the resource types that a backup operator can assign to a backup plan or restore from a backup. You do this by allowing only certain service roles to be passed to AWS Backup that have permissions for a certain resource type.

To view the permissions for this policy, see [AWSBackupOperatorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupOperatorAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupOrganizationAdminAccess
<a name="AWSBackupOrganizationAdminAccess"></a>

The organization administrator has full access to AWS Organizations operations, including creating, editing, or deleting backup policies, assigning backup policies to accounts and organizational units, and monitoring backup activities within the organization. Organization administrators are responsible for protecting accounts in their organization by defining and assigning backup policies that meet their organization's business and regulatory requirements.

To view the permissions for this policy, see [AWSBackupOrganizationAdminAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupOrganizationAdminAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupRestoreAccessForSAPHANA
<a name="AWSBackupRestoreAccessForSAPHANA"></a>

This policy provides AWS Backup permission to restore a backup of SAP HANA on Amazon EC2.

To view the permissions for this policy, see [AWSBackupRestoreAccessForSAPHANA](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupRestoreAccessForSAPHANA.html) in the *AWS Managed Policy Reference*.

### AWSBackupSearchOperatorAccess
<a name="AWSBackupSearchOperatorAccess"></a>

The search operator role has access to create backup indexes and to create searches of indexed backup metadata.

This policy contains the necessary permissions for those functions.

To view the permissions for this policy, see [AWSBackupSearchOperatorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupSearchOperatorAccess.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceLinkedRolePolicyForBackup
<a name="AWSBackupServiceLinkedRolePolicyForBackup"></a>

This policy is attached to the service-linked role named AWSServiceRoleforBackup to allow AWS Backup to call AWS services on your behalf to manage your backups. For more information, see [Using roles to back up and copy](using-service-linked-roles-AWSServiceRoleForBackup.md).

To view the permissions for this policy, see [ AWSBackupServiceLinkedRolePolicyforBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceLinkedRolePolicyForBackup.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceLinkedRolePolicyForBackupTest
<a name="AWSBackupServiceLinkedRolePolicyForBackupTest"></a>

To view the permissions for this policy, see [AWSBackupServiceLinkedRolePolicyForBackupTest](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceLinkedRolePolicyForBackupTest.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceRolePolicyForBackup
<a name="AWSBackupServiceRolePolicyForBackup"></a>

Provides AWS Backup permissions to create backups of all supported resource types on your behalf.

To view the permissions for this policy, see [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceRolePolicyForItemRestores
<a name="AWSBackupServiceRolePolicyForItemRestores"></a>

**Description**

This policy grants users permissions to restore individual files and items in a snapshot (periodic backup recovery point) to a new or existing Amazon S3 bucket or new Amazon EBS volume. These permissions include: read permissions to Amazon EBS for snapshots managed by AWS Backup read/write permissions to Amazon S3 buckets, and generate and describe permissions for AWS KMS keys.

**Using this policy**

You can attach `AWSBackupServiceRolePolicyForItemRestores` to your users, groups, and roles.

**Policy details**
+ **Type:** AWS managed policy
+ **Creation time:** 21 November 2024, 22:45 UTC
+ **Edited time:** First instance
+ **ARN:** `arn:aws:iam::aws:policy/AWSBackupServiceRolePolicyForItemRestores`

**Policy version:** v1 (default)

This policy’s version defines the permissions for the policy. When the user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request or not.

**JSON policy document:**

#### AWSBackupServiceRolePolicyForItemRestores JSON
<a name="AWSBackupServiceRolePolicyForItemRestoresJSON"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EBSReadOnlyPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSnapshots"
            ],
            "Resource": "arn:aws:ec2:*::snapshot/*"
        },
        {
            "Sid": "KMSReadOnlyPermissions",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": "*"
        },
        {
            "Sid": "EBSDirectReadAPIPermissions",
            "Effect": "Allow",
            "Action": [
                "ebs:ListSnapshotBlocks",
                "ebs:GetSnapshotBlock"
            ],
            "Resource": "arn:aws:ec2:*::snapshot/*"
        },
        {
            "Sid": "S3ReadonlyPermissions",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation",
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Sid": "S3PermissionsForFileLevelRestore",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::*/*"
        },
        {
            "Sid": "KMSDataKeyForS3AndEC2Permissions",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": [
                        "ec2.*.amazonaws.com",
                        "s3.*.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

### AWSBackupServiceRolePolicyForIndexing
<a name="AWSBackupServiceRolePolicyForIndexing"></a>

**Description**

This policy grants users permissions to index snapshot, also known as periodic, recovery points. These permissions include: read permissions to Amazon EBS for snapshots managed by AWS Backup read/write permissions to Amazon S3 buckets, and generate and describe permissions for AWS KMS keys.

**Using this policy**

You can attach `AWSBackupServiceRolePolicyForIndexing` to your users, groups, and roles.

**Policy details**
+ **Type:** AWS managed policy
+ **Edited time:** First instance
+ **ARN:** `arn:aws:iam::aws:policy/AWSBackupServiceRolePolicyForIndexing`

**Policy version:** v1 (default)

This policy’s version defines the permissions for the policy. When the user or or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request or not.

**JSON policy document:**

#### AWSBackupServiceRolePolicyForIndexing JSON
<a name="AWSBackupServiceRolePolicyForIndexingJSON"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EBSReadOnlyPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSnapshots"
            ],
            "Resource": "arn:aws:ec2:*::snapshot/*"
        },
        {
            "Sid": "KMSReadOnlyPermissions",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": "*"
        },
        {
            "Sid": "EBSDirectReadAPIPermissions",
            "Effect": "Allow",
            "Action": [
                "ebs:ListSnapshotBlocks",
                "ebs:GetSnapshotBlock"
            ],
            "Resource": "arn:aws:ec2:*::snapshot/*"
        },
        {
            "Sid": "KMSDataKeyForEC2Permissions",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": [
                        "ec2.*.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

### AWSBackupServiceRolePolicyForRestores
<a name="AWSBackupServiceRolePolicyForRestores"></a>

Provides AWS Backup permissions to restore backups of all supported resource types on your behalf.

To view the permissions for this policy, see [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html) in the *AWS Managed Policy Reference*.

For EC2 instance restores, you must also include the following permissions to launch the EC2 instance:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowPassRole",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{123456789012}}:role/{{role-name}}",
      "Effect": "Allow"
    }
  ]
}
```

------

### AWSBackupServiceRolePolicyForS3Backup
<a name="AWSBackupServiceRolePolicyForS3Backup"></a>

This policy contains the permissions necessary for AWS Backup to back up any S3 bucket. This includes access to all objects in a bucket and any associated AWS KMS key.

To view the permissions for this policy, see [AWSBackupServiceRolePolicyForS3Backup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Backup.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceRolePolicyForS3Restore
<a name="AWSBackupServiceRolePolicyForS3Restore"></a>

This policy contains permissions necessary for AWS Backup to restore an S3 backup to a bucket. This includes read and write permissions to the buckets and the usage of any AWS KMS key in regards to S3 operations.

To view the permissions for this policy, see [AWSBackupServiceRolePolicyForS3Restore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.html) in the *AWS Managed Policy Reference*.

### AWSBackupServiceRolePolicyForScans
<a name="AWSBackupServiceRolePolicyForScans"></a>

The policy should be attached to the IAM role that you use in your backup plan's resource selection. This role grants AWS Backup permission to initiate scans in Amazon GuardDuty. 

To view the permissions for this policy, see [AWSBackupServiceRolePolicyForScans](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForScans.html) in the *AWS Managed Policy Reference*.

### AWSServiceRolePolicyForBackupReports
<a name="AWSServiceRolePolicyForBackupReports"></a>

AWS Backup uses this policy for the [AWSServiceRoleForBackupReports](https://docs.aws.amazon.com/aws-backup/latest/devguide/using-service-linked-roles-AWSServiceRoleForBackupReports.html) service-linked role. This service-linked role gives AWS Backup permissions to monitor and report on the compliance of your backup settings, jobs, and resources with your frameworks.

To view the permissions for this policy, see [AWSServiceRolePolicyForBackupReports](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRolePolicyForBackupReports.html) in the *AWS Managed Policy Reference*.

### AWSServiceRolePolicyForBackupRestoreTesting
<a name="AWSServiceRolePolicyForBackupRestoreTesting"></a>

To view the permissions for this policy, see [AWSServiceRolePolicyForBackupRestoreTesting](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRolePolicyForBackupRestoreTesting.html) in the *AWS Managed Policy Reference*.

## Customer managed policies
<a name="customer-managed-policies"></a>

The following sections describe the recommended backup and restore permissions for the AWS services and third-party application supported by AWS Backup. You can use the existing AWS managed policies as a model as you create your own policy documents, and then customize them to further restrict access to your AWS resources.

### How to build a customer managed policy from managed policy statements
<a name="customer-managed-policies-howto"></a>

Each service section below lists the specific statement names (Sids) you need from the AWS Backup managed policies. To build a least-privilege customer managed policy for a specific service, follow these steps:

1. Open the managed policy reference for [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html) (for backup permissions) or [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html) (for restore permissions).

1. Locate each statement by its `Sid` value as listed in the service section below.

1. Copy the full JSON block for each required statement into your custom policy document.

1. Wrap the statements in a valid IAM policy structure. Include the `Version` element to avoid [IAM Access Analyzer warnings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html#access-analyzer-reference-policy-checks-general-warning-missing-version):

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {{// Paste your extracted statements here}}
     ]
   }
   ```

1. (Optional) Narrow the `Resource` field in each statement to restrict access to specific resources rather than using `"*"`.

Alternatively, you can retrieve the full policy JSON using the AWS CLI:

```
aws iam get-policy-version \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup \
    --version-id $(aws iam get-policy --policy-arn arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup --query "Policy.DefaultVersionId" --output text) \
    --query "PolicyVersion.Document" \
    --output json
```

This returns the complete policy document, from which you can extract the statements you need by matching the `Sid` values listed in the service sections below.

**Important**  
When using custom IAM roles for AWS Backup, you must include resource-specific permissions in addition to AWS Backup permissions. For example, when calling `backup:ListTags` on an Amazon RDS resource, your custom IAM role must also include `rds:ListTagsForResource` permission. While these permissions are included in the default AWS Backup service role, they must be explicitly added to customer-managed policies. The underlying resource permissions required depend on the specific AWS service and operation being performed.

### Amazon Aurora
<a name="aurora-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `DynamoDBBackupPermissions`
+ `RDSClusterModifyPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`
+ `KMSPermissions`

**Restore**  
Start with the `RDSPermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Amazon Aurora DSQL
<a name="aurora-dsql-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `DSQLBackupPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`
+ `KMSPermissions`

**Restore**  
Start with the `DSQLRestorePermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Amazon DynamoDB
<a name="ddb-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `DynamoDBPermissions`
+ `DynamoDBBackupResourcePermissions`
+ `DynamodbBackupPermissions`
+ `KMSDynamoDBPermissions`

**Restore**

Start with the following statements from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html):
+ `DynamoDBPermissions`
+ `DynamoDBBackupResourcePermissions`
+ `DynamoDBRestorePermissions`
+ `KMSPermissions`

### Amazon EBS
<a name="ebs-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `EBSResourcePermissions`
+ `EBSTagAndDeletePermissions`
+ `EBSCopyPermissions`
+ `EBSSnapshotTierPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`

**Restore**  
Start with the `EBSPermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

Add the following statement.

```
{
      "Effect":"Allow",
      "Action": [
        "ec2:DescribeSnapshots",
        "ec2:DescribeVolumes"
      ],
      "Resource":"*"
},
```

### Amazon EC2
<a name="ec2-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `EBSCopyPermissions`
+ `EC2CopyPermissions`
+ `EC2Permissions`
+ `EC2TagPermissions`
+ `EC2ModifyPermissions`
+ `EBSResourcePermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`

**Restore**

Start with the following statements from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html):
+ `EBSPermissions`
+ `EC2DescribePermissions`
+ `EC2RunInstancesPermissions`
+ `EC2TerminateInstancesPermissions`
+ `EC2CreateTagsPermissions`

Add the following statement.

```
{
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{account-id}}:role/{{role-name}}"
},
```

Replace {{role-name}} with the name of the EC2 instance profile role that will be attached to the restored EC2 instance. This is not the AWS Backup service role, but rather the IAM role that provides permissions to applications running on the EC2 instance.

### Amazon EFS
<a name="efs-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `EFSPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`

**Restore**  
Start with the `EFSPermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Amazon FSx
<a name="fsx-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `FsxBackupPermissions`
+ `FsxCreateBackupPermissions`
+ `FsxPermissions`
+ `FsxVolumePermissions`
+ `FsxListTagsPermissions`
+ `FsxDeletePermissions`
+ `FsxResourcePermissions`
+ `KMSPermissions`

**Restore**

Start with the following statements from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html):
+ `FsxPermissions`
+ `FsxTagPermissions`
+ `FsxBackupPermissions`
+ `FsxDeletePermissions`
+ `FsxDescribePermissions`
+ `FsxVolumeTagPermissions`
+ `FsxBackupTagPermissions`
+ `FsxVolumePermissions`
+ `DSPermissions`
+ `KMSDescribePermissions`

### Amazon Neptune
<a name="neptune-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `DynamoDBBackupPermissions`
+ `RDSClusterModifyPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`
+ `KMSPermissions`

**Restore**  
Start with the `RDSPermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Amazon RDS
<a name="rds-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `DynamoDBBackupPermissions`
+ `RDSBackupPermissions`
+ `RDSClusterModifyPermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`
+ `KMSPermissions`

**Restore**  
Start with the `RDSPermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Amazon S3
<a name="s3-customer-managed-policies"></a>

**Backup**  
Start with [AWSBackupServiceRolePolicyForS3Backup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Backup.html).

Add the `BackupVaultPermissions` and `BackupVaultCopyPermissions` statements if you need to copy backups to a different account.

**Restore**  
Start with [AWSBackupServiceRolePolicyForS3Restore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForS3Restore.html).

### AWS Storage Gateway
<a name="storage-gateway-customer-managed-policies"></a>

**Backup**

Start with the following statements from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html):
+ `StorageGatewayPermissions`
+ `EBSTagAndDeletePermissions`
+ `GetResourcesPermissions`
+ `BackupVaultPermissions`

Add the following statement.

```
{
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSnapshots"
      ],
      "Resource":"*"
},
```

**Restore**

Start with the following statements from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html):
+ `StorageGatewayVolumePermissions`
+ `StorageGatewayGatewayPermissions`
+ `StorageGatewayListPermissions`

### Virtual machine
<a name="vm-customer-managed-policies"></a>

**Backup**  
Start with the `BackupGatewayBackupPermissions` statement from [AWSBackupServiceRolePolicyForBackup](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForBackup.html).

**Restore**  
Start with the `GatewayRestorePermissions` statement from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html).

### Encrypted backup
<a name="customer-managed-policies-encrypted-backup"></a>

**To restore an encrypted backup, do one of the following**
+ Add your role to the allowlist for the AWS KMS key policy
+ Add the following statements from [AWSBackupServiceRolePolicyForRestores](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.html) to your IAM role for restores:
  + `KMSDescribePermissions`
  + `KMSPermissions`
  + `KMSCreateGrantPermissions`

## Policy updates for AWS Backup
<a name="policy-updates"></a>

View details about updates to AWS managed policies for AWS Backup since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the following permission to this policy:+  `cloudformation:UntagResource` <br />This permission allows AWS Backup to untag CloudFormation resources. | August 27, 2026 | 
| [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – Update to an existing policy | AWS Backup added the following permission to this policy:+  `s3:ListTagsForResource` <br />With this permission, AWS Backup can verify the Amazon S3 bucket system tag `aws:backup:enabled` when configuring Amazon EventBridge event notifications for Amazon S3 backups. | August 24, 2026 | 
| [AWSBackupAccessPointOperatorAccess](#AWSBackupAccessPointOperatorAccess) – New policy | Use this new managed policy to create and manage backup access points and access backup data in recovery points through Amazon S3 access points. | August 6, 2026 | 
| [AWSServiceRolePolicyForBackupRestoreTesting](#AWSServiceRolePolicyForBackupRestoreTesting) – Update to an existing policy | AWS Backup added the following permission to this policy:+  `rds:DeleteTenantDatabase` <br />These permissions allow AWS Backup Restore Testing to delete RDS Tenant Databases after restore test completion. | March 18, 2026 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `guardduty:StartMalwareScan` <br />+  `guardduty:GetMalwareScan` <br />+  `iam:PassRole` <br />These permissions allow AWS Backup to initiate malware scans on your recovery points. | February 23, 2026 | 
| [AWSBackupGuardDutyRolePolicyForScans](#AWSBackupGuardDutyRolePolicyForScans) – New policy | AWS Backup added a new AWS managed policy that provides Amazon GuardDuty permission to read and scan customer backups. AWS Backup passes a role with this policy to GuardDuty when initiating the operations `StartMalwareScan`.<br />This is necessary to provide all necessary permissions needed for malware scans on recovery points of Amazon EC2,Amazon EBS, and Amazon S3 resources.<br />For more information, see the managed policy [AWSBackupGuardDutyRolePolicyForScans](#AWSBackupGuardDutyRolePolicyForScans). | November 19, 2025 | 
| [AWSBackupServiceRolePolicyForScans](#AWSBackupServiceRolePolicyForScans) – New policy | AWS Backup added a new AWS managed policy that provides AWS Backup permission to initiate malware scans on your recovery points.<br />This is necessary to provide all necessary permissions needed for malware scans on recovery points of Amazon EC2,Amazon EBS, and Amazon S3 resources.<br />For more information, see the managed policy [AWSBackupServiceRolePolicyForScans](#AWSBackupServiceRolePolicyForScans). | November 19, 2025 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added `malware-protection.guardduty.amazonaws.com` to `IamPassRolePermissions`, which is necessary to initiate malware scan jobs.  | November 19, 2025 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `malware-protection.guardduty.amazonaws.com` to `IamPassRolePermissions` <br />+  `backup:StartScanJob` <br />These permissions are necessary to initiate malware scan jobs. | November 19, 2025 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `eks:ListClusters` <br />+  `eks:ListTagsForResource` <br />+  `eks:DescribeCluster` <br />These permissions allow AWS Backup to backup and restore Amazon EKS clusters. | November 10, 2025 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `eks:ListClusters` <br />+  `eks:ListTagsForResource` <br />+  `eks:DescribeCluster` <br />These permissions allow AWS Backup to backup and restore Amazon EKS clusters. | November 10, 2025 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `eks:ListClusters` <br />+  `eks:ListTagsForResource` <br />+  `eks:DescribeCluster` <br />+  `eks:ListAddons` <br />+  `eks:DescribeAddon` <br />+  `eks:ListNodegroups` <br />+  `eks:DescribeNodegroup` <br />+  `eks:ListPodIdentityAssociations` <br />+  `eks:DescribePodIdentityAssociation` <br />+  `eks:ListAccessEntries` <br />+  `eks:DescribeAccessEntry` <br />+  `eks:ListAssociatedAccessPolicies` <br />+  `eks:ListFargateProfiles` <br />+  `eks:DescribeFargateProfile` <br />+  `ec2:DescribeLaunchTemplateVersions` <br />+  `eks:CreateAccessEntry` <br />+  `eks:AssociateAccessPolicy` <br />+  `eks:DisassociateAccessPolicy` <br />These permissions allow AWS Backup to create backups of Amazon EKS clusters and their associated resources on behalf of customers. | November 10, 2025 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `eks:ListClusters` <br />+  `eks:ListTagsForResource` <br />+  `eks:DescribeCluster` <br />+  `eks:ListAddons` <br />+  `eks:DescribeAddon` <br />+  `eks:ListNodegroups` <br />+  `eks:DescribeNodegroup` <br />+  `eks:ListPodIdentityAssociations` <br />+  `eks:DescribePodIdentityAssociation` <br />+  `eks:ListAccessEntries` <br />+  `eks:DescribeAccessEntry` <br />+  `eks:ListAssociatedAccessPolicies` <br />+  `eks:ListFargateProfiles` <br />+  `eks:DescribeFargateProfile` <br />+  `ec2:DescribeLaunchTemplateVersions` <br />+  `eks:CreateAccessEntry` <br />+  `eks:AssociateAccessPolicy` <br />+  `eks:DisassociateAccessPolicy` <br />These permissions allow AWS Backup to create backups of Amazon EKS clusters and their associated resources on behalf of customers. | November 10, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `eks:CreateCluster` <br />+  `eks:DescribeCluster` <br />+  `eks:CreateAccessEntry` <br />+  `eks:DescribeAccessEntry` <br />+  `eks:AssociateAccessPolicy` <br />+  `eks:ListAssociatedAccessPolicies` <br />+  `eks:CreateAddon` <br />+  `eks:DescribeAddon` <br />+  `eks:CreateNodegroup` <br />+  `eks:DescribeNodegroup` <br />+  `eks:CreateFargateProfile` <br />+  `eks:DescribeFargateProfile` <br />+  `eks:CreatePodIdentityAssociation` <br />+  `eks:DescribePodIdentityAssociation` <br />+  `eks:TagResource` <br />+  `eks:DisassociateAccessPolicy` <br />+  `iam:PassRole` <br />+  `ec2:DescribeLaunchTemplateVersions` <br />+  `ec2:DescribeSubnets` <br />+  `ec2:RunInstances` <br />+  `ec2:CreateTags` <br />+  `iam:GetRole` <br />+  `iam:ListAttachedRolePolicies` <br />+  `backup:StartRestoreJob` <br />+  `backup:ListRestoreJobs` <br />+  `backup:ListRecoveryPointsByBackupVault` <br />+  `backup:DescribeRestoreJob` <br />These permissions allow AWS Backup to perform restore operations for Amazon EKS clusters and their associated resources on behalf of customers. | November 10, 2025 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permission to this policy:+  `organizations:ListDelegatedAdministrators` <br />This permission allows AWS Backup to synchronize delegated administrator information with Organizations for cross-account management features. | September 9, 2025 | 
| [AWSBackupGuardDutyRolePolicyForScans](#AWSBackupGuardDutyRolePolicyForScans) – New policy | AWS Backup added a new AWS managed policy that provides Amazon GuardDuty permission to read and scan customer backups. AWS Backup passes a role with this policy to GuardDuty when initiating the operations `StartMalwareScan`.<br />This is necessary to provide all necessary permissions needed for malware scans on recovery points of Amazon EC2,Amazon EBS, and Amazon S3 resources.<br />For more information, see the managed policy [AWSBackupGuardDutyRolePolicyForScans](#AWSBackupGuardDutyRolePolicyForScans). | November 24, 2025 | 
| [AWSBackupServiceRolePolicyForScans](#AWSBackupServiceRolePolicyForScans) – New policy | AWS Backup added a new AWS managed policy that provides AWS Backup permission to initiate malware scans on your recovery points.<br />This is necessary to provide all necessary permissions needed for malware scans on recovery points of Amazon EC2,Amazon EBS, and Amazon S3 resources.<br />For more information, see the managed policy [AWSBackupServiceRolePolicyForScans](#AWSBackupServiceRolePolicyForScans). | November 24, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `dsql:UpdateCluster` <br />+  `dsql:AddPeerCluster` <br />+  `dsql:RemovePeerCluster` <br />+  `dsql:GetCluster` <br />These permissions are necessary for AWS Backup to perform orchestrated multi-Region restore operations for DSQL resources on behalf of customers. | July 17, 2025 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `mpa:GetApprovalTeam` <br />+  `mpa:ListApprovalTeams` <br />+  `mpa:StartSession` <br />+  `mpa:CancelSession` <br />+  `mpa:GetSession` <br />+  `mpa:ListSessions` <br />These permissions are necessary for AWS Backup integration with AWS Account Management and AWS Organizations so customers have the option of Multi-party approval (MPA) as part of their logically air-gapped vaults. | June 17, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy: | AWS Backup added the following permissions to this policy:+  `ec2:DescribeRouteTables` <br />+  `ec2:CreateTags` <br />These permissions are necessary to allow customers to restore Amazon FSx for OpenZFS Multi-availability zone (Multi-AZ) snapshots through AWS Backup. | May 27, 2025 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `dsql:GetCluster` <br />+  `dsql:ListClusters` <br />+  `dsql:ListTagsForResource` <br />These permissions allow AWS Backup to backup and restore Amazon Aurora DSQL resources. | May 21, 2025 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `dsql:GetCluster` <br />+  `dsql:ListClusters` <br />+  `dsql:ListTagsForResource` <br />These permissions allow AWS Backup to backup and restore Amazon Aurora DSQL resources. | May 21, 2025 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `kms:Decrypt` <br />+  `kms:ReEncryptTo` <br />+  `kms:ReEncryptFrom` <br />+  `dsql:StartBackupJob` <br />+  `dsql:GetBackupJob` <br />+  `dsql:StopBackupJob` <br />+  `dsql:GetCluster` <br />+  `dsql:ListClusters` <br />+  `dsql:ListTagsForResource` <br />These permissions allow AWS Backup to create, delete, retrieve, and manage Amazon Aurora DSQL snapshots on behalf of customers. | May 21, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `ec2:DescribeRouteTables` <br />+  `ec2:CreateTags` <br />+  `dsql:StartRestoreJob` <br />+  `dsql:GetRestoreJob` <br />+  `dsql:StopRestoreJob` <br />+  `dsql:TagResource` <br />+  `dsql:CreateCluster` <br />+  `dsql:PutMultiRegionProperties` <br />+  `dsql:PutWitnessRegion` <br />+  `kms:DescribeKey` <br />These permissions allow AWS Backup to create, delete, retrieve, encrypt, decrypt, and manage Amazon Aurora DSQL snapshots on behalf of customers. | May 21, 2025 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `dsql:ListClusters` <br />+  `dsql:ListTagsForResource` <br />These permissions allow AWS Backup to manage Aurora DSQL backups at customer-specified intervals. | May 21, 2025 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `aws:CalledVia` <br />+  `redshift-serverless:DeleteSnapshot` <br />+  `redshift-serverless:GetNamespace` <br />+  `redshift-serverless:GetSnapshot` <br />+  `redshift-serverless:GetWorkgroup` <br />+  `redshift-serverless:ListNamespaces` <br />+  `redshift-serverless:ListSnapshots` <br />+  `redshift-serverless:ListWorkgroups` <br />These permissions are necessary for designated customers to have full access to Amazon Redshift Serverless backups, including required read permissions as well as the ability to delete Amazon Redshift Serverless recovery points (snapshot backups).  | March 31, 2025 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `redshift-serverless:GetNamespace` <br />+  `redshift-serverless:GetSnapshot` <br />+  `redshift-serverless:GetWorkgroup` <br />+  `redshift-serverless:ListNamespaces` <br />+  `redshift-serverless:ListSnapshots` <br />+  `redshift-serverless:ListWorkgroups` <br />These permissions are necessary for designated customers to have all necessary backup permissions to Amazon Redshift Serverless, including required read permissions. | March 31, 2025 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `redshift-serverless:DeleteSnapshot` <br />+  `redshift-serverless:GetNamespace` <br />+  `redshift-serverless:GetSnapshot` <br />+  `redshift-serverless:GetWorkgroup` <br />+  `redshift-serverless:ListNamespaces` <br />+  `redshift-serverless:ListSnapshots` <br />+  `redshift-serverless:ListTagsForResource` <br />+  `redshift-serverless:ListWorkgroups` <br />These permissions are necessary for AWS Backup to manage Amazon Redshift Serverless snapshots at customer specified intervals. | March 31, 2025 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `redshift-serverless:CreateSnapshot` <br />+  `redshift-serverless:DeleteSnapshot` with a condition to only allow snapshots deletion with the `"aws:backup:source-resource"` tag <br />+  `redshift-serverless:GetNamespace` <br />+  `redshift-serverless:GetSnapshot` <br />+  `redshift-serverless:ListNamespaces` <br />+  `redshift-serverless:ListSnapshots` <br />+  `redshift-serverless:ListTagsForResource` <br />+  `redshift-serverless:TagResource` <br />These permissions are necessary to allow AWS Backup to create, delete, retrieve, and manage Amazon Redshift Serverless snapshots on behalf of customers. | March 31, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the following permissions to this policy:+  `redshift-serverless:GetNamespace` <br />+  `redshift-serverless:GetTableRestoreStatus` <br />+  `redshift-serverless:RestoreTableFromSnapshot` <br />These permissions are necessary to allow AWS Backup to restore Amazon Redshift and Amazon Redshift Serverless snapshots on behalf of the customer. | March 31, 2025 | 
| [AWSBackupSearchOperatorAccess](#AWSBackupSearchOperatorAccess) – Added a new AWS managed policy | AWS Backup added the AWSBackupSearchOperatorAccess AWS managed policy. | February 27, 2025 | 
|  [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | AWS Backup added the permission `rds:AddTagsToResource` to support Amazon RDS multi-tenant snapshot cross-account copy of backups.<br />This permission is necessary to complete operations when a customer chooses to create a cross-account copy of a multi-tenant RDS snapshot. | January 8, 2025 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | AWS Backup added the permissions `rds:CreateTenantDatabase` and `rds:DeleteTenantDatabase` to this policy to support the restore process of Amazon RDS resources.<br />These permissions are necessary to complete customer operations for restoring multi-tenant snapshots. | January 8, 2025 | 
| [AWSBackupServiceRolePolicyForItemRestores](#AWSBackupServiceRolePolicyForItemRestores) – Added a new AWS managed policy | AWS Backup added the AWSBackupServiceRolePolicyForItemRestores AWS managed policy. | November 26, 2024 | 
| [AWSBackupServiceRolePolicyForIndexing](#AWSBackupServiceRolePolicyForIndexing) – Added a new AWS managed policy | AWS Backup added the AWSBackupServiceRolePolicyForIndexing AWS managed policy. | November 26, 2024 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | AWS Backup added permission `backup:TagResource` to this policy.<br />The permission is necessary to obtain tagging permissions during the creation of a recovery point. | May 17, 2024 | 
|  [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – Update to an existing policy  | AWS Backup added permission `backup:TagResource` to this policy.<br />The permission is necessary to obtain tagging permissions during the creation of a recovery point. | May 17, 2024 | 
|  [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | AWS Backup added permission `backup:TagResource` to this policy.<br />The permission is necessary to obtain tagging permissions during the creation of a recovery point. | May 17, 2024 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the permission `rds:DeleteDBInstanceAutomatedBackups`. <br />This permission is necessary for AWS Backup to support continuous backup and point-in-time-restore of Amazon RDS instances. | May 1, 2024 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | AWS Backup updated the Amazon Resource Name (ARN) in permission `storagegateway:ListVolumes` from `arn:aws:storagegateway:*:*:gateway/*` to `*` in order to accommodate a change in the Storage Gateway API model. | May 1, 2024 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | AWS Backup updated the Amazon Resource Name (ARN) in permission `storagegateway:ListVolumes` from `arn:aws:storagegateway:*:*:gateway/*` to `*` in order to accommodate a change in the Storage Gateway API model. | May 1, 2024 | 
| [AWSServiceRolePolicyForBackupRestoreTesting](#AWSServiceRolePolicyForBackupRestoreTesting) – Update to an existing policy | Added the following permissions to describe and list recovery points and protected resources in order to conduct restore testing plans: `backup:DescribeRecoveryPoint`, `backup:DescribeProtectedResource`, `backup:ListProtectedResources`, and `backup:ListRecoveryPointsByResource`.<br />Added the permission `ec2:DescribeSnapshotTierStatus` to support Amazon EBS archive tier storage.<br />Added the permission `rds:DescribeDBClusterAutomatedBackups` to support Amazon Aurora continuous backups.<br />Added the following permissions to support restore testing of Amazon Redshift backups: `redshift:DescribeClusters` and `redshift:DeleteCluster`.<br />Added the permission `timestream:DeleteTable` to support restore testing of Amazon Timestream backups. | February 14, 2024 | 
|  [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the permissions `ec2:DescribeSnapshotTierStatus` and `ec2:RestoreSnapshotTier`.<br />These permissions are necessary for users to have the option to restore Amazon EBS resources stored with AWS Backup from archive storage.<br />For EC2 instance restores, you must also include permissions as shown in the following policy statement to launch the EC2 instance: | November 27, 2023 | 
|  [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Added the permissions `ec2:DescribeSnapshotTierStatus` and `ec2:ModifySnapshotTier` to support an additional storage option for backed up Amazon EBS resources to be transitioned to the archive storage tier.<br />These permissions are necessary for users to have the option to transition Amazon EBS resources stored with AWS Backup to archive storage. | November 27, 2023 | 
|  [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added the permissions `ec2:DescribeSnapshotTierStatus` and `ec2:ModifySnapshotTier` to support an additional storage option for backed up Amazon EBS resources to be transitioned to the archive storage tier.<br />These permissions are necessary for users to have the option to transition Amazon EBS resources stored with AWS Backup to archive storage.<br />Added the permissions `rds:DescribeDBClusterSnapshots` and `rds:RestoreDBClusterToPointInTime`, which is necessary for PITR (point-in-time restores) of Aurora clusters. | 
| [AWSServiceRolePolicyForBackupRestoreTesting](#AWSServiceRolePolicyForBackupRestoreTesting) – New policy | Provides the permissions necessary to conduct restore testing. The permissions include the actions `list, read, and write` for the following services to be included in restore tests: Aurora, DocumentDB, DynamoDB, Amazon EBS, Amazon EC2, Amazon EFS, FSx for Lustre, FSx for Windows File Server, FSx for ONTAP, FSx for OpenZFS, Amazon Neptune, Amazon RDS, and Amazon S3. | November 27, 2023 | 
|  [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy  | Added `restore-testing.backup.amazonaws.com` to `IamPassRolePermissions` and `IamCreateServiceLinkedRolePermissions`. This addition is necessary for AWS Backup to conduct restore tests on behalf of customers.  | November 27, 2023 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | Added the permissions `rds:DescribeDBClusterSnapshots` and `rds:RestoreDBClusterToPointInTime`, which is necessary for PITR (point-in-time restores) of Aurora clusters. | September 6, 2023 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the permission `rds:DescribeDBClusterAutomatedBackups`, which is necessary for continuous backup and point-in-time restore of Aurora clusters. | September 6, 2023 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the permission `rds:DescribeDBClusterAutomatedBackups`, which is necessary for continuous backup and point-in-time restore of Aurora clusters. | September 6, 2023 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the permission `rds:DescribeDBClusterAutomatedBackups`. This permission is necessary for AWS Backup support of continuous backup and point-in-time restore of Aurora clusters.<br />Added the permission `rds:DeleteDBClusterAutomatedBackups` to allow AWS Backup lifecycle to delete and disassociate Amazon Aurora continuous recovery points when a retention period finishes. This permission is necessary for the Aurora recovery point to avoid a transition into an `EXIPIRED` state.<br />Added the permission `rds:ModifyDBCluster` which allows AWS Backup to interact with Aurora clusters. This addition allows users the ability to enable or disable continuous backups based on desired configurations. | September 6, 2023 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the action `ram:GetResourceShareAssociations` to grant the user permission to get resource share associations for new vault type. | August 8, 2023 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the action `ram:GetResourceShareAssociations` to grant the user permission to get resource share associations for new vault type. | August 8, 2023 | 
|  [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – Update to an existing policy  | Added the permission `s3:PutInventoryConfiguration` to enhance backup performance speeds by using a bucket inventory. | August 1, 2023 | 
|  [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the following actions to grant the user permissions to add tags to restore resources: `storagegateway:AddTagsToResource`, `elasticfilesystem:TagResource`, `ec2:CreateTags` for only `ec2:CreateAction` that includes either `RunInstances` or `CreateVolume`, `fsx:TagResource`, and `cloudformation:TagResource`. | May 22, 2023 | 
|  [AWSBackupAuditAccess](#AWSBackupAuditAccess) – Update to an existing policy  | Replaced the resource selection within the API `config:DescribeComplianceByConfigRule` with a wildcard resource to make it easier for a user to select resources. | April 11, 2023 | 
|  [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the following permission to restore Amazon EFS using a customer managed key: `kms:GenerateDataKeyWithoutPlaintext`. This helps to ensure users have required permissions to restore Amazon EFS resources. | March 27, 2023 | 
|  [AWSServiceRolePolicyForBackupReports](#AWSServiceRolePolicyForBackupReports) – Update to an existing policy  | Updated the `config:DescribeConfigRules` and `config:DescribeConfigRuleEvaluationStatus` actions to allow AWS Backup Audit Manager to access AWS Backup Audit Manager-managed AWS Config rules. | March 9, 2023 | 
|  [AWSBackupServiceRolePolicyForS3Restore](#AWSBackupServiceRolePolicyForS3Restore) – Update to an existing policy  | Added the following permissions: `kms:Decrypt`, `s3:PutBucketOwnershipControls`, and `s3:GetBucketOwnershipControls` to the policy `AWSBackupServiceRolePolicyForS3Restore`. These permissions are necessary to support restores of objects when KMS encryption is used in the original backup and for restoring objects when object ownership is configured on the original bucket instead of ACL. | February 13, 2023 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the following permissions to schedule backups using VMware tags of virtual machines and to support schedule-based bandwidth throttling: `backup-gateway:GetHypervisorPropertyMappings`, `backup-gateway:GetVirtualMachine`, `backup-gateway:PutHypervisorPropertyMappings`, `backup-gateway:GetHypervisor`, `backup-gateway:StartVirtualMachinesMetadataSync`, `backup-gateway:GetBandwidthRateLimitSchedule`, and `backup-gateway:PutBandwidthRateLimitSchedule`. | December 15, 2022 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the following permissions to schedule backups using VMware tags of virtual machines and to support schedule-based bandwidth throttling: `backup-gateway:GetHypervisorPropertyMappings`, `backup-gateway:GetVirtualMachine`, `backup-gateway:GetHypervisor`, and `backup-gateway:GetBandwidthRateLimitSchedule`. | December 15, 2022 | 
| [AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync](#AWSBackupGatewayServiceRolePolicyForVirtualMachineMetadataSync) – New policy | Provides permissions for AWS Backup Gateway to sync the metadata of virtual machines in on-premise networks with Backup Gateway. | December 15, 2022 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support Timestream backup jobs: `timestream:StartAwsBackupJob`, `timestream:GetAwsBackupStatus`, `timestream:ListTables`, `timestream:ListDatabases`, `timestream:ListTagsForResource`, `timestream:DescribeTable`, `timestream:DescribeDatabase`, and `timestream:DescribeEndpoints`. | December 13, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | Added the following permissions to support Timestream restore jobs: `timestream:StartAwsRestoreJob`, `timestream:GetAwsRestoreStatus`, `timestream:ListTables`, `timestream:ListTagsForResource`, `timestream:ListDatabases`, `timestream:DescribeTable`, `timestream:DescribeDatabase`, `s3:GetBucketAcl`, and `timestream:DescribeEndpoints`. | December 13, 2022 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the following permissions to support Timestream resources: `timestream:ListTables`, `timestream:ListDatabases`, `s3:ListAllMyBuckets` and `timestream:DescribeEndpoints`. | December 13, 2022 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the following permissions to support Timestream resources: `timestream:ListDatabases`, `timestream:ListTables`, `s3:ListAllMyBuckets`, and `timestream:DescribeEndpoints`. | December 13, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support Timestream resources: `timestream:ListDatabases`, `timestream:ListTables`, `timestream:ListTagsForResource`, `timestream:DescribeDatabase`, `timestream:DescribeTable`, `timestream:GetAwsBackupStatus`, `timestream:GetAwsRestoreStatus`, and `timestream:DescribeEndpoints`. | December 13, 2022 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the following permissions to support Amazon Redshift resources: `redshift:DescribeClusters`, `redshift:DescribeClusterSubnetGroups`, `redshift:DescribeNodeConfigurationOptions`, `redshift:DescribeOrderableClusterOptions`, `redshift:DescribeClusterParameterGroups`, `redshift:DescribeClusterTracks`, `redshift:DescribeSnapshotSchedules`, and `ec2:DescribeAddresses`. | November 27, 2022 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the following permissions to support Amazon Redshift resources: `redshift:DescribeClusters`, `redshift:DescribeClusterSubnetGroups`, `redshift:DescribeNodeConfigurationOptions`, `redshift:DescribeOrderableClusterOptions`, `redshift:DescribeClusterParameterGroups,`, `redshift:DescribeClusterTracks`. `redshift:DescribeSnapshotSchedules`, and `ec2:DescribeAddresses`. | November 27, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | Added the following permissions to support Amazon Redshift restore jobs: `redshift:RestoreFromCluster Snapshot`, `redshift:RestoreTableFromClusterSnapshot`, `redshift:DescribeClusters`, and `redshift:DescribeTableRestoreStatus`. | November 27, 2022 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support Amazon Redshift backup jobs: `redshift:CreateClusterSnapshot`, `redshift:DescribeClusterSnapshots`, `redshift:DescribeTags`, `redshift:DeleteClusterSnapshot`, `redshift:DescribeClusters`, and `redshift:CreateTags`. | November 27, 2022 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the following permission to support CloudFormation resources: `cloudformation:ListStacks`. | November 27, 2022 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the following permission to support CloudFormation resources: `cloudformation:ListStacks`. | November 27, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support CloudFormation resources: `redshift:DescribeClusterSnapshots`, `redshift:DescribeTags`, `redshift:DeleteClusterSnapshot`, and `redshift:DescribeClusters`. | November 27, 2022 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support CloudFormation application stack backup jobs: `cloudformation:GetTemplate`, `cloudformation:DescribeStacks`, and `cloudformation:ListStackResources`. | November 16, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | Added the following permissions to support CloudFormation application stack backup jobs: `cloudformation:CreateChangeSet` and `cloudformation:DescribeChangeSet` | November 16, 2022 | 
| [AWSBackupOrganizationAdminAccess](#AWSBackupOrganizationAdminAccess) – Update to an existing policy | Added the following permissions to this policy to allow organization administrators to usethe Delegated Administrator feature: `organizations:ListDelegatedAdministrator`, `organizations:RegisterDelegatedAdministrator`, and `organizations:DeregisterDelegatedAdministrator` | November 27, 2022 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy | Added the following permissions to support SAP HANA on Amazon EC2 instances: `ssm-sap:GetOperation`, `ssm-sap:ListDatabases`, `ssm-sap:BackupDatabase`, `ssm-sap:UpdateHanaBackupSettings`, `ssm-sap:GetDatabase`, and `ssm-sap:ListTagsForResource`. | November 20, 2022 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy | Added the following permissions to support SAP HANA on Amazon EC2 instances: `ssm-sap:GetOperation`, `ssm-sap:ListDatabases`, `ssm-sap:GetDatabase`, and `ssm-sap:ListTagsForResource`. | November 20, 2022 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy | Added the following permissions to support SAP HANA on Amazon EC2 instances: `ssm-sap:GetOperation`, `ssm-sap:ListDatabases`, `ssm-sap:GetDatabase`, and `ssm-sap:ListTagsForResource`. | November 20, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy | Added the following permission to support SAP HANA on Amazon EC2 instances: `ssm-sap:GetOperation`. | November 20, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy | Added the following permission to support Backup gateway restore jobs to an EC2 instance: `ec2:CreateTags`. | November 20, 2022 | 
| [AWSBackupDataTransferAccess](#AWSBackupDataTransferAccess) – Update to an existing policy | Added the following permissions to support secure storage data transfer for SAP HANA On Amazon EC2 resources: `backup-storage:StartObject`, `backup-storage:PutChunk`, `backup-storage:GetChunk`, `backup-storage:ListChunks`, `backup-storage:ListObjects`, `backup-storage:GetObjectMetadata`, and `backup-storage:NotifyObjectComplete`. | November 20, 2022 | 
| [AWSBackupRestoreAccessForSAPHANA](#AWSBackupRestoreAccessForSAPHANA) – Update to an existing policy | Added the following permissions for resource owners to perform restore of SAP HANA On Amazon EC2 resources: `backup:Get*`, `backup:List*`, `backup:Describe*`, `backup:StartBackupJob`, `backup:StartRestoreJob`, `ssm-sap:GetOperation`, `ssm-sap:ListDatabases`, `ssm-sap:BackupDatabase`, `ssm-sap:RestoreDatabase`, `ssm-sap:UpdateHanaBackupSettings`, `ssm-sap:GetDatabase`, and `ssm-sap:ListTagsForResource`. | November 20, 2022 | 
| [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – Update to an existing policy  | Added the permission `s3:GetBucketAcl` to support backup operations of AWS Backup for Amazon S3. | August 24, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the following actions to grant access to create a database instance to support multi-Availability Zone (Multi-AZ) functionality: `rds:CreateDBInstance`. | July 20, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added the `s3:GetBucketTagging` permission to grant the user permission to select buckets to backup with a resource wildcard. Without this permission, users who select which buckets to backup with a resource wildcard are unsuccessful. | May 6, 2022 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Added volume resources in the scope of existing `fsx:CreateBackup` and `fsx:ListTagsForResource` actions, and added new action `fsx:DescribeVolumes` to support FSx for ONTAP volume level backups. | April 27, 2022 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the following actions to grant the users permissions to restore FSx for ONTAP volumes `fsx:DescribeVolumes`, `fsx:CreateVolumeFromBackup`, `fsx:DeleteVolume`, and `fsx:UntagResource`. | April 27, 2022 | 
| [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – Update to an existing policy  | Added the following actions to grant the user permissions to receive notifications of changes to their Amazon S3 buckets during backup operations: `s3:GetBucketNotification` and `s3:PutBucketNotification`. | February 25, 2022 | 
| [AWSBackupServiceRolePolicyForS3Backup](#AWSBackupServiceRolePolicyForS3Backup) – New policy  | Added the following actions to grant the user permissions to back up their Amazon S3 buckets: `s3:GetInventoryConfiguration`, `s3:PutInventoryConfiguration`, `s3:ListBucketVersions`, `s3:ListBucket`, `s3:GetBucketTagging`, `s3:GetBucketVersioning`, `s3:GetBucketNotification`,`s3:GetBucketLocation`, and `s3:ListAllMyBuckets`<br />Added the following actions to grant the user permissions to back up their Amazon S3 objects: `s3:GetObject`,`s3GetObjectAcl`, `s3:GetObjectVersionTagging`, `s3:GetObjectVersionAcl`, `s3:GetObjectTagging`, and `s3:GetObjectVersion`. <br />Added the following actions to grant the user permissions to back up their encrypted Amazon S3 data: `kms:Decrypt` and `kms:DescribeKey`. <br />Added the following actions to grant the user permissions to take incremental backups of their Amazon S3 data using Amazon EventBridge rules: `events:DescribeRule`, `events:EnableRule`, `events:PutRule`, `events:DeleteRule`, `events:PutTargets`, `events:RemoveTargets`, `events:ListTargetsByRule`, `events:DisableRule`, `cloudwatch:GetMetricData`, and `events:ListRules`. | February 17, 2022 | 
| [AWSBackupServiceRolePolicyForS3Restore](#AWSBackupServiceRolePolicyForS3Restore) – New policy  | Added the following actions to grant the user permissions to restore their Amazon S3 buckets: `s3:CreateBucket`, `s3:ListBucketVersions`, `s3:ListBucket`, `s3:GetBucketVersioning`, `s3:GetBucketLocation`, and `s3:PutBucketVersioning`.<br />Added the following actions to grant the user permissions to restore their Amazon S3 buckets: `s3:GetObject`, `s3:GetObjectVersion`, `s3:DeleteObject`, `s3:PutObjectVersionAcl`, `s3:GetObjectVersionAcl`, `s3:GetObjectTagging`, `s3:PutObjectTagging`, `s3:GetObjectAcl`, `s3:PutObjectAcl`, `s3:PutObject`, and `s3:ListMultipartUploadParts`.<br />Added the following actions to grant the user permissions to encrypt their restored Amazon S3 data: `kms:Decrypt`, `kms:DescribeKey`, and `kms:GenerateDataKey`. | February 17, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added `s3:ListAllMyBuckets` to grant the user permissions to view a list of their buckets and choose which ones to assign to a backup plan. | February 14, 2022 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added `backup-gateway:ListVirtualMachines` to grant the user permissions to view a list of their virtual machines and choose which ones to assign to a backup plan.<br />Added `backup-gateway:ListTagsForResource` to grant the user permissions to list the tags for their virtual machines. | November 30, 2021 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Added `backup-gateway:Backup` to grant the user permissions restore their virtual machine backups. AWS Backup also added `backup-gateway:ListTagsForResource` to grant the user permissions to list the tags assigned to their virtual machine backups. | November 30, 2021 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added `backup-gateway:Restore` to grant the user permissions restore their virtual machine backups. | November 30, 2021 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy  | Added the following actions to grant the users permissions to use AWS Backup Gateway to back up, restore, and manage their virtual machines: `backup-gateway:AssociateGatewayToServer`, `backup-gateway:CreateGateway`, `backup-gateway:DeleteGateway`, `backup-gateway:DeleteHypervisor`, `backup-gateway:DisassociateGatewayFromServer`, `backup-gateway:ImportHypervisorConfiguration`, `backup-gateway:ListGateways`, `backup-gateway:ListHypervisors`, `backup-gateway:ListTagsForResource`, `backup-gateway:ListVirtualMachines`, `backup-gateway:PutMaintenanceStartTime`, `backup-gateway:TagResource`, `backup-gateway:TestHypervisorConfiguration`, `backup-gateway:UntagResource`, `backup-gateway:UpdateGatewayInformation`, and `backup-gateway:UpdateHypervisor`. | November 30, 2021 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy  | Added the following actions to grant the user permissions to back up their virtual machines: `backup-gateway:ListGateways`, `backup-gateway:ListHypervisors`, `backup-gateway:ListTagsForResource`, and `backup-gateway:ListVirtualMachines`. | November 30, 2021 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added `dynamodb:ListTagsOfResource` to grant the user permissions to list tags of their DynamoDB tables to back up using AWS Backup's advanced DynamoDB backup features. | November 23, 2021 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Added `dynamodb:StartAwsBackupJob` to grant the user permissions to back up their DynamoDB tables using advanced backup features.<br />Added `dynamodb:ListTagsOfResource` to grant the user to permissions to copy tags from their source DynamoDB tables to their backups. | November 23, 2021 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added `dynamodb:RestoreTableFromAwsBackup` to grant the user permissions restore their DynamoDB tables backed up using AWS Backup's advanced DynamoDB advanced backup features. | November 23, 2021 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added `dynamodb:RestoreTableFromAwsBackup` to grant the user permissions restore their DynamoDB tables backed up using AWS Backup's advanced DynamoDB advanced backup features. | November 23, 2021 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy  | Removed the actions `backup:GetRecoveryPointRestoreMetadata` and `rds:DescribeDBSnapshots` because they were redundant.<br /> AWS Backup did not need both `backup:GetRecoveryPointRestoreMetadata` and `backup:Get*` as part of `AWSBackupOperatorAccess`. Also, AWS Backup did not need both `rds:DescribeDBSnapshots` and `rds:describeDBSnapshots` as part of `AWSBackupOperatorAccess`. | November 23, 2021 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added the new actions `elasticfilesystem:DescribeFileSystems`, `dynamodb:ListTables`, `storagegateway:ListVolumes`, `ec2:DescribeVolumes`, `ec2:DescribeInstances`, `rds:DescribeDBInstances`, `rds:DescribeDBClusters`, and `fsx:DescribeFileSystems` to allow customers to view and choose from a list of their AWS Backup-supported resources when selecting which resources to assign to a backup plan. | November 10, 2021 | 
| [AWSBackupAuditAccess](#AWSBackupAuditAccess) – New policy  | Added `AWSBackupAuditAccess` to grant the user permissions to use AWS Backup Audit Manager. Permissions include the ability to configure compliance frameworks and generate reports. | August 24, 2021 | 
| [AWSServiceRolePolicyForBackupReports](#AWSServiceRolePolicyForBackupReports) – New policy  | Added `AWSServiceRolePolicyForBackupReports` to grant permissions for a service-linked role to automate the monitoring of backup settings, jobs, and resources for compliance with frameworks configured by the user. | August 24, 2021 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy  | Added `iam:CreateServiceLinkedRole` to create a service-linked role (on a best-effort basis) to automate the deletion of expired recovery points for you. Without this service-linked role, AWS Backup cannot delete expired recovery points after customers delete the original IAM role they used to create their recovery points. | July 5, 2021 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added the new action `dynamodb:DeleteBackup` to grant `DeleteRecoveryPoint` permission to automate the deletion of expired DynamoDB recovery points based on your backup plan lifecycle settings. | July 5, 2021 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy  | Removed the actions `backup:GetRecoveryPointRestoreMetadata` and `rds:DescribeDBSnapshots` because they were redundant.<br />AWS Backup did not need both `backup:GetRecoveryPointRestoreMetadata` and `backup:Get*` as part of `AWSBackupOperatorAccess` Also, AWS Backup did not need both `rds:DescribeDBSnapshots` and `rds:describeDBSnapshots` as part of `AWSBackupOperatorAccess` | May 25, 2021 | 
| [AWSBackupOperatorAccess](#AWSBackupOperatorAccess) – Update to an existing policy  | Removed the actions `backup:GetRecoveryPointRestoreMetadata` and `rds:DescribeDBSnapshots` because they were redundant.<br />AWS Backup did not need both `backup:GetRecoveryPointRestoreMetadata` and `backup:Get*` as part of `AWSBackupOperatorAccess`. Also, AWS Backup did not need both `rds:DescribeDBSnapshots` and `rds:describeDBSnapshots` as part of `AWSBackupOperatorAccess`. | May 25, 2021 | 
| [AWSBackupServiceRolePolicyForRestores]() – Update to an existing policy  | Added the new action `fsx:TagResource` to grant `StartRestoreJob` permission to allow you to apply tags to Amazon FSx file systems during the restore process. | May 24, 2021 | 
| [AWSBackupServiceRolePolicyForRestores](#AWSBackupServiceRolePolicyForRestores) – Update to an existing policy  | Added the new actions `ec2:DescribeImages` and `ec2:DescribeInstances` to grant `StartRestoreJob` permission to allow you to restore Amazon EC2 instances from recovery points. | May 24, 2021 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Added the new action `fsx:CopyBackup` to grant `StartCopyJob` permission to allow you to copy Amazon FSx recovery points across Regions and accounts. | April 12, 2021 | 
| [AWSBackupServiceLinkedRolePolicyForBackup](#AWSBackupServiceLinkedRolePolicyForBackup) – Update to an existing policy  | Added the new action `fsx:CopyBackup` to grant `StartCopyJob` permission to allow you to copy Amazon FSx recovery points across Regions and accounts. | April 12, 2021 | 
| [AWSBackupServiceRolePolicyForBackup](#AWSBackupServiceRolePolicyForBackup) – Update to an existing policy  | Updated to comply with the following requirement:<br />For AWS Backup to create a backup of an encrypted DynamoDB table, you must add the permissions `kms:Decrypt` and `kms:GenerateDataKey` to the IAM role used for backup. | March 10, 2021 | 
| [AWSBackupFullAccess](#AWSBackupFullAccess) – Update to an existing policy  | Updated to comply with the following requirements:<br />To use AWS Backup to configure continuous backups for your Amazon RDS database, verify the API permission `rds:ModifyDBInstance` exists in the IAM role defined by your Backup plan configuration.<br />To restore Amazon RDS continuous backups, you must add the permission `rds:RestoreDBInstanceToPointInTime` to the IAM role you submitted for restore job.<br />In the AWS Backup console, to describe the range of times available for point-in-time recovery, you must include the `rds:DescribeDBInstanceAutomatedBackups` API permission in your IAM-managed policy. | March 10, 2021 | 
| AWS Backup started tracking changes | AWS Backup started tracking changes for its AWS-managed policies. | March 10, 2021 | 