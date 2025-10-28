# Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces

This section includes examples of how to use the console, CQL, and the AWS CLI to
manage the Amazon Keyspaces auto scaling settings of provisioned multi-Region tables. For more
information about general auto scaling configuration options and how they work, see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").

Note that if you're using provisioned capacity mode for multi-Region tables, you must
always use Amazon Keyspaces API calls to configure auto scaling. This is because the underlying
Application Auto Scaling API operations are not Region-aware.

For more information on how to estimate write capacity throughput of provisioned
multi-Region tables, see [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md "tables-multi-region-capacity.md").

For more information about the Amazon Keyspaces API, see [_Amazon Keyspaces API
Reference_](../APIReference/Welcome.md "../APIReference/Welcome.md").

When you update the provisioned mode or auto scaling settings of a multi-Region table,
you can update read capacity settings and the read auto scaling configuration for each
replica of the table.

The write capacity, however, remains synchronized between all replicas to ensure that
there's enough capacity to replicate writes across all Regions.

Cassandra Query Language (CQL)

###### Update the provisioned capacity and

auto scaling settings of a multi-Region table using CQL

- You can use `ALTER TABLE` to update the capacity mode and auto scaling
  settings of an existing table. If you're updating a table that is currently in on-demand
  capacity mode, `capacity_mode` is required. If your table is already in
  provisioned capacity mode, this field can be omitted.

For detailed information about auto scaling settings, the target tracking policy,
target value, and optional settings, see [Create a new table with automatic scaling](autoscaling.md "autoscaling.md").

In the same statement, you can also update the read capacity and auto scaling settings
of table replicas in specific Regions by updating the table's
`replica_updates` property. The following statement is an example of
this.

```
ALTER TABLE mykeyspace.mytable
WITH CUSTOM_PROPERTIES = {
    'capacity_mode': {
        'throughput_mode': 'PROVISIONED',
        'read_capacity_units': 1,
        'write_capacity_units': 1
    }
} AND AUTOSCALING_SETTINGS = {
    'provisioned_write_capacity_autoscaling_update': {
        'maximum_units': 10,
        'minimum_units': 5,
        'scaling_policy': {
            'target_tracking_scaling_policy_configuration': {
                'target_value': 50
            }
        }
    },
    'provisioned_read_capacity_autoscaling_update': {
        'maximum_units': 10,
        'minimum_units': 5,
        'scaling_policy': {
            'target_tracking_scaling_policy_configuration': {
                'target_value': 50,
                'scale_in_cooldown': 60,
                'scale_out_cooldown': 60
            }
        }
    },
    'replica_updates': {
        'us-east-1': {
            'provisioned_read_capacity_autoscaling_update': {
                'maximum_units': 20,
                'minimum_units': 5,
                'scaling_policy': {
                    'target_tracking_scaling_policy_configuration': {
                        'target_value': 70
                    }
                }
            }
        }
    }
};
```

CLI

###### Update the provisioned capacity and

auto scaling settings of a multi-Region table using the AWS CLI

- To update the provisioned mode and auto scaling configuration of an existing table,
  you can use the AWS CLI `update-table` command.

Note that you must use the Amazon Keyspaces CLI commands to create or modify multi-Region auto
scaling settings. This is because Application Auto Scaling, the service that Amazon Keyspaces uses to perform auto
scaling of table capacity on your behalf, doesn't support multiple AWS Regions.

To update the read
capacity for a table replica in a specific Region, you can change one of the following
optional parameters of the table's `replicaSpecifications`:

    + The provisioned read capacity units (optional)
    + Auto scaling settings for read capacity (optional)

When you're updating multi-Region tables with complex auto scaling settings and
different configurations for table replicas, it's helpful to load the table's auto
scaling settings and replica configurations from JSON files.

To use the following code example, you can download the example JSON files from [auto-scaling.zip](samples/auto-scaling.md "samples/auto-scaling.md"), and extract
`auto-scaling.json` and `replication.json`.
Take note of the path to the files.

In this example, the JSON files are located in the current directory. For different
file path options, see [How to load parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how "../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how").

```
aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable \
--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1 \
--auto-scaling-specification file://auto-scaling.json \
--replica-specifications file://replication.json
```
