# Step 2: Choose data sources and classifiers

Next, configure the data sources and classifiers for the crawler.

For more information about supported data sources, see [Supported data sources for crawling](crawler-data-stores.md "crawler-data-stores.md").

**Data source configuration**

Select the appropriate option for **Is your data already mapped to AWS Glue tables?**
choose 'Not yet' or 'Yes'. By default, 'Not yet' is selected.

The crawler can access data stores directly as the source of the crawl, or it can
use existing tables in the Data Catalog as the source. If the crawler uses existing catalog tables,
it crawls the data stores that are specified by those catalog tables.

- Not yet: Select one or more data sources to be crawled. A crawler can crawl multiple data stores of different types (Amazon S3, JDBC, and so on).

You can configure only one data store at a time. After you have provided the
connection information and include paths and exclude patterns, you then have the option
of adding another data store.

- Yes: Select existing tables from your AWS Glue Data Catalog.

The catalog tables specify the data stores to crawl. The crawler can crawl only
catalog tables in a single run; it can't mix in other source types.

A common reason to specify a catalog table as the source is when you create the table
manually (because you already know the structure of the data store) and you want a crawler
to keep the table updated, including adding new partitions. For a discussion of other
reasons, see [Updating manually created Data Catalog tables using
crawlers](tables-described.md#update-manual-tables "tables-described.md#update-manual-tables").

When you specify existing tables as the crawler source type, the following conditions
apply:

    + Database name is optional.
    + Only catalog tables that specify Amazon S3, Amazon DynamoDB, or Delta Lake data stores are permitted.
    + No new catalog tables are created when the crawler runs. Existing tables are updated
     as needed, including adding new partitions.
    + Deleted objects found in the data stores are ignored; no catalog tables are deleted.
     Instead, the crawler writes a log message.
     (`SchemaChangePolicy.DeleteBehavior=LOG`)
    + The crawler configuration option to create a single schema for each Amazon S3 path is
     enabled by default and cannot be disabled.
     (`TableGroupingPolicy`=`CombineCompatibleSchemas`) For more
     information, see [Creating a single schema for each Amazon S3 include
     path](crawler-grouping-policy.md "crawler-grouping-policy.md").
    + You can't mix catalog tables as a source with any other source types (for example
     Amazon S3 or Amazon DynamoDB).

To use Delta tables, first create a Delta table using Athena DDL or the AWS Glue API.

Using Athena, set the location to your Amazon S3 folder and the table type to 'DELTA'.

```
CREATE EXTERNAL TABLE database_name.table_name
LOCATION 's3://bucket/folder/'
TBLPROPERTIES ('table_type' = 'DELTA')
```

Using the AWS Glue API, specify the table type within the table parameters map. The table parameters need to include the
following key/value pair. For more information on how to create a table, see
[Boto3 documentation for create_table](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_table.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_table.html") .

```
{
    "table_type":"delta"
}
```

**Data sources**

Select or add the list of data sources to be scanned by the crawler.

(Optional) If you choose JDBC as the data source, you can use your own JDBC drivers when specifying the Connection access where the driver info is stored.

**Include path**

When evaluating what to include or exclude in a crawl, a crawler starts by evaluating
the required include path. For Amazon S3, MongoDB, MongoDB Atlas, Amazon DocumentDB (with MongoDB compatibility), and
relational data stores, you must specify an include path.

For an Amazon S3 data store

Choose whether to specify a path in this account or in a different account, and then
browse to choose an Amazon S3 path.

For Amazon S3 data stores, include path syntax is
`bucket-name/folder-name/file-name.ext`. To crawl all objects in a bucket, you
specify just the bucket name in the include path. The exclude pattern is relative to the
include path

For a Delta Lake data store

Specify one or more Amazon S3 paths to Delta tables as s3://`bucket`/`prefix`/`object`.

For an Iceberg or Hudi data store

Specify one or more Amazon S3 paths that contain folders with Iceberg or Hudi table metadata as s3://`bucket`/`prefix`.

For Iceberg and Hudi data stores, the Iceberg/Hudi folder may be located in a child folder of the root folder. The crawler will scan all folders underneath a path for a Hudi folder.

For a JDBC data store

Enter
`<database>`/`<schema>`/`<table>`
or `<database>`/`<table>`,
depending on the database product. Oracle Database and MySQL don’t support schema
in the path. You can substitute the percent (%) character for
`<schema>` or `<table>`.
For example, for an Oracle database with a system identifier (SID) of
`orcl`, enter `orcl/%` to import all tables to which the
user named in the connection has access.

###### Important

This field is case-sensitive.

###### Note

If you choose to bring in your own JDBC driver versions, AWS Glue crawlers will consume resources in AWS Glue jobs and
Amazon S3 buckets to ensure your provided driver are run in your environment. The additional usage of resources will be reflected in your account.
Drivers are limited to the properties described in
[Adding an AWS Glue connection](console-connections.md "console-connections.md").

For a MongoDB, MongoDB Atlas, or Amazon DocumentDB data store

For MongoDB, MongoDB Atlas, and Amazon DocumentDB (with MongoDB compatibility), the syntax is
`database/collection`.

For JDBC data stores, the syntax is either
`database-name/schema-name/table-name` or
`database-name/table-name`. The syntax depends on whether the database engine
supports schemas within a database. For example, for database engines such as MySQL or
Oracle, don't specify a `schema-name` in your include path. You can substitute
the percent sign (`%`) for a schema or table in the include path to represent all
schemas or all tables in a database. You cannot substitute the percent sign (`%`)
for database in the include path.

**Maximum transversal depth (for Iceberg or Hudi data stores only)**

Defines the maximum depth of the Amazon S3 path that the crawler can traverse to discover the Iceberg or Hudi metadata folder in your Amazon S3 path. The purpose of this parameter is to limit the crawler run time. The default value is 10 and the maximum is 20.

**Exclude patterns**

These enable you to exclude certain files or tables from the crawl. The exclude path is relative to the include path. For
example, to exclude a table in your JDBC data store, type the table name in the exclude
path.

A crawler connects to a JDBC data store using an AWS Glue connection that contains a JDBC
URI connection string. The crawler only has access to objects in the database engine using
the JDBC user name and password in the AWS Glue connection. _The crawler can only
create tables that it can access through the JDBC connection._ After the crawler
accesses the database engine with the JDBC URI, the include path is used to determine which
tables in the database engine are created in the Data Catalog. For example, with MySQL, if you
specify an include path of `MyDatabase/%`, then all tables within
`MyDatabase` are created in the Data Catalog. When accessing Amazon Redshift, if you specify an
include path of `MyDatabase/%`, then all tables within all schemas for database
`MyDatabase` are created in the Data Catalog. If you specify an include path of
`MyDatabase/MySchema/%`, then all tables in database `MyDatabase`
and schema `MySchema` are created.

After you specify an include path, you can then exclude objects from the crawl that your
include path would otherwise include by specifying one or more Unix-style `glob`
exclude patterns. These patterns are applied to your include path to determine which objects
are excluded. These patterns are also stored as a property of tables created by the crawler.
AWS Glue PySpark extensions, such as `create_dynamic_frame.from_catalog`, read the
table properties and exclude objects defined by the exclude pattern.

AWS Glue supports the following `glob` patterns in the exclude pattern.

| Exclude pattern | Description                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `*.csv`         | Matches an Amazon S3 path that represents an object name in the current folder<br>ending in `.csv`                       |
| `*.*`           | Matches all object names that contain a dot                                                                              |
| `*.{csv,avro}`  | Matches object names ending with `.csv` or<br>`.avro`                                                                    |
| `foo.?`         | Matches object names starting with `foo.` that are followed by a<br>single character extension                           |
| `myfolder/*`    | Matches objects in one level of subfolder from `myfolder`, such as<br>`/myfolder/mysource`                               |
| `myfolder/*/*`  | Matches objects in two levels of subfolders from `myfolder`, such as<br>`/myfolder/mysource/data`                        |
| `myfolder/**`   | Matches objects in all subfolders of `myfolder`, such as<br>`/myfolder/mysource/mydata` and<br>`/myfolder/mysource/data` |
| `myfolder**`    | Matches subfolder `myfolder` as well as files below<br>`myfolder`, such as `/myfolder` and<br>`/myfolder/mydata.txt`     |
| `Market*`       | Matches tables in a JDBC database with names that begin with<br>`Market`, such as `Market_us` and<br>`Market_fr`         |

AWS Glue interprets `glob` exclude patterns as follows:

- The slash (`/`) character is the delimiter to separate Amazon S3 keys into a
  folder hierarchy.
- The asterisk (`*`) character matches zero or more characters of a name
  component without crossing folder boundaries.
- A double asterisk (`**`) matches zero or more characters crossing folder
  or schema boundaries.
- The question mark (`?`) character matches exactly one character of a name
  component.
- The backslash (`\`) character is used to escape characters that otherwise
  can be interpreted as special characters. The expression `\\` matches a
  single backslash, and `\{` matches a left brace.
- Brackets `[ ]` create a bracket expression that matches a single
  character of a name component out of a set of characters. For example,
  `[abc]` matches `a`, `b`, or `c`. The
  hyphen (`-`) can be used to specify a range, so `[a-z]` specifies
  a range that matches from `a` through `z` (inclusive). These forms
  can be mixed, so [`abce-g`] matches `a`, `b`,
  `c`, `e`, `f`, or `g`. If the character
  after the bracket (`[`) is an exclamation point (`!`), the bracket
  expression is negated. For example, `[!a-c]` matches any character except
  `a`, `b`, or `c`.

Within a bracket expression, the `*`, `?`, and `\`
characters match themselves. The hyphen (`-`) character matches itself if it
is the first character within the brackets, or if it's the first character after the
`!` when you are negating.

- Braces (`{ }`) enclose a group of subpatterns, where the group matches if
  any subpattern in the group matches. A comma (`,`) character is used to
  separate the subpatterns. Groups cannot be nested.
- Leading period or dot characters in file names are treated as normal characters in
  match operations. For example, the `*` exclude pattern matches the file name
  `.hidden`.

###### Example Amazon S3 exclude patterns

Each exclude pattern is evaluated against the include path. For example, suppose that
you have the following Amazon S3 directory structure:

```
/mybucket/myfolder/
   departments/
      finance.json
      market-us.json
      market-emea.json
      market-ap.json
   employees/
      hr.json
      john.csv
      jane.csv
      juan.txt
```

Given the include path `s3://mybucket/myfolder/`, the following are some
sample results for exclude patterns:

| Exclude pattern       | Results                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| `departments/**`      | Excludes all files and folders below `departments` and includes the<br>`employees` folder and its files |
| `departments/market*` | Excludes `market-us.json`, `market-emea.json`, and<br>`market-ap.json`                                  |
| `**.csv`              | Excludes all objects below `myfolder` that have a name ending with<br>`.csv`                            |
| `employees/*.csv`     | Excludes all `.csv` files in the `employees`<br>folder                                                  |

###### Example Excluding a subset of Amazon S3 partitions

Suppose that your data is partitioned by day, so that each day in a year is in a
separate Amazon S3 partition. For January 2015, there are 31 partitions. Now, to crawl data for
only the first week of January, you must exclude all partitions except days 1 through
7:

```

 2015/01/{[!0],0[8-9]}**, 2015/0[2-9]/**, 2015/1[0-2]/**

```

Take a look at the parts of this glob pattern. The first part, `2015/01/{[!0],0[8-9]}**`, excludes all days that don't begin with a "0" in
addition to day 08 and day 09 from month 01 in year 2015. Notice that "\*\*" is used as the
suffix to the day number pattern and crosses folder boundaries to lower-level folders. If
"\*" is used, lower folder levels are not excluded.

The second part, `2015/0[2-9]/**`, excludes days in months 02 to 09, in
year 2015.

The third part, `2015/1[0-2]/**`, excludes days in months 10, 11, and 12,
in year 2015.

###### Example JDBC exclude patterns

Suppose that you are crawling a JDBC database with the following schema
structure:

```
MyDatabase/MySchema/
   HR_us
   HR_fr
   Employees_Table
   Finance
   Market_US_Table
   Market_EMEA_Table
   Market_AP_Table
```

Given the include path `MyDatabase/MySchema/%`, the following are some
sample results for exclude patterns:

| Exclude pattern | Results                                                  |
| --------------- | -------------------------------------------------------- |
| `HR*`           | Excludes the tables with names that begin with `HR`      |
| `Market_*`      | Excludes the tables with names that begin with `Market_` |
| `**_Table`      | Excludes all tables with names that end with `_Table`    |

**Additional crawler source parameters**

Each source type requires a different set of additional parameters.

**Connection**

Select or add an AWS Glue connection. For information about connections, see
[Connecting to data](glue-connections.md "glue-connections.md").

**Additional metadata - optional (for JDBC data stores)**

Select additional metadata properties for the crawler to crawl.

- Comments: Crawl associated table level and column level comments.
- Raw types: Persist the raw datatypes of the table columns in additional metadata. As a default behavior, the crawler translates the raw datatypes to Hive-compatible types.

**JDBC Driver Class name - optional (for JDBC data stores)**

Type a custom JDBC driver class name for the crawler to connect to the data source:

- Postgres: org.postgresql.Driver
- MySQL: com.mysql.jdbc.Driver, com.mysql.cj.jdbc.Driver
- Redshift: com.amazon.redshift.jdbc.Driver, com.amazon.redshift.jdbc42.Driver
- Oracle: oracle.jdbc.driver.OracleDriver
- SQL Server: com.microsoft.sqlserver.jdbc.SQLServerDriver

**JDBC Driver S3 Path - optional (for JDBC data stores)**

Choose an existing Amazon S3 path to a `.jar` file. This is where the `.jar` file will be stored
when using a custom JDBC driver for the crawler to connect to the data source.

**Enable data sampling (for Amazon DynamoDB, MongoDB, MongoDB Atlas, and Amazon DocumentDB data stores
only)**

Select whether to crawl a data sample only. If not selected the entire table is crawled. Scanning all the records can take a long time when the table is not a high throughput table.

**Create tables for querying (for Delta Lake data stores only)**

Select how you want to create the Delta Lake tables:

- Create Native tables: Allow integration with query engines that support querying of the Delta transaction log directly.
- Create Symlink tables: Create a symlink manifest folder with manifest files partitioned by the partition keys, based on the specified configuration parameters.

**Scanning rate - optional (for DynamoDB data stores only)**

Specify the percentage of the DynamoDB table Read Capacity Units to use by the crawler. Read capacity units is a term defined by DynamoDB, and is a numeric
value that acts as rate limiter for the number of reads that can be performed on
that table per second. Enter a value between 0.1 and 1.5. If not specified,
defaults to 0.5 for provisioned tables and 1/4 of maximum configured capacity for
on-demand tables. Note that only provisioned capacity mode should be used with AWS Glue crawlers.

###### Note

For DynamoDB data stores, set the provisioned capacity mode for processing reads and writes on your tables. The AWS Glue crawler should not be used with the on-demand capacity mode.

**Network connection - optional (for Amazon S3, Delta, Iceberg, Hudi and Catalog target data stores)**

Optionally include a Network connection to use with this Amazon S3 target. Note that each crawler is limited to one Network connection so any other Amazon S3 targets will also use the same connection (or none, if left blank).

For information about connections, see
[Connecting to data](glue-connections.md "glue-connections.md").

**Sample only a subset of files and Sample size (for Amazon S3 data stores only)**

Specify the number of files in each leaf folder to be crawled when crawling sample files in a dataset. When this feature is turned on, instead of crawling all the files in this dataset, the crawler randomly selects some files in each leaf folder to crawl.

The sampling crawler is best suited for customers who have previous knowledge about their data formats and know that schemas in their folders do not change. Turning on this feature will significantly reduce crawler runtime.

A valid value is an integer between 1 and 249. If not specified, all the files are crawled.

**Subsequent crawler runs**

This field is a global field that affects all Amazon S3 data sources.

- Crawl all sub-folders: Crawl all folders again with every subsequent crawl.
- Crawl new sub-folders only: Only Amazon S3 folders that were added since the last crawl will be crawled. If the schemas are compatible, new partitions will be added to existing tables. For more information, see [Scheduling incremental crawls for adding new partitions](incremental-crawls.md "incremental-crawls.md").
- Crawl based on events: Rely on Amazon S3 events to control what folders to crawl. For more information, see [Accelerating crawls using Amazon S3 event notifications](crawler-s3-event-notifications.md "crawler-s3-event-notifications.md").

**Custom classifiers - optional**

Define custom classifiers before defining crawlers. A classifier checks whether a given file is in a format the crawler can handle. If it is, the classifier creates a schema in the form of a `StructType` object that matches that data format.

For more information, see [Defining and managing classifiers](add-classifier.md "add-classifier.md").
