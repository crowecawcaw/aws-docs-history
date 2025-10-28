# Cluster resources

This section covers the following topics.

###### Topics

- [Enable and start the cluster](#start-cluster "#start-cluster")
- [Check cluster status](#cluster-status "#cluster-status")
- [Prepare for resource creation](#resource-creation "#resource-creation")
- [Reset configuration – optional](#reset-configuration "#reset-configuration")
- [Cluster bootstrap](#cluster-bootstrap "#cluster-bootstrap")
- [Create Amazon EC2 STONITH resource](#create-stonith "#create-stonith")
- [Create file system resources](#filesystem-resources "#filesystem-resources")
- [Create overlay IP resources](#overlay-ip-resources "#overlay-ip-resources")
- [Create SAP ASE database resource](#ase-database-resource "#ase-database-resource")
- [Activate cluster](#activate-cluster "#activate-cluster")

## Enable and start the cluster

This is applicable to both cluster nodes. Run the following command to enable and start the `pacemaker` cluster service on both nodes.

```
systemctl enable --now pacemaker
```

or

```
systemctl start pacemaker
```

By enabling the `pacemaker` service, the server automatically joins the cluster after a reboot. This ensures that your system is protected. Alternatively, you can start the `pacemaker` service manually on boot. You can then investigate the cause of failure. However, this is generally not required for SAP NetWeaver ASCS cluster.

Run the following command to check the status of the `pacemaker` service.

```
systemctl status pacemaker
● pacemaker.service - Pacemaker High Availability Cluster Manager
     Loaded: loaded (/usr/lib/systemd/system/pacemaker.service; <enabled>; vendor preset: disabled)
     Active: <active (running)> since Tue XXXX-XX-XX XX:XX:XX XXX; XXh ago
       Docs: man:pacemakerd
             https://clusterlabs.org/pacemaker/doc/en-US/Pacemaker/2.0/html-single/Pacemaker_Explained/index.html
   Main PID: 1899 (pacemakerd)
Enable cluster service (optional)
```

## Check cluster status

Once the cluster service `pacemaker` is started, check the cluster status with `crm mon` command, as shown in the following example.

```
crm_mon -1
Cluster Summary:
  * Stack: corosync
  * Current DC: <slxdbhost01> (version 2.0.xxxxxxxxxxx) - partition with quorum
  * Last updated:
  * Last change:  by hacluster via crmd on slxdbhost01
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ <slxdbhost0> <slxdbhost02> ]

Active Resources:
  * No active resources
```

The primary (`slxdbhost01`) and secondary (`slxdbhost02`) must show up as online.

You can find the ring status and the associated IP address of the cluster with `corosync-cfgtool` command, as shown in the following example.

```
corosync-cfgtool -s
Printing ring status.
Local node ID 1
RING ID 0
        id      = <10.1.10.1>
        status  = ring 0 active with no faults
RING ID 1
        id      = <10.1.10.2>
        status  = ring 1 active with no faults
```

## Prepare for resource creation

To ensure that the cluster does not perform any unexpected actions during setup of resources and configuration, set the maintenance mode to true.

Run the following command to put the cluster in maintenance mode.

```
crm maintenance on
```

## Reset configuration – _optional_

###### Note

The following instructions help you reset the complete configuration. Run these commands only if you want to start setup from the beginning. You can make minor changes with the `crm edit` command.

Run the following command to back up the current configuration for reference.

```
crm config show > /tmp/crmconfig_backup.txt
```

Run the following command to clear the current configuration.

```
crm configure erase
```

###### Important

Once the preceding erase command is executed, it removes all of the cluster resources from Cluster Information Base (CIB), and disconnects the communication from `corosync` to the cluster. Before starting the resource configuration run `crm cluster restart`, so that cluster reestablishes communication with `corosync`, and retrieves the configuration. The restart of cluster removes _maintenance mode_. Reapply before commencing additional configuration and resource setup.

## Cluster bootstrap

Configure the cluster bootstrap parameters by running the following commands.

```
crm configure rsc_defaults resource-stickiness=1
crm configure rsc_defaults migration-threshold=3
crm configure property stonith-enabled="true"
crm configure property stonith-action="off"
crm configure property stonith-timeout="300s"
crm configure op_defaults timeout="300s"
crm configure op_defaults record-pending="true"
```

## Create Amazon EC2 STONITH resource

Modify the following command to match your configuration values.

```
crm configure primitive res_{aws}_STONITH stonith:external/ec2 op start interval=0 timeout=180s op stop interval=0 timeout=180s op monitor interval=180s timeout=60s params tag=pacemaker profile=cluster pcmk_delay_max=30
```

**profile** – this refers to the AWS CLI profile crated during setup. In the preceding command, _cluster_ is the profile name.

## Create file system resources

Mounting and unmounting file system resources to align with the location of SAP ASE database is done using cluster resources.

Modify and run the following commands to create these file system resources.

**/sybase**

```
crm configure primitive rsc_fs_<DBSID>_sybase ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sybase" directory="/sybase" fstype="nfs4" options=" rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/sapdata_1**

```
crm configure primitive rsc_fs_<DBSID>_data ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/asedata" directory="/sybase/<DBSID>/sapdata_1" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=8,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/saplog_1**

```
crm configure primitive rsc_fs_<DBSID>_log ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/aselog" directory="/sybase/<DBSID>/saplog_1" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/sapdiag**

```
crm configure primitive rsc_fs_<DBSID>_diag ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sapdiag" directory="/sybase/<DBSID>/sapdiag" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/saptmp**

```
crm configure primitive rsc_fs_<DBSID>_tmp ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/saptmp" directory="/sybase/<DBSID>/saptmp" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybasebackup**

```
crm configure primitive rsc_fs_<DBSID>_bkp ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sybasebackup" directory="/backup" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/usr/sap**

```
crm configure primitive rsc_fs_<DBSID>_sap ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/usrsap" directory="/usr/sap" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**Notes**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP and AWS.
- <nfs.fqdn> must be the alias of the FSx for ONTAP resource. For example, `svm-xxxxx.fs-xxxxx.<region>.amazonaws.com`.
- Your file system structure can vary – it can have multiple data file systems. The preceding examples must be adapted to your environment.

## Create overlay IP resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Modify and run the following command to create IP resources.

```
crm configure primitive rsc_ip_<DBSID>_ASEDB ocf:heartbeat:aws-vpc-move-ip params ip=172.16.0.29 routing_table=rtb-xxxxxroutetable1 interface=eth0 profile=cluster op start interval=0 timeout=180s op stop interval=0 timeout=180s op monitor interval=20s timeout=40s
```

**Notes**

- If more than one route table is required for connectivity or because of subnet associations, the `routing_table` parameter can have multiple values separated by a comma. For example, `routing_table=rtb-xxxxxroutetable1, rtb-xxxxxroutetable2`.
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see [Shared VPC – optional](../sap-netweaver/sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc "../sap-netweaver/sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc").

## Create SAP ASE database resource

SAP ASE database is started and stopped using cluster resources.

Modify and run the following command to create the `SAPDatabase` resource.

```
crm configure primitive rsc_ase_<DBSID>_ASEDB ocf:heartbeat:SAPDatabase SID=<DBSID> DBTYPE=SYB STRICT_MONITORING=TRUE op start timeout=300 op stop timeout=300
```

Create the cluster resource group, and the resources together in the order in which the services will be started and stopped.

```
crm configure group grp_<DBSID>_ASEDB rsc_fs_<DBSID>_sybase rsc_fs_<DBSID>_data rsc_fs_<DBSID>_log rsc_fs_<DBSID>_diag rsc_fs_<DBSID>_tmp rsc_fs_<DBSID>_bkp rsc_fs_<DBSID>_sap rsc_aws_stonith_<DBSID> rsc_ase_<DBSID>_ASEDB
```

## Activate cluster

Use `crm config show` and `crm config edit` commands to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources.

`crm maintenance off`

See the [Sample configuration](../sap-netweaver/sample-configuration.md "../sap-netweaver/sample-configuration.md").
