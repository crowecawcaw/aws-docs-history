# Working with DB shard groups

You perform the following tasks to add and manage a DB shard group for Aurora PostgreSQL Limitless Database.

###### Topics

- [Connecting to your Aurora PostgreSQL Limitless Database DB cluster](#limitless-endpoint "#limitless-endpoint")
- [Finding the number of routers and shards in a DB shard group](#limitless-shard.number "#limitless-shard.number")
- [Describing DB shard groups](#limitless-describe "#limitless-describe")
- [Rebooting a DB shard group](#limitless-reboot "#limitless-reboot")
- [Changing the capacity of a DB shard group](limitless-capacity.md "limitless-capacity.md")
- [Splitting a shard in a DB shard group](limitless-shard-split.md "limitless-shard-split.md")
- [Adding a router to a DB shard group](limitless-add-router.md "limitless-add-router.md")
- [Deleting a DB shard group](limitless-shard-delete.md "limitless-shard-delete.md")
- [Adding a DB shard group to an existing Aurora PostgreSQL Limitless Database DB cluster](limitless-shard-add.md "limitless-shard-add.md")

## Connecting to your Aurora PostgreSQL Limitless Database DB cluster

To work with Aurora PostgreSQL Limitless Database, you connect to the cluster writer or reader endpoint. You can use `psql` or any other connection utility that works with PostgreSQL:

```
`$` psql -h `DB_cluster_endpoint` -p `port_number` -U `database_username` -d postgres_limitless
```

The following example uses the endpoint for the DB cluster that you created in [CLI](limitless-create-cluster.md#limitless-create-CLI "limitless-create-cluster.md#limitless-create-CLI").

```
`$` psql -h my-limitless-cluster.cluster-ckifpdyyyxxx.us-east-1.rds.amazonaws.com -p 5432 -U postgres -d postgres_limitless
```

###### Note

The default database for the DB shard group in Aurora PostgreSQL Limitless Database is `postgres_limitless`.

### Using the Limitless Connection Plugin

When connecting to Aurora PostgreSQL Limitless Database, clients connect using the cluster endpoint, and are routed to a transaction router by Amazon Route 53. However, Route 53 is
limited in its ability to load balance, and can allow uneven workloads on transaction routers. The [Limitless Connection Plugin](https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheLimitlessConnectionPlugin.md "https://github.com/aws/aws-advanced-jdbc-wrapper/blob/main/docs/using-the-jdbc-driver/using-plugins/UsingTheLimitlessConnectionPlugin.md") for the [AWS JDBC Driver](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper") addresses
this by performing client-side load balancing with load awareness. For more information on the [AWS JDBC Driver](https://github.com/awslabs/aws-advanced-jdbc-wrapper "https://github.com/awslabs/aws-advanced-jdbc-wrapper"), see [Connecting to Aurora PostgreSQL with the Amazon Web Services (AWS) JDBC Driver](Aurora.md#Aurora.Connecting.JDBCDriverPostgreSQL "Aurora.md#Aurora.Connecting.JDBCDriverPostgreSQL").

## Finding the number of routers and shards in a DB shard group

You can use the following query to find the number of routers and shards:

```
SELECT * FROM rds_aurora.limitless_subclusters;

 subcluster_id | subcluster_type
---------------+-----------------
 1             | router
 2             | router
 3             | shard
 4             | shard
 5             | shard
 6             | shard
```

## Describing DB shard groups

Use the `describe-db-shard-groups` AWS CLI command to describe your DB shard groups. The following parameter is optional:

- `--db-shard-group-identifier` – The name of a DB shard group.

The following example describes a specific DB shard group.

```
aws rds describe-db-shard-groups --db-shard-group-identifier `my-db-shard-group`
```

The output resembles the following example.

```
{
    "DBShardGroups": [
        {
            "DBShardGroupResourceId": "shardgroup-8986d309a93c4da1b1455add17abcdef",
            "DBShardGroupIdentifier": "my-shard-group",
            "DBClusterIdentifier": "my-limitless-cluster",
            "MaxACU": 1000.0,
            "ComputeRedundancy": 0,
            "Status": "available",
            "PubliclyAccessible": false,
            "Endpoint": "my-limitless-cluster.limitless-ccetp2abcdef.us-east-1.rds.amazonaws.com"
        }
    ]
}
```

## Rebooting a DB shard group

Sometimes you have to reboot your DB shard group, for example when the `max_connections` parameter changes because of a maximum
capacity change.

You can use the AWS Management Console or AWS CLI to change the capacity of a DB shard group.

Use the following procedure.

Sign in to the AWS Management Console and open the Amazon RDS console at
[https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").

1. Navigate to the **Databases** page.
2. Select the DB shard group that you want to reboot.
3. For **Actions**, choose **Reboot**.
4. Choose **Confirm**.
   To reboot a DB shard group, use the `reboot-db-shard-group` AWS CLI command with the following parameter:

- `--db-shard-group-identifier` – The name of a DB shard group.
  The following example reboots a DB shard group.

```
aws rds reboot-db-shard-group --db-shard-group-identifier `my-db-shard-group`
```
