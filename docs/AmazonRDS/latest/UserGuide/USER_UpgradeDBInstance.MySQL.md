# Using a read replica to reduce downtime when upgrading an RDS for MySQL database

In most cases, a blue/green deployment is the best option to reduce downtime when
upgrading a MySQL DB instance. For more information, see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

If you can't use a blue/green deployment and your MySQL DB instance is currently in use with a production application, you can
use the following procedure to upgrade the database version for your DB instance. This
procedure can reduce the amount of downtime for your application.

By using a read replica, you can perform most of the maintenance steps ahead of time and minimize
the necessary changes during the actual outage. With this technique, you can test and prepare the
new DB instance without making any changes to your existing DB instance.

The following procedure shows an example of upgrading from MySQL version 5.7 to MySQL
version 8.0. You can use the same general steps for upgrades to other major versions.
You can use the same general steps for upgrades to other major versions.

###### Note

When you are upgrading from MySQL version 5.7 to MySQL version 8.0, or from MySQL
version 8.0 to MySQL version 8.4, complete the prechecks before performing the
upgrade. For more information, see [Prechecks for upgrades from MySQL 5.7 to 8.0](USER_UpgradeDBInstance.MySQL.md#USER_UpgradeDBInstance.MySQL.57to80Prechecks "USER_UpgradeDBInstance.MySQL.md#USER_UpgradeDBInstance.MySQL.57to80Prechecks") and [Prechecks for
upgrades from MySQL 8.0 to 8.4](USER_UpgradeDBInstance.MySQL.md#USER_UpgradeDBInstance.MySQL.80to84Prechecks "USER_UpgradeDBInstance.MySQL.md#USER_UpgradeDBInstance.MySQL.80to84Prechecks").

###### To upgrade a MySQL database while a DB instance is in use

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Create a read replica of your MySQL 5.7 DB instance. This process creates an
   upgradable copy of your database. Other read replicas of the DB instance might also exist.
   1. In the console, choose **Databases**, and then choose the DB instance that you want
      to upgrade.
   2. For **Actions**, choose **Create read replica**.
   3. Provide a value for **DB instance identifier** for your read replica and
      ensure that the **DB instance class** and other
      settings match your MySQL 5.7 DB instance.
   4. Choose **Create read replica**.

3. (Optional) When the read replica has been created and **Status** shows
   **Available**, convert the read replica into a Multi-AZ deployment and enable backups.

By default, a read replica is created with backups disabled. Because the read
replica ultimately becomes the production DB instance, it is a best practice to
configure a Multi-AZ deployment and enable backups.

    1. In the console, choose **Databases**, and then choose the read replica that
     you just created.
    2. Choose **Modify**.
    3. For **Multi-AZ deployment**, choose **Create a standby instance**.
    4. For **Backup Retention Period**, choose a positive nonzero value, such as 3
     days, and then choose **Continue**.
    5. For **Scheduling of modifications**, choose **Apply immediately**.
    6. Choose **Modify DB instance**.

4. When the read replica **Status** shows **Available**, upgrade the read replica to MySQL 8.0:
   1. In the console, choose **Databases**, and then choose the read replica that
      you just created.
   2. Choose **Modify**.
   3. For **DB engine version**, choose the MySQL 8.0 version to upgrade to,
      and then choose **Continue**.
   4. For **Scheduling of modifications**, choose **Apply immediately**.
   5. Choose **Modify DB instance** to start the upgrade.

5. When the upgrade is complete and **Status** shows
   **Available**, verify that the upgraded read replica is
   up-to-date with the source MySQL 5.7 DB instance. To verify, connect to the read
   replica and run the `SHOW REPLICA STATUS` command. If the
   `Seconds_Behind_Master` field is `0`, then replication
   is up-to-date.

###### Note

Previous versions of MySQL used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MySQL version
before 8.0.23, then use `SHOW SLAVE STATUS`. 6. (Optional) Create a read replica of your read replica.

If you want the DB instance to have a read replica after it is promoted to a standalone DB instance,
you can create the read replica now.

    1. In the console, choose **Databases**, and then choose the read replica that
     you just upgraded.
    2. For **Actions**, choose **Create read replica**.
    3. Provide a value for **DB instance identifier** for your read replica and
     ensure that the **DB instance class** and other
     settings match your MySQL 5.7 DB instance.
    4. Choose **Create read replica**.

7. (Optional) Configure a custom DB parameter group for the read replica.

If you want the DB instance to use a custom parameter group after it is
promoted to a standalone DB instance, you can create the DB parameter group now
and associate it with the read replica.

    1. Create a custom DB parameter group for MySQL 8.0. For instructions, see
     [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
    2. Modify the parameters that you want to change in the DB parameter group you just created.
     For instructions, see [Modifying parameters in a DB parameter group
     in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
    3. In the console, choose **Databases**, and then choose the read replica.
    4. Choose **Modify**.
    5. For **DB parameter group**, choose the MySQL 8.0 DB parameter group you just created,
     and then choose **Continue**.
    6. For **Scheduling of modifications**, choose **Apply immediately**.
    7. Choose **Modify DB instance** to start the upgrade.

8. Make your MySQL 8.0 read replica a standalone DB instance.

###### Important

When you promote your MySQL 8.0 read replica to a standalone DB instance, it is no longer a
replica of your MySQL 5.7 DB instance. We recommend that you promote your
MySQL 8.0 read replica during a maintenance window when your source MySQL
5.7 DB instance is in read-only mode and all write operations are suspended.
When the promotion is completed, you can direct your write operations to the
upgraded MySQL 8.0 DB instance to ensure that no write operations are
lost.

In addition, we recommend that, before promoting your MySQL 8.0 read
replica, you perform all necessary data definition language (DDL) operations
on your MySQL 8.0 read replica. An example is creating indexes. This
approach avoids negative effects on the performance of the MySQL 8.0 read
replica after it has been promoted. To promote a read replica, use the
following procedure.

    1. In the console, choose **Databases**, and then choose the read replica that
     you just upgraded.
    2. For **Actions**, choose **Promote**.
    3. Choose **Yes** to enable automated backups for the read replica instance. For
     more information, see [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").
    4. Choose **Continue**.
    5. Choose **Promote Read Replica**.

9. You now have an upgraded version of your MySQL database. At this point, you
   can direct your applications to the new MySQL 8.0 DB instance.
