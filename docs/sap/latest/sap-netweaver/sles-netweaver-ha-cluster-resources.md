# Cluster resources

This section covers the following topics.

###### Topics

- [Enable and start the cluster](#start-cluster "#start-cluster")
- [Check cluster status](#cluster-status "#cluster-status")
- [Prepare for resource creation](#resource-creation "#resource-creation")
- [Reset configuration – optional](#reset-configuration "#reset-configuration")
- [Cluster bootstrap](#cluster-bootstrap "#cluster-bootstrap")
- [Create Amazon EC2 STONITH resource](#create-stonith "#create-stonith")
- [Create file system resources (classic only)](#filesystem-resources "#filesystem-resources")
- [Create overlay IP resources](#overlay-ip-resources "#overlay-ip-resources")
- [Create sapstartsrv resources (simple-mount only)](#sapstartsrv-resources "#sapstartsrv-resources")
- [Create SAP instance resources (simple-mount only)](#sap-resources-simple "#sap-resources-simple")
- [Create SAP instance resources (classic only)](#sap-resources-classic "#sap-resources-classic")
- [Create cluster resource groups for ip / sapstart / sap (simple-mount only)](#resource-groups-simple "#resource-groups-simple")
- [Create cluster resource groups for ip/sapstart/sap (classic only)](#resource-groups-classic "#resource-groups-classic")
- [Create resource constraints](#resource-constraints "#resource-constraints")
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
  * Current DC: <slxhost01> (version 2.0.xxxxxxxxxxx) - partition with quorum
  * Last updated:
  * Last change:  by hacluster via crmd on slxhost01
  * 2 nodes configured
  * 0 resource instances configured

Node List:
  * Online: [ <slxhost01> <slxhost02> ]

Active Resources:
  * No active resources
```

The primary (`slxhost01`) and secondary (`slxhost02`) must show up as online.

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

Add the following command for ENSA2 only. Priority fencing is not possible with ENSA1 constraint priority settings.

```
crm configure property priority-fencing-delay="30s"
```

## Create Amazon EC2 STONITH resource

Modify the commands in the following table to match your configuration values.

ENSA1

- Use the following command to create STONITH resource.

```
crm configure primitive res_AWS_STONITH stonith:external/ec2 op start interval=0
timeout=180s op stop interval=0 timeout=180s op monitor interval=180s timeout=60s params
tag=<pacemaker> profile=<cluster> pcmk_delay_max=30
```

**profile** – this refers to the AWS CLI profile crated during setup. In the preceding command, _cluster_ is the profile name.

ENSA2

- Use the following command to create STONITH resource with priority fencing delay.

```
crm configure primitive res_AWS_STONITH stonith:external/ec2 op start interval=0
timeout=180s op stop interval=0 timeout=180s op monitor interval=180s timeout=60s params
tag=<pacemaker> profile=<cluster> pcmk_delay_max=10
```

**profile** – this refers to the AWS CLI profile crated during setup. In the preceding command, _cluster_ is the profile name.

## Create file system resources (classic only)

In classic configuration, the mounting and unmounting of file system resources to align with the location of the SAP services is done using cluster resources.

Modify and run the following commands to create the file system resources.

**ASCS**

Use the following command to create ASCS file system resources.

```
crm configure primitive rsc_fs_<SLX>_ASCS<00> ocf:heartbeat:Filesystem params
device="<nfs.fqdn>:/<SLX>_ASCS<00>" directory="/usr/sap/<SLX>/ASCS<00>" fstype="nfs4"
options=<"rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2"> op start timeout=60s
interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**ERS**

Use the following command to create ERS file system resources.

```
crm configure primitive rsc_fs_<SLX>_ERS<10> ocf:heartbeat:Filesystem params
device="<nfs.fqdn>:/<SLX>_ERS<10>" directory="/usr/sap/<SLX>/ERS<10>" fstype="nfs4"
options=<"rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2"> op start timeout=60s
interval=0 op stop timeout=60s interval=0 op monitor interval=20s timeout=40s
```

**Notes**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP.
- <nfs.fqdn> can either be an alias or the default file system resource name of the NFS or FSx for ONTAP resource. For example, `fs-xxxxxx.efs.xxxxxx.amazonaws.com`.

## Create overlay IP resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Modify and run the commands in the table to create IP resources.

**ASCS**

Use the following command to create an ASCS IP resource.

```
crm configure primitive rsc_ip_<SLX>_ASCS<00> ocf:heartbeat:aws-vpc-move-ip params
ip=<172.16.30.5> routing_table=<rtb-xxxxxroutetable1> interface=eth0 profile=<cluster> op start
interval=0 timeout=180s op stop interval=0 timeout=180s op monitor interval=20s timeout=40s
```

**ERS**

Use the following command to create an ERS IP resource.

```
crm configure primitive rsc_ip_<SLX>_ERS<10> ocf:heartbeat:aws-vpc-move-ip params ip=<172.16.30.6>
routing_table=<rtb-xxxxxroutetable1> interface=eth0 profile=<cluster> op start interval=0
timeout=180s op stop interval=0 timeout=180s op monitor interval=20s timeout=40s
```

**Notes**

- If more than one route table is required for connectivity or because of subnet associations, the `routing_table` parameter can have multiple values separated by a comma. For example, `routing_table=rtb-xxxxxroutetable1, rtb-xxxxxroutetable2`.
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see {https---docs-aws-amazon-com-sap-latest-sap-netweaver-sles-netweaver-ha-settings-html-sles-netweaver-ha-shared-vpc}[Shared VPC – optional].

## Create `sapstartsrv` resources (simple-mount only)

In simple-mount architecture, the `sapstartsrv` process that is used to control start/stop and monitoring of an SAP instance, is controlled by a cluster resource. This new resource adds additional control that removes the requirement for file system resources to be restricted to a single node.

Modify and run the commands in the table to create `sapstartsrv` resource.

**ASCS**

Use the following command to create an ASCS `sapstartsrv` resource.

```
crm configure primitive rsc_sapstart_<SLX>_ASCS<00> ocf:suse:SAPStartSrv params
InstanceName=<SLX>_ASCS<00>_<slxascs>
```

**ERS**

Use the following command to create an ERS `sapstartsrv` resource.

```
crm configure primitive rsc_sapstart_<SLX>_ERS<10> ocf:suse:SAPStartSrv params
InstanceName=<SLX>_ERS<10>_<slxers>
```

## Create SAP instance resources (simple-mount only)

The minor difference in creating SAP instance resources between classic and simple-mount configurations is the addition of `MINIMAL_PROBE=true` parameters.

The SAP instance is started and stopped using cluster resources. Modify and run the commands in the table to create SAP instance resources.

ENSA1

- Use the following command to create an **ASCS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ASCS<00> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ASCS<00>-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX>_ASCS<00>_<slxascs>
START_PROFILE="/usr/sap/SLX/SYS/profile/<SLX_ASCS00_slxascs>" AUTOMATIC_RECOVER=false
MINIMAL_PROBE=true meta resource-stickiness=5000 failure-timeout=60 migration-threshold=1
priority=10
```

Use the following command to create an **ERS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ERS<10> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ERS<10>-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ERS10_slxers>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ERS10_slxers<" AUTOMATIC_RECOVER=false
MINIMAL_PROBE=true IS_ERS=true meta priority=1000
```

ENSA2

- Use the following command to create an **ASCS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ASCS<00> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_SLX_ASCS00-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ASCS00_slxascs>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ASCS00_slxascs>" AUTOMATIC_RECOVER=false
MINIMAL_PROBE=true meta resource-stickiness=5000 priority=1000
```

Use the following command to create an **ERS** SAP instance resource.

```
crm configure primitive rsc_sap_SLX_ERS10 ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_SLX_ERS10-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ERSSLX_slxers>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/SLX_ERS10_slxers" AUTOMATIC_RECOVER=false
MINIMAL_PROBE=true IS_ERS=true
```

The difference between ENSA1 and ENSA2 is that ENSA2 allows the lock table to be consumed remotely, which means that for ENSA2, ASCS can restart in its current location (assuming the node is still available). This change impacts stickiness, migration and priority parameters. Ensure that you use the right command for your enqueue version.

## Create SAP instance resources (classic only)

The SAP instance is started and stopped using cluster resources. Modify and run the commands in the table to create SAP instance resources.

ENSA1

- Use the following command to create an **ASCS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ASCS<00> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ASCS<00>-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ASCS00_slxascs>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ASCS00_slxascs>" AUTOMATIC_RECOVER=false meta
resource-stickiness=5000 failure-timeout=60 migration-threshold=1 priority=10
```

Use the following command to create an **ERS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ERS<10> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ERS<10>-operations op monitor interval=11s on-fail=restart timeout=60s op
stop interval=0s timeout=240s on-fail=restart params InstanceName=<SLX_ERS10_slxers>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ERS10_slxers>" AUTOMATIC_RECOVER=false
IS_ERS=true meta priority=1000
```

ENSA2

- Use the following command to create an **ASCS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ASCS<00> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ASCS<00>-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ASCS00_slxascs>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ASCS00_slxascs>" AUTOMATIC_RECOVER=false meta
resource-stickiness=5000 priority=1000
```

Use the following command to create an **ERS** SAP instance resource.

```
crm configure primitive rsc_sap_<SLX>_ERS<10> ocf:heartbeat:SAPInstance operations
\$id=rsc_sap_<SLX>_ERS<10>-operations op monitor interval=11s timeout=60s on-fail=restart op
stop interval=0s timeout=240s params InstanceName=<SLX_ERS10_slxers>
START_PROFILE="/usr/sap/<SLX>/SYS/profile/<SLX_ERS10_slxers>" AUTOMATIC_RECOVER=false
IS_ERS=true
```

The change between ENSA1 and ENSA2 allows the lock table to be consumed remotely. If the node is still available, ASCS can restart in its current location for ENSA2. This impacts stickiness, migration, and priority parameters. Make sure to use the right command, depending on your enqueue server.

## Create cluster resource groups for `ip / sapstart / sap` (simple-mount only)

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

In simple-mount architecture, the overlay IP must be available first, then the SAP services are started before the SAP instance can start. Modify and run the commands in the table to create cluster resource groups.

**ASCS**

Use the following command to create an ASCS cluster resource group.

```
crm configure group grp_<SLX>_ASCS<00> rsc_ip_<SLX>_ASCS
rsc_sapstart_SLX_ASCS00 rsc_sap_<SLX>_ASCS<00> meta resource-stickiness=3000
```

**ERS**

Use the following command to create an ERS cluster resource group.

```
crm configure group grp_<SLX>_ERS<10> rsc_ip_<SLX>_ERS<10> rsc_sapstart_<SLX>_ERS<10> rsc_sap_<SLX>_ERS

```

## Create cluster resource groups for `ip/sapstart/sap` (classic only)

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

In classic architecture, the file system is mounted first, then the overlay IP must be available before the SAP instance can start. Modify and run the commands in the table to create cluster resource groups.

**ASCS**

Use the following command to create an ASCS cluster resource group.

```
crm configure group grp_<SLX>_ASCS<00> rsc_fs_<SLX>_ASCS<00> rsc_ip_<SLX>_ASCS<00> rsc_sap_<SLX>_ASCS
meta resource-stickiness=3000
```

**ERS**

Use the following command to create an ERS cluster resource group.

```
crm configure group grp_<SLX>_ERS<10> rsc_fs_<SLX>_ERS<10> rsc_ip_<SLX>_ERS<10> rsc_sap_<SLX>_ERS

```

## Create resource constraints

Resource constraints are used to determine where resources run per the conditions. Constraints for SAP NetWeaver ensure that ASCS and ERS are started on separate nodes and locks are preserved in case of failures. The following are the different types of constraints.

**Colocation constraint**

The negative score ensures that ASCS and ERS are run on separate nodes, wherever possible.

```
crm configure colocation col_sap_<SLX>_separate -5000: grp_<SLX>_ERS<10> grp_<SLX>_ASCS

```

**Order constraint**

This constraint ensures the ASCS instance is started prior to stopping the ERS instance. This is necessary to consume the lock table.

```
crm configure order ord_sap_<SLX>_first_start_ascs Optional: rsc_sap_<SLX>_ASCS<00>:start rsc_sap_<SLX>_ERS<10>:stop symmetrical=false
```

**Location constraint** (ENSA1 only)

This constraint is only required for ENSA1. The lock table can be retrieved remotely for ENSA2, and as a result ASCS doesn’t failover to where ERS is running.

```
crm configure location loc_sap_<SLX>_failover_to_ers rsc_sap_<SLX>_ASCS<00> rule 2000: runs_ers_<SLX> eq 1
```

## Activate cluster

Use `crm config show` and `crm config edit` commands to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources.

`crm maintenance off`

See the [Sample configuration](sample-configuration.md "sample-configuration.md").
