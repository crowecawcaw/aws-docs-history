

# Collations for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.collations"></a>

This topic provides reference content comparing collation and character set support between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can gain insight into how these database systems handle string management, storage, and comparison rules.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Collations](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.collations)  | UNICODE uses `CHARACTER SET` property instead of `NCHAR` or `NVARCHAR` data types. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.collations.sqlserver"></a>

SQL Server collations define the rules for string management and storage in terms of sorting, case sensitivity, accent sensitivity, and code page mapping. SQL Server supports both ASCII and UCS-2 UNICODE data.

UCS-2 UNICODE data uses a dedicated set of UNICODE data types denoted by the prefix `N`: `Nchar` and `Nvarchar`. Their ASCII counterparts are CHAR and VARCHAR.

Choosing a collation and a character set has significant implications on data storage, logical predicate evaluations, query results, and query performance.

**Note**  
To view all collations supported by SQL Server, use the `fn_helpcollations` function as shown following: `SELECT * FROM sys.fn_helpcollations()`.

Collations define the actual bitwise binary representation of all string characters and the associated sorting rules. SQL Server supports multiple collations down to the column level. A table may have multiple string columns that use different collations. Collations for non-UNICODE character sets determine the code page number representing the string characters.

**Note**  
UNICODE and non-UNICODE data types in SQL Server aren’t compatible. A predicate or data modification that introduces a type conflict is resolved using predefined collation precedence rules. For more information, see [Collation Precedence](https://docs.microsoft.com/en-us/sql/t-sql/statements/collation-precedence-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

Collations define sorting and matching sensitivity for the following string characteristics:
+ Case
+ Accent
+ Kana
+ Width
+ Variation selector

SQL Server uses a suffix naming convention that appends the option name to the collation name. For example, the collation `Azeri_Cyrillic_100_CS_AS_KS_WS_SC`, is an Azeri-Cyrillic-100 collation that is case-sensitive, accent-sensitive, kana type-sensitive, width-sensitive, and has supplementary characters.

SQL Server supports three types of collation sets: \* Windows Collations use the rules defined for collations by the operating system locale where UNICODE and non-UNICODE data use the same comparison algorithms. \* Binary Collations use the binary bit-wise code for comparison. Therefore, the locale doesn’t affect sorting. \* SQL Server Collations provide backward compatibility with previous SQL Server versions. They aren’t compatible with the windows collation rules for non-UNICODE data.

You can define collations at various levels:
+  **Server-level collations** determine the collations used for all system databases and is the default for future user databases. While the system databases collation can’t be changed, an alternative collation can be specified as part of the `CREATE DATABASE` statement
+  **Database-level collations** inherit the server default unless the `CREATE DATABASE` statement explicitly sets a different collation. This collation is used as a default for all `CREATE TABLE` and `ALTER TABLE` statements.
+  **Column-level collations** can be specified as part of the `CREATE TABLE` or `ALTER TABLE` statements to override the database’s default collation setting.
+  **Expression-level collations** can be set for individual string expressions using the `COLLATE` function. For example, `SELECT * FROM MyTable ORDER BY StringColumn COLLATE Latin1_General_CS_AS`.

**Note**  
SQL Server supports UCS-2 UNICODE only.

SQL Server 2019 adds support for UTF-8 for import and export encoding, and as database-level or column-level collation for string data. Support includes PolyBase external tables, and Always Encrypted (when not used with Enclaves). For more information, see [Collation and Unicode Support](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver15) in the *SQL Server documentation*.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.collations.sqlserver.syntax"></a>

```
CREATE DATABASE <Database Name>
[ ON <File Specifications> ]
COLLATE <Collation>
[ WITH <Database Option List> ];
```

```
CREATE TABLE <Table Name>
(
    <Column Name> <String Data Type>
    COLLATE <Collation> [ <Column Constraints> ]...
);
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.collations.sqlserver.examples"></a>

The following example creates a database with a default Bengali\_100\_CS\_AI collation.

```
CREATE DATABASE MyBengaliDatabase
ON
( NAME = MyBengaliDatabase_Datafile,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\MyBengaliDatabase.mdf',
    SIZE = 100)
LOG ON
    ( NAME = MyBengaliDatabase_Logfile,
FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\MyBengaliDblog.ldf',
    SIZE = 25)
COLLATE Bengali_100_CS_AI;
```

The following example creates a table with two different collations.

```
CREATE TABLE MyTable
(
    Col1 CHAR(10) COLLATE Hungarian_100_CI_AI_SC NOT NULL PRIMARY KEY,
    COL2 VARCHAR(100) COLLATE Sami_Sweden_Finland_100_CS_AS_KS NOT NULL
);
```

For more information, see [Collation and Unicode support](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.collations.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports multiple character sets and a variety of collations that can be used for comparison. Similar to SQL Server, you can define collations at the server, database, and column level. Additionally, you can define collations at the table level in Aurora MySQL.

The paradigm of collations in Aurora MySQL is different than in SQL Server and consists of separate character set and collation objects. Aurora MySQL supports 41 different character sets and 222 collations. Seven different UNICODE character sets are supported including UCS-2, UTF-8 and UTF-32.

**Note**  
Use UCS-2 which is compatible with SQL Server UNICODE types.

Each character set can have one or more associated collations with a single default collation.

Collation names have prefixes consisting of the name of their associated character set followed by suffixes that indicate additional characteristics.

To see all character sets supported by Aurora MySQL, use the `INFORMATION_SCHEMA.CHARACTER_SETS` table or the `SHOW CHARACTER SET` statement.

To see all collations for a character set, use the `INFORMATION_SCHEMA.COLLATIONS` table or the `SHOW COLLATION` statement.

**Note**  
Character set and collation settings also affect client-to -server communications. You can set explicit collations for sessions using the `SET` command. For example, `SET NAMES 'utf8';` causes Aurora MySQL to treat incoming object names as UTF-8 encoded.

You can set the default character set and collations at the server level using custom cluster parameter groups. For more information, see [Server Options](chap-sql-server-aurora-mysql.configuration.serveroptions.md).

At the database level, you can set a default character set and collation with the `CREATE DATABASE` and `ALTER DATABASE` statements. Consider the following example:

```
CREATE DATABASE MyDatabase
CHARACTER SET latin1 COLLATE latin1_swedish_ci;
```

To view the default character set and collation for an Aurora MySQL databases, use the following statement:

```
SELECT DEFAULT_CHARACTER_SET_NAME,
    DEFAULT_COLLATION_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = '<Database Name>';
```

**Note**  
In Aurora MySQL, a *database* is equivalent to an SQL Server *schema*. For more information, see [Databases and Schemas](chap-sql-server-aurora-mysql.tsql.databasesschemas.md).

Every string column in Aurora MySQL has a character set and an associated collation. If not explicitly specified, it will inherit the table default. To specify a non-default character set and collation, use the `CHARACTER SET` and `COLLATE` clauses of the `CREATE TABLE` statement.

```
CREATE TABLE MyTable
(
    StringColumn VARCHAR(5) NOT NULL
    CHARACTER SET latin1
    COLLATE latin1_german1_ci
);
```

At the expression level, similar to SQL Server, you can use the `COLLATE` function to explicitly declare a string’s collation. In addition, a prefix to the string can be used to denote a specific character set. Consider the following example:

```
SELECT _latin1'Latin non-UNICODE String',
_utf8'UNICODE String' COLLATE utf8_danish_ci;
```

**Note**  
The Aurora MySQL term for this prefix or string header is introducer. It doesn’t change the value of the string; only the character set.

At the session level, the server’s setting determines the default character set and collation used to evaluate nonqualified strings.

Although the server’s character set and collation default settings can be modified using the cluster parameter groups, it is recommended that client applications don’t assume a specific setting and explicitly set the required character set and collation using the `SET NAMES` and `SET CHARACTER SET` statements.

For more information, see [Connection Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-connection.html) in the *MySQL documentation*.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.collations.mysql.syntax"></a>

The following example creates a database-level collation.

```
CREATE DATABASE <Database Name>
[DEFAULT] CHARACTER SET <Character Set>
[[DEFAULT] COLLATE <Collation>];
```

The following example creates a table-level collation.

```
CREATE TABLE <Table Name>
(Column Specifications)
[DEFAULT] CHARACTER SET <Character Set>
[COLLATE <Collation>];
```

The following example creates a column collation.

```
CREATE TABLE <Table Name>
(
<Column Name> {CHAR | VARCHAR | TEXT} (<Length>)
CHARACTER SET CHARACTER SET <Character Set>
[COLLATE <Collation>];
```

The following example creates an expression collation.

```
_<Character Set>'<String>' COLLATE <Collation>
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.collations.mysql.examples"></a>

The following walkthrough describes how to change the cluster character set and collation.

1. Log in to your [Management Console](https://eu-central-1.console.aws.amazon.com/rds/home?#databases:), choose ** Amazon RDS **, and then choose **Parameter groups**.

1. Choose **Create parameter group**.

1. For **Parameter group family**, choose **aurora-mysql5.7**.

1. For **Type**, choose **DB Cluster Parameter Group**.

1. For **Group name**, enter the identified for the DB parameter group.

1. Choose **Create**.

1. Choose the newly created group on the **Parameter groups** list.

1. For **Parameters**, enter **character\_set\_server** in the search box and choose **Edit parameters**.

1. Choose the server default character set.

1. Delete the search term and enter collation. Select the desired default server collation and choose **Preview changes**.

1. Check the values and choose **Close**, and then choose **Save changes**.

1. Return to the Management Console dashboard and choose **Create database**.

1. For **Choose a database creation method**, choose **Easy create**.

1. For **Engine type**, choose ** Amazon Aurora **.

1. Enter the instance size, cluster identifier and username. Choose **Create database**.

1. Modify the created instance to change the **DB Parameter group**.

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.collations.summary"></a>

The following table identifies similarities, differences, and key migration considerations.


| Feature | SQL Server |  Aurora MySQL  | 
| --- | --- | --- | 
| Unicode support | UTF 16 using `NCHAR` and `NVARCHAR` data types | 8 UNICODE character sets, using the `CHARACTER SET` option | 
| Collations levels | Server, Database, Column, Expression | Server, Database, Table, Column, Expression | 
| View collation metadata |  `fn_helpcollation` system view |  `INFORMATION_SCHEMA.SCHEMATA`, `SHOW COLLATION`, `SHOW CHARACTER SET`  | 

For more information, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/5.7/en/charset.html) in the *MySQL documentation*.