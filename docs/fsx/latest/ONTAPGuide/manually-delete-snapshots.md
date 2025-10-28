# Deleting snapshots

Use the
[**volume snapshot delete**](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-delete.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-delete.html")
ONTAP CLI command to manually delete snapshots, replacing the following placeholder values with your data:

- Replace `svm_name` with the name of the SVM that the
  volume is created on.
- Replace `vol_name` with name of the volume.
- Replace `snapshot_name` with the name of the snapshot.
  This command supports wildcard characters (`*`) for
  `snapshot_name`. Therefore, you can delete all hourly
  snapshots, for example, by using `hourly*`.

###### Important

If you have Amazon FSx backups enabled, Amazon FSx retains a snapshot for the most recent Amazon FSx backup
of each volume. Those snapshots are used to maintain incrementality between backups, and must
not be deleted by using this method. For more information, see [Viewing the common snapshot](common-snapshot.md "common-snapshot.md").

```
`FsxIdabcdef01234567892::>` `volume snapshot delete -vserver `svm_name` -volume `vol_name` -snapshot `snapshot_name``
```
