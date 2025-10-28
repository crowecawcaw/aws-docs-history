# Creating a data migration in AWS DMS

After you create a migration project with compatible data providers of the same type,
you can use this project for homogeneous data migrations. For more information, see [Creating migration projects](migration-projects-create.md "migration-projects-create.md").

To start using homogeneous data migrations, create a new data migration. You can create several homogeneous data migrations of different
types in a single migration project.

AWS DMS has the maximum number of homogeneous data migrations that you can create for your AWS account.
See the following section for information about AWS DMS service quotas [Quotas for AWS Database Migration Service](CHAP_Limits.md "CHAP_Limits.md").

Before you create a data migration, make sure that you set up the required resources such as
your source and target databases, an IAM policy and role, an instance profile, and data providers.
For more information, see [Creating IAM resources](dm-iam-resources.md "dm-iam-resources.md"),
[Creating instance profiles](instance-profiles.md "instance-profiles.md"), and
[Creating data providers](data-providers-create.md "data-providers-create.md").

Also, we recommend that you don't use homogeneous data migrations to migrate data from a higher database version
to a lower database version. Check the versions of databases that you use for source and target
data providers, and upgrade your target database version, if needed.

###### To create a data migration

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project, and on the **Data migrations** tab,
   choose **Create data migration**.
4. For **Name**, enter a name for your data migration. Make sure that you use
   a unique name for your data migration so that you can easily identify it.
5. For **Replication type**, choose the type of data migration that you want to
   configure. You can choose one of the following options.
   - **Full load** — Migrates your existing source data.
   - **Full load and change data capture (CDC)** — Migrates your
     existing source data and replicates ongoing changes.
   - **Change data capture (CDC)** — Replicates ongoing changes.

6. Select the check box for **Turn on CloudWatch logs** to store data migration
   logs in Amazon CloudWatch. If you don't choose this option, then you can't see the log files when your
   data migration fails.
7. (Optional) Expand **Advanced settings**. For **Number of jobs**,
   enter the number of parallel threads that AWS DMS can use to migrate your source data to the target.
8. For **IAM service role**, choose the IAM role that you created in prerequisites.
   For more information, see [Creating an IAM role for homogeneous data migrations in AWS DMS](dm-iam-resources.md#dm-resources-iam-role "dm-iam-resources.md#dm-resources-iam-role").
9. Configure the **Start mode** for data migrations of the
   **Change data capture (CDC)** type. You can choose one of the following options.
   - **Immediately** — Starts the ongoing replication when you start your data
     migration.
   - **Using a native start point** — Starts the ongoing replication from
     the specified point.

   For PostgreSQL databases, enter the name of the logical replication slot for
   **Slot name** and enter the transaction log sequence number for
   **Native start point**.

   For MySQL databases, enter the transaction log sequence number for
   **Log sequence number (LSN)**.

10. Configure the **Stop mode** for data migrations of the
    **Change data capture (CDC)** or **Full load and change data capture (CDC)**
    type. You can choose one of the following options.
    - **Don’t stop CDC** — AWS DMS continues the ongoing replication until you
      stop your data migration.
    - **Using a server time point** — AWS DMS stops the ongoing replication at
      the specified time.

    If you choose this option, then for **Stop date and time**, enter the date
    and time when you want to automatically stop the ongoing replication.

11. Choose **Create data migration**.
    AWS DMS creates your data migration and adds it to the list on the **Data migrations** tab
    in your migration project. Here you can see the status of your data migration. For more information,
    see [Migration statuses](dm-migrating-data-statuses.md "dm-migrating-data-statuses.md").

###### Important

For data migrations of the **Full load** and
**Full load and change data capture (CDC)** type, AWS DMS deletes all data, tables,
and other database objects on your target database. Make sure you have a backup of your target database.

After AWS DMS creates your data migration, the status of this data migration is set to
**Ready**. To migrate your data, you must start the data migration manually.
To do so, choose your data migration from the list. Next, for **Actions**,
choose **Start**. For more information, see [Managing data migrations](dm-migrating-data-manage.md "dm-migrating-data-manage.md").

The first launch of a homogeneous data migration requires some setup. AWS DMS creates a serverless
environment for your data migration. This process takes up to 15 minutes. After you stop and restart your
data migration, AWS DMS doesn't create the environment again, and you can access your data migration faster.
