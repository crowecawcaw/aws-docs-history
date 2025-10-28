# Expanding FlexGroup volumes

You can add additional constituent volumes to your FlexGroup volume with the `volume expand` command in the
ONTAP CLI. This is a best practice after adding high-availability (HA) pairs to your file system because it ensures that your FlexGroup volume stays balanced.

Before expanding your FlexGroup volume, consider the following points:

- All of a FlexGroup's constituent volumes have the same storage capacity. When you expand your FlexGroup volume with additional
  constituents, each constituent is the same size as the existing constituents. Therefore, ensure that each aggregate has sufficient space available before adding
  constituents.
- AWS recommends maintaining eight constituent volumes per aggregate for each FlexGroup volume. Eight constituent volumes per aggregate maximizes the parallelism
  of FlexGroup volumes and offers the most optimal performance for your workload. Generally, we only recommend expanding your FlexGroup volume with
  additional constituents if you add HA pairs. This is the only scenario in which you would need to add constituents to maintain eight constituents per aggregate.
- If your FlexGroup volume is in a SnapMirror relationship, then both the source and destination FlexGroup volumes need to have
  the same number of constituents. Otherwise, SnapMirror transfers will fail. SnapMirror operates at the constituent level and transfers data
  between each individual constituent. Therefore, if you expand a FlexGroup volume with additional constituent volumes, you must also manually expand any volume that
  is in a SnapMirror relationship with it.
- When you expand a FlexGroup volume with additional constituents, all of its existing snapshot copies become "partial" copies. Partial copies can't be restored,
  but they can be browsed and the individual files can be restored. Additionally, this results in the loss of any incrementality for Amazon FSx backups, AWS backups,
  or SnapMirror relationships.
- You can't remove constituent volumes once you add them.

## Adding FlexGroup volume constituents

You can use the ONTAP CLI to add constituent volumes to your FlexGroup volume.

###### To add FlexGroup volume constituents

1. To access the NetApp ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Use the [volume expand](https://docs.netapp.com/us-en/ontap-cli-9141/volume-expand.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-expand.html")
ONTAP CLI command to expand your FlexGroup volume with additional constituents. Replace the following values:

    * `svm_name` with the name of the storage virtual machine (SVM) that hosts your FlexGroup volume (for example, `svm1`).
    * `vol_name` with the name of the FlexGroup volume that you want to expand (for example, `vol1`).
    * `aggregates` with a comma-separated list of aggregates that you want to add FlexGroup constituent volumes into. For example,
     `aggr1` for a single aggregate or `aggr1,aggr2` for multiple aggregates.
    * `constituent_per_aggregate` with the number of additional constituents that you want to add to each of the specified `aggregates`.
     You should only add enough constituents to ensure that your FlexGroup volume has a balanced number of constituents across the aggregates it resides on.

```
::> volume expand -vserver `svm_name` -volume `vol_name` -aggr-list `aggregates` -aggr-list-multiplier `constituents_per_aggregate`
```

###### Important

You can't remove FlexGroup constituents after you add them, so check your inputs before running the previous command.
