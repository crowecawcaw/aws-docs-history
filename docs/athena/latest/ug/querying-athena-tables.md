# Run SQL queries in Amazon Athena

You can run SQL queries using Amazon Athena on data sources that are registered with the
AWS Glue Data Catalog and data sources such as Hive metastores and Amazon DocumentDB instances that you connect
to using the Athena Federated Query feature. For more information about working with data sources, see
[Connect to data sources](work-with-data-stores.md "work-with-data-stores.md"). When you
run a Data Definition Language (DDL) query that modifies schema, Athena writes the metadata
to the metastore associated with the data source. In addition, some queries, such as
`CREATE TABLE AS` and `INSERT INTO` can write records to the
dataset—for example, adding a CSV record to an Amazon S3 location.

This section provides guidance for running Athena queries on common data sources and data
types using a variety of SQL statements. General guidance is provided for working with
common structures and operators—for example, working with arrays, concatenating,
filtering, flattening, and sorting. Other examples include queries for data in tables with
nested structures and maps, tables based on JSON-encoded datasets, and datasets associated
with AWS services such as AWS CloudTrail logs and Amazon EMR logs. Comprehensive coverage of standard
SQL usage is beyond the scope of this documentation. For more information about SQL, refer
to the [Trino](https://trino.io/docs/current/language.html "https://trino.io/docs/current/language.html") and [Presto](https://prestodb.io/docs/current/sql.html "https://prestodb.io/docs/current/sql.html") language
references.

###### Topics

- [View query plans](query-plans.md "query-plans.md")
- [Work with query results and recent queries](querying.md "querying.md")
- [Reuse query results in Athena](reusing-query-results.md "reusing-query-results.md")
- [View query stats](query-stats.md "query-stats.md")
- [Work with views](views.md "views.md")
- [Use saved queries](saved-queries.md "saved-queries.md")
- [Use parameterized queries](querying-with-prepared-statements.md "querying-with-prepared-statements.md")
- [Use the cost-based optimizer](cost-based-optimizer.md "cost-based-optimizer.md")
- [Query S3 Express One Zone](querying-express-one-zone.md "querying-express-one-zone.md")
- [Query Amazon Glacier](querying-glacier.md "querying-glacier.md")
- [Handle schema updates](handling-schema-updates-chapter.md "handling-schema-updates-chapter.md")
- [Query arrays](querying-arrays.md "querying-arrays.md")
- [Query geospatial data](querying-geospatial-data.md "querying-geospatial-data.md")
- [Query JSON data](querying-JSON.md "querying-JSON.md")
- [Use ML with Athena](querying-mlmodel.md "querying-mlmodel.md")
- [Query with UDFs](querying-udf.md "querying-udf.md")
- [Query across regions](querying-across-regions.md "querying-across-regions.md")
- [Query the AWS Glue Data Catalog](querying-glue-catalog.md "querying-glue-catalog.md")
- [Query AWS service logs](querying-aws-service-logs.md "querying-aws-service-logs.md")
- [Query web server logs](querying-web-server-logs.md "querying-web-server-logs.md")
  For considerations and limitations, see [Considerations and limitations for SQL queries in Amazon Athena](other-notable-limitations.md "other-notable-limitations.md").
