# Considerations for Amazon EBS snapshot lock

Keep the following in mind when locking Amazon EBS snapshots.

- You can lock a snapshot only if it is in the `pending` or `completed`
  state.
  - If you lock a snapshot while it is in the `pending` state, and you lock
    it for a specific duration, the lock duration starts only when the snapshot reaches
    the `completed` state. The snapshot can't be deleted while it is in the
    `pending` state.
  - If you lock a snapshot while it is in the `pending` state and the snapshot
    creation fails for any reason, the lock is canceled.

- If you extend the lock duration for a snapshot that is locked in compliance mode
  after the cooling-off period has expired, you can't specify another cooling-off period.
  If you specify a cooling-off period, the request fails.
- You can lock archived snapshots. And you can archive locked snapshots.
- You can lock snapshots that are associated with an AMI.
- You can deregister an AMI that has associated snapshots that are locked.
- You can delete the KMS key used to encrypt a locked snapshot.
- We recommend that you do not lock snapshots created by AWS Backup. AWS Backup already ensures
  that its snapshots are not deleted before their retention period expires. To add an
  additional layer of security for snapshots managed by AWS Backup, we recommend that you use
  AWS Backup Vault Lock. For more information, see [AWS Backup Vault Lock](../../../aws-backup/latest/devguide/vault-lock.md "../../../aws-backup/latest/devguide/vault-lock.md").
- You can't lock snapshots during creation or during AMI registration.
- You can't lock local Amazon EBS snapshots on AWS Outposts.
- The only way to delete a snapshot that is locked in compliance mode before its lock
  expires is to close the associated AWS account.

If you close your AWS account while you have locked snapshots, AWS suspends your
account for 90 days with your snapshots intact. If you do not reopen your account
within the 90 days, AWS deletes your snapshots, even if they are locked.
