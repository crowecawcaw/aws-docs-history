# Working with Multi-AZ DB cluster read replicas for Amazon RDS

A DB cluster read replica is a special type of cluster that you create from a source DB
instance. After you create a read replica, any updates made to the primary DB instance are
asynchronously copied to the Multi-AZ DB cluster read replica. You can reduce the load on your primary DB
instance by routing read queries from your applications to the read replica. Using read
replicas, you can elastically scale out beyond the capacity constraints of a single DB
instance for read-heavy database workloads.

You can also create one or more DB instance read replicas from a Multi-AZ DB cluster. DB instance read
replicas let you scale beyond the compute or I/O capacity of the source Multi-AZ DB cluster by directing
excess read traffic to the read replicas. Currently, you can't create a Multi-AZ DB cluster read replica
from an existing Multi-AZ DB cluster.

When choosing between migrating to a Multi-AZ DB cluster using a read replica or creating a DB instance
read replica from a Multi-AZ DB cluster, consider your specific use case and performance
requirements.

**Migrating to a Multi-AZ DB cluster using a read replica**

This approach is ideal when you need to enhance the availability and durability of your database while
minimizing downtime. By using a read replica to transition to a Multi-AZ DB cluster, you can ensure
continuous operation and data consistency. This method is particularly useful for production
environments where maintaining availability and reducing impact on live workloads are
critical.

**Creating a DB instance read replica from a Multi-AZ DB cluster**

This method is suitable when you want to scale read operations or offload read traffic from your
primary database instance. By creating a read replica from an existing Multi-AZ DB cluster, you can
distribute read-heavy workloads and improve performance without affecting the primary
instance's stability.

Choosing the right approach depends on whether your priority is to ensure high
availability and durability or to scale read performance. Evaluate your workload
characteristics and operational requirements to make an informed decision.

###### Topics

- [Migrating to a Multi-AZ DB cluster using a read replica](multi-az-db-clusters-migrating-to-with-read-replica.md "multi-az-db-clusters-migrating-to-with-read-replica.md")
- [Creating a DB instance read replica from a Multi-AZ DB cluster](multi-az-db-clusters-create-instance-read-replica.md "multi-az-db-clusters-create-instance-read-replica.md")
