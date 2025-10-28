# Using AWS Lake Formation with Amazon Athena

[Amazon Athena](../../../athena/index.md "../../../athena/index.md") is a server-less
query service that helps you analyze structured, semi-structured, and unstructured data stored
in Amazon S3. You can use Athena SQL to query data from CSV, JSON, Parquet, and Avro data formats. Athena SQL
also supports table formats like [Apache Hive](https://hive.apache.org/ "https://hive.apache.org/"),
[Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/"), and [Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/"). Athena integrates with the
AWS Glue Data Catalog to store metadata of your data sets in Amazon S3. Athena can use Lake Formation to define and
maintain access control policies on those data sets.

Here are some common use cases where you can use Lake Formation with Athena.

- Use Lake Formation permissions for accessing the Data Catalog resources (database and tables) from Athena. You
  can use either the named resource method or LF-tags to define permissions on database and
  tables. For more information, see:
  - [Granting database permissions using the
    named resource method](granting-database-permissions.md "granting-database-permissions.md")
  - [Lake Formation tag-based access control](tag-based-access-control.md "tag-based-access-control.md")

###### Note

Lake Formation permissions apply only when using Athena SQL to query source data from Amazon S3 and metadata
in the Data Catalog.

Athena Spark doesn't support querying Data Catalog tables with Lake Formation permissions. Lake Formation
permissions support both read and write operations on databases and tables.

###### Note

You can't apply data filters when you use LF-Tags to manage permissions on Data Catalog
resources.

- Control the query results by using [Data filters in Lake Formation](data-filtering.md#data-filters-about "data-filtering.md#data-filters-about") to secure tables in your Amazon S3 data lakes by granting permissions at column, row, and cell-levels.
  See the [limitation on partition projection](../../../athena/latest/ug/lf-athena-limitations.md#lf-athena-limitations-data-filters "../../../athena/latest/ug/lf-athena-limitations.md#lf-athena-limitations-data-filters") in Amazon Athena User Guide.
- Enforce fine-grained access control on the data available to the SAML-based Athena user when
  running federated queries.

Athena JDBC and ODBC drivers support configuring federated access to your data source using SAML-based Identity Provider (IdP).
Use Quick Suite integrated with Lake Formation with your existing IAM role or SAML users or groups to visualize Athena query results.

###### Note

Lake Formation permissions for SAML users and groups will apply only when you submit queries to Athena using the JDBC or ODBC driver.

For more information, see [Using Lake Formation and the Athena JDBC and ODBC drivers for federated access to Athena](../../../athena/latest/ug/security-athena-lake-formation-jdbc.md "../../../athena/latest/ug/security-athena-lake-formation-jdbc.md").

###### Note

Currently, authorizing access to SAML identities in Lake Formation is not
supported in the following regions:

    + Middle East (Bahrain) - me-south-1
    + Asia Pacific (Hong Kong) - ap-east-1
    + Africa (Cape Town) - af-south-1
    + China (Ningxia) - cn-northwest-1
    + Asia Pacific (Osaka) - ap-northeast-3

- Use [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md") to
  query tables in another account.

###### Note

For more information on limitations when using Lake Formation permissions to `Views`, see [Considerations and Limitations](../../../athena/latest/ug/security-athena-lake-formation.md "../../../athena/latest/ug/security-athena-lake-formation.md").

## Support for transactional table formats

Applying Lake Formation permissions allows you to secure your transactional data in your Amazon S3
based data lakes. The table below lists transactional table formats supported in Athena
and the Lake Formation permissions. Lake Formation enforces these permissions when Athena users run their queries.

| Table format                | Description and allowed operations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Lake Formation permissions supported in Athena                                                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Apache Hudi                 | A format used to simplify incremental data processing and data pipeline development. Athena supports create and read operations using Apache Hudi table formats on Amazon S3 data sets for both **Copy on Write (CoW)** and **Merge On Read (MoR)** Hudi table types. Athena does not support write operations on Hudi tables. Use [Athena to query Hudi datasets](../../../athena/latest/ug/querying-hudi.md "../../../athena/latest/ug/querying-hudi.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Use [Data filtering and cell-level security in Lake Formation](data-filtering.md "data-filtering.md") to secure Hudi table using table, column, row, and cell-level permissions.                                                     |
| Apache Iceberg              | An open table format that manages large collections of files as tables, and supports modern analytic data lake operations such as record-level insert, update, delete, and time travel queries. For more information on Athena's support for Iceberg tables, see [Using Iceberg tables](../../../athena/latest/ug/querying-iceberg.md "../../../athena/latest/ug/querying-iceberg.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Table, column, row, and cell-level permissions are supported. Currently, Lake Formation doesn't support managing permissions on write operations such as `VACUUM`, `MERGE`, `UPDATE` and `OPTIMIZE` on tables in Open Table Formats. |
| Linux Foundation Delta Lake | Delta Lake is an open-source project that helps to implement modern data lake architectures commonly built on Amazon S3 or Hadoop Distributed File System (HDFS). Athena supports Delta lake tables created using a symlink-based manifest table definition on AWS Glue Data Catalog from a Delta Lake table. For more information, see [Crawl Delta Lake tables using AWS Glue crawlers](https://aws.amazon.com/blogs/big-data/crawl-delta-lake-tables-using-aws-glue-crawlers/ "https://aws.amazon.com/blogs/big-data/crawl-delta-lake-tables-using-aws-glue-crawlers/"). Athena (engine version 3) supports reading native Delta Lake tables. For more information, see [Introducing native Delta Lake table support with AWS Glue crawlers](https://aws.amazon.com/blogs/big-data/introducing-native-delta-lake-table-support-with-aws-glue-crawlers/ "https://aws.amazon.com/blogs/big-data/introducing-native-delta-lake-table-support-with-aws-glue-crawlers/") . | Table, column, row, and cell-level permissions are supported for symlink tables and native Delta Lake tables.                                                                                                                        | ## Additional resources ###### Blog posts, videos, and workshops <br>• [Query an Apache Hudi dataset in an Amazon S3 data lake with Amazon Athena](https://aws.amazon.com/blogs/big-data/part-1-query-an-apache-hudi-dataset-in-an-amazon-s3-data-lake-with-amazon-athena-part-1-read-optimized-queries/ "https://aws.amazon.com/blogs/big-data/part-1-query-an-apache-hudi-dataset-in-an-amazon-s3-data-lake-with-amazon-athena-part-1-read-optimized-queries/") <br>• [Build an Apache Iceberg data lake using Amazon Athena, Amazon EMR, and AWS Glue](https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/ "https://aws.amazon.com/blogs/big-data/build-an-apache-iceberg-data-lake-using-amazon-athena-amazon-emr-and-aws-glue/") <br>• [Insert, update, delete on Amazon S3 with Athena and Apache Iceberg](https://www.youtube.com/watch?v=u1v666EXCJw "https://www.youtube.com/watch?v=u1v666EXCJw") <br>• [LF-Tag based access control](https://catalog.us-east-1.prod.workshops.aws/workshops/78572df7-d2ee-4f78-b698-7cafdb55135d/en-US/lakeformation-basics/querying-datalake/tag-based-access-control "https://catalog.us-east-1.prod.workshops.aws/workshops/78572df7-d2ee-4f78-b698-7cafdb55135d/en-US/lakeformation-basics/querying-datalake/tag-based-access-control") Lake Formation workshop on querying a data lake. |
