# ADVPERF04-BP03 Review your distributed database setup (sharding and replication) for performance, cost, and availability needs

Customers need to consider tradeoffs between performance, cost,
and availability needs, while using features like sharding for
scaling and replication for availability requirements.

## Implementation guidance

Use availability zone affinity in Aerospike to allow client
applications to access Aerospike nodes in the same zone, which
optimizes data transfer across zones.

Distributed databases often support data partitioning or
sharding, which allows you to split your data across multiple
nodes or clusters. This can help distribute the load and optimize cost by reducing the need for high-performance instances or storage
solutions for the entire dataset.

Carefully plan your data replication strategy across
Availability Zones. While replication provides high availability
and durability, replicating data across multiple Availability
Zones can increase costs. Consider replicating only the
essential data or implementing read replicas in different
Availability Zones while keeping the primary node in a single
Availability Zone.

## Key AWS services

- [Amazon RDS](https://aws.amazon.com/rds "https://aws.amazon.com/rds")

## Resources

- [Architecture
  II: Distributed Data Stores](https://aws.amazon.com/blogs/startups/distributed-data-stores-for-mere-mortals/ "https://aws.amazon.com/blogs/startups/distributed-data-stores-for-mere-mortals/")
- [Building globally distributed MySQL applications using write
  forwarding in Amazon Aurora Global Database](https://aws.amazon.com/blogs/database/building-globally-distributed-mysql-applications-using-write-forwarding-in-amazon-aurora-global-database/ "https://aws.amazon.com/blogs/database/building-globally-distributed-mysql-applications-using-write-forwarding-in-amazon-aurora-global-database/")
- [Amazon Ads Architecture at Scale - ReInvent 2021](https://www.youtube.com/watch?v=YRbIAmzFxxc "https://www.youtube.com/watch?v=YRbIAmzFxxc")
