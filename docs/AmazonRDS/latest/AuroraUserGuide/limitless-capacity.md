# Changing the capacity of a DB shard group

You can use the AWS Management Console or AWS CLI to change the capacity of a DB shard group.

Use the following procedure.

Sign in to the AWS Management Console and open the Amazon RDS console at
[https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").

1. Navigate to the **Databases** page.
2. Select the DB shard group that you want to modify.
3. For **Actions**, choose **Modify**.

The **Modify DB shard group** page displays.

![Modify DB shard group page.](images/limitless_modify_shard_group.png) 4. Enter a new **Minimum capacity (ACUs)** value, for example `100`. 5. Enter a new **Maximum capacity (ACUs)** value, for example `1000`. 6. Choose **Continue**.

The confirmation page displays, with a summary of your changes. 7. Review your changes, then choose **Modify DB shard group**.
Use the `modify-db-shard-group` AWS CLI command with the following parameters:

- `--db-shard-group-identifier` – The name of the DB shard group.
- `--max-acu` – The new maximum capacity of the DB shard group. You can set the maximum capacity of the DB shard
  group to 16–6144 ACUs. For capacity limits higher than 6144 ACUs, contact AWS.

The number of routers and shards doesn't change.

- `--min-acu` – The new minimum capacity of your DB shard group. It must be at least 16 ACUs, which is the default
  value.
  The following CLI example changes the capacity range of a DB shard group to 100–1000 ACUs.

```
aws rds modify-db-shard-group \
    --db-shard-group-identifier `my-db-shard-group` \
    --min-acu 100 \
    --max-acu 1000
```
