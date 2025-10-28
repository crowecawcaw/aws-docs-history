# ADVREL03-BP03 Configure databases to span across multiple Availability Zones

Explore database configuration strategies for reliability and
disaster recovery, such as periodic snapshots to warm standby
solutions. Evaluate trade-offs between single-AZ and multi-AZ
deployments, costs considerations, and specific recovery time
objectives (RTO).

## Implementation guidance

Carefully consider the trade-offs between disaster recovery
strategies when configuring databases in multi-AZ and single-AZ
deployments. While multi-AZ deployments offer high availability,
they can incur significant cross-AZ data transfer costs.

For cost-sensitive workloads, consider implementing a single-AZ
database cluster with the following resilience strategies:

1. **Periodic snapshots:**
   Implement frequent automated snapshots of your database.
   This approach provides point-in-time recovery capabilities
   with a relatively low RTO, typically in the range of 15-60
   minutes, depending on the database size and recovery
   process.
2. **Read replicas:** Deploy
   read replicas in a different Availability Zone. While this
   incurs some cross-AZ data transfer costs, it's generally
   less expensive than a full multi-AZ deployment. In case of a
   primary Availability Zone failure, promote the read replica
   to become the new primary. This can reduce RTO to between
   five and 15 minutes.
3. **Cold standby:** Maintain a
   stopped database instance in another Availability Zone, and
   periodically update it with snapshots. This approach
   balances cost and recovery time, with an RTO of
   approximately 10-30 minutes.

For mission-critical applications, where minimal downtime is
essential, consider:

1. **Warm standby:** Keep an
   active, scaled-down secondary database in another
   Availability Zone continuously updated using asynchronous
   replication. This approach offers a lower RTO (between one
   and five minutes), but at a higher cost than cold standby.

Choose the strategy that best aligns with your specific RTO
requirements and budget constraints. Implement and regularly
test your chosen disaster recovery process to verify that it
meets your RTO targets.

For AdTech customers who require multi-region deployment for
global resilience, use services like Amazon Aurora Global
Database or Amazon DynamoDB global tables. These services
provide Region-wide resilience with minimal impact on
performance and manageable costs.

Regularly review and optimize your database architecture as your
workload and requirements evolve. Always weigh the costs of
potential downtime against the ongoing expenses of more
resilient configurations.

## Key AWS services

- [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")
  provides a Multi-AZ deployment option
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/")
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/")

## Resources

- [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/ "https://aws.amazon.com/rds/features/multi-az/")
- [Protect
  critical workload with Pod Disruption Budgets](../../../eks/latest/best-practices/application.md#_recommendations_3 "../../../eks/latest/best-practices/application.md#_recommendations_3")
- [Using
  Amazon Aurora Global Database](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database.md")
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/ "https://aws.amazon.com/dynamodb/global-tables/")
- [What
  is Amazon Relational Database Service (Amazon RDS)?](../../../AmazonRDS/latest/UserGuide/Welcome.md "../../../AmazonRDS/latest/UserGuide/Welcome.md")
- [Multi-AZ
  DB instance deployments for Amazon RDS](../../../AmazonRDS/latest/UserGuide/Concepts.md "../../../AmazonRDS/latest/UserGuide/Concepts.md")
