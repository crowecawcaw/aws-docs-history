# Loading data from an Aurora PostgreSQL DB cluster or RDS for PostgreSQL DB instance

After you complete the resource and authentication setup, connect to the cluster endpoint and call the
`rds_aurora.limitless_data_load_start` stored procedure from a limitless database, such as `postgres_limitless`. The
limitless database is a database on the DB shard group into which you want to migrate data.

This function connects asynchronously in the background to the source database specified in the command, reads the data from the source, and
loads the data onto the shards. For better performance, the data is loaded using parallel threads. The function retrieves a point-in-time table
snapshot by running a `SELECT` command to read the data of the table(s) provided in the command.

You can load data into sharded, reference, and standard tables.

You can load data at the database, schema, or table level in `rds_aurora.limitless_data_load_start` calls.

- Database – You can load one database at a time in each call, with no limit on the schema or table count within the
  database.
- Schema – You can load a maximum of 15 schemas in each call, with no limit on the table count within each schema.
- Table – You can load a maximum of 15 tables in each call.

###### Note

This feature doesn't use Amazon RDS snapshots or point-in-time isolation of the database. For consistency across tables, we recommend cloning
the source database and pointing to that cloned database as the source.

The stored procedure uses the following syntax:

```
CALL rds_aurora.limitless_data_load_start('`source_type`',
    '`source_DB_cluster_or_instance_ID`',
    '`source_database_name`',
    '`streaming_mode'`,
    '`data_loading_IAM_role_arn`',
    '`source_DB_secret_arn`',
    '`destination_DB_secret_arn`',
    '`ignore_primary_key_conflict_boolean_flag`',
    '`is_dry_run`',
    (optional parameter) schemas/tables => ARRAY['`name1`', '`name2`', ...]);
```

The input parameters are the following:

- `source_type` – The source type: `aurora_postgresql` or `rds_postgresql`
- `source_DB_cluster_or_instance_ID` – The source Aurora PostgreSQL DB cluster identifier or RDS for PostgreSQL DB instance
  identifier
- `source_database_name` – The source database name, such as `postgres`
- `streaming_mode` – Whether to include change data capture (CDC): `full_load` or
  `full_load_and_cdc`
- `data_loading_IAM_role_arn` – The IAM role Amazon Resource Name (ARN) for `aurora-data-loader`
- `source_DB_secret_arn` – The source DB secret ARN
- `destination_DB_secret_arn` – The destination DB secret ARN
- `ignore_primary_key_conflict_boolean_flag` – Whether to continue if a primary key conflict occurs:
  - If set to `true`, data loading ignores new changes for rows with a primary key conflict.
  - If set to `false`, data loading overwrites the existing rows on destination tables when it encounters a primary key
    conflict.

- `is_dry_run` – Whether to test that the data loading job can connect to the source and destination databases:
  - If set to `true`, tests the connections without loading data
  - If set to `false`, loads the data

- (optional) `schemas` or `tables` – An array of schemas or tables to load. You can specify either of the
  following:

      + A list of tables in the format `tables => ARRAY['`schema1`.`table1`',
       '`schema1`.`table2`',
       '`schema2`.`table1`', ...]`
      + A list of schemas in the format `schemas => ARRAY[`'schema1`',
       '`schema2`', ...]`

  If you don't include this parameter, the entire specified source database is migrated.
  The output parameter is the job ID with a message.

The following example shows how to use the `rds_aurora.limitless_data_load_start` stored procedure to load data from an
Aurora PostgreSQL DB cluster.

```
CALL rds_aurora.limitless_data_load_start('aurora_postgresql',
    'my-db-cluster',
    'postgres',
    'full_load_and_cdc',
    'arn:aws:iam::123456789012:role/aurora-data-loader-8f2c66',
    'arn:aws:secretsmanager:us-east-1:123456789012:secret:secret-source-8f2c66-EWrr0V',
    'arn:aws:secretsmanager:us-east-1:123456789012:secret:secret-destination-8f2c66-d04fbD',
    'true',
    'false',
    tables => ARRAY['public.customer', 'public.order', 'public.orderdetails']);

INFO: limitless data load job id 1688761223647 is starting.
```
