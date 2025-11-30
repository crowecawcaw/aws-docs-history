# View your table's Amazon Keyspaces auto scaling configuration

You can use the console, CQL, or the AWS CLI to view and update the Amazon Keyspaces automatic scaling
settings of a table.

Console

###### View automatic scaling settings using the console

1. Choose the table you want to view and go to the
   **Capacity** tab.
2. In the **Capacity settings** section, choose **Edit**. You
   can now modify the settings in the **Read
   capacity** or **Write capacity**
   sections. For more information about these settings, see [Create a new table with automatic scaling](autoscaling.md "autoscaling.md").

Cassandra Query Language (CQL)
**View your table's Amazon Keyspaces automatic scaling policy using CQL**

To view details of the auto scaling configuration of a table, use the following command.

```
SELECT * FROM system_schema_mcs.autoscaling WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

The output for this command looks like this.

```
 `keyspace_name | table_name | provisioned_read_capacity_autoscaling_update | provisioned_write_capacity_autoscaling_update
---------------+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mykeyspace | mytable | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 60, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 60}}} | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 0, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 0}}}`
```

CLI
**View your table's Amazon Keyspaces automatic scaling policy using the AWS CLI**

To view the auto scaling configuration of a table, you can use the
`get-table-auto-scaling-settings` operation. The following CLI command is an example of this.

```
aws keyspaces get-table-auto-scaling-settings --keyspace-name mykeyspace --table-name mytable
```

The output for this command looks like this.

```
`{
 "keyspaceName": "mykeyspace",
 "tableName": "mytable",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable",
 "autoScalingSpecification": {
 "writeCapacityAutoScaling": {
 "autoScalingDisabled": false,
 "minimumUnits": 5,
 "maximumUnits": 10,
 "scalingPolicy": {
 "targetTrackingScalingPolicyConfiguration": {
 "disableScaleIn": false,
 "scaleInCooldown": 0,
 "scaleOutCooldown": 0,
 "targetValue": 50.0
 }
 }
 },
 "readCapacityAutoScaling": {
 "autoScalingDisabled": false,
 "minimumUnits": 5,
 "maximumUnits": 10,
 "scalingPolicy": {
 "targetTrackingScalingPolicyConfiguration": {
 "disableScaleIn": false,
 "scaleInCooldown": 60,
 "scaleOutCooldown": 60,
 "targetValue": 50.0
 }
 }
 }
 }
}`
```
