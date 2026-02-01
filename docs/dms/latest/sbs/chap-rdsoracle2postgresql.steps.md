# Step 5: Create an AWS DMS Replication Instance

After validating the schema structure between source and target databases, continue with the core part of this walkthrough, which is the data migration. The following illustration shows a high-level view of the migration process.

![Migration process](images/datarep-conceptual2.png)
An AWS DMS replication instance performs the actual data migration between source and target. The replication instance also caches the transaction logs during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration.

1. Sign in to the AWS Management Console, and select AWS DMS at https://console.aws.amazon.com/dms/v2/. Next, choose **Create Migration**. If you are signed in as an AWS Identity and Access Management (IAM) user, then you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM Permissions](../userguide/CHAP_Security.md#CHAP_Security.IAMPermissions "../userguide/CHAP_Security.md#CHAP_Security.IAMPermissions").
2. Choose **Next** to start a database migration from the console’s Welcome page.
3. On the **Create replication instance** page, specify your replication instance information.

| Parameter               | Description                                                                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                | Select a name for your replication instance. If you will be using multiple replication servers or sharing an account, then choose a name that will help you quickly differentiate between the different servers.                                             |
| **Description**         | Enter a brief description.                                                                                                                                                                                                                                   |
| **Instance class**      | Select the type of replication server to create. Each size and type of instance class will have increasing CPU, memory, and I/O capacity. Generally, the `t2` instances are for lower load tasks, and the `c4` instances are for higher load and more tasks. |
| **VPC**                 | Choose the VPC in which your replication instance will be launched. If possible, select the same VPC in which either your source or target database resides (or both).                                                                                       |
| **Multi-AZ**            | When \*_Yes_<br>• is selected, AWS DMS creates a second replication server in a different Availability Zone for failover if there is a problem with the primary replication server.                                                                          |
| **Publicly accessible** | If either your source or target database resides outside of the VPC in which your replication server resides, then you must make your replication server policy publicly accessible.                                                                         |

4. For the **Advanced** section, specify the following information.

| Parameter                    | Description                                                                                                                                                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Allocated storage (GB)**   | Amount of storage on the replication server for the AWS DMS task logs, including historical tasks logs. AWS DMS also uses disk storage to cache certain data while it replicates it from the source to the target. Additionally, more storage generally enables better IOPS on the server. |
| **Replication Subnet Group** | If you are running in a Multi-AZ configuration, then you will need at least two subnet groups.                                                                                                                                                                                             |
| **Availability zone**        | Generally, performance is better if you locate your primary replication server in the same Availability Zone as your target database.                                                                                                                                                      |
| **VPC Security Group(s)**    | Security groups enable you to control ingress and egress to your VPC. AWS DMS allows you to associate one or more security groups with the VPC in which your replication server is launched.                                                                                               |
| **KMS key**                  | With AWS DMS, all data is encrypted at rest using a KMS encryption key. By default, AWS DMS will create a new encryption key for your replication server. However, you may choose to use an existing key.                                                                                  |

For information about the KMS key, see [Setting an Encryption Key and Specifying KMS Permissions](../userguide/CHAP_Security.md "../userguide/CHAP_Security.md"). 5. Click **Next**.
