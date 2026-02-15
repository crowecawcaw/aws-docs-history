# Considerations

and limitations

When you use Athena to read Apache Hudi tables, consider the following points.

- Read and write operations – Athena can
  read compacted Hudi datasets but not write Hudi data.
- Hudi versions – Athena supports Hudi
  version 0.14.0 (default) and 0.15.0. Athena cannot guarantee read compatibility
  with tables that are created with later versions of Hudi. For more information
  about Hudi features and versioning, see the [Hudi documentation](https://hudi.apache.org/ "https://hudi.apache.org/") on the Apache website.
  Note that version 0.15.0 of the Hudi connector on Athena does not support
  bootstrapped tables. To use 0.15.0 of the
  Hudi connector, set the following table property:

```
ALTER TABLE `table_name` SET TBLPROPERTIES ('athena_enable_native_hudi_connector_implementation' = 'true')
```

- Cross account queries – Version 0.15.0
  of the Hudi connector does not support cross account queries.
- Query types – Currently, Athena supports
  snapshot queries and read optimized queries, but not incremental queries. On MoR
  tables, all data exposed to read optimized queries are compacted. This provides
  good performance but does not include the latest delta commits. Snapshot queries
  contain the freshest data but incur some computational overhead, which makes
  these queries less performant. For more information about the tradeoffs between
  table and query types, see [Table & Query
  Types](https://hudi.apache.org/docs/table_types/ "https://hudi.apache.org/docs/table_types/") in the Apache Hudi documentation.
- Incremental queries – Athena does not
  support incremental queries.
- CTAS – Athena does not support [CTAS](ctas.md "ctas.md") or [INSERT INTO](insert-into.md "insert-into.md") on Hudi data. If you
  would like Athena support for writing Hudi datasets, send feedback to
  `<athena-feedback@amazon.com>`.

For more information about writing Hudi data, see the following
resources:

    + [Working with a Hudi dataset](../../../emr/latest/ReleaseGuide/emr-hudi-work-with-dataset.md "../../../emr/latest/ReleaseGuide/emr-hudi-work-with-dataset.md") in the [Amazon EMR Release Guide](../../../emr/latest/ReleaseGuide.md "../../../emr/latest/ReleaseGuide.md").
    + [Writing Data](https://hudi.apache.org/docs/0.8.0/writing_data.html "https://hudi.apache.org/docs/0.8.0/writing_data.html") in the Apache Hudi documentation.

- MSCK REPAIR TABLE – Using MSCK REPAIR
  TABLE on Hudi tables in Athena is not supported. If you need to load a Hudi table
  not created in AWS Glue, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md").
- Skipping Amazon Glacier objects not supported –
  If objects in the Apache Hudi table are in an Amazon Glacier storage class, setting the
  `read_restored_glacier_objects` table property to
  `false` has no effect.

For example, suppose you issue the following command:

```
ALTER TABLE `table_name` SET TBLPROPERTIES ('read_restored_glacier_objects' = 'false')
```

For Iceberg and Delta Lake tables, the command produces the error
**`Unsupported table property key:
 read_restored_glacier_objects`**. For Hudi tables, the `ALTER
 TABLE` command does not produce an error, but Amazon Glacier objects are still
not skipped. Running `SELECT` queries after the `ALTER
 TABLE` command continues to return all objects.

- Timestamp queries – Currently, queries
  that attempt to read timestamp columns in Hudi real time tables either fail or
  produce empty results. This limitation applies only to queries that read a
  timestamp column. Queries that include only non-timestamp columns from the same
  table succeed.

Failed queries return a message similar to the following:

**`GENERIC_INTERNAL_ERROR: class org.apache.hadoop.io.ArrayWritable
 cannot be cast to class org.apache.hadoop.hive.serde2.io.TimestampWritableV2
 (org.apache.hadoop.io.ArrayWritable and
 org.apache.hadoop.hive.serde2.io.TimestampWritableV2 are in unnamed module
 of loader io.trino.server.PluginClassLoader @75c67992)`**
