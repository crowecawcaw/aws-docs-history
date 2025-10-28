# Step 1: Create an AWS DMS Replication Instance

To create an AWS Database Migration Service (AWS DMS) replication instance, see [Creating a replication instance](../userguide/CHAP_ReplicationInstance.md "../userguide/CHAP_ReplicationInstance.md"). Usually, the full load phase is multi-threaded (depending on task configurations) and has a greater resource footprint than ongoing replication. Consequently, it’s advisable to start with a larger instance class and then scale down once the task is in the ongoing replication phase. Moreover, if you intend to migrate your workload using multiple tasks, monitor your replication instance metrics and re-size your instance accordingly.

For this use case, we will migrate a subset (the Sales schema) of the `AdventureWorks` database, which is over 3 GB in size. Because we perform a heterogenous migration without many LOB columns, we can start with a compute optimized instance like c5.xlarge running the latest AWS DMS engine version. We can later scale up or down based on resource utilization during task execution.

###### Note

Scaling replication instance during full load and ongoing replication phases is usually based on CloudWatch metrics such as CPU, memory, I/O, and so on. Choosing the appropriate replication instance class and size depends on several factors such as number of tasks, table size, DML activity, size of transactions, Large Objects (LOB), and so on. This is out of scope for this walkthrough. To learn more about these topics, see [Choosing replication instance types](../userguide/CHAP_ReplicationInstance.md "../userguide/CHAP_ReplicationInstance.md") and [Sizing a replication instance](../userguide/CHAP_BestPractices.md "../userguide/CHAP_BestPractices.md").

To create an AWS DMS replication instance, do the following:

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2").
2. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM permissions](../userguide/CHAP_Security.md#CHAP_Security.IAMPermissions "../userguide/CHAP_Security.md#CHAP_Security.IAMPermissions").
3. On the Welcome page, choose **Create replication instance** to start a database migration.
4. On the **Create replication instance** page, specify your replication instance information.

| For This Parameter          | Do This                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **Name**                    | Enter `datalake-migration-ri`. If you are using multiple replication servers or sharing a user, choose a name that helps you quickly differentiate between the different servers.         |
| **Description**             | Enter `Migrate SQL Server to Amazon S3 data lake`.                                                                                                                                        |
| **Instance class**          | Choose `dms.c5.xlarge`. Each size and type of instance class has increasing CPU, memory, and I/O capacity.                                                                                |
| **Engine version**          | Leave the default value, which is the latest stable version of the AWS DMS replication engine.                                                                                            |
| **Allocated storage (GiB)** | Choose `50`.                                                                                                                                                                              |
| **VPC**                     | Choose the virtual private cloud (VPC) in which your replication instance will launch. If possible, select the same VPC in which either your source or target database resides (or both). |
| **Multi AZ**                | If you choose **Yes**, AWS DMS creates a second replication server in a different Availability Zone for failover if there is a problem with the primary replication server.               |
| **Publicly accessible**     | If either your source or target database resides outside of the VPC in which your replication server resides, you must make your replication server policy publicly accessible.           | 5. Choose **Create**. |
