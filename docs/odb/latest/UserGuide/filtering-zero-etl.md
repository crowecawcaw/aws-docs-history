# Data filtering for zero-ETL integrations in

Oracle Database@AWS

Oracle Database@AWS zero-ETL integrations support data filtering. You can use it to control which data
your source Oracle Exadata database replicates to your target data warehouse. Instead of
replicating the entire database, you can apply one or more filters to selectively include or
exclude specific tables. This helps you optimize storage and query performance by ensuring that
only relevant data is transferred. Filtering is limited to the database and table levels.
Column- and row-level filtering aren't supported.

Oracle Database and Amazon Redshift handle object name casing differently, which affects
both data filter configuration and target queries. Note the following:

- Oracle Database stores database, schema, and object names in uppercase unless explicitly
  quoted in the `CREATE` statement. For example, if you create `mytable`
  (no quotes), the Oracle data dictionary stores the table name as `MYTABLE`. If
  you quote the object name in your creation statement, the Oracle data dictionary preserves
  the case.
- Zero-ETL data filters are case sensitive and must match the exact case of object names
  as they appear in the Oracle data dictionary. For example, if the Oracle dictionary stores
  schema and table name `REINVENT.MYTABLE`, then create a filter using
  `include: ORCL.REINVENT.MYTABLE`.
- Amazon Redshift queries default to lowercase object names unless explicitly quoted. For
  example, a query of `MYTABLE` (no quotes) searches for
  `mytable`.
  Be mindful of the case differences when you create the Amazon Redshift filter and query the
  data. The filtering considerations for Oracle Database@AWS are the same as for Amazon RDS for Oracle. For examples
  of how case can affect data filters in an Oracle database, see [RDS for Oracle examples](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.filtering-examples-oracle "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.filtering-examples-oracle") in the _Amazon Relational Database Service User Guide_.
