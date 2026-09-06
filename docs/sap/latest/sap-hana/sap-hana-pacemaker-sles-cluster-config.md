

# Cluster Configuration
<a name="sap-hana-pacemaker-sles-cluster-config"></a>

Bootstrap the cluster and configure all required cluster resources and constraints.

**Topics**
+ [Prepare for Resource Creation](#_prepare_for_resource_creation)
+ [Cluster Bootstrap](#cluster-bootstrap)
+ [Create STONITH Fencing Resource](#resource-stonith)
+ [Create Overlay IP Resources](#resource-overlayip)
+ [Create SAPHanaTopology Resource](#resource-saphanatop)
+ [Create SAPHANA Resource (based on resource agent SAPHana or SAPHanaController)](#resource-saphana)
+ [Create Resource Constraints](#resource-constraints)
+ [Activate Cluster](#_activate_cluster)
+ [Reset Configuration – Optional](#_reset_configuration_optional)

## Prepare for Resource Creation
<a name="_prepare_for_resource_creation"></a>

To ensure that the cluster does not perform unexpected actions during setup of resources and configuration, set the maintenance mode to true.

Run the following command to put the cluster in maintenance mode:

```
# crm maintenance on
```

To verify the current maintenance state:

```
# crm status
```

**Note**  
There are two types of maintenance mode:  
Cluster-wide maintenance (set with `crm maintenance on`)
Node-specific maintenance (set with `crm node maintenance nodename`)
Always use cluster-wide maintenance mode when making configuration changes. For node-specific operations like hardware maintenance, refer to the Operations for proper procedures.  
To disable maintenance mode after configuration is complete:  

```
# crm maintenance off
```

## Cluster Bootstrap
<a name="cluster-bootstrap"></a>

### Configure Cluster Properties
<a name="_configure_cluster_properties"></a>

Configure cluster properties to establish fencing behavior and resource failover settings:

```
# crm configure property stonith-enabled="true"
# crm configure property stonith-timeout="600"
# crm configure property priority-fencing-delay="20"
# crm configure property stonith-action="off"
```
+ The **priority-fencing-delay** is recommended for protecting SAP HANA nodes during network partitioning events. When a cluster partition occurs, this delay gives preference to nodes hosting higher priority resources, with SAP HANA Primary (promoted) instances receiving additional priority weighting. This helps ensure the Primary HANA node survives in split-brain scenarios. The recommended 20 second priority-fencing-delay works in conjunction with the pcmk\_delay\_max (10 seconds) configured in the stonith resource, providing a total potential delay of up to 30 seconds before fencing occurs
+ Setting **stonith-action="off"** ensures fenced nodes remain down until manually investigated, preventing potentially compromised nodes from automatically rejoining the cluster. While "reboot" is available as an alternative if automated recovery is preferred, "off" is recommended for SAP HANA clusters to prevent potential data corruption and enable root cause analysis

To verify your cluster property settings:

```
# crm configure show property
```

### Configure Resource Defaults
<a name="_configure_resource_defaults"></a>

Configure resource default behaviors:

```
# crm configure rsc_defaults resource-stickiness="1000"
# crm configure rsc_defaults migration-threshold="5000"
```
+ The **resource-stickiness** value prevents unnecessary resource movement, effectively setting a "cost" for moving resources. A value of 1000 strongly encourages resources to remain on their current node, avoiding the downtime associated with movement.
+ The **migration-threshold** of 5000 ensures the cluster will attempt to recover a resource on the same node many times before declaring that node unsuitable for hosting the resource.

Individual resources may override these defaults with their own defined values.

To verify your resource default settings:

```
# crm configure show rsc_defaults
```

### Configure Operation Defaults
<a name="_configure_operation_defaults"></a>

Configure operation timeout defaults:

```
# crm configure op_defaults timeout="600"
```
+ The **op\_defaults timeout** ensures all cluster operations have a reasonable default timeout of 600 seconds. Individual resources may override this with their own timeout values.

To verify your operation default settings:

```
# crm configure show op_defaults
```

## Create STONITH Fencing Resource
<a name="resource-stonith"></a>

An AWS STONITH resource agent is recommended for AWS deployments on SUSE as it leverages the AWS API to safely fence failed or incommunicable nodes by stopping the EC2 instances. See [Pacemaker - STONITH Fencing Agent](sap-hana-pacemaker-sles-concepts.md#fencing-sles).

As of SLES 15 SP5 with the latest fence-agents package, we recommend resource agent `fence_aws` which can leverage a new API feature to skip the shutdown of the Operating System and fence unresponsive Instances more quickly. For older SLES versions, the `stonith:external/ec2` resource is supported.

------
#### [ SLES 15 SP5 and above ]

Create the STONITH resource using resource agent ** `fence_aws` **:

```
# crm configure primitive <stonith_resource_name> stonith:fence_aws \
params pcmk_host_map="<hostname_1>:<instance_id_1>;<hostname_2>:<instance_id_2>" \
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
+  **pcmk\_host\_map** - Maps cluster node hostnames to their EC2 instance IDs. This mapping must be unique within the AWS account and follow the format hostname:instance-id, with multiple entries separated by semicolons.
+  **region** - AWS region where the EC2 instances are deployed
+  **pcmk\_delay\_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing in 2-node clusters. Historically set to higher values, but with `priority-fencing-delay` now handling primary node protection, a lower value (10s) is sufficient. Omit in clusters with real quorum (3\+ nodes) to avoid unnecessary delay.
+  **pcmk\_reboot\_timeout** - Maximum time in seconds allowed for a reboot operation
+  **pcmk\_reboot\_retries** - Number of times to retry a failed reboot operation
+  **skip\_os\_shutdown** (recommended) - Leverages a new ec2 stop-instance API flag to forcefully stop an EC2 Instance by skipping the shutdown of the Operating System.
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :

  ```
  # crm configure primitive rsc_fence_aws stonith:fence_aws \
  params pcmk_host_map="hanahost01:i-xxxxinstidforhost1;hanahost02:i-xxxxinstidforhost2" region="us-east-1" \
  skip_os_shutdown="true" \
  pcmk_delay_max="10" \
  pcmk_reboot_timeout="600" \
  pcmk_reboot_retries="4" \
  op start interval="0" timeout="600" \
  op stop interval="0" timeout="180" \
  op monitor interval="300" timeout="60"
  ```

  When configuring the STONITH resource, consider your instance’s startup and shutdown times. The default pcmk\_reboot\_action is 'reboot', where the cluster waits for both stop and start actions to complete before considering the fencing action successful. Setting `pcmk_reboot_action=off` allows the cluster to proceed immediately after shutdown. For High Memory Metal instances, only 'off' is recommended due to the extended time to initialize memory during startup. If changing `pcmk_reboot_action="off"`, also add `pcmk_off_timeout="600"` and `pcmk_off_retries="4"`. Use `crm configure edit <stonith_resource_name>` to modify.

------
#### [ Older SLES versions ]

Create the STONITH resource using resource agent ** `external/ec2` **:

```
# crm configure primitive <stonith_resource_name> stonith:external/ec2 \
params tag="<cluster_tag>" profile="<cli_cluster_profile>" pcmk_delay_max="10" \
op start interval="0" timeout="180" \
op stop interval="0" timeout="180" \
op monitor interval="300" timeout="60"
```

Details:
+  **tag** - EC2 instance tag key name that associates instances with this cluster configuration. This tag key must be unique within the AWS account and have a value which matches the instance hostname. See [Create Amazon EC2 Resource Tags Used by Amazon EC2 STONITH Agent](sap-hana-pacemaker-sles-ec2-configuration.md#create-cluster-tags) for EC2 instance tagging configuration.
+  **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
+  **pcmk\_delay\_max** - Random delay before fencing operations. Works in conjunction with cluster property `priority-fencing-delay` to prevent simultaneous fencing. Historically set to higher values (45s), but with `priority-fencing-delay` now handling primary node protection, a lower value (10s) is sufficient.

   *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :

  ```
  # crm configure primitive res_stonith_ec2 stonith:external/ec2 \
  params tag="pacemaker" profile="cluster" \
  pcmk_delay_max="10" \
  op start interval="0" timeout="180" \
  op stop interval="0" timeout="180" \
  op monitor interval="300" timeout="60"
  ```

------

**Note**  
 **Migrating from `external/ec2` to `fence_aws` **   
Ensure fence-agents is updated to the latest available version on all cluster nodes:  

```
# zypper refresh
# zypper up fence-agents
```
On SLES 15 SP5 and SP6, the following Python 3.11 packages are also required as dependencies for `fence_aws`:  

```
# zypper install python311-pycurl python311-pexpect
```
Then place the cluster in maintenance mode, delete the existing STONITH resource, create the new `fence_aws` resource, and disable maintenance mode:  

```
# crm maintenance on
# crm configure delete <old_stonith_resource_name>
# crm configure primitive <new_resource> stonith:fence_aws \
params pcmk_host_map="<hostname_1>:<instance_id_1>;<hostname_2>:<instance_id_2>" \
region="<aws_region>" ...
# crm maintenance off
```
EC2 instance tags used by `external/ec2` can remain in place — they do not interfere with `fence_aws`.

## Create Overlay IP Resources
<a name="resource-overlayip"></a>

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
+  **ip** - Overlay IP address that will be used to connect to the Primary SAP HANA database. See [Overlay IP Concept](sap-hana-pacemaker-sles-concepts.md#overlay-ip-sles) 
+  **routing\_table** - AWS route table ID(s) that need to be updated. Multiple route tables can be specified using commas (For example, `routing_table=rtb-xxxxxroutetable1,rtb-xxxxxroutetable2`). Ensure initial entries have been created following [Add VPC Route Table Entries for Overlay IPs](sap-hana-pacemaker-sles-infra-setup.md#rt-sles) 
+  **interface** - Network interface for the IP address (typically eth0)
+  **profile** - (optional) AWS CLI profile name for API authentication. Verify profile exists with `aws configure list-profiles`. If a profile is not explicitly configured the default profile will be used.
+  **awscli** - (optional) Path to the AWS CLI executable. The default path is `/usr/bin/aws`. Only specify this parameter if the AWS CLI is installed in a different location. To confirm the path on your system, run `which aws`.
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-rhel-parameters.md) * :  
**Example**  

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

**For Active/Active Read Enabled**  
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
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :  
**Example**  

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

**For Shared VPC**  
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
+  **lookup\_type** = NetworkInterfaceId
+  **routing\_table\_role** = "arn:aws:iam::<shared\_vpc\_account\_id>:role/<sharing\_vpc\_account\_cluster\_role>"

## Create SAPHanaTopology Resource
<a name="resource-saphanatop"></a>

The SAPHanaTopology resource agent helps manage high availability for SAP HANA databases with system replication. It analyzes the SAP HANA topology and reports findings via node status attributes. These attributes are used by either the SAPHana or SAPHanaController resource agents to control the SAP HANA databases. SAPHanaTopology starts and monitors the local saphostagent, leveraging SAP interfaces like landscapeHostConfiguration.py, hdbnsutil, and saphostctrl to gather information about system status, roles, and configuration.

### SAPHanaSR-angi and Classic Deployments
<a name="_saphanasr_angi_and_classic_deployments"></a>

For both scale-up and scale-out deployments

For documentation on the resource you can review the man page.

```
# man ocf_suse_SAPHanaTopology
```

------
#### [ For scale-up (2-node) ]

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
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :  
**Example**  

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

------
#### [ For scale-out ]

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
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :  
**Example**  

  ```
  # crm configure primitive rsc_SAPHanaTopology_HDB_HDB00 ocf:suse:SAPHanaTopology \
  params SID="HDB" InstanceNumber="00" \
  op start interval="0" timeout="600" \
  op stop interval="0" timeout="300" \
  op monitor interval="10" timeout="600"
  
  # crm configure clone cln_SAPHanaTopology_HDB_HDB00 rsc_SAPHanaTopology_HDB_HDB00 \
  meta clone-node-max="1" interleave="true" clone-max="6"
  ```

------

Details:
+  **SID** - SAP System ID for the HANA instance
+  **InstanceNumber** - Instance number of the SAP HANA instance
+  **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
+  **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
+  **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)

## Create SAPHANA Resource (based on resource agent SAPHana or SAPHanaController)
<a name="resource-saphana"></a>

The SAP HANA resource agents manage system replication and failover between SAP HANA databases. These agents control start, stop, and monitoring operations while checking synchronization status to maintain data consistency. They leverage SAP interfaces including sapcontrol, landscapeHostConfiguration, hdbnsutil, systemReplicationStatus, and saphostctrl. All configurations work in conjunction with the SAPHanaTopology agent, which gathers information about the system replication status across cluster nodes.

Choose the appropriate resource agent configuration based on your SAP HANA architecture:

### SAPHanaSR-angi Deployments (Available in SLES 15 SP4\+)
<a name="_saphanasr_angi_deployments_available_in_sles_15_sp4"></a>

Available and recommended for new deployments on SLES 15 SP4 and above. The SAPHanaController resource agent with next generation system replication architecture (SAPHanaSR-angi) provides improved integration and management capabilities for both scale-up and scale-out deployments. For detailed information:

For documentation on the resource you can review the man page.

```
# man ocf_suse_SAPHanaController
```

------
#### [ For scale-up (2-node) ]

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
meta clone-node-max="1" promotable="true" interleave="true" clone-max="2"
```
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :  
**Example**  

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
  meta clone-node-max="1" promotable="true" interleave="true" clone-max="2"
  ```

------
#### [ For scale-out ]

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
meta clone-node-max="1" promotable="true" interleave="true" clone-max="<number-of-nodes>"
```
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :  
**Example**  

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
  meta clone-node-max="1" promotable="true" interleave="true" clone-max="6"
  ```

------

Details:
+  **SID** - SAP System ID for the HANA instance
+  **InstanceNumber** - Instance number of the SAP HANA instance
+  **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
+  **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
+  **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)
+  **PREFER\_SITE\_TAKEOVER** defines whether a takeover to the secondary is preferred. Review for non standard deployments.
+  **AUTOMATED\_REGISTER** defines whether the ex-primary should be registered as a secondary. Review for non standard deployments.
+  **DUPLICATE\_PRIMARY\_TIMEOUT** is the wait time to minimise the risk of an unintended dual primary.
+  **meta priority** - Setting this to 100 works in conjunction with priority-fencing-delay to ensure proper failover order and prevent simultaneous fencing operations
+ The start and stop timeout values (3600s) may need to be increased for larger databases. Adjust these values based on your database size and observed startup/shutdown times

### Classic Deployments
<a name="_classic_deployments"></a>

For classic scale-up deployments, the SAPHana resource agent manages takeover between two SAP HANA databases. For detailed information:

```
# man ocf_suse_SAPHana
```

------
#### [ For scale-up (2-node) ]

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
# crm configure ms msl_SAPHana_<SID>_HDB<hana_sys_nr> rsc_SAPHana_<SID>_HDB<hana_sys_nr> \
meta clone-node-max="1" interleave="true" clone-max="2"
```
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :

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
  
  # crm configure ms msl_SAPHana_HDB_HDB00 rsc_SAPHana_HDB_HDB00 \
  meta clone-node-max="1" interleave="true" clone-max="2"
  ```

------
#### [ For scale-out ]

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
+  *Example using values from [Parameter Reference](sap-hana-pacemaker-sles-parameters.md) * :

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
  
  # crm configure ms msl_SAPHana_HDB_HDB00 rsc_SAPHana_HDB_HDB00 \
  meta clone-node-max="1" interleave="true" clone-max="6"
  ```

------

Details:
+  **SID** - SAP System ID for the HANA instance
+  **InstanceNumber** - Instance number of the SAP HANA instance
+  **clone-node-max** - Defines how many copies of the resource agent can be started on a single node (set to 1)
+  **interleave** - Enables parallel starting of dependent clone resources on the same node (set to true)
+  **clone-max** - Defines the total number of clone instances that can be started in the cluster (For example, use 2 for scale-out or set to 6 for scale-out with 3 nodes per site, do not include majority maker node)
+  **PREFER\_SITE\_TAKEOVER** defines whether a takeover to the secondary is preferred. Review for non standard deployments.
+  **AUTOMATED\_REGISTER** defines whether the ex-primary should be registered as a secondary. Review for non standard deployments.
+  **DUPLICATE\_PRIMARY\_TIMEOUT** is the wait time to minimise the risk of an unintended dual primary.
+  **meta priority** - Setting this to 100 works in conjunction with priority-fencing-delay to ensure proper failover order and prevent simultaneous fencing operations
+ The start and stop timeout values (3600s) may need to be increased for larger databases. Adjust these values based on your database size and observed startup/shutdown times

## Create Resource Constraints
<a name="resource-constraints"></a>

The following constraints are required.

### Order Constraint
<a name="_order_constraint"></a>

This constraint defines the start order between the SAPHanaTopology and SAPHana resources:

```
# crm configure order <order_rule_name> Optional: <SAPHanaTopology_clone> <SAPHana/SAPHanaController_Clone>
```
+  *Example* :

  ```
  # crm configure order ord_SAPHana Optional: cln_SAPHanaTopology_HDB_HDB00 msl_SAPHana_HDB_HDB00
  ```

### Colocation Constraint
<a name="_colocation_constraint"></a>

#### IP with Primary
<a name="_ip_with_primary"></a>

This constraint ensures that the IP resource which determines the target of the overlay IP runs on the node which has the primary SAP HANA role:

```
# crm configure colocation <colocation_rule_name> 2000: <ip_resource_name> <saphana/saphanacontroller name>:Master
```
+  *Example* :

  ```
  # crm configure colocation col_ip_SAPHana_Primary 2000: rsc_ip_HDB_HDB00 msl_SAPHana_HDB_HDB00:Master
  ```

#### ReadOnly IP with Secondary (Only for ReadOnly Patterns)
<a name="_readonly_ip_with_secondary_only_for_readonly_patterns"></a>

This constraint ensures that the read-enabled IP resource runs on the secondary (Unpromoted) node. When the secondary node is unavailable, the IP will move to the primary node, where read workloads will share capacity with primary workloads:

```
# crm configure colocation <colocation_rule_name> 2000: rsc_ip_<SID>_HDB<hana_sys_nr>_readenabled msl_SAPHana/SAPHanaController_<SID>_HDB<hana_sys_nr>:Unpromoted
```
+  *Example* :

  ```
  # crm configure colocation col_ip_readenabled_SAPHana_Secondary 2000: rsc_ip_HDB_HDB00_readenabled msl_SAPHana_HDB_HDB00:Unpromoted
  ```

### Location Constraint
<a name="_location_constraint"></a>

#### No SAP HANA Resources on the Majority Maker (Scale Out Only)
<a name="_no_sap_hana_resources_on_the_majority_maker_scale_out_only"></a>

This location constraint ensures that SAP HANA Resources avoid the Majority Maker, which is not suited to running them.

```
# crm configure location loc_SAPHanaTopology_avoid_majority_maker cln_SAPHanaTopology_<SID>_HDB<hana_sys_nr> -inf:<hostname_mm>

# crm configure location loc_SAPHana/SAPHanaController_avoid_majority_maker msl_SAPHana/SAPHanaController_<SID>_HDB<hana_sys_nr> -inf:<hostname_mm>
```
+  *Example* :

  ```
  # crm configure location loc_SAPHanaTopology_avoid_majority_maker cln_SAPHanaTopology_HDB_HDB00 -inf:hanamm
  # crm configure location loc_SAPHana_avoid_majority_maker msl_SAPHana_HDB_HDB00 -inf:hanamm
  ```

## Activate Cluster
<a name="_activate_cluster"></a>

Use `crm config show` and `crm config edit` commands to review that all the values have been entered correctly.

On confirmation of correct values, set the maintenance mode to false using the following command. This enables the cluster to take control of the resources:

```
# crm maintenance off
```

## Reset Configuration – Optional
<a name="_reset_configuration_optional"></a>

**Important**  
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