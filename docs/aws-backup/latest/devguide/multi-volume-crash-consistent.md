# Amazon EBS and AWS Backup

The backup process for Amazon EBS resources is similar to the steps used to back up
other resources types:

- [Create an on-demand backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md")
- [Create a scheduled backup](creating-a-backup-plan.md "creating-a-backup-plan.md")
  Resource-specific information is noted in the following sections.

## Amazon EBS Archive Tier for cold storage

EBS is one of the resource that supports a transition of backups to cold storage. For
more information, see [Lifecycle and storage tiers](plan-options-and-configuration.md#backup-lifecycle "plan-options-and-configuration.md#backup-lifecycle").

## Amazon EBS multi-volume, crash-consistent backups

By default, AWS Backup creates crash-consistent backups of Amazon EBS volumes that are attached to
an Amazon EC2 instance. Crash consistency means that the snapshots for every Amazon EBS volume
attached to the same Amazon EC2 instance are taken at the exact same moment. You no longer have
to stop your instances or coordinate between multiple Amazon EBS volumes to ensure
crash-consistency of your application state.

Since multi-volume, crash-consistent snapshots are a default AWS Backup functionality, you
don’t need to do anything different to use this feature.

The role used to create an EBS snapshot recovery point is associated with that snapshot.
This same role must be used to delete recovery points created by it or to transition recovery
points of it to an archive tier.

## Amazon EBS Snapshot Lock and AWS Backup

AWS Backup managed Amazon EBS snapshots and snapshots associated with a AWS Backup managed Amazon EC2 AMI
which have Amazon EBS Snapshot Lock applied may not be deleted as part of the recovery point
lifecycle if the snapshot lock duration exceeds the backup lifecycle. Instead, these
recovery points will have the status of `EXPIRED`. These recovery points can be
[deleted
manually](deleting-backups.md#deleting-backups-manually "deleting-backups.md#deleting-backups-manually") if you choose to first remove the Amazon EBS snapshot lock.

## Restoring Amazon EBS resources

To restore your Amazon EBS volumes, follow the steps in [Restoring an Amazon EBS volume](restoring-ebs.md "restoring-ebs.md").
