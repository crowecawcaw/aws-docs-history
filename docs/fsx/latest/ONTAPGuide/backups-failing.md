# Your backups fail due to insufficient volume capacity

Automatic daily backups of your volume fails with the following message:

```
Amazon FSx could not create a backup of your volume because the backup snapshot was deleted.
```

Automatic daily backups are failing because there is insufficient free storage capacity on the volume.
To mitigate this condition, you will need to free up storage capacity on the volume. You can accomplish this
using one or more of the following options, depending on your situation:

- [Increase the volume's storage capacity](manage-volume-capacity.md#increase-volume-size "manage-volume-capacity.md#increase-volume-size")
- [Increase the volume's snapshot reserve](snapshots-ontap.md#snapshot-reserve "snapshots-ontap.md#snapshot-reserve")
- [Disable snapshot auto-delete](snapshot-autodelete-policy.md "snapshot-autodelete-policy.md")
- [Don't delete the backup-snapshot](common-snapshot.md "common-snapshot.md") using the ONTAP CLI
