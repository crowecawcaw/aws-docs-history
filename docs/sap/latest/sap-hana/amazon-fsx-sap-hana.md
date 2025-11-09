# Set up FSx for ONTAP file system, SVMs, and volumes

Before you create FSx for ONTAP file system, determine the total storage space you need for your SAP HANA workload. You can increase the storage size later. To decrease the storage size, you must create a new file system.

To create a FSx for ONTAP file system, see [Step 1: Create an Amazon FSx for NetApp ONTAP file system](../../../fsx/latest/ONTAPGuide/getting-started-step1.md "../../../fsx/latest/ONTAPGuide/getting-started-step1.md"). For more information, see [Managing FSx for ONTAP file systems](../../../fsx/latest/ONTAPGuide/managing-file-systems.md "../../../fsx/latest/ONTAPGuide/managing-file-systems.md").

###### Note

Only single Availability Zone file systems are supported for SAP HANA workloads.

###### Topics

- [Create storage virtual machines (SVM)](#svm-sap-hana "#svm-sap-hana")
- [Volume configuration](#volume-fsx-sap-hana "#volume-fsx-sap-hana")
- [Sample estimate](#sizing-estimation "#sizing-estimation")
- [Volume layout](#vol-layout-fsx-sap-hana "#vol-layout-fsx-sap-hana")
- [File system setup](#filesys-fsx-sap-hana "#filesys-fsx-sap-hana")
- [Disable snapshots](#snaps-fsx-sap-hana "#snaps-fsx-sap-hana")
- [Quality of Service (QoS)](#fsx-qos "#fsx-qos")
- [Backup](#fsx-backup "#fsx-backup")

## Create storage virtual machines (SVM)

You get one SVM per FSx for ONTAP file system by default. You can create additional SVMs at any time. For optimal performance, mount data and log volumes using different IP addresses. You can achieve this using separate SVMs for data and log volumes. If you plan to use NetApp SnapCenter, all SVMs used for SAP HANA must have unique names. You don’t need to join your file system to Active Directory for SAP HANA. For more information, see [Managing FSx for ONTAP storage virtual machines](../../../fsx/latest/ONTAPGuide/managing-svms.md "../../../fsx/latest/ONTAPGuide/managing-svms.md").

## Volume configuration

The storage capacity of your file system should align with the needs of `/hana/shared`, `/hana/data`, and `/hana/log` volumes. You must also consider the capacity required for snapshots, if applicable.

We recommend creating separate FSx for ONTAP volumes for each of SAP HANA data, log, shared, and binary volumes. The following table lists the recommended minimum sizes per volume.

| Volume         | Recommended size for scale-up                                  | Recommended size for scale-out                                         |
| -------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `/usr/sap`     | 50 GiB                                                         | 50 GiB                                                                 |
| `/hana/shared` | Minimum of 1 x memory of your Amazon EC2 instance or 1TB       | 1 x memory of your Amazon EC2 instance for every 4 subordinate nodes\* |
| `/hana/data`   | At least 1.2 x memory of your Amazon EC2 instance              | At least 1.2 x memory of your Amazon EC2 instance                      |
| `/hana/log`    | Minimum of 0.5 x memory of your Amazon EC2 instance or 600 GiB | Minimum of 0.5 x memory of your Amazon EC2 instance or 600 GiB         |

\*For example, if you have 2-4 scale-out nodes, you need 1 x memory of your single Amazon EC2 instance. If you have 5-8 scale-out nodes, you need 2 x memory of your single Amazon EC2 instance.

The following limitations apply when you create a FSx for ONTAP file system for SAP HANA.

- _Storage Efficiency_ is not supported for SAP HANA and must be **disabled**.
- _Capacity Pool Tiering_ is not supported for SAP HANA and must be set to **None**.
- _Daily automatic backups_ must be **disabled** for SAP HANA. Default FSx for ONTAP backups are not application-aware and cannot be used to restore SAP HANA to a consistent state.

## Sample estimate

You can use the formulas in the following table to create estimates for SAP HANA performance KPIs for production systems. These systems can be in single Availability Zone setup or a multi-Availability Zone setup. See the storage architecture for [Amazon FSx for NetApp ONTAP](architecture-fsx.md "architecture-fsx.md") to learn more.

Note: Amazon EC2 root volumes used as boot volumes for the operating system always need to be based on Amazon EBS. For example, `gp3` – using an EBS-based SAP HANA log volume with FSx for ONTAP is supported.

| Volume ID          | Type                                                         | Minimum volume size                                            | Additional space for local snapshots                 | Storage efficiency | % space required on SSD                        |
| ------------------ | ------------------------------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ---------------------------------------------- |
| HANA data          | FSxN #1<br>• Single-AZ1<br>• 1024 MB/s (\*)                  | 1.2 x RAM                                                      | DB Size x SNAPSHOTS-KEPT-AT-PRIMARY x CHANGE-RATE-DB | Must be disabled   | 100%                                           |
| HANA log           | IF(RAM ⇐ 512; RAM/2; 512)                                    | N/A                                                            | Must be disabled                                     | 100%               |
| HANA shared        | MIN(RAM; 1024) x 50%                                         | Volume Size x SNAPSHOTS-KEPT-AT-PRIMARY x CHANGE-RATE-BINARIES | Enabled, assume ~50%                                 | 100%               |
| APPSRV bin         | 100 GB x 50%                                                 | Volume Size x SNAPSHOTS-KEPT-AT-PRIMARY x CHANGE-RATE-BINARIES | Enabled, assume ~50%                                 | 100%               |
| Backup HANA log    | FSxN #2<br>• Multi-AZ1+2<br>• 512 MB/s (\*\*)                | DB Size x LOG-RATE x RETENTION x % SSD                         | N/A                                                  | Optional           | MIN(SNAPSHOTS-KEPT-AT-PRIMARY / RETENTION; 5%) |
| Backup HANA data   | FSxN #3<br>• Single-AZ3<br>• 512 MB/s                        | DB Size x (1 + RETENTION x CHANGE-RATE-DB) x % SSD             | N/A                                                  | Optional           | ~5%                                            |
| Backup HANA shared | Volume Size x (1 + RETENTION x CHANGE-RATE-BINARIES) x % SSD | N/A                                                            | Enabled, assume ~50%                                 | ~5%                |
| Backup APPSRV bin  | Volume Size x (1 + RETENTION x CHANGE-RATE-BINARIES) x % SSD | N/A                                                            | Enabled, assume ~50%                                 | ~5%                |

###### Note

- (\*) You must provision a secondary FSx for ONTAP volume for SAP HANA multi-Availability Zone deployments.
- (\*\*) This can be deployed in a single-Availability Zone setup for cost efficiency.

**Common parameters**

- CHANGE-RATE-DB: 30%for prod, 5% for non-prod
- CHANGE-RATE-BINARIES: 5%
- LOG-RATE: 5%
- SNAPSHOTS-KEPT-AT-PRIMARY: 3 days
- RETENTION: 30 days

## Volume layout

###### Topics

- [SAP HANA scale-up](#fsx-volume-layout-scaleup "#fsx-volume-layout-scaleup")
- [SAP HANA scale-out](#fsx-volume-layout-scaleout "#fsx-volume-layout-scaleout")

### SAP HANA scale-up

The following table presents an example of volume and mount point configuration for scale-up setup. It includes a single host. `HDB` is the SAP HANA system ID. To place the home directory of the `hdbadm` user on the central storage, the `/usr/sap/HDB` file system must be mounted from the `HDB_shared` volume.

| Volume name       | Junction path     | Directory | Mount point             |
| ----------------- | ----------------- | --------- | ----------------------- |
| HDB_data_mnt00001 | HDB_data_mnt00001 | -         | /hana/data/HDB/mnt00001 |
| HDB_log_mnt00001  | HDB_log_mnt00001  | -         | /hana/log/HDB/mnt00001  |
| HDB_shared        | HDB_shared        | usr-sap   | /usr/sap/HDB            |
| shared            | /hana/shared      |

### SAP HANA scale-out

You must mount all the data, log, and shared volumes in every node, including the standby node.

The following table presents an example of volume and mount point configuration for a scale-out setup. It includes four active and one standby host. `HDB` is the SAP HANA system ID. The home (`/usr/sap/HDB`) and shared (`(/hana/shared`) directories of every host are stored in the `HDB_shared` volume. To place the home directory of the `hdbadm` user on the central storage, the `/usr/sap/HDB` file system must be mounted from the `HDB_shared` volume.

| Volume name       | Junction path     | Directory     | Mount point             | Note                 |
| ----------------- | ----------------- | ------------- | ----------------------- | -------------------- |
| HDB_data_mnt00001 | HDB_data_mnt00001 | N/A           | /hana/data/HDB/mnt00001 | Mounted on all hosts |
| HDB_log_mnt00001  | HDB_log_mnt00001  | N/A           | /hana/log/HDB/mnt00001  | Mounted on all hosts |
| HDB_data_mnt00002 | HDB_data_mnt00002 | N/A           | /hana/data/HDB/mnt00002 | Mounted on all hosts |
| HDB_log_mnt00002  | HDB_log_mnt00002  | N/A           | /hana/log/HDB/mnt00002  | Mounted on all hosts |
| HDB_data_mnt00003 | HDB_data_mnt00003 | N/A           | /hana/data/HDB/mnt00003 | Mounted on all hosts |
| HDB_log_mnt00003  | HDB_log_mnt00003  | N/A           | /hana/log/HDB/mnt00003  | Mounted on all hosts |
| HDB_data_mnt00004 | HDB_data_mnt00004 | N/A           | /hana/data/HDB/mnt00004 | Mounted on all hosts |
| HDB_log_mnt00004  | HDB_log_mnt00004  | N/A           | /hana/log/HDB/mnt00004  | Mounted on all hosts |
| HDB_shared        | HDB_shared        | HDB_shared    | /hana/shared/HDB        | Mounted on all hosts |
| HDB_shared        | HDB_shared        | usr-sap-host1 | /usr/sap/HDB            | Mounted on host 1    |
| HDB_shared        | HDB_shared        | usr-sap-host2 | /usr/sap/HDB            | Mounted on host 2    |
| HDB_shared        | HDB_shared        | usr-sap-host3 | /usr/sap/HDB            | Mounted on host 3    |
| HDB_shared        | HDB_shared        | usr-sap-host4 | /usr/sap/HDB            | Mounted on host 4    |
| HDB_shared        | HDB_shared        | usr-sap-host5 | /usr/sap/HDB            | Mounted on host 5    |

## File system setup

After creating a FSx for ONTAP file system, you must complete additional file system setup.

### Set administrative password

If you did not create an administrative password during FSx for ONTAP file system creation, you must set an ONTAP administrative password for `fsxadmin` user.

The administrative password enables you to access the file system via SSH, the ONTAP CLI, and REST API. To use tools like NetApp SnapCenter, you must have an administrative password.

### Sign in to the management endpoint via SSH

Get the DNS name of the management endpoint from AWS console. Sign in to the management endpoint via SSH, using the `fsxadmin` user and administrative password.

```
ssh fsxadmin@management.<file-system-id>.fsx.<aws-region>.amazonaws.com Password:
```

### Set TCP max transfer size

We recommend a TCP max transfer size of 262,144 for your SAP HANA workloads. Elevate the privilege level to _advanced_ and use the following command on each SVM.

```
set advanced
nfs modify -vserver <svm> -tcp-max-xfer-size 262144
set admin
```

### Set the lease time on NFSv4 protocol

This task applies to SAP HANA scale-out with standby node setup.

Lease period refers to the time in which ONTAP irrevocably grants a lock to a client. It is set to 30 seconds by default. You can have faster server recovery by setting shorter lease time.

You can change the lease time with the following command.

```
set advanced
nfs modify -vserver <svm> -v4-lease-seconds 10
set admin
```

###### Note

Starting with SAP HANA 2.0 SPS4, SAP provides parameters to control failover behavior. NetApp recommends using these parameters instead of setting the lease time at the SVM level. For more details, see.

## Disable snapshots

FSx for ONTAP automatically enables a snapshot policy for volumes that take hourly snapshots. The default policy offers limited value to SAP HANA due to missing application awareness. We recommend disabling the automatic snapshots by setting the policy to none. You can disable snapshots during volume creation or by using the following command.

```
volume modify -vserver <vserver-name> -volume <volume-name> -snapshot-policy none
```

### Data volume

The automatic FSx for ONTAP snapshots do not have application awareness. A database-consistent snapshot of the SAP HANA data volume must be prepared by creating a data snapshot. For more information, see [Create a Data Snapshot](https://help.sap.com/docs/SAP_HANA_COCKPIT/afa922439b204e9caf22c78b6b69e4f2/9fd1c8bb3b60455caa93b7491ae6d830.html "https://help.sap.com/docs/SAP_HANA_COCKPIT/afa922439b204e9caf22c78b6b69e4f2/9fd1c8bb3b60455caa93b7491ae6d830.html").

### Log volume

The log volume is automatically backed up every 15 minutes by SAP HANA. An hourly volume snapshot does not offer any additional value in terms of RPO reduction.

The high frequency of changes on the log volume can rapidly increase the total capacity used for snapshots. This can cause the log volume to run out of capacity, making the SAP HANA workload unresponsive.

## Quality of Service (QoS)

Quality of Service (QoS) enables FSx for ONTAP to consistently deliver predictable performance to multiple applications, and eliminate noisy neighbor applications. When sharing a file system, you can use the quality of service feature for consistent performance and reduced interference between competing workloads. For more information, see [Using Quality of Service in Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-quality-of-service-in-amazon-fsx-for-netapp-ontap/ "https://aws.amazon.com/blogs/storage/using-quality-of-service-in-amazon-fsx-for-netapp-ontap/").

QoS is configured by creating a QoS policy group, setting ceiling or floor performance levels (minimum or maximum performance), and assigning the policy to an SVM or volume. Performance can be specified in either IOPS or throughput.

**Example**

You are creating a test system, based on a snapshot from production, on the same file system as your production SAP HANA database. You want to ensure that the test system does not impact the performance of the production system. You create a QoS policy group (`qos-test`) and define an upper limit of 200 MB/s for data and log volumes (`vol-data` and `vol-log`), which share the same SVM (`svm-test`).

```
 Create QoS policy group
qos policy-group create -policy-group qos-test -vserver svm-test -is-shared false -max-throughput 200MBs

 Assign QoS policy group to data on log volumes
volume modify -vserver svm-test -volume vol-data -qos-policy-group qos-test
volume modify -vserver svm-test -volume vol-log -qos-policy-group qos-test
```

## Backup

You must disable automatic backups for FSx for ONTAP volumes and file systems for SAP HANA. The backups cannot be used to restore SAP HANA to a consistent state. You can use the SnapCenter plugin for SAP HANA backups. For more details, see NetApp docs – [SnapCenter Plug-in for SAP HANA Database overview](https://docs.netapp.com/us-en/snapcenter/protect-hana/concept_snapcenter_plug_in_for_sap_hana_database_overview.html "https://docs.netapp.com/us-en/snapcenter/protect-hana/concept_snapcenter_plug_in_for_sap_hana_database_overview.html") and [SAP HANA on Amazon FSx for NetApp ONTAP - Backup and recovery with SnapCenter](https://docs.netapp.com/us-en/netapp-solutions-sap/backup/amazon-fsx-overview.html "https://docs.netapp.com/us-en/netapp-solutions-sap/backup/amazon-fsx-overview.html").

You can also use SnapMirror for SAP HANA backups. For more information, see [How can I optimize SnapMirror performance, and what are the best practices for FSx for ONTAP?](https://repost.aws/knowledge-center/fsx-ontap-optimize-snapmirror "https://repost.aws/knowledge-center/fsx-ontap-optimize-snapmirror")

For point-in-time resilient restores, we highly recommend storing three days of snapshots on a local disk and replicating older backups via SnapVault to a secondary FSx for ONTAP file system using the capacity pool tier. For more information, see [Managing storage capacity](../../../fsx/latest/ONTAPGuide/managing-storage-capacity.md#storage-tiers "../../../fsx/latest/ONTAPGuide/managing-storage-capacity.md#storage-tiers").
