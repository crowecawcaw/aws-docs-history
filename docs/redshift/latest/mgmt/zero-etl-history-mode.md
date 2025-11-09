Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# History mode

With history mode, you can configure your zero-ETL integrations to track every version (including
updates and deletes) of your records in source tables, directly in Amazon Redshift. You can run advanced
analytics on all your data, such as, run a historical analysis, build look-back reports,
perform trend analysis, and send incremental updates to downstream applications built on top
of Amazon Redshift. History mode is supported with multiple Amazon Redshift zero-ETL integrations, including Amazon Aurora MySQL,
Amazon Aurora PostgreSQL, Amazon RDS for MySQL, and Amazon DynamoDB. History mode is also supported by several
applications, such as Salesforce, SAP, ServiceNow, and Zendesk.

You can turn on and off history mode for your zero-ETL integrations from the Amazon Redshift console
([https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/")). Use history mode to keep track of records that have been deleted or
modified in the source of integration. Tracking happens in the target Amazon Redshift data warehouse.
Turning on history mode does not impact the performance of regular analytic queries on these
tables.

After you turn on history mode, tables that you drop within the source won't be dropped in
Amazon Redshift. Instead, tables will appear in a `DroppedSource` state and you can still
query these tables. You can also still use the DROP and RENAME commands with regular
SQL.

If you want to reuse the same table name on the source, you must DROP or RENAME the
corresponding `DroppedState` table before it can be replicated to Amazon Redshift. Make sure
to do so before you create the table on the source.

For information about what to consider when using history mode, see [Considerations when using history
mode on the target](zero-etl.md#zero-etl-considerations-history-mode "zero-etl.md#zero-etl-considerations-history-mode").

###### To manage history mode for a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. From the left navigation pane, choose either the **Serverless** or
   **Provisioned clusters** dashboard. Then, choose
   **Zero-ETL integrations**.
3. Select the zero-ETL integration that you want to manage, choose **Manage history
   mode**. The **Manage history mode** window is
   displayed.
4. You can **Turn off** or **Turn on** history mode
   for a target table that is replicated from a source type that has a single source table,
   such as, Amazon DynamoDB. When the zero-ETL integration has multiple target tables possible, you can
   **Turn off for all existing and future tables**, **Turn on for
   all existing and future tables**, or **Manage history mode for
   individual tables**. The default is history mode `off` when the
   zero-ETL integration is created.

When history mode is turned `on`, the following columns are added to your
target table to keep track of changes in the source. History mode `on`
increases monthly usage and cost because Amazon Redshift doesn't delete any records in the target
tables. Any source record that is deleted or changed creates a new record in the target,
resulting in more total rows in the target with multiple record versions. Records are not
deleted from the target table when deleted or modified in the source. You can manage
target tables by deleting inactive records.

| Column name          | Data type | Description                                                                                                    |
| -------------------- | --------- | -------------------------------------------------------------------------------------------------------------- |
| \_record_is_active   | Boolean   | Indicates if a record in the target is currently active in the<br>source. True indicates the record is active. |
| \_record_create_time | Timestamp | Starting time (UTC) when the source record is active.                                                          |
| \_record_delete_time | Timestamp | Ending time (UTC) when the source record is updated or<br>deleted.                                             |

You can delete inactive records from a history mode table by filtering on records
where the column `_record_is_active` is false. The following SQL DELETE command
deletes inactive records from a table where the id column is less than or equal to 100.
After you delete records, when automatic vacuum delete runs, storage for the deleted
records is reclaimed.

```
DELETE FROM myschema.mytable where not _record_is_active AND id <= 100;
```

When history mode is turned `off`, Amazon Redshift makes a copy of your table in the
target database with active records and without the added history columns. Amazon Redshift renames
your table to
``table-name`_historical_`timestamp``
for your use. You can drop this copy of your table if you no longer need it. You can
rename these tables using the ALTER TABLE command. For example:

```
ALTER TABLE `[schema-name.]``table-name_historical_timestamp` RENAME TO `new_table_name`;
```

For more information, see [ALTER TABLE](../dg/r_ALTER_TABLE.md "../dg/r_ALTER_TABLE.md") in the
_Amazon Redshift Database Developer Guide_.
You can also manage history mode using SQL commands CREATE DATABASE and ALTER DATABASE.
For more information about how to set HISTORY_MODE, see [CREATE DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md")
in the _Amazon Redshift Database Developer Guide_.
