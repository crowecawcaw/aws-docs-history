# Creating a Snapshot autodelete policy

You can create a policy to automatically delete snapshots when the amount of available
space in your volume is running low. Use the
[volume snapshot autodelete modify](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-autodelete-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-autodelete-modify.html")
ONTAP CLI command to establish an autodelete policy for a volume.

When using this command, use your data to replace the following placeholder values:

- Replace `svm_name` with the name of the SVM that
  the volume is created on.
- Replace `vol_name` with name of the volume.
  For `-trigger`, assign one of the following values:

- `volume` – Use `volume` if you want the threshold at which
  snapshots are deleted to correspond to a total used-volume capacity threshold. The
  used-volume capacity thresholds that trigger snapshot deletion are determined by the size of
  your volume, with the threshold scaling from 85–98 percent used capacity. Smaller
  volumes have a smaller threshold, and larger volumes have a larger one.
- `snap_reserve` – Use `snap_reserve` if you want snapshots to be
  deleted based on what can be held in your snapshot reserve.

```
`::>` `volume snapshot autodelete modify -vserver `svm_name` -volume `vol_name` -enabled true -trigger [volume|snap_reserve]`
```

For more information, see the [volume snapshot autodelete modify](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-autodelete-modify.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-autodelete-modify.html") command in the _NetApp ONTAP
Documentation Center_.
