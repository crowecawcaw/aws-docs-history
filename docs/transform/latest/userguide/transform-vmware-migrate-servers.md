

# Migrate servers

AWS Transform automates the rehosting of your servers to Amazon EC2 at scale. The AI-powered agent guides you through each migration wave, from inventory validation and replication agent deployment through testing and final cutover. AWS Transform handles the orchestration across hundreds of servers while you maintain control over configuration and approval decisions. Internally, AWS Transform uses AWS Transform MGN (MGN) for data replication. For more information about MGN, see [What is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html) in the *MGN User Guide*.

Server migration has the following parts:
+ [Prerequisites](transform-vmware-ms-prerequisites.md) – Make sure your target accounts, network infrastructure, and inventory file are in place.
+ [Configure Migration Defaults](transform-vmware-ms-migration-defaults.md) – Configure how instances are launched and how replication is set up, including post-launch actions. AWS Transform provides intelligent defaults so you can get started quickly.
+ [Wave execution](transform-vmware-ms-wave-execution.md) – Migrate your servers wave by wave, from wave setup through testing and cutover.
+ [Server lifecycle states](transform-vmware-ms-server-lifecycle.md) – Track the state of each server as it moves through the migration.

## Source environments
<a name="transform-vmware-ms-source-environments"></a>

You can migrate servers from virtually any source environment, including on-premises data centers, other cloud providers, or other AWS Regions. AWS Transform supports both physical servers and virtual servers running on VMware, Hyper-V, KVM, or other virtualization platforms. The source infrastructure and hypervisor are not important as long as the source operating system is supported.

## Target environments
<a name="transform-vmware-ms-target-locations"></a>

Use the same workflow to place each workload where it needs to run: in an AWS Region (commercial or AWS GovCloud (US)), in an AWS Local Zone close to your users, or on premises on AWS Outposts. For the list of supported target Regions, see [Supported target Regions](transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions). For more information about Local Zones and Outposts, see [Replicating to AWS Local Zones](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#local-zone-snapshots) and [Migrating to AWS Outposts](https://docs.aws.amazon.com/mgn/latest/ug/outposts.html) in the *AWS Transform MGN User Guide*.

When you migrate to an AWS Local Zone or an Outpost, set up the following:
+ **Connector** – Create the connector in the parent AWS Region of the Local Zone or Outpost. For more information, see [Step 3: Connector configuration](transform-vmware-connect-target-account.md#transform-vmware-cta-connector).
+ **Target subnet** – In the migration inventory file, specify a subnet on the Local Zone or Outpost. For more information, see [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md).
+ **Staging area subnet** – Choose the subnet where replication servers run. The right choice depends on the target, as described in the following sections. For more information, see [Step 4: Data replication](transform-vmware-ms-data-replication.md).

### Local Zones
<a name="transform-vmware-ms-target-local-zones"></a>

For a Local Zone, we recommend that you specify a subnet in the parent AWS Region as your staging area subnet, and a subnet on the Local Zone as your target subnet. Support for storing snapshots in the Local Zone depends on the Local Zone. For more information, see [Replicating to AWS Local Zones](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#local-zone-snapshots) in the *AWS Transform MGN User Guide*.

### Outposts
<a name="transform-vmware-ms-target-outposts"></a>

For an Outpost, specify a subnet on the Outpost as your staging area subnet. MGN requires that the target subnet is on the same Outpost as the staging area subnet. You can't launch to a different Outpost or outside the Outpost.

Also consider the following:
+ AWS Transform supports AWS Outposts racks only, not Outposts servers.
+ AWS Transform instance type recommendations don't account for the instance types that are available on your Outpost. Review the recommended instance types in the migration inventory file, and change any that your Outpost doesn't offer.

For more information, see the following topics in the *AWS Transform MGN User Guide*:
+ [Replication settings for Outposts](https://docs.aws.amazon.com/mgn/latest/ug/outposts.html#outposts-replication-settings)
+ [Launch settings for Outposts](https://docs.aws.amazon.com/mgn/latest/ug/outposts.html#outposts-launch-settings)
+ [Permissions for Outposts](https://docs.aws.amazon.com/mgn/latest/ug/outposts.html#outposts-permissions)
+ [Considerations and constraints](https://docs.aws.amazon.com/mgn/latest/ug/outposts.html#outposts-considerations)

## Deployment approvals
<a name="transform-vmware-ms-approvals"></a>

AWS Transform includes built-in approval workflows to ensure production changes go through your organization's review process. When an operation requires approval, AWS Transform routes the request to authorized approvers through the Approvals tab. Only users with the Admin role in AWS Transform can approve deployment requests. Deployments proceed only after receiving confirmation.