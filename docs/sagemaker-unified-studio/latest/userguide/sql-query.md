# Query data with SQL

Use the query editor in Amazon SageMaker Unified Studio to write SQL queries, run them against your data
sources, and visualize results, all within your project. You can work with multiple query
engines, browse your data catalog, generate SQL using natural language, and schedule
queries to run automatically.

###### Note

If your Amazon SageMaker Unified Studio domain uses IAM Identity Center (IdC), some query editor features
behave differently. See [Query editor in IdC domains](sql-query-idc.md "sql-query-idc.md") for details.

###### Topics

- [Supported query engines](#sql-query-engines "#sql-query-engines")
- [Get started with the query editor](sql-query-get-started.md "sql-query-get-started.md")
- [Write, run, and view query results](sql-query-write-run.md "sql-query-write-run.md")
- [Generate SQL with the Data Agent](sql-query-data-agent.md "sql-query-data-agent.md")
- [Save, schedule, and review queries](sql-query-save-share.md "sql-query-save-share.md")
- [Query editor in IdC domains](sql-query-idc.md "sql-query-idc.md")

## Supported query engines

The query editor supports the following engines. You can switch between engines
within the same querybook.

| Engine          | Description                                                                                                                            | SQL reference                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Amazon Athena   | Serverless query engine for data stored in Amazon S3 and AWS Glue Data Catalog.<br>Best for ad-hoc queries against lakehouse data.     | [Athena SQL reference](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md") |
| Amazon Redshift | Data warehouse engine for structured and semi-structured data. Best for<br>complex analytical queries and joins across large datasets. | [Redshift SQL reference](../../../redshift/latest/dg/c_redshift-sql.md "../../../redshift/latest/dg/c_redshift-sql.md") |
