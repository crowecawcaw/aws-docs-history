

# Monitoring data quality in the AWS Glue Data Catalog

With data quality monitoring at the catalog and database level, AWS Glue Data Quality evaluates the tables in your AWS Glue Data Catalog without data quality runs that you set up for each table. You create a data quality evaluation configuration at the catalog or database level, and AWS Glue Data Quality evaluates every table in scope, including tables that you add later. For a table that needs different checks, you can also create a configuration at the table level.

A configuration evaluates tables once, on a schedule, or when table metadata changes. It uses a built-in ruleset to gather baseline statistics for every column, or your own Data Quality Definition Language (DQDL) ruleset. The statistics also build the history that AWS Glue Data Quality anomaly detection uses to flag unexpected changes in your data. Results are stored with each table.

Data quality monitoring at the catalog and database level works with tables in Amazon S3 and Amazon S3 Tables. For more information, see the following topics:
+ [Data quality monitoring at the catalog and database level](data-quality-catalog-monitoring.md)
+ [Getting started with data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-getting-started.md)
+ [IAM permissions for data quality evaluation configurations](data-quality-authorization.md#data-quality-authorization-evaluation-configs)
+ [Troubleshooting data quality monitoring at the catalog and database level](data-quality-catalog-monitoring-troubleshooting.md)