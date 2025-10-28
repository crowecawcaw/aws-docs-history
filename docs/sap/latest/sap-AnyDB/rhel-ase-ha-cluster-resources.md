# Cluster resources

This section covers the following topics.

###### Topics

- [Enable and start the cluster](#start-cluster "#start-cluster")
- [Increase corosync totem timeout](#increase-timeout "#increase-timeout")
- [Check cluster status](#cluster-status "#cluster-status")
- [Prepare for resource creation](#resource-creation "#resource-creation")
- [Cluster bootstrap](#cluster-bootstrap "#cluster-bootstrap")
- [Create fence_aws STONITH resource](#create-stonith "#create-stonith")
- [Create file system resources](#filesystem-resources "#filesystem-resources")
- [Create overlay IP resources](#overlay-ip-resources "#overlay-ip-resources")
- [Create SAP ASE database resource](#ase-database-resource "#ase-database-resource")
- [Activate cluster](#activate-cluster "#activate-cluster")

## Enable and start the cluster

This is applicable to both cluster nodes. Run the following command to enable and start the `pacemaker` cluster service on both nodes.

```
pcs cluster enable --all
rhxdbhost01: Cluster Enabled
rhxdbhost02: Cluster Enabled


pcs cluster start --all
rhxdbhost01: Starting Cluster...
rhxdbhost02: Starting Cluster...
```

By enabling the `pacemaker` service, the server automatically joins the cluster after a reboot. This ensures that your system is protected. Alternatively, you can start the `pacemaker` service manually on boot. You can then investigate the cause of failure. However, this is generally not required for SAP NetWeaver ASCS cluster.

## Increase corosync totem timeout

**RHEL 7.x**

1. Edit the `/etc/corosync/corosync.conf` file in all cluster nodes to increase the token value or to add a value if it is not present.

```
totem {
    version: 2
    secauth: off
    cluster_name: my-rhel-sap-cluster
    transport: udpu
    rrp_mode: passive
    token: 29000  <------ Value to be set
}
```

2. Reload the corosync with the following command, on any one of the cluster nodes. This does not cause any downtime.

```
pcs cluster reload corosync
```

3. Use the following command to confirm if the changes are active.

```
corosync-cmapctl | grep totem.token
Runtime.config.totem.token (u32) = 29000
```

**RHEL 8.x**

Use the following command to increase the token value or to add a value if it is not present.

```
pcs cluster config update totem token=29000
```

## Check cluster status

Once the cluster service `pacemaker` is started, check the cluster status with `pcs status` command, as shown in the following example. Both the primary (`rhxdbhost01`) and secondary (`rhxdbhost02`) servers should be seen as online.

```
pcs status
Cluster name: rhelha

WARNINGS:
No stonith devices and stonith-enabled is not false

Cluster Summary:
  * Stack: corosync
  * Current DC: rhxdbhost01 (version 2.0.3-5.el8_2.5-4b1f869f0f) - partition with quorum
  * Last updated: Tue Jan 10 21:32:15 2023
  * Last change:  Tue Jan 10 19:46:50 2023 by hacluster via crmd on rhxdbhost01
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ rhxdbhost01 rhxdbhost02 ]

Full List of Resources:
  * No resources

Daemon Status:
  corosync: active/enabled
  pacemaker: active/enabled
  pcsd: active/enabled
```

## Prepare for resource creation

To ensure that the cluster does not perform any unexpected actions during setup of resources and configuration, set the maintenance mode to true.

Run the following command to put the cluster in maintenance mode.

```
pcs property set maintenance-mode=true
```

## Cluster bootstrap

Configure the cluster bootstrap parameters by running the following commands.

```
pcs resource defaults update resource-stickiness=1
pcs resource defaults update migration-threshold=3
```

## Create `fence_aws` STONITH resource

Modify the commands in the following table to match your configuration values.

```
pcs stonith create rsc_aws_stonith_<DBSID> fence_aws region=us-east-1 pcmk_host_map="rhxdbhost01:i-xxxxinstidforhost1;rhxdbhost02:i-xxxxinstidforhost2" power_timeout=240 pcmk_reboot_timeout=300 pcmk_reboot_retries=2 pcmk_delay_max=30 pcmk_reboot_action=reboot op start timeout=180 op stop timeout=180 op monitor interval=180 timeout=60
```

###### Note

The default `pcmk` action is reboot. If you want to have the instance remain in a stopped state until it has been investigated, and then manually started again, add `pcmk_reboot_action=off`. Any High Memory (`u-**tb1.**`) instance or metal instance running on a dedicated host won’t support reboot, and will require `pcmk_reboot_action=off`.

## Create file system resources

Mounting and unmounting file system resources to align with the location of SAP ASE database is done using cluster resources.

Modify and run the following commands to create these file system resources.

**/sybase**

```
pcs resource create rsc_fs_<DBSID>_sybase ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sybase" directory="/sybase" fstype="nfs4" options=" rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/sapdata_1**

```
pcs resource create rsc_fs_<DBSID>_data ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/asedata" directory="/sybase/<DBSID>/sapdata_1" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=8,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/saplog_1**

```
pcs resource create rsc_fs_<DBSID>_log ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/aselog" directory="/sybase/<DBSID>/saplog_1" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/sapdiag**

```
pcs resource create rsc_fs_<DBSID>_diag ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sapdiag" directory="/sybase/<DBSID>/sapdiag" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybase/<DBSID>/saptmp**

```
pcs resource create rsc_fs_<DBSID>_tmp ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/saptmp" directory="/sybase/<DBSID>/saptmp" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/sybasebackup**

```
pcs resource create rsc_fs_<DBSID>_bkp ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/sybasebackup" directory="/backup" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**/usr/sap**

```
pcs resource create rsc_fs_<DBSID>_sap ocf:heartbeat:Filesystem params device="<nfs.fqdn>:/usrsap" directory="/usr/sap" fstype="nfs4"
options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" op start timeout=60s interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**Notes**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP and AWS.
- <nfs.fqdn> must be the alias of the FSx for ONTAP resource. For example, `fs-xxxxxx.efs.xxxxxx.amazonaws.com`.
- It is important to create the resources in the proper mount order/sequence.

## Create overlay IP resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Use the following command to create an SAP ASE database IP resource.

```
pcs resource create rsc_ip_<DBSID>_ASEDB ocf:heartbeat:aws-vpc-move-ip ip=172.16.0.23 interface=eth0 routing_table=rtb-xxxxxroutetable1 op monitor interval=20s timeout=40s --group rsc_asedb_group
```

**Notes**

- If more than one route table is required for connectivity or because of subnet associations, the `routing_table` parameter can have multiple values separated by a comma. For example, `routing_table=rtb-xxxxxroutetable1, rtb-xxxxxroutetable2`.
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see [Shared VPC – optional](../sap-netweaver/rhel-netweaver-ha-settings.md#rhel-netweaver-ha-shared-vpc "../sap-netweaver/rhel-netweaver-ha-settings.md#rhel-netweaver-ha-shared-vpc").

## Create SAP ASE database resource

SAP ASE database is started and stopped using cluster resources.

Modify and run the following command to create the `SAPDatabase` resource.

```
pcs resource create rsc_ase_<DBSID>_ASEDB ocf:heartbeat:SAPDatabase SID=<DBSID> DBTYPE=SYB STRICT_MONITORING=TRUE op start timeout=300 op stop timeout=300 --group grp_<DBSID>_ASEDB
```

Use the following command for more details on the resource.

```
pcs resource describe ocf:heartbeat:SAPDatabase
```

## Activate cluster

Use `pcs config show` to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources.

```
pcs property set maintenance-mode=false
```

See the [Sample configuration](../sap-netweaver/rhel-sample-configuration.md "../sap-netweaver/rhel-sample-configuration.md").
