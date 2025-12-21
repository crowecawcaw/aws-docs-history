# Configure automatic scaling on an existing table

You can update an existing Amazon Keyspaces table to turn on auto scaling for the table's write or
read capacity. If you're updating a table
that is currently in on-demand capacity mode, than you first have to change the table's capacity mode
to provisioned capacity mode.

For more information on how to update auto scaling settings for a multi-Region table, see
[Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md "tables-mrr-autoscaling.md").

Amazon Keyspaces automatic scaling requires the presence of a service-linked role
(`AWSServiceRoleForApplicationAutoScaling_CassandraTable`) that
performs automatic scaling actions on your behalf. This role is created
automatically for you. For more information, see [Using service-linked roles for
Amazon Keyspaces](using-service-linked-roles.md "using-service-linked-roles.md").

Console

###### Configure Amazon Keyspaces automatic scaling for an existing table

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table that you want to work with, and go to the **Capacity** tab.
3. In the **Capacity settings** section, choose **Edit**.
4. Under **Capacity mode**, make sure that the table is using
   **Provisioned** capacity mode.
5. Select **Scale automatically** and see step 6 in
   [Create a new table with automatic scaling](autoscaling.md "autoscaling.md") to edit read and write
   capacity.
6. When the automatic scaling settings are defined, choose
   **Save**.

Cassandra Query Language (CQL)
**Configure an existing table with Amazon Keyspaces automatic scaling using CQL**

You can use the `ALTER TABLE` statement for an existing Amazon Keyspaces table to configure auto scaling for the table's write or
read capacity. If you're updating a table
that is currently in on-demand capacity mode, you have to set `capacity_mode` to provisioned.
If your table is already in provisioned capacity mode, this field can be
omitted.

In the following example, the statement updates the table
_mytable_, which is in on-demand capacity mode. The statement changes
the capacity mode of the table to provisioned mode with auto scaling enabled.

The write capacity is configured within the range of 5–10 capacity units with a
target value of 50%. The read capacity is also configured within the range of
5–10 capacity units with a target value of 50%. For read capacity, you set the
values for `scale_out_cooldown` and `scale_in_cooldown` to 60
seconds.

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
    }
};
```

CLI
**Configure an existing table with Amazon Keyspaces automatic scaling using the AWS CLI**

For an existing Amazon Keyspaces table, you can turn on auto scaling for the table's write or
read capacity using the `UpdateTable` operation.

You can use the following command to turn on Amazon Keyspaces auto scaling for an existing table.
The auto scaling settings for the table are loaded from a JSON file. For the following
example, you can download the example JSON file from [auto-scaling.zip](samples/auto-scaling.md "samples/auto-scaling.md") and extract
`auto-scaling.json`, taking note of the path to the file. In this
example, the JSON file is located in the current directory. For different file path
options, see [How to load parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how "../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how").

For more information about the auto scaling settings used in the following
example, see [Create a new table with automatic scaling](autoscaling.md "autoscaling.md").

```
aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable
            \ --capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1
            \ --auto-scaling-specification file://auto-scaling.json
```
