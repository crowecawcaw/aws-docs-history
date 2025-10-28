# Cluster resources

This section covers the following topics.

###### Topics

- [Enable and start the cluster](#start-cluster "#start-cluster")
- [Check cluster status](#cluster-status "#cluster-status")
- [Prepare for resource creation](#resource-creation "#resource-creation")
- [Cluster bootstrap](#cluster-bootstrap "#cluster-bootstrap")
- [Create fence_aws STONITH resource](#create-stonith "#create-stonith")
- [Create file system resources](#filesystem-resources "#filesystem-resources")
- [Create overlay IP resources](#overlay-ip-resources "#overlay-ip-resources")
- [Create SAPInstance resources](#sap-resources "#sap-resources")
- [Create resource constraints](#resource-constraints "#resource-constraints")
- [Activate cluster](#activate-cluster "#activate-cluster")

## Enable and start the cluster

This is applicable to both cluster nodes. Run the following command to enable and start the `pacemaker` cluster service on both nodes.

```
pcs cluster enable --all
<rhxhost01>: Cluster Enabled
<rhxhost02>: Cluster Enabled


pcs cluster start --all
<rhxhost01>: Starting Cluster...
<rhxhost02>: Starting Cluster...
```

By enabling the `pacemaker` service, the server automatically joins the cluster after a reboot. This ensures that your system is protected. Alternatively, you can start the `pacemaker` service manually on boot. You can then investigate the cause of failure. However, this is generally not required for SAP NetWeaver ASCS cluster.

## Check cluster status

Once the cluster service `pacemaker` is started, check the cluster status with `pcs status` command, as shown in the following example. Both the primary (`rhxhost01`) and secondary (`rhxhost02`) servers should be seen as online.

```
pcs status
Cluster name: <rhelha>

WARNINGS:
No stonith devices and stonith-enabled is not false

Cluster Summary:
  * Stack: corosync
  * Current DC: <rhxhost01> (version <2.0.3-5.el8_2.5-4b1f869f0f>) - partition with quorum
  * Last updated: Tue Jan 10 21:32:15 2023
  * Last change:  Tue Jan 10 19:46:50 2023 by hacluster via crmd on <rhxhost01>
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ <rhxhost01> <rhxhost02> ]

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
pcs stonith create <rsc_aws_stonith_RHX> fence_aws region=<us-east-1> pcmk_host_map="<rhxhost01>:<i-xxxxinstidforhost1>;<rhxhost02>:<i-xxxxinstidforhost2>" power_timeout=240 pcmk_reboot_timeout=300 pcmk_reboot_retries=2 pcmk_delay_max=30 pcmk_reboot_action=reboot op start timeout=180 op stop timeout=180 op monitor interval=180 timeout=60
```

###### Note

The default `pcmk` action is reboot. If you want to have the instance remain in a stopped state until it has been investigated, and then manually started again, add `pcmk_reboot_action=off`. Any High Memory (`u-*tb1.*`) instance or metal instance running on a dedicated host won’t support reboot, and will require `pcmk_reboot_action=off`.

## Create file system resources

Mounting and unmounting of file system resources to align with the location of the SAP services is done using cluster resources.

Modify and run the following commands to create the file system resources.

**ASCS**

Use the following command to create ASCS file system resources.

```
pcs resource create <rsc_fs_RHX_ASCS0> ocf:heartbeat:Filesystem device=<nfs.fqdn>:/<RHX_ASCS00> directory=</usr/sap/RHX/ASCS00> fstype=nfs4 options="<nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport>" force_unmount=safe --group <grp_RHX_ASCS00>
```

**ERS**

Use the following command to create ERS file system resources.

```
pcs resource create <rsc_fs_RHX_ERS10> ocf:heartbeat:Filesystem device=<nfs.fqdn>:/<RHX_ERS10> directory=</usr/sap/RHX/ERS10> fstype=nfs4 options="<nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport>" force_unmount=safe --group <grp_RHX_ERS10>
```

**Notes for ASCS and ERS**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP.
- <nfs.fqdn> can either be an alias or the default file system resource name of the NFS or FSx for ONTAP resource. For example, `fs-xxxxxx.efs.xxxxxx.amazonaws.com`.

## Create overlay IP resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Modify and run the commands in the table to create IP resources.

**ASCS**

Use the following command to create an ASCS IP resource.

```
pcs resource create <rsc_ip_RHX_ASCS00> ocf:heartbeat:aws-vpc-move-ip ip=<172.16.30.5> interface=eth0 routing_table=<rtb-xxxxxroutetable1> op monitor interval=20s timeout=40s --group <grp_RHX_ASCS00>
```

**ERS**

Use the following command to create an ERS IP resource.

```
pcs resource create <rsc_ip_RHX_ERS10> ocf:heartbeat:aws-vpc-move-ip ip=<172.16.30.6> interface=eth0 routing_table=<rtb-xxxxxroutetable1> op monitor interval=20s timeout=40s --group <grp_RHX_ERS10>
```

**Notes for ASCS and ERS**

- If more than one route table is required for connectivity or because of subnet associations, the `routing_table` parameter can have multiple values separated by a comma. For example, `routing_table=rtb-xxxxxroutetable1, rtb-xxxxxroutetable2`.
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see [Shared VPC – optional](rhel-netweaver-ha-settings.md#rhel-netweaver-ha-shared-vpc "rhel-netweaver-ha-settings.md#rhel-netweaver-ha-shared-vpc").

## Create `SAPInstance` resources

The SAP instance is started and stopped using cluster resources. Modify and run the commands in the table to create `SAPInstance` resources.

###### Note

The change between ENSA1 and ENSA2 that allows the lock table to be consumed remotely, means that for ENSA2, ASCS can restart in its current location (assuming the node is still available). This change impacts stickiness, migration, and priority parameters. Ensure to use the right command for your enqueue version.

ENSA1
Use the following command to create an **ASCS**
`SAPInstance` resource.

```
pcs resource create <rsc_sap_RHX_ASCS00> ocf:heartbeat:SAPInstance InstanceName="<RHX_ASCS00_rhxascs>" START_PROFILE=</usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs> AUTOMATIC_RECOVER=false meta resource-stickiness=5000 migration-threshold=1 op monitor interval=20s on-fail=restart timeout=60s op start interval=0s timeout=240s op stop interval=0s timeout=600s --group <grp_RHX_ASCS00>
```

Add a resource stickiness to the group to ensure that ASCS will stay on node, if possible.

```
pcs resource meta <grp_RHX_ASCS00> resource-stickiness=3000
```

Use the following command to create an **ERS**
`SAPInstance` resource.

```
pcs resource create <rsc_sap_RHX_ERS10> ocf:heartbeat:SAPInstance InstanceName="<RHX_ERS10_rhxers>" START_PROFILE=</usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers> AUTOMATIC_RECOVER=false IS_ERS=true op monitor interval=20s on-fail=restart timeout=60s op start interval=0s timeout=600s op stop interval=0s timeout=240s --group <grp_RHX_ERS10>
```

ENSA2
Use the following command to create an **ASCS**
`SAPInstance` resource.

```
pcs resource create <rsc_sap_RHX_ASCS0> ocf:heartbeat:SAPInstance InstanceName="<RHX_ASCS00_rhxascs>" START_PROFILE=</usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxasc> AUTOMATIC_RECOVER=false meta resource-stickiness=5000 op monitor interval=11s on-fail=restart timeout=60s op start interval=0s timeout=600s op stop interval=0s timeout=240s --group <grp_RHX_ASCS00>
```

Add a resource stickiness to the group to ensure that ASCS will stay on node, if possible.

```
pcs resource meta <grp_RHX_ASCS00> resource-stickiness=3000
```

###### Note

`meta resource-stickiness=5000` is here to balance the failover constraint with ERS, so the resource stays on the node where it started, and doesn’t migrate around cluster uncontrollably.

Use the following command to create an **ERS**
`SAPInstance` resource.

```
pcs resource create <rsc_sap_RHX_ERS10> ocf:heartbeat:SAPInstance InstanceName="<RHX_ERS10_rhxers>" START_PROFILE=</usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers> AUTOMATIC_RECOVER=false op monitor interval=20s on-fail=restart timeout=60s op start interval=0s timeout=600s op stop interval=0s timeout=240s --group <grp_RHX_ERS10>
```

The difference between ENSA1 and ENSA2 is that ENSA2 allows the lock table to be consumed remotely, which means that for ENSA2, ASCS can restart in its current location (assuming the node is still available). This change impacts stickiness, migration and priority parameters. Ensure that you use the right command for your enqueue version.

## Create resource constraints

Resource constraints are used to determine where resources run, or alternatively where resources are located, per the conditions. Constraints for SAP NetWeaver ensure that ASCS and ERS are started on separate nodes, and locks are preserved in case of failures. The following are the different types of constraints.

**Colocation constraint**

The negative score ensures that ASCS and ERS are run on separate nodes, wherever possible.

```
pcs constraint colocation add <grp_RHX_ERS10> with <grp_RHX_ASCS00> -5000
```

**Order constraint**

This constraint ensures the ASCS instance is started prior to stopping the ERS instance. This can be necessary to consume the lock table.

```
pcs constraint order start <grp_RHX_ASCS00> then stop <grp_RHX_ERS10> symmetrical=false kind=Optional
```

**Location constraint** (ENSA1 only)

This constraint is only required for ENSA1. The lock table can be retrieved remotely for ENSA2, and as a result ASCS doesn’t failover to where ERS is running.

```
pcs constraint location <rsc_sap_RHX_ASCS00> rule score=2000 <runs_ers_RHX> eq 1
```

## Activate cluster

Use `pcs config show` to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources.

```
pcs property set maintenance-mode=false
```

See the [Sample configuration](rhel-sample-configuration.md "rhel-sample-configuration.md").
