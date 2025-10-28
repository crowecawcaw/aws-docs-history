For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Running Telegraf with the Timestream for LiveAnalytics output

plugin

You can follow the instructions below to run Telegraf with the Timestream for LiveAnalytics plugin.

1. Generate an example configuration using Telegraf.

```
telegraf --section-filter agent:inputs:outputs --input-filter cpu:mem --output-filter timestream config > example.config
```

2. Create a database in Timestream [using the management
   console](console_timestream.md#console_timestream.db.using-console "console_timestream.md#console_timestream.db.using-console"), [CLI](../../../cli/latest/reference/timestream-write/create-database.md "../../../cli/latest/reference/timestream-write/create-database.md"), or [SDKs](getting-started-sdks.md "getting-started-sdks.md").
3. In the `example.config` file, add your database name by
   editing the following key under the `[[outputs.timestream]]`
   section.

```
database_name = "yourDatabaseNameHere"
```

4. By default, Telegraf will create a table. If you wish create a table manually,
   set `create_table_if_not_exists` to `false` and follow the
   instructions to create a table [using the management
   console](console_timestream.md#console_timestream.table.using-console "console_timestream.md#console_timestream.table.using-console"), [CLI](../../../cli/latest/reference/timestream-write/create-table.md "../../../cli/latest/reference/timestream-write/create-table.md"),
   or [SDKs](getting-started-sdks.md "getting-started-sdks.md").
5. In the _example.config_ file, configure credentials under
   the `[[outputs.timestream]]` section. The credentials should allow
   the following operations.

```
timestream:DescribeEndpoints
timestream:WriteRecords

```

###### Note

If you leave `create_table_if_not_exists` set to
`true`, include:

```
timestream:CreateTable
```

###### Note

If you set `describe_database_on_start` to `true`,
include the following.

```
timestream:DescribeDatabase
```

6. You can edit the rest of the configuration according to your
   preferences.
7. When you have finished editing the config file, run Telegraf with the
   following.

```
./telegraf --config example.config
```

8. Metrics should appear within a few seconds, depending on your agent
   configuration. You should also see the new tables, _cpu_ and
   _mem_, in the Timestream console.
