# Best practices for Aurora MySQL high availability

You can apply the following best practices to improve the availability of your Aurora MySQL clusters.

###### Topics

- [Using Amazon Aurora for
  Disaster Recovery with your MySQL databases](#AuroraMySQL.BestPractices.DisasterRecovery "#AuroraMySQL.BestPractices.DisasterRecovery")
- [Migrating from MySQL to Amazon Aurora MySQL with reduced downtime](#AuroraMySQL.BestPractices.Migrating "#AuroraMySQL.BestPractices.Migrating")
- [Avoiding slow performance, automatic restart, and failover for
  Aurora MySQL DB instances](#AuroraMySQL.BestPractices.Avoiding "#AuroraMySQL.BestPractices.Avoiding")

## Using Amazon Aurora for

Disaster Recovery with your MySQL databases

You can use Amazon Aurora with your MySQL DB instance to create an offsite backup for
disaster recovery. To use Aurora for disaster recovery of your MySQL DB instance, create
an Amazon Aurora DB cluster and make it a read replica of your MySQL DB instance. This
applies to an RDS for MySQL DB instance, or a MySQL database running external to
Amazon RDS.

###### Important

When you set up replication between a MySQL DB instance and an Amazon Aurora MySQL DB
cluster, you should monitor the replication
to ensure that it remains healthy and repair it if necessary.

For instructions on how to create an Amazon Aurora MySQL DB cluster and make it a
read replica of your MySQL DB instance, follow the procedure in
[Using Amazon Aurora to scale reads for
your MySQL database](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.ReadScaling "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.ReadScaling").

For more information on disaster recovery models, see [How to choose the best disaster recovery option for your Amazon Aurora MySQL cluster](https://aws.amazon.com/blogs/database/how-to-choose-the-best-disaster-recovery-option-for-your-amazon-aurora-mysql-cluster/ "https://aws.amazon.com/blogs/database/how-to-choose-the-best-disaster-recovery-option-for-your-amazon-aurora-mysql-cluster/").

## Migrating from MySQL to Amazon Aurora MySQL with reduced downtime

When importing data from a MySQL database that supports a live application to an
Amazon Aurora MySQL DB cluster, you might want to reduce the time that service is interrupted
while you migrate. To do so, you can use the procedure documented in
[Importing data to an Amazon RDS for MySQL DB instance with reduced downtime](../UserGuide/mysql-importing-data-reduced-downtime.md "../UserGuide/mysql-importing-data-reduced-downtime.md")
in the _Amazon Relational Database Service User Guide_. This procedure can
especially help if you are working with a very large database. You can use the procedure
to reduce the cost of the import by minimizing the amount of data that is passed across
the network to AWS.

The procedure lists steps to transfer a copy of your database data to an Amazon EC2
instance and import the data into a new RDS for MySQL DB instance. Because Amazon Aurora is
compatible with MySQL, you can instead use an Amazon Aurora DB cluster for the target Amazon RDS
MySQL DB instance.

## Avoiding slow performance, automatic restart, and failover for

Aurora MySQL DB instances

If you're running a heavy workload or workloads that spike beyond the allocated resources of your DB instance, you can
exhaust the resources on which you're running your application and Aurora database. To get metrics on your database instance
such as CPU utilization, memory usage, and number of database connections used, you can refer to the metrics provided by
Amazon CloudWatch, Performance Insights, and Enhanced Monitoring. For more information on monitoring your DB instance, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md "MonitoringAurora.md").

If your workload exhausts the resources you're using, your DB instance might slow down, restart, or even fail over to
another DB instance. To avoid this, monitor your resource utilization, examine the workload running on your DB instance, and
make optimizations where necessary. If optimizations don't improve the instance metrics and mitigate the resource
exhaustion, consider scaling up your DB instance before you reach its limits. For more information on available DB instance
classes and their specifications, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md").
