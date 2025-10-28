# Host setup for databases with Amazon FSx for NetApp ONTAP

This section walks you through an example host setup for deploying a database system on AWS using Amazon FSx for NetApp ONTAP as the primary storage solution.

###### Topics

- [Linux kernel parameters](#linux-parameters "#linux-parameters")
- [Network File System (NFS)](#nfs-setup "#nfs-setup")
- [Create mount points](#mount-points "#mount-points")
- [Mount file systems](#mount-filesystem "#mount-filesystem")
- [Host setup for MSSQL](mssql.md "mssql.md")

## Linux kernel parameters

See the following tabs for details.

IBM Db2
Use the following steps to setup the Linux kernel parameters.

1. Create a file named `91-NetApp-DB2.conf` with the following configurations in the `/etc/sysctl.d` directory.

```
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 131072 16777216
net.ipv4.tcp_wmem = 4096 16384 16777216
net.core.netdev_max_backlog = 300000
net.ipv4.tcp_slow_start_after_idle=0
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
```

2. Increase the max sessions slots for NFSv4 to 180.

```
echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
```

3. Set `sunrpc.tcp_slot_table_entries = 128` in `/etc/sysctl.conf`.
4. Reboot your instance for the kernel parameters and NFS settings to take effect.

SAP MaxDB
Use the following steps to setup the Linux kernel parameters.

1. Create a file named `91-NetApp-MaxDB.conf` with the following configurations in the `/etc/sysctl.d` directory.

```
net.core.rmem_max = 16777216
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

2. Increase the max sessions slots for NFSv4 to 180.

```
echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
```

3. Reboot your instance for the kernel parameters and NFS settings to take effect.

SAP ASE
Use the following steps to setup the Linux kernel parameters.

1. Create a file named `91-NetApp-ASE.conf` with the following configurations in the `/etc/sysctl.d` directory.

```
net.core.rmem_max = 16777216
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

2. Increase the max sessions slots for NFSv4 to 180.

```
echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
```

3. Reboot your instance for the kernel parameters and NFS settings to take effect.

Oracle
Use the following steps to setup the Linux kernel parameters.

1. Take a backup of `/etc/sysctl.conf` file by using the following command.

```
sudo cp /etc/sysctl.conf /etc/sysctl.conf.bak
```

2. Open the `/etc/sysctl.conf` file in a text editor, add the following entries to it, and save the file.

```
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.optmem_max = 16777216
net.core.somaxconn = 4096
net.core.netdev_max_backlog = 300000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_slow_start_after_idle=0
net.ipv4.tcp_rmem = 4096 131072 16777216
net.ipv4.tcp_wmem = 4096 16384  16777216
net.ipv4.tcp_max_syn_backlog = 16348
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_dsack = 1
net.ipv4.tcp_sack = 1
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_syn_retries = 8
```

3. Increase the max sessions slots for NFSv4 to 180.

```
echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
```

4. Reboot your instance for the kernel parameters and NFS settings to take effect.

## Network File System (NFS)

Network File System (NFS) version 4 and higher requires user authentication. You can authenticate with Lightweight Directory Access Protocol (LDAP) server or local user accounts.

If you are using local user accounts, the NFSv4 domain must be set to the same value on all Linux servers and SVMs. Set the following parameters in the `/etc/idmapd.conf` file on the Linux hosts.

```
Domain = <domain name>
Nobody-User = root
Nobody-Group = root
```

###### Note

You must restart the `nfs-idmapd.service` service after making changes to the domain.

**Oracle Direct Network File System (dNFS)**

SAP only supports deployment of Oracle database on Amazon FSx for NetApp ONTAP using Direct NFS with NFSv3, NFSv4 and NFSv4.1.

You must setup the `oranfstab` file before enabling dNFS client control of NFS. For more details, refer [Deploying Oracle Direct NFS](https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/deploying-dnfs.html#GUID-D06079DB-8C71-4F68-A1E3-A75D7D96DCE2 "https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/deploying-dnfs.html#GUID-D06079DB-8C71-4F68-A1E3-A75D7D96DCE2"). On configuration completion, query the `V$DNFS_SERVERS` view to verify that the server name, NFS mount points, and NFS version shown in the output match the configuration in `oranfstab` file.

## Create mount points

See the following for details.

IBM Db2
Create the following mount points on your Amazon EC2 instance.

```
mkdir -p /sapmnt
mkdir -p /usr/sap
mkdir -p /db2/db2<dbsid>
mkdir -p /db2/<DBSID>
mkdir -p /db2/<DBSID>/sapdata1
mkdir -p /db2/<DBSID>/sapdata<x>
mkdir -p /db2/<DBSID>/saptmp1
mkdir -p /db2/<DBSID>/saptmp<x>
mkdir -p /db2/<DBSID>/db2dump
mkdir -p /db2/<DBSID>/log_dir
mkdir -p /db2/<DBSID>/log_arch
mkdir -p /db2backup
```

SAP MaxDB
Create the following mount points on your Amazon EC2 instance.

```
mkdir -p /sapmnt
mkdir -p /usr/sap
mkdir -p /sapdb/<DBSID>/sapdata
mkdir -p /sapdb/<DBSID>/saplog
mkdir -p /backup
mkdir -p /sapdb
```

SAP ASE
Create the following mount points on your Amazon EC2 instance.

```
mkdir -p /sapmnt
mkdir -p /usr/sap
mkdir -p /sybase
mkdir -p /sybase/<SID>/sapdata_1
mkdir -p /sybase/<SID>/saplog_1
mkdir -p /sybase/<SID>/sapdiag
mkdir -p /sybase/<SID>/saptmp
mkdir -p /sybasebackup
```

Oracle
Create the following mount points on your Amazon EC2 instance.

```
mkdir -p /oracle
mkdir -p /oracle/<DBSID>
mkdir -p /oracle/<DBSID>/sapdata1
mkdir -p /oracle/<DBSID>/sapdata2
mkdir -p /oracle/<DBSID>/sapdata3
mkdir -p /oracle/<DBSID>/sapdata4
mkdir -p /oracle/<DBSID>/origlogA
mkdir -p /oracle/<DBSID>/origlogB
mkdir -p /oracle/<DBSID>/mirrlogA
mkdir -p /oracle/<DBSID>/mirrlogB
mkdir -p /oracle/<DBSID>/sapreorg
mkdir -p /oracle/<DBSID>/saptrace
mkdir -p /oracle/<DBSID>/saparch
mkdir -p /oracle/<DBSID>/sapcheck
mkdir -p /oracle/<DBSID>/oraarch
mkdir -p /oracle/<DBSID>/sapbackup
```

## Mount file systems

The created file systems must be mounted as NFS file systems on Amazon EC2. See the following for details.

The following table is an example recommendation of NFS options for different IBM Db2 file systems.

IBM Db2

|                      |                               |
| -------------------- | ----------------------------- | ----------------------------- | -------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File systems**     | **NFS mount options**         |
| \***\*Common\*\***   | \***\*NFS version\*\***       | \***\*NFS transfer size\*\*** |
| \***\*nconnect\*\*** |
| Db2 data             | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=8      |
| Db2 log              | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Backup               | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Db2 binary           | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      | **Example** Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems. `<SVM NFSIP>:/<SID>-sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<SID>-usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-db2dbsid /db2/db2<dbsid> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-dbpath /db2/<DBSID> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-sapdata1 /db2/<DBSID>/sapdata1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8 <SVM NFSIP>:/<DBSID>-sapdata<x> /db2/<DBSID>/sapdata<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8 <SVM NFSIP>:/<DBSID>-saptmp1 /db2/<DBSID>/saptmp1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-saptmp<x> /db2/<DBSID>/saptmp<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-logdir /db2/<DBSID>/log_dir nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-logarch /db2/<DBSID>/log_arch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-db2dump /db2/<DBSID>/db2dump nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFSIP>:/<DBSID>-backup /db2backup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2` The following table is an example recommendation of NFS options for different SAP MaxDB file systems. SAP MaxDB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                      |                               |                               | ---                        | ---             |
| **File systems**     | **NFS mount options**         |                               | **Common**                 | **NFS version** | **NFS transfer size**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **nconnect**         |
| SAP MaxDB data       | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=8      |
| SAP MaxDB log        | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Backup               | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| SAP MaxDB binary     | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      | **Example** Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems. `<BackupSVM NFSIP>:/<DBSID>_sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <BackupSVM NFSIP>:/<DBSID>_usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <BackupSVM NFSIP>:/<DBSID>_backup /backup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SAPLOGSVM NFSIP>:/<DBSID>_sapdb /sapdb nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SAPLOGSVM NFSIP>:/<DBSID>_log /sapdb/<DBSID>/saplog nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SAPLOGSVM NFSIP>:/<DBSID>_sapdata /sapdb/<DBSID>/sapdata nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8` The following table is an example recommendation of NFS options for different SAP ASE file systems. SAP ASE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                      |                               |                               | ---                        | ---             |
| **File systems**     | **NFS mount options**         |                               | **Common**                 | **NFS version** | **NFS transfer size**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **nconnect**         |
| SAP ASE data         | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=8      |
| SAP ASE log          | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Backup               | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| SAP ASE binary       | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      | **Example** Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems. `<SVM-ASEDBData NFSIP>:/<SID>-sapdata_1 /sybase/<SID>/sapdata_1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8 <SVM-ASEDBLog NFSIP>:/<SID>-saplog_1 /sybase/<SID>/saplog_1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBShared NFSIP>:/<SID>-sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBShared NFSIP>:/<SID>-usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBShared NFSIP>:/<SID>-sybase /sybase nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBShared NFSIP>:/<SID>-sapdiag /sybase/<SID>/sapdiag nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBShared NFSIP>:/<SID>-saptmp /sybase/<SID>/saptmp nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM-ASEDBBackup NFSIP>:/<SID>-backup /sybasebackup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2` You must assign a virtual hostname to each SVM NFS IP address in `/etc/hosts` file. These hostnames are used in the `oranfstab` file for values of the NFS server `(server: )` during Oracle dNFS configuration. The following table is an example recommendation of NFS options for different SAP Oracle file systems. Oracle                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                      |                               |                               | ---                        | ---             |
| **File systems**     | **NFS mount options**         |                               | **Common**                 | **NFS version** | **NFS transfer size**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **nconnect**         |
| Oracle data          | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=8      |
| Oracle log           | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Oracle backup        | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      |
| Oracle binary        | rw,bg,hard,timeo=600,noatime, | vers=4,minorversion=1,lock,   | rsize=262144,wsize=262144, | nconnect=2      | **Example** Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems. `<SVM NFS Host>:/<DBSID>-oracle /oracle nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-oracle<DBSID> /oracle/<DBSID> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-oraarch /oracle/<DBSID>/oraarch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-saparch /oracle/<DBSID>/saparch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-sapreorg /oracle/<DBSID>/sapreorg nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-sapbackup /oracle/<DBSID>/sapbackup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-saptrace /oracle/<DBSID>/saptrace nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-sapdata1 /oracle/<DBSID>/sapdata1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8 <SVM NFS Host>:/<DBSID>-sapdata2 /oracle/<DBSID>/sapdata<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8 <SVM NFS Host>:/<DBSID>-origlogA /oracle/<DBSID>/origlogA nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-origlogB /oracle/<DBSID>/origlogB nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-mirrlogB /oracle/<DBSID>/mirrlogB nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2 <SVM NFS Host>:/<DBSID>-mirrlogA /oracle/<DBSID>/mirrlogA nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2` <SVM NFS Host> are the values that you have assigned in the `/etc/hosts` file for each SVM NFS IP address. <br>• Changes to the `nconnect` parameter take effect only if the NFS file system is unmounted and mounted again. <br>• Client systems must have unique host names when accessing FSx for ONTAP. If there are systems with the same name, the second system may not be able to access FSx for ONTAP. <br>• For RHEL operating system, the `nconnect` parameter is supported only on RHEL 8.3 or higher. |
