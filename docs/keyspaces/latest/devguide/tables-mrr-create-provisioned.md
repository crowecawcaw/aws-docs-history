# Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces

This section provides examples of how to create a multi-Region table in provisioned mode with auto scaling. You can
do this on the Amazon Keyspaces console, using CQL or the AWS CLI.

For more information about supported configurations and multi-Region replication features, see [Amazon Keyspaces multi-Region replication usage notes](multiRegion-replication_usage-notes.md "multiRegion-replication_usage-notes.md").

To create a multi-Region keyspace, see [Create a multi-Region keyspace in Amazon Keyspaces](keyspaces-mrr-create.md "keyspaces-mrr-create.md").

When you create a new multi-Region table in provisioned mode with auto scaling
settings, you can specify the general settings for the table that are valid for all
AWS Regions that the table is replicated in. You can then overwrite read capacity
settings and read auto scaling settings for each replica. The write capacity, however,
remains synchronized between all replicas to ensure that there's enough capacity to
replicate writes across all Regions.

###### Note

Amazon Keyspaces automatic scaling requires the presence of a service-linked role
(`AWSServiceRoleForApplicationAutoScaling_CassandraTable`) that
performs automatic scaling actions on your behalf. This role is created automatically for
you. For more information, see [Using service-linked roles for
Amazon Keyspaces](using-service-linked-roles.md "using-service-linked-roles.md").

Console

###### Create a new multi-Region table with automatic scaling enabled

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose a multi-Region keyspace.
3. On the **Tables** tab, choose **Create
   table**.
4. On the **Create table** page in the **Table
   details** section, select a keyspace and provide a name for the new
   table.
5. In the **Columns** section, create the schema for your
   table.
6. In the **Primary key** section, define the primary key of the table and
   select optional clustering columns.
7. In the **Table settings** section, choose **Customize
   settings**.
8. Continue to **Read/write capacity settings**.
9. For **Capacity mode**, choose
   **Provisioned**.
10. In the **Read capacity** section, confirm that
    **Scale automatically** is selected.

You can select to configure the same read capacity units for all AWS Regions
that the table is replicated in. Alternatively, you can clear the check box and
configure the read capacity for each Region differently.

If you choose to configure each Region differently, you select the minimum and maximum
read capacity units for each table replica, as well as the target utilization.

    * **Minimum capacity units** – Enter the
     value for the minimum level of throughput that the table should
     always be ready to support. The value must be between 1 and the
     maximum throughput per second quota for your account (40,000 by
     default).
    * **Maximum capacity units** – Enter the maximum
     amount of throughput that you want to provision for the table. The value
     must be between 1 and the maximum throughput per second quota for your
     account (40,000 by default).
    * **Target utilization** – Enter a
     target utilization rate between 20% and 90%. When traffic
     exceeds the defined target utilization rate, capacity is
     automatically scaled up. When traffic falls below the defined
     target, it is automatically scaled down again.
    * Clear the **Scale automatically** check box if you
     want to provision the table's read capacity manually. This setting
     applies to all replicas of the table.


    ###### Note

    To ensure that there's enough read capacity for all replicas, we
     recommend Amazon Keyspaces automatic scaling for provisioned multi-Region
     tables.###### Note

To learn more about default quotas for your account and how to increase them, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md"). 11. In the **Write capacity** section, confirm that
**Scale automatically** is selected. Then configure the
capacity units for the table. The write capacity units stay synced across all
AWS Regions to ensure that there is enough capacity to replicate write events
across the Regions.

    * Clear **Scale automatically** if you want to
     provision the table's write capacity manually. This setting applies to
     all replicas of the table.


    ###### Note

    To ensure that there's enough write capacity for all replicas, we
     recommend Amazon Keyspaces automatic scaling for provisioned multi-Region
     tables.

12. Choose **Create table**. Your table is created with the
    specified automatic scaling parameters.

Cassandra Query Language (CQL)

###### Create a multi-Region table with

provisioned capacity mode and auto scaling using CQL

- To create a multi-Region table in provisioned mode with auto scaling, you must first
  specify the capacity mode by defining `CUSTOM_PROPERTIES` for the table.
  After specifying provisioned capacity mode, you can configure the auto scaling settings
  for the table using `AUTOSCALING_SETTINGS`.

For detailed information about auto scaling settings, the target
tracking policy, target value, and optional settings, see [Create a new table with automatic scaling](autoscaling.md "autoscaling.md").

To define the read capacity for a table replica in a specific Region, you can
configure the following parameters as part of the table's
`replica_updates`:

    + The Region
    + The provisioned read capacity units (optional)
    + Auto scaling settings for read capacity (optional)

The following example shows a `CREATE TABLE` statement for a multi-Region
table in provisioned mode. The general write and read capacity auto scaling settings are
the same. However, the read auto scaling settings specify additional cooldown periods of
60 seconds before scaling the table's read capacity up or down. In addition, the read
capacity auto scaling settings for the Region US East (N. Virginia) are higher than those
for other replicas. Also, the target value is set to 70% instead of 50%.

```
CREATE TABLE mykeyspace.mytable(pk int, ck int, PRIMARY KEY (pk, ck))
WITH CUSTOM_PROPERTIES = {
    'capacity_mode': {
        'throughput_mode': 'PROVISIONED',
        'read_capacity_units': 5,
        'write_capacity_units': 5
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

###### Create a new multi-Region table in

provisioned mode with auto scaling using the AWS CLI

- To create a multi-Region table in provisioned mode with auto scaling configuration,
  you can use the AWS CLI. Note that you must use the Amazon Keyspaces CLI `create-table`
  command to configure multi-Region auto scaling settings. This is because Application Auto Scaling, the
  service that Amazon Keyspaces uses to perform auto scaling on your behalf, doesn't support multiple
  Regions.

For more information about auto scaling settings, the target tracking policy, target
value, and optional settings, see [Create a new table with automatic scaling](autoscaling.md "autoscaling.md").

To define the read capacity for a table replica in a specific Region, you can
configure the following parameters as part of the table's
`replicaSpecifications`:

    + The Region
    + The provisioned read capacity units (optional)
    + Auto scaling settings for read capacity (optional)

When you're creating provisioned multi-Region tables with complex auto scaling
settings and different configurations for table replicas, it's helpful to load the
table's auto scaling settings and replica configurations from JSON files.

To use the following code example, you can download the example JSON files from [auto-scaling.zip](samples/auto-scaling.md "samples/auto-scaling.md"), and extract
`auto-scaling.json` and `replication.json`.
Take note of the path to the files.

In this example, the JSON files are located in the current directory. For different
file path options, see [How to load parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how "../../../cli/latest/userguide/cli-usage-parameters-file.md#cli-usage-parameters-file-how").

```
aws keyspaces create-table --keyspace-name mykeyspace --table-name mytable \
--schema-definition 'allColumns=[{name=pk,type=int},{name=ck,type=int}],partitionKeys=[{name=pk},{name=ck}]' \
--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1 \
--auto-scaling-specification file://auto-scaling.json \
--replica-specifications file://replication.json
```
