# Step 3: Set throughput capacity for the

table

This tutorial shows you how to tune cqlsh to load data within a set time range.
Because you know how many reads and writes you perform in advance, use provisioned
capacity mode. After you finish the data transfer, you should set the capacity mode of
the table to match your application’s traffic patterns. To learn more about capacity
management, see [Managing serverless resources in
Amazon Keyspaces (for Apache Cassandra)](serverless_resource_management.md "serverless_resource_management.md").

With provisioned capacity mode, you specify how much read and write capacity you want
to provision to your table in advance. Write capacity is billed hourly and metered in
write capacity units (WCUs). Each WCU is enough write capacity to support writing 1 KB
of data per second. When you load the data, the write rate must be under the max WCUs
(parameter: `write_capacity_units`) that are set on the target table.

By default, you can provision up to 40,000 WCUs to a table and 80,000 WCUs across all
the tables in your account. If you need additional capacity, you can request a quota
increase in the [Service Quotas](https://console.aws.amazon.com/servicequotas/home#!/services/cassandra/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/cassandra/quotas") console. For more information about quotas, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

###### Calculate the average number of WCUs required for an insert

Inserting 1 KB of data per second requires 1 WCU. If your CSV file has 360,000
rows and you want to load all the data in 1 hour, you must write 100 rows per second
(360,000 rows / 60 minutes / 60 seconds = 100 rows per second). If each row has up
to 1 KB of data, to insert 100 rows per second, you must provision 100 WCUs to your
table. If each row has 1.5 KB of data, you need two WCUs to insert one row per
second. Therefore, to insert 100 rows per second, you must provision 200
WCUs.

To determine how many WCUs you need to insert one row per second, divide the average
row size in bytes by 1024 and round up to the nearest whole number.

For example, if the average row size is 3000 bytes, you need three WCUs to insert one
row per second.

```
ROUNDUP(3000 / 1024) = ROUNDUP(2.93) = 3 WCUs
```

###### Calculate data load time and capacity

Now that you know the average size and number of rows in your CSV file, you can
calculate how many WCUs you need to load the data in a given amount of time, and the
approximate time it takes to load all the data in your CSV file using different WCU
settings.

For example, if each row in your file is 1 KB and you have 1,000,000 rows in your CSV
file, to load the data in 1 hour, you need to provision at least 278 WCUs to your table
for that hour.

```
1,000,000 rows * 1 KBs = 1,000,000 KBs
1,000,000 KBs / 3600 seconds =277.8 KBs / second = 278 WCUs
```

###### Configure provisioned capacity settings

You can set a table’s write capacity settings when you create the table or by
using the `ALTER TABLE` CQL command. The following is the syntax for altering
a table’s provisioned capacity settings with the `ALTER TABLE`
CQL statement.

```
ALTER TABLE `mykeyspace.mytable` WITH custom_properties={'capacity_mode':{'throughput_mode': 'PROVISIONED', 'read_capacity_units': `100`, 'write_capacity_units': `278`}} ;
```

For the complete language reference, see [ALTER TABLE](cql.ddl.md#cql.ddl.table.alter "cql.ddl.md#cql.ddl.table.alter").
