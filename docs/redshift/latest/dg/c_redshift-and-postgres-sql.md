Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift and PostgreSQL

###### Topics

- [Amazon Redshift and PostgreSQL JDBC and
  ODBC](c_redshift-postgres-jdbc.md "c_redshift-postgres-jdbc.md")
- [Features that are
  implemented differently](c_redshift-sql-implementated-differently.md "c_redshift-sql-implementated-differently.md")
- [Unsupported PostgreSQL
  features](c_unsupported-postgresql-features.md "c_unsupported-postgresql-features.md")
- [Unsupported PostgreSQL data
  types](c_unsupported-postgresql-datatypes.md "c_unsupported-postgresql-datatypes.md")
- [Unsupported PostgreSQL
  functions](c_unsupported-postgresql-functions.md "c_unsupported-postgresql-functions.md")
  Amazon Redshift is based on PostgreSQL. Amazon Redshift and PostgreSQL have a number of very
  important differences that you must be aware of as you design and develop your data
  warehouse applications.

Amazon Redshift is specifically designed for online analytic processing (OLAP) and business
intelligence (BI) applications, which require complex queries against large datasets.
Because it addresses very different requirements, the specialized data storage schema
and query execution engine that Amazon Redshift uses are completely different from the
PostgreSQL implementation. For example, where online transaction processing (OLTP)
applications typically store data in rows, Amazon Redshift stores data in columns, using
specialized data compression encodings for optimum memory usage and disk I/O. Some
PostgreSQL features that are suited to smaller-scale OLTP processing, such as secondary
indexes and efficient single-row data manipulation operations, have been omitted to
improve performance.

See [Amazon Redshift architecture](c_redshift_system_overview.md "c_redshift_system_overview.md") for a detailed explanation of the
Amazon Redshift data warehouse system architecture.

PostgreSQL 9.x includes some features that are not supported in Amazon Redshift. In
addition, there are important differences between Amazon Redshift SQL and PostgreSQL that you
must be aware of. This section highlights the differences between Amazon Redshift and
PostgreSQL and provides guidance for developing a data warehouse that takes full
advantage of the Amazon Redshift SQL implementation.
