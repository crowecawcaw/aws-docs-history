# Recovering deleted FSx for ONTAP volumes

When an FSx for ONTAP volume is deleted, it's placed in ONTAP's recovery queue. While you can recover a volume
directly from this queue using the ONTAP CLI, the recovered volume won't reappear in the AWS console or Amazon FSx API and
any AWS tags that were previously applied to the volume will be permanently lost. To properly recover an FSx for ONTAP volume while preserving
AWS integration and tag-based security policies, you can either [restore a backup to a new volume](to-restore-backups.md "to-restore-backups.md") or
[replicate the volume's data to a new volume using SnapMirror](scheduled-replication.md "scheduled-replication.md"). For more information
about ONTAP's recovery queue, see [NetApp's
documentation.](https://docs.netapp.com/us-en/ontap-cli/volume-recovery-queue-show.html "https://docs.netapp.com/us-en/ontap-cli/volume-recovery-queue-show.html")
