# Cluster Configuration

The following sections provide details on the resources, groups and constraints necessary to ensure high availability of SAP Central Services.

###### Topics

- [Prepare for Resource Creation](#prepare-resource-nw-sles "#prepare-resource-nw-sles")
- [Cluster Bootstrap](#cluster-bootstrap-nw-sles "#cluster-bootstrap-nw-sles")
- [Create STONITH (external/ec2) resource](#create-stonith-ec2-nw-sles "#create-stonith-ec2-nw-sles")
- [Create Filesystem resources (classic only)](#filesystem-resources-nw-sles "#filesystem-resources-nw-sles")
- [Create Overlay IP (aws-vpc-move-ip) resources](#overlay-ip-resources-nw-sles "#overlay-ip-resources-nw-sles")
- [Create SAPStartSrv resources (simple-mount only)](#sapstartsrv-resources-nw-sles "#sapstartsrv-resources-nw-sles")
- [Create SAPInstance resources (simple-mount only)](#sap-resources-simple-nw-sles "#sap-resources-simple-nw-sles")
- [Create SAPInstance resources (classic only)](#sap-resources-classic-nw-sles "#sap-resources-classic-nw-sles")
- [Create resource groups for aws-vpc-move-ip / SAPStartSrv / SAPInstance (simple-mount only)](#resource-groups-simple-nw-sles "#resource-groups-simple-nw-sles")
- [Create resource groups for Filesystem / aws-vpc-move-ip / SAPInstance (classic only)](#resource-groups-classic-nw-sles "#resource-groups-classic-nw-sles")
- [Create resource constraints](#resource-constraints-nw-sles "#resource-constraints-nw-sles")
- [Reset Configuration – Optional](#reset-config-nw-sles "#reset-config-nw-sles")

## Prepare for Resource Creation

To ensure that the cluster does not perform unexpected actions during setup of resources and configuration, set the maintenance mode to true.

Run the following command to put the cluster in maintenance mode:

```
# crm maintenance on
```

To verify the current maintenance state:

```
# crm status
```

###### Note

There are two types of maintenance mode:

- Cluster-wide maintenance (set with `crm maintenance on`)
- Node-specific maintenance (set with `crm node maintenance nodename`)
  Always use cluster-wide maintenance mode when making configuration changes. For node-specific operations like hardware maintenance, refer to the Operations for proper procedures.

To disable maintenance mode after configuration is complete:

```
# crm maintenance off
```

## Cluster Bootstrap

### Configure Cluster Properties

Configure cluster properties to establish fencing behavior and resource failover settings:

```
# crm configure property stonith-enabled="true"
# crm configure property stonith-timeout="600"
# crm configure property priority-fencing-delay="20"
```

- The **priority-fencing-delay** is recommended for protecting the SAP ASCS nodes during network partitioning events. When a cluster partition occurs, this delay gives preference to nodes hosting higher priority resources, with the ASCS receiving additional priority weighting over the ERS . This helps ensure the ASCS node survives in split-brain scenarios. The recommended 20 second priority-fencing-delay works in conjunction with the pcmk_delay_max (10 seconds) configured in the stonith resource, providing a total potential delay of up to 30 seconds before fencing occurs

To verify your cluster property settings:

```
# crm configure show property
```

### Configure Resource Defaults

Configure resource default behaviors:

```
# crm configure rsc_defaults resource-stickiness="1"
# crm configure rsc_defaults migration-threshold="3"
# crm configure rsc_defaults failure-timeout="600s"
```

- The **resource-stickiness** value of 1 encourages the ASCS resource to stay on its current node, avoiding unnecessary resource movement.
- The **migration-threshold** of causes a resource to move to a different node after 3 consecutive failures, ensuring timely failover when issues persist.
- The **failure-timeout** automatically removes a failure count after 10 minutes, preventing individual historical failures from accumulating and affecting long-term resource behavior. If testing failover scenarios in quick succession, it may be necessary to manually query and clear accumulated failure counts between tests. Use `crm resource failcount <resource_name> show <hostname>` and `crm resource refresh`.

Individual resources may override these defaults with their own defined values.

To verify your resource default settings:

```
# crm configure show rsc_defaults
```

### Configure Operation Defaults

Configure operation timeout defaults:

```
# crm configure op_defaults timeout="600"
```

- The **op_defaults timeout** ensures all cluster operations have a reasonable default timeout of 600 seconds. Individual resources may override this with their own timeout values.

To verify your operation default settings:

```
# crm configure show op_defaults
```

## Create STONITH (external/ec2) resource

Create the STONITH or Fencing resource using resource agent **`external/ec2`**:

```
# crm configure primitive <stonith_resource_name> stonith:external/ec2 \
params tag="<cluster_tag>" profile="<cli_cluster_profile>" pcmk_delay_max="<delay_value>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

Details:

- **tag** - EC2 instance tag key name that associates instances with this cluster configuration. This tag key must be unique within the AWS account and have a value which matches the instance hostname. See [Create Amazon EC2 Resource Tags Used by Amazon EC2 STONITH Agent](sap-nw-pacemaker-sles-ec2-configuration.md#create-cluster-tags-nw-sles "sap-nw-pacemaker-sles-ec2-configuration.md#create-cluster-tags-nw-sles") for EC2 instance tagging configuration.
- **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
- **pcmk_delay_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing. For ENSA1 use 30 seconds, for ENSA2 use 10 seconds (lower value sufficient as `priority-fencing-delay` handles primary node protection).

###### Example

ENSA1

_Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive res_stonith_ec2 stonith:external/ec2 \
params tag="pacemaker" profile="cluster" \
pcmk_delay_max="30" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

ENSA2

_Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive res_stonith_ec2 stonith:external/ec2 \
params tag="pacemaker" profile="cluster" \
pcmk_delay_max="10" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

## Create Filesystem resources (classic only)

In classic configuration, the mounting and unmounting of file system resources to align with the location of the SAP services is done using cluster resources.

Create **ASCS** file system resources:

```
# crm configure primitive rsc_fs_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:Filesystem \
params \
device="<nfs.fqdn>:/<SID>_ASCS<ascs_sys_nr>" \
directory="/usr/sap/<SID>/ASCS<ascs_sys_nr>" \
fstype="nfs4" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"
```

Create **ERS** file system resources:

```
# crm configure primitive rsc_fs_<SID>_ERS<ers_sys_nr> ocf:heartbeat:Filesystem \
params \
device="<nfs.fqdn>:/<SID>_ERS<ers_sys_nr>" \
directory="/usr/sap/<SID>/ERS<ers_sys_nr>" \
fstype="nfs4" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_fs_SLX_ASCS00 ocf:heartbeat:Filesystem \
params \
device="fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/SLX_ASCS00" \
directory="/usr/sap/SLX/ASCS00" \
fstype="nfs4" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"

# crm configure primitive rsc_fs_SLX_ERS10 ocf:heartbeat:Filesystem \
params \
device="fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/SLX_ERS10" \
directory="/usr/sap/SLX/ERS10" \
fstype="nfs4" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"
```

**Notes**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP.
- <nfs.fqdn> can either be an alias or the default file system resource name of the NFS or FSx for ONTAP resource. For example, `fs-xxxxxx.efs.xxxxxx.amazonaws.com`.

## Create Overlay IP (aws-vpc-move-ip) resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Create **ASCS** IP Resource:

```
# crm configure primitive rsc_ip_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
params \
ip="<ascs_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"
```

Create **ERS** IP Resource:

```
# crm configure primitive rsc_ip_<SID>_ERS<ers_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
params \
ip="<ers_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_ip_SLX_ASCS00 ocf:heartbeat:aws-vpc-move-ip \
params \
ip="172.16.30.5" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"

# crm configure primitive rsc_ip_SLX_ERS10 ocf:heartbeat:aws-vpc-move-ip \
params \
ip="172.16.30.6" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"
```

**Notes**

- If more than one route table is required for connectivity or because of subnet associations, the `routing_table` parameter can have multiple values separated by a comma. For example, `routing_table=rtb-xxxxxroutetable1,rtb-xxxxxroutetable2`.
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see {https---docs-aws-amazon-com-sap-latest-sap-netweaver-sles-netweaver-ha-settings-html-sles-netweaver-ha-shared-vpc}[Shared VPC – optional].

## Create SAPStartSrv resources (simple-mount only)

In simple-mount architecture, the `sapstartsrv` process that is used to control start/stop and monitoring of an SAP instance, is controlled by a cluster resource. This new resource adds additional control that removes the requirement for file system resources to be restricted to a single node.

Modify and run the commands in the table to create `sapstartsrv` resource.

Create **ASCS** SAPStartSrv Resource

Use the following command to create an ASCS SAPStartSrv resource.

```
# crm configure primitive rsc_sapstart_<SID>_ASCS<ascs_sys_nr> ocf:suse:SAPStartSrv \
params \
InstanceName=<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>
```

Create **ERS** SAPStartSrv Resource

Use the following command to create an ERS SAPStartSrv resource.

```
# crm configure primitive rsc_sapstart_<SID>_ERS<ers_sys_nr> ocf:suse:SAPStartSrv \
params  \
InstanceName=<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
#crm configure primitive rsc_sapstart_SLX_ASCS00 ocf:suse:SAPStartSrv \
params \
InstanceName=SLX_ASCS00_slxascs

#crm configure primitive rsc_sapstart_SLX_ERS10 ocf:suse:SAPStartSrv \
params \
InstanceName=SLX_ERS10_slxers
```

## Create SAPInstance resources (simple-mount only)

The minor difference in creating SAP instance resources between classic and simple-mount configurations is the addition of `MINIMAL_PROBE=true` parameters.

The SAP instance is started and stopped using cluster resources.

###### Example

ENSA1
Create an **ASCS** SAP instance resource:

```
# crm configure primitive rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
operations \$id="rsc_sap_<SID>_ASCS<ascs_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
failure-timeout="60" \
migration-threshold="1" \
priority="10"
```

Create an **ERS** SAP instance resource:

```
# crm configure primitive rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
operations \$id="rsc_sap_<SID>_ERS<ers_sys_nr>-operations" \
op start interval="0" timeout="240" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
priority="1000"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_sap_SLX_ASCS00 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ASCS00_slxascs" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
operations \$id="rsc_sap_SLX_ASCS00-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
failure-timeout="60" \
migration-threshold="1" \
priority="10"

# crm configure primitive rsc_sap_SLX_ERS10 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ERS10_slxers" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
operations \$id="rsc_sap_SLX_ERS10-operations" \
op start interval="0" timeout="240" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
priority="1000"
```

ENSA2
Create an **ASCS** SAP instance resource:

```
# crm configure primitive rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
operations \$id="rsc_sap_<SID>_ASCS<ascs_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
priority="1000"
```

Create an **ERS** SAP instance resource:

```
# crm configure primitive rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
operations \$id="rsc_sap_<SID>_ERS<ers_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_sap_SLX_ASCS00 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ASCS00_slxascs" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
operations \$id="rsc_sap_SLX_ASCS00-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
priority="1000"

# crm configure primitive rsc_sap_SLX_ERS10 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ERS10_slxers" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
operations \$id="rsc_sap_SLX_ERS10-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart"
```

The difference between ENSA1 and ENSA2 is that ENSA2 allows the lock table to be consumed remotely, which means that for ENSA2, ASCS can restart in its current location (assuming the node is still available). This change impacts stickiness, migration and priority parameters. Ensure that you use the right command for your enqueue version.

## Create SAPInstance resources (classic only)

The SAP instance is started and stopped using cluster resources.

###### Example

ENSA1
Create an **ASCS** SAPInstance resource:

```
# crm configure primitive rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
operations \$id="rsc_sap_<SID>_ASCS<ascs_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
failure-timeout="60" \
migration-threshold="1" \
priority="10"
```

Create an **ERS** SAPInstance resource:

```
# crm configure primitive rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
operations \$id="rsc_sap_<SID>_ERS<ers_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
priority="1000"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_sap_SLX_ASCS00 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ASCS00_slxascs" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs" \
AUTOMATIC_RECOVER="false" \
operations \$id="rsc_sap_SLX_ASCS00-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
failure-timeout="60" \
migration-threshold="1" \
priority="10"

# crm configure primitive rsc_sap_SLX_ERS10 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ERS10_slxers" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
operations \$id="rsc_sap_SLX_ERS10-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
priority="1000"
```

ENSA2
Create an **ASCS** SAPInstance resource:

```
# crm configure primitive rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
operations \$id="rsc_sap_<SID>_ASCS<ascs_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
priority="1000"
```

Create an **ERS** SAPInstance resource:

```
# crm configure primitive rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
params \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
operations \$id="rsc_sap_<SID>_ERS<ers_sys_nr>-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure primitive rsc_sap_SLX_ASCS00 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ASCS00_slxascs" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs" \
AUTOMATIC_RECOVER="false" \
operations \$id="rsc_sap_SLX_ASCS00-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
resource-stickiness="5000" \
priority="1000"

# crm configure primitive rsc_sap_SLX_ERS10 ocf:heartbeat:SAPInstance \
params \
InstanceName="SLX_ERS10_slxers" \
START_PROFILE="/usr/sap/SLX/SYS/profile/SLX_ERS10_slxers" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
operations \$id="rsc_sap_SLX_ERS10-operations" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart"
```

The change between ENSA1 and ENSA2 allows the lock table to be consumed remotely. If the node is still available, ASCS can restart in its current location for ENSA2. This impacts stickiness, migration, and priority parameters. Make sure to use the right command, depending on your enqueue server.

## Create resource groups for aws-vpc-move-ip / SAPStartSrv / SAPInstance (simple-mount only)

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

In simple-mount architecture, the overlay IP must be available first, then the SAP start services are started before the SAP instance can start. The order of the group must be as defined here.

Create an **ASCS** cluster resource group:

```
# crm configure group grp_<SID>_ASCS<ascs_sys_nr> \
rsc_ip_<SID>_ASCS<ascs_sys_nr> \
rsc_sapstart_<SID>_ASCS<ascs_sys_nr> \
rsc_sap_<SID>_ASCS<ascs_sys_nr> \
meta resource-stickiness="3000"
```

Create an **ERS** cluster resource group:

```
# crm configure group grp_<SID>_ERS<ers_sys_nr> \
rsc_ip_<SID>_ERS<ers_sys_nr> \
rsc_sapstart_<SID>_ERS<ers_sys_nr> \
rsc_sap_<SID>_ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure group grp_SLX_ASCS00 \
rsc_ip_SLX_ASCS00 \
rsc_sapstart_SLX_ASCS00 \
rsc_sap_SLX_ASCS00 \
meta resource-stickiness="3000"

# crm configure group grp_SLX_ERS10 \
rsc_ip_SLX_ERS10 \
rsc_sapstart_SLX_ERS10 \
rsc_sap_SLX_ERS10
```

## Create resource groups for Filesystem / aws-vpc-move-ip / SAPInstance (classic only)

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

In classic architecture, the file system is mounted first, then the overlay IP must be available before the SAP instance can start.

Create an **ASCS** cluster resource group:

```
# crm configure group grp_<SID>_ASCS<ascs_sys_nr> \
rsc_fs_<SID>_ASCS<ascs_sys_nr> \
rsc_ip_<SID>_ASCS<ascs_sys_nr> \
rsc_sap_<SID>_ASCS<ascs_sys_nr> \
meta resource-stickiness="3000"
```

Create an **ERS** cluster resource group:

```
# crm configure group grp_<SID>_ERS<ers_sys_nr> \
rsc_fs_<SID>_ERS<ers_sys_nr> \
rsc_ip_<SID>_ERS<ers_sys_nr> \
rsc_sap_<SID>_ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure group grp_SLX_ASCS00 \
rsc_fs_SLX_ASCS00 \
rsc_ip_SLX_ASCS00 \
rsc_sap_SLX_ASCS00 \
meta resource-stickiness="3000"

# crm configure group grp_SLX_ERS10 \
rsc_fs_SLX_ERS10 \
rsc_ip_SLX_ERS10 \
rsc_sap_SLX_ERS10
```

## Create resource constraints

Resource constraints are used to determine where resources run per the conditions. Constraints for SAP NetWeaver ensure that ASCS and ERS are started on separate nodes and locks are preserved in case of failures. The following are the different types of constraints.

### Colocation constraint

The negative score ensures that ASCS and ERS are run on separate nodes, wherever possible.

```
# crm configure colocation col_sap_<SID>_ascs_ers_separate_nodes \
-5000: grp_<SID>_ERS<ers_sys_nr> grp_<SID>_ASCS<ascs_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure colocation col_sap_SLX_ascs_ers_separate_nodes \
-5000: grp_SLX_ERS10 grp_SLX_ASCS00
```

### Order constraint

This constraint ensures the ASCS instance is started prior to stopping the ERS instance. This is necessary to consume the lock table.

```
# crm configure order ord_sap_<SID>_ascs_start_before_ers_stop \
Optional: rsc_sap_<SID>_ASCS<ascs_sys_nr>:start rsc_sap_<SID>_ERS<ers_sys_nr>:stop \
symmetrical="false"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure order ord_sap_SLX_ascs_start_before_ers_stop \
Optional: rsc_sap_SLX_ASCS00:start rsc_sap_SLX_ERS10:stop \
symmetrical="false"
```

### Location constraint (ENSA1 only)

This constraint is only required for ENSA1. The lock table can be retrieved remotely for ENSA2, and as a result ASCS doesn’t failover to where ERS is running.

```
# crm configure location loc_sap_<SID>_ascs_follows_ers \
rsc_sap_<SID>_ASCS<ascs_sys_nr> rule 2000: runs_ers_<SID> eq 1
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-sles-parameters.md "sap-nw-pacemaker-sles-parameters.md")_:

```
# crm configure location loc_sap_SLX_ascs_follows_ers \
rsc_sap_SLX_ASCS00 rule 2000: runs_ers_SLX eq 1
```

## Reset Configuration – Optional

###### Important

The following instructions help you reset the complete configuration. Run these commands only if you want to start setup from the beginning. You can make minor changes with the crm edit command.

Run the following command to back up the current configuration for reference:

```
# crm config show > /tmp/crmconfig_backup.txt
```

Run the following command to clear the current configuration:

```
# crm configure erase
```

Once the preceding erase command is executed, it removes all of the cluster resources from Cluster Information Base (CIB), and disconnects the communication from corosync to the cluster. Before starting the resource configuration run crm cluster restart, so that cluster reestablishes communication with corosync, and retrieves the configuration. The restart of cluster removes maintenance mode. Reapply before commencing additional configuration and resource setup.
