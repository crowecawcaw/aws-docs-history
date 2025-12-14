# Cluster Configuration

The following sections provide details on the resources, groups and constraints necessary to ensure high availability of SAP Central Services.

###### Topics

- [Prepare for Resource Creation](#prepare-resource-nw-rhel "#prepare-resource-nw-rhel")
- [Cluster Bootstrap](#cluster-bootstrap-nw-rhel "#cluster-bootstrap-nw-rhel")
- [Create STONITH Fencing Resource](#create-stonith-ec2-nw-rhel "#create-stonith-ec2-nw-rhel")
- [SAP Resource Groups and Ordering](#resource-groups-nw-rhel "#resource-groups-nw-rhel")
- [Create Filesystem resources (classic only)](#filesystem-resources-nw-rhel "#filesystem-resources-nw-rhel")
- [Create overlay IP resources](#overlay-ip-resources-nw-rhel "#overlay-ip-resources-nw-rhel")
- [Create SAPStartSrv resources (simple-mount only)](#sapstartsrv-resources-nw-rhel "#sapstartsrv-resources-nw-rhel")
- [Create SAPInstance resources (simple-mount only)](#sap-resources-simple-nw-rhel "#sap-resources-simple-nw-rhel")
- [Create SAPInstance resources (classic only)](#sap-resources-classic-nw-rhel "#sap-resources-classic-nw-rhel")
- [Review ASCS Resource group and modify stickiness.](#resource-groups-review-nw-rhel "#resource-groups-review-nw-rhel")
- [Create resource constraints](#resource-constraints-nw-rhel "#resource-constraints-nw-rhel")
- [Reset Configuration – Optional](#reset-config-nw-rhel "#reset-config-nw-rhel")

## Prepare for Resource Creation

To ensure that the cluster does not perform any unexpected actions during setup of resources and configuration, set the maintenance mode to true.

Run the following command to put the cluster in maintenance mode:

```
# pcs property set maintenance-mode=true
```

To verify the current maintenance state:

```
$ pcs status
```

###### Note

There are two types of maintenance mode:

- Cluster-wide maintenance (set with `pcs property set maintenance-mode=true`)
- Node-specific maintenance (set with `pcs node maintenance nodename`)
  Always use cluster-wide maintenance mode when making configuration changes. For node-specific operations like hardware maintenance, refer to the Operations section for proper procedures.

To disable maintenance mode after configuration is complete:

```
# pcs property set maintenance-mode=false
```

## Cluster Bootstrap

### Configure Cluster Properties

Configure cluster properties to establish fencing behavior and resource failover settings:

```
# pcs property set stonith-enabled="true"
# pcs property set stonith-timeout="600"
# pcs property set priority-fencing-delay="20"
```

- The **priority-fencing-delay** is recommended for protecting the SAP ASCS nodes during network partitioning events. When a cluster partition occurs, this delay gives preference to nodes hosting higher priority resources, with the ASCS receiving additional priority weighting over the ERS . This helps ensure the ASCS node survives in split-brain scenarios. The recommended 20 second priority-fencing-delay works in conjunction with the pcmk_delay_max (10 seconds) configured in the stonith resource, providing a total potential delay of up to 30 seconds before fencing occurs

To verify your cluster property settings:

```
# pcs property config
# pcs property config <property_name>
```

### Configure Resource Defaults

Configure resource default behaviors:

RHEL 8.4 and above

```
# pcs resource defaults update resource-stickiness="1"
# pcs resource defaults update migration-threshold="3"
# pcs resource defaults update failure-timeout="600s"
```

RHEL 7.x and RHEL 8.0 to 8.3

```
# pcs resource defaults resource-stickiness="1"
# pcs resource defaults migration-threshold="3"
# pcs resource defaults failure-timeout="600s"
```

- The **resource-stickiness** value of 1 encourages the ASCS resource to stay on its current node, avoiding unnecessary resource movement.
- The **migration-threshold** causes a resource to move to a different node after 3 consecutive failures, ensuring timely failover when issues persist.
- The **failure-timeout** automatically removes a failure count after 10 minutes, preventing individual historical failures from accumulating and affecting long-term resource behavior. If testing failover scenarios in quick succession, it may be necessary to manually query and clear accumulated failure counts between tests. Use `pcs resource failcount` and `pcs resource refresh`.

Individual resources may override these defaults with their own defined values.

To verify your resource default settings:

```
# pcs resource defaults
```

### Configure Operation Defaults

```
# pcs resource op defaults update timeout="600"
```

- The **op_defaults timeout** ensures all cluster operations have a reasonable default timeout of 600 seconds. Individual resources may override this with their own timeout values.

To verify your operation default settings:

```
# pcs resource op defaults
```

## Create STONITH Fencing Resource

An AWS STONITH resource is required for proper cluster fencing operations. The `fence_aws` resource is recommended for AWS deployments as it leverages the AWS API to safely fence failed or incommunicable nodes by stopping their EC2 instances.

Create the STONITH resource using resource agent **`fence_aws`**:

```
# pcs stonith create <stonith_resource_name> fence_aws \
pcmk_host_map="<hostname_1>:<instance_id_1>;<hostname_2>:<instance_id_2>" \
region="<aws_region>" \
skip_os_shutdown="true" \
pcmk_delay_max="10" \
pcmk_reboot_timeout="300" \
pcmk_reboot_retries="2" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="180" timeout="60"
```

Details:

- **pcmk_host_map** - Maps cluster node hostnames to their EC2 instance IDs. This mapping must be unique within the AWS account and follow the format hostname:instance-id, with multiple entries separated by semicolons.
- **region** - AWS region where the EC2 instances are deployed
- **pcmk_delay_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing. Historically set to higher values, but with `priority-fencing-delay` now handling primary node protection, a lower value (10s) is sufficient.
- **pcmk_reboot_timeout** - Maximum time in seconds allowed for a reboot operation
- **pcmk_reboot_retries** - Number of times to retry a failed reboot operation
- **skip_os_shutdown** (NEW) - Leverages a new ec2 stop-instance API flag to forcefully stop an EC2 Instance by skipping the shutdown of the Operating System.
  - [Red Hat Solution 4963741 - fence_aws fence action fails with "Timed out waiting to power OFF"](https://access.redhat.com/solutions/4963741 "https://access.redhat.com/solutions/4963741") (requires Red Hat Customer Portal access)

ENSA1

_Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs stonith create rsc_fence_aws fence_aws \
pcmk_host_map="rhxhost01:i-xxxxinstidforhost1;rhxhost02:i-xxxxinstidforhost2" \
region="us-east-1" \
skip_os_shutdown="true" \
pcmk_delay_max="30" \
pcmk_reboot_timeout="120" \
pcmk_reboot_retries="4" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="180" timeout="60"
```

ENSA2

_Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs stonith create rsc_fence_aws fence_aws \
pcmk_host_map="rhxhost01:i-xxxxinstidforhost1;rhxhost02:i-xxxxinstidforhost2" \
region="us-east-1" \
skip_os_shutdown="true" \
pcmk_delay_max="10" \
pcmk_reboot_timeout="120" \
pcmk_reboot_retries="4" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="180" timeout="60"
```

## SAP Resource Groups and Ordering

When creating the resources for the SAP ASCS and ERS, it is necessary to specify a group.

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

Depending on the configuration pattern the following groups will be created for the ASCS and ERS

- **Classic**: Filesystem, IP, SAPInstance
- **SimpleMount**: IP, SAPStartSrv, SAPInstance

Since RHEL 9.4 a new syntax for creating a resource in a group has been introduced in addition to the --group parameter. You receive the following deprecation warning now:

```
Deprecation Warning: Using '--group' is deprecated and will be replaced with 'group' in a future release. Specify --future to switch to the future behavior.
```

## Create Filesystem resources (classic only)

In classic configuration, the mounting and unmounting of file system resources to align with the location of the SAP services is done using cluster resources.

Create **ASCS** file system resources:

```
# pcs resource create rsc_fs_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:Filesystem \
device="<nfs.fqdn>:/<SID>_ASCS<ascs_sys_nr>" \
directory="/usr/sap/<SID>/ASCS<ascs_sys_nr>" \
fstype="nfs4" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
force_unmount="safe" \
fast_stop="no" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40" \
--group "grp_<SID>_ASCS<ascs_sys_nr>"
```

Create **ERS** file system resources:

```
# pcs resource create rsc_fs_<SID>_ERS<ers_sys_nr> ocf:heartbeat:Filesystem \
device="<nfs.fqdn>:/<SID>_ERS<ers_sys_nr>" \
directory="/usr/sap/<SID>/ERS<ers_sys_nr>" \
fstype="nfs4" \
force_unmount="safe" \
fast_stop="no" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40" \
--group "grp_<SID>_ERS<ers_sys_nr>"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_fs_RHX_ASCS00 ocf:heartbeat:Filesystem \
device="fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ASCS00" \
directory="/usr/sap/RHX/ASCS00" \
fstype="nfs4" \
force_unmount="safe" \
fast_stop="no" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"

# pcs resource create rsc_fs_RHX_ERS10 ocf:heartbeat:Filesystem \
device="fs-xxxxxxxxxxxxxefs1.efs.us-east-1.amazonaws.com:/RHX_ERS10" \
directory="/usr/sap/RHX/ERS10" \
fstype="nfs4" \
force_unmount="safe" \
fast_stop="no" \
options="rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2" \
op start timeout="60" interval="0" \
op stop timeout="60" interval="0" \
op monitor interval="20" timeout="40"
```

**Notes**

- Review the mount options to ensure that they match with your operating system, NFS file system type, and the latest recommendations from SAP.
- <nfs.fqdn> can either be an alias or the default file system resource name of the NFS or FSx for ONTAP resource. For example, `fs-xxxxxx.efs.xxxxxx.amazonaws.com`.
- `force_unmount` and `fast_stop` are recommendations for ensuring the filesystem can be quickly unmounted. See Red Hat solutions:
  - [Red Hat Solution 3357961 - During failover of a pacemaker resources, a Filesystem resource kills processes not using the filesystem](https://access.redhat.com/solutions/3357961 "https://access.redhat.com/solutions/3357961") (requires Red Hat customer portal login)
  - [Red Hat Solution 4801371 - What is the fast_stop option for a Filesystem resource in a Pacemaker cluster?](https://access.redhat.com/solutions/4801371 "https://access.redhat.com/solutions/4801371") (requires Red Hat customer portal login)

## Create overlay IP resources

The IP resource provides the details necessary to update the route table entry for overlay IP.

Create **ASCS** IP Resource:

```
# pcs resource create rsc_ip_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
ip="<ascs_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"
--group "grp_<SID>_ASCS<ascs_sys_nr>"
```

Create **ERS** IP Resource:

```
# pcs resource create rsc_ip_<SID>_ERS<ers_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
ip="<ers_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40" \
--group "grp_<SID>_ERS<ers_sys_nr>"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_ip_RHX_ASCS00 ocf:heartbeat:aws-vpc-move-ip \
ip="172.16.30.5" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40" \
--group grp_RHX_ASCS00

# pcs resource create rsc_ip_RHX_ERS10 ocf:heartbeat:aws-vpc-move-ip \
ip="172.16.30.6" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_ip_RHX_ASCS00 ocf:heartbeat:aws-vpc-move-ip \
ip="172.16.30.5" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="20" timeout="40" \
--group grp_RHX_ASCS00

# pcs resource create rsc_ip_RHX_ERS10 ocf:heartbeat:aws-vpc-move-ip \
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
- Additional parameters – `lookup_type` and `routing_table_role` are required for shared VPC. For more information, see {https---docs-aws-amazon-com-sap-latest-sap-netweaver-rhel-netweaver-ha-settings-html-rhel-netweaver-ha-shared-vpc}[Shared VPC – optional].

## Create SAPStartSrv resources (simple-mount only)

In simple-mount architecture, the `sapstartsrv` process that is used to control start/stop and monitoring of an SAP instance, is controlled by a cluster resource. This new resource adds additional control that removes the requirement for file system resources to be restricted to a single node.

Modify and run the commands in the table to create `sapstartsrv` resource.

Create **ASCS** SAPStartSrv Resource

Use the following command to create an ASCS SAPStartSrv resource.

```
# pcs resource create rsc_sapstart_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPStartSrv \
InstanceName=<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>
op monitor interval=0 timeout=20 enabled=0
--group grp_<SID>_ASCS<instance>
```

Create **ERS** SAPStartSrv Resource

Use the following command to create an ERS SAPStartSrv resource.

```
# pcs resource create rsc_sapstart_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPStartSrv \
InstanceName=<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>
op monitor interval=0 timeout=20 enabled=0
--group grp_<SID>_ERS<ers_sys_nr>
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
#crm configure primitive rsc_sapstart_RHX_ASCS00 ocf:heartbeat:SAPStartSrv \
params \
InstanceName=RHX_ASCS00_rhxascs \
op monitor interval=0 timeout=20 enabled=0 \
--group grp_RHX_ASCS00

#crm configure primitive rsc_sapstart_RHX_ERS10 ocf:heartbeat:SAPStartSrv \
params \
InstanceName=RHX_ERS10_rhxers \
op monitor interval=0 timeout=20 enabled=0 \
--group grp_RHX_ERS10
```

## Create SAPInstance resources (simple-mount only)

The minor difference in creating SAP instance resources between classic and simple-mount configurations is the addition of `MINIMAL_PROBE=true` parameters.

The SAP instance is started and stopped using cluster resources.

ENSA1
Create an **ASCS** SAP instance resource:

```
# pcs resource create rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta failure-timeout="60" \
meta migration-threshold="1" \
meta priority="10"
```

Create an **ERS** SAP instance resource:

```
# pcs resource create rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
op start interval="0" timeout="240" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta priority="1000"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_sap_RHX_ASCS00 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ASCS00_rhxascs" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta failure-timeout="60" \
meta migration-threshold="1" \
meta priority="10"

# pcs resource create rsc_sap_RHX_ERS10 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ERS10_rhxers" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
IS_ERS="true" \
op start interval="0" timeout="240" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta priority="1000"
```

ENSA2
Create an **ASCS** SAP instance resource:

```
# pcs resource create rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="20" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta priority="1000"
```

Create an **ERS** SAP instance resource:

```
# pcs resource create rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="20" timeout="60" on-fail="restart"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_sap_RHX_ASCS00 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ASCS00_rhxascs" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs" \
AUTOMATIC_RECOVER="false" \
MINIMAL_PROBE="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="20" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta priority="1000"

# pcs resource create rsc_sap_RHX_ERS10 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ERS10_rhxers" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="20" timeout="60" on-fail="restart"
```

The difference between ENSA1 and ENSA2 is that ENSA2 allows the lock table to be consumed remotely, which means that for ENSA2, ASCS can restart in its current location (assuming the node is still available). This change impacts stickiness, migration and priority parameters. Ensure that you use the right command for your enqueue version.

## Create SAPInstance resources (classic only)

The SAP instance is started and stopped using cluster resources.

ENSA1
Create an **ASCS** SAPInstance resource:

```
# pcs resource create rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta failure-timeout="60" \
meta migration-threshold="1" \
meta priority="10" \
--group "grp_<SID>_ASCS<ascs_sys_nr>"
```

Create an **ERS** SAPInstance resource:

```
# pcs resource create rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta \
priority="1000"
--group "grp_<SID>_ERS<ers_sys_nr>"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_sap_RHX_ASCS00 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ASCS00_rhxascs" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs" \
AUTOMATIC_RECOVER="false" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta failure-timeout="60" \
meta migration-threshold="1" \
meta priority="10"

# pcs resource create rsc_sap_RHX_ERS10 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ERS10_rhxers" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta priority="1000"
```

ENSA2
Create an **ASCS** SAPInstance resource:

```
# pcs resource create rsc_sap_<SID>_ASCS<ascs_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ASCS<ascs_sys_nr>_<ascs_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta priority="1000" \
--group "grp_<SID>_ASCS<ascs_sys_nr>"
```

Create an **ERS** SAP instance resource:

```
# pcs resource create rsc_sap_<SID>_ERS<ers_sys_nr> ocf:heartbeat:SAPInstance \
InstanceName="<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
START_PROFILE="/usr/sap/<SID>/SYS/profile/<SID>_ERS<ers_sys_nr>_<ers_virt_hostname>" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
--group "grp_<SID>_ERS<ers_sys_nr>"
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs resource create rsc_sap_RHX_ASCS00 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ASCS00_rhxascs" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs" \
AUTOMATIC_RECOVER="false" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart" \
meta resource-stickiness="5000" \
meta priority="1000"

# pcs resource create rsc_sap_RHX_ERS10 ocf:heartbeat:SAPInstance \
InstanceName="RHX_ERS10_rhxers" \
START_PROFILE="/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers" \
AUTOMATIC_RECOVER="false" \
IS_ERS="true" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="240" \
op monitor interval="11" timeout="60" on-fail="restart"
```

The change between ENSA1 and ENSA2 allows the lock table to be consumed remotely. If the node is still available, ASCS can restart in its current location for ENSA2. This impacts stickiness, migration, and priority parameters. Make sure to use the right command, depending on your enqueue server.

## Review ASCS Resource group and modify stickiness.

A cluster resource group is a set of resources that need to be located together, start sequentially, and stopped in the reverse order.

```
# pcs resource meta grp_<SID>_ASCS<ascs_sys_nr> resource-stickiness=3000
```

In simple-mount architecture, the overlay IP must be available first, then the SAP services are started before the SAP instance can start.

## Create resource constraints

Resource constraints are used to determine where resources run per the conditions. Constraints for SAP NetWeaver ensure that ASCS and ERS are started on separate nodes and locks are preserved in case of failures. The following are the different types of constraints.

### Colocation constraint

The negative score ensures that ASCS and ERS are run on separate nodes, wherever possible.

```
# pcs constraint colocation add grp_<SID>_ERS<ers_sys_nr> with grp_<SID>_ASCS<ascs_sys_nr> score=-5000
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs constraint colocation add grp_RHX_ERS10 with grp_RHX_ASCS00 score=-5000
```

### Order constraint

This constraint ensures the ASCS instance is started prior to stopping the ERS instance. This is necessary to consume the lock table.

```
# pcs constraint order start rsc_sap_<SID>_ASCS<ascs_sys_nr> then stop rsc_sap_<SID>_ERS<ers_sys_nr> kind=Optional symmetrical=false
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs constraint order start rsc_sap_RHX_ASCS00 then stop rsc_sap_RHX_ERS10 kind=Optional symmetrical=false
```

### Location constraint (ENSA1 only)

This constraint is only required for ENSA1. The lock table can be retrieved remotely for ENSA2, and as a result ASCS doesn’t failover to where ERS is running.

```
# pcs constraint location rsc_sap_<SID>_ASCS<ascs_sys_nr> rule score=2000 runs_ers_<SID> eq 1
```

- _Example using values from [Parameter Reference](sap-nw-pacemaker-rhel-parameters.md "sap-nw-pacemaker-rhel-parameters.md")_:

```
# pcs constraint location rsc_sap_RHX_ASCS00 rule score=2000 runs_ers_RHX eq 1
```

## Reset Configuration – Optional

###### Important

The following instructions help you reset the complete configuration. Run these commands only if you want to start setup from the beginning. You can make minor changes with the crm edit command.

Run the following command to back up the current configuration for reference:

```
# pcs config > /tmp/pcsconfig_backup.txt
```

Run the following command to clear the current configuration:

```
# pcs cluster cib-push --config /dev/null
```

Once the preceding command is executed, it removes all of the cluster resources from Cluster Information Base (CIB). Before starting the resource configuration, run pcs cluster start --all to ensure the cluster is running properly. The restart removes maintenance mode. Reapply maintenance mode before commencing additional configuration and resource setup.
