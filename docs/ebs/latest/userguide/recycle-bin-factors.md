# Considerations for Recycle Bin

The following considerations apply when working with Recycle Bin and retention rules.

###### General considerations

- Deleted resources are moved to the Recycle Bin only if they match an existing
  retention rule. If you delete a resource that does not match a retention rule, or
  if you do not have any retention rules at that time, that resource is permanently
  deleted; it is not moved to the Recycle Bin.
- ###### Important

Retention rules follow an eventual consistency model for the first retention rule
created per resource type, per Region in your account. When you create your first
retention rule for a resource type in a Region, that rule might not become active and
start retaining resources immediately. However, any subsequent retention rules you
create for that same resource type in the same Region will become active and start
retaining resources almost immediately.

- If a resource matches more than one retention rule upon deletion, then the retention
  rule with the longest retention period takes precedence.
- You can't manually delete a resource from the Recycle Bin. The resource will be
  automatically deleted when its retention period expires.
- While a resource is in the Recycle Bin, you can only view it, restore it, or modify
  its tags. To use the resource in any other way, you must first restore it.
- If any AWS service, such as AWS Backup or Amazon Data Lifecycle Manager, deletes a resource that matches
  a retention rule, that resource is automatically retained by Recycle Bin. If needed,
  you can prevent these resources from entering into Recycle Bin upon deletion by
  tagging those resources and then adding those tags as exclusion tags to your retention
  rules.
- When a resource is sent to the Recycle Bin, the following system-generate tag is
  assigned to the resource:

      + Tag key — `aws:recycle-bin:resource-in-bin`
      + Tag value — `true`

  You can't manually edit or delete this tag. When the resource is restored from the
  Recycle Bin, the tag is automatically removed.

###### Considerations for volumes

- Volumes deleted due to instance termination or root volume replacement are protected by
  Recycle Bin.
- Volumes that fail to be created are not protected by Recycle Bin on deletion.
- Volumes of failed instance launches are not protected by Recycle Bin on deletion.
- Volumes of managed instances are not protected by Recycle Bin on deletion.
- Ongoing volume creation or modification will not be paused when the volume enters
  Recycle Bin. This means that you are still billed accordingly if the volume was created
  with an Amazon EBS Provisioned Rate for Volume Initialization.
- Volumes in Recycle Bin count towards your quotas in the same way as regular volumes.
- Volumes in Recycle Bin are not billed after their Recycle Bin exit time has elapsed. You
  cannot restore these volumes but you can discover them if they have not yet been deleted.
- The `deleteVolume` event will be sent only after the volume is deleted from
  Recycle Bin. This event is not emitted when the volume enters Recycle Bin.

###### Considerations for snapshots

- ###### Important

If you have retention rules for AMIs and for their associated snapshots, make the retention
period for the snapshots the same or longer than the retention period for the AMIs. This
ensures that Recycle Bin does not delete the snapshots associated with an AMI before deleting
the AMI itself, as this would make the AMI unrecoverable.

- If a snapshot is enabled for fast snapshot restore when it is deleted, fast snapshot
  restore is automatically disabled shortly after the snapshot is sent to the Recycle Bin.
  - If you restore the snapshot before fast snapshot restore is disabled for the
    snapshot, it remains enabled.
  - If you restore the snapshot, after fast snapshot restore has been disabled,
    it remains disabled. If needed, you must
    manually re-enable fast snapshot restore.

- If a snapshot is shared when it is deleted, it is automatically unshared when it is sent
  to the Recycle Bin. If you restore the snapshot, all of the previous sharing
  permissions are automatically restored.
- If a snapshot that was created by another AWS service, such as AWS Backup is sent to the
  Recycle Bin and you later restore that snapshot from the Recycle Bin, it is
  no longer managed by the AWS service that created it. You must manually delete
  the snapshot if it is no longer needed.

###### Considerations for AMIs

- Only Amazon EBS-backed AMIs are supported.
- ###### Important

If you have retention rules for AMIs and for their associated snapshots, make the retention
period for the snapshots the same or longer than the retention period for the AMIs. This
ensures that Recycle Bin does not delete the snapshots associated with an AMI before deleting
the AMI itself, as this would make the AMI unrecoverable.

- If an AMI is shared when it is deleted, it is automatically unshared when it is sent to
  the Recycle Bin. If you restore the AMI, all of the previous sharing permissions are
  automatically restored.
- Before you can restore an AMI from the Recycle Bin, you must first restore all of its
  associated snapshots from the Recycle Bin and ensure that they are in the `available`
  state.
- If the snapshots that are associated with the AMI are deleted from the Recycle Bin, the
  AMI is no longer recoverable. The AMI will be deleted when the retention period expires.
- If an AMI that was created by another AWS service, such as AWS Backup, is sent to the
  Recycle Bin and you later restore that AMI from the Recycle Bin, it is no longer
  managed by the AWS service that created it. You must manually delete the AMI if it is no
  longer needed.

###### Considerations for Amazon Data Lifecycle Manager snapshot policies

- If Amazon Data Lifecycle Manager deletes a snapshot that matches a retention rule, that snapshot is automatically retained
  by Recycle Bin.
- If Amazon Data Lifecycle Manager deletes a snapshot and sends it to the Recycle Bin when the policy's retention threshold is
  reached, and you manually restore the snapshot from the Recycle Bin, you must manually delete that
  snapshot when it is no longer needed. Amazon Data Lifecycle Manager will no longer manage the snapshot.
- If you manually delete a snapshot that was created by a policy, and that snapshot is in the Recycle Bin
  when the policy’s retention threshold is reached, Amazon Data Lifecycle Manager will not delete the snapshot. Amazon Data Lifecycle Manager does not manage
  the snapshots while they are stored in the Recycle Bin.

If the snapshot is restored from the Recycle Bin before the policy's retention threshold is reached,
Amazon Data Lifecycle Manager will delete the snapshot when the policy's retention threshold is reached.

If the snapshot is restored from the Recycle Bin after the policy's retention threshold is reached,
Amazon Data Lifecycle Manager will no longer delete the snapshot. You must manually delete the snapshot when it is no longer
needed.

###### Considerations for AWS Backup

- If AWS Backup deletes a snapshot that matches a retention rule, that snapshot is automatically retained
  by Recycle Bin.

###### Considerations for archived snapshots

- Recycle Bin retention rules also apply to archived snapshots in the archive storage
  tier. If you delete an archived snapshot that matches a retention rule, that snapshot is
  retained in the Recycle Bin for the period defined in the retention rule.

Archived snapshots are billed at the rate for archived snapshots while they are in the
Recycle Bin.

If a retention rule deletes an archived snapshot from the Recycle Bin before the minimum
archive period of 90 days, you are billed for the remaining days. For more information, see
[Archived snapshot pricing and billing](snapshot-archive.md#snapshot-archive-pricing "snapshot-archive.md#snapshot-archive-pricing").

To use an archived snapshot that is in the Recycle Bin, you must first recover the
snapshot from the Recycle Bin and then restore it from the archive tier to the standard
tier.
