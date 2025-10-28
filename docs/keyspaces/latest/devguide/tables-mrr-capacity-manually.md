# Set the provisioned capacity of a multi-Region table manually in Amazon Keyspaces

If you have to turn off auto scaling for a multi-Region table, you can provision the table's read capacity for a replica table
manually using CQL or the AWS CLI.

###### Note

We recommend using auto scaling for multi-Region tables that use provisioned
capacity mode. For more information, see [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md "tables-multi-region-capacity.md").

Cassandra Query Language (CQL)

###### Setting the provisioned capacity of a

multi-Region table manually using CQL

- You can use `ALTER
TABLE` to provision the table's read capacity for a replica table
  manually.

```
ALTER TABLE mykeyspace.mytable
WITH CUSTOM_PROPERTIES = {
    'capacity_mode': {
        'throughput_mode': 'PROVISIONED',
        'read_capacity_units': 1,
        'write_capacity_units': 1
    },
    'replica_updates': {
        'us-east-1': {
            'read_capacity_units': 2
         }
    }
};
```

CLI

###### Set the provisioned capacity of a

multi-Region table manually using the AWS CLI

- If you have to turn off auto scaling for a multi-Region table, you can use
  `update-table` to provision the table's read capacity for a replica table
  manually.

```
aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable \
--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=1,writeCapacityUnits=1 \
--replica-specifications region="us-east-1",readCapacityUnits=5
```
