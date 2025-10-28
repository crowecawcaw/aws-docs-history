# Setting up an Amazon Neptune global database

You can create a Neptune global database in one of the following ways:

- [Create a global database with
  all new DB clusters and instances](#neptune-gdb-creating-cli "#neptune-gdb-creating-cli").
- [Create a global database using
  an existing Neptune DB cluster as the primary cluster](#neptune-gdb-add-existing "#neptune-gdb-add-existing").

###### Topics

- [Configuration requirements for a global database in Amazon Neptune](#neptune-gdb-setup-config "#neptune-gdb-setup-config")
- [Using the AWS CLI to create a global database in Amazon Neptune](#neptune-gdb-creating-cli "#neptune-gdb-creating-cli")
- [Turning an existing DB cluster into a global database](#neptune-gdb-add-existing "#neptune-gdb-add-existing")
- [Adding secondary global
  database regions to a primary region in Amazon Neptune](#neptune-gdb-attaching "#neptune-gdb-attaching")
- [Connecting to a Neptune global database](#neptune-gdb-connect "#neptune-gdb-connect")

## Configuration requirements for a global database in Amazon Neptune

A Neptune global database spans at least two AWS Regions. The primary AWS Region
contains a Neptune DB cluster that has one writer instance. One to five secondary AWS Regions
each contain a read-only Neptune DB cluster made up entirely of read-replica instances. At least
one secondary AWS Region is required.

The Neptune DB clusters that make up a global database have the
following specific requirements:

- **DB instance class requirements**   —  
  A global database requires `r5` or `r6g` DB instance
  classes that are optimized for memory-intensive workloads, such as an
  `db.r5.large` instance type.
- **AWS Region requirements**   —  
  A global database needs a primary Neptune DB cluster in one AWS Region,
  and at least one secondary Neptune DB cluster in a different region. You can
  create up to five secondary read-only Neptune DB clusters, and each must be
  in a different region. In other words, no two Neptune DB clusters in a Neptune
  global database can be in the same AWS Region.
- **Engine version requirements**   —  
  The Neptune engine version used by all DB clusters in the global database should be
  the same, and must be greater than or equal to `1.2.0.0`. If you do not
  specify the engine version when creating a new global database or cluster or
  instance, the most recent engine version will be used.

###### Important

Although the DB cluster parameter groups can be configured independently
for each DB cluster in a global database, it's best to keep settings consistent across
the clusters to avoid unexpected behavior changes if a secondary cluster has to be promoted
to primary. For example, use the same settings for object indexes, streams, and
so forth in all the DB clusters.

## Using the AWS CLI to create a global database in Amazon Neptune

###### Note

The examples in this section follow the UNIX convention of using a backslash
(`\`) as the line-extender character. For Windows, replace the backslach
with a caret (`^`).

###### To create a global database using the AWS CLI

1. Start by creating an empty global database using the `create-global-cluster`
   AWS CLI command (which wraps the [CreateGlobalCluster](api-global-dbs.md#CreateGlobalCluster "api-global-dbs.md#CreateGlobalCluster") API). Specify the name of the
   AWS Region that you want to be primary, set Neptune as the
   database engine, and optionally, specify the engine version you want
   to use (this must be version 1.2.0.0 or higher):

```
aws neptune create-global-cluster
  --region `(primary region, such as us-east-1)` \
  --global-cluster-identifier `(ID for the global database)` \
  --engine neptune \
  --engine-version `(engine version; this is optional)`
```

2. It can take a few minutes for the global database to be available, so before
   going to the next step, use the `describe-global-clusters`
   CLI command (which wraps the [DescribeGlobalClusters](api-global-dbs.md#DescribeGlobalClusters "api-global-dbs.md#DescribeGlobalClusters") API) to check that the
   global database is available:

```
aws neptune describe-global-clusters \
  --region `(primary region)` \
  --global-cluster-identifier `(global database ID)`
```

3. After the Neptune global database becomes available, you can create
   a new Neptune DB cluster to be its primary cluster:

```
aws neptune create-db-cluster \
  --region `(primary region)` \
  --db-cluster-identifier `(ID for the primary DB cluster)` \
  --engine neptune \
  --engine-version `(engine version; must be >= 1.2.0.0)` \
  --global-cluster-identifier `(global database ID)`
```

4. Use the `describe-db-clusters`
   AWS CLI command to confirm that the new DB cluster is ready for you to add its
   primary DB instance:

```
aws neptune describe-db-clusters \
  --region `(primary region)` \
  --db-cluster-identifier `(primary DB cluster ID)`
```

When the response shows `"Status": "available"`, go on to the next step. 5. Create the primary DB instance for the primary cluster using the `create-db-instance`
AWS CLI command. You must use one of the memory-optimized `r5` or
`r6g` instance types, such as `db.r5.large`.

```
aws neptune create-db-instance \
  --region `(primary region)` \
  --db-cluster-identifier `(primary cluster ID)` \
  --db-instance-class `(instance class)` \
  --db-instance-identifier `(ID for the DB instance)` \
  --engine neptune \
  --engine-version `(optional: engine version)`
```

###### Note

If you are planning to add data to the new primary DB cluster using the
Neptune bulk loader, do so _before_ you add secondary regions.
This is faster and more cost-efficient than performing a bulk load after the global
database is fully set up.

Now add one or more secondary regions to the new global database, as described
in [Adding a secondary region using the AWS CLI](#neptune-gdb-attach-cli "#neptune-gdb-attach-cli").

## Turning an existing DB cluster into a global database

To turn an existing DB cluster into a global database, use the `create-global-cluster`
AWS CLI command to create a new global database in the same AWS Region as the existing
DB cluster is located, and set its `--source-db-cluster-identifier`
parameter to the Amazon Resource Name (ARN) of the existing cluster located there:

```
aws neptune create-global-cluster \
  --region `(region where the existing cluster is located)` \
  --global-cluster-identifier `(provide an ID for the new global database)` \
  --source-db-cluster-identifier `(the ARN of the existing DB cluster)` \
  --engine neptune \
  --engine-version `(engine version; this is optional)`
```

Now add one or more secondary regions to the new global database, as described
in [Adding a secondary region using the AWS CLI](#neptune-gdb-attach-cli "#neptune-gdb-attach-cli").

### Use a DB cluster restored from a snapshot as the primary cluster

You can turn a DB cluster restored from a snapshot into a Neptune global
database. After the restore is complete, turn the DB cluster that it created into
the primary cluster of a new global database as described above.

## Adding secondary global

database regions to a primary region in Amazon Neptune

A Neptune global database needs at least one secondary Neptune DB cluster in
a different AWS Region than the primary DB cluster. You can attach up to five secondary
DB clusters to the primary DB cluster.

Each secondary DB cluster that you add reduces by one the maximum number of
read-replica instances you can have on the primary cluster. For example, if there are
4 secondary clusters, then the maximum number of read-replica instances you
can have on the primary cluster is `15 - 4 = 11`. This means that if you
already have 14 reader instances in the primary DB cluster and one secondary cluster,
you won't be able to add another secondary cluster.

### Using the AWS CLI to add a secondary region

to a global database in Neptune

###### To add a secondary AWS Region to a Neptune global database using the AWS CLI

1. Use the `create-db-cluster`
   AWS CLI command to create a new DB cluster in a different region than that of your primary cluster,
   and set its `--global-cluster-identifier` parameter to specify the ID of the
   global database:

```
aws neptune create-db-cluster \
  --region `(the secondary region)` \
  --db-cluster-identifier `(ID for the new secondary DB cluster)` \
  --global-cluster-identifier `(global database ID)`
  --engine neptune \
  --engine-version `(optional: engine version)`
```

2. Use the `describe-db-clusters`
   AWS CLI command to confirm that the new DB cluster is ready for you to add its
   primary DB instance:

```
aws neptune describe-db-clusters \
  --region `(primary region)` \
  --db-cluster-identifier `(primary DB cluster ID)`
```

When the response shows `"Status": "available"`, go on to the next step. 3. Create the primary DB instance for the primary cluster using the `create-db-instance`
AWS CLI command, using an instance type in the `r5` or `r6g`
instance class:

```
aws neptune create-db-instance \
  --region `(secondary region)` \
  --db-cluster-identifier `(secondary cluster ID)` \
  --db-instance-class `(instance class)` \
  --db-instance-identifier `(ID for the DB instance)` \
  --engine neptune \
  --engine-version `(optional: engine version)`
```

###### Note

If you do not intend to serve a large number of read requests in
the secondary region, and are mainly concerned with keeping your data reliably
backed up there, you can create a secondary DB cluster with no DB instances. This
saves money, since you are then only paying for the secondary cluster's storage,
which Neptune will keep in sync with storage in the primary DB cluster.

## Connecting to a Neptune global database

How you connect to a Neptune global database depends on whether you need to
write to it or read from it:

- For read-only requests or queries, connect to the reader endpoint for the
  Neptune cluster in your AWS Region.
- To run mutation queries, connect to the cluster endpoint for the
  primary DB cluster, which might be in a different AWS Region than your
  application.
