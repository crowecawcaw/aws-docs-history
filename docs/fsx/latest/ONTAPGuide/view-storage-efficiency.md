# Monitoring storage efficiency savings

When enabled, you can see how much storage capacity you are saving in the Amazon FSx console, the Amazon CloudWatch console, and the
ONTAP CLI.

###### To view storage efficiency savings (console)

The storage efficiency savings displayed in the Amazon FSx console for an FSx for ONTAP file system includes
the savings from FlexClones and SnapShots.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose the FSx for ONTAP file system that you want to view storage efficiency saving for
   from the list of **File systems**.
3. Choose **Summary** in the **Monitoring & performance**
   tab on the second panel in the file system details page.
4. The **Storage efficiency savings** chart shows how much space you are saving as a percentage
   of your logical data size and in physical bytes.

###### To view storage efficiency savings (ONTAP CLI)

You can see storage efficiency savings of just compaction, compression, and deduplication – without
the effects of snapshots and FlexClones – by running the `storage aggregate show-efficiency`
command using the ONTAP CLI. For more information, see
[storage aggregate show-efficiency](https://docs.netapp.com/us-en/ontap-cli-9131/storage-aggregate-show-efficiency.html "https://docs.netapp.com/us-en/ontap-cli-9131/storage-aggregate-show-efficiency.html")
in the NetApp ONTAP Documentation Center.

1. To access the ONTAP CLI, establish an SSH session on the management port of the
   Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace
   `management_endpoint_ip` with the IP address of the file system's
   management port.

```
`[~]$` `ssh fsxadmin@`management_endpoint_ip``
```

For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli"). 2. The **storage aggregate show-efficiency** command displays information about the storage efficiency of all the aggregates.
The storage efficiency is displayed at four different levels:

    * Total
    * Aggregate
    * Volume
    * Snapshot and FlexClone volume

```
`::*>` `aggr show-efficiency`
`Aggregate: aggr1
 Node: node1

Total Data Reduction Efficiency Ratio: 3.29:1
Total Storage Efficiency Ratio: 4.29:1
Aggregate: aggr2
 Node: node1

Total Data Reduction Efficiency Ratio: 4.50:1
Total Storage Efficiency Ratio: 5.49:1

cluster::*> aggr show-efficiency -details

Aggregate: aggr1
 Node: node1

Total Data Reduction Ratio: 2.39:1
Total Storage Efficiency Ratio: 4.29:1

Aggregate level Storage Efficiency
(Aggregate Deduplication and Data Compaction): 1.00:1
Volume Deduplication Efficiency: 5.03:1
Compression Efficiency: 1.00:1

Snapshot Volume Storage Efficiency: 8.81:1
FlexClone Volume Storage Efficiency: 1.00:1
Number of Efficiency Disabled Volumes: 1

Aggregate: aggr2
 Node: node1
Total Data Reduction Ratio: 2.39:1
Total Storage Efficiency Ratio: 4.29:1

Aggregate level Storage Efficiency
(Aggregate Deduplication and Data Compaction): 1.00:1
Volume Deduplication Efficiency: 5.03:1
Compression Efficiency: 1.00:1

Snapshot Volume Storage Efficiency: 8.81:1
FlexClone Volume Storage Efficiency: 1.00:1
Number of Efficiency Disabled Volumes: 1`
```
