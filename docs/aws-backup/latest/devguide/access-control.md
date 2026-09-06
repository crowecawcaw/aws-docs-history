

# Access control
<a name="access-control"></a>

You can have valid credentials to authenticate your requests, but unless you have the appropriate permissions, you can't access AWS Backup resources such as backup vaults. You also can't back up AWS resources such as Amazon Elastic Block Store (Amazon EBS) volumes.

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies. An account administrator can attach permissions policies to AWS Identity and Access Management (IAM) identities (that is, users, groups, and roles). And some services also support attaching permissions policies to resources. 

An *account administrator* (or administrator user) is a user with administrator permissions. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

When granting permissions, you decide who is getting the permissions, the resources they get permissions for, and the specific actions that you want to allow on those resources.

The following sections cover how access policies work and how you use them to protect your backups. 

**Topics**
+ [Resources and operations](#access-control-resources)
+ [Resource ownership](#access-control-owner)
+ [Specifying policy elements: actions, effects, and principals](#access-control-specify-backup-actions)
+ [Specifying conditions in a policy](#specifying-conditions)
+ [API permissions: actions, resources, and conditions reference](#backup-api-permissions-ref)
+ [Copy tags permissions](#copy-tags)
+ [Access policies](#access-policies)

## Resources and operations
<a name="access-control-resources"></a>

A resource is an object that exists within a service. AWS Backup resources include backup plans, backup vaults, and backups. *Backup* is a general term that refers to the various types of backup resources that exist in AWS. For example, Amazon EBS snapshots, Amazon Relational Database Service (Amazon RDS) snapshots, and Amazon DynamoDB backups are all types of backup resources. 

In AWS Backup, backups are also referred to as *recovery points*. When using AWS Backup, you also work with the resources from other AWS services that you are trying to protect, such as Amazon EBS volumes or DynamoDB tables. These resources have unique Amazon Resource Names (ARNs) associated with them. ARNs uniquely identify AWS resources. You must have an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies or API calls. 

The following table lists resources, subresources, ARN format, and an example unique ID.


**AWS Backup resource ARNs**  

| Resource type | ARN format | Example unique ID | 
| --- | --- | --- | 
| Backup plan | arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\* |  | 
| Backup vault | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\* |  | 
| Recovery point for Amazon EBS | arn:aws:ec2:{{region}}::snapshot/\* | snapshot/snap-05f426fd8kdjb4224 | 
| Recovery point for Amazon EC2 images | arn:aws:ec2:{{region}}::image/ami-\* | image/ami-1a2b3e4f5e6f7g890 | 
| Recovery point for Amazon RDS | arn:aws:rds:{{region}}:{{account-id}}:snapshot:awsbackup:\* | awsbackup:job-be59cf2a-2343-4402-bd8b-226993d23453 | 
| Recovery point for Aurora | arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:awsbackup:\* | awsbackup:job-be59cf2a-2343-4402-bd8b-226993d23453 | 
| Recovery point for Aurora DSQL | arn:{{aws-partition}}:backup:{{region}}:{{account-id}}:recovery-point:{{recovery-point-id}} | arn:aws:backup:us-east-1:012345678901:recovery-point:8a92c3f1-b475-4d9e-95e6-7c138f2d4b0a | 
| Recovery point for Storage Gateway | arn:aws:ec2:{{region}}::snapshot/\* | snapshot/snap-0d40e49137e31d9e0 | 
| Recovery point for DynamoDB without [Advanced DynamoDB backup](advanced-ddb-backup.md) | arn:aws:dynamodb:{{region}}:{{account-id}}:table/\*/backup/\* | table/MyDynamoDBTable/backup/01547087347000-c8b6kdk3 | 
| Recovery point for DynamoDB with [Advanced DynamoDB backup](advanced-ddb-backup.md) enabled | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | 12a34a56-7bb8-901c-cd23-4567d8e9ef01 | 
| Recovery point for Amazon EFS | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | d99699e7-e183-477e-bfcd-ccb1c6e5455e | 
| Recovery point for Amazon FSx | arn:aws:fsx:{{region}}:{{account-id}}:backup/backup-\* | backup/backup-1a20e49137e31d9e0 | 
| Recovery point for virtual machine | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | 1801234a-5b6b-7dc8-8032-836f7ffc623b | 
| Recovery point for Amazon S3 continuous backup | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | {{amzn-s3-demo-bucket}}-5ec207d0 | 
| Recovery point for S3 periodic backup | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | {{amzn-s3-demo-bucket}}-20211231900000-5ec207d0 | 
| Recovery point for Amazon DocumentDB | arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:awsbackup:\* | awsbackup:job-ab12cd3e-4567-8901-fg1h-234567i89012 | 
| Recovery point for Neptune | arn:aws:rds:{{region}}:{{account-id}}:cluster-snapshot:awsbackup:\* | awsbackup:job-ab12cd3e-4567-8901-fg1h-234567i89012 | 
| Recovery point for Amazon Redshift | arn:aws:redshift:{{region}}:{{account-id}}:snapshot:{{resource}}/awsbackup:\* | awsbackup:job-ab12cd3e-4567-8901-fg1h-234567i89012 | 
| Recovery point for Amazon Redshift Serverless | arn:aws:redshift-serverless:{{region}}:{{account-id}}:snapshot:{{resource}}/awsbackup:\* | awsbackup:job-ab12cd3e-4567-8901-fg1h-234567i89012 | 
| Recovery point for Amazon Timestream | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | recovery-point:1a2b3cde-f405-6789-012g-3456hi789012\_beta | 
| Recovery point for AWS CloudFormation template | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | recovery-point:1a2b3cde-f405-6789-012g-3456hi789012 | 
| Recovery point for SAP HANA database on Amazon EC2 instance | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | recovery-point:1a2b3cde-f405-6789-012g-3456hi789012 | 
| Backup access point | arn:aws:backup:{{region}}:{{account-id}}:accesspoint/\* | accesspoint/my-access-point | 

Resources that support full AWS Backup management all have recovery points in the format `arn:aws:backup:{{region}}:{{account-id:}}:recovery-point:*`. making it easier for you to apply permissions policies to protect those recovery points. To see which resources support full AWS Backup management, see that section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource) table.

AWS Backup provides a set of operations to work with AWS Backup resources. For a list of available operations, see AWS Backup [Operations](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_Operations.html).

## Resource ownership
<a name="access-control-owner"></a>

The AWS account owns the resources that are created in the account, regardless of who created the resources. Specifically, the resource owner is the AWS account of the [principal entity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts) (that is, the AWS account root user, an IAM user, or an IAM role) that authenticates the resource creation request. The following examples illustrate how this works:
+ If you use the AWS account root user credentials of your AWS account to create a backup vault, your AWS account is the owner of the vault.
+ If you create an IAM user in your AWS account and grant permissions to create a backup vault to that user, the user can create a backup vault. However, your AWS account, to which the user belongs, owns the backup vault resource.
+ If you create an IAM role in your AWS account with permissions to create a backup vault, anyone who can assume the role can create a vault. Your AWS account, to which the role belongs, owns the backup vault resource. 

## Specifying policy elements: actions, effects, and principals
<a name="access-control-specify-backup-actions"></a>

For each AWS Backup resource (see [Resources and operations](#access-control-resources)), the service defines a set of API operations (see [Operations](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_Operations.html)). To grant permissions for these API operations, AWS Backup defines a set of actions that you can specify in a policy. Performing an API operation can require permissions for more than one action.

The following are the most basic policy elements:
+ Resource – In a policy, you use an Amazon Resource Name (ARN) to identify the resource to which the policy applies. For more information, see [Resources and operations](#access-control-resources).
+ Action – You use action keywords to identify resource operations that you want to allow or deny.
+ Effect – You specify the effect when the user requests the specific action—this can be either allow or deny. If you don't explicitly grant access to (allow) a resource, access is implicitly denied. You can also explicitly deny access to a resource, which you might do to make sure that a user cannot access it, even if a different policy grants access.
+ Principal – In identity-based policies (IAM policies), the user that the policy is attached to is the implicit principal. For resource-based policies, you specify the user, account, service, or other entity that you want to receive permissions (applies to resource-based policies only).

To learn more about IAM policy syntax and descriptions, see [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

For a table showing all of the AWS Backup API actions, see [API permissions: actions, resources, and conditions reference](#backup-api-permissions-ref).

## Specifying conditions in a policy
<a name="specifying-conditions"></a>

When you grant permissions, you can use the IAM policy language to specify the conditions when a policy should take effect. For example, you might want a policy to be applied only after a specific date. For more information about specifying conditions in a policy language, see [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*. 

AWS supports global condition keys and service-specific condition keys. To see all global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

AWS Backup defines its own set of condition keys. To see a list of AWS Backup condition keys, see [Condition keys for AWS Backup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackup.html#awsbackup-policy-keys) in the *Service Authorization Reference*.

For restore testing selections, AWS Backup passes the IAM role to the service principal `restore-testing.backup.amazonaws.com`, not `backup.amazonaws.com`. If you use the [`iam:PassedToService`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_PassedToService) condition key for `CreateRestoreTestingSelection` or `UpdateRestoreTestingSelection`, set the value to `restore-testing.backup.amazonaws.com`. For more information, see [Using roles for restore testing](using-service-linked-roles-AWSServiceRoleForBackupRestoreTesting.md).

## API permissions: actions, resources, and conditions reference
<a name="backup-api-permissions-ref"></a>

When you are setting up [Access control](#access-control) and writing a permissions policy that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference. The table lists each AWS Backup API operation, the corresponding actions for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field. If `Resource` field is blank, you can use the wildcard (`*`) to include all resources.

You can use AWS-wide condition keys in your AWS Backup policies to express conditions. For a complete list of AWS-wide keys, see [Available Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

Use the scroll bars to see the rest of the table.


**AWS Backup API and required permissions for actions**  

| AWS Backup API operations | Required permissions (API actions) | Resources | 
| --- | --- | --- | 
|  [CreateBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupAccessPoint.html)  | `backup:CreateBackupAccessPoint`<br />`s3:CreateAccessPoint`<br />`s3:GetAccessPoint` | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | 
|  [CreateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupPlan.html)  | backup:CreateBackupPlan | arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\* | 
|  [CreateBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupSelection.html)  | backup:CreateBackupSelection | arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\* | 
|  [CreateBackupVault](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupVault.html)  | `backup:CreateBackupVault`<br />`backup-storage:MountCapsule`<br />`kms:CreateGrant`<br />`kms:GenerateDataKey`<br />`kms:Decrypt`<br />`kms:RetireGrant`<br />`kms:DescribeKey` | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*For `backup-storage`: \*<br />For `kms`: `arn:aws:kms:{{region}}:{{account-id}}:key/{{keystring}}` | 
|  [DeleteBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupAccessPoint.html)  | `backup:DeleteBackupAccessPoint`<br />`s3:GetAccessPoint`<br />`s3:DeleteAccessPoint` | arn:aws:backup:{{region}}:{{account-id}}:accesspoint/\* | 
|  [DeleteBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupPlan.html)  | backup:DeleteBackupPlan | arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\* | 
|  [DeleteBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupSelection.html)  | backup:DeleteBackupSelection | arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\* | 
|  [DeleteBackupVault](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVault.html)  | backup:DeleteBackupVault 1 | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\* | 
|  [DeleteBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVaultAccessPolicy.html)  | backup:DeleteBackupVaultAccessPolicy | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\* | 
|  [DeleteBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupVaultNotifications.html)  |  backup:DeleteBackupVaultNotifications 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [DeleteRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteRecoveryPoint.html)  |  backup:DeleteRecoveryPoint 1  | 2 | 
|  [DescribeBackupAccessPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeBackupAccessPoint.html)  | `backup:DescribeBackupAccessPoint`<br />`s3:GetAccessPoint` | arn:aws:backup:{{region}}:{{account-id}}:accesspoint/\* | 
|  [DescribeBackupJob](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeBackupJob.html)  | backup:DescribeBackupJob |  | 
|  [DescribeBackupVault](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeBackupVault.html)  |  backup:DescribeBackupVault 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [DescribeProtectedResource](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeProtectedResource.html)  | backup:DescribeProtectedResource |  | 
|  [DescribeRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeRecoveryPoint.html)  |  backup:DescribeRecoveryPoint 1  | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*2 | 
|  [DescribeRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeRestoreJob.html)  | backup:DescribeRestoreJob |  | 
|  [DescribeRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeRegionSettings.html)  |  backup:DescribeRegionSettings  |  | 
|  [ExportBackupPlanTemplate](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ExportBackupPlanTemplate.html)  | backup:ExportBackupPlanTemplate |  | 
|  [GetBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupPlan.html)  | backup:GetBackupPlan |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [GetBackupPlanFromJSON](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupPlanFromJSON.html)  | backup:GetBackupPlanFromJSON |  | 
|  [GetBackupPlanFromTemplate](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupPlanFromTemplate.html)  | backup:GetBackupPlanFromTemplate |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [GetBackupSelection](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupSelection.html)  | backup:GetBackupSelection |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [GetBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupVaultAccessPolicy.html)  |  backup:GetBackupVaultAccessPolicy 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [GetBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupVaultNotifications.html)  |  backup:GetBackupVaultNotifications 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [GetRecoveryPointRestoreMetadata](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRecoveryPointRestoreMetadata.html)  |  backup:GetRecoveryPointRestoreMetadata 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [GetSupportedResourceTypes](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetSupportedResourceTypes.html)  | backup:GetSupportedResourceTypes |  | 
|  [ListBackupAccessPoints](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupAccessPoints.html)  | backup:ListBackupAccessPoints |  | 
|  [ListBackupAccessPointsByRecoveryPoint](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupAccessPointsByRecoveryPoint.html)  | backup:ListBackupAccessPointsByRecoveryPoint | arn:aws:backup:{{region}}:{{account-id}}:recovery-point:\* | 
|  [ListBackupAccessPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupAccessPointsByResource.html)  | backup:ListBackupAccessPointsByResource |  | 
|  [ListBackupJobs](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupJobs.html)  | backup:ListBackupJobs |  | 
|  [ListBackupPlans](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupPlans.html)  | backup:ListBackupPlans |  | 
|  [ListBackupPlanTemplates](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupPlanTemplates.html)  | backup:ListBackupPlanTemplates |  | 
|  [ListBackupPlanVersions](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupPlanVersions.html)  | backup:ListBackupPlanVersions |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [ListBackupSelections](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupSelections.html)  | backup:ListBackupSelections |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [ListBackupVaults](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupVaults.html)  | backup:ListBackupVaults |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [ListProtectedResources](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListProtectedResources.html)  | backup:ListProtectedResources |  | 
|  [ListRecoveryPointsByBackupVault](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRecoveryPointsByBackupVault.html)  |  backup:ListRecoveryPointsByBackupVault 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [ListRecoveryPointsByResource](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRecoveryPointsByResource.html)  | backup:ListRecoveryPointsByResource |  | 
|  [ListRestoreJobs](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRestoreJobs.html)  | backup:ListRestoreJobs |  | 
|  [ListTags](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListTags.html)  | backup:ListTags |  | 
|  [PutBackupVaultAccessPolicy](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutBackupVaultAccessPolicy.html)  |  backup:PutBackupVaultAccessPolicy 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [PutBackupVaultLockConfiguration](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutBackupVaultLockConfiguration.html)  |  backup:PutBackupVaultLockConfiguration 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [PutBackupVaultNotifications](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutBackupVaultNotifications.html)  |  backup:PutBackupVaultNotifications 1  |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [StartBackupJob](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StartBackupJob.html)  | backup:StartBackupJob |  arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*  | 
|  [StartRestoreJob](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StartRestoreJob.html)  | backup:StartRestoreJob | `arn:aws:backup:{{region}}:{{account-id}}:backup-vault:*`<br />`arn:aws:backup:{{region}}:{{account-id:}}recovery-point:*`<br />3 | 
|  [StopBackupJob](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StopBackupJob.html)  | backup:StopBackupJob |  | 
|  [TagResource](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_TagResource.html)  | backup:TagResource | arn:aws:backup:{{region}}:{{account-id:}}recovery-point:\* | 
|  [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UntagResource.html)  | backup:UntagResource |  | 
|  [UpdateBackupPlan](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateBackupPlan.html)  | backup:UpdateBackupPlan |  arn:aws:backup:{{region}}:{{account-id}}:backup-plan:\*  | 
|  [UpdateRecoveryPointLifecycle](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRecoveryPointLifecycle.html)  |  backup:UpdateRecoveryPointLifecycle 1  | arn:aws:backup:{{region}}:{{account-id}}:backup-vault:\*2 | 
|  [UpdateRegionSettings](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRegionSettings.html)  | `backup:UpdateRegionSettings`<br />`backup:DescribeRegionSettings` |  | 

1 Uses the existing vault access policy.

2 See [AWS Backup resource ARNs](#resource-arns-table) for resource-specific recovery point ARNs.

3 `StartRestoreJob` must have the key-value pair in the metadata for the resource. To get the metadata of the resource, call the `GetRecoveryPointRestoreMetadata` API.

For more information, see [Actions, resources, and condition keys for AWS Backup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackup.html) in the *Service Authorization Reference*.

## Copy tags permissions
<a name="copy-tags"></a>

When AWS Backup performs a backup or copy job, it attempts to copy the tags from your source resource (or recovery point in the case of copy) to your recovery point.

**Note**  
AWS Backup does **not** natively copy tags during restore jobs. For an event-driven architecture that will copy tags during restore jobs, see [How to retain resource tags in AWS Backup restore jobs](https://aws.amazon.com/blogs/storage/how-to-retain-resource-tags-in-aws-backup-restore-jobs/).

During a backup or copy job, AWS Backup aggregates the tags you specify in your backup plan (or copy plan, or on-demand backup) with the tags from your source resource. However, AWS enforces a limit of 50 tags per resource, which AWS Backup cannot exceed. When a backup or copy job aggregates tags from the plan and the source resource, it might discover more than 50 total tags, it will be unable to complete the job, and will fail the job. This is consistent with AWS-wide tagging best practices.
+ Your resource has more than 50 tags after aggregating your backup job tags with your source resource tags. AWS supports up to 50 tags per resource.
+ The IAM role you provide to AWS Backup lacks permissions to read the source tags or set the destination tags. For more information and sample IAM role policies, see [Managed Policies](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies).

You can use your backup plan (tags added to recovery points) to create tags that contradict your source resource tags. When the two conflict, the tags from your backup plan take precedence. Use this technique if you prefer not to copy a tag value from your source resource. Specify the same tag key, but different or empty value, using your backup plan.


**Permissions Required to assign tags to backups**  

| Resource type | Required permission | 
| --- | --- | 
| Amazon EFS file system | `elasticfilesystem:DescribeTags` | 
| Amazon FSx file system | `fsx:ListTagsForResource` | 
| Amazon RDS database and Amazon Aurora cluster | `rds:AddTagsToResource`<br />`rds:ListTagsForResource` | 
| Storage Gateway volume | `storagegateway:ListTagsForResource` | 
| Amazon EC2 instance and Amazon EBS volume | `EC2:CreateTags`<br />`EC2:DescribeTags` | 

DynamoDB does not support assigning tags to backups unless you first enable [Advanced DynamoDB backup](advanced-ddb-backup.md).

When an Amazon EC2 backup creates an Image Recovery Point and a set of snapshots, AWS Backup copies tags to the resulting AMI. AWS Backup also copies the tags from the volumes associated with the Amazon EC2 instance to the resulting snapshots.

## Access policies
<a name="access-policies"></a>

A *permissions* policy describes who has access to what. Policies attached to an IAM identity are referred to as *identity-based* policies (IAM policies). Policies attached to a resource are referred to as *resource-based* policies. AWS Backup supports both identity-based policies and resource-based policies.

**Note**  
This section discusses using IAM in the context of AWS Backup. It doesn't provide detailed information about the IAM service. For complete IAM documentation, see [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*. For information about IAM policy syntax and descriptions, see [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

### Identity-based policies (IAM policies)
<a name="identity-based-policies"></a>

Identity-based policies are policies that you can attach to IAM identities, such as users or roles. For example, you can define a policy that allows a user to view and back up AWS resources, but prevents them from restoring backups.

For more information about users, groups, roles, and permissions, see [Identities (Users, Groups, and Roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

For information about how to use IAM policies to control access to backups, see [Managed policies for AWS Backup](security-iam-awsmanpol.md).

### Resource-based policies
<a name="resource-based-policies"></a>

AWS Backup supports resource-based access policies for backup vaults. This enables you to define an access policy that can control which users have what kind of access to any of the backups organized in a backup vault. Resource-based access policies for backup vaults provide an easy way to control access to your backups. 

Backup vault access policies control user access when you use AWS Backup APIs. Some backup types, such as Amazon Elastic Block Store (Amazon EBS) and Amazon Relational Database Service (Amazon RDS) snapshots, can also be accessed using those services' APIs. You can create separate access policies in IAM that control access to those APIs in order to fully control access to backups.

To learn how to create an access policy for backup vaults, see [Vault access policies](create-a-vault-access-policy.md).