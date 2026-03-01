# Backup and tag copy

You can copy backups to multiple AWS accounts or AWS Regions on demand or
automatically as part of a scheduled backup plan for most resource types, though backups in
cold storage or archive tiers cannot be copied. See [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") and
[Encryption for a backup copy to a
different account or AWS Region](encryption.md#copy-encryption "encryption.md#copy-encryption") for details.

Some resource types have both continuous backup capability and cross-Region and
cross-account copy available. When a cross-Region or cross-account copy of a continuous backup
is made, the copied recovery point (backup) becomes a snapshot (periodic) backup (not
available for all resource types that support both backup types). Depending on the [resource type](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource"), the snapshots may be an incremental
copy or a full copy. PITR (Point-in-Time Restore) is not available for these copies.

###### Important

Copies retain their source configuration, including creation dates and retention period.
The creation date refers to when the source was created, not when the copy was created. You
can override the retention period.

The configuration of the source backup being copied overrides its
copy’s expiration setting if the copy retention period is set to **Always**
in the AWS Backup console (or [`DeleteAfterDays`](API_CopyAction.md#Backup-Type-CopyAction-Lifecycle "API_CopyAction.md#Backup-Type-CopyAction-Lifecycle") value is set to `-1` in the API
request); that is, a copy with a retention setting set to never expire will
retain its source recovery point's expiration date.

If you want your backup copies to never expire, either set your source backups to never
expire or specify your copy to expire 100 years after its creation.

## Copy job retry

AWS Backup implements the following retry strategy for copy jobs: If AWS Backup
encounters any system errors, the copy job enters a retry phase that lasts for 2 hours.
During this time, the copy job status remains in the `CREATED` state while the system
periodically attempts to initiate the job. If the job successfully starts within this
window, it transitions to the `RUNNING` state.

If issues persist beyond the 2-hour retry period, the AWS Backup service team is
automatically alerted. The team then investigates and addresses any underlying problems.
Once resolved, they manually retry the copy request, ensuring that the copy jobs are
completed as requested.

The copy job retry process differs from backup job retry process, which uses a defined
start window with regular retry attempts until either success or expiration. The copy job
mechanism provides an additional layer of reliability by incorporating direct service team
intervention for persistent issues.

###### Contents

- [Creating backup copies across AWS Regions](cross-region-backup.md "cross-region-backup.md")
- [Creating backup copies across AWS accounts](create-cross-account-backup.md "create-cross-account-backup.md")
- [Copy tags onto backups](tags-on-backups.md "tags-on-backups.md")
