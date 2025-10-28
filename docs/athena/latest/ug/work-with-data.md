# Create databases and tables

Amazon Athena supports a subset of data definition language (DDL) statements and ANSI SQL
functions and operators to define and query external tables where data resides in Amazon Simple Storage Service.

When you create a database and table in Athena, you describe the schema and the location of
the data, making the data in the table ready for real-time querying.

To improve query performance and reduce costs, we recommend that you partition your data
and use open source columnar formats for storage in Amazon S3, such as [Apache parquet](https://parquet.apache.org "https://parquet.apache.org") or [ORC](https://orc.apache.org/ "https://orc.apache.org/").

###### Topics

- [Create databases](creating-databases.md "creating-databases.md")
- [Create tables](creating-tables.md "creating-tables.md")
- [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md")
- [Escape reserved keywords](reserved-words.md "reserved-words.md")
