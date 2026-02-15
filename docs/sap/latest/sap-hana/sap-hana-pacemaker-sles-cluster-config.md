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
- [Activate Cluster](#_activate_cluster "#_activate_cluster")
- [Reset Configuration – Optional](#_reset_configuration_optional "#_reset_configuration_optional")

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
# crm configure property stonith-action="off"
```

- The **priority-fencing-delay** is recommended for protecting SAP HANA nodes during network partitioning events. When a cluster partition occurs, this delay gives preference to nodes hosting higher priority resources, with SAP HANA Primary (promoted) instances receiving additional priority weighting. This helps ensure the Primary HANA node survives in split-brain scenarios. The recommended 20 second priority-fencing-delay works in conjunction with the pcmk_delay_max (10 seconds) configured in the stonith resource, providing a total potential delay of up to 30 seconds before fencing occurs
- Setting **stonith-action="off"** ensures fenced nodes remain down until manually investigated, preventing potentially compromised nodes from automatically rejoining the cluster. While "reboot" is available as an alternative if automated recovery is preferred, "off" is recommended for SAP HANA clusters to prevent potential data corruption and enable root cause analysis

To verify your cluster property settings:

```
# crm configure show property
```

### Configure Resource Defaults

Configure resource default behaviors:

```
# crm configure rsc_defaults resource-stickiness="1000"
# crm configure rsc_defaults migration-threshold="5000"
```

- The **resource-stickiness** value prevents unnecessary resource movement, effectively setting a "cost" for moving resources. A value of 1000 strongly encourages resources to remain on their current node, avoiding the downtime associated with movement.
- The **migration-threshold** of 5000 ensures the cluster will attempt to recover a resource on the same node many times before declaring that node unsuitable for hosting the resource.

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

## Create STONITH Fencing Resource

An AWS STONITH resource agent is recommended for AWS deployments on SUSE as it leverages the AWS API to safely fence failed or incommunicable nodes by stopping the EC2 instances. See [Pacemaker - STONITH Fencing Agent](sap-hana-pacemaker-sles-concepts.md#fencing-sles "sap-hana-pacemaker-sles-concepts.md#fencing-sles").

Create the STONITH resource using resource agent **`external/ec2`**:

```
# crm configure primitive <stonith_resource_name> stonith:external/ec2 \
params tag="<cluster_tag>" profile="<cli_cluster_profile>" pcmk_delay_max="10" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

Details:

- **tag** - EC2 instance tag key name that associates instances with this cluster configuration. This tag key must be unique within the AWS account and have a value which matches the instance hostname. See [Create Amazon EC2 Resource Tags Used by Amazon EC2 STONITH Agent](sap-hana-pacemaker-sles-ec2-configuration.md#create-cluster-tags "sap-hana-pacemaker-sles-ec2-configuration.md#create-cluster-tags") for EC2 instance tagging configuration.
- **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
- **pcmk_delay_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing. Historically set to higher values (45s), but with `priority-fencing-delay` now handling primary node protection, a lower value (10s) is sufficient.
- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

```
# crm configure primitive res_stonith_ec2 stonith:external/ec2 \
params tag="pacemaker" profile="cluster" \
pcmk_delay_max="10" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

## Create Overlay IP Resources

This resource ensures client connections follow the SAP HANA primary instance during failover by updating AWS route table entries. It manages an overlay IP address that always points to the active SAP HANA database

Create the IP resource:

```
# crm configure primitive rsc_ip_<SID>_HDB<hana_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
params ip="<hana_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

Details:

- **ip** - Overlay IP address that will be used to connect to the Primary SAP HANA database. See [Overlay IP Concept](sap-hana-pacemaker-sles-concepts.md#overlay-ip-sles "sap-hana-pacemaker-sles-concepts.md#overlay-ip-sles")
- **routing_table** - AWS route table ID(s) that need to be updated. Multiple route tables can be specified using commas (For example, `routing_table=rtb-xxxxxroutetable1,rtb-xxxxxroutetable2`). Ensure initial entries have been created following [Add VPC Route Table Entries for Overlay IPs](sap-hana-pacemaker-sles-infra-setup.md#rt-sles "sap-hana-pacemaker-sles-infra-setup.md#rt-sles")
- **interface** - Network interface for the IP address (typically eth0)
- **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

```
# crm configure primitive rsc_ip_HDB_HDB00 ocf:heartbeat:aws-vpc-move-ip \
params ip="172.16.52.1" \
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
# crm configure primitive rsc_ip_<SID>_HDB<hana_sys_nr>_readenabled ocf:heartbeat:aws-vpc-move-ip \
params ip="<readenabled_overlayip>" \
routing_table="<routetable_id>" \
interface="eth0" \
profile="<cli_cluster_profile>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

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
# crm configure primitive rsc_ip_<SID>_HDB<hana_sys_nr> ocf:heartbeat:aws-vpc-move-ip \
params ip="<hana_overlayip>" routing_table=<routetable_id> interface=eth0 \
profile="<cli_cluster_profile>" lookup_type=NetworkInterfaceId \
routing_table_role="arn:aws:iam::<sharing_vpc_account_id>:role/<sharing_vpc_account_cluster_role>" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="60" timeout="60"
```

Additional details:

- **lookup_type** = NetworkInterfaceId
- **routing_table_role** = "arn:aws:iam::<shared_vpc_account_id>:role/<sharing_vpc_account_cluster_role>"

## Create SAPHanaTopology Resource

The SAPHanaTopology resource agent helps manage high availability for SAP HANA databases with system replication. It analyzes the SAP HANA topology and reports findings via node status attributes. These attributes are used by either the SAPHana or SAPHanaController resource agents to control the SAP HANA databases. SAPHanaTopology starts and monitors the local saphostagent, leveraging SAP interfaces like landscapeHostConfiguration.py, hdbnsutil, and saphostctrl to gather information about system status, roles, and configuration.

### SAPHanaSR-angi and Classic Deployments

For both scale-up and scale-out deployments

For documentation on the resource you can review the man page.

```
# man ocf_suse_SAPHanaTopology
```

For scale-up (2-node)
For the primitive:

```
# crm configure primitive rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHanaTopology \
params SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600"
```

For the clone:

```
# crm configure clone cln_SAPHanaTopology_<SID>_HDB<hana_sys_nr> rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="2"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

```
# crm configure primitive rsc_SAPHanaTopology_HDB_HDB00 ocf:suse:SAPHanaTopology \
params SID="HDB" \
InstanceNumber="00" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600"

# crm configure clone cln_SAPHanaTopology_HDB_HDB00 rsc_SAPHanaTopology_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="2"
```

For scale-out
For the primitive:

```
# crm configure primitive rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHanaTopology \
params SID="<SID>" InstanceNumber="<hana_sys_nr>" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600"
```

For the clone:

```
# crm configure clone cln_SAPHanaTopology_<SID>_HDB<hana_sys_nr> rsc_SAPHanaTopology_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

```
# crm configure primitive rsc_SAPHanaTopology_HDB_HDB00 ocf:suse:SAPHanaTopology \
params SID="HDB" InstanceNumber="00" \
op start interval="0" timeout="600" \
op stop interval="0" timeout="300" \
op monitor interval="10" timeout="600"

# crm configure clone cln_SAPHanaTopology_HDB_HDB00 rsc_SAPHanaTopology_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="6"
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

### SAPHanaSR-angi Deployments (Available in SLES 15 SP4+)

Available and recommended for new deployments on SLES 15 SP4 and above.
The SAPHanaController resource agent with next generation system replication architecture (SAPHanaSR-angi) provides improved integration and management capabilities for both scale-up and scale-out deployments. For detailed information:

For documentation on the resource you can review the man page.

```
# man ocf_suse_SAPHanaController
```

For scale-up (2-node)
Create the primitive

```
# crm configure primitive rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHanaController \
params SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
meta priority="100"
```

Create the clone

```
# crm configure clone msl_SAPHanaController_<SID>_HDB<hana_sys_nr> rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="2"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

```
# crm configure primitive rsc_SAPHanaController_HDB_HDB00 ocf:suse:SAPHanaController \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700" \
meta priority="100"
# crm configure clone msl_SAPHanaController_HDB_HDB00 rsc_SAPHanaController_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="2"
```

For scale-out
Create the primitive

```
# crm configure primitive rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHanaController \
params SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" "\
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700"
```

Create the clone

```
# crm configure clone msl_SAPHanaController_<SID>_HDB<hana_sys_nr> rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

###### Example

```
# crm configure primitive rsc_SAPHanaController_HDB_HDB00 ocf:suse:SAPHanaController \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" "\
op monitor interval="60" role="Promoted" timeout="700" \
op monitor interval="61" role="Unpromoted" timeout="700"

# crm configure clone msl_SAPHanaController_HDB_HDB00 rsc_SAPHanaController_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="6"
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

### Classic Deployments

For classic scale-up deployments, the SAPHana resource agent manages takeover between two SAP HANA databases. For detailed information:

```
# man ocf_suse_SAPHana
```

For scale-up (2-node)
Create the primitive using the SAPHana Resource Agent

```
# crm configure primitive rsc_SAPHana_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHana \
params SID="<SID>" \
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Master" timeout="700" \
op monitor interval="61" role="Slave" timeout="700" \
meta priority="100"
```

Create the clone

```
# crm configure clone msl_SAPHana_<SID>_HDB<hana_sys_nr> rsc_SAPHana_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="2"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

```
# crm configure primitive rsc_SAPHana_HDB_HDB00 ocf:suse:SAPHana \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" "\
op monitor interval="60" role="Master" timeout="700" \
op monitor interval="61" role="Slave" timeout="700" \
meta priority="100"

# crm configure clone msl_SAPHana_HDB_HDB00 rsc_SAPHana_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="2"
```

For scale-out
Create the primitive using the SAPHanaController Resource Agent:

```
# crm configure primitive rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> ocf:suse:SAPHanaController \
params SID="<SID>"
InstanceNumber="<hana_sys_nr>" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Master" timeout="700" \
op monitor interval="61" role="Slave" timeout="700"
```

Create the clone

```
# crm configure clone msl_SAPHanaController_<SID>_HDB<hana_sys_nr> rsc_SAPHanaController_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="<number-of-nodes>"
```

- _Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md "sap-hana-pacemaker-sles-parameters.md")_ :

```
# crm configure primitive rsc_SAPHanaController_HDB_HDB00 ocf:suse:SAPHanaController \
params SID="HDB" \
InstanceNumber="00" \
PREFER_SITE_TAKEOVER="true" \
DUPLICATE_PRIMARY_TIMEOUT="7200" \
AUTOMATED_REGISTER="true" \
op start interval="0" timeout="3600" \
op stop interval="0" timeout="3600" \
op promote interval="0" timeout="3600" \
op monitor interval="60" role="Master" timeout="700" \
op monitor interval="61" role="Slave" timeout="700"

# crm configure clone msl_SAPHana_HDB_HDB00 rsc_SAPHana_HDB_HDB00 \
meta clone-node-max="1" interleave="true" clone-max="6"
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

## Create Resource Constraints

The following constraints are required.

### Order Constraint

This constraint defines the start order between the SAPHanaTopology and SAPHana resources:

```
# crm configure order <order_rule_name> Optional: <SAPHanaTopology_clone> <SAPHana/SAPHanaController_Clone>
```

- _Example_ :

```
# crm configure order ord_SAPHana Optional: cln_SAPHanaTopology_HDB_HDB00 msl_SAPHana_HDB_HDB00
```

### Colocation Constraint

#### IP with Primary

This constraint ensures that the IP resource which determines the target of the overlay IP runs on the node which has the primary SAP HANA role:

```
# crm configure colocation <colocation_rule_name> 2000: <ip_resource_name> <saphana/saphanacontroller name>:Master
```

- _Example_ :

```
# crm configure colocation col_ip_SAPHana_Primary 2000: rsc_ip_HDB_HDB00 msl_SAPHana_HDB_HDB00:Master
```

#### ReadOnly IP with Secondary (Only for ReadOnly Patterns)

This constraint ensures that the read-enabled IP resource runs on the secondary (Unpromoted) node. When the secondary node is unavailable, the IP will move to the primary node, where read workloads will share capacity with primary workloads:

```
# crm configure colocation <colocation_rule_name> 2000: rsc_ip_<SID>_HDB<hana_sys_nr>_readenabled msl_SAPHana/SAPHanaController_<SID>_HDB<hana_sys_nr>:Unpromoted
```

- _Example_ :

```
# crm configure colocation col_ip_readenabled_SAPHana_Secondary 2000: rsc_ip_HDB_HDB00_readenabled msl_SAPHana_HDB_HDB00:Unpromoted
```

### Location Constraint

#### No SAP HANA Resources on the Majority Maker (Scale Out Only)

This location constraint ensures that SAP HANA Resources avoid the Majority Maker, which is not suited to running them.

```
# crm configure location loc_SAPHanaTopology_avoid_majority_maker cln_SAPHanaTopology_<SID>_HDB<hana_sys_nr> -inf:<hostname_mm>

# crm configure location loc_SAPHana/SAPHanaController_avoid_majority_maker msl_SAPHana/SAPHanaController_<SID>_HDB<hana_sys_nr> -inf:<hostname_mm>
```

- _Example_ :

```
# crm configure location loc_SAPHanaTopology_avoid_majority_maker cln_SAPHanaTopology_HDB_HDB00 -inf:hanamm
# crm configure location loc_SAPHana_avoid_majority_maker msl_SAPHana_HDB_HDB00 -inf:hanamm
```

## Activate Cluster

Use `crm config show` and `crm config edit` commands to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources:

```
# crm maintenance off
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
