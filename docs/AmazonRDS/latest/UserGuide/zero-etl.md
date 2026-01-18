# Data filtering for Amazon RDS zero-ETL integrations

Amazon RDS
zero-ETL integrations support data filtering, which lets you control which data is replicated from
your source Amazon RDS database to your target data warehouse. Instead of replicating the entire
database, you can apply one or more filters to selectively include or exclude specific tables.
This helps you optimize storage and query performance by ensuring that only relevant data is
transferred. Currently, filtering is limited to the database and table levels. Column- and
row-level filtering are not supported.

Data filtering can be useful when you want to:

- Join certain tables from two or more different source databases, and you don't need
  complete data from either database.
- Save costs by performing analytics using only a subset of tables rather than an entire
  fleet of databases.
- Filter out sensitive information—such as phone numbers, addresses, or credit card
  details—from certain tables.
  You can add data filters to a zero-ETL integration using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or
  the Amazon RDS API.

If the integration has a provisioned cluster as its target, the cluster must be on [patch 180](../../../redshift/latest/mgmt/cluster-versions.md#cluster-version-180 "../../../redshift/latest/mgmt/cluster-versions.md#cluster-version-180") or higher to
use data filtering.

###### Topics

- [Format of a data filter](#zero-etl.filtering-format "#zero-etl.filtering-format")
- [Filter logic](#zero-etl.filtering-evaluate "#zero-etl.filtering-evaluate")
- [Filter precedence](#zero-etl.filtering-precedence "#zero-etl.filtering-precedence")
- [RDS for MySQL examples](#zero-etl.filtering-examples-mysql "#zero-etl.filtering-examples-mysql")
- [RDS for PostgreSQL examples](#zero-etl.filtering-examples-postgres "#zero-etl.filtering-examples-postgres")
- [RDS for Oracle examples](#zero-etl.filtering-examples-oracle "#zero-etl.filtering-examples-oracle")
- [Adding data filters to an integration](#zero-etl.add-filter "#zero-etl.add-filter")
- [Removing data filters from an integration](#zero-etl.remove-filter "#zero-etl.remove-filter")

## Format of a data filter

You can define multiple filters for a single integration. Each filter either includes or
excludes any existing and future database tables that match one of the patterns in the filter
expression. Amazon RDS zero-ETL integrations use [Maxwell filter syntax](https://maxwells-daemon.io/filtering/ "https://maxwells-daemon.io/filtering/") for data filtering.

Each filter has the following elements:

| Element           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter type       | An `Include` filter type *includes<br>• all tables<br>that match one of the patterns in the filter expression. An `Exclude`<br>filter type *excludes<br>• all tables that match one of the<br>patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Filter expression | A comma-separated list of patterns. Expressions must use [Maxwell filter syntax](https://maxwells-daemon.io/filtering/ "https://maxwells-daemon.io/filtering/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pattern           | A filter pattern in the format<br>``database`.`table``<br>for RDS for MySQL, or<br>``database`.`schema`.`table``<br>for RDS for PostgreSQL. You can specify literal names, or define regular<br>expressions.<br>NoteFor RDS for MySQL, regular expressions are supported in both the database and<br>table name. For RDS for PostgreSQL, regular expressions are supported only in the<br>schema and table name, not in the database name.<br>You can't include column-level filters or denylists.<br>A single integration can have a maximum of 99 total patterns. In the console, you<br>can enter patterns within a single filter expression, or spread them out among<br>multiple expressions. A single pattern can't exceed 256 characters in length. |

###### Important

If you select an RDS for PostgreSQL source database, you must specify at least one
data filter pattern. At minimum, the pattern must include a single database
(``database-name`._._`) for replication to
the target data warehouse.

The following image shows the structure of RDS for MySQL data filters in the
console:

![Data filters for a zero-ETL integration](images/zero-etl-filter.png)

###### Important

Do not include personally identifying, confidential, or sensitive information in your
filter patterns.

### Data filters in the AWS CLI

When using the AWS CLI to add a data filter, the syntax differs slightly from the console.
You must assign a filter type (`Include` or `Exclude`) to each pattern
individually, so you can't group multiple patterns under one filter type.

For example, in the console you can group the following comma-separated patterns under a
single `Include` statement:

**RDS for MySQL**

```
`mydb`.`mytable`, `mydb`.`/table_\d+/`
```

**RDS for PostgreSQL**

```
`mydb`.`myschema`.`mytable`, `mydb`.`myschema`.`/table_\d+/`
```

However, when using the AWS CLI, the same data filter must be in the following
format:

**RDS for MySQL**

```
'include: `mydb.mytable`, include: `mydb./table_\d+/`'
```

**RDS for PostgreSQL**

```
'include: `mydb.myschema.mytable`, include: `mydb.myschema./table_\d+/`'
```

## Filter logic

If you don't specify any data filters in your integration, Amazon RDS assumes a default filter of
`include:*.*`, which replicates all tables to the target data warehouse. However,
if you add at least one filter, the default logic switches to `exclude:*.*`, which
excludes all tables by default. This lets you explicitly define which databases and tables to
include in replication.

For example, if you define the following filter:

```
'include: db.table1, include: db.table2'
```

Amazon RDS
evaluates the filter as follows:

```
'**exclude:\*.\***, include: db.table1, include: db.table2'
```

Therefore, Amazon RDS only replicates `table1` and `table2` from the
database named `db` to the target data warehouse.

## Filter precedence

Amazon RDS
evaluates data filters in the order you specify. In the AWS Management Console, it processes filter
expressions from left to right and top to bottom. A second filter or an individual pattern
that follows the first can override it.

For example, if the first filter is `Include books.stephenking`, it includes
only the `stephenking` table from the `books` database. However, if you
add a second filter, `Exclude books.*`, it overrides the first filter. This
prevents any tables from the `books` index from being replicated to the target data warehouse.

When you specify at least one filter, the logic starts by assuming
`exclude:*.*` by default, which automatically _excludes_ all
tables from replication. As a best practice, define filters from broadest to most specific.
Start with one or more `Include` statements to specify the data to replicate, then
add `Exclude` filters to selectively remove certain tables.

The same principle applies to filters that you define using the AWS CLI. Amazon RDS evaluates
these filter patterns in the order that you specify them, so a pattern might override one that
you specify before it.

## RDS for MySQL examples

The following examples demonstrate how data filtering works for
RDS for MySQL examples zero-ETL integrations:

- Include all databases and all tables:

```
'include: *.*'
```

- Include all tables within the `books` database:

```
'include: books.*'
```

- Exclude any tables named `mystery`:

```
'include: *.*, exclude: *.mystery'
```

- Include two specific tables within the `books` database:

```
'include: books.stephen_king, include: books.carolyn_keene'
```

- Include all tables in the `books` database, except for those containing the
  substring `mystery`:

```
'include: books.*, exclude: books./.*mystery.*/'
```

- Include all tables in the `books` database, except those starting with
  `mystery`:

```
'include: books.*, exclude: books./mystery.*/'
```

- Include all tables in the `books` database, except those ending with
  `mystery`:

```
'include: books.*, exclude: books./.*mystery/'
```

- Include all tables in the `books` database that start with
  `table_`, except for the one named `table_stephen_king`. For
  example, `table_movies` or `table_books` would be replicated, but
  not `table_stephen_king`.

```
'include: books./table_.*/, exclude: books.table_stephen_king'
```

## RDS for PostgreSQL examples

The following examples demonstrate how data filtering works for RDS for PostgreSQL
zero-ETL integrations:

- Include all tables within the `books` database:

```
'include: books.*.*'
```

- Exclude any tables named `mystery` in the `books`
  database:

```
'include: books.*.*, exclude: books.*.mystery'
```

- Include one table within the `books` database in the `mystery`
  schema, and one table within `employee` database in the `finance`
  schema:

```
'include: books.mystery.stephen_king, include: employee.finance.benefits'
```

- Include all tables in the `books` database and `science_fiction`
  schema, except for those containing the substring `king`:

```
'include: books.science_fiction.*, exclude: books.*./.*king.*/
```

- Include all tables in the `books` database, except those with a schema name
  starting with `sci`:

```
'include: books.*.*, exclude: books./sci.*/.*'
```

- Include all tables in the `books` database, except those in the
  `mystery` schema ending with `king`:

```
'include: books.*.*, exclude: books.mystery./.*king/'
```

- Include all tables in the `books` database that start with
  `table_`, except for the one named `table_stephen_king`. For
  example, `table_movies` in the `fiction` schema and
  `table_books` in the `mystery` schema are replicated, but not
  `table_stephen_king` in either schema:

```
'include: books.*./table_.*/, exclude: books.*.table_stephen_king'
```

## RDS for Oracle examples

The following examples demonstrate how data filtering works for RDS for Oracle
zero-ETL integrations:

- Include all tables within the books database:

```
'include: books.*.*'
```

- Exclude any tables named mystery in the books database:

```
'include: books.*.*, exclude: books.*.mystery'
```

- Include one table within the books database in the mystery schema, and one table
  within employee database in the finance schema:

```
'include: books.mystery.stephen_king, include: employee.finance.benefits'
```

- Include all tables in the mystery schema within the books database:

```
'include: books.mystery.*'
```

### Case sensitivity considerations

Oracle Database and Amazon Redshift handle object name casing differently, which affects both data
filter configuration and target queries. Note the following:

- Oracle Database stores database, schema, and object names in uppercase unless
  explicitly quoted in the `CREATE` statement. For example, if you create
  `mytable` (no quotes), the Oracle data dictionary stores the table name as
  `MYTABLE`. If you quote the object name, the data dictionary preserves the
  case.
- Zero-ETL data filters are case sensitive and must match the exact case of object
  names as they appear in the Oracle data dictionary.
- Amazon Redshift queries default to lowercase object names unless explicitly quoted. For
  example, a query of `MYTABLE` (no quotes) searches for
  `mytable`.

Be mindful of the case differences when you create the Amazon Redshift filter and query the
data.

#### Creating an uppercase

integration

When you create a table without specifying the name in double quotes, the Oracle
database stores the name in uppercase in the data dictionary. For example, you can create
`MYTABLE` using any of the following SQL statements.

```
CREATE TABLE REINVENT.MYTABLE (id NUMBER PRIMARY KEY, description VARCHAR2(100));
CREATE TABLE reinvent.mytable (id NUMBER PRIMARY KEY, description VARCHAR2(100));
CREATE TABLE REinvent.MyTable (id NUMBER PRIMARY KEY, description VARCHAR2(100));
CREATE TABLE reINVENT.MYtabLE (id NUMBER PRIMARY KEY, description VARCHAR2(100));
```

Because you didn't quote the table name in the preceding statements, the Oracle
database stores the object name in uppercase as `MYTABLE`.

To replicate this table to Amazon Redshift, you must specify the uppercase name in your data
filter of your `create-integration` command. The Zero-ETL filter name and
Oracle data dictionary name must match.

```
aws rds create-integration \
  --integration-name upperIntegration \
  --data-filter "include: ORCL.REINVENT.MYTABLE" \
...
```

By default, Amazon Redshift stores data in lowercase. To query `MYTABLE` in the
replicated database in Amazon Redshift, you must quote the uppercase name `MYTABLE` so
that it matches the case in the Oracle data dictionary.

```
SELECT * FROM targetdb1."REINVENT"."MYTABLE";
```

The following queries don't use the quoting mechanism. They all return an error
because they search for an Amazon Redshift table named `mytable`, which uses the default
lowercase name, but the table is named `MYTABLE` in the Oracle data
dictionary.

```
SELECT * FROM targetdb1."REINVENT".MYTABLE;
SELECT * FROM targetdb1."REINVENT".MyTable;
SELECT * FROM targetdb1."REINVENT".mytable;
```

The following queries uses the quoting mechanism to specify a mixed case name. The
queries all return an error because they search for an Amazon Redshift table that isn't named
`MYTABLE`.

```
SELECT * FROM targetdb1."REINVENT"."MYtablE";
SELECT * FROM targetdb1."REINVENT"."MyTable";
SELECT * FROM targetdb1."REINVENT"."mytable";
```

#### Creating a lowercase

integration

In the following alternative example, you use double quotes to store the table name in
lowercase in the Oracle data dictionary. You create `mytable` as
follows.

```
CREATE TABLE REINVENT."mytable" (id NUMBER PRIMARY KEY, description VARCHAR2(100));
```

The Oracle database stores the table name as `mytable` in lowercase. To
replicate this table to Amazon Redshift, you must specify the lowercase name `mytable` in
your Zero-ETL data filter.

```
aws rds create-integration \
  --integration-name lowerIntegration \
  --data-filter "include: ORCL.REINVENT.mytable" \
...
```

When you query this table in the replicated database in Amazon Redshift, you can specify the
lowercase name `mytable`. The query succeeds because it searches for a table
named `mytable`, which is the table name in the Oracle data dictionary.

```
SELECT * FROM targetdb1."REINVENT".mytable;
```

Because Amazon Redshift defaults to lowercase object names, the following queries also succeed in
finding `mytable`.

```
SELECT * FROM targetdb1."REINVENT".MYtablE;
SELECT * FROM targetdb1."REINVENT".MYTABLE;
SELECT * FROM targetdb1."REINVENT".MyTable;
```

The following queries use the quoting mechanism for the object name. They all return
an error because they search for an Amazon Redshift table whose name is different from
`mytable`.

```
SELECT * FROM targetdb1."REINVENT"."MYTABLE";
SELECT * FROM targetdb1."REINVENT"."MyTable";
SELECT * FROM targetdb1."REINVENT"."MYtablE";
```

#### Create a table with a

mixed-case integration

In the following example, you use double quotes to store the table name in lowercase
in the Oracle data dictionary. You create `MyTable` as follows.

```
CREATE TABLE REINVENT."MyTable" (id NUMBER PRIMARY KEY, description VARCHAR2(100));
```

The Oracle database stores this table name as `MyTable` with mixed case. To
replicate this table to Amazon Redshift, you must specify the mixed case name in the data
filter.

```
aws rds create-integration \
  --integration-name mixedIntegration \
  --data-filter "include: ORCL.REINVENT.MyTable" \
...
```

When you query this table in the replicated database in Amazon Redshift, you must specify the
mixed case name `MyTable` by quoting the object name.

```
SELECT * FROM targetdb1."REINVENT"."MyTable";
```

Because Amazon Redshift defaults to lowercase object names, the following queries don't find the
object because they are searching for the lowercase name `mytable`.

```
SELECT * FROM targetdb1."REINVENT".MYtablE;
SELECT * FROM targetdb1."REINVENT".MYTABLE;
SELECT * FROM targetdb1."REINVENT".mytable;
```

###### Note

You can't use regular expressions in the filter value for database name, schema, or
table name in RDS for Oracle integrations.

## Adding data filters to an integration

You can configure data filtering using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

###### Important

If you add a filter after you create an integration, Amazon RDS treats it as if it always
existed. It removes any data in the target data warehouse that doesn’t match the new
filtering criteria and resynchronizes all affected tables.

###### To add data filters to a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Zero-ETL integrations**. Select the
   integration that you want to add data filters to, and then choose
   **Modify**.
3. Under **Source**, add one or more `Include` and
   `Exclude` statements.

The following image shows an example of data filters for a MySQL integration:

![Data filters for a zero-ETL integration in the RDS console](images/zero-etl-filter-data.png) 4. When you're satisfied with the changes, choose **Continue** and
**Save changes**.
To add data filters to a zero-ETL integration using the AWS CLI, call the [modify-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-integration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-integration.html") command. In addition to the integration identifier, specify
the `--data-filter` parameter with a comma-separated list of
`Include` and `Exclude` Maxwell filters.

The following example adds filter patterns to `my-integration`.

For Linux, macOS, or Unix:

```
aws rds modify-integration \
    --integration-identifier `my-integration` \
    --data-filter `'include: foodb.*, exclude: foodb.tbl, exclude: foodb./table_\d+/'`
```

For Windows:

```
aws rds modify-integration ^
    --integration-identifier `my-integration` ^
    --data-filter `'include: foodb.*, exclude: foodb.tbl, exclude: foodb./table_\d+/'`
```

To modify a zero-ETL integration using the RDS API, call the [ModifyIntegration](../APIReference/API_ModifyIntegration.md "../APIReference/API_ModifyIntegration.md")
operation. Specify the integration identifier and provide a comma-separated list of filter
patterns.

## Removing data filters from an integration

When you remove a data filter from an integration, Amazon RDS reevaluates the remaining filters
as if the removed filter never existed. It then replicates any previously excluded data that
now meets the criteria into the target data warehouse. This triggers a resynchronization
of all affected tables.
