

# Host setup for databases with Amazon FSx for NetApp ONTAP
<a name="host"></a>

This section walks you through an example host setup for deploying a database system on AWS using Amazon FSx for NetApp ONTAP as the primary storage solution.

**Topics**
+ [Linux kernel parameters](#linux-parameters)
+ [Network File System (NFS)](#nfs-setup)
+ [Create mount points](#mount-points)
+ [Mount file systems](#mount-filesystem)
+ [Host setup for MSSQL](mssql.md)

## Linux kernel parameters
<a name="linux-parameters"></a>

See the following tabs for details.

**Example**  
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

1. Increase the max sessions slots for NFSv4 to 180.

   ```
   echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
   ```

1. Set `sunrpc.tcp_slot_table_entries = 128` in `/etc/sysctl.conf`.

1. Reboot your instance for the kernel parameters and NFS settings to take effect.
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

1. Increase the max sessions slots for NFSv4 to 180.

   ```
   echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
   ```

1. Reboot your instance for the kernel parameters and NFS settings to take effect.
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

1. Increase the max sessions slots for NFSv4 to 180.

   ```
   echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
   ```

1. Reboot your instance for the kernel parameters and NFS settings to take effect.
Use the following steps to setup the Linux kernel parameters.  

1. Take a backup of `/etc/sysctl.conf` file by using the following command.

   ```
   sudo cp /etc/sysctl.conf /etc/sysctl.conf.bak
   ```

1. Open the `/etc/sysctl.conf` file in a text editor, add the following entries to it, and save the file.

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

1. Increase the max sessions slots for NFSv4 to 180.

   ```
   echo options nfs max_session_slots=180 > /etc/modprobe.d/nfsclient.conf
   ```

1. Reboot your instance for the kernel parameters and NFS settings to take effect.

## Network File System (NFS)
<a name="nfs-setup"></a>

Network File System (NFS) version 4 and higher requires user authentication. You can authenticate with Lightweight Directory Access Protocol (LDAP) server or local user accounts.

If you are using local user accounts, the NFSv4 domain must be set to the same value on all Linux servers and SVMs. Set the following parameters in the `/etc/idmapd.conf` file on the Linux hosts.

```
Domain = <domain name>
Nobody-User = root
Nobody-Group = root
```

**Note**  
You must restart the `nfs-idmapd.service` service after making changes to the domain.

 **Oracle Direct Network File System (dNFS)** 

SAP only supports deployment of Oracle database on Amazon FSx for NetApp ONTAP using Direct NFS with NFSv3, NFSv4 and NFSv4.1.

You must setup the `oranfstab` file before enabling dNFS client control of NFS. For more details, refer [Deploying Oracle Direct NFS](https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/deploying-dnfs.html#GUID-D06079DB-8C71-4F68-A1E3-A75D7D96DCE2). On configuration completion, query the `V$DNFS_SERVERS` view to verify that the server name, NFS mount points, and NFS version shown in the output match the configuration in `oranfstab` file.

## Create mount points
<a name="mount-points"></a>

See the following for details.

**Example**  
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
Create the following mount points on your Amazon EC2 instance.  

```
mkdir -p /sapmnt
mkdir -p /usr/sap
mkdir -p /sapdb/<DBSID>/sapdata
mkdir -p /sapdb/<DBSID>/saplog
mkdir -p /backup
mkdir -p /sapdb
```
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
<a name="mount-filesystem"></a>

The created file systems must be mounted as NFS file systems on Amazon EC2. See the following for details.

The following table is an example recommendation of NFS options for different IBM Db2 file systems.

**Example**  


<table>
<tbody>
  <tr><td rowspan="2"> <b>File systems</b> </td><td colspan="4"> <b>NFS mount options</b> </td></tr>
  <tr><td> <b> <b>Common</b> </b> </td><td> <b> <b>NFS version</b> </b> </td><td> <b> <b>NFS transfer size</b> </b> </td><td> <b> <b>nconnect</b> </b> </td></tr>
  <tr><td>Db2 data</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=8</td></tr>
  <tr><td>Db2 log</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Backup</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Db2 binary</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
</tbody>
</table>

 **Example**   
Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems.  

```
<SVM NFSIP>:/<SID>-sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<SID>-usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-db2dbsid /db2/db2<dbsid> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-dbpath /db2/<DBSID> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-sapdata1 /db2/<DBSID>/sapdata1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
<SVM NFSIP>:/<DBSID>-sapdata<x> /db2/<DBSID>/sapdata<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
<SVM NFSIP>:/<DBSID>-saptmp1 /db2/<DBSID>/saptmp1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-saptmp<x> /db2/<DBSID>/saptmp<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-logdir /db2/<DBSID>/log_dir nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-logarch /db2/<DBSID>/log_arch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-db2dump /db2/<DBSID>/db2dump nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFSIP>:/<DBSID>-backup /db2backup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
```
The following table is an example recommendation of NFS options for different SAP MaxDB file systems.


<table>
<tbody>
  <tr><td rowspan="2"> <b>File systems</b> </td><td colspan="4"> <b>NFS mount options</b> </td></tr>
  <tr><td> <b>Common</b> </td><td> <b>NFS version</b> </td><td> <b>NFS transfer size</b> </td><td> <b>nconnect</b> </td></tr>
  <tr><td>SAP MaxDB data</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=8</td></tr>
  <tr><td>SAP MaxDB log</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Backup</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>SAP MaxDB binary</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
</tbody>
</table>

 **Example**   
Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems.  

```
<BackupSVM NFSIP>:/<DBSID>_sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<BackupSVM NFSIP>:/<DBSID>_usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<BackupSVM NFSIP>:/<DBSID>_backup /backup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SAPLOGSVM NFSIP>:/<DBSID>_sapdb /sapdb nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SAPLOGSVM NFSIP>:/<DBSID>_log /sapdb/<DBSID>/saplog nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SAPLOGSVM NFSIP>:/<DBSID>_sapdata /sapdb/<DBSID>/sapdata nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
```
The following table is an example recommendation of NFS options for different SAP ASE file systems.


<table>
<tbody>
  <tr><td rowspan="2"> <b>File systems</b> </td><td colspan="4"> <b>NFS mount options</b> </td></tr>
  <tr><td> <b>Common</b> </td><td> <b>NFS version</b> </td><td> <b>NFS transfer size</b> </td><td> <b>nconnect</b> </td></tr>
  <tr><td>SAP ASE data</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=8</td></tr>
  <tr><td>SAP ASE log</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Backup</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>SAP ASE binary</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
</tbody>
</table>

 **Example**   
Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems.  

```
<SVM-ASEDBData NFSIP>:/<SID>-sapdata_1 /sybase/<SID>/sapdata_1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
<SVM-ASEDBLog NFSIP>:/<SID>-saplog_1 /sybase/<SID>/saplog_1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBShared NFSIP>:/<SID>-sapmnt /sapmnt nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBShared NFSIP>:/<SID>-usrsap /usr/sap nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBShared NFSIP>:/<SID>-sybase /sybase nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBShared NFSIP>:/<SID>-sapdiag /sybase/<SID>/sapdiag nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBShared NFSIP>:/<SID>-saptmp /sybase/<SID>/saptmp nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM-ASEDBBackup NFSIP>:/<SID>-backup /sybasebackup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
```
You must assign a virtual hostname to each SVM NFS IP address in `/etc/hosts` file. These hostnames are used in the `oranfstab` file for values of the NFS server `(server: )` during Oracle dNFS configuration.  
The following table is an example recommendation of NFS options for different SAP Oracle file systems.


<table>
<tbody>
  <tr><td rowspan="2"> <b>File systems</b> </td><td colspan="4"> <b>NFS mount options</b> </td></tr>
  <tr><td> <b>Common</b> </td><td> <b>NFS version</b> </td><td> <b>NFS transfer size</b> </td><td> <b>nconnect</b> </td></tr>
  <tr><td>Oracle data</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=8</td></tr>
  <tr><td>Oracle log</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Oracle backup</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
  <tr><td>Oracle binary</td><td>rw,bg,hard,timeo=600,noatime,</td><td>vers=4,minorversion=1,lock,</td><td>rsize=262144,wsize=262144,</td><td>nconnect=2</td></tr>
</tbody>
</table>

 **Example**   
Add the following lines to `/etc/fstab` to preserve mounted file systems during an instance reboot. You can then run `mount -a` to mount the NFS file systems.  

```
<SVM NFS Host>:/<DBSID>-oracle /oracle nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-oracle<DBSID> /oracle/<DBSID> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-oraarch /oracle/<DBSID>/oraarch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-saparch /oracle/<DBSID>/saparch nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-sapreorg /oracle/<DBSID>/sapreorg nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-sapbackup /oracle/<DBSID>/sapbackup nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-saptrace /oracle/<DBSID>/saptrace nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-sapdata1 /oracle/<DBSID>/sapdata1 nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
<SVM NFS Host>:/<DBSID>-sapdata2 /oracle/<DBSID>/sapdata<x> nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=8
<SVM NFS Host>:/<DBSID>-origlogA /oracle/<DBSID>/origlogA nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-origlogB /oracle/<DBSID>/origlogB nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-mirrlogB /oracle/<DBSID>/mirrlogB nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
<SVM NFS Host>:/<DBSID>-mirrlogA /oracle/<DBSID>/mirrlogA nfs rw,bg,hard,timeo=600,noatime,vers=4,minorversion=1,lock,rsize=262144,wsize=262144,nconnect=2
```
<SVM NFS Host> are the values that you have assigned in the `/etc/hosts` file for each SVM NFS IP address.  
+ Changes to the `nconnect` parameter take effect only if the NFS file system is unmounted and mounted again.
+ Client systems must have unique host names when accessing FSx for ONTAP. If there are systems with the same name, the second system may not be able to access FSx for ONTAP.
+ For RHEL operating system, the `nconnect` parameter is supported only on RHEL 8.3 or higher.