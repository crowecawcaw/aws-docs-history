

# Resource sharing in Oracle Database@AWS
<a name="resource-sharing"></a>

With Oracle Database@AWS, you can share Exadata infrastructure and your ODB network across multiple AWS accounts in the same AWS organization. This enables you to provision infrastructure once and reuse it across trusted accounts, allowing you to reduce costs while separating responsibilities.

When you share resources:
+ The account that owns the resource (owner account) maintains control over the resource lifecycle.
+ Accounts that receive access to shared resources (trusted accounts) can view and use these resources based on the permissions granted.
+ Trusted accounts can create their own resources on shared infrastructure but cannot delete the underlying shared resources.

## Oracle Database@AWS integration with AWS RAM
<a name="odb-ram"></a>

Oracle Database@AWS uses AWS Resource Access Manager (AWS RAM) to enable secure, controlled sharing of resources across accounts. With AWS RAM, you can securely share your Oracle Database@AWS resources across multiple AWS accounts within the same AWS organization. AWS RAM simplifies resource sharing, reduces operational overhead, and provides security and visibility into shared Oracle Database@AWS resources. 

With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the AWS accounts with whom to share them.

## Benefits of resource sharing in Oracle Database@AWS
<a name="resource-sharing-benefits"></a>

Sharing Oracle Database@AWS resources across accounts provides the following benefits:
+ **Cost optimization** – Provision expensive Exadata infrastructure once through an administrative account and share it with multiple accounts, reducing overall costs.
+ **Separation of responsibilities** – Maintain clear boundaries between infrastructure administrators and database users while allowing collaboration.
+ **Simplified management** – Centralize infrastructure provisioning and management while enabling distributed database operations.
+ **Consistent governance** – Apply consistent policies and controls across shared resources.

For example, an administrator can provision the Oracle Exadata infrastructure and ODB network in their AWS account and share it with developer accounts. Developers can then create VM clusters on this shared infrastructure without needing to provision their own expensive hardware. This approach significantly reduces costs while maintaining proper separation of responsibilities between accounts.

## How resource sharing works in Oracle Database@AWS
<a name="resource-sharing-how-it-works"></a>

You can share the following Oracle Database@AWS resources:
+ Oracle Exadata infrastructure
+ ODB network

Oracle Database@AWS shares the preceding resources through the following process:

1. The buyer account (the account that accepts the Oracle Database@AWS private offer or public offer via AWS Marketplace) provisions Oracle Database@AWS resources, such as Exadata infrastructure and an ODB network.

1. The buyer account creates a resource share using AWS RAM, specifying the resources to share and the trusted accounts to share them with.

1. The resource shares for the trusted accounts within the same organization are accepted automatically.

1. Before using shared resources, trusted accounts must initialize the Oracle Database@AWS service in their account by using the `aws odb initialize-service` command or by choosing **Activate account** in the Oracle Database@AWS console.

1. After initialization, trusted accounts can create their own resources on the shared infrastructure, such as VM clusters on shared Exadata infrastructure and ODB network.

## Permissions on shared resources for trusted accounts
<a name="managed-permissions"></a>

When you share resources, Oracle Database@AWS automatically selects specific actions (managed permissions) for each resource type:

**For Exadata infrastructure**  
Oracle Database@AWS grants the following permissions to trusted accounts:  
+ `odb:CreateCloudVmCluster`
+ `odb:CreateCloudAutonomousVmCluster`
+ `odb:GetCloudExadataInfrastructure`
+ `odb:ListCloudExadataInfrastructures`
+ `odb:GetCloudExadataInfrastructureUnallocatedResources`
+ `odb:ListDbServers`
+ `odb:GetDbServer`
+ `odb:ListCloudVmClusters`
+ `odb:ListCloudAutonomousVmClusters`

**For ODB network**  
The following permissions are granted to trusted accounts:  
+ `odb:CreateCloudVmCluster`
+ `odb:CreateCloudAutonomousVmCluster`
+ `odb:GetOdbNetwork`
+ `odb:ListOdbNetworks`
+ `odb:CreateOdbPeeringConnection`
+ `odb:ListOdbPeeringConnections`

Resource sharing respects the hierarchical nature of Oracle Database@AWS resources. For example, if you share Exadata infrastructure, trusted accounts can create VM clusters on this infrastructure, but they can't modify or delete the Exadata infrastructure itself.

When a resource is unshared, trusted accounts lose the ability to create new resources on the shared infrastructure. However, any resources they've already created remain accessible and functional.

## Limitations for Oracle Database@AWS resource sharing
<a name="resource-sharing-considerations"></a>

Before sharing resources, keep the following limitations in mind.

### Limitations for sharing resources
<a name="limitations-sharing"></a>

When sharing Oracle Database@AWS resources, keep in mind the following limitations:
+ You can share resources only with AWS account IDs.
+ You can share resources only for AWS accounts within the same AWS organization.
+ You share resources within a specific AWS Region. To share resources across Regions, you must create separate resource shares in each Region.
+ When you create a resource share, the actions (managed permissions) for each resource type are automatically selected and can't be modified.
+ You can't use Oracle Database@AWS as a resource and share with other AWS accounts.
+ A trusted account can use shared resources from only one buyer account (from one private offer or one public offer). Thus, two buyer accounts can't share resources with the same trusted account. However, a grantee account that received an entitlement share from the buyer account can also share its own resources with the same trusted account. For more information about entitlement sharing, see [Sharing Oracle Database@AWS entitlements with another account using AWS License Manager](sharing-entitlement-task.md#sharing-entitlements).
+ A buyer account can't share resources with another buyer account.
+ Resources shared with a trusted account must be shared by the buyer account in the buyer's [home region](https://docs.oracle.com/en/cloud/foundation/cloud_architecture/governance/regions.html#home-region) first.
+ When you unshare a resource, we recommend that you wait approximately 15 minutes before resharing the same resource with the same trusted account.

### Limitations for creating and using shared resources
<a name="limitations-creating"></a>

When creating or using Oracle Database@AWS resources, keep in mind the following limitations:
+ Only the buyer account can create Exadata infrastructure and ODB network resources. The buyer account is the one that accepts the Oracle Database@AWS offer.
+ Trusted accounts can create resources only on Exadata infrastructure shared by the buyer account. Both Exadata infrastructure and the ODB network must be shared for a trusted account to create a VM cluster.
+ Trusted accounts can view and manage only their own VM clusters on shared Exadata infrastructure. They can't see VM clusters that other trusted accounts created on the same Exadata infrastructure.
+ Trusted accounts must initialize the Oracle Database@AWS service in their account before they can use shared resources.

### Limitations for deleting shared resources
<a name="limitations-deleting"></a>
+ You can't delete Exadata infrastructure that has VM clusters created by trusted accounts until those VM clusters are removed.
+ You can't delete an ODB network that has an ODB peering connection created by a trusted account until the ODB peering connection has been removed.
+ The buyer account can't delete Oracle Database@AWS resources created by trusted accounts.
+ Trusted accounts can view shared resources but can't modify or delete Oracle Database@AWS resources owned by the buyer account.