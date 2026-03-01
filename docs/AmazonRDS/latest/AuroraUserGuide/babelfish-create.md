# Creating a Babelfish for Aurora PostgreSQL DB cluster

Babelfish for Aurora PostgreSQL is supported on Aurora PostgreSQL version 13.4 and higher.

You can use the AWS Management Console or the AWS CLI to create an Aurora PostgreSQL cluster with
Babelfish.

###### Note

In an Aurora PostgreSQL cluster, the `babelfish_db` database name is
reserved for Babelfish. Creating your own "babelfish_db" database
on a Babelfish for Aurora PostgreSQL prevents Aurora from successfully provisioning Babelfish.

###### To create a cluster with Babelfish running with the AWS Management Console

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/"), and choose **Create
   database**.

![Creating an Aurora PostgreSQL cluster with Babelfish running.](images/bbf_create_cluster_1.png) 2. For **Choose a database creation method**, do one of
the following:

    * To specify detailed engine options, choose **Standard
     create**.
    * To use preconfigured options that support best practices for
     an Aurora cluster, choose **Easy
     create**.

3. For **Engine type**, choose **Aurora
   (PostgreSQL Compatible)**.
4. Choose **Show filters**, and then choose
   **Show versions that support the Babelfish for
   PostgreSQL feature** to list the engine types that support
   Babelfish. Babelfish is currently supported on
   Aurora PostgreSQL 13.4 and higher versions.
5. For **Available versions**, choose an Aurora PostgreSQL
   version. To get the latest Babelfish features, choose the highest
   Aurora PostgreSQL major version.

![Choose an Aurora PostgreSQL version.](images/bbf_create_cluster_3.png) 6. For **Templates**, choose the template that matches
your use case. 7. For **DB cluster identifier**, enter a name that you
can easily find later in the DB cluster list. 8. For **Master username**, enter an administrator user
name. The default value for Aurora PostgreSQL is `postgres`. You
can accept the default or choose a different name. For example, to
follow the naming convention used on your SQL Server databases, you can
enter `sa` (system administrator) for the Master
username.

If you don't create a user named `sa` at this time,
you can create one later with your choice of client. After creating the
user, use the `ALTER SERVER ROLE` command to add it to the
`sysadmin` group (role) for the cluster.

###### Warning

Master username must always use lowercase characters failing which
the DB cluster can't connect to Babelfish via the TDS port. 9. For **Master password**, create a strong password and
confirm the password. 10. For the options that follow, until the **Babelfish
settings** section, specify your DB cluster settings. For
information about each setting, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings"). 11. To make Babelfish functionality available, select the
**Turn on Babelfish** box.

![Turn on Babelfish in your Aurora PostgreSQL cluster.](images/bbf_create_cluster_5.png) 12. For **DB cluster parameter group**, do one of the
following:

    * Choose **Create new** to create a new
     parameter group with Babelfish turned on.
    * Choose **Choose existing** to use an existing
     parameter group. If you use an existing group, make sure to
     modify the group before creating the cluster and add values for
     Babelfish parameters. For information about
     Babelfish parameters, see [DB cluster parameter group settings for Babelfish](babelfish-configuration.md "babelfish-configuration.md").


    If you use an existing group, provide the group name in the
     box that follows.

13. For **Database migration mode**, choose one of the
    following:
    - **Single database** to migrate a single SQL
      Server database.

    In some cases, you might migrate multiple user databases
    together, with your end goal a complete migration to native
    Aurora PostgreSQL without Babelfish. If the final
    applications require consolidated schemas (a single
    `dbo` schema), make sure to first consolidate
    your SQL Server databases into a single SQL server database.
    Then migrate to Babelfish using **Single
    database** mode.
    - **Multiple databases** to migrate multiple
      SQL Server databases (originating from a single SQL Server
      installation). Multiple database mode doesn't consolidate
      multiple databases that don't originate from a single SQL
      Server installation. For information about migrating multiple
      databases, see [Using Babelfish with a single database or multiple databases](babelfish-architecture.md#babelfish-single_vs_multi_db "babelfish-architecture.md#babelfish-single_vs_multi_db").

###### Note

From Aurora PostgreSQL 16 version, **Multiple
databases** is chosen by default as the Database
migration mode.

![Choose a migration mode for your SQL Server databases.](images/bbf_create_cluster_6.png) 14. For **Default collation locale**, enter your server
locale. The default is `en-US`. For detailed information
about collations, see [Understanding Collations in Babelfish for Aurora PostgreSQL](babelfish-collations.md "babelfish-collations.md"). 15. For **Collation name** field, enter your default
collation. The default is `sql_latin1_general_cp1_ci_as`. For
detailed information, see [Understanding Collations in Babelfish for Aurora PostgreSQL](babelfish-collations.md "babelfish-collations.md"). 16. For **Babelfish TDS port**, enter the default
port `1433`. Currently, Babelfish only supports port
`1433` for your DB cluster. 17. For **DB parameter group**, choose a parameter group
or have Aurora create a new group for you with default settings. 18. For **Failover priority**, choose a failover priority
for the instance. If you don't choose a value, the default is
`tier-1`. This priority determines the order in which
replicas are promoted when recovering from a primary instance failure.
For more information, see [Fault tolerance for an Aurora DB cluster](Concepts.md#Aurora.Managing.FaultTolerance "Concepts.md#Aurora.Managing.FaultTolerance"). 19. For **Backup retention period**, choose the length of
time (1–35 days) that Aurora retains backup copies of the
database. You can use backup copies for point-in-time restores (PITR) of
your database down to the second. The default retention period is seven
days.

![Choose an Aurora PostgreSQL version.](images/bbf_create_cluster_7.png) 20. Choose **Copy tags to snapshots** to copy any DB
instance tags to a DB snapshot when you create a snapshot.

###### Note

When restoring a DB cluster from a snapshot, it does not restore as a
Babelfish for Aurora PostgreSQL DB cluster. You need to turn on the parameters that
control Babelfish preferences in the DB cluster parameter group to
enable Babelfish again. For more information on the
Babelfish parameters, see [DB cluster parameter group settings for Babelfish](babelfish-configuration.md "babelfish-configuration.md"). 21. Choose **Enable encryption** to turn on encryption at
rest (Aurora storage encryption) for this DB cluster. 22. Choose **Enable Performance Insights** to turn on
Amazon RDS Performance Insights. 23. Choose **Enable Enhanced monitoring** to start
gathering metrics in real time for the operating system that your DB
cluster runs on. 24. Choose **PostgreSQL log** to publish the log files to
Amazon CloudWatch Logs. 25. Choose **Enable auto minor version upgrade** to
automatically update your Aurora DB cluster when a minor version upgrade
is available. 26. For **Maintenance window**, do the following:

    * To choose a time for Amazon RDS to make modifications or perform
     maintenance, choose **Select window**.
    * To perform Amazon RDS maintenance at an unscheduled time, choose
     **No preference**.

27. Select the **Enable deletion protection** box to
    protect your database from being deleted by accident.

If you turn on this feature, you can't directly delete the
database. Instead, you need to modify the database cluster and turn off
this feature before deleting the database.

![Choose from additional Aurora PostgreSQL administrative features.](images/bbf_create_cluster_9.png) 28. Choose **Create database**.
You can find your new database set up for Babelfish in the
**Databases** listing. The **Status**
column displays **Available** when the deployment is
complete.

![An Aurora PostgreSQL cluster with Babelfish running.](images/bbf_create_cluster_10.png)
When you create an Babelfish for Aurora PostgreSQL; using the AWS CLI, you need to pass the
command the name of the DB cluster parameter group to use for the cluster. For
more information, see [DB cluster prerequisites](Aurora.md#Aurora.CreateInstance.Prerequisites "Aurora.md#Aurora.CreateInstance.Prerequisites").

Before you can use the AWS CLI to create an Aurora PostgreSQL cluster with
Babelfish, do the following:

- Choose your endpoint URL from the list of services at [Amazon Aurora
  endpoints and quotas](../../../general/latest/gr/aurora.md "../../../general/latest/gr/aurora.md").
- Create a parameter group for the cluster. For more information about
  parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
- Modify the parameter group, adding the parameter that turns on
  Babelfish.

###### To create an Aurora PostgreSQL DB cluster with Babelfish using the AWS CLI

The examples that follow use the default Master username,
`postgres`. Replace as needed with the username that you
created for your DB cluster, such as `sa` or whatever username
you chose if you didn't accept the default.

1. Create a parameter group.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-parameter-group \
--endpoint-url `endpoint-url` \
--db-cluster-parameter-group-name `parameter-group` \
--db-parameter-group-family `aurora-postgresql14` \
--description `"description"`
```

For Windows:

```
aws rds create-db-cluster-parameter-group ^
--endpoint-url `endpoint-URL` ^
--db-cluster-parameter-group-name `parameter-group` ^
--db-parameter-group-family `aurora-postgresql14` ^
--description `"description"`
```

2. Modify your parameter group to turn on Babelfish.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
--endpoint-url `endpoint-url` \
--db-cluster-parameter-group-name `parameter-group` \
--parameters "ParameterName=rds.babelfish_status,ParameterValue=on,ApplyMethod=pending-reboot"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
--endpoint-url `endpoint-url` ^
--db-cluster-parameter-group-name `paramater-group` ^
--parameters "ParameterName=rds.babelfish_status,ParameterValue=on,ApplyMethod=pending-reboot"
```

3. Identify your DB subnet group and the virtual private cloud (VPC)
   security group ID for your new DB cluster, and then call the [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") command.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
--db-cluster-identifier  `cluster-name`\
--master-username `postgres` \
--manage-master-user-password \
--engine aurora-postgresql \
--engine-version `14.3`            \
--vpc-security-group-ids `security-group` \
--db-subnet-group-name `subnet-group-name` \
--db-cluster-parameter-group-name `parameter-group`
```

For Windows:

```
aws rds create-db-cluster ^
--db-cluster-identifier `cluster-name` ^
--master-username `postgres` ^
--manage-master-user-password ^
--engine aurora-postgresql ^
--engine-version `14.3` ^
--vpc-security-group-ids `security-group` ^
--db-subnet-group-name `subnet-group` ^
--db-cluster-parameter-group-name `parameter-group`
```

This example specifies the `--manage-master-user-password`
option to generate the master user password and manage it in Secrets Manager. For
more information, see [Password management with Amazon Aurora and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md"). Alternatively, you can use
the `--master-password` option to specify and manage the
password yourself. 4. Explicitly create the primary instance for your DB cluster. Use the
name of the cluster that you created in step 3 for the
`--db-cluster-identifier` argument when you call the
[create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command, as shown following.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
--db-instance-identifier `instance-name` \
--db-instance-class `db.r6g` \
--db-subnet-group-name `subnet-group` \
--db-cluster-identifier `cluster-name` \
--engine aurora-postgresql
```

For Windows:

```
aws rds create-db-instance ^
--db-instance-identifier `instance-name` ^
--db-instance-class `db.r6g` ^
--db-subnet-group-name `subnet-group` ^
--db-cluster-identifier `cluster-name` ^
--engine aurora-postgresql
```
