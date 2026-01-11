# Pre-warm an existing table for

on-demand capacity mode in Amazon Keyspaces

Amazon Keyspaces automatically scales storage partitions based on throughput, but for new tables or new throughput
peaks, it can take longer to allocate the required storage partitions. To insure that tables in on-demand and
provisioned capacity mode have enough storage partitions to support the sudden higher throughput, you can
_pre-warm_ a new or existing table.

If you anticipate a spike in peak capacity for your table that is twice
as high as the previous peek withing the same 30 minutes, you can pre-warm the table
to the peak capacity of the expected spike.

To pre-warm an existing on-demand table
in Amazon Keyspaces, you can follow these steps. To pre-warm a new table, see [Pre-warm a new table for
on-demand capacity mode in Amazon Keyspaces](ReadWriteCapacityMode.prewarming.md "ReadWriteCapacityMode.prewarming.md").

Before you get started, review your [account and table quotas](quotas.md#table "quotas.md#table") for provisioned
mode and adjust them as needed.

Next review the required [waiting periods](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md") between changing capacity modes.
Note that you'll incur costs for the provisioned capacity until the table is back in on-demand mode.

Console

###### How to pre-warm an existing table in on-demand mode

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table that you want to work with, and go to the **Capacity** tab.
3. In the **Capacity settings** section, choose **Edit**.
4. Under **Capacity mode**, change the table to
   **Provisioned** capacity mode.
5. In the **Read capacity** section, deselect
   **Scale automatically**.

Set the table's **Provisioned capacity units** to the expected peak value. 6. In the **Write capacity** section, choose the same settings
as defined in the previous step for read capacity, or configure capacity
values manually. 7. When the provisioned capacity settings are defined, choose
**Save**. After you save changes, the table's status shows as **Updating...**
until the capacity is provisioned. Note that for large tables, the pre-warming process can take some time,
because the data needs to be divided across partitions. During this time, you can continue to access
the table and expect the previously configured peak capacity to be available. 8. When the table's status turns to **Active**, you can switch the table back to
**On-demand** capacity mode.

Cassandra Query Language (CQL)

###### Pre-warm an existing table for on-demand mode using CQL

1. Change the table's capacity mode to `PROVIOSIONED` and configure the read capacity
   and write capacity based on your expected peak values.

```

ALTER TABLE catalog.book_awards WITH CUSTOM_PROPERTIES={'capacity_mode':{'throughput_mode': 'PROVISIONED', 'read_capacity_units': 18000, 'write_capacity_units': 6000}};
```

2. Confirm that the table is active. The following statement is an example.

```
SELECT * from system_schema_mcs.tables where keyspace_name = 'catalog' and table_name = 'book_awards';
```

3. When the table's status is `ACTIVE`, you can use the following statement to change
   the capacity mode of the table to on-demand mode by setting the throughput mode to `PAY_PER_REQUEST`.
   The following statement is an example of this.

```
ALTER TABLE catalog.book_awards WITH CUSTOM_PROPERTIES={'capacity_mode':{'throughput_mode': 'PAY_PER_REQUEST'}};
```

4. You can use the following statement to confirm that the table is now in on-demand mode and see the
   table's status.

```
SELECT * from system_schema_mcs.tables where keyspace_name = 'catalog' and table_name = 'book_awards';
```

CLI

###### Pre-warm an existing table for on-demand mode using the AWS CLI

1. Change the table's capacity mode to `PROVIOSIONED` and configure the read capacity
   and write capacity based on your expected peak values. The following command is an example of this.

```
aws keyspaces update-table --keyspace-name catalog --table-name book_awards
                                    \--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=18000,writeCapacityUnits=6000
```

2. Confirm that the status of the table is active and that the capacity has been provisioned. You can use the following statement.

```
aws keyspaces get-table --keyspace-name catalog --table-name book_awards
```

3. When the table's status is `ACTIVE` and the capacity has been provisioned,
   you can use the following statement to change
   the capacity mode of the table to on-demand mode by setting the throughput mode to `PAY_PER_REQUEST`.
   The following statement is an example of this.

```
aws keyspaces update-table --keyspace-name catalog --table-name book_awards
                                    \--capacity-specification throughputMode=PAY_PER_REQUEST
```

4. You can use the following statement to confirm that the table is now in on-demand mode and see the
   table's status.

```
aws keyspaces get-table --keyspace-name catalog --table-name book_awards
```

When the table is active in on-demand capacity mode,
it's prepared to handle a similar throughput capacity as before in provisioned capacity mode.
