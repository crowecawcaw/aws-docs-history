# View the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces

You can view a multi-Region table's provisioned capacity and auto scaling settings
on the Amazon Keyspaces console, using CQL, or the AWS CLI. This section provides examples of how to do this using CQL and the AWS CLI.

Cassandra Query Language (CQL)

###### View the provisioned capacity and auto

scaling settings of a multi-Region table using CQL

- To view the auto scaling configuration of a multi-Region table, use the following command.

```
SELECT * FROM system_multiregion_info.autoscaling WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

The output for this command looks like the following:

```
 `keyspace_name | table_name | region | provisioned_read_capacity_autoscaling_update | provisioned_write_capacity_autoscaling_update
----------------+------------+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mykeyspace | mytable | ap-southeast-1 | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 60, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 60}}} | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 0, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 0}}}
 mykeyspace | mytable | us-east-1 | {'minimum_units': 5, 'maximum_units': 20, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 60, 'disable_scale_in': false, 'target_value': 70, 'scale_in_cooldown': 60}}} | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 0, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 0}}}
 mykeyspace | mytable | eu-west-1 | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 60, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 60}}} | {'minimum_units': 5, 'maximum_units': 10, 'scaling_policy': {'target_tracking_scaling_policy_configuration': {'scale_out_cooldown': 0, 'disable_scale_in': false, 'target_value': 50, 'scale_in_cooldown': 0}}}`
```

CLI

###### View the provisioned capacity and auto

scaling settings of a multi-Region table using the AWS CLI

- To view the auto scaling configuration of a multi-Region table, you can use the
  `get-table-auto-scaling-settings` operation. The following CLI command is
  an example of this.

```
aws keyspaces get-table-auto-scaling-settings --keyspace-name mykeyspace --table-name mytable
```

You should see the following output.

```
`{
 "keyspaceName": "mykeyspace",
 "tableName": "mytable",
 "resourceArn": "arn:aws:cassandra:us-east-1:777788889999:/keyspace/mykeyspace/table/mytable",
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
 "maximumUnits": 20,
 "scalingPolicy": {
 "targetTrackingScalingPolicyConfiguration": {
 "disableScaleIn": false,
 "scaleInCooldown": 60,
 "scaleOutCooldown": 60,
 "targetValue": 70.0
 }
 }
 }
 },
 "replicaSpecifications": [
 {
 "region": "us-east-1",
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
 "maximumUnits": 20,
 "scalingPolicy": {
 "targetTrackingScalingPolicyConfiguration": {
 "disableScaleIn": false,
 "scaleInCooldown": 60,
 "scaleOutCooldown": 60,
 "targetValue": 70.0
 }
 }
 }
 }
 },
 {
 "region": "eu-north-1",
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
 }
 ]
}`
```
