# Migrating a snapshot of an RDS for PostgreSQL DB instance to an Aurora PostgreSQL DB cluster

To create an Aurora PostgreSQL DB cluster, you can migrate a DB snapshot of an
RDS for PostgreSQL DB instance. The new Aurora PostgreSQL DB cluster is populated with the data from
the original RDS for PostgreSQL DB instance. For information about creating a DB snapshot,
see [Creating a DB
snapshot](../UserGuide/USER_CreateSnapshot.md "../UserGuide/USER_CreateSnapshot.md").

In some cases, the DB snapshot might not be in the AWS Region where you want
to locate your data. If so, use the Amazon RDS console to copy the DB snapshot to that
AWS Region. For information about copying a DB snapshot, see [Copying a DB snapshot](../UserGuide/USER_CopySnapshot.md "../UserGuide/USER_CopySnapshot.md").

You can migrate RDS for PostgreSQL snapshots that are compatible with the
Aurora PostgreSQL versions available in the given AWS Region. For example, you can migrate
a snapshot from an RDS for PostgreSQL 11.1 DB instance to Aurora PostgreSQL version 11.4, 11.7,
11.8, or 11.9 in the US West (N. California) Region. You can migrate RDS for PostgreSQL 10.11 snapshot to
Aurora PostgreSQL 10.11, 10.12, 10.13, and 10.14. In other words, the RDS for PostgreSQL snapshot
must use the same or a lower minor version as the Aurora PostgreSQL.

You can also choose for your new Aurora PostgreSQL DB cluster to be encrypted at
rest by using an AWS KMS key. This option is available only for
unencrypted DB snapshots.

To migrate an RDS for PostgreSQL DB snapshot to an Aurora PostgreSQL DB cluster, you can
use the AWS Management Console, the AWS CLI, or the RDS API. When you use the AWS Management Console, the console takes the
actions necessary to create both the DB cluster and the primary instance.

###### To migrate a PostgreSQL DB snapshot by using the RDS console

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  Choose **Snapshots**.
3.  On the **Snapshots** page, choose the RDS for PostgreSQL
    snapshot that you want to migrate into an Aurora PostgreSQL DB cluster.
4.  Choose **Actions** then choose **Migrate
    snapshot**.
5.  Set the following values on the **Migrate database**
    page:
    - **DB engine version**: Choose a DB engine version you
      want to use for the new migrated instance.
    - **DB instance identifier**: Enter a name for
      the DB cluster that is unique for your account in the AWS Region that
      you chose. This identifier is used in the endpoint addresses for the
      instances in your DB cluster. You might choose to add some intelligence
      to the name, such as including the AWS Region and DB engine that you
      chose, for example `aurora-cluster1`.

    The DB instance identifier has the following
    constraints:

        + It must contain 1–63 alphanumeric characters or
         hyphens.
        + Its first character must be a letter.
        + It can't end with a hyphen or contain two
         consecutive hyphens.
        + It must be unique for all DB instances per AWS
         account, per AWS Region.

    - **DB instance class**: Choose a DB instance class
      that has the required storage and capacity for your database, for
      example `db.r6g.large`. Aurora cluster volumes automatically
      grow as the amount of data in your database increases.
      So you only need to choose a DB instance class
      that meets your current storage requirements. For more information, see
      [Overview of Amazon Aurora storage](Aurora.Overview.md#Aurora.Overview.Storage "Aurora.Overview.md#Aurora.Overview.Storage").
    - **Virtual private cloud (VPC)**: If you have
      an existing VPC, then you can use that VPC with your Aurora PostgreSQL DB
      cluster by choosing your VPC identifier, for example
      `vpc-a464d1c1`. For information about creating a VPC,
      see [Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md").

    Otherwise, you can choose to have Amazon RDS create a VPC for you
    by choosing **Create new VPC**.
    - **DB subnet group**: If you have an existing
      subnet group, then you can use that subnet group with your Aurora PostgreSQL
      DB cluster by choosing your subnet group identifier, for example
      `gs-subnet-group1`.
    - **Public access**: Choose
      **No** to specify that instances in your DB cluster
      can only be accessed by resources inside of your VPC. Choose
      **Yes** to specify that instances in your DB
      cluster can be accessed by resources on the public network.

    ###### Note

    Your production DB cluster might not need to be in a
    public subnet, because only your application servers require access
    to your DB cluster. If your DB cluster doesn't need to be in a
    public subnet, set **Public access** to
    **No**.
    - **VPC security group**: Choose a VPC security group
      to allow access to your database.
    - **Availability Zone**: Choose the
      Availability Zone to host the primary instance for your Aurora PostgreSQL DB
      cluster. To have Amazon RDS choose an Availability Zone for you, choose
      **No preference**.
    - **Database port**: Enter the default port to
      be used when connecting to instances in the Aurora PostgreSQL DB cluster.
      The default is `5432`.

    ###### Note

    You might be behind a corporate firewall that doesn't
    allow access to default ports such as the PostgreSQL default
    port, 5432. In this case, provide a port value that your
    corporate firewall allows. Remember that port value later
    when you connect to the Aurora PostgreSQL DB cluster.
    - **Enable Encryption**: Choose
      **Enable Encryption** for your new Aurora PostgreSQL DB
      cluster to be encrypted at rest. Also choose a KMS key
      as the **AWS KMS key** value.
    - **Auto minor version upgrade**: Choose **Enable auto minor version
      upgrade** to enable your Aurora PostgreSQL DB cluster to receive minor PostgreSQL DB engine
      version upgrades automatically when they become available.

    The **Auto minor version upgrade** option
    only applies to upgrades to PostgreSQL minor engine versions for your
    Aurora PostgreSQL DB cluster. It doesn't apply to regular patches applied to
    maintain system stability.

6.  Choose **Migrate** to migrate your DB snapshot.
7.  Choose **Databases** to see the new DB cluster.
    Choose the new DB cluster to monitor the progress of the migration. When the migration
    completes, the Status for the cluster is **Available**. On the
    **Connectivity & security** tab, you can find the
    cluster endpoint to use for connecting to the primary writer instance of the DB
    cluster. For more information on connecting to an Aurora PostgreSQL DB cluster, see
    [Connecting to an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
    Using the AWS CLI to migrate an RDS for PostgreSQL DB snapshot to an Aurora PostgreSQL involves two separate AWS CLI commands. First, you use
    the `restore-db-cluster-from-snapshot` AWS CLI command create a new Aurora PostgreSQL DB cluster. You then use the `create-db-instance`
    command to create the primary DB instance in the new cluster
    to complete the migration. The following procedure creates an Aurora PostgreSQL DB cluster with primary DB instance that has
    the same configuration as the DB instance used to create the snapshot.

###### To migrate an RDS for PostgreSQL DB snapshot to an Aurora PostgreSQL DB cluster

1. Use the [describe-db-snapshots](../../../cli/latest/reference/rds/describe-db-snapshots.md "../../../cli/latest/reference/rds/describe-db-snapshots.md")
   command to obtain information about the DB snapshot you want to migrate. You can specify either the
   `--db-instance-identifier` parameter or the `--db-snapshot-identifier` in the command. If you
   don't specify one of these parameters, you get all snapshots.

```
aws rds describe-db-snapshots --db-instance-identifier `<your-db-instance-name>`
```

2. The command returns all configuration details for any snapshots created from the DB instance specified. In the output, find the snapshot that you want to migrate and locate its Amazon Resource Name (ARN).
   To learn more about
   Amazon RDS ARNs, see [Amazon Relational Database Service (Amazon RDS)](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-rds "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-rds").
   An ARN looks similar to the output following.

```
`“DBSnapshotArn": "arn:aws:rds:`aws-region`:111122223333:snapshot:<snapshot_name>"`
```

Also in the output you can find configuration details for the RDS for PostgreSQL DB instance, such as the engine version, allocated storage, whether or not the DB instance is encrypted, and so on. 3. Use the [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md") command to
start the migration. Specify the following parameters:

    * `--db-cluster-identifier` – The name that you want to give to the Aurora PostgreSQL DB cluster. This Aurora DB cluster
     is the target for your DB snapshot migration.
    * `--snapshot-identifier` – The Amazon Resource Name (ARN) of the DB snapshot to migrate.
    * `--engine` – Specify `aurora-postgresql` for the Aurora DB cluster engine.
    * `--kms-key-id` – This optional parameter lets you create an encrypted Aurora PostgreSQL DB cluster from an
     unencrypted DB snapshot. It also lets you choose a different encryption key for the DB cluster than the key used for
     the DB snapshot.


    ###### Note

    You can't create an unencrypted Aurora PostgreSQL DB cluster from an encrypted DB snapshot.

Without the `--kms-key-id` parameter specified as shown following, the [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md")
AWS CLI command creates an empty Aurora PostgreSQL DB cluster that's either encrypted using the same key as the DB snapshot or is unencrypted if
the source DB snapshot isn't encrypted.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `cluster-name` \
    --snapshot-identifier arn:aws:rds:`aws-region`:`111122223333`:snapshot:`your-snapshot-name` \
    --engine aurora-postgresql
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `new_cluster` ^
    --snapshot-identifier arn:aws:rds:`aws-region`:`111122223333`:snapshot:`your-snapshot-name` ^
    --engine aurora-postgresql
```

4. The command returns details about the Aurora PostgreSQL DB cluster that's being created for the migration. You can check the
   status of the Aurora PostgreSQL DB cluster by using the [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clussters.md "../../../cli/latest/reference/rds/describe-db-clussters.md") AWS CLI command.

```
aws rds describe-db-clusters --db-cluster-identifier `cluster-name`
```

5.  When the DB cluster becomes "available", you use [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command to populate
    the Aurora PostgreSQL DB cluster with the DB instance based on your Amazon RDS DB snapshot. Specify the following parameters:

        * `--db-cluster-identifier` – The name of the new Aurora PostgreSQL DB cluster that you created in the previous step.
        * `--db-instance-identifier` – The name you want to give to the DB instance. This instance becomes the primary node in your Aurora PostgreSQL DB cluster.
        * `----db-instance-class`  – Specify the DB instance class to use. Choose from among the DB instance classes supported by the Aurora PostgreSQL version to which
         you're migrating. For more information, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md") and
         [Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").
        * `--engine` – Specify `aurora-postgresql` for the DB instance.

    You can also create the DB instance with a different configuration than the source DB snapshot, by passing in the appropriate
    options in the `create-db-instance` AWS CLI command. For more information, see the
    [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-cluster-identifier `cluster-name` \
    --db-instance-identifier --db-instance-class db.`instance.class` \
    --engine aurora-postgresql
```

For Windows:

```
aws rds create-db-instance ^
    --db-cluster-identifier `cluster-name` ^
    --db-instance-identifier --db-instance-class db.`instance.class` ^
    --engine aurora-postgresql
```

When the migration process completes, the Aurora PostgreSQL cluster has a populated primary DB instance.
