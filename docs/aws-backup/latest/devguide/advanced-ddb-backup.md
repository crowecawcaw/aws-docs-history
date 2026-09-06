

# Advanced DynamoDB backup
<a name="advanced-ddb-backup"></a>

AWS Backup supports additional, advanced features for your Amazon DynamoDB data protection needs.

Customers who started using AWS Backup after November 2021 have advanced DynamoDB backup features enabled by default. Specifically, advanced DynamoDB backup features are enabled by default to customers who have not created a backup vault prior to November 21, 2021.

It's best practice for existing AWS Backup customers to enable advanced features for DynamoDB. There is no difference in warm backup storage pricing after you enable advanced features. You can potentially save money by moving backups to cold storage and optimize your costs by using cost allocation tags. You can also start taking advantage of AWS Backup's cross-Region and cross-account copy and security features.

**Topics**
+ [Benefits of advanced DDB backup](#advanced-ddb-backup-benefits)
+ [Considerations for Advanced DynamoDB backup](#advanced-ddb-considerations)
+ [Understanding backup overlap and costs](#advanced-ddb-backup-overlap-costs)
+ [Enabling advanced DynamoDB backup using the console](#advanced-ddb-backup-enable-console)
+ [Enabling advanced DynamoDB backup programmatically](#advanced-ddb-backup-enable-cli)
+ [Editing an advanced DynamoDB backup](#advanced-ddb-backup-edit)
+ [Restoring an advanced DynamoDB backup](#advanced-ddb-backup-restore)
+ [Deleting an advanced DynamoDB backup](#advanced-ddb-backup-delete)
+ [Other benefits of full AWS Backup management when you enable advanced DynamoDB backup](#advanced-ddb-backup-other-benefits)

## Benefits of advanced DDB backup
<a name="advanced-ddb-backup-benefits"></a>

After you enable AWS Backup's advanced features in your AWS Region, you unlock the following features for all new for DynamoDB table backups you create:
+ Cost savings and optimization:
  + [Tiering backups to cold storage](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Lifecycle.html) to reduce storage costs
  + [ Cost allocation tagging for use with Cost Explorer](https://docs.aws.amazon.com/aws-backup/latest/devguide/metering-and-billing.html#cost-allocation-tags)
+ Additional copy options:
  + [Cross-Region copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html)
  + [Cross-account copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html#prereq-cab)
+ Security:
  + Backups inherit tags from their source DynamoDB tables, allowing you to use those tags to set permissions and [ service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

## Considerations for Advanced DynamoDB backup
<a name="advanced-ddb-considerations"></a>

**Opting in**

Backups, including those of Advanced DDB resources, can be created by a backup plan, an on-demand backup, or through a backup policy. Backups created by a plan or on-demand will automatically opt-in your account to allow backups of Advanced DDB resources.

If your backup job is created by a backup policy, you need to manually opt-in to Advanced DynamoDB backups, either through the [Backup console](assigning-resources-console.md) or through [CLI](assigning-resources-json.md).

**Custom policies and roles**

If you use a custom role or policy instead of AWS Backup's default service role, you must add or use the following permissions policies (or add their equivalent permissions) to your custom role:
+ `AWSBackupServiceRolePolicyForBackup` to perform advanced DynamoDB backup.
+ `AWSBackupServiceRolePolicyForRestores` to restore advanced DynamoDB backups.

To learn more about AWS-managed policies and view examples of customer-managed policies, see [Managed policies for AWS Backup](security-iam-awsmanpol.md).

## Understanding backup overlap and costs
<a name="advanced-ddb-backup-overlap-costs"></a>

AWS Backup advanced DynamoDB features provide periodic snapshot-based backups with additional capabilities. These do not replace or duplicate native DynamoDB point-in-time recovery (PITR), which provides continuous backup with second-level granularity. If your recovery strategy requires both periodic snapshots (for long-term retention, cross-Region DR, or compliance) and continuous recovery (for operational recovery within a short window), you may choose to enable both AWS Backup advanced features and native DynamoDB PITR. In this case, you will incur charges for both — this is intentional complementary protection, not unintended duplication. If your recovery requirements are met by periodic snapshots alone, native DynamoDB PITR can be disabled to reduce costs.

## Enabling advanced DynamoDB backup using the console
<a name="advanced-ddb-backup-enable-console"></a>

You can enable AWS Backup advanced features for DynamoDB backups using either the AWS Backup or DynamoDB console.

**To enable advanced DynamoDB backup features from the AWS Backup console:**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation menu, choose **Settings**.

1. Under the **Supported services** section, verify that **DynamoDB** is **Enabled**.

   If it is not, choose **Opt-in** and enable DynamoDB as an AWS Backup supported service.

1. Under the **Advanced features for DynamoDB backups** section, choose **Enable**.

1. Choose **Enable features**.

For how to enable AWS Backup advanced features using the DynamoDB console, see [ Enabling AWS Backup features](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html#CreateBackupAWS_enabling) in the *Amazon DynamoDB User Guide*.

## Enabling advanced DynamoDB backup programmatically
<a name="advanced-ddb-backup-enable-cli"></a>

You can also enable AWS Backup advanced features for DynamoDB backups using the AWS Command Line Interface (CLI). You enable advanced DynamoDB backups when you set both of the following values to `true`:

**To programmatically enable AWS Backup advanced features for DynamoDB backups:**

1. Check if you already enabled AWS Backup advanced features for DynamoDB using the following command:

   ```
   $ aws backup describe-region-settings
   ```

   If `"DynamoDB":true` under both `"ResourceTypeManagementPreference"` and `"ResourceTypeOptInPreference"`, you have already enabled advanced DynamoDB backup.

   If, like the following output, you have at least one instance of `"DynamoDB":false`, you have not yet enabled advanced DynamoDB backup, proceed to the next step.

   ```
   {
     "ResourceTypeManagementPreference":{
       "DynamoDB":false,
       "EFS":true
     }
     "ResourceTypeOptInPreference":{
       "Aurora":true,
       "DocumentDB":false,
       "DynamoDB":false,
       "EBS":true,
       "EC2":true,
       "EFS":true,
       "FSx":true,
       "Neptune":false,
       "RDS":true,
       "Storage Gateway":true
     }
   }
   ```

1. Use the following [`UpdateRegionSettings`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UpdateRegionSettings.html) operation to set both `"ResourceTypeManagementPreference"` and `"ResourceTypeOptInPreference"` to `"DynamoDB":true`:

   ```
   aws backup update-region-settings \ 
                 --resource-type-opt-in-preference DynamoDB=true \
                 --resource-type-management-preference DynamoDB=true
   ```

## Editing an advanced DynamoDB backup
<a name="advanced-ddb-backup-edit"></a>

When you create a DynamoDB backup after you enable AWS Backup advanced features, you can use AWS Backup to:
+ Copy a backup across Regions
+ Copy a backup across accounts
+ Change when AWS Backup tiers a backup to cold storage
+ Tag the backup

To use those advanced features on an existing backup, see [ Editing a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/editing-a-backup.html).

If you later disable AWS Backup advanced features for DynamoDB, you can continue to perform those operations to DynamoDB backups that you created during the period of time when you enabled advanced features.

## Restoring an advanced DynamoDB backup
<a name="advanced-ddb-backup-restore"></a>

You can restore DynamoDB backups taken with AWS Backup advanced features enabled in the same way you restore DynamoDB backups taken prior to enabling AWS Backup advanced features. You can perform a restore using either AWS Backup or DynamoDB.

You can specify how to encrypt your newly-restored table with the following options:
+ When you restore in the same Region as your original table, you can optionally specify an encryption key for your restored table. If you do not specify an encryption key, AWS Backup will automatically encrypt your restored table using the same key that encrypted your original table.
+ When you restore in a different Region than your original table, you must specify an encryption key.

 To restore using AWS Backup, see [Restore a Amazon DynamoDB table](restoring-dynamodb.md).

To restore using DynamoDB, see [Restoring a DynamoDB table from a backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html) in the *Amazon DynamoDB User Guide*.

## Deleting an advanced DynamoDB backup
<a name="advanced-ddb-backup-delete"></a>

You cannot delete backups created using these advanced features in DynamoDB. You must use AWS Backup to delete backups to maintain global consistency throughout your AWS environment.

To delete a DynamoDB backup, see [Backup deletion](deleting-backups.md).

## Other benefits of full AWS Backup management when you enable advanced DynamoDB backup
<a name="advanced-ddb-backup-other-benefits"></a>

When you enable AWS Backup advanced features for DynamoDB, you give full management of your DynamoDB backups to AWS Backup. Doing so gives you the following, additional benefits:

**Encryption**

AWS Backup automatically encrypts the backups with the KMS key of your destination AWS Backup vault. Previously, they were encrypted using the same encryption method of your source DynamoDB table. This increases the number of defenses you can use to safeguard your data. See [Encryption for backups in AWS Backup](encryption.md) for more information.

**Amazon Resource Name (ARN)**

Each backup ARN’s service namespace is `awsbackup`. Previously, the service namespace was `dynamodb`. Put another way, the beginning of each ARN will change from `arn:aws:dynamodb` to `arn:aws:backup`. See [ARNs for AWS Backup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbackup.html#awsbackup-resources-for-iam-policies) in the *Service Authorization Reference*.

With this change, you or your backup administrator can create access policies for backups using the `awsbackup` service namespace that now apply to DynamoDB backups created after you enable advanced features. By using the `awsbackup` service namespace, you can also apply policies to other backups taken by AWS Backup. See [Access control](access-control.md) for more information.

**Location of charges on billing statement**

Charges for backups (including storage, data transfers, restores, and early deletion) appear under “Backup” in your AWS bill. Previously, charges appeared under “DynamoDB” in your bill.

This change ensures that you can use AWS Backup billing to centrally monitor your backup costs. See [Metering, costs, and billing for AWS Backup](metering-and-billing.md) for more information.