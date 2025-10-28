# Deploying a cluster

Creating a new DAX cluster requires configurations beyond those needed for DynamoDB. These configurations are particularly for networking because DAX is based on [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md"). This gives you complete control over your virtual networking environment, including resource placement, connectivity, and security. This section presents the best practices for the settings needed during cluster creation.

For information about choosing cluster nodes, see [Sizing your DAX cluster](dax-cluster-sizing.md "dax-cluster-sizing.md").

###### In this section

- [Configure networks](#dax-cluster-config-network "#dax-cluster-config-network")
- [Configure security](#dax-cluster-config-security "#dax-cluster-config-security")
- [Parameter group](#dax-cluster-parameter-group "#dax-cluster-parameter-group")
- [Maintenance window](#dax-cluster-maintenance-window "#dax-cluster-maintenance-window")

## Configure networks

DAX uses a [subnet group](DAX.concepts.md#DAX.concepts.cluster.security "DAX.concepts.md#DAX.concepts.cluster.security") to determine which Availability Zones it can run nodes in and which IP addresses to use from the subnets. To minimize latency between your application and DAX, the subnets and Availability Zones for your application servers and the DAX cluster should be the same.

We recommend that you spread the DAX nodes across multiple Availability Zones. The default option of Automatic allocation does this for you.

For best practices about setting up your VPC, see [Get started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the _Amazon VPC User Guide_.

## Configure security

This section discusses the security measures that you should implement for your applications that use DAX. This section also briefly discusses the support that DAX includes for data encryption.

###### IAM

DAX and DynamoDB have separate [access control](DAX.md "DAX.md") mechanisms. DAX requires an IAM role to access your DynamoDB tables. This role should follow the principle of least privilege and grant access only to specific tables and DynamoDB operations, such as [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md") and [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md"). For more information about the access control mechanisms provided by DAX, see [DAX access control](DAX.md "DAX.md").

###### Encryption

You configure encryption at rest and encryption in transit while creating a DAX cluster. These are enabled by default. We recommend that you keep the default encryption settings unless business requirements prevent it. For more information, see [DAX encryption at rest](DAXEncryptionAtRest.md "DAXEncryptionAtRest.md") and [DAX encryption in transit](DAXEncryptionInTransit.md "DAXEncryptionInTransit.md").

## Parameter group

DAX applies a set of configurations on every node in a cluster called a [parameter group](../APIReference/API_dax_ParameterGroup.md "../APIReference/API_dax_ParameterGroup.md"). You can change this configuration after creating the cluster.

The DAX parameter group holds TTL settings for item cache and query cache. By default, the TTL duration is 5 minutes. You can override the TTL duration to any integer value greater than or equal to 1 millisecond.

You can't modify parameter groups when a running DAX instance is using them. You can change the parameter group values during the downtime of a DAX cluster.

## Maintenance window

To allow for occasional software upgrades and patches to your nodes, a weekly [maintenance window](DAX.concepts.md#DAX.concepts.maintenance-window "DAX.concepts.md#DAX.concepts.maintenance-window") is configured for the DAX cluster. During this window, DAX performs rolling updates to the nodes. Clusters with more than one node don't lose availability of the cluster during these updates, but have reduced cluster capacity until the node returns. If your organization has a predictable time of low usage, consider setting the maintenance window manually to this time.
