# Cluster Configuration

Bootstrap the cluster and configure all required cluster resources and constraints.

###### Topics

- [Prepare for Resource Creation](#_prepare_for_resource_creation "#_prepare_for_resource_creation")
- [Cluster Bootstrap](#cluster-bootstrap "#cluster-bootstrap")
- [Create STONITH Fencing Resource](#resource-stonith "#resource-stonith")
- [Create Overlay IP Resources](#resource-overlayip "#resource-overlayip")
- [Create SAPHanaTopology Resource](#resource-saphanatop "#resource-saphanatop")
- [Create SAPHANA Resource (based on resource agent SAPHana or SAPHanaController)](#resource-saphana "#resource-saphana")
- [Create Resource Constraints](#resource-constraints "#resource-constraints")
- [Reset Configuration – Optional](#_reset_configuration_optional "#_reset_configuration_optional")

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

- The **priority-fencing-delay** is recommended for protecting SAP HANA nodes during network partitioning events. When a cluster partition occurs, this delay gives preference to nodes hosting higher priority resources, with SAP HANA Primary (promoted) instances receiving additional priority weighting. This helps ensure the Primary HANA node survives in split-brain scenarios. The recommended 20 second priority-fencing-delay works in conjunction with the pcmk_delay_max (10 seconds) configured in the stonith resource, providing a total potential delay of up to 30 seconds before fencing occurs.

To verify your cluster property settings:

```
# pcs property list
# pcs property config <property_name>
```

### Configure Resource Defaults

Configure resource default behaviors:

RHEL 8.4 and above

```
# pcs resource defaults update resource-stickiness="1000"
# pcs resource defaults update migration-threshold="5000"
```

RHEL 7.x and RHEL 8.0 to 8.3

```
# pcs resource defaults resource-stickiness="1000"
# pcs resource defaults migration-threshold="5000"
```

- The **resource-stickiness** value prevents unnecessary resource movement, effectively setting a "cost" for moving resources. A value of 1000 strongly encourages resources to remain on their current node, avoiding the downtime associated with movement.
- The **migration-threshold** of 5000 ensures the cluster will attempt to recover a resource on the same node many times before declaring that node unsuitable for hosting the resource.

Individual resources may override these defaults with their own defined values.

To verify your resource default settings:

### Configure Operation Defaults

```
# pcs resource op defaults update timeout="600"
```

The op_defaults timeout ensures all cluster operations have a reasonable default timeout of 600 seconds when resource-specific timeouts are not defined. Defaults do not apply to resources which override them with their own defined values

## Create STONITH Fencing Resource

An AWS STONITH resource is required for proper cluster fencing operations. The `fence_aws` resource is recommended for AWS deployments as it leverages the AWS API to safely fence failed or incommunicable nodes by stopping their EC2 instances.

Create the STONITH resource using resource agent **`fence_aws`**:

```
# pcs stonith create <stonith_resource_name> fence_aws \
pcmk_host_map="<hostname_1>:<instance_id_1>;<hostname_2>:<instance_id_2>" \
region="<aws_region>" \
skip_os_shutdown="true" \
pcmk_delay_max="10" \
pcmk_reboot_timeout="600" \
pcmk_reboot_retries="4" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

Details:

- **pcmk_host_map** - Maps cluster node hostnames to their EC2 instance IDs. This mapping must be unique within the AWS account and follow the format hostname:instance-id, with multiple entries separated by semicolons.
- **region** - AWS region where the EC2 instances are deployed
- **pcmk_delay_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing. Historically set to higher values, but with `priority-fencing-delay` now handling primary node protection, a lower value (10s) is sufficient.
- **pcmk_reboot_timeout** - Maximum time in seconds allowed for a reboot operation
- **pcmk_reboot_retries** - Number of times to retry a failed reboot operation
- **skip_os_shutdown** (NEW) - Leverages a new ec2 stop-instance API flag to forcefully stop an EC2 Instance by skipping the shutdown of the Operating System.
  - [Red Hat Solution 4963741 - fence_aws fence action fails with "Timed out waiting to power OFF"](https://access.redhat.com/solutions/4963741 "https://access.redhat.com/solutions/4963741") (requires Red Hat Customer Portal access)

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs stonith create rsc_fence_aws fence_aws \
pcmk_host_map="hanahost01:i-xxxxinstidforhost1;hanahost02:i-xxxxinstidforhost2" \
region="us-east-1" \
skip_os_shutdown="true" \
pcmk_delay_max="10" \
pcmk_reboot_timeout="600" \
pcmk_reboot_retries="4" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

###### Note

When configuring the STONITH resource, consider your instance’s startup and shutdown times. The default pcmk_reboot_action is 'reboot', where the cluster waits for both stop and start actions to complete before considering the fencing action successful. This allows the cluster to return to a protected state. Setting `pcmk_reboot_action=off` allows the cluster to proceed immediately after shutdown. For High Memory Metal instances, only 'off' is recommended due to the extended time to initialize memory during startup.

```
# pcs resource update <stonith_resource_name> pcmk_reboot_action="off"
# pcs resource update <stonith_resource_name> pcmk_off_timeout="600"
# pcs resource update <stonith_resource_name> pcmk_off_retries="4"
```

## Create Overlay IP Resources

This resource ensures client connections follow the SAP HANA primary instance during failover by updating AWS route table entries. It manages an overlay IP address that always points to the active SAP HANA database

Create the IP resource:

```
# pcs resource create rsc_ip_<SID>_HDB<hana_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
ip="<hana_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

Details:

- **ip** - Overlay IP address that will be used to connect to the Primary SAP HANA database. See [Overlay IP Concept](sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel "sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel")
- **routing_table** - AWS route table ID(s) that need to be updated. Multiple route tables can be specified using commas (For example, `routing_table=rtb-xxxxxroutetable1,rtb-xxxxxroutetable2`). Ensure initial entries have been created following [Add VPC Route Table Entries for Overlay IPs](sap-hana-pacemaker-rhel-infra-setup.md#rt-rhel "sap-hana-pacemaker-rhel-infra-setup.md#rt-rhel")
- **interface** - Network interface for the IP address (typically eth0)
- **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_ip_HDB_HDB00 ocf:heartbeat:aws-vpc-move-ip \
ip="172.16.52.1" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

###### For Active/Active Read Enabled

Only if you are using `logreplay_readenabled` and require that your secondary is accessible via overlay IP. You can create an additional IP resource.

```
# pcs resource create primitive rsc_ip_<SID>_HDB<hana_sys_nr>_readenabled ocf:heartbeat:aws-vpc-move-ip \
ip="<readenabled_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# crm configure primitive rsc_ip_HDB_HDB00_readenabled ocf:heartbeat:aws-vpc-move-ip \
params ip="172.16.52.2" \
routing_table="rtb-xxxxxroutetable1" \
interface="eth0" \
profile="cluster" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

###### For Shared VPC

If your configuration requires a shared vpc, two additional parameters are required.

```
# pcs resource create primitive rsc_ip_<SID>_HDB<hana_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
ip="<hana_overlayip>" routing_table=<routetable_id> interface=eth0 \
profile="<cli_cluster_profile>" lookup_type=NetworkInterfaceId \
routing_table_role="arn:aws:iam::<sharing_vpc_account_id>:role/<sharing_vpc_account_cluster_role>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

Additional details:

- lookup_type=NetworkInterfaceId
- routing_table_role="arn:aws:iam::<shared_vpc_account_id>:role/<sharing_vpc_account_cluster_role>"

## Create SAPHanaTopology Resource

The SAPHanaTopology resource agent helps manage high availability for SAP HANA databases with system replication. It analyzes the HANA topology and reports findings via node status attributes. These attributes are used by either the SAPHana or SAPHanaController resource agents to control the HANA databases. SAPHanaTopology starts and monitors the local saphostagent, leveraging SAP interfaces like landscapeHostConfiguration.py, hdbnsutil, and saphostctrl to gather information about system status, roles, and configuration.

For both scale-up and scale-out deployments

For documentation on the resource you can review the man page.

```
# man ocf_heartbeat_SAPHanaTopology
```

For scale-up (2-node)
For the primitive and clone:

```
# pcs resource create rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaTopology \
SID="<SID>" InstanceNumber="<hana_sys_nr>" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600" \
clone clone-node-max="1" interleave="true" clone-max="2"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHanaTopology_HDB_HDB00 ocf:heartbeat:SAPHanaTopology \
SID="HDB" \
InstanceNumber="00" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600" \
clone clone-node-max="1" interleave="true" clone-max="2"
```

For scale-out
For the primitive and clone:

```
# pcs resource create rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaTopology \
SID="<SID>" InstanceNumber="<hana_sys_nr>" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600" \
clone clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHanaTopology_HDB_HDB00 ocf:heartbeat:SAPHanaTopology \
SID="HDB" InstanceNumber="00" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600" \
clone clone-node-max="1" interleave="true" clone-max="6"
```

Details:

- **SID** - SAP System ID for the HANA instance
- **InstanceNumber** - Instance number of the SAP HANA instance
- **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
- **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
- **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)

## Create SAPHANA Resource (based on resource agent SAPHana or SAPHanaController)

The SAP HANA resource agents manage system replication and failover between SAP HANA databases. These agents control start, stop, and monitoring operations while checking synchronization status to maintain data consistency. They leverage SAP interfaces including sapcontrol, landscapeHostConfiguration, hdbnsutil, systemReplicationStatus, and saphostctrl. All configurations work in conjunction with the SAPHanaTopology agent, which gathers information about the system replication status across cluster nodes.

Choose the appropriate resource agent configuration based on your SAP HANA architecture:

### SAPHanaSR-angi Deployments (Available in RHEL 9.6 and 10+)

Available and recommended for new deployments on RHEL 9.6 and 10 +.
The SAPHanaController resource agent with next generation system replication architecture (SAPHanaSR-angi) provides improved integration and management capabilities for both scale-up and scale-out deployments. For detailed information:

For documentation on the resource you can review the man page.

```
# man ocf_heartbeat_SAPHanaController
```

For scale-up (2-node)
Create the primitive

```
# pcs resource create rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaController \
SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="2" \
meta priority="100"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHanaController_HDB_HDB00 ocf:heartbeat:SAPHanaController \
SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="2" \
meta priority="100"
```

For scale-out
Create the primitive using the SAPHanaController Resource Agent:

```
# pcs resource create rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaController \
SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaController \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" "\
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

Details:

- **SID** - SAP System ID for the HANA instance
- **InstanceNumber** - Instance number of the SAP HANA instance
- **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
- **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
- **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)
- **PREFER_SITE_TAKEOVER** defines whether a takeover to the secondary is preferred. Review for non standard deployments.
- **AUTOMATED_REGISTER** defines whether the ex-primary should be registered as a secondary. Review for non standard deployments.
- **DUPLICATE_PRIMARY_TIMEOUT** is the wait time to minimise the risk of an unintended dual primary.
- **meta priority** - Setting this to 100 works in conjunction with priority-fencing-delay to ensure proper failover order and prevent simultaneous fencing operations
- The start and stop timeout values (3600s) may need to be increased for larger databases. Adjust these values based on your database size and observed startup/shutdown times
- If you need to update your configuration, the following examples may help you with the right command

```
# pcs resource update rsc_SAPHanaController_HDB_HDB00 op monitor role="Promoted" timeout=900
# pcs resource update rsc_SAPHanaController_HDB_HDB00 DUPLICATE_PRIMARY_TIMEOUT=3600
# pcs resource meta rsc_SAPHanaController_HDB_HDB00-clone priority=100
```

### Classic Deployments

For classic scale-up deployments, the SAPHana resource agent manages takeover between two SAP HANA databases. For detailed information:

```
# man ocf_heartbeat_SAPHana
```

For scale-up (2-node)
Create the primitive using the SAPHana Resource Agent

```
# pcs resource create rsc_SAPHana_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHana \
SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="2" \
meta priority="100"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHana_HDB_HDB00 ocf:heartbeat:SAPHana \
SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="2" \
meta priority="100"
```

For scale-out
Create the primitive using the SAPHanaController Resource Agent:

```
# pcs resource create rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaController \
SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md "sap-hana-pacemaker-rhel-parameters.md")_ :

```
# pcs resource create rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:heartbeat:SAPHanaController \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" "\
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
promotable notify="true" clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

Details:

- **SID** - SAP System ID for the HANA instance
- **InstanceNumber** - Instance number of the SAP HANA instance
- **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
- **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
- **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)
- **PREFER_SITE_TAKEOVER** defines whether a takeover to the secondary is preferred. Review for non standard deployments.
- **AUTOMATED_REGISTER** defines whether the ex-primary should be registered as a secondary. Review for non standard deployments.
- **DUPLICATE_PRIMARY_TIMEOUT** is the wait time to minimise the risk of an unintended dual primary.
- **meta priority** - Setting this to 100 works in conjunction with priority-fencing-delay to ensure proper failover order and prevent simultaneous fencing operations
- The start and stop timeout values (3600s) may need to be increased for larger databases. Adjust these values based on your database size and observed startup/shutdown times
- If you need to update your configuration, the following examples may help you with the right command

```
# pcs resource update rsc_SAPHana_HDB_HDB00 op monitor role="Promoted" timeout=900
# pcs resource update rsc_SAPHana_HDB_HDB00 DUPLICATE_PRIMARY_TIMEOUT=3600
# pcs resource meta rsc_SAPHana_HDB_HDB00-clone priority=100
```

## Create Resource Constraints

The following constraints are required.

### Order Constraint

This constraint defines the start order between the SAPHanaTopology and SAPHana resources:

```
# pcs constraint order <SAPHanaTopology-clone> <SAPHana/SAPHanaController-clone> symmetrical=false
```

- _Example_ :

```
# pcs constraint order start rsc_SAPHanaTopology_HDB_HDB00-clone then rsc_SAPHana_HDB_HDB00-clone symmetrical=false
```

### Colocation Constraint

#### IP with Primary

This constraint ensures that the IP resource which determines the target of the overlay IP runs on the node which has the primary SAP Hana role:

```
# pcs constraint colocation add <ip_resource> with promoted <SAPHana/SAPHanaController-clone> 2000
```

- _Example_ :

```
# pcs constraint colocation add rsc_ip_HDB_HDB00 with promoted rsc_SAPHana_HDB_HDB00-clone 2000
```

#### ReadOnly IP with Secondary (Only for ReadOnly Patterns)

This constraint ensures that the read-enabled IP resource runs on the secondary (Unpromoted) node. When the secondary node is unavailable, the IP will move to the primary node, where read workloads will share capacity with primary workloads:

```
# pcs constraint colocation add <ip_resource> with unpromoted <SAPHana/SAPHanaController-clone> 2000
```

- _Example_ :

```
# pcs constraint colocation add rsc_ip_HDB_HDB00_readenabled  with unpromoted rsc_SAPHana_HDB_HDB00-clone 2000
```

### Location Constraint

#### No SAP HANA Resources on the Majority Maker (Scale Out Only)

This location constraint ensures that SAP HANA Resources avoid the Majority Maker, which is not suited to running them.

```
# pcs constraint location <SAPHanaTopology-clone> avoids <hostname_mm>
# pcs constraint location <SAPHana/SAPHanaController-clone> avoids <hostname_mm>
```

### Activate Cluster

Use `pcs config show` to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This allows the cluster to take control of the resources:

```
# pcs property set maintenance-mode=false
```

## Reset Configuration – Optional

###### Important

The following instructions help you reset the complete configuration. Run these commands only if you want to start setup from the beginning.

Run the following command to back up the current configuration for reference:

```
# pcs config backup /tmp/cluster_backup_$(date +%Y%m%d)
# pcs config show > /tmp/config_backup_$(date +%Y%m%d).txt
```

Run the following command to stop and clear the current configuration

```
# pcs cluster stop --all
hanahost02: Stopping Cluster (pacemaker)...
hanahost01: Stopping Cluster (pacemaker)...
hanahost02: Stopping Cluster (corosync)...
hanahost01: Stopping Cluster (corosync)...
# pcs cluster destroy
Shutting down pacemaker/corosync services...
Killing any remaining services...
Removing all cluster configuration files...
```

Once the preceding erase command is executed, it removes all of the cluster resources from Cluster Information Base (CIB), and disconnects the communication from corosync to the cluster. Only perform these steps if you absolutely need to reset everything to defaults. For minor changes, use pcs resource update or pcs property set instead.
