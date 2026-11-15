

# Step 1: Set up migration wave
<a name="transform-vmware-ms-setup-wave"></a>

In this phase, AWS Transform prepares the migration wave by configuring the target account, verifying service permissions, setting up resource tags, adding networking data to your inventory, and configuring replication and launch settings.

## Migration mode and account configuration
<a name="transform-vmware-ms-migration-mode"></a>

AWS Transform supports two migration modes:
+ **Single-account migration** – All servers in the wave migrate to the same target account configured in your connector.
+ **Multi-account migration** – Servers migrate to different target accounts specified in your inventory file. For multi-account migrations, your inventory file must include an `mgn:account-id` column with the target account ID for each server.

AWS Transform confirms the target account configuration and verifies that MGN is initialized in each target account. If MGN is not yet initialized, AWS Transform provides instructions to complete the initialization. During initialization, MGN creates the following IAM service roles for replication and launch operations:
+ `AWSApplicationMigrationReplicationServerRole`
+ `AWSApplicationMigrationConversionServerRole`
+ `AWSApplicationMigrationMGHRole`
+ `AWSApplicationMigrationLaunchInstanceWithDrsRole`
+ `AWSApplicationMigrationLaunchInstanceWithSsmRole`
+ `AWSApplicationMigrationAgentRole`

To learn more about these roles, see [Initializing MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html) or [Initializing MGN with the API](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-api.html) in the *MGN User Guide*.

For multi-account migrations, AWS Transform also creates the following role during the initialization step: `AWSTransformRehostSharingRole_<management-or-delegated-admin-account-id>`. This role is deployed across all migration target accounts.

## Resource tagging verification
<a name="transform-vmware-ms-resource-tagging"></a>

After service permissions are confirmed, AWS Transform verifies that all required resources are properly tagged for the migration to be operated by the agent successfully. If any resources are missing required tags, AWS Transform provides a link to the tagging page where you can apply the missing tags before continuing. The following tags are required:
+ Existing source servers must have tags `CreatedBy: AWSTransform` and `ATWorkspace: <workspace_id>`. If you have already started replication on source servers and created them in the AWS Transform MGN service, you need to tag these servers so that AWS Transform can correlate them with the source servers discovered from your on-premises environment, and avoid unnecessary creation of duplicate source servers. AWS Transform automatically correlates between them using the user-provided ID, FQDN, or hostname keys.
+ Network resources must be properly tagged for both replication (staging area) and launch instances. AWS Transform displays the full list of network resources in your target account, with an indication of whether each resource is already tagged or not. You can review the list and select any untagged resources you want to add. For each resource you select, AWS Transform applies the relevant tag:
  + `CreatedBy: AWSTransform` or `CreatedFor: AWSTransform`, depending on the resource type.
  + `ATWorkspace: <workspace_id>` is applied to all selected resources.

  VPCs and subnets created by the AWS Transform network migration agent are automatically tagged.
+ In addition to VPCs and subnets, AWS Transform also displays all existing Elastic Network Interfaces (ENIs) found in your target account. If you want AWS Transform to use them as part of your instance launch, they must be tagged with `CreatedFor: AWSTransform` and `ATWorkspace: <workspace_id>`. For more information on how to attach or add ENIs to the Amazon EC2 launch template, see [Detailed considerations](https://docs.aws.amazon.com/mgn/latest/ug/detailed-considerations.html) in the *MGN User Guide*.

## Add networking data to inventory
<a name="transform-vmware-ms-networking-data"></a>

AWS Transform adds networking information from your network migration to the inventory file. This step maps your servers to the appropriate target subnets and security groups based on the network configuration generated during the migrate network phase.

## Replication and launch settings
<a name="transform-vmware-ms-replication-settings"></a>

### Replication settings configuration
<a name="transform-vmware-ms-replication-config"></a>

Replication settings determine how data is replicated from your source servers to AWS. Configure the replication settings in the replication template before adding source servers to AWS Transform MGN. AWS Transform shows you all the replication settings parameters — you can configure them through a dedicated HITL or through the chat interface.

For more details about the replication settings parameters, see [Replication settings template](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html) in the *MGN User Guide*.

### Launch template settings
<a name="transform-vmware-ms-launch-template-config"></a>

The launch template allows you to control the way AWS Transform MGN launches instances in AWS. The default configuration defined in the template is automatically applied to every newly added server. You can configure launch template settings through a dedicated HITL or through the chat interface.

For more details about the launch template settings parameters, see [Launch template](https://docs.aws.amazon.com/mgn/latest/ug/launch-template.html) in the *MGN User Guide*.

AWS Transform also provides a link to the Amazon EC2 launch template ID associated with the launch template, allowing you to change additional Amazon EC2 launch template attributes. To edit the Amazon EC2 launch template, follow the instructions in [Launch template](https://docs.aws.amazon.com/mgn/latest/ug/launch-template.html) in the *MGN User Guide*.

## IP assignment strategy
<a name="transform-vmware-ms-ip-assignment"></a>

You choose how IP addresses are assigned to your migrated servers:
+ **Static IP** – The source server's IP address is maintained. If CIDR transformation is required, AWS Transform automatically converts the IP address to match the new CIDR.
+ **Dynamic IP (DHCP)** – Each server is assigned a new IP address from the subnet's IP pool.

**Note**  
If you selected the MAP security groups mapping strategy during network migration, only static IP assignment is available. For more details, see [Security groups mapping](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-security-group-association).