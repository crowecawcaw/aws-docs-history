# Deleting a DB shard group

You can delete a DB shard group if necessary. Deleting the DB shard group deletes the compute nodes (shards and routers), but not the
storage.

Sign in to the AWS Management Console and open the Amazon RDS console at
[https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").

1. Navigate to the **Databases** page.
2. Select the DB shard group that you want to delete.
3. For **Actions**, choose **Delete**.
4. Enter `delete me` in the box, then choose **Delete**.
   The DB shard group is deleted.

To delete your DB shard group, use the `delete-db-shard-group` AWS CLI command with the following parameter:

- `--db-shard-group-identifier` – The name of the DB shard group.
  The following example deletes a DB shard group in the Aurora PostgreSQL DB cluster that you created previously.

```
aws rds delete-db-shard-group --db-shard-group-identifier `my-db-shard-group`
```
