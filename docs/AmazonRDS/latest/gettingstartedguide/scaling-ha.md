# Scaling and high availability in Amazon RDS

Scaling and high availability are important aspects of managing your Amazon RDS DB instance to
meet changing application requirements. Scaling helps your database handle increased
workloads, while high availability ensures minimal disruption during unexpected failures or
maintenance events.

This topic highlights features such as instance resizing, read replicas, and Multi-AZ
deployments to improve performance and resilience.

###### Topics

- [Changing instance sizes to adjust for demand](#changing-instances "#changing-instances")
- [Adding read replicas for load distribution](#read-replicas "#read-replicas")
- [Enabling Multi-AZ for high availability](#multi-az "#multi-az")

## Changing instance sizes to adjust for demand

With Amazon RDS, you can scale vertically by modifying your DB instance size to meet your
performance and capacity requirements. Resizing an instance helps accommodate changes in
application demand, such as increased traffic or computational needs.

To change the instance size for your DB instance, navigate to the DB instance details
page in the AWS Management Console and choose **Modify**. For the **Instance
configuration**, choose a new instance class that aligns with your requirements,
such as compute optimized or memory optimized.

![Instance configuration options showing burstable classes selected with db.t4g.micro specs.](images/size-change.png)

Apply changes during a maintenance window or immediately, depending on your
application’s tolerance for downtime.

**Key considerations**:

- Make sure the instance class that you choose supports your storage and workload
  requirements.
- Larger instance sizes often come with increased costs, so evaluate your budget
  before scaling.

For comprehensive documentation, see [DB instance classes](../UserGuide/Concepts.md "../UserGuide/Concepts.md")
in the _Amazon RDS User Guide_.

## Adding read replicas for load distribution

Amazon RDS provides horizontal scaling by using read replicas to offload read-intensive
workloads and improve database performance. Read replicas are copies of your primary
database that asynchronously replicate data. They’re ideal for scaling read-heavy
applications and improving response times. Read replicas distribute read traffic across
multiple instances, and provide additional redundancy for disaster recovery
scenarios.

To create a read replica for an existing DB instance, select it within the AWS Management Console.
From the **Actions** menu, choose **Create read replica**,
then configure the instance class and AWS Region for the replica. Launch the replica and
update your application to direct read traffic accordingly.

**Key considerations**:

- Read replicas are read-only and can't handle write operations.
- Replicas might introduce minor latency due to asynchronous replication.

For comprehensive documentation, see [Working with DB instance read replicas](../UserGuide/USER_ReadRepl.md "../UserGuide/USER_ReadRepl.md") in the _Amazon RDS User Guide_.

## Enabling Multi-AZ for high availability

Multi-AZ deployments provide high availability and durability by automatically
maintaining a synchronous standby replica in a different Availability Zone. Multi-AZ
deployments minimize downtime during planned maintenance or infrastructure failure by
automatically failing over to the standby replica.

To create a Multi-AZ DB instance, select **Multi-AZ DB instance** under
**Availability and durability** when you create the DB instance. Amazon RDS
handles data replication and failover management transparently.

![Comparison of three AWS RDS deployment options showing instances, availability zones, and uptime percentages.](images/multi-az.png)

**Key considerations**:

- Multi-AZ deployments increase storage requirements, which might impact storage costs
  and capacity planning.
- Failover between Availability Zones might result in a brief interruption, so
  configure your applications to handle reconnections.

For comprehensive documentation, see [Multi-AZ DB instance deployments for Amazon RDS](../UserGuide/Concepts.md "../UserGuide/Concepts.md") in the _Amazon RDS User
Guide_.
