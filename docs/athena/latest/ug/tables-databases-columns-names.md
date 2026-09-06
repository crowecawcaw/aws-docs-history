

# Name databases, tables, and columns
<a name="tables-databases-columns-names"></a>

Use these guidelines for naming databases, tables, and columns in Athena.

## Database, table, and column name requirements
<a name="tables-databases-columns-names-requirements"></a>
+ Acceptable characters for database names, table names, and column names in AWS Glue must be a UTF-8 string and should be in lower case. Note that Athena automatically lowers any upper case names in DDL queries when it creates databases, tables, or columns. The string must not be less than 1 or more than 255 bytes long.
+ Currently, it is possible to have leading spaces at the start of names. Because these leading spaces can be hard to detect and can cause usability issues after creation, avoid inadvertently creating object names that have leading spaces.
+ If you use an [AWS::Glue::Database](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html) CloudFormation template to create an AWS Glue database and do not specify a database name, AWS Glue automatically generates a database name in the format {{resource\_name–random\_string}} that is not compatible with Athena.
+ You can use the AWS Glue Catalog Manager to rename columns, but not table names or database names. To work around this limitation, you must use a definition of the old database to create a database with the new name. Then you use definitions of the tables from the old database to re-create the tables in the new database. To do this, you can use the AWS CLI or AWS Glue SDK. For steps, see [Use the AWS CLI to recreate an AWS Glue database and its tables](glue-recreate-db-and-tables-cli.md).

## Use lower case for table names and table column names in Athena
<a name="table-names-and-table-column-names-in-ate-must-be-lowercase"></a>

Athena accepts mixed case in DDL and DML queries, but lower cases the names when it executes the query. For this reason, avoid using mixed case for table or column names, and do not rely on casing alone in Athena to distinguish such names. For example, if you use a DDL statement to create a column named `Castle`, the column created will be lowercased to `castle`. If you then specify the column name in a DML query as `Castle` or `CASTLE`, Athena will lowercase the name for you to run the query, but display the column heading using the casing that you chose in the query.

Database, table, and column names must be less than or equal to 255 characters long.

## Names that begin with an underscore
<a name="names-that-begin-with-an-underscore"></a>

When creating tables, use backticks to enclose table, view, or column names that begin with an underscore. For example:

```
CREATE EXTERNAL TABLE IF NOT EXISTS `_myunderscoretable`(
  `_id` string, `_index` string)
LOCATION 's3://amzn-s3-demo-bucket/'
```

## Table, view, or column names that begin with numbers
<a name="table-names-that-include-numbers"></a>

When running `SELECT`, `CTAS`, or `VIEW` queries, put quotation marks around identifiers like table, view, or column names that start with a digit. For example:

```
CREATE OR REPLACE VIEW "123view" AS
SELECT "123columnone", "123columntwo"
FROM "234table"
```

## Column names and complex types
<a name="tables-databases-columns-names-complex-types"></a>

For complex types, only alphanumeric characters, underscore (`_`), and period (`.`) are allowed in column names. To create a table and mappings for keys that have restricted characters, you can use a custom DDL statement. For more information, see the article [Create tables in Amazon Athena from nested JSON and mappings using JSONSerDe](https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/) in the *AWS Big Data Blog*.

## Reserved words
<a name="tables-databases-columns-names-reserved-words"></a>

Certain reserved words in Athena must be escaped. To escape reserved keywords in DDL statements, enclose them in backticks (`). To escape reserved keywords in SQL `SELECT` statements and in queries on [views](views.md), enclose them in double quotes (''). 

For more information, see [Escape reserved keywords in queries](reserved-words.md).

## Additional resources
<a name="tables-databases-columns-names-additional-resources"></a>

For full database and table creation syntax, see the following pages.
+ [CREATE DATABASE](create-database.md)
+ [CREATE TABLE](create-table.md)

For more information about databases and tables in AWS Glue, see [Databases](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html) and [Tables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html) in the *AWS Glue Developer Guide*.