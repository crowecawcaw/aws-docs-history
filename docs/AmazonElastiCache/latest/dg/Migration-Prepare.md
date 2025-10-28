# Preparing your source and target for migration

With these steps you can prepare to migrate your data from a self-hosted Valkey or Redis source on EC2 to ElastiCache, or from a Redis OSS cluster to an ElastiCache Valkey cluster.

This refers to migration from a self-hosted instance to the ElastiCache service. For information on upgrading from Redis OSS to Valkey on ElastiCache see [Upgrading engine versions including cross engine
upgrades](VersionManagement.md "VersionManagement.md").

You must ensure that all four of the prerequisites mentioned following are satisfied
before you start the migration from ElastiCache console, API or AWS CLI.

###### To prepare your source and target Valkey or Redis OSS Nodes for migration

1. Identify the target ElastiCache deployment and make sure that you can migrate data
   to it.

An existing or newly created ElastiCache deployment should meet the following
requirements for migration:

    * It is using Valkey, or Redis OSS 5.0.6 or higher.
    * It doesn't have encryption in-transit enabled.
    * It has Multi-AZ enabled.
    * It has sufficient memory available to fit the data from your Valkey or Redis OSS cluster. To configure the right reserved memory settings, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").
    * For cluster-mode disabled, you can migrate directly from Valkey or Redis OSS versions
     2.8.21 onward to Valkey or Redis OSS version 5.0.6 onward if are using the CLI or
     Valkey or Redis OSS versions 5.0.6 onward using the CLI or console. For cluster
     mode enabled, you can migrate directly from any cluster-mode enabled Valkey or Redis OSS version
     to Redis OSS version 5.0.6 onward, if are using the CLI or Redis OSS versions
     5.0.6 onward using the CLI or console.
    * Number of shards in source and target match.
    * It is not part of a global datastore.
    * It has data tiering disabled.

2. Make sure that the configurations of your open-source Valkey or Redis OSS and the ElastiCache deployment are
   compatible.

At a minimum, all the following in the target ElastiCache deployment should be
compatible with your Valkey or Redis OSS configuration for replication:

    * Your cluster should not have AUTH enabled.
    * The config `protected-mode` should be set to
     `no`.
    * If you have `bind` configuration in your Valkey or Redis OSS config, then
     it should be updated to allow requests from ElastiCache nodes.
    * The number of logical databases should be the same on the ElastiCache node
     and your Valkey or Redis OSS cluster. This value is set using `databases`
     in the Valkey or Redis OSS config.
    * Valkey or Redis OSS commands that perform data modification should not be renamed to
     allow replication of the data to succeed. for example `sync`,
     `psync`, `info`, `config`,
     `command`, and `cluster`.
    * To replicate the data from your Valkey or Redis OSS cluster to ElastiCache, make sure that
     there is sufficient CPU and memory to handle this additional load. This
     load comes from the RDB file created by your Valkey or Redis OSS cluster and
     transferred over the network to ElastiCache node.
    * All Valkey or Redis OSS instances in the source cluster should be running on the
     same port.

3. Make sure that your instances can connect with ElastiCache by doing the
   following:
   - Ensure that each instance's IP address is private.
   - Assign or create the ElastiCache deployment in the same virtual private
     cloud (VPC) as your Valkey or Redis OSS on your instance (recommended).
   - If the VPCs are different, set up VPC peering to allow access between
     the nodes. For more information on VPC peering, see [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md "elasticache-vpc-accessing.md").
   - The security group attached to your Valkey or Redis OSS instances should allow
     inbound traffic from ElastiCache nodes.

4. Make sure that your application can direct traffic to ElastiCache nodes after
   migration of data is complete. For more information, see [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md "elasticache-vpc-accessing.md").
