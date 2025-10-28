# Considerations when using an external

metastore

- You can configure databases that are compatible with MariaDB JDBC as your
  metastore. Examples of these databases are RDS for MariaDB, MySQL, and Amazon Aurora.
- Metastores aren't auto-initialized. If your metastore isn't initialized with a
  schema for your Hive version, use the [Hive Schema
  Tool](https://cwiki.apache.org/confluence/display/Hive/Hive+Schema+Tool "https://cwiki.apache.org/confluence/display/Hive/Hive+Schema+Tool").
- EMR Serverless doesn't support Kerberos authentication. You can't use a thrift
  metastore server with Kerberos authentication with EMR Serverless Spark or Hive
  jobs.
- You must configure VPC access to use the multi-catalog hierarchy.
