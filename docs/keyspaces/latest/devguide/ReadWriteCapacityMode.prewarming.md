# Pre-warm a new table for

on-demand capacity mode in Amazon Keyspaces

Amazon Keyspaces automatically scales storage partitions based on throughput, but for new tables or new throughput
peaks, it can take longer to allocate the required storage partitions. To insure that tables in on-demand and
provisioned capacity mode have enough storage partitions to support the sudden higher throughput, you can
_pre-warm_ a new or existing table.

A common scenario for pre-warming a new table is when you're migrating data
from another database, which may require loading terabytes of data in a short period of time.

For on-demand tables, Amazon Keyspaces automatically allocates more capacity as your traffic volume increases.
New on-demand tables can sustain up to 4,000 writes per second and 12,000 strongly consistent reads
or 24,000 eventually consistent reads per second. An on-demand table grows traffic based on previously
recorded throughput over time.

If you anticipate a spike in peak capacity that exceeds the settings for new tables,
you can pre-warm the table to the peak capacity of the expected spike.

To pre-warm a new table for on-demand capacity mode in Amazon Keyspaces, you can follow these steps. To pre-warm an
existing table, see [Pre-warm an existing table for
on-demand capacity mode in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

Before you get started, review your [account and table quotas](quotas.md#table "quotas.md#table") for provisioned mode and adjust them as needed.

Console

###### How to pre-warm a new table for on-demand capacity mode

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose
   **Create table**.
3. On the **Create table** page in the **Table
   details** section, select a keyspace and provide a name for the new
   table.
4. In the **Columns** section, create the schema for your
   table.
5. In the **Primary key** section, define the primary key of the table and
   select optional clustering columns.
6. In the **Table settings** section, choose **Customize
   settings**.
7. Continue to **Read/write capacity settings**.
8. For **Capacity mode**, choose
   **Provisioned**.
9. In the **Read capacity** section, deselect
   **Scale automatically**.

Set the table's **Provisioned capacity units** to the expected peak value. 10. In the **Write capacity** section, choose the same settings
as defined in the previous step for read capacity, or configure capacity
values manually. 11. Choose **Create table**. Your table is getting created with the
specified capacity settings. 12. When the table's status turns to **Active**, you can switch the table to
**On-demand** capacity mode.

Cassandra Query Language (CQL)

###### Pre-warm a new table for on-demand mode using CQL

1. Create a new table in provisioned mode and specify the expected peak capacity for reads and
   writes for the new table. The following statement is an example of this.

```
CREATE TABLE catalog.book_awards (
   year int,
   award text,
   rank int,
   category text,
   book_title text,
   author text,
   publisher text,
   PRIMARY KEY ((year, award), category, rank))
WITH CUSTOM_PROPERTIES = {
    'capacity_mode': {
        'throughput_mode': 'PROVISIONED',
        'read_capacity_units': 18000,
        'write_capacity_units': 6000
     }
};
```

2. Confirm the status of the table. You can use the following statement.

```
SELECT keyspace_name, table_name, status FROM system_schema_mcs.tables WHERE keyspace_name = 'catalog' AND table_name = 'book_awards';

 keyspace_name | table_name      | status
---------------+-----------------+--------
       catalog | book_awards     | ACTIVE

(1 rows)
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

###### Pre-warm a new table for on-demand capacity mode using the AWS CLI

1. Create a new table in provisioned mode and specify the expected peak capacity values for reads
   and writes for the new table. The following statement is an
   example of this.

```
aws keyspaces create-table --keyspace-name catalog --table-name book_awards
                                    \--schema-definition 'allColumns=[{name=pk,type=int},{name=ck,type=int}],partitionKeys=[{name=pk},{name=ck}]'
                                    \--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=18000,writeCapacityUnits=6000
```

2. Confirm the status of the table. You can use the following statement.

```
aws keyspaces get-table --keyspace-name catalog --table-name book_awards
```

3. When the table is active and the capacity has been provisioned, you can change the table to
   on-demand mode. The following is an example of this.

```
aws keyspaces update-table --keyspace-name catalog --table-name book_awards --capacity-specification throughputMode=PAY_PER_REQUEST
```

4. You can use the following statement to confirm that the table is now in on-demand mode and see the
   table's status.

```
aws keyspaces get-table --keyspace-name catalog --table-name book_awards
```

When the table is active in on-demand capacity mode,
it's prepared to handle a similar throughput capacity as before in provisioned capacity mode.
