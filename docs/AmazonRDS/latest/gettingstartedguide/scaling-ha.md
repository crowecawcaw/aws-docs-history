

# Scaling and high availability in Amazon RDS
<a name="scaling-ha"></a>

Scaling and high availability are important aspects of managing your Amazon RDS DB instance to meet changing application requirements. Scaling helps your database handle increased workloads, while high availability ensures minimal disruption during unexpected failures or maintenance events. 

This topic highlights features such as instance resizing, read replicas, and Multi-AZ deployments to improve performance and resilience.

**Topics**
+ [Changing instance sizes to adjust for demand](#changing-instances)
+ [Adding read replicas for load distribution](#read-replicas)
+ [Enabling Multi-AZ for high availability](#multi-az)

## Changing instance sizes to adjust for demand
<a name="changing-instances"></a>

With Amazon RDS, you can scale vertically by modifying your DB instance size to meet your performance and capacity requirements. Resizing an instance helps accommodate changes in application demand, such as increased traffic or computational needs.

To change the instance size for your DB instance, navigate to the DB instance details page in the AWS Management Console and choose **Modify**. For the **Instance configuration**, choose a new instance class that aligns with your requirements, such as compute optimized or memory optimized. 

![Instance configuration section showing DB instance class filters and db.t4g.micro selection.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/size-change.png)


Apply changes during a maintenance window or immediately, depending on your application’s tolerance for downtime.

**Key considerations**:
+ Make sure the instance class that you choose supports your storage and workload requirements.
+ Larger instance sizes often come with increased costs, so evaluate your budget before scaling.

For comprehensive documentation, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide*.

## Adding read replicas for load distribution
<a name="read-replicas"></a>

Amazon RDS provides horizontal scaling by using read replicas to offload read-intensive workloads and improve database performance. Read replicas are copies of your primary database that asynchronously replicate data. They’re ideal for scaling read-heavy applications and improving response times. Read replicas distribute read traffic across multiple instances, and provide additional redundancy for disaster recovery scenarios.

To create a read replica for an existing DB instance, select it within the AWS Management Console. From the **Actions** menu, choose **Create read replica**, then configure the instance class and AWS Region for the replica. Launch the replica and update your application to direct read traffic accordingly.

**Key considerations**:
+ Read replicas are read-only and can't handle write operations.
+ Replicas might introduce minor latency due to asynchronous replication.

For comprehensive documentation, see [Working with DB instance read replicas ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) in the *Amazon RDS User Guide*.

## Enabling Multi-AZ for high availability
<a name="multi-az"></a>

Multi-AZ deployments provide high availability and durability by automatically maintaining a synchronous standby replica in a different Availability Zone. Multi-AZ deployments minimize downtime during planned maintenance or infrastructure failure by automatically failing over to the standby replica. 

To create a Multi-AZ DB instance, select **Multi-AZ DB instance** under **Availability and durability** when you create the DB instance. Amazon RDS handles data replication and failover management transparently.

![Three deployment options showing Multi-AZ cluster, Multi-AZ instance, and Single-AZ configurations.](http://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/images/multi-az.png)


**Key considerations**:
+ Multi-AZ deployments increase storage requirements, which might impact storage costs and capacity planning.
+ Failover between Availability Zones might result in a brief interruption, so configure your applications to handle reconnections.

For comprehensive documentation, see [Multi-AZ DB instance deployments for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html) in the *Amazon RDS User Guide*.