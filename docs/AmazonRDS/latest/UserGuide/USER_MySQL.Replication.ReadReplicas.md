# Working with Multi-AZ read replica deployments with MySQL

You can create a read replica from either single-AZ or Multi-AZ DB instance deployments.
You use Multi-AZ deployments to improve the durability and availability of critical
data, but you can't use the Multi-AZ secondary to serve read-only queries. Instead,
you can create read replicas from high-traffic Multi-AZ DB instances to offload
read-only queries. If the source instance of a Multi-AZ deployment fails over to the
secondary, any associated read replicas automatically switch to use the secondary
(now primary) as their replication source. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

You can create a read replica as a Multi-AZ DB instance. Amazon RDS creates a standby of your
replica in another Availability Zone for failover support for the replica. Creating
your read replica as a Multi-AZ DB instance is independent of whether the source
database is a Multi-AZ DB instance.
