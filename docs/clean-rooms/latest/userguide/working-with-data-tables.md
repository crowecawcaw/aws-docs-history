# Prepare data tables in AWS Clean Rooms

###### Note

Preparing data tables can take place before or after you have joined a collaboration.
After a table is prepared, you can reuse it across multiple collaborations as long as your
privacy needs for that table are the same.

As a member in the collaboration, you must prepare your data tables before they can be
queried in AWS Clean Rooms by the collaboration member who can query.

The data tables that you use for queries in AWS Clean Rooms are commonly the same types of data
tables that you use for other applications. For example, the same types of datasets are used
with Amazon Athena, Amazon EMR, Amazon Redshift Spectrum, and Amazon Quick Suite.

You can query the data in its original format directly from any of the following data
sources:

- Amazon Simple Storage Service (Amazon S3)
- Amazon Athena
- Snowflake
  AWS Clean Rooms accesses the dataset at query run time, ensuring that members who can query always
  access the most up-to-date data. Any data that is temporarily read into an AWS Clean Rooms collaboration
  is deleted after the query completes. The query results are written to your Amazon S3 bucket.

If your use case involves querying identity data, see [AWS Entity Resolution in AWS Clean Rooms](working-with-entity-resolution.md "working-with-entity-resolution.md").

###### Topics

- [Data formats for AWS Clean Rooms](data-formats.md "data-formats.md")
- [Apache Iceberg tables in AWS Clean Rooms](iceberg-tables.md "iceberg-tables.md")
- [Preparing data tables for queries in AWS Clean Rooms](prepare-data.md "prepare-data.md")
- [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md")
- [Decrypting data tables with the C3R encryption client](decrypt-data.md "decrypt-data.md")
