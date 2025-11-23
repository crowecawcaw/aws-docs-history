# View states for Amazon EC2 High Availability for SQL Server

You can view the Amazon EC2 High Availability for SQL Server (SQL HA) current and historical states. Use one of the following
methods:

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances**.
3. Select the instances in the High Availability deployment for which to view the SQL HA
   states, then choose the **SQL High Availability** tab.

AWS CLI
To view the current SQL HA states for Amazon EC2 instances, use the [describe-instance-sql-ha-states](../../../cli/latest/reference/ec2/describe-instance-sql-ha-states.md "../../../cli/latest/reference/ec2/describe-instance-sql-ha-states.md")
command. This command only shows the current SQL HA status of your onboarded instances.

```
aws ec2 describe-instance-sql-ha-states \
--instance-ids `instance_ids`
```

To view the historical SQL HA states for instances, use the [describe-instance-sql-ha-history-states](../../../cli/latest/reference/ec2/describe-instance-sql-ha-history-states.md "../../../cli/latest/reference/ec2/describe-instance-sql-ha-history-states.md") command. This command returns your SQL HA instance
state transitions in descending time order.

```
aws ec2 describe-instance-sql-ha-history-states \
--instance-ids `instance_ids` \
--start-time `period_start_timestamp` \
--end-time `period_end_timestamp`
```
