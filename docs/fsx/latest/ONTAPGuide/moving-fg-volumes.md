# Moving volumes between aggregates

When you add high-availability (HA) pairs to your file system, you need to rebalance the existing data by moving volumes
to the new aggregates. To move a volume between aggregates, you can use the `volume move` command in the ONTAP CLI.

Before using the `volume move` command, consider the following points:

- Using the `volume move` command can impact performance because it consumes network and disk resources on your file system.
  Therefore, we recommend moving volumes between aggregates during periods of low activity. Alternatively, you can reduce the network throughput
  utilization and disk throughput utilization on your file system to no more than 50% while moving volumes.
- To reduce the performance impact on your file system, we recommend moving a single volume between two HA pairs and aggregates at a time.
  For example, if your file system has four HA pairs, we recommend moving two volumes at a time (assuming the volume moves are not from or toward the same HA pairs).
  ONTAP supports moving up to eight volumes on each HA pair at a time, but more simultaneous volume moves will reduce the performance
  of both client I/O and any in-progress volume moves.
- Any data stored on the SSD tier on the impacted volume is physically moved to a different set of disks on a different
  file server. This operation occurs in the background and takes time. The rate of time that the transfer takes depends on your file system's
  throughput capacity and the amount of activity on your file system. However, the volume move can be throttled. For more information, see
  [Throttling volume moves](#throttle-volume-moves "#throttle-volume-moves").
- Data stored in capacity pool is not physically moved because the HA pairs share the same capacity pool storage. Instead, ONTAP moves metadata that fully describes each block in capacity pool (a logical move). Keep in mind that file metadata is always stored on the SSD tier. For more information, see
  [Volume data tiering](volume-storage-capacity.md#volume-data-tiering "volume-storage-capacity.md#volume-data-tiering").

## Phases of moving a volume

There are two phases in a volume move operation: the replication phase and the cutover
phase. During the replication phase, existing data is replicated to the volume's new
aggregate. During the cutover phase, ONTAP attempts a final rapid transfer to the
volume's new aggregate. This includes transferring any data that has been written
during the transfer phase and redirecting new traffic to the volume's new aggregate.
By default, the cutover window is 30 seconds and halts all I/O to your volume. If
ONTAP can't perform all of these steps during the cutover window, it will fail. By
default, ONTAP will try to cut over three times consecutively. If all three
consecutive attempts fail, then ONTAP will retry once an hour until it succeeds. You
can reduce the load on your file system to ensure that the cutover phase is
successful by reducing or pausing I/O traffic to the volume before the cutover phase
begins.

## Starting volume moves

###### To start a volume move

1. To access the NetApp ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. Run the [volume move start](https://docs.netapp.com/us-en/ontap-cli-9131/volume-move-start.html#description "https://docs.netapp.com/us-en/ontap-cli-9131/volume-move-start.html#description")
ONTAP CLI command. Replace the following values:

    * `vserver_name` with the name of the SVM hosting the volume that you're moving.
    * `volume_name` with the name of the volume's constituent (for example, `vol1__0001`).
    * `aggregate_name` with the name of the destination aggregate for the volume.
    * `-enforce-network-throttling` to throttle the volume move's total throughput. This is optional.

```
::> volume move start -vserver `svm_name` -volume `volume_name` --destination-aggregate `aggregate_name` -foreground false
[Job 1] Job is queued: Move "vol1__0001" in Vserver "svm01" to aggregate "aggr1". Use the "volume move show -vserver svm01 -volume vol1__0001" command to view the status of this operation.

```

###### Important

Moving volumes consumes network and disk resources for the source and destination file servers. Therefore, your workload's
performance can be impacted by any volume moves that are in progress. Additionally, your I/O traffic to the volume will be temporarily paused during the cutover phase of
the volume move.

## Monitoring volume moves

###### To monitor a volume move

- To check the status of the volume move operation, use the `volume move show` ONTAP CLI command.

```
::> volume move show -vserver `svm_name` -volume `volume_name`

Vserver Name: svm01
Volume Name: vol1__0001
Actual Completion Time: -
Bytes Remaining: 1.00TB
Specified Action For Cutover: retry_on_failure
Specified Cutover Time Window: 30
Destination Aggregate: aggr2
Destination Node: FsxId01234567890abcdef-03
Detailed Status: Transferring data: 12.23GB sent.
Percentage Complete: 1%
Move Phase: replicating
Prior Issues Encountered: -
Estimated Remaining Duration: 00:40:25
Replication Throughput: 434.3MB/s
Duration of Move: 00:00:27
Source Aggregate: aggr1
Source Node: FsxId01234567890abcdef-01
Move State: healthy

```

The command output shows the estimated time to complete the move.
When it's finished, the `Move phase` will show the `completed` status.

## Maintaining balanced FlexGroup volumes

In order for your workload to perform optimally, your FlexGroup volumes should span all aggregates and have an even number of constituent volumes
per aggregate. We recommend having eight constituents per aggregate. Consider the following scenarios when rebalancing FlexGroup volumes:

- **Moving FlexGroup constituents among existing aggregates:** If you move a FlexGroup's constituent volume to another aggregate of
  an otherwise balanced FlexGroup, you should then move another constituent that's less utilized to the original aggregate. This ensures that your
  FlexGroup has an even number of constituents per aggregate.

**Moving FlexGroup constituents into new aggregates after adding HA pairs:** If you move a FlexGroup's constituent volumes to new
aggregates after adding HA pairs, then you should expand the FlexGroup with additional constituents on the aggregates that lost constituents.
This ensures that your FlexGroup has an even number of constituents per aggregate. For more information, see [Expanding FlexGroup volumes](expanding-fg-volumes.md "expanding-fg-volumes.md").

## Throttling volume moves

If you want to limit the bandwidth of a volume move on your file system, you can add the `-enforce-network-throttling` option at the beginning of the operation.

###### Note

Using this option affects incoming SnapMirror replication data transfers for the file system. Keep track of how you configure your file system's replication options because you can't
view them after setting them.

###### To throttle a volume move

1. The throttle uses the global replication throttle. To set the global replication throttle, use the following command in the ONTAP CLI.

```
::> options -option-name replication.throttle.enable on
```

2. Specify the maximum total bandwidth that can be used by replication, replacing the following option:
   - `kbs_throttle` with the maximum desired throughput to use for any replication (including SnapMirror and volume moves), in Kilobytes per second.

```
::> options -option-name replication.throttle.incoming.max_kbs `kbs_throttle`
::> options -option-name replication.throttle.outgoing.max_kbs `kbs_throttle`
```
