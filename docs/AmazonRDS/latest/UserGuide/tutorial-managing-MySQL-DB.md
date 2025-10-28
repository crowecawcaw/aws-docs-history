# Tutorial: Managing a MySQL DB instance environment from development to production

## Introduction

A common scenario when managing an Amazon RDS DB instance involves the oversight of its lifecycle from initial development through to production deployment. This tutorial offers guidance to handle key tasks to ensure your database performs optimally and adapts to meet your evolving operational needs. Additionally, it outlines options to synchronize changes made between your development and production environments to ensure consistency and reliability.

By completing these steps, you learn:

- How to perform specific tasks with MySQL DB instances, such as adding and updating Amazon RDS tags, expanding storage, creating read replicas, and deleting resources.
- How to synchronize updates from a production environment to a development environment for comprehensive testing and validation.

To complete this tutorial, carry out the following tasks:

1. Create a MySQL DB instance.
2. Add Amazon RDS tags to categorize your DB instance as a development environment.
3. Increase the storage capacity of your DB instance to accommodate increased workloads.
4. Create read replicas to enhance the resilience and availability of your DB instance.
5. Update Amazon RDS tags to categorize your DB instance as a production environment.
6. Delete DB instance that you no longer need so that they don’t incur additional costs.
7. Next Steps: Synchronize your development instance with production for consistency across environments

## Prerequisites

Before you begin, complete the steps in the following sections:

- [Sign up for an AWS account](CHAP_SettingUp.md#sign-up-for-aws "CHAP_SettingUp.md#sign-up-for-aws")
- [Create a user with administrative access](CHAP_SettingUp.md#create-an-admin "CHAP_SettingUp.md#create-an-admin")

## Add tags to categorize your DB instance as a development environment

To categorize the DB instance as a development environment, add an Amazon RDS tag to the instance you created.
An Amazon RDS tag is a key-value pair that you define and associate with your RDS instance.
Tagging your AWS resources helps distinguish between your development and production AWS resources.
For more information on Amazon RDS tags, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").

1. In the Amazon RDS console, choose **Databases**.
2. Select the DB instance you want to tag.
3. In the details section, scroll to the **Tags** section.
4. Choose **Manage tags** and select**dd new tag**.
5. Enter a value for **Tag key** and **Value**. For instance, you might use the tag key environment with the value dev to specify that the database instance is part of the development environment.
6. Choose **Add new tag**and **Save changes**.

Your DB instance is now tagged as a development environment. This makes it easier to identify the DB instance and to manage costs associated with this resource.

## Increase the storage capacity of a DB instance to accommodate growing data needs

Next, modify the storage capacity of the MySQL DB instance to accommodate additional data.
Initially, the storage capacity of your DB instance is set to meet the immediate needs of your application.
However, as data volumes grow, it might be necessary to adjust the storage settings to ensure the
database’s continued performance and stability. This process involves increasing the allocated storage of your DB instance.
For more information on modifying the storage capacity of your DB instance, see
[Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md").

1. In the Amazon RDS console, choose **Databases**.
2. Select the DB instance you want to modify.
3. Choose **Modify**.
4. In Storage, increase the **Allocated Storage**.
   The modified storage value must be greater than the current one.
5. Choose **Continue**.
6. In **Scheduling of modifications**, you can either choose **Apply immediately**  
   to apply the storage changes to the DB instance immediately or choose
   **Apply during the next scheduled maintenance window** to apply the changes during the next maintenance window.
7. When the settings are as you want them, choose **Modify DB instance**.

The storage capacity of your DB instance is now increased. This enables it to effectively handle larger
data volumes and ensures continued performance and stability as your application's data needs grow.

## Create read replicas to enhance the resilience

and availability of a DB instance

Create a read replica of the MySQL DB instance. Read replicas enhance the resilience and availability of your DB instance.
To reduce the read traffic on your primary DB instance, create a read replica of your DB instance. This routes queries to the read replica,
which can help distribute the load and improve overall database performance. For more information on DB instance read replicas, see
[Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

Before a MySQL DB instance can serve as a replication source, automatic backups must be enabled on the source DB instance.
This can be done by setting the backup retention period to a value other than 0. For more information on MySQL read replicas,
see [Working with MySQL read replicas](USER_MySQL.Replication.md "USER_MySQL.Replication.md").

1. In the Amazon RDS console, choose **Databases**.
2. Select the DB instance you want to use as the source for the read replica.
3. In Actions, select **Create read replica**.
4. For **DB instance identifier**, enter a name for the read replica in all lowercase letters.
5. Choose your instance configuration. We recommend that you use the same or larger DB instance class
   and storage type as the source DB instance for the read replica.
6. For **AWS Region**, specify the destination Region for the read replica.
7. Leave the default settings or modify them as you require.
8. Choose **Create read replica**.

The read replica appears underneath your source DB instance on the **Databases** page in the RDS console.
It shows **Replica** in the Role column.

## Update tags to categorize a DB instance

as a production environment

When your DB instance is ready to move from the development phase to production, it is important to update
its tags to reflect its transition. To align your DB instance with your operational and monitoring
strategies, update the initial tags to indicate that the DB instance is now part of the production
environment. This ensures better visibility and management of the database.

1. In the Amazon RDS console, choose **Databases**.
2. Select the DB instance you want to update
3. In the details section, scroll to the **Tags** section.
4. Select **Manage tags**.
5. **Remove** your initial tag signifying a development environment.
6. Select**Add new tag**.
7. Enter a new value for **Tag key** and **Value**.
   For instance, you might use the tag key environment with the value prod to specify that the
   DB instance is part of the production environment.
8. Choose **Add new tag** and **Save changes**.

The tag on your DB instance is updated to signify the database’s transition to a production environment.

### Delete a DB instance when it is no longer needed to avoid

incurring additional costs

Before the end of this tutorial, it is crucial to address the management of your resources. If you have any resources that are no longer required,
you should proceed to delete them to prevent incurring additional costs and optimize your cloud environment.

1. In the Amazon RDS console, choose **Databases**.
2. Select the DB instance you want to delete
3. In Actions, select **Delete**. Deleting a DB instance will permanently delete the instance
   with all its content and related resources.
4. Confirm the deletion of the DB instance and select **Delete**.

Alternatively, if you choose to maintain your DB instance for future use, you can continue to manage
it as part of your production environment. This involves maintaining a synchronized development environment
to facilitate comprehensive testing and validation. For more information, see
[Next steps: Synchronize your development
instance with production for consistency across environments](#tutorial-managing-MySQL-DB.next-steps-synch-env "#tutorial-managing-MySQL-DB.next-steps-synch-env").

### Next steps: Synchronize your development

instance with production for consistency across environments

#### Create a development environment

To manage a production environment, it’s important to maintain a synchronized development environment for
comprehensive testing and validation. To create a new development environment, first create a DB snapshot
of the current production DB instance. A DB snapshot captures the entire DB instance by creating a storage volume snapshot.
For instructions on how to create a DB snapshot on the Amazon RDS console, see
[Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").

After you create the DB snapshot of your production environment, create a new DB instance for your development
environment by restoring a DB snapshot. Restored DB instances are automatically associated with the default
DB parameter and option groups. However, you can apply a custom parameter group and option group by
specifying them during a restore. For instructions on restoring a DB snapshot, see
[Tutorial: Restore an Amazon RDS DB instance from a DB snapshot](CHAP_Tutorials.md "CHAP_Tutorials.md").

Finally, designate the new DB instance as your new development environment by updating its Amazon RDS tags.
For guidance on updating Amazon RDS tags to reflect this change, see the previous section
[Update tags to categorize a DB instance
as a production environment](#tutorial-managing-MySQL-DB.update-tags "#tutorial-managing-MySQL-DB.update-tags").

You now have a new development environment that mirrors the database configuration of your
production environment.

#### Synchronize a development environment with production environment

Once your new development environment is established, it is necessary to keep it synchronized with any changes that
occur in the production environment. This ensures that your development environment accurately reflects the current state
of production, which is essential for effective testing, validation, and troubleshooting. Amazon RDS provides a variety of different
ways to keep your development environment up to date with your production environment. For more information on these options,
see [Orchestrating database refreshes for Amazon RDS and Amazon Aurora](https://aws.amazon.com/blogs/database/orchestrating-database-refreshes-for-amazon-rds-and-amazon-aurora/ "https://aws.amazon.com/blogs/database/orchestrating-database-refreshes-for-amazon-rds-and-amazon-aurora/").

One of the primary ways in which you can synchronize your development and production environments is through creating
and restoring DB snapshots. A DB snapshot allows you to create a development environment that reflects the database
configuration of the production environment during the time the snapshot was created. For more information on DB snapshots,
see [Managing manual backups](USER_ManagingManualBackups.md "USER_ManagingManualBackups.md"). For more information on restoring
a DB instance, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").

DB snapshots are particularly valuable for the following use cases.

- Initial setup of a development environment: DB snapshots are useful to create the initial development environment
  for testing as it provides a consistent baseline that mirrors the exact state of the production environment at the
  time of the snapshot.
- High traffic applications: In production environments where continuous operation is critical, using Multi-AZ deployments
  for snapshots avoids I/O suspension on the primary database, ensuring uninterrupted performance and high availability.
- Sharing data across different RDS accounts: DB snapshots can be shared across different AWS accounts, facilitating the
  transfer of data between accounts or regions. This is useful for collaborative projects or scenarios where data needs
  to be shared for various purposes. For more information, see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md "USER_ShareSnapshot.md").

In this tutorial, you explored essential tasks for managing your DB instance throughout its lifecycle. You learned how to create a DB instance, add and update Amazon RDS tags,
expand storage, and create read replicas. You also learned ways to build on these fundamental operations and manage your production environment
effectively. This included establishing a development environment for testing and synchronizing it with the production environment
for consistency. These tasks help maintain a resilient and scalable database infrastructure, ensuring your Amazon RDS environment operates efficiently.
