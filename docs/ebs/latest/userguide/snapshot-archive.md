# Archive Amazon EBS snapshots

Amazon EBS Snapshots Archive is a storage tier that you can use for low-cost, long-term storage
of your rarely-accessed snapshots that do not need frequent or fast retrieval.

By default, when you create a snapshot, it is stored in the Amazon EBS Snapshot Standard tier
(_standard tier_). Snapshots stored in the standard tier are incremental. This means
that only the blocks on the volume that have changed after your most recent snapshot are saved.

When you archive a snapshot, the incremental snapshot is converted to a full snapshot, and it is
moved from the standard tier to the Amazon EBS Snapshots Archive tier (_archive tier_).
Full snapshots include all of the blocks that were written to the volume at the time when the snapshot
was created.

When you need to access an archived snapshot, you can restore it from the archive tier to the
standard tier, and then use it in the same way that you use any other snapshot in your account.

Amazon EBS Snapshots Archive offers up to 75 percent lower snapshot storage costs for snapshots
that you plan to store for 90 days or longer and that you rarely need to access.

Some typical use cases include:

- Archiving the only snapshot of a volume, such as end-of-project snapshots
- Archiving full, point-in-time incremental snapshots for compliance reasons.
- Archiving monthly, quarterly, or yearly incremental snapshots.

###### Topics

- [Quotas](#archive-quotas "#archive-quotas")
- [Considerations and limitations](snapshot-archive-considerations.md "snapshot-archive-considerations.md")
- [Pricing and billing](snapshot-archive-pricing.md "snapshot-archive-pricing.md")
- [Guidelines and best practices](archiving-guidelines.md "archiving-guidelines.md")
- [Required permissions](snapshot-archiving-iam.md "snapshot-archiving-iam.md")
- [Archive a snapshot](archive-snapshot.md "archive-snapshot.md")
- [Restore an archived snapshot](restore-archived-snapshot.md "restore-archived-snapshot.md")
- [Modify the restore period](modify-temp-restore-period.md "modify-temp-restore-period.md")
- [View archived snapshots](view-archived-snapshot.md "view-archived-snapshot.md")
- [Monitor snapshot archiving](monitor-snapshot-archiving.md "monitor-snapshot-archiving.md")

## Quotas

This section describes the default quotas for archived and in-progress snapshots.

| Quota                                                | Default quota |
| ---------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Archived snapshots per volume                        | 25            |
| Concurrent in-progress snapshot archives per account | 25            |
| Concurrent in-progress snapshot restores per account | 5             | If you need more than the default limits, complete the Support Center [Create case](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ebs "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ebs") form to request a limit increase. |
