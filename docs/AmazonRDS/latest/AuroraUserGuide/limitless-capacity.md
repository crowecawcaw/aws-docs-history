

# Changing the capacity of a DB shard group
<a name="limitless-capacity"></a>

You can use the AWS Management Console or AWS CLI to change the capacity of a DB shard group.

## Console
<a name="limitless-capacity.CON"></a>

Use the following procedure.

Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to the **Databases** page.

1. Select the DB shard group that you want to modify.

1. For **Actions**, choose **Modify**.

   The **Modify DB shard group** page displays.  
![Modify DB shard group page.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/limitless_modify_shard_group.png)

1. Enter a new **Minimum capacity (ACUs)** value, for example **100**.

1. Enter a new **Maximum capacity (ACUs)** value, for example **1000**.

1. Choose **Continue**.

   The confirmation page displays, with a summary of your changes.

1. Review your changes, then choose **Modify DB shard group**.

## CLI
<a name="limitless-capacity.CLI"></a>

Use the `modify-db-shard-group` AWS CLI command with the following parameters:
+ `--db-shard-group-identifier` – The name of the DB shard group.
+ `--max-acu` – The new maximum capacity of the DB shard group. You can set the maximum capacity of the DB shard group to 16–6144 ACUs. For capacity limits higher than 6144 ACUs, contact AWS.

  The number of routers and shards doesn't change.
+ `--min-acu` – The new minimum capacity of your DB shard group. It must be at least 16 ACUs, which is the default value.

The following CLI example changes the capacity range of a DB shard group to 100–1000 ACUs.

```
aws rds modify-db-shard-group \
    --db-shard-group-identifier {{my-db-shard-group}} \
    --min-acu 100 \
    --max-acu 1000
```