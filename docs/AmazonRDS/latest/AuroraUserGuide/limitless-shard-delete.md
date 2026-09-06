

# Deleting a DB shard group
<a name="limitless-shard-delete"></a>

You can delete a DB shard group if necessary. Deleting the DB shard group deletes the compute nodes (shards and routers), but not the storage.

## Console
<a name="limitless-shard-delete.CON"></a>

Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to the **Databases** page.

1. Select the DB shard group that you want to delete.

1. For **Actions**, choose **Delete**.

1. Enter **delete me** in the box, then choose **Delete**.

The DB shard group is deleted.

## AWS CLI
<a name="limitless-shard-delete.CLI"></a>

To delete your DB shard group, use the `delete-db-shard-group` AWS CLI command with the following parameter:
+ `--db-shard-group-identifier` – The name of the DB shard group.

The following example deletes a DB shard group in the Aurora PostgreSQL DB cluster that you created previously.

```
aws rds delete-db-shard-group --db-shard-group-identifier {{my-db-shard-group}}
```