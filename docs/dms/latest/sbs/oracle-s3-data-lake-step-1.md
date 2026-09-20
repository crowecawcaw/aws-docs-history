

# Step 1: Create an AWS DMS Replication Instance
<a name="oracle-s3-data-lake-step-1"></a>

An AWS DMS replication instance hosts the software migrates data between the source and target. The replication instance also caches the transaction logs during the migration. The CPU and memory capacity of the replication instance influences the overall time needed for the migration. Make sure that you consider the specifics of your particular use case when you determine the size of your replication instance. A full load task consumes a lot of memory if it is run multithreaded. For more information, see [Choosing the right replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html).

For our use case, we have a limited time window of 8 hours to complete the full load, and the sales table that includes 197 GB of data. Our goal is to fit into the 8 hour window. Therefore, we scale the replication instance to accommodate these requirements.

Each type of instance class has different CPU, memory, and I/O capacity. Sizing the replication instance should be based on factors like data volume, transaction frequency, large objects (LOBs) within storage of the data migration, and so on. We initially chose a DMS t3.medium instance running the latest AWS DMS engine version. This instance completed the migration in 18 hours. We then upgraded to a DMS c5.12xlarge instance. This instance size, combined with the proper task configuration, brought the full load time to under 8 hours.

We also upgraded the storage of the replication instance to 200 GB, and as a result, 600 IOPS were available for our replication instance. By default, DMS allocates 50 GB of storage to a replication instance. This may not be sufficient for use cases where more tasks are running on same replication instance or when running tasks with parallel load for large tables. With 600 IOPS, we saved several minutes of migration time. For more information about storage volume performance and burst I/O credits, see [General Purpose SSD (gp2) volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html#EBSVolumeTypes_gp2).

Because we replicate production data in this walkthrough, we use the Multi-AZ deployment option for our replication instance for high availability. Also, we didn’t make this replication instance publicaly accessible for additional security.

For information about best practices for using AWS DMS, see [Database Migration Service Best Practices](https://d0.awsstatic.com/whitepapers/RDS/AWS_Database_Migration_Service_Best_Practices.pdf).

 **To create an AWS DMS replication instance** 

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2).

1. Choose **Replication instances**, then choose **Create replication instance**.

1. On the **Create replication instance** page, enter the following information.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>Enter <code>oracle-s3-migration-replication-instance</code>. If you use multiple replication servers or sharing a user, choose a name that helps you quickly differentiate between the different servers.</td></tr>
  <tr><td> <b>Description</b> </td><td>Enter <code>Replication instance that suports Oracle to S3 data lake migration</code>. You can change the description to fit your use case.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>Choose <code>dms.c5.12xlarge</code>.</td></tr>
  <tr><td> <b>VPC</b> </td><td>Choose the virtual private cloud (VPC) where AWS DMS launches your replication instance. If possible, select the same VPC in which either your source or target database resides (or both).</td></tr>
  <tr><td> <b>Multi AZ</b> </td><td>Choose <b>Yes</b>.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>Turn off this option.</td></tr>
</tbody>
</table>


1. Choose **Create**.