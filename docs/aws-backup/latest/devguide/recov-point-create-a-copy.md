

# Backup and tag copy
<a name="recov-point-create-a-copy"></a>

You can copy backups to multiple AWS accounts or AWS Regions on demand or automatically as part of a scheduled backup plan for most resource types, though backups in cold storage or archive tiers cannot be copied. See [Feature availability by resource](backup-feature-availability.md#features-by-resource) and [Encryption for a backup copy to a different account or AWS Region](encryption.md#copy-encryption) for details.

**Note**  
If a resource type does not support cross-Region or cross-account copy in AWS Backup, then copy operations for that resource type are not supported in any scenario, including same-Region and same-account copies to a different vault. To determine which resource types support copy operations, see the Cross-Region backup and Cross-account backup columns in [Feature availability by resource](backup-feature-availability.md#features-by-resource). If the underlying AWS service provides its own native copy or replication feature, refer to that service's documentation.

**Note**  
AWS Backup does not provide any service-level agreements (SLAs) for copy job completion times. Copy times can vary based upon system load, capacity, and the size of the resources being copied, even for copy jobs containing the same resources.

Some resource types have both continuous backup capability and cross-Region and cross-account copy available. When a cross-Region or cross-account copy of a continuous backup is made, the copied recovery point (backup) becomes a snapshot (periodic) backup (not available for all resource types that support both backup types). Depending on the [resource type](backup-feature-availability.md#features-by-resource), the snapshots may be an incremental copy or a full copy. PITR (Point-in-Time Restore) is not available for these copies.

**Important**  
Copies retain their source configuration, including creation dates and retention period. The creation date refers to when the source was created, not when the copy was created. You can override the retention period.  
The configuration of the source backup being copied overrides its copy’s expiration setting if the copy retention period is set to **Always** in the AWS Backup console (or [`DeleteAfterDays`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CopyAction.html#Backup-Type-CopyAction-Lifecycle) value is set to `-1` in the API request); that is, a copy with a retention setting set to never expire will retain its source recovery point's expiration date.  
If you want your backup copies to never expire, either set your source backups to never expire or specify your copy to expire 100 years after its creation.

## Copy job retry
<a name="backup-copy-retry"></a>

AWS Backup implements the following retry strategy for copy jobs: If AWS Backup encounters any system errors, the copy job enters a retry phase that lasts for 2 hours. During this time, the copy job status remains in the `CREATED` state while the system periodically attempts to initiate the job. If the job successfully starts within this window, it transitions to the `RUNNING` state.

If issues persist beyond the 2-hour retry period, the AWS Backup service team is automatically alerted. The team then investigates and addresses any underlying problems. After the issue is resolved, they manually retry the copy request, ensuring that the copy jobs are completed as requested.

The copy job retry process differs from backup job retry process, which uses a defined start window with regular retry attempts until either success or expiration. The copy job mechanism provides an additional layer of reliability by incorporating direct service team intervention for persistent issues.

## Copy job concurrency
<a name="backup-copy-concurrency"></a>

Only one backup or copy job can run at a time for a given resource. Additional copy jobs for the same resource remain in `CREATED` status until the running job completes. For more information about concurrency limits, see [AWS Backup quotas](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-limits.html).

Copy jobs for large resources can take several hours to complete, which can result in additional copy jobs waiting in `CREATED` status. For resource types that support incremental copies, a short retention period can lead to situations where the only recovery point in the destination vault expires. If no recovery point exists in the destination vault, then the next copy must be a full copy instead of an incremental copy. To avoid this, set the copy retention period to at least one week. For more information, see [Metering, costs, and billing](https://docs.aws.amazon.com/aws-backup/latest/devguide/metering-and-billing.html). To determine which resource types support incremental copies, see [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource).

If copy jobs continue to queue in `CREATED` status for the same resource, reduce the copy frequency.

**Topics**
+ [Copy job retry](#backup-copy-retry)
+ [Copy job concurrency](#backup-copy-concurrency)
+ [Creating backup copies across AWS Regions](cross-region-backup.md)
+ [Creating backup copies across AWS accounts](create-cross-account-backup.md)
+ [Copy tags onto backups](tags-on-backups.md)