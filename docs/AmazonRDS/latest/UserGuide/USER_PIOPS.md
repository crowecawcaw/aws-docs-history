# I/O-intensive storage modifications

Amazon RDS DB instances use Amazon Elastic Block Store (EBS) volumes for database and log storage. Depending on the amount of storage requested, RDS
(except for RDS for SQL Server) automatically _stripes_ across multiple Amazon EBS volumes to enhance performance. RDS DB
instances with SSD storage types are backed by either one or four striped Amazon EBS volumes in a RAID 0 configuration. By design,
storage modification operations for an RDS DB instance have minimal impact on ongoing database operations.

In most cases, storage scaling modifications are completely offloaded to the Amazon EBS layer and are transparent to the database.
This process is typically completed within a few minutes. However, some older RDS storage volumes require a different process
for modifying the size, Provisioned IOPS, or storage type. This involves making a full copy of the data using a potentially
I/O-intensive operation.

Storage modification uses an I/O-intensive operation if any of the following factors apply:

- The source storage type is magnetic. Magnetic storage doesn't support elastic volume modification.
- The RDS DB instance isn't on a one- or four-volume Amazon EBS layout. You can view the number of Amazon EBS volumes in use
  on your RDS DB instances by using Enhanced Monitoring metrics. For more information, see [Viewing OS metrics in the RDS console](USER_Monitoring.OS.md "USER_Monitoring.OS.md").
- The target size of the modification request increases the allocated storage above 400 GiB for RDS for MariaDB, MySQL, and
  PostgreSQL instances, and 200 GiB for RDS for Oracle. Storage autoscaling operations have the same effect when they increase
  the allocated storage size of your DB instance above these thresholds.
  If your storage modification involves an I/O-intensive operation, it consumes I/O resources and increases the load on your DB
  instance. Storage modifications with I/O-intensive operations involving General Purpose SSD (gp2) storage can deplete your I/O
  credit balance, resulting in longer conversion times.

We recommend as a best practice to schedule these storage modification requests outside of peak hours to help reduce the time
required to complete the storage modification operation. Alternatively, you can create a read replica of the DB instance and
perform the storage modification on the read replica. Then promote the read replica to be the primary DB instance. For more
information, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

For more information, see [Why is an
Amazon RDS DB instance stuck in the modifying state when I try to increase the allocated storage?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-stuck-modifying/ "https://aws.amazon.com/premiumsupport/knowledge-center/rds-stuck-modifying/")
