# Creating an Amazon Aurora global database

To create an Aurora global database and its associated resources by using the AWS Management Console, the AWS CLI,
or the RDS API, use the following steps.

###### Note

If you have an existing Aurora DB cluster running an Aurora
database engine that's global-compatible, you can use a shorter form of this procedure.
In that case, you can add another AWS Region to the existing DB cluster
to create your Aurora global database. To do so, see
[Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").

The steps for creating an Aurora global database begin by signing in to an AWS Region that supports the Aurora
global database feature. For a complete list, see
[Supported
Regions and DB engines for Aurora global databases](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

One of the following steps is choosing a virtual private cloud (VPC) based on Amazon VPC for
your Aurora DB cluster. To use your own VPC, we recommend that you create it in advance
so it's available for you to choose. At the same time, create any related subnets,
and as needed a subnet group and security group. To learn how, see
[Tutorial: Create a VPC for use with a
DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md").

For general information about creating an Aurora DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

###### To create an Aurora global database

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Create database**. On the **Create database** page,
   do the following:
   - For the database creation method, choose **Standard create**. (Don't
     choose Easy create.)
   - For `Engine type` in the **Engine options** section, choose
     the applicable engine type, **Aurora (MySQL Compatible)** or **Aurora (PostgreSQL Compatible)**.

3. Continue creating your Aurora global database by using the steps from the following procedures.

### Creating a global

database using Aurora MySQL

The following steps apply to all versions of Aurora MySQL.

###### To create an Aurora global database using Aurora MySQL

Complete the **Create database** page.

1. For **Engine options**, choose the following:
   1. For **Engine version**, choose the version of Aurora MySQL that you want to use for your Aurora global database.

2. For **Templates**, choose **Production**. Or you can choose
   Dev/Test if appropriate for your use case. Don't use Dev/Test in production
   environments.
3. For **Settings**, do the following:
   1. Enter a meaningful name for the DB cluster identifier. When you finish creating the Aurora
      global database, this name identifies the primary DB cluster.
   2. Enter your own password for the `admin` user account for the DB instance, or have
      Aurora generate one for you. If you choose to autogenerate a password, you get
      an option to copy the password.

   ![Screenshot of Settings choices when creating a global database.](images/aurora-global-db-create-ams-3.png)

4. For **DB instance class**, choose `db.r5.large` or another memory
   optimized DB instance class. We recommend that you use a db.r5 or higher instance
   class.
5. For **Availability & durability**, we recommend that you choose to have
   Aurora create an Aurora Replica in a different Availability Zone (AZ) for you. If
   you don't create an Aurora Replica now, you need to do it later.

![Screenshot of Availability & durability.](images/aurora-global-db-create-ams-4b.png) 6. For **Connectivity**, choose the virtual private cloud (VPC) based on Amazon VPC that
defines the virtual networking environment for this DB instance. You can choose the
defaults to simplify this task. 7. Complete the **Database authentication** settings. To simplify the process,
you can choose **Password authentication** now and set up
AWS Identity and Access Management (IAM) later. 8. For **Additional configuration**, do the following:

    1. Enter a name for **Initial database
     name** to create the primary Aurora DB instance for this cluster. This is the writer node for the
     Aurora primary DB cluster.


    Leave the defaults selected for the DB cluster parameter group and DB parameter group, unless you have your
     own custom parameter groups that you want to use.
    2. Clear the **Enable backtrack** check box if it's selected. Aurora global
     databases don't support backtracking. Otherwise, accept the other default
     settings for **Additional configuration**.

9. Choose **Create database**.

It can take several minutes for Aurora to complete the process of creating the
Aurora DB instance, its Aurora Replica, and the Aurora DB cluster. You can tell when
the Aurora DB cluster is ready to use as the primary DB cluster in an Aurora global
database by its status. When that's so, its status and that of the writer and
replica node is **Available**, as shown following.

![Screenshot of Databases with an Aurora DB cluster ready to use for Aurora global database.](images/aurora-global-db-create-ams-5.png)

When your primary DB cluster is available, create the Aurora global database by adding
a secondary cluster to it. To do this, follow the steps in [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").

### Creating a global

database using Aurora PostgreSQL

###### To create an Aurora global database using Aurora PostgreSQL

Complete the **Create database** page.

1. For **Engine options**, choose the following:
   1. For **Engine version**, choose the version of Aurora PostgreSQL that you want to use for your Aurora global database.

2. For **Templates**, choose **Production**. Or you can choose
   Dev/Test if appropriate. Don't use Dev/Test in production environments.
3. For **Settings**, do the following:
   1. Enter a meaningful name for the DB cluster identifier. When you finish creating the Aurora
      global database, this name identifies the primary DB cluster.
   2. Enter your own password for the default admin account for the DB cluster, or have Aurora
      generate one for you. If you choose Auto generate a password, you get an
      option to copy the password.

   ![Screenshot of Settings choices when creating a global database.](images/aurora-global-db-create-apg-2.png)

4. For **DB instance class**, choose `db.r5.large` or another memory
   optimized DB instance class. We recommend that you use a db.r5 or higher instance class.
5. For **Availability & durability**, we recommend that you choose to have
   Aurora create an Aurora Replica in a different AZ for you. If you don't create
   an Aurora Replica now, you need to do it later.
6. For **Connectivity**, choose the virtual private cloud (VPC) based on Amazon VPC that
   defines the virtual networking environment for this DB instance. You can choose the
   defaults to simplify this task.
7. (Optional) Complete the **Database authentication** settings. Password authentication is always enabled. To simplify the process,
   you can skip this section and set up IAM or password and Kerberos authentication later.
8. For **Additional configuration**, do the following:
   1. Enter a name for **Initial database
      name** to create the primary Aurora DB instance for this cluster. This is the writer node for the
      Aurora primary DB cluster.

   Leave the defaults selected for the DB cluster parameter group and DB parameter group, unless you have your
   own custom parameter groups that you want to use. 2. Accept all other default settings for **Additional configuration**, such as
   Encryption, Log exports, and so on.

9. Choose **Create database**.

It can take several minutes for Aurora to complete the process of creating the
Aurora DB instance, its Aurora Replica, and the Aurora DB cluster. When the cluster
is ready to use, the Aurora DB cluster and its writer and replica nodes display
**Available** status. This becomes the primary DB cluster of
your Aurora global database, after you add a secondary.

![Screenshot of Databases with an Aurora DB cluster ready to use for Aurora global database.](images/aurora-global-db-create-apg-5-add-region.png)

When your primary DB cluster is available, create one or more secondary clusters by following the steps in
[Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").

The AWS CLI commands in the procedures following accomplish the following tasks:

1. Create an Aurora global database, giving it a name and specifying the Aurora database engine
   type that you plan to use.
2. Create an Aurora DB cluster for the Aurora global database.
3. Create the Aurora DB instance for the cluster. This is the primary Aurora DB cluster for the global database.
4. Create a second DB instance for Aurora DB cluster. This is a reader to complete the Aurora DB
   cluster.
5. Create a second Aurora DB cluster in another Region and then add it to your Aurora global database, by following the steps in
   [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").
   Follow the procedure for your Aurora database engine.

### Creating a global database using

Aurora MySQL

###### To create an Aurora global database using Aurora MySQL

1. Use the `create-global-cluster` CLI command, passing the name of the AWS Region, Aurora database engine,
   and version.

For Linux, macOS, or Unix:

```
aws rds create-global-cluster --region `primary_region` \
    --global-cluster-identifier `global_database_id` \
    --engine aurora-mysql \
    --engine-version `version` # optional
```

For Windows:

```
aws rds create-global-cluster ^
    --global-cluster-identifier `global_database_id` ^
    --engine aurora-mysql ^
    --engine-version `version` # optional
```

This creates an "empty" Aurora global database, with just a name (identifier) and Aurora database engine. It can take a few minutes for the Aurora global database to be available. Before going to the next step, use the
`describe-global-clusters` CLI command to see if it's available.

```
aws rds describe-global-clusters --region `primary_region` --global-cluster-identifier `global_database_id`
```

When the Aurora global database is available, you can create its primary Aurora DB cluster. 2. To create a primary Aurora DB cluster, use the `create-db-cluster`
CLI command. Include the name of your Aurora global database by using the
`--global-cluster-identifier` parameter.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
  --region `primary_region` \
  --db-cluster-identifier `primary_db_cluster_id` \
  --master-username `userid` \
  --master-user-password `password` \
  --engine aurora-mysql \
  --engine-version `version` \
  --global-cluster-identifier `global_database_id`

```

For Windows:

```
aws rds create-db-cluster ^
  --region `primary_region` ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --master-username `userid` ^
  --master-user-password `password` ^
  --engine aurora-mysql ^
  --engine-version `version` ^
  --global-cluster-identifier `global_database_id`

```

Use the `describe-db-clusters` AWS CLI command to confirm that
the Aurora DB cluster is ready. To single out a specific Aurora DB cluster, use `--db-cluster-identifier` parameter. Or you can leave out the
Aurora DB cluster name in the command to get details about all your Aurora DB clusters in the given Region.

```
aws rds describe-db-clusters --region `primary_region` --db-cluster-identifier `primary_db_cluster_id`
```

When the response shows `"Status": "available"` for the cluster, it's ready to use. 3. Create the DB instance for your primary Aurora DB cluster. To do so, use the `create-db-instance` CLI command. Give the command your Aurora DB
cluster's name, and specify the configuration details for the instance. You
don't need to pass the `--master-username` and
`--master-user-password` parameters in the command, because it gets
those from the Aurora DB cluster.

For the `--db-instance-class`, you can use only those from the memory optimized
classes, such as `db.r5.large`. We recommend that you use a db.r5 or
higher instance class. For information about these classes, see
[DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
  --db-cluster-identifier `primary_db_cluster_id` \
  --db-instance-class `instance_class` \
  --db-instance-identifier `db_instance_id` \
  --engine aurora-mysql \
  --engine-version `version` \
  --region `primary_region`

```

For Windows:

```
aws rds create-db-instance ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --db-instance-class `instance_class` ^
  --db-instance-identifier `db_instance_id` ^
  --engine aurora-mysql ^
  --engine-version `version` ^
  --region `primary_region`

```

The `create-db-instance` operation might take some time to complete. Check the
status to see if the Aurora DB instance is available before continuing.

```
aws rds describe-db-clusters --db-cluster-identifier `primary_db_cluster_id`
```

When the command returns a status of `available`, you can create another Aurora DB instance for
your primary DB cluster. This is the reader instance (the Aurora Replica) for the Aurora DB cluster. 4. To create another Aurora DB instance for the cluster, use the
`create-db-instance` CLI command.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
  --db-cluster-identifier `primary_db_cluster_id` \
  --db-instance-class `instance_class` \
  --db-instance-identifier `replica_db_instance_id` \
  --engine aurora-mysql
```

For Windows:

```
aws rds create-db-instance ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --db-instance-class `instance_class` ^
  --db-instance-identifier `replica_db_instance_id` ^
  --engine aurora-mysql
```

When the DB instance is available, replication begins from the writer node to the replica.
Before continuing, check that the DB instance is available with the
`describe-db-instances` CLI command.

At this point, you have an Aurora global database with its primary Aurora DB cluster containing a writer DB instance
and an Aurora Replica. You can now add a read-only Aurora DB cluster in a different Region to
complete your Aurora global database. To do so, follow the steps in
[Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").

### Creating a global database using Aurora PostgreSQL

When you create Aurora objects for an Aurora global database by using the following commands,
it can take a few minutes for each to become available. We recommend that after
completing any given command, you check the specific Aurora object's status to
make sure that the status is available.

To do so, use the
`describe-global-clusters` CLI command.

```
aws rds describe-global-clusters --region `primary_region`
    --global-cluster-identifier `global_database_id`

```

###### To create an Aurora global database using Aurora PostgreSQL

1. Use the `create-global-cluster` CLI command.

For Linux, macOS, or Unix:

```
aws rds create-global-cluster --region `primary_region` \
    --global-cluster-identifier `global_database_id` \
    --engine aurora-postgresql \
    --engine-version `version` # optional

```

For Windows:

```
aws rds create-global-cluster ^
    --global-cluster-identifier `global_database_id` ^
    --engine aurora-postgresql ^
    --engine-version `version` # optional

```

When the Aurora global database is available, you can create its primary Aurora DB cluster. 2. To create a primary Aurora DB cluster, use the
`create-db-cluster`
CLI command. Include the name of your Aurora global database by using the
`--global-cluster-identifier` parameter.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
  --region `primary_region` \
  --db-cluster-identifier `primary_db_cluster_id` \
  --master-username `userid` \
  --master-user-password `password` \
  --engine aurora-postgresql \
  --engine-version `version` \
  --global-cluster-identifier `global_database_id`
```

For Windows:

```
aws rds create-db-cluster ^
  --region `primary_region` ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --master-username `userid` ^
  --master-user-password `password` ^
  --engine aurora-postgresql ^
  --engine-version `version` ^
  --global-cluster-identifier `global_database_id`
```

Check that the Aurora DB cluster is ready. When the response from the following command shows `"Status": "available"` for the Aurora DB cluster, you can continue.

```
aws rds describe-db-clusters --region `primary_region` --db-cluster-identifier `primary_db_cluster_id`
```

3. Create the DB instance for your primary Aurora DB cluster. To do so, use the
   `create-db-instance` CLI command.

Pass the name of your Aurora DB cluster with the `--db-cluster-identifier`
parameter.

You don't need to pass the `--master-username` and
`--master-user-password` parameters in the command, because it
gets those from the Aurora DB cluster.

For the `--db-instance-class`, you can use only those from the memory
optimized classes, such as `db.r5.large`. We recommend that you use
a db.r5 or higher instance class. For information about these classes, see
[DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
  --db-cluster-identifier `primary_db_cluster_id` \
  --db-instance-class `instance_class` \
  --db-instance-identifier `db_instance_id` \
  --engine aurora-postgresql \
  --engine-version `version` \
  --region `primary_region`

```

For Windows:

```
aws rds create-db-instance ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --db-instance-class `instance_class` ^
  --db-instance-identifier `db_instance_id` ^
  --engine aurora-postgresql ^
  --engine-version `version` ^
  --region `primary_region`

```

4. Check the status of the Aurora DB instance before continuing.

```
aws rds describe-db-clusters --db-cluster-identifier `primary_db_cluster_id`

```

If the response shows that Aurora DB instance status is `available`, you can create another Aurora DB instance
for your primary DB cluster. 5. To create an Aurora Replica for Aurora DB cluster, use the
`create-db-instance` CLI command.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
  --db-cluster-identifier `primary_db_cluster_id` \
  --db-instance-class `instance_class` \
  --db-instance-identifier `replica_db_instance_id` \
  --engine aurora-postgresql
```

For Windows:

```
aws rds create-db-instance ^
  --db-cluster-identifier `primary_db_cluster_id` ^
  --db-instance-class `instance_class` ^
  --db-instance-identifier `replica_db_instance_id` ^
  --engine aurora-postgresql
```

When the DB instance is available, replication begins from the writer node to the replica.
Before continuing, check that the DB instance is available with the
`describe-db-instances` CLI command.

Your Aurora global database exists, but it has only its primary Region with an Aurora DB cluster made up of a writer DB instance and an Aurora Replica. You can now add
a read-only Aurora DB cluster in a different Region to complete your Aurora global database. To do so, follow the steps in
[Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").

To create an Aurora global database with the RDS API, run the
[CreateGlobalCluster](../APIReference/API_CreateGlobalCluster.md "../APIReference/API_CreateGlobalCluster.md") operation.
