# SAP HANA scale-up

The following section is an example host setup for SAP HANA scale-up deployment with FSx for ONTAP.

###### Topics

- [Linux kernel parameters](#linux-setup-scaleup "#linux-setup-scaleup")
- [Network File System (NFS)](#nfs-setup-scaleup "#nfs-setup-scaleup")
- [Create subdirectories](#subdirectories-scaleup "#subdirectories-scaleup")
- [Create mount points](#mount-points-scaleup "#mount-points-scaleup")
- [Mount file systems](#mount-filesys-scaleup "#mount-filesys-scaleup")
- [Data volume partitions](#partitions-scaleup "#partitions-scaleup")

## Linux kernel parameters

Create a file named `91-NetApp-HANA.conf` with the following configurations in the `/etc/sysctl.d` directory.

```
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 131072 16777216
net.ipv4.tcp_wmem = 4096 16384  16777216
net.core.netdev_max_backlog = 300000
net.ipv4.tcp_slow_start_after_idle=0
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
```

Increase the max sessions slots for NFSv4 to 180.

```
echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
```

You must reboot your instance for the kernel parameters and NFS settings to take effect.

## Network File System (NFS)

Network File System (NFS) version 4 and higher requires user authentication. You can authenticate with Lightweight Directory Access Protocol (LDAP) server or local user accounts.

If you are using local user accounts, the NFSv4 domain must be set to the same value on all Linux servers and SVMs. You can set the domain parameter (`Domain = <domain name>`) in the `/etc/idmapd.conf` file on the Linux hosts.

To identify the domain setting of the SVM, use the following command:

```
nfs show -vserver hana-data -fields v4-id-domain
```

The following is example output:

```
vserver   v4-id-domain
--------- ------------
hana-data ec2.internal
```

## Create subdirectories

Mount the `/hana/shared` volume, create `shared` and `usr-sap` subdirectories, and unmount.

```
mkdir /mnt/tmp
mount -t nfs -o sec=sys,vers=4.1 <svm-shared>:/HDB-shared /mnt/tmp
cd /mnt/tmp
mkdir shared
mkdir usr-sap
cd
umount /mnt/tmp
```

## Create mount points

On single-host systems, create the following mount points on your Amazon EC2 instance.

```
mkdir -p /hana/data/HDB/mnt00001
mkdir -p /hana/log/HDB/mnt00001
mkdir -p /hana/shared
mkdir -p /usr/sap/HDB
```

## Mount file systems

The created file systems must be mounted as NFS file systems on Amazon EC2. The following table is an example recommendation of NFS options for different SAP HANA file systems.

|                  |                               |                             |                            |                        |
| ---------------- | ----------------------------- | --------------------------- | -------------------------- | ---------------------- |
| **File systems** | **Common mount options**      | **Version options**         | **Transfer size options**  | **Connection options** |
| SAP HANA data    | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock, | rsize=262144,wsize=262144, | nconnect=4             |
| SAP HANA log     | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock, | rsize=262144,wsize=262144, | nconnect=2             |
| SAP HANA shared  | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock, | rsize=262144,wsize=262144, | nconnect=2             |
| SAP HANA binary  | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock, | rsize=262144,wsize=262144, | nconnect=2             |

- Changes to the `nconnect` parameter take effect only if the NFS file system is unmounted and mounted again.
- Client systems must have unique host names when accessing FSx for ONTAP. If there are systems with the same name, the second system may not be able to access FSx for ONTAP.

**Example**

Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems.

```
<svm-data>:/HDB_data_mnt00001 /hana/data/HDB/mnt00001 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=4
<svm-log>:/HDB_log_mnt00001 /hana/log/HDB/mnt00001 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<svm-shared>:/HDB_shared/usr-sap /usr/sap/HDB nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<svm-shared>:/HDB_shared/shared /hana/shared nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
```

## Data volume partitions

With SAP HANA 2.0 SPS4, additional data volume partitions allow configuring two or more file system volumes for the DATA volume of an SAP HANA tenant database in a single-host or multi-host system. Data volume partitions enable SAP HANA to scale beyond the size and performance limits of a single volume. You can add additional data volume partitions at any time. For more information, see [Host configuration](https://docs.netapp.com/us-en/netapp-solutions-sap/bp/saphana_aff_nfs_adding_additional_data_volume_partitions.html#host-configuration "https://docs.netapp.com/us-en/netapp-solutions-sap/bp/saphana_aff_nfs_adding_additional_data_volume_partitions.html#host-configuration").

### Host preparation

Additional mount points and `/etc/fstab` entries must be created and the new volumes must be mounted.

- Create additional mount points and assign the required permissions, group, and ownership.

```
mkdir -p /hana/data2/HDB/mnt00001
chmod -R 777 /hana/data2/HDB/mnt00001
```

- Add additional file systems to `/etc/fstab`.

```
<data2>:/data2 /hana/data/HDB/mnt00001 nfs <mount options>
```

- Set the permissions to 777. This is required to enable SAP HANA to add a new data volume in the subsequent step. SAP HANA sets more restrictive permissions automatically during data volume creation.

### Enabling data volume partitioning

To enable data volume partitions, add the following entry in the `global.ini` file in the `SYSTEMDB` configuration.

```
[customizable_functionalities]
persistence_datavolume_partition_multipath = true
```

```
ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM')
SET ('customizable_functionalities', 'PERSISTENCE_DATAVOLUME_PARTITION_MULTIPATH') = 'true'
WITH RECONFIGURE;
```

###### Note

You must restart your database after updating the `global.ini` file.

### Adding additional data volume partition

Run the following SQL statement against the tenant database to add an additional data volume partition to your tenant database.

```
ALTER SYSTEM ALTER DATAVOLUME ADD PARTITION PATH '/hana/data/HDB/mnt00002/';
```

Adding a data volume partition is quick. The new data volume partitions are empty after creation. Data is distributed equally across data volumes over time.

After you configure and mount FSx for ONTAP file systems, you can install and setup your SAP HANA workload on AWS. For more information, see [SAP HANA Environment Setup on AWS](std-sap-hana-environment-setup.md "std-sap-hana-environment-setup.md").
