# Override connection properties

Your administrator's predefined connection definitions may not have the exact parameters
you need to connect to a specific data store. You can add or override parameters in the
connection string by using the `--connection-properties` argument.

The arguments are applied in the following order of precedence:

1. Overridden connection properties provided as inline arguments.
2. Connection properties present in the AWS Secrets Manager.
3. Connection properties in the AWS Glue connection.
   If the same connection property is present in all three (command line argument, Secrets Manager,
   and connection), the value provided in the command line argument takes precedence.

For more information on the available connection properties per data source, see the
[Connection parameters](sagemaker-sql-extension-connection-properties.md "sagemaker-sql-extension-connection-properties.md").

The following example illustrates a connection property argument that sets the schema
name for Amazon Athena.

```
%%sm_sql --connection-properties '{"schema_name": "`athena-db-name`"}' --metastore-id `athena-connection-name` --metastore-type GLUE_CONNECTION
```
