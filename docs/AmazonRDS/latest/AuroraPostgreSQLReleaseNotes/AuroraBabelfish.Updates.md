

# Babelfish for Aurora PostgreSQL updates
<a name="AuroraBabelfish.Updates"></a>

Following, you can find information about versions of the Babelfish that have been released for Aurora PostgreSQL. Babelfish is an option available with Aurora PostgreSQL version 13.4 and higher releases. Updates to Babelfish become available with certain new releases of the Aurora PostgreSQL database engine.

For information about Aurora PostgreSQL extensions with Babelfish, see [Using Aurora PostgreSQL extensions with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html).

For information about Babelfish version updates, see [Babelfish version updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information.html).

For a list of supported and unsupported functionality across different Babelfish releases, see [Babelfish for Aurora PostgreSQL reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_AuroraPostgreSQL_Babelfish_Reference.html).

**Topics**
+ [Babelfish for Aurora PostgreSQL 6.x versions](#aurorababelfish-versions-version6x)
+ [Babelfish for Aurora PostgreSQL 5.x versions](#aurorababelfish-versions-version5x)
+ [Babelfish for Aurora PostgreSQL 4.x versions](#aurorababelfish-versions-version4x)
+ [Babelfish for Aurora PostgreSQL 3.x versions (includes some deprecated versions)](#aurorababelfish-versions-version3x)
+ [Babelfish for Aurora PostgreSQL 2.x versions (includes some deprecated versions)](#aurorababelfish-versions-version2x)
+ [Babelfish for Aurora PostgreSQL 1.x versions (includes some deprecated versions)](#aurorababelfish-versions-version1x)

## Babelfish for Aurora PostgreSQL 6.x versions
<a name="aurorababelfish-versions-version6x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 6.1](#AuroraBabelfish.Updates.61X)
+ [Babelfish for Aurora PostgreSQL 6.0](#AuroraBabelfish.Updates.60X)

### Babelfish for Aurora PostgreSQL 6.1
<a name="AuroraBabelfish.Updates.61X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 18.4. For more information about the improvements in Aurora PostgreSQL 18.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 6.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 6.1.0, August 21, 2026
<a name="AuroraBabelfish.Updates.610"></a>

**New Features**
+ Added support for STGeometryType(), STNumPoints(), Parse(), MakeValid() and STMPointFromText() Geospatial functions.
+ Added support for Multipoint instances in Babelfish.
+ Babelfish now extends support for Shared Plan Cache to T-SQL queries.
+ Added support for ELEMENTS directive in FOR XML RAW and FOR XML PATH.

**Critical enhancements**
+ Fixed an issue that could cause crash in SPI\_finish after Out Of Memory error.
+ Fixed crash in FOR XML PATH queries when processing all-NULL rows without a root element.
+ Improved query performance when expanding the views and procedures in SSMS Object Explorer.

**High Priority stability enhancements**
+ Fixed sys.fn\_varbintohexsubstring function definition after major version upgrade.
+ Fixed an issue that could cause a database reboot when dropping a temporary table from within a nested stored procedure.
+ Fixed an issue where queries with local variables could return inconsistent results when using generic query plans.
+ Fixed an issue that could cause a database reboot when dropping a temporary table from within a nested stored procedure.
+ Fixed an issue where creating a function or procedure in a schema created from the PostgreSQL endpoint could cause a database reboot.

**Additional improvements and enhancements**
+ Improved memory handling in FOR XML query processing.
+ Fixed an issue where sp\_execute returned an error when invoked with named parameters.
+ Fixed FOR XML RAW to properly handle empty element names by omitting the row wrapper element instead of generating invalid empty tags.
+ Fixed DATETIME2FROMPARTS function to properly handle fractional second values in the range 32786 to 9999999.
+ Improved memory handling in PrepareRowDescription and rewrite\_if\_condition functions.
+ Fixed an issue where go-sqlcmd client driver failed to return query results.
+ Fixed Memory management issue in IsTopTransactionName function.
+ Fixed allocation of savepoint\_name in correct memory context in pltsql\_eval\_txn\_data.

### Babelfish for Aurora PostgreSQL 6.0
<a name="AuroraBabelfish.Updates.60X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 18.3. For more information about the improvements in Aurora PostgreSQL 18.3, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 6.0 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 6.0.0, June 10, 2026
<a name="AuroraBabelfish.Updates.600"></a>

**New Features**
+ Added support for Eager aggregation, which pushes aggregation before joins to improve query performance. Controlled by GUCs `babelfishpg_tsql.enable_eager_aggregate` (default: ON) and `min_eager_agg_group_size` to set the minimum average group size required to consider applying Eager aggregation (default: 8).
+ Added support for Polygon instances for geography/geometry datatype.
+ Added support for implicit cast from (n)varchar/(n)char to datetimeoffset datatype.
+ Added support for sys.fn\_varbintohexstr system object.

**Critical enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.
+ Fixed an issue where update with output clause may skip rows during concurrent updates.
+ DROP LOGIN now correctly returns an error when attempting to drop a login that is the owner of a database.

**High Priority stability enhancements**
+ Fixed incorrect return datatype in UNION queries involving datetimeoffset, (n)varchar and datetime types.
+ Fixed issue in coalesce involving datetimeoffset and (n)varchar types.
+ Fixed UNION and CASE expressions with varbinary and string literals to correctly resolve to varchar instead of varbinary.
+ Restricted ownership change of Babelfish objects from PG port.
+ Fixed an issue in procedure calls leading to incorrect lifecycle handling of temp tables.
+ Restricted users from altering Babelfish objects in sys schema.
+ Fixed the scale/precision handling for MIN/MAX functions on CHAR/NCHAR datatypes.
+ Fixed high CPU utilization during concurrent connection establishment for pyODBC connections.
+ Fixed inconsistent index scans for binary/varbinary comparison operators and added cross-type support.
+ Fixed an issue in nested procedure calls that caused temp table cleanup failures and parser errors.
+ Blocked ALTER AUTHORIZATION on database when the new owner is a database role, fixed server role, or sysadmin.

**Additional improvements and enhancements**
+ Fixed an issue where casting string values to sqlvariant may cause client to hang.
+ Fixed cast and convert functions between datatypes (n)char & (var)binary.
+ Added fix to handle UDT datatypes in DATEADD() function.
+ Fixed handling for white space characters in the ISNUMERIC() function to match T-SQL behavior.
+ Fixed an issue in SELECT queries with reserved keywords used as column aliases.
+ Fixed output format when casting datetime and smalldatetime to (n)varchar/(n)char.
+ Fixed handling of scale/precision for empty string casting to binary.
+ Fixed concatenation of binaries to produce expected results.
+ Fixed trailing blanks being incorrectly treated as insignificant in LIKE operator in case of exact pattern matching.
+ Fixed an issue where primary key information was not being sent in TDS response for ADO.NET FillSchema() operations.
+ Fixed scale/precision handling for concatenated results of binaries.
+ Fixed a rare issue where parallel query runs into unexpected error when table OID reaches to certain limit.
+ Fixed an issue where MONEY type conversion incorrectly rejected few valid ASCII and special characters.
+ Fixed convert function to properly apply style parameter when converting SMALLMONEY to string types, ensuring correct formatting for styles 0, 1, 2, and 126 matching with T-SQL behavior.
+ Fixed multiple convert function issues for MONEY/SMALLMONEY type to string conversions, including proper handling of negative style parameters and invalid style value.

## Babelfish for Aurora PostgreSQL 5.x versions
<a name="aurorababelfish-versions-version5x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 5.6](#AuroraBabelfish.Updates.56X)
+ [Babelfish for Aurora PostgreSQL 5.5](#AuroraBabelfish.Updates.55X)
+ [Babelfish for Aurora PostgreSQL 5.4](#AuroraBabelfish.Updates.54X)
+ [Babelfish for Aurora PostgreSQL 5.3](#AuroraBabelfish.Updates.53X)
+ [Babelfish for Aurora PostgreSQL 5.2](#AuroraBabelfish.Updates.52X)
+ [Babelfish for Aurora PostgreSQL 5.1](#AuroraBabelfish.Updates.51X)

### Babelfish for Aurora PostgreSQL 5.6
<a name="AuroraBabelfish.Updates.56X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.10. For more information about the improvements in Aurora PostgreSQL 17.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.6.0, August 21, 2026
<a name="AuroraBabelfish.Updates.560"></a>

**New Features**
+ Added support for STGeometryType(), STNumPoints(), Parse(), MakeValid() and STMPointFromText() Geospatial functions.
+ Added support for Multipoint instances in Babelfish.
+ Babelfish now extends support for Shared Plan Cache to T-SQL queries.
+ Added support for ELEMENTS directive in FOR XML RAW and FOR XML PATH.

**Critical enhancements**
+ Fixed an issue that could cause crash in SPI\_finish after Out Of Memory error.
+ Fixed crash in FOR XML PATH queries when processing all-NULL rows without a root element.
+ Improved query performance when expanding the views and procedures in SSMS Object Explorer.

**High Priority stability enhancements**
+ Fixed sys.fn\_varbintohexsubstring function definition after major version upgrade.
+ Fixed an issue that could cause a database reboot when dropping a temporary table from within a nested stored procedure.
+ Fixed an issue where queries with local variables could return inconsistent results when using generic query plans.
+ Fixed an issue that could cause a database reboot when dropping a temporary table from within a nested stored procedure.
+ Fixed an issue where creating a function or procedure in a schema created from the PostgreSQL endpoint could cause a database reboot.

**Additional improvements and enhancements**
+ Improved memory handling in FOR XML query processing.
+ Fixed an issue where sp\_execute returned an error when invoked with named parameters.
+ Fixed FOR XML RAW to properly handle empty element names by omitting the row wrapper element instead of generating invalid empty tags.
+ Fixed DATETIME2FROMPARTS function to properly handle fractional second values in the range 32786 to 9999999.
+ Improved memory handling in PrepareRowDescription and rewrite\_if\_condition functions.
+ Fixed an issue where go-sqlcmd client driver failed to return query results.
+ Fixed Memory management issue in IsTopTransactionName function.
+ Fixed allocation of savepoint\_name in correct memory context in pltsql\_eval\_txn\_data.

### Babelfish for Aurora PostgreSQL 5.5
<a name="AuroraBabelfish.Updates.55X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.9. For more information about the improvements in Aurora PostgreSQL 17.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.5.0, April 6, 2026
<a name="AuroraBabelfish.Updates.550"></a>

**New Features**
+ Added support for Polygon instances for geography/geometry datatype.
+ Added support for implicit cast from (n)varchar/(n)char to datetimeoffset datatype.
+ Added support for sys.fn\_varbintohexstr system object.

**Critical enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.
+ Fixed an issue where update with output clause may skip rows during concurrent updates.
+ DROP LOGIN now correctly returns an error when attempting to drop a login that is the owner of a database.

**High Priority stability enhancements**
+ Fixed incorrect return datatype in UNION queries involving datetimeoffset, (n)varchar and datetime types.
+ Fixed issue in coalesce involving datetimeoffset and (n)varchar types.
+ Fixed UNION and CASE expressions with varbinary and string literals to correctly resolve to varchar instead of varbinary.
+ Restricted ownership change of Babelfish objects from PG port.
+ Fixed an issue in procedure calls leading to incorrect lifecycle handling of temp tables.
+ Restricted users from altering Babelfish objects in sys schema.
+ Fixed the scale/precision handling for MIN/MAX functions on CHAR/NCHAR datatypes.
+ Fixed high CPU utilization during concurrent connection establishment for pyODBC connections.
+ Fixed inconsistent index scans for binary/varbinary comparison operators and added cross-type support.
+ Blocked ALTER AUTHORIZATION on database when the new owner is a database role, fixed server role, or sysadmin.

**Additional improvements and enhancements**
+ Fixed an issue where casting string values to sqlvariant may cause client to hang.
+ Fixed cast and convert functions between datatypes (n)char & (var)binary.
+ Added fix to handle UDT datatypes in DATEADD() function.
+ Fixed handling for white space characters in the ISNUMERIC() function to match T-SQL behavior.
+ Fixed an issue in SELECT queries with reserved keywords used as column aliases.
+ Fixed output format when casting datetime and smalldatetime to (n)varchar/(n)char.
+ Fixed handling of scale/precision for empty string casting to binary.
+ Fixed concatenation of binaries to produce expected results.
+ Fixed an issue where primary key information was not being sent in TDS response for ADO.NET FillSchema() operations.
+ Fixed scale/precision handling for concatenated results of binaries.
+ Fixed a rare issue where parallel query runs into unexpected error when table OID reaches to certain limit.
+ Fixed an issue where MONEY type conversion incorrectly rejected few valid ASCII and special characters.
+ Fixed convert function to properly apply style parameter when converting SMALLMONEY to string types, ensuring correct formatting for styles 0, 1, 2, and 126 matching with T-SQL behavior.
+ Fixed trailing blanks being incorrectly treated as insignificant in LIKE operator in case of exact pattern matching.
+ Fixed multiple convert function issues for MONEY/SMALLMONEY type to string conversions, including proper handling of negative style parameters and invalid style value.

### Babelfish for Aurora PostgreSQL 5.4
<a name="AuroraBabelfish.Updates.54X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.7. For more information about the improvements in Aurora PostgreSQL 17.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.4.2, March 20, 2026
<a name="AuroraBabelfish.Updates.542"></a>

**Critical stability enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.

#### Aurora Babelfish release 5.4.1, January 16, 2026
<a name="AuroraBabelfish.Updates.541"></a>

**Critical stability enhancements**
+ Fixed an issue where an `UPDATE` statement with `OUTPUT` clause may skip rows when there are concurrent updates on the same row.

**High Priority stability enhancements**
+ Fixed an issue in nested procedure calls that caused temp table cleanup failures and parser errors.

#### Aurora Babelfish release 5.4.0, December, 18, 2025
<a name="AuroraBabelfish.Updates.540"></a>

**New Features**
+ Enabled support of SELECT TOP N PERCENT clause with few [limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.tsql.limited-implementation.html).
+ Enabled support for Linestring instances for [geography/geometry datatypes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html).
+ Enabled support for system procedures sp\_xml\_preparedocument, sp\_xml\_removedocument and [OPENXML](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-xml-datatype-methods.html).
+ Enabled support for XML method .VALUE() for XML Data Types.
+ Enabled support for ownership chaining for object references inside views and stored procedures/functions. Permission checking on underlying objects is determined by either the user's direct permissions or through ownership chaining.
+ Enabled support of sys.time\_zone\_info view
+ Enabled support for Values clause and subquery columns in SELECT list in FOR JSON AUTO functionality

**Critical enhancements**
+ Fixed STPointFromText() and Point() to throw error on NULL arguments.
+ Fixed issues with Geometry/Geography to (var)char and (var)binary conversions.
+ Fixed function definition of STPointFromText(), STPointFromText(), STAsText() and STAsBinary().
+ Fixed bytea to Geometry/Geography conversion for Point instance.
+ ASCII function returns incorrect results with argument type as Binary and Varbinary.
+ Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

**High Priority stability enhancements**
+ Fixed an issue where user can not be dropped when permissions have been granted to that user.
+ Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
+ Fixed precision/scale for Round() function.
+ Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.
+ Fixed an issue where errors in pg\_cron job was leading to server reboot.

**Additional improvements and enhancements**
+ Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.
+ Fixed an issue which resets the escape hatch settings to default with the first temp table creation.
+ Fixed Datetime and Varbinary to Binary CAST functions.
+ Fixed an issue to match CONVERT and CAST function return values for Binary type.
+ Fixed INSERT INTO table DEFAULT VALUES for domain types, by setting appropriate function return type.
+ Fixed an issue where running multi-Statement table valued function throws syntax error if the database name contains a symbol for an operator.
+ Fixed REVOKE permission execution to correctly handle overlapping schema-level and object-level grants.
+ Enabled support for the NULL/NOT NULL syntax in ALTER TABLE ALTER COLUMN statements.
+ Add identifier delimiters to handle special characters in login and role names.
+ Fixed indexes that were created on top of T-SQL temporary tables to correctly follow transaction semantics.
+ Fixed various mathematical functions for Money and smallmoney datatype.
+ Fixed an issue to persist column level permissions when modifying views using ALTER VIEW.
+ Enabled support to allow alter on functions with dependent weak schemabinding views.
+ Fixed issue with Geometry/Geography static methods when using delimited identifiers for data types.
+ Fixed return type of SQRT() function to float.
+ Fixed issues with assignment of multibyte characters to local variable of type nchar/nvarchar.
+ Added empty string handling in ISNUMERIC(), to ensure compatibility with T-SQL behavior.
+ Fixed DATALENGTH() to return correct byte length value for various datatypes and their UDTs.
+ Fixed DATETIME to VARBINARY CAST function.
+ Fixed precision/scale in SELECT INTO while using with GROUP BY clause.
+ Fixed an issue of protocol error in TDS stream due to Numeric/Decimal overflow.
+ Fixed issues with CTE logic and missing intermediate levels in the output of FOR JSON AUTO clause.
+ Fixed an issue related to LIKE operator where ESCAPE character does not work as expected when ESCAPE character comes after wildcard in pattern.
+ Fixed an issue which occurs when parameter of type binary(8) passed from .NET driver.

### Babelfish for Aurora PostgreSQL 5.3
<a name="AuroraBabelfish.Updates.53X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.6. For more information about the improvements in Aurora PostgreSQL 17.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.3.2, May 07, 2026
<a name="AuroraBabelfish.Updates.532"></a>

**Critical stability enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.

#### Aurora Babelfish release 5.3.1, November 25, 2025
<a name="AuroraBabelfish.Updates.531"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 5.3.0, November 25, 2025
<a name="AuroraBabelfish.Updates.530"></a>

**New Features**
+ Added support for boolean operators and prefix term grammer in T-SQL CONTAINS clause for [ Full-Text Search ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-fulltextsearch.html).
+ Added support for Z-M flags for Point Instances and Z, M, HasZ and HasM functions for [ GEOMETRY and GEOGRAPHY datatypes ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html).
+ Added support for sp\_helplogins stored procedure.
+ Enabled Support for weak binding views with few limitations.

**Critical enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.
+ Fixed an issue in GroupAD where login with mapped user should not have access to guest privileges.
+ Improved the performance of queries using the ISNUMERIC() function in predicates.
+ Added support for queries to choose index scan for queries having predicates comparing numeric and integer data types.

**High Priority stability enhancements**
+ Fixed overflow checks in all arithmetic operations with money, smallmoney being a higher precedence operand.
+ Fixed the output datatype for all arithmetic operations involving smallmoney and bit.
+ Fixed behavior of certain math functions like CEIL, ROUND, POWER and FLOOR for money and smallmoney data types.
+ Fixed issue with connection crash during arithmetic operations on smallmoney and int.
+ Fixed overflow checks in all arithmetic/numeric operations with smallmoney/money being a operand.
+ Fixed an issue with DATENAME() to gives correct value of TZOFFSET part.
+ Handling for CHAR()/NCHAR() function to return NULL instead of errors when values are out of range.
+ Handling for NCHAR() function to accept inputs that can be converted to integers.
+ Fixed PATINDEX() function to correctly finds patterns at the end of text and handles wildcard searches accurately.
+ Enabled index usage for Accent Sensitive / Insensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match with following conditions:
  + For Accent Sensitive collation, user needs to create index from TSQL endpoint : CREATE INDEX <index\_name> ON <table\_name>(<column\_name>)
  + For Accent Insensitive collation, user needs to create index from PSQL endpoint: CREATE INDEX <index\_name> ON <schema\_name>.<table\_name>(sys.remove\_accents\_internal\_using\_cache(<column\_name>))
+ Fixed an issue where TRY\_CAST and TRY\_CONVERT was incorrectly rounding decimal values when casting to integer types, instead of truncating the fractional part.
+ Fixed precision and scale for arithmetic operations between money/smallmoney and numeric and for money/smallmoney in union operators.
+ Fixed precision and scale handling for case expressions and nested case expressions when with numeric and smallmoney/money branches.
+ Fixed precision and scale handling for numeric expressions with sub-expressions as money/smallmoney or fixed length datatypes.
+ Fixed an issue with handling of bigint and money/smallmoney multiplication operations.
+ Fixed an issue where money/smallmoney multiplications was incorrectly truncating decimal values in result, insetad of rounding the fractional part.
+ Fixed precision and scale handling for SUM()/AVG() functions with money/smallmoney and fixed length datatypes.
+ Fixed an issue with airthetic operations between numeric variable and fixed length variables.
+ Fixed precision and scale handling for aggregate functions with numeric.
+ Fixed an issue with babelfish connections restored during ZDP.
+ Fixed an issue with RESET ALL command from postgres endpoint.
+ Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
+ Fixed an issue where parallelism won't be used for pltsql RETURN expression.
+ Fixed permission denied issue in cross-db table valued functions.
+ Added handling for empty input string handling in date and time datatypes.
+ Fixed precision and scale handling for money/smallmoney while creating objects, casts, variables and user defined datatypes using it.
+ Fixed an issue to preserve Timezone information during casting from string to datetimeoffset.
+ Fixed Function QUOTENAME() to return correct strings.
+ Added handling of binary arguments for Len() function.
+ Fixed the precision and scale for aggregate function that have \*(all columns) as input.
+ Fixed an issue for CaseExpr with numeric computation.
+ Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'.
+ Fixed rounding off issue during storing datetime datatype. Existing users should run the following query from TSQL endpoint to update their existing data: UPDATE <table\_name> SET <datetime\_col> = CAST(CAST(<datetime\_col> as VARCHAR) AS DATETIME).
+ Fixed datetime comparison in Babelfish to match TSQL behavior of treating datetime values within 0.00333 second precision as equal.

**Additional improvements and enhancements**
+ Fixed an issue with OBJECT\_DEFINITION function where it was trucating the output after 4000 characters.
+ Fixed the database\_principals view to display the correct SID.
+ Handle PostgreSQL reserved keywords in Cursor operations.
+ Added support for sys.server\_permissions, sys.sql\_logins views and sys.fn\_varbintohexsubstring system function.
+ Fixed an issue while adding a column with default value which resulted in an error.
+ Fixed an issue with INSERT ... EXECUTE statements in stored procedures related to nested levels.

### Babelfish for Aurora PostgreSQL 5.2
<a name="AuroraBabelfish.Updates.52X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.5. For more information about the improvements in Aurora PostgreSQL 17.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.2.2, January 15, 2026
<a name="AuroraBabelfish.Updates.522"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 5.2.1, August 08, 2025
<a name="AuroraBabelfish.Updates.521"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.
+ Fixed an issue with babelfish connections restored during ZDP.

#### Aurora Babelfish release 5.2.0, June 30, 2025
<a name="AuroraBabelfish.Updates.520"></a>

**New Features**
+ Added CREATE OR ALTER VIEW / ALTER VIEW syntax support in Babelfish with few limitations.
+ Added support of Transact-SQL UNPIVOT operators for Babelfish.
+ Added support for `STDimension`, `STDisjoint`, `STIntersects`, `STIsClosed`, `STIsEmpty`, `STIsValid` Geospatial functions.
+ Added support for collation in partition functions and partitioning columns.
+ Enabled support for scripting logins in SSMS for Babelfish.
+  Added support for column\_list in T-SQL CONTAINS clause for Full-Text Search. 

**Critical enhancements**
+ Added “\+” and “-” operator for varbinary.
+ Added new GUCs `babelfishpg_tsql.apg_enable_correlated_scalar_transform` and `babelfishpg_tsql.apg_enable_subquery_cache` to control subquery optimization features in Babelfish. The new GUCs are `ON` by default.
+ Added support for larger server hello messages during SSL handshake by segmenting them into 4096 byte packets.
+ Added support for CAST from VARBINARY to DATETIME in Babelfish.
+ Added support for altering user/role in Babelfish GroupAD for fixed database roles’ member.
+ Allow CREATE schema in Babelfish GroupAD via fixed db roles’ membership.
+ Fixed an issue with object ownership. Any new object created by a user from TDS endpoint will now be owned by schema owner as opposed to previous behaviour where the current user always owned the new object.
+ Added handling for default schema name for procedure in Group-AD session, when Table Valued Parameter is used as an argument of a procedure.

**High Priority stability enhancements**
+ Fixed logic to adjust precision and scale in Numeric Multiplication and Division.
+ Fixed computation of precision and scale for User defined types.
+ Fixed computation of precision and scale for constant with value 0.
+ Fixed the issue `wrong varnullingrels` error could be reported incorrectly after subquery transformation.
+ Fixed the issue that alter table will cause follow up cascade drop command failed to drop the database contain this table.
+ Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
+ Restrict dropping of Babelfish login via PG port, if a BBF login has mapped users in all three master, tempdb and msdb databases.
+ Fixed permission denied error in Babelfish Group AD while using table variables in some scenarios.
+ Fixed bug which prevented enable/disable all triggers on tables.
+ Fixed incorrect conversion from integers to varbinary datatype.
+ Fixed Casting and Conversion from Float to Varchar datatype.
+ Fixed suser\_sname() function to handle the null inputs.
+ Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
+ Fixed issue which causes incorrect result in arithmetic operations which results in numeric/decimal type.
+ Fixed an issue which caused communication link failure with DROP LOGIN/USER/ROLE [public].
+ Restricted dropping of system procedures and views from dbo schema.
+ Fixed an issue in round() function to ensure return types match input argument types.
+ Transfer nullability and identity properties of columns in SELECT INTO statement to new table. These properties are only transferred if there is a single table in FROM clause of SELECT INTO and the column isn't part of expression in select into statements target list.

**Additional improvements and enhancements**
+ Fixed JSON string formatting to prevent improper backslash escaping in “FOR JSON” output with json\_query function.
+ Fixed an issue where guest user could create objects in guest schema.
+ Fixed PUBLIC role attributes in system views.
+ Fixed sys.objects catalog to correctly populate unique constraints metadata.
+ Fixed issue when max length of a RPC character based parameter is 0.
+ Restricted members of fixed database role db\_ddladmin from creating schema for database principals that it isn't a member of.
+ Restricted members of fixed database role db\_ddladmin from creating schema for database principals that it isn't a member of.
+ Added an escape hatch for the INLINE option in CREATE FUNCTION statements, defaulting to “strict” mode for proper error handling.
+ Fixed the entry in `babelfish_schema_permissions` which was getting overridden if there were table and procedure with the same name.
+ Fixed an errors while fetching the object definition of tsql objects due to handling of few nodes in `sys.tsql_get_expr`.
+ Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
+ Fixed some cases of object resolution inside stored procedures, functions and trigger.
+ Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
+ Improved index name handling in Babelfish by preserving the original index name in the catalog, making it visible in catalog views like sys.indexes. It also adds support for renaming existing indexes using sp\_rename to preserve and display their original names.
+ Fixed a crash in `resolve_numeric_typmod_from_exp` for aggregate functions using \*(all columns).

### Babelfish for Aurora PostgreSQL 5.1
<a name="AuroraBabelfish.Updates.51X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.4. For more information about the improvements in Aurora PostgreSQL 17.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 5.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 5.1.3, February 02, 2026
<a name="AuroraBabelfish.Updates.513"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 5.1.2, October 09, 2025
<a name="AuroraBabelfish.Updates.512"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.
+ Fixed crash in `resolve_numeric_typmod_from_exp` for aggragate functions using \*(all columns)

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 5.1.1, June 03, 2025
<a name="AuroraBabelfish.Updates.511"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

**Critical stability enhancements**
+ Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 5.1.0, May 01, 2025
<a name="AuroraBabelfish.Updates.510"></a>

**New Features**
+ Added support for fixed database-level roles `db_securityadmin`, `db_accessadmin`, `db_ddladmin`, `db_datareader` and `db_datawriter`. T-SQL users can be added to these fixed database roles.
+ Added support for fixed server-level roles `securityadmin` and `dbcreator`. T-SQL logins can be added to these fixed server roles.
+ Added support for adding T-SQL users to `db_owner` fixed database-level role. This T-SQL will have privileges similar to the database owner.

For more information about relevant permission management and access control settings for these new features in Babelfish, see [Managing permissions and access control in Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-permissions.html).

**Critical enhancements**
+ Fixed issues with `Convert` function when converting from `string` to `date`, `datetimeoffset`, `datetime2`, `datetime`, `smalldatetime` and `time`.
+ Fixed the issue of parameter declarations containing \# characters not being handled correctly.
+ Supported `SET IDENTITY_INSERT` for three part relation references.
+ Fixed an issue with the `HASHBYTES` function to ensure correct behavior when processing `NVARCHAR` argument.
+ Fixed the issue of `CREATE PARTITION SCHEME` not supporting “PRIMARY” syntax.
+ Fixed the issue of UPDATE/DELETE of table variable query in a function getting incorrectly rejected with multi-table FROM clause.
+ Restricted user defined @@function from being mapped to sys function.
+ Fixed the issue of comparison with empty double quoted string raised the error about “zero-length delimited identifier”.
+ Fixed a crash which could occur in rare situations when using temporary tables with certain orphaned catalog entries.
+ Fixed an issue where trigger gets dropped when dropping a column in a table.
+ Improved performance of queries having join between `TABLE_CONSTRAINTS` and `KEY_COLUMN_USAGE` view in the INFORMATION\_SCHEMA schema.
+ Fixed inconsistent formatting issue with `Convert` function when converting MONEY datatype with value 0 to string datatypes.
+ Fixed formatting issues in `CAST` from `MONEY` to `CHAR/VARCHAR`.
+ Fixed the issue where `SELECT...INTO` with `MIN` and `MAX` aggregations on `MONEY` columns lost type information.
+ Implement modulo operator for `MONEY` type.
+ Added cleanup of stale parameters and configs in case of connection pooling.
+ Added comprehensive cursor state cleanup to avoid stale data in case of connection pooling.
+ Fixed a issue with `IDENTITY` columns not being recognized during `DML` statements using `OUTPUT` and `WHERE` clause.

**High Priority stability enhancements**
+ Fixed an issue where @@function in `UPDATE SET` clause causes syntax error.
+ Fixed dynamic evaluation of @local\_var for `UPDATE ... SET` @local\_var and `SELECT` command.
+ Fixed an issue with `sp_columns_100` where partial data could be returned if @fUsePattern = 0 is used.
+ Fixed an issue where local variables may not be updated correct when query involves manipulation of local variable.
+ Improved the general performance of parsing.
+ Fixed an issue with system function `OPENJSON`.
+ Fixed the incorrect result datatype of `UNION` involving `MONEY` type.
+ Fixed offset when using “AT TIME ZONE” with DATETIME2 datatype conversion with convert() function in non-default local timezone setting.
+ Fixed an issue where batches containing cross database queries looks up the objects in incorrect database.
+ Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions for week and quarter `Datepart`.
+ Fixed an issue where `sys.column_property` may return incorrect results for ordinal property of a column.
+ Fixed “`AT TIME ZONE`” issue near DST change time with `DATETIME2` datatype conversion.
+ Fixed behavior of queries which use `sys.Db_id()`function which returned empty rows in enforced parallel mode.

**Additional improvements and enhancements**
+ Optimize execution the `plan` extension by removing unnecessary `CAST` functions.
+ `EXECUTE`() on a double-quoted string no longer raises an error.
+ Fixed an error when using functions as column default values on temp tables.
+ Fixed an error in `OPENJSON` function call to allow parse on long `JSON` string.
+ Fixed issue where dropping member from role does not work after restoring Babelfish database.
+ Fixed the alias issue when if exists co-exists with a “=” alias in select list.
+ Restricted declaring the reserved @@function names as common variables.
+ Corrected the implementation of procedure `sp_helpuser` for database roles where `sp_helpuser` should show roles only when explicitly specified.
+ Fixed an issue where smalldatetime type and date type can more flexibly access data through index.
+ Fixed an issue with system procedure `fn_listextendedproperty`.
+ Fixed the use of table-valued parameters as arguments in procedures. Previously, you had to specify the type name of the table-valued parameter when calling the procedure, now it is optional.
+ Fixed precision and scale when common type of `CASE` expression is `NUMERIC` / `DECIMAL` .
+ Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for already terminated connections.
+ Fixed an issue where a login with mapped database user still has guest user privileges.
+ Fixed an issue where transaction count changes after execution of some system functions.
+ Fixed issue where `Datepart` functions were having different output based on the GUC `timezone`.

## Babelfish for Aurora PostgreSQL 4.x versions
<a name="aurorababelfish-versions-version4x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 4.10](#AuroraBabelfish.Updates.410X)
+ [Babelfish for Aurora PostgreSQL 4.9](#AuroraBabelfish.Updates.49X)
+ [Babelfish for Aurora PostgreSQL 4.8](#AuroraBabelfish.Updates.48X)
+ [Babelfish for Aurora PostgreSQL 4.7](#AuroraBabelfish.Updates.47X)
+ [Babelfish for Aurora PostgreSQL 4.6](#AuroraBabelfish.Updates.46X)
+ [Babelfish for Aurora PostgreSQL 4.5](#AuroraBabelfish.Updates.45X)
+ [Babelfish for Aurora PostgreSQL 4.4](#AuroraBabelfish.Updates.44X)
+ [Babelfish for Aurora PostgreSQL 4.3](#AuroraBabelfish.Updates.43X)
+ [Babelfish for Aurora PostgreSQL 4.2](#AuroraBabelfish.Updates.42X)
+ [Babelfish for Aurora PostgreSQL 4.1](#AuroraBabelfish.Updates.41X)
+ [Babelfish for Aurora PostgreSQL 4.0](#AuroraBabelfish.Updates.40X)

### Babelfish for Aurora PostgreSQL 4.10
<a name="AuroraBabelfish.Updates.410X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.14. For more information about the improvements in Aurora PostgreSQL 16.14, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.10 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 4.10.0, August 21, 2026
<a name="AuroraBabelfish.Updates.4100"></a>

**New Features**
+ Babelfish now extends support for Shared Plan Cache to T-SQL queries.

**Critical enhancements**
+ Fixed an issue that could cause crash in SPI\_finish after Out Of Memory error.
+ Fixed crash in FOR XML PATH queries when processing all-NULL rows without a root element.
+ Improved query performance when expanding the views and procedures in SSMS Object Explorer.

**High Priority stability enhancements**
+ Fixed an issue where queries with local variables could return inconsistent results when using generic query plans.
+ Fixed an issue where creating a function or procedure in a schema created from the PostgreSQL endpoint could cause a database reboot.

**Additional improvements and enhancements**
+ Improved memory handling in FOR XML query processing.
+ Fixed an issue where sp\_execute returned an error when invoked with named parameters.
+ Fixed DATETIME2FROMPARTS function to properly handle fractional second values in the range 32786 to 9999999.
+ Improved memory handling in PrepareRowDescription and rewrite\_if\_condition functions.
+ Fixed Memory management issue in IsTopTransactionName function.
+ Fixed allocation of savepoint\_name in correct memory context in pltsql\_eval\_txn\_data.

### Babelfish for Aurora PostgreSQL 4.9
<a name="AuroraBabelfish.Updates.49X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.13. For more information about the improvements in Aurora PostgreSQL 16.13, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.9 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 4.9.0, April 6, 2026
<a name="AuroraBabelfish.Updates.490"></a>

**New Features**
+ Added support for implicit cast from (n)varchar/(n)char to datetimeoffset datatype.
+ Added support for sys.fn\_varbintohexstr system object.

**Critical enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.
+ Fixed an issue where update with output clause may skip rows during concurrent updates.
+ DROP LOGIN now correctly returns an error when attempting to drop a login that is the owner of a database.

**High Priority stability enhancements**
+ Fixed incorrect return datatype in UNION queries involving datetimeoffset, (n)varchar and datetime types.
+ Fixed issue in coalesce involving datetimeoffset and (n)varchar types.
+ Fixed UNION and CASE expressions with varbinary and string literals to correctly resolve to varchar instead of varbinary.
+ Restricted ownership change of Babelfish objects from PG port.
+ Fixed an issue in procedure calls leading to incorrect lifecycle handling of temp tables.
+ Restricted users from altering Babelfish objects in sys schema.
+ Fixed the scale/precision handling for MIN/MAX functions on CHAR/NCHAR datatypes.
+ Blocked ALTER AUTHORIZATION on database when the new owner is a database role, fixed server role, or sysadmin.
+ Fixed high CPU utilization during concurrent connection establishment for pyODBC connections.

**Additional improvements and enhancements**
+ Fixed an issue where casting string values to sqlvariant may cause client to hang.
+ Fixed cast and convert functions between datatypes (n)char & (var)binary.
+ Added fix to handle UDT datatypes in DATEADD() function.
+ Fixed handling for white space characters in the ISNUMERIC() function to match T-SQL behavior.
+ Fixed an issue in SELECT queries with reserved keywords used as column aliases.
+ Fixed output format when casting datetime and smalldatetime to (n)varchar/(n)char.
+ Fixed handling of scale/precision for empty string casting to binary.
+ Fixed concatenation of binaries to produce expected results.
+ Fixed scale/precision handling for concatenated results of binaries.
+ Fixed a rare issue where parallel query runs into unexpected error when table OID reaches to certain limit.
+ Fixed an issue where MONEY type conversion incorrectly rejected few valid ASCII and special characters.
+ Fixed convert function to properly apply style parameter when converting SMALLMONEY to string types, ensuring correct formatting for styles 0, 1, 2, and 126 matching with T-SQL behavior.
+ Fixed trailing blanks being incorrectly treated as insignificant in LIKE operator in case of exact pattern matching.
+ Fixed multiple convert function issues for MONEY/SMALLMONEY type to string conversions, including proper handling of negative style parameters and invalid style value.

### Babelfish for Aurora PostgreSQL 4.8
<a name="AuroraBabelfish.Updates.48X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.11. For more information about the improvements in Aurora PostgreSQL 16.11, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.8 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 4.8.2, March 20, 2026
<a name="AuroraBabelfish.Updates.482"></a>

**Critical stability enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.

**High Priority stability enhancements**
+ Fixed an issue in nested procedure calls that caused temp table cleanup failures and parser errors.

#### Aurora Babelfish release 4.8.1, January 16, 2026
<a name="AuroraBabelfish.Updates.481"></a>

**Critical stability enhancements**
+ Fixed an issue where an `UPDATE` statement with `OUTPUT` clause may skip rows when there are concurrent updates on the same row.

#### Aurora Babelfish release 4.8.0, December 18, 2025
<a name="AuroraBabelfish.Updates.480"></a>

**New Features**
+ Enabled support of SELECT TOP N PERCENT clause with few [limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.tsql.limited-implementation.html).
+ Enabled support of sys.time\_zone\_info view.
+ Enabled support for Values clause and subquery columns in SELECT list in FOR JSON AUTO functionality.

**Critical enhancements**
+ Fixed STPointFromText() and Point() to throw error on NULL arguments.
+ Fixed issues with Geometry/Geography to (var)char and (var)binary conversions.
+ Fixed function definition of STPointFromText(), STPointFromText(), STAsText() and STAsBinary().
+ Fixed bytea to Geometry/Geography conversion for Point instance.
+ Fixed handling of STPointFromText, STGeomFromText, STLineFromText for incorrect binary input.
+ ASCII function returns incorrect results with argument type as Binary and Varbinary.
+ Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

**High Priority stability enhancements**
+ Fixed an issue where user can not be dropped when permissions have been granted to that user.
+ Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
+ Fixed precision/scale for Round() function.
+ Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.
+ Fixed an issue where errors in pg\_cron job was leading to server reboot.

**Additional improvements and enhancements**
+ Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.
+ Fixed an issue which resets the escape hatch settings to default with the first temp table creation.
+ Fixed Datetime and Varbinary to Binary CAST functions.
+ Fixed an issue to match CONVERT and CAST function return values for Binary type.
+ Fixed INSERT INTO table DEFAULT VALUES for domain types, by setting appropriate function return type.
+ Fixed an issue where running multi-Statement table valued function throws syntax error if the database name contains a symbol for an operator.
+ Fixed REVOKE permission execution to correctly handle overlapping schema-level and object-level grants.
+ Enabled support for the NULL/NOT NULL syntax in ALTER TABLE ALTER COLUMN statements.
+ Add identifier delimiters to handle special characters in login and role names.
+ Fixed indexes that were created on top of T-SQL temporary tables to correctly follow transaction semantics.
+ Fixed various mathematical functions for Money and smallmoney datatype.
+ Fixed an issue to persist column level permissions when modifying views using ALTER VIEW.
+ Enabled support to allow alter on functions with dependent weak schemabinding views.
+ Fixed issue with Geometry/Geography static methods when using delimited identifiers for data types.
+ Fixed return type of SQRT() function to float.
+ Fixed issues with assignment of multibyte characters to local variable of type nchar/nvarchar.
+ Added empty string handling in ISNUMERIC(), to ensure compatibility with T-SQL behavior.
+ Fixed DATALENGTH() to return correct byte length value for various datatypes and their UDTs.
+ Fixed DATETIME to VARBINARY CAST function.
+ Fixed precision/scale in SELECT INTO while using with GROUP BY clause.
+ Fixed an issue of protocol error in TDS stream due to Numeric/Decimal overflow.
+ Fixed issues with CTE logic and missing intermediate levels in the output of FOR JSON AUTO clause.
+ Fixed an issue related to LIKE operator where ESCAPE character does not work as expected when ESCAPE character comes after wildcard in pattern.
+ Fixed an issue which occurs when parameter of type binary(8) passed from .NET driver.

### Babelfish for Aurora PostgreSQL 4.7
<a name="AuroraBabelfish.Updates.47X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.10. For more information about the improvements in Aurora PostgreSQL 16.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.7 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.7.2, May 07, 2026](#AuroraBabelfish.Updates.472)
+ [Aurora Babelfish release 4.7.1, November 25, 2025](#AuroraBabelfish.Updates.471)
+ [Aurora Babelfish release 4.7.0, November 25, 2025](#AuroraBabelfish.Updates.470)

#### Aurora Babelfish release 4.7.2, May 07, 2026
<a name="AuroraBabelfish.Updates.472"></a>

**Critical stability enhancements**
+ Fixed an issue where executing queries from PostgreSQL endpoint in Active Directory Authentication enabled instances may lead to a reboot.

#### Aurora Babelfish release 4.7.1, November 25, 2025
<a name="AuroraBabelfish.Updates.471"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 4.7.0, November 25, 2025
<a name="AuroraBabelfish.Updates.470"></a>

**New Features**
+ Added support for Z-M flags for Point Instances and Z, M, HasZ and HasM functions for [ GEOMETRY and GEOGRAPHY datatypes. ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html) 
+ Added support for sp\_helplogins stored procedure.
+ Enabled Support for weak binding views with few limitations.

**Critical enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.
+ Fixed an issue in GroupAD where login with mapped user should not have access to guest privileges.
+ Improved the performance of queries using the ISNUMERIC() function in predicates.
+ Added support for queries to choose index scan for queries having predicates comparing numeric and integer data types.

**High Priority stability enhancements**
+ Fixed overflow checks in all arithmetic operations with money, smallmoney being a higher precedence operand.
+ Fixed the output datatype for all arithmetic operations involving smallmoney and bit.
+ Fixed behavior of certain math functions like CEIL, ROUND, POWER and FLOOR for money and smallmoney data types.
+ Fixed issue with connection crash during arithmetic operations on smallmoney and int.
+ Fixed overflow checks in all arithmetic/numeric operations with smallmoney/money being a operand.
+ Fixed an issue with DATENAME() to gives correct value of TZOFFSET part.
+ Handling for CHAR()/NCHAR() function to return NULL instead of errors when values are out of range.
+ Handling for NCHAR() function to accept inputs that can be converted to integers.
+ Fixed PATINDEX() function to correctly finds patterns at the end of text and handles wildcard searches accurately.
+ To use Index for Accent Sensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match, user needs to create index from TSQL endpoint : CREATE INDEX <index\_name> ON <table\_name>(<column\_name>). To use Index for Accent Insensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match, user needs to create index from PSQL endpoint: CREATE INDEX <index\_name> ON <schema\_name>.<table\_name>(sys.remove\_accents\_internal\_using\_cache(<column\_name>)).
+ Fixed an issue where TRY\_CAST and TRY\_CONVERT was incorrectly rounding decimal values when casting to integer types, instead of truncating the fractional part.
+ Fixed precision and scale for arithmetic operations between money/smallmoney and numeric and for money/smallmoney in union operators.
+ Fixed precision and scale handling for case expressions and nested case expressions when with numeric and smallmoney/money branches.
+ Fixed precision and scale handling for numeric expressions with sub-expressions as money/smallmoney or fixed length datatypes.
+ Fixed an issue with handling of bigint and money/smallmoney multiplication operations.
+ Fixed an issue where money/smallmoney multiplications was incorrectly truncating decimal values in result, insetad of rounding the fractional part.
+ Fixed precision and scale handling for nested case expressions with numeric and money/smallmoney as their branches.
+ Fixed precision and scale handling for SUM()/AVG() functions with money/smallmoney and fixed length datatypes.
+ Fixed an issue with airthetic operations between numeric variable and fixed length variables.
+ Fixed precision and scale handling for aggregate functions with numeric.
+ Fixed an issue with babelfish connections restored during ZDP.
+ Fixed an issue with RESET ALL command from postgres endpoint.
+ Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
+ Fixed an issue where parallelism won't be used for pltsql RETURN expression.
+ Fixed permission denied issue in cross-db table valued functions.
+ Added Handling for empty input string handling in date and time datatypes.
+ Fixed precision and scale handling for money/smallmoney while creating objects,casts,variables and user defined datatypes using it.
+ Fixed an issue to preserve Timezone information during casting from string to datetimeoffset.
+ Fixed Function QUOTENAME() to return correct strings.
+ Added handling of binary arguments for Len() function.
+ Fixed the precision and scale for aggregate function that have \*(all columns) as input.
+ Fixed an issue for CaseExpr with numeric computation.
+ Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'.
+ Fixed rounding off issue during storing datetime datatype. Existing users should run the following query from TSQL endpoint to update their existing data: UPDATE <table\_name> SET <datetime\_col> = CAST(CAST(<datetime\_col> as VARCHAR) AS DATETIME).
+ Fixed datetime comparison in Babelfish to match TSQL behavior of treating datetime values within 0.00333 second precision as equal.

**Additional improvements and enhancements**
+ Fixed an issue with OBJECT\_DEFINITION function where it was trucating the output after 4000 characters.
+ Fixed the database\_principals view to display the correct SID.
+ Handle PostgreSQL reserved keywords in Cursor operations.
+ Add full support for sys.server\_permissions, sys.sql\_logins views and sys.fn\_varbintohexsubstring system function.
+ Fixed an issue while adding a column with default value which resulted in an error.
+ Fixed an issue with INSERT ... EXECUTE statements in stored procedures related to nested levels.

### Babelfish for Aurora PostgreSQL 4.6
<a name="AuroraBabelfish.Updates.46X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.9. For more information about the improvements in Aurora PostgreSQL 16.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.6.2, January 15, 2026](#AuroraBabelfish.Updates.462)
+ [Aurora Babelfish release 4.6.1, August 08, 2025](#AuroraBabelfish.Updates.461)
+ [Aurora Babelfish release 4.6.0, June 30, 2025](#AuroraBabelfish.Updates.46X)

#### Aurora Babelfish release 4.6.2, January 15, 2026
<a name="AuroraBabelfish.Updates.462"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 4.6.1, August 08, 2025
<a name="AuroraBabelfish.Updates.461"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.
+ Fixed an issue with babelfish connections restored during ZDP.

#### Aurora Babelfish release 4.6.0, June 30, 2025
<a name="AuroraBabelfish.Updates.46X"></a>

**New Features**
+ Added CREATE OR ALTER VIEW / ALTER VIEW syntax support in Babelfish with few limitations.
+ Added support of Transact-SQL UNPIVOT operators for Babelfish.
+ Added support for `STDimension`, `STDisjoint`, `STIntersects`, `STIsClosed`, `STIsEmpty`, `STIsValid` Geospatial functions.
+ Added support for collation in partition functions and partitioning columns.
+ Enabled support for scripting logins in SSMS for Babelfish.

**Critical enhancements**
+ Added “\+” and “-” operator for varbinary.
+ Added new GUCs `babelfishpg_tsql.apg_enable_correlated_scalar_transform` and `babelfishpg_tsql.apg_enable_subquery_cache` to control subquery optimization features in Babelfish. The new GUCs are ON by default.
+ Added support for larger server hello messages during SSL handshake by segmenting them into 4096 byte packets.
+ Added support for CAST from VARBINARY to DATETIME in Babelfish.
+ Added support for altering user/role in Babelfish GroupAD for fixed database roles’ member.
+ Allow CREATE schema in Babelfish GroupAD via fixed db roles’ membership.
+ Fixed an issue with object ownership. Any new object created by a user from TDS endpoint will now be owned by schema owner as opposed to previous behaviour where the current user always owned the new object.
+ Added handling for default schema name for procedure in Group-AD session, when Table Valued Parameter is used as an argument of a procedure.

**High Priority stability enhancements**
+ Fixed logic to adjust precision and scale in Numeric Multiplication and Division.
+ Fixed computation of precision and scale for User defined types.
+ Fixed computation of precision and scale for constant with value 0.
+ Fixed the issue `wrong varnullingrels` error could be reported incorrectly after subquery transformation.
+ Fixed the issue that alter table will cause follow up cacade drop cmd failed to drop the database contain this table.
+ Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
+ Restrict dropping of Babelfish login via PG port, if a BBF login has mapped users in all three master, tempdb and msdb databases.
+ Fixed permission denied error in Babelfish Group AD while using table variables in some scenarios.
+ Fixed bug which prevented enable/disable all triggers on tables.
+ Fixed incorrect conversion from integers to varbinary datatype.
+ Fixed Casting and Conversion from Float to Varchar datatype.
+ Fixed suser\_sname() function to handle the null inputs.
+ Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
+ Fixed issue which causes incorrect result in arithmetic operations which results in numeric/decimal type.
+ Fixed an issue which caused communication link failure with DROP LOGIN/USER/ROLE [public].
+ Restricted dropping of system procedures and views from dbo schema.
+ Fixed an issue in round() function to ensure return types match input argument types.
+ Transfer nullability and identity properties of columns in SELECT INTO statement to new table. These properties are only transferred if there is a single table in FROM clause of SELECT INTO and the column isn't part of expression in select into statements target list.

**Additional improvements and enhancements**
+ Fixed JSON string formatting to prevent improper backslash escaping in “FOR JSON” output with json\_query function.
+ Fixed CONVERT function to allow empty string values to be converted to `datetime` format.
+ Fixed an issue where guest user could create objects in guest schema.
+ Fixed PUBLIC role attributes in system views.
+ Fixed sys.objects catalog to correctly populate unique constraints metadata.
+ Fixed issue when max length of a RPC character based parameter is 0.
+ Restricted members of fixed database role db\_ddladmin from creating schema for database principals that it isn't a member of.
+ Restricted members of fixed database role db\_ddladmin from creating schema for database principals that it isn't a member of.
+ Added an escape hatch for the INLINE option in CREATE FUNCTION statements, defaulting to “strict” mode for proper error handling.
+ Fixed the entry in `babelfish_schema_permissions` which was getting overridden if there were table and procedure with the same name.
+ Fixed an errors while fetching the object definition of tsql objects due to handling of few nodes in `sys.tsql_get_expr`.
+ Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
+ Fixed some cases of object resolution inside stored procedures, functions and trigger.
+ Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
+ Improved index name handling in Babelfish by preserving the original index name in the catalog, making it visible in catalog views like sys.indexes. It also adds support for renaming existing indexes using sp\_rename to preserve and display their original names.
+ Fixed a crash in resolve\_numeric\_typmod\_from\_exp for aggragate functions using \*(all columns).

### Babelfish for Aurora PostgreSQL 4.5
<a name="AuroraBabelfish.Updates.45X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.8. For more information about the improvements in Aurora PostgreSQL 16.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.5.3, February 02, 2026](#AuroraBabelfish.Updates.453)
+ [Aurora Babelfish release 4.5.2, October 09, 2025](#AuroraBabelfish.Updates.452)
+ [**Aurora Babelfish release 4.5.1, June 03, 2025**](#AuroraBabelfish.Updates.451)
+ [Aurora Babelfish release 4.5.0, April 08, 2025](#AuroraBabelfish.Updates.450)

#### Aurora Babelfish release 4.5.3, February 02, 2026
<a name="AuroraBabelfish.Updates.453"></a>

**Critical stability enhancements**
+ Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

#### Aurora Babelfish release 4.5.2, October 09, 2025
<a name="AuroraBabelfish.Updates.452"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.
+ Fixed crash in `resolve_numeric_typmod_from_exp` for aggragate functions using \*(all columns)

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### **Aurora Babelfish release 4.5.1, June 03, 2025**
<a name="AuroraBabelfish.Updates.451"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

**Critical stability enhancements**
+ Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 4.5.0, April 08, 2025
<a name="AuroraBabelfish.Updates.450"></a>

**New Features**
+ Added support for fixed database-level roles `db_securityadmin`, `db_accessadmin`, `db_ddladmin`, `db_datareader` and `db_datawriter`. T-SQL users can be added to these fixed database roles.
+ Added support for fixed server-level roles `securityadmin` and `dbcreator`. T-SQL logins can be added to these fixed server roles.
+ Added support for adding T-SQL users to `db_owner` fixed database-level role. This T-SQL will have privileges similar to the database owner.

For more information about relevant permission management and access control settings for these new features in Babelfish, see [Managing permissions and access control in Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-permissions.html).

**Critical enhancements**
+ Fixed the issue of parameter declarations containing \# characters not being handled correctly.
+ Supported `SET IDENTITY_INSERT` for three part relation references.
+ Fixed an issue with the `HASHBYTES` function to ensure correct behavior when processing `NVARCHAR` argument.
+ Fixed the issue of `CREATE PARTITION SCHEME` not supporting “PRIMARY” syntax.
+ Fixed the issue of UPDATE/DELETE of table variable query in a function getting incorrectly rejected with multi-table FROM clause.
+ Restricted user defined @@function from being mapped to sys function.
+ Fixed the issue of comparison with empty double quoted string raised the error about “zero-length delimited identifier”.
+ Fixed a crash which could occur in rare situations when using temporary tables with certain orphaned catalog entries.
+ Fixed an issue where trigger gets dropped when dropping a column in a table.
+ Improved performance of queries having join between `TABLE_CONSTRAINTS` and `KEY_COLUMN_USAGE` view in the INFORMATION\_SCHEMA schema.
+ Fixed inconsistent formatting issue with `Convert` function when converting MONEY datatype with value 0 to string datatypes.
+ Fixed formatting issues in `CAST` from `MONEY` to `CHAR/VARCHAR`.
+ Fixed the issue where `SELECT...INTO` with `MIN` and `MAX` aggregations on `MONEY` columns lost type information.
+ Implement modulo operator for `MONEY` type.
+ Added Cleanup of stale parameters and configs in case of connection pooling.
+ Added comprehensive cursor state cleanup to avoid stale data in case of connection pooling.
+ Fixed a issue with `IDENTITY` columns not being recognized during `DML` statements using `OUTPUT` and `WHERE` clause.

**High Priority stability enhancements**
+ Fixed an issue where @@function in `UPDATE SET` clause causes syntax error.
+ Fixed dynamic evaluation of @local\_var for `UPDATE ... SET` @local\_var and `SELECT` command.
+ Fixed an issue with `sp_columns_100` where partial data could be returned if @fUsePattern = 0 is used.
+ Fixed an issue where local variables may not be updated correct when query involves manipulation of local variable.
+ Improved the general performance of antlr parsing.
+ Fixed an issue with system function `OPENJSON`.
+ Fixed the incorrect result datatype of `UNION` involving `MONEY` type.
+ Fixed offset when using “`AT TIME ZONE`” with `DATETIME2` datatype conversion with convert() function in non-default local timezone setting.
+ Improved string functions to handle a wider range of datatypes.
+ Fixed an issue where batches containing cross database queries looks up the objects in incorrect database.
+ Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions for week and quarter `Datepart`.
+ Fixed an issue where `sys.column_property` may return incorrect results for ordinal property of a column.
+ Fixed “`AT TIME ZONE`” issue near DST change time with `DATETIME2` datatype conversion.
+ Fixed behavior of queries which use `sys.Db_id()` function which returned empty rows in enforced parallel mode.

**Additional improvements and enhancements**
+ Optimize execution the `plan` extension by removing unnecessary `CAST` functions.
+ `EXECUTE`() on a double-quoted string no longer raises an error.
+ Fixed an error when using functions as column default values on temp tables.
+ Fixed an error in `OPENJSON` function call to allow parse on long `JSON` string.
+ Fixed issue where dropping member from role does not work after restoring Babelfish database.
+ Fixed the alias issue when if exists co-exists with a “=” alias in select list.
+ Restricted declaring the reserved @@function names as common variables.
+ Corrected the implementation of procedure `sp_helpuser` for database roles where `sp_helpuser` should show roles only when explicitly specified.
+ Fixed an issue where smalldatetime type and date type can more flexibly access data through index.
+ Fixed an issue with system procedure `fn_listextendedproperty`.
+ Fixed the use of table-valued parameters as arguments in procedures. Previously, you had to specify the type name of the table-valued parameter when calling the procedure, now it is optional.
+ Fixed precision and scale when common type of `CASE` expression is `NUMERIC` / `DECIMAL` .
+ Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for already terminated connections.
+ Fixed an issue where a login with mapped database user still has guest user privileges.
+ Fixed an issue where transaction count changes after execution of some system functions.
+ Fixed issue where `Datepart` functions were having different output based on the GUC `timezone`.

### Babelfish for Aurora PostgreSQL 4.4
<a name="AuroraBabelfish.Updates.44X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.6. For more information about the improvements in Aurora PostgreSQL 16.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.4.3, November 13, 2025](#AuroraBabelfish.Updates.443)
+ [Aurora Babelfish release 4.4.2, June 24, 2025](#AuroraBabelfish.Updates.442)
+ [Aurora Babelfish release 4.4.1, January 20, 2025](#AuroraBabelfish.Updates.441)
+ [Aurora Babelfish release 4.4.0, December 27, 2024](#AuroraBabelfish.Updates.440)

#### Aurora Babelfish release 4.4.3, November 13, 2025
<a name="AuroraBabelfish.Updates.443"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 4.4.2, June 24, 2025
<a name="AuroraBabelfish.Updates.442"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 4.4.1, January 20, 2025
<a name="AuroraBabelfish.Updates.441"></a>

**High priority stability enhancements**
+ Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 4.4.0, December 27, 2024
<a name="AuroraBabelfish.Updates.440"></a>

***New features***
+ Added support for `ALTER FUNCTION` syntax.
+ Added support for view usage for `PIVOT` operator .
+ Added `pgaudit` extension support with Babelfish.
+ Added support of XML method `.EXIST()` for XML Datatypes.
+ Enabled support of Geospatial data types in data migration via DMS for Babelfish under PostgreSQL endpoint.
+ Enabled user to create database with specific collations. For more information, see [Collation supported at database level in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-collations.html#babelfish-collations.database-level).
+ Enabled support of `sys.sp_reset_connection` stored procedure to reset connection.
+ Enabled cross-database references of objects (tables/views/functions) in views.
+ Enabled support of `sys.dm_os_sys_info` view to provides information about the instance like `server_start_time` and `ms_ticks`.
+ Enabled support of user connection and network packet size information in `sys.configurations` view.
+ Enabled support of correlated subquery transformation for more scenarios. For more information, refer to Limitations section in [Improving Babelfish query performance using subquery transformation ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-correlated-subquery.html#babelfish-corsubquery-transformation).

***High priority stability enhancements***
+ Fixed date functions to take into account the timezone setting.
+ Improved error handling behavior for `relation does not exist` and `column does not exist` errors.
+ Fixed `sp_tables` stored procedure to correctly handle three-part object names across databases to retrieve correct database name during linked servers usage.
+ Fixed an issue to enable database owner login to explore database objects in SSMS.
+ Fixed `sp_tables` stored procedure to return correct result when @table\_name parameter has square brackets around underscore (\_).
+ Fixed an issue where individual login active directory authentication used to throw error of pg\_ad\_mapping the `plugin` extension pointer not initialized.
+ Fixed an issue where index creation could fail if the table is created using SELECT INTO syntax.
+ Fixed an permission issue with cross-database function calls.
+ Enabled Grant on schema to takes effect correctly on future objects created in that schema by any of the schema’s authorized users.
+ Fixed an issue to pick correct collation for prepared statements.
+ Fixed an issue to have foreign key constraint check work correctly when column is created using non-default collation.
+ Enabled the bcp queries to run with the `pgaudit` extension enabled.
+ Fixed an issue to insert correct value in the table having identity column.
+ Fixed an issue to have correct identity sequence value when bcp / SqlBulkCopy / insert bulk are used with `keep identity values` mode.

***Additional improvements and enhancements***
+ Fixed the issue with Kill command which still left few sessions running after the command.
+ Fixed the issue of `sys.identity_columns` view was wrongly returning more entries than it should.
+ Fixed the issue of CASE statement and MIN/MAX functions related to error of string size not being defined or using explicit cast.
+ Fixed an issue with `ISNUMERIC` function to return correct result for nvarchar/varchar parameters.
+ Fixed the issue of CASE statement not working correctly when branch expression is of NVARCHAR type.
+ Fixed behavior of CONCAT() and CONCAT\_WS() functions for multibyte characters and to work with atleast 2 and 3 arguments respectively.
+ Fixed an issue to allow ALTER COLUMN with type char for Temp Table.
+ Fixed an issue in CONVERT function to make it work consistently with BINARY and VARBINARY types in Babelfish.
+ Fixed the issue of inconsistent output from select query with FOR XML PATH clause.
+ Fixed an issue to rethrow correct TSQL error code.
+ Fixed behaviour of STRING\_AGG() function for input containing multibyte characters.
+ Fixed an issue where wrong overloaded variant of regexp\_replace is called during restore.
+ Fixed cast from sys.varchar to TIME type.
+ Enabled use of nvarchar(max) as output parameter in procedure.
+ Fixed an issue of missing brackets while declaring the variables in the definition of procedure.

### Babelfish for Aurora PostgreSQL 4.3
<a name="AuroraBabelfish.Updates.43X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.4. For more information about the improvements in Aurora PostgreSQL 16.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.3.3, November 21, 2025](#AuroraBabelfish.Updates.433)
+ [Aurora Babelfish release 4.3.2, July 11, 2025](#AuroraBabelfish.Updates.432)
+ [Aurora Babelfish release 4.3.1, January 02, 2025](#AuroraBabelfish.Updates.431)
+ [Aurora Babelfish release 4.3.0, September 30, 2024](#AuroraBabelfish.Updates.430)

#### Aurora Babelfish release 4.3.3, November 21, 2025
<a name="AuroraBabelfish.Updates.433"></a>

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 4.3.2, July 11, 2025
<a name="AuroraBabelfish.Updates.432"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 4.3.1, January 02, 2025
<a name="AuroraBabelfish.Updates.431"></a>

**High priority stability enhancements**
+ Fixed an issue where individual login active directory authentication used to throw error of `pg_ad_mapping` the `plugin` extension pointer not initialized.
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

**Additional improvements and enhancements**
+ Fixed an issue where reserved keyword `PRIMARY` caused syntax errors when used as a column name or alias in DML and DDL statements.

#### Aurora Babelfish release 4.3.0, September 30, 2024
<a name="AuroraBabelfish.Updates.430"></a>

**New Features**
+ Added support for Partitioning in Babelfish. For more information, see [Understanding partitioning in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-partition.html).
+ Support system functions `CHARINDEX()`, `PATINDEX()` and `REPLACE()` for Babelfish non deterministic collations.
+ Enabling support for `STContains`, `STEquals`, `STArea` the `PostGIS` extension functions for geospatial datatypes.

**Security enhancements**
+ Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
+ Fixed an issue with `sys.database_principals` view where it was showing metadata related to all the users irrespective of privileges of server principal.

**High Priority stability enhancements**
+ Fixed an issue with information\_schema.tables returning incorrect table\_name.
+ Fixed an issue where less than operator gives incorrect results for binary data types.
+ Fixed inconsistency with OIDs of triggers in `OBJECT_ID()` function and `sys.objects` view.
+ Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is installed.

**Additional improvements and enhancements**
+ Fixed behavior of `TRIM()`, `LTRIM()`, `RTRIM()`, `LEFT()`, and `RIGHT()` functions for input containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
+ Improved performance of like operator with non deterministic collations.
+ Fixed an issue where search patch may be incorrect when database name and/or schema name contains special characters in quotes.
+ Fixed difference in behavior in Babelfish and TSQL for `UPPER()` and `LOWER()` functions with multibyte characters and appropriate argument and return types.
+ Added Support of `WITH RECOMPILE` for Transact-SQL stored procedures and for ALTER PROCEDURE clause.
+ The `sp_tables` procedure now allows you to use the `%` wildcard character in the `@table_qualifier` parameter. This makes it easier to search for tables by matching patterns in the table names.
+ Fixed difference in behavior in Babelfish and TSQL for `STUFF()` , `SUBSTRING()` and `TRANSLATE()` functions with multibyte characters and appropriate argument and return types.
+ Updated error message for `GRANT`, `REVOKE`, `DENY` statements.
+ Fixed behavior of `REVERSE()`, `REPLACE()`, and `REPLICATE()` functions for input containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
+ Fixed output of `SPACE()` function for non-positve input argument.
+ Improved memory handling when using BCP on a table with indexes.
+ Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
+ Fixed a data type resolve issue with union clause.
+ Fixed an error message for `SUBSTRING()` function when the number of arguments are not appropriate.
+ Fixed an issue when comment comes with the column name.
+ Fixed an issue with `sys.server_principals` view to show `public` role entry.
+ Added support for `WITHIN GROUP` clause for `STRING_AGG()` function.
+ Fixed DDL export issue for database with SSMS.
+ Added support for new vector extensions like `halfvec` and sparsevec which got introduced in version 0.7 of pgvector.
+ Added support to show windows group membership in T-SQL function `IS_MEMBER()`.

### Babelfish for Aurora PostgreSQL 4.2
<a name="AuroraBabelfish.Updates.42X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.3. For more information about the improvements in Aurora PostgreSQL 16.3, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.2.3, July 17, 2025](#AuroraBabelfish.Updates.423)
+ [Aurora Babelfish release 4.2.2, January 23, 2025](#AuroraBabelfish.Updates.422)
+ [Aurora Babelfish release 4.2.1, September 27, 2024](#AuroraBabelfish.Updates.421)
+ [Aurora Babelfish release 4.2.0, August 8, 2024](#AuroraBabelfish.Updates.420)

#### Aurora Babelfish release 4.2.3, July 17, 2025
<a name="AuroraBabelfish.Updates.423"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 4.2.2, January 23, 2025
<a name="AuroraBabelfish.Updates.422"></a>

**High priority stability enhancements**
+ Fixed an issue where individual login active directory authentication used to throw error of pg\_ad\_mapping the `plugin` extension pointer not initialized.
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 4.2.1, September 27, 2024
<a name="AuroraBabelfish.Updates.421"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.2.0, August 8, 2024
<a name="AuroraBabelfish.Updates.420"></a>

**New features**
+ Introduced support for PostgreSQL native logical replication so that users can replicate and synchronize individual tables from a source to one or more recipients using a publisher and subscriber model.
+ Added support for Blue/Green deployments with Babelfish. You can now use Amazon RDS Blue/Green Deployments, to make and test database changes before implementing them in a production environment. For more information, see [Overview of Amazon RDS Blue/Green Deployments for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html).
+ Added support for GRANT/REVOKE .. ON SCHEMA .. in Babelfish. 
  + Following permissions are supported based on the object types.
    + Scalar function permissions – EXECUTE.
    + Table-valued function permissions – EXECUTE.
    + Stored procedure permissions – EXECUTE.
    + Table permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
    + View permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
  + CASCADE isn't supported with Grant/Revoke on Schema.
  + GRANT/REVOKE OPTION FOR .. on SCHEMA isn't supported in Babelfish.
  + GRANT/REVOKE inside CREATE SCHEMA isn't supported in Babelfish.
+ Added support for `sys.login_token` and `sys.user_token` system views.
+ Added support for LIKE clause for some AI collations. For more information, see [Deterministic and nondeterministic collations in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-collations.html#babelfish-collations.deterministic-nondeterministic).
+ Added support to Group Security based Active Directory authentication. Users can manage their workloads without provisioning individual logins with enhanced security posture. For more information, see [Setting up kerberos authentication using Active Directory security groups for Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad.html).
+ Added support of CTE and JOIN for PIVOT operator.
+ Support ALTER syntax for Proc.
+ Support renaming of a SQL Server database.
+ Support unique constraints on nullable columns. Escape hatch `babelfishpg_tsql.escape_hatch_unique_constraint` has been deprecated. 
+ Introduced support to correlated subquery transform and cache for enhancement of query performance by transforming scalar correlated subquery into join query, or caching the subquery result set and reduce duplicate subquery re-executions when transformation is not possible. For more information, see [Improving Aurora PostgreSQL query performance using subquery transformation ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-correlated-subquery.html#apg-corsubquery-transformation).

**Critical stability enhancements**
+ Fixed issue producing syntax error with delimited column alias without preceding whitespace.
+ Creating a user for a login is blocked when its login is already a member of sysadmin.
+ Fixed the column type of the T-SQL views to use nvarchar(max).
+ Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.
+ Fixed casting issue from geometry to `varbinary` or `byte` datatype when `SRID` is zero.
+ Fixed the issue of indexes not being used in case of queries comparing numeric and integer data types.

**High priority stability enhancements**
+ Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
+ Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
+ Fixed issue of crash under certain conditions while executing bulk copy.
+ Crash in `handle_where_clause_restargets_right()`.
+ Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
+ Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
+ Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
+ Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
+ Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases. 
+ Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
+ Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
+ Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
+ Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.
+ Fixed an issue where some queries with ORDER BY clause did not use primary key indexes.
+ Fixed an issue with CREATE/ALTER PROCEDURE command that could cause server restart if procedure name contains special white characters.
+ Fixed an issue where query may return incorrect result when predicate involves SCOPE\_IDENTITY().

**Additional improvements and enhancements**
+ Fixed memory leak in decimal (numeric) conversion for BCP import.
+ Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
+ Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
+ Added restriction on dropping of Babelfish extensions for all users except admin role.
+ Prevent partial upgrades of Babelfish extensions.
+ sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
+ DDL scripting of indexes or constraints will now include correct ordering with columns.
+ Fixed an error to allow referencing a `#tmp table` in a nested procedure through OBJECT\_ID() clause.
+ Fixed an issue to avoid error when dropping trigger created on temp table.
+ Made an enhancement to allow table variables having a name longer than 63 characters.
+ Fixed issue with --schema-only and --data-only options of BabelfishDump utilities.
+ Fixed issue with BabelfishDump utility where it wasn't able to dump extended properties.
+ Fixed issue of fully qualified column reference doesn't work in PIVOT aggregate function.
+ Fixed an error to allow alter procedure from PG endpoint.
+ Blocked SET/RESET role statements execution from TDS endpoint.
+ Changed the default behavior of the full-text search GUC to have the feature turned `OFF` by default. You can set the GUC to `ignore` to use FTS features.

### Babelfish for Aurora PostgreSQL 4.1
<a name="AuroraBabelfish.Updates.41X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.2. For more information about the improvements in Aurora PostgreSQL 16.2, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.1.4, July 30, 2025](#AuroraBabelfish.Updates.414)
+ [Aurora Babelfish release 4.1.3, February 02, 2025](#AuroraBabelfish.Updates.413)
+ [Aurora Babelfish release 4.1.2, October 7, 2024](#AuroraBabelfish.Updates.412)
+ [Aurora Babelfish release 4.1.1, June 20, 2024](#AuroraBabelfish.Updates.411)
+ [Aurora Babelfish release 4.1.0, April 29, 2024](#AuroraBabelfish.Updates.410)

#### Aurora Babelfish release 4.1.4, July 30, 2025
<a name="AuroraBabelfish.Updates.414"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 4.1.3, February 02, 2025
<a name="AuroraBabelfish.Updates.413"></a>

**High priority stability enhancements**.
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 4.1.2, October 7, 2024
<a name="AuroraBabelfish.Updates.412"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.1.1, June 20, 2024
<a name="AuroraBabelfish.Updates.411"></a>

**High priority stability enhancements**
+ Optimized performance for Create and Drop Databases for Babelfish.
+ Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 4.1.0, April 29, 2024
<a name="AuroraBabelfish.Updates.410"></a>

**New features**
+ Babelfish introduces support for two spatial data types Geometry and Geography to store and manipulate spatial data under a limited scope. For more information, see [Babelfish supports Geospatial data types](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html).
+ Allowing `SELECT FOR JSON AUTO` support in Babelfish.
+ Support the ability to perform vector similarity search using the `pgvector` extension through Babelfish. The ability to use `HNSW` and `IVFLAT` indexes is also supported. For more information, see [Using pgvector in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html#babelfish-postgres-aws-extensions-using-pgvector).
+ Support the ability to access Amazon Machine Learning services such as Amazon Comprehend, Amazon Sagemaker and Amazon Bedrock through `aws_ml` extension. For more information, see [Using Amazon Aurora machine learning with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html#babelfish-postgres-aws-extensions-using-ml).
+ Support T-SQL procedure `sp_procedure_params_100_managed`.
+ CONTAINS clause used in Full Text Search will also support for special characters and single digit in search condition. For more information, see [Full Text Search in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-fulltextsearch.html).

**Critical stability enhancements**
+ Fixed an issue in Object Explorer Database enumeration with SSMS version 19.2.
+ Fixed an issue that caused error during Selecting data from variable `NVARCHAR(MAX)`, `VARCHAR(MAX)`, `VARBINARY(MAX)` with large length strings.
+ Fixed blank space padding related issue in char datatype for multibyte characters.
+ Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
+ Fixed default column collation to match server collation handled through `babelfishpg_tsql.server_collation_name` for some system views. List of fixed system views are `sys.check_constraints`, `sys.data_spaces`, `sys.default_constraints`, `sys.dm_exec_connections`, `sys.foreign_keys`, `sys.key_constraints`, `sys.stats`, `sys.syscolumns`, `sys.sysforeignkeys`, `sys.sysprocesses`, `sys.system_objects`, `sys.table_types`, `sys.tables`, `sys.types`, `sys.views` and `sys.xml_indexes`.
+ Restrict creation of functions/procedures with the same name in Babelfish.

**High priority stability enhancements**
+ Improved performance for system procedure `sp_tablecollations_100`.
+ Fixed an issue with major version upgrades where views contains cast from string literal to binary type.
+ Fixed a bug where parallel worker was unable to fetch the logical database name.
+ Fixed the performance issue of comparing `date` to `datetime`.

**Additional improvements and enhancements**
+ Fixed an issue on duplicate `object_id` in `sys.all_objects` after major version upgrade.
+ Fixed an issue in `CAST` functions for `Binary` to `Varchar` and `Rowversion` to `Varchar`.
+ Fixed an issue with insert into statement execution with table variable when table variable did not exist.
+ Fixed an issue where input hex string being converted to type binary did not have the correct data length.
+ Fixed an issue with mixed casing error in `sp_columns_100`.
+ Fixed a crash in Table Variable lookup after `TVP` execution via `TDS RPC SPExecuteSQL`.
+ Support embedded whitespace in multi-character comparison operators.
+ Support operators adjacent to `@@variables` without separating whitespace.
+ Fixed a crash with procedure execution if procedure deletes itself or rolls back the transaction which created the procedure.
+ Support for the `AS` keyword in `CREATE` function for all cases.
+ Support expressions in `SELECT...OFFSET...FETCH` clauses.
+ Support `SET TRAN ISOLATION LEVEL` syntax.
+ Support floating-point notation without exponent.
+ Support comparison operators `!<` and `!>`.
+ Support for `DROP INDEX schema.table.index` and `DROP INDEX index ON schema.table` syntax.

### Babelfish for Aurora PostgreSQL 4.0
<a name="AuroraBabelfish.Updates.40X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.1. For more information about the improvements in Aurora PostgreSQL 16.1, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 4.0 (version 4.0 is build on top of version 3.4) adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 4.0.4, August 4, 2025](#AuroraBabelfish.Updates.404)
+ [Aurora Babelfish release 4.0.3, February 5, 2025](#AuroraBabelfish.Updates.403)
+ [Aurora Babelfish release 4.0.2, September 17, 2024](#AuroraBabelfish.Updates.402)
+ [Aurora Babelfish release 4.0.1, June 24, 2024](#AuroraBabelfish.Updates.401)
+ [Aurora Babelfish release 4.0.0, January 31, 2024](#AuroraBabelfish.Updates.400)

#### Aurora Babelfish release 4.0.4, August 4, 2025
<a name="AuroraBabelfish.Updates.404"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 4.0.3, February 5, 2025
<a name="AuroraBabelfish.Updates.403"></a>

**High priority stability enhancements**
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 4.0.2, September 17, 2024
<a name="AuroraBabelfish.Updates.402"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.0.1, June 24, 2024
<a name="AuroraBabelfish.Updates.401"></a>

**High priority stability enhancements**
+ Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
+ Optimized performance for Create and Drop Databases for Babelfish.
+ Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 4.0.0, January 31, 2024
<a name="AuroraBabelfish.Updates.400"></a>

**New features**
+ Limited support for Full Text Search in Babelfish. For more information, see [Full Text Search in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-fulltextsearch.html).
+ Added support for creating INSTEAD OF Triggers on Views.
+ Changed the default Babelfish migration mode from single database to multiple databases.

**Security enhancements**
+ Fixed security issues with handling of TSQL login and users.

**High priority stability enhancements**
+ Fixed a regression issue where update-join with inserted table in trigger procedure causes `result relation must be a regular relation` error.
+ Fixed the issue where querying `information_schema` for type U and V was earlier giving different results in Babelfish.
+ Fixed an issue to avoid blocking of vacuum progress when using temp tables in certain situations.

**Additional improvements and enhancements**
+ Fixed an issue with principal name in `pg_stat_gssapi` catalog view.
+ Fixed issue in functions `parsename`, `session_context` and `sp_set_session_context` when using with non-default server collation.

**Recommendations**
+ We recommend you to upgrade from Aurora PostgreSQL version 14 to 15 and then from version 15 to 16. Currently, direct upgrade from version 14 to 16 isn't supported and it fails with an error. 

## Babelfish for Aurora PostgreSQL 3.x versions (includes some deprecated versions)
<a name="aurorababelfish-versions-version3x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 3.14](#AuroraBabelfish.Updates.314X)
+ [Babelfish for Aurora PostgreSQL 3.13](#AuroraBabelfish.Updates.313X)
+ [Babelfish for Aurora PostgreSQL 3.12](#AuroraBabelfish.Updates.312X)
+ [Babelfish for Aurora PostgreSQL 3.11](#AuroraBabelfish.Updates.311)
+ [Babelfish for Aurora PostgreSQL 3.10](#AuroraBabelfish.Updates.310)
+ [Babelfish for Aurora PostgreSQL 3.9](#AuroraBabelfish.Updates.39X)
+ [Babelfish for Aurora PostgreSQL 3.8](#AuroraBabelfish.Updates.38X)
+ [Babelfish for Aurora PostgreSQL 3.7](#AuroraBabelfish.Updates.37X)
+ [Babelfish for Aurora PostgreSQL 3.6](#AuroraBabelfish.Updates.36X)
+ [Babelfish for Aurora PostgreSQL 3.5](#AuroraBabelfish.Updates.35X)
+ [Babelfish for Aurora PostgreSQL 3.4](#AuroraBabelfish.Updates.34X)
+ [Babelfish for Aurora PostgreSQL 3.3](#AuroraBabelfish.Updates.33X)
+ [Babelfish for Aurora PostgreSQL 3.2](#AuroraBabelfish.Updates.32X)
+ [Babelfish for Aurora PostgreSQL 3.1 (Deprecated)](#AuroraBabelfish.Updates.31X)

### Babelfish for Aurora PostgreSQL 3.14
<a name="AuroraBabelfish.Updates.314X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.18. For more information about the improvements in Aurora PostgreSQL 15.18, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.14 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 3.14.0, August 21, 2026
<a name="AuroraBabelfish.Updates.3140"></a>

**Critical enhancements**
+ Fixed an issue that could cause crash in SPI\_finish after Out Of Memory error.

### Babelfish for Aurora PostgreSQL 3.13
<a name="AuroraBabelfish.Updates.313X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.17. For more information about the improvements in Aurora PostgreSQL 15.17, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 3.13.0, April 6, 2026
<a name="AuroraBabelfish.Updates.3130"></a>

**Critical enhancements**
+ Fixed an issue where update with output clause may skip rows during concurrent updates.

**High Priority stability enhancements**
+ Blocked GRANT/REVOKE/DROP operations on Babelfish roles from PostgreSQL endpoint.

### Babelfish for Aurora PostgreSQL 3.12
<a name="AuroraBabelfish.Updates.312X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.15. For more information about the improvements in Aurora PostgreSQL 15.15, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.12 adds several enhancements and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 3.12.1, January 16, 2026
<a name="AuroraBabelfish.Updates.3121"></a>

**Critical stability enhancements**
+ Fixed an issue where an `UPDATE` statement with `OUTPUT` clause may skip rows when there are concurrent updates on the same row.

#### Aurora Babelfish release 3.12.0, December 18, 2025
<a name="AuroraBabelfish.Updates.3120"></a>

**Critical enhancements**
+ Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.

**High Priority stability enhancements**
+ Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
+ Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.

**Additional improvements and enhancements**
+ Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.

### Babelfish for Aurora PostgreSQL 3.11
<a name="AuroraBabelfish.Updates.311"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.14. For more information about the improvements in Aurora PostgreSQL 15.14, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.11 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.11.0, November 25, 2025](#AuroraBabelfish.Updates.3110)

#### Aurora Babelfish release 3.11.0, November 25, 2025
<a name="AuroraBabelfish.Updates.3110"></a>

**Critical enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations
+ Added support to let index scan used in case of queries having predicates comparing numeric and integer data types

**High Priority stability enhancements**
+ Fixed an issue with RESET ALL command from postgres endpoint
+ Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
+ Fixed an issue where parallelism won't be used for pltsql RETURN expression
+ Fixed an issue to preserve Timezone information during casting from string to datetimeoffset
+ Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'

**Additional improvements and enhancements**
+ Fixed an issue while adding a column with default value which resulted in an error

### Babelfish for Aurora PostgreSQL 3.10
<a name="AuroraBabelfish.Updates.310"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.13. For more information about the improvements in Aurora PostgreSQL 15.13, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.10 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.10.1, August 08, 2025](#AuroraBabelfish.Updates.3101)
+ [Aurora Babelfish release 3.10.0, June 30, 2025](#AuroraBabelfish.Updates.3100)

#### Aurora Babelfish release 3.10.1, August 08, 2025
<a name="AuroraBabelfish.Updates.3101"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 3.10.0, June 30, 2025
<a name="AuroraBabelfish.Updates.3100"></a>

**Critical enhancements**
+ Added support for larger server hello messages during SSL handshake by segmenting them into 4096 byte packets.
+ Added support for CAST from VARBINARY to DATETIME in Babelfish.
+ Added handling for default schema name for procedure in Group-AD session, when Table Valued Parameter is used as an argument of a procedure.
+ Added “\+” and “-” operator for varbinary.

**High Priority stability enhancements**
+ Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
+ Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
+ Fixed issue which causes incorrect result in arithmetic operations which results in numeric/decimal type.
+ Fixed an issue in round() function to ensure return types match input argument types.

**Additional improvements and enhancements**
+ Fixed the entry in `babelfish_schema_permissions` which was getting overridden if there were table and procedure with the same name.
+ Fixed an errors while fetching the object definition of tsql objects due to handling of few nodes in `sys.tsql_get_expr`.
+ Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
+ Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
+ Fixed a crash in `resolve_numeric_typmod_from_exp` for aggregate functions using \*(all columns).

### Babelfish for Aurora PostgreSQL 3.9
<a name="AuroraBabelfish.Updates.39X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.12. For more information about the improvements in Aurora PostgreSQL 15.12, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.9 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.9.2, October 09, 2025](#AuroraBabelfish.Updates.392)
+ [Aurora Babelfish release 3.9.1, June 03, 2025](#AuroraBabelfish.Updates.391)
+ [Aurora Babelfish release 3.9.0, April 08, 2025](#AuroraBabelfish.Updates.390)

#### Aurora Babelfish release 3.9.2, October 09, 2025
<a name="AuroraBabelfish.Updates.392"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.
+ Fixed crash in `resolve_numeric_typmod_from_exp` for aggragate functions using \*(all columns)

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 3.9.1, June 03, 2025
<a name="AuroraBabelfish.Updates.391"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

**Critical stability enhancements**
+ Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 3.9.0, April 08, 2025
<a name="AuroraBabelfish.Updates.390"></a>

**Critical enhancements**
+ Fixed an issue where trigger gets dropped when dropping a column in a table.
+ Improved performance of queries having join between `TABLE_CONSTRAINTS` and `KEY_COLUMN_USAGE` view in the INFORMATION\_SCHEMA schema.
+ Fixed inconsistent formatting issue with `Convert` function when converting MONEY datatype with value 0 to string datatypes.
+ Fixed formatting issues in `CAST` from `MONEY` to `CHAR/VARCHAR`.
+ Fixed the issue where `SELECT...INTO` with `MIN` and `MAX` aggregations on `MONEY` columns lost type information.
+ Implement modulo operator for `MONEY` type.
+ Added Cleanup of stale parameters and configs in case of connection pooling.
+ Added comprehensive cursor state cleanup to avoid stale data in case of connection pooling.
+ Fixed a issue with `IDENTITY` columns not being recognized during `DML` statements using `OUTPUT` and `WHERE` clause.

**High Priority stability enhancements**
+ Fixed an issue with system function `OPENJSON`.
+ Fixed the incorrect result datatype of `UNION` involving `MONEY` type.
+ Fixed offset when using “`AT TIME ZONE`” with `DATETIME2` datatype conversion with convert() function in non-default local timezone setting.
+ Improved string functions to handle a wider range of datatypes.
+ Fixed an issue where batches containing cross database queries looks up the objects in incorrect database.
+ Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions for week and quarter `Datepart`.
+ Fixed an issue where `sys.column_property` may return incorrect results for ordinal property of a column.
+ Fixed “`AT TIME ZONE`” issue near DST change time with `DATETIME2` datatype conversion.
+ Fixed behavior of queries which use `sys.Db_id()` function which returned empty rows in enforced parallel mode.

**Additional improvements and enhancements**
+ Fixed an issue where smalldatetime type and date type can more flexibly access data through index.
+ Fixed an issue with system procedure `fn_listextendedproperty`.
+ Fixed the use of table-valued parameters as arguments in procedures. Previously, you had to specify the type name of the table-valued parameter when calling the procedure, now it is optional.
+ Fixed precision and scale when common type of `CASE` expression is `NUMERIC` / `DECIMAL` .
+ Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for already terminated connections.
+ Fixed an issue where a login with mapped database user still has guest user privileges.
+ Fixed an issue where transaction count changes after execution of some system functions.
+ Fixed issue where `Datepart` functions were having different output based on the GUC `timezone`.

### Babelfish for Aurora PostgreSQL 3.8
<a name="AuroraBabelfish.Updates.38X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.10. For more information about the improvements in Aurora PostgreSQL 15.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.8 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.8.3, November 13, 2025](#AuroraBabelfish.Updates.383)
+ [Aurora Babelfish release 3.8.2, June 24, 2025](#AuroraBabelfish.Updates.382)
+ [Aurora Babelfish release 3.8.1, January 20, 2025](#AuroraBabelfish.Updates.380)
+ [Aurora Babelfish release 3.8.0, December 27, 2024](#AuroraBabelfish.Updates.380)

#### Aurora Babelfish release 3.8.3, November 13, 2025
<a name="AuroraBabelfish.Updates.383"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 3.8.2, June 24, 2025
<a name="AuroraBabelfish.Updates.382"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 3.8.1, January 20, 2025
<a name="AuroraBabelfish.Updates.380"></a>

**High priority stability enhancements**
+ Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 3.8.0, December 27, 2024
<a name="AuroraBabelfish.Updates.380"></a>

***New features***
+ Added support for `ALTER FUNCTION` syntax.
+ Enabled the `pgaudit` extension support with Babelfish.
+ Enabled user to create view on statement with `PIVOT` operator.
+ Enabled support of `sys.sp_reset_connection` stored procedure to reset connection.
+ Enabled cross-database references of objects (tables/views/functions) in views.

***High priority stability enhancements***
+ Fixed date functions to take into account the timezone setting.
+ Improved error handling behavior for `relation does not exist` and `column does not exist` errors.
+ Fixed `sp_tables` stored procedure to correctly handle three-part object names across databases to retrieve correct database name during linked servers usage.
+ Fixed an issue to enable database owner login to explore database objects in SSMS.
+ Fixed `sp_tables` stored procedure to return correct result when @table\_name parameter has square brackets around underscore (\_).
+ Fixed an issue where individual login active directory authentication used to throw error of `pg_ad_mapping` the `plugin` extension pointer not initialized.
+ Fixed an issue where index creation could fail if the table is created using `SELECT INTO` syntax.
+ Fixed an permission issue with cross-database function calls.
+ Enabled Grant on schema to takes effect correctly on future objects created in that schema by any of the schema’s authorized users.
+ Fixed an issue to insert correct value in the table having identity column.
+ Fixed an issue to have correct identity sequence value when bcp or SqlBulkCopy or insert bulk are used with `keep identity values` mode.

***Additional improvements and enhancements***
+ Fixed the issue with Kill command which still left few sessions running after the command.
+ Fixed the issue of `sys.identity_columns` view was wrongly returning more entries than it should.
+ Fixed the issue of CASE statement and MIN/MAX functions related to error of string size not being defined or using explicit cast.
+ Fixed an issue with ISNUMERIC function to return correct result for nvarchar/varchar parameters.
+ Fixed the issue of CASE statement not working correctly when branch expression is of NVARCHAR type.
+ Fixed behavior of CONCAT() and CONCAT\_WS() functions for multibyte characters and to work with atleast 2 and 3 arguments respectively.
+ Fixed an issue to allow ALTER COLUMN with type char for Temp Table.
+ Fixed an issue in CONVERT function to make it work consistently with BINARY and VARBINARY types in Babelfish.
+ Fixed the issue of inconsistent output from select query with FOR XML PATH clause.
+ Fixed an issue to rethrow correct TSQL error code.
+ Fixed behaviour of `STRING_AGG()` function for input containing multibyte characters.
+ Fixed an issue where wrong overloaded variant of `regexp_replace` is called during restore.
+ Fixed cast from `sys.varchar` to TIME type.

### Babelfish for Aurora PostgreSQL 3.7
<a name="AuroraBabelfish.Updates.37X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.8. For more information about the improvements in Aurora PostgreSQL 15.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.7 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.7.3, November 21, 2025](#AuroraBabelfish.Updates.373)
+ [Aurora Babelfish release 3.7.2, July 11, 2025](#AuroraBabelfish.Updates.372)
+ [Aurora Babelfish release 3.7.1, January 02, 2025](#AuroraBabelfish.Updates.371)
+ [Aurora Babelfish release 3.7.0, September 30, 2024](#AuroraBabelfish.Updates.370)

#### Aurora Babelfish release 3.7.3, November 21, 2025
<a name="AuroraBabelfish.Updates.373"></a>

**High priority stability enhancements**
+ Fixed a crash in queries using `FOR JSON AUTO` and `JSON PATH`.

#### Aurora Babelfish release 3.7.2, July 11, 2025
<a name="AuroraBabelfish.Updates.372"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 3.7.1, January 02, 2025
<a name="AuroraBabelfish.Updates.371"></a>

**High priority stability enhancements**
+ Fixed an issue where individual login active directory authentication used to throw error of pg\_ad\_mapping the `plugin` extension pointer not initialized.
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 3.7.0, September 30, 2024
<a name="AuroraBabelfish.Updates.370"></a>

***New Features***
+ Enabling support for `STContains`, `STEquals`, `STArea` the `PostGIS` extension functions for geospatial datatypes.

**Security enhancements**
+ Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
+ Fixed an issue with `sys.database_principals` view where it was showing metadata related to all the users irrespective of privileges of server principal.

**High Priority stability enhancements**
+ Fixed an issue with `information_schema.tables` returning incorrect table\_name.
+ Fixed an issue where less than operator gives incorrect results for binary data types.
+ Fixed inconsistency with OIDs of triggers in `OBJECT_ID()` function and `sys.objects` view.
+ Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is installed.

**Additional improvements and enhancements**
+ Fixed behavior of `TRIM()`, `LTRIM()`, `RTRIM()`, `LEFT()`, and `RIGHT()` functions for input containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
+ Improved performance of like operator with non deterministic collations.
+ Fixed an issue where search patch may be incorrect when database name and/or schema name contains special characters in quotes.
+ Fixed difference in behavior in Babelfish and TSQL for `UPPER()` and `LOWER()` functions with multibyte characters and appropriate argument and return types.
+ The `sp_tables` procedure now allows you to use the `%` wildcard character in the `@table_qualifier` parameter. This makes it easier to search for tables by matching patterns in the table names.
+ Fixed difference in behavior in Babelfish and TSQL for `STUFF()` , `SUBSTRING()` and `TRANSLATE()` functions with multibyte characters and appropriate argument and return types.
+ Updated error message for GRANT/REVOKE/DENY statements.
+ Fixed behavior of `REVERSE()`, `REPLACE()`, and `REPLICATE()` functions for input containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
+ Fixed output of `SPACE()` function for non-positve input argument.
+ Improved memory handling when using BCP on a table with indexes.
+ Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
+ Fixed a data type resolve issue with union clause.
+ Fixed an error message for `SUBSTRING()` function when the number of arguments are not appropriate.
+ Fixed an issue when comment comes with the column name.
+ Fixed an issue with `sys.server_principals` view to show `public` role entry.
+ Fixed DDL export issue for database with SSMS.
+ Added support to show windows group membership in T-SQL function `IS_MEMBER()`.

### Babelfish for Aurora PostgreSQL 3.6
<a name="AuroraBabelfish.Updates.36X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.7. For more information about the improvements in Aurora PostgreSQL 15.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.6.3, July 17, 2025](#AuroraBabelfish.Updates.363)
+ [Aurora Babelfish release 3.6.2, January 23, 2025](#AuroraBabelfish.Updates.362)
+ [Aurora Babelfish release 3.6.1, September 27, 2024](#AuroraBabelfish.Updates.361)
+ [Aurora Babelfish release 3.6.0, August 8, 2024](#AuroraBabelfish.Updates.360)

#### Aurora Babelfish release 3.6.3, July 17, 2025
<a name="AuroraBabelfish.Updates.363"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 3.6.2, January 23, 2025
<a name="AuroraBabelfish.Updates.362"></a>

**High priority stability enhancements**
+ Fixed an issue where individual login active directory authentication used to throw error of pg\_ad\_mapping the `plugin` extension pointer not initialized.
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 3.6.1, September 27, 2024
<a name="AuroraBabelfish.Updates.361"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.6.0, August 8, 2024
<a name="AuroraBabelfish.Updates.360"></a>

**New features**
+ Introduced support for PostgreSQL native logical replication so that users can replicate and synchronize individual tables from a source to one or more recipients using a publisher and subscriber model.
+ Added support for Blue/Green deployments with Babelfish. You can now use Amazon RDS Blue/Green Deployments, to make and test database changes before implementing them in a production environment. For more information, see [Overview of Amazon RDS Blue/Green Deployments for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html).
+ Added support for GRANT/REVOKE .. ON SCHEMA .. in Babelfish. 
  + Following permissions are supported based on the object types.
    + Scalar function permissions – EXECUTE.
    + Table-valued function permissions – EXECUTE.
    + Stored procedure permissions – EXECUTE.
    + Table permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
    + View permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
  + CASCADE isn't supported with Grant/Revoke on Schema.
  + GRANT/REVOKE OPTION FOR .. on SCHEMA isn't supported in Babelfish.
  + GRANT/REVOKE inside CREATE SCHEMA isn't supported in Babelfish.
+ Added support for `sys.login_token` and `sys.user_token` system views.
+ Added support for LIKE clause for some AI collations. For more information, see [Deterministic and nondeterministic collations in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-collations.html#babelfish-collations.deterministic-nondeterministic).
+ Added support to Group Security based Active Directory authentication. Users can manage their workloads without provisioning individual logins with enhanced security posture. For more information, see [Setting up kerberos authentication using Active Directory security groups for Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad.html).
+ Added support of CTE and JOIN for PIVOT operator.
+ Support ALTER syntax for Proc.
+ Support renaming of a SQL Server database.
+ Support unique constraints on nullable columns. Escape hatch `babelfishpg_tsql.escape_hatch_unique_constraint` has been deprecated. 

**Critical stability enhancements**
+ Fixed issue producing syntax error with delimited column alias without preceding whitespace.
+ Creating a user for a login is blocked when its login is already a member of sysadmin.
+ Fixed the column type of the T-SQL views to use nvarchar(max).
+ Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.
+ Fixed casting issue from geometry to `varbinary` or `byte` datatype when `SRID` is zero.
+ Fixed the issue of indexes not being used in case of queries comparing numeric and integer data types.

**High priority stability enhancements**
+ Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
+ Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
+ Fixed issue of crash under certain conditions while executing bulk copy.
+ Crash in `handle_where_clause_restargets_right()`.
+ Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
+ Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
+ Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
+ Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
+ Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases. 
+ Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
+ Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
+ Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
+ Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.
+ Fixed an issue where some queries with ORDER BY clause did not use primary key indexes.
+ Fixed an issue with CREATE/ALTER PROCEDURE command that could cause server restart if procedure name contains special white characters.
+ Fixed an issue where query may return incorrect result when predicate involves SCOPE\_IDENTITY().

**Additional improvements and enhancements**
+ Fixed memory leak in decimal (numeric) conversion for BCP import.
+ Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
+ Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
+ Added restriction on dropping of Babelfish extensions for all users except admin role.
+ Prevent partial upgrades of Babelfish extensions.
+ sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
+ DDL scripting of indexes or constraints will now include correct ordering with columns.
+ Fixed an error to allow referencing a `#tmp table` in a nested procedure through OBJECT\_ID() clause.
+ Fixed an issue to avoid error when dropping trigger created on temp table.
+ Made an enhancement to allow table variables having a name longer than 63 characters.
+ Fixed issue with --schema-only and --data-only options of BabelfishDump utilities.
+ Fixed issue with BabelfishDump utility where it wasn't able to dump extended properties.
+ Fixed issue of fully qualified column reference doesn't work in PIVOT aggregate function.
+ Fixed an error to allow alter procedure from PG endpoint.
+ Blocked SET/RESET role statements execution from TDS endpoint.

### Babelfish for Aurora PostgreSQL 3.5
<a name="AuroraBabelfish.Updates.35X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.6. For more information about the improvements in Aurora PostgreSQL 15.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.5.4, July 30, 2025](#AuroraBabelfish.Updates.354)
+ [Aurora Babelfish release 3.5.3, February 02, 2025](#AuroraBabelfish.Updates.353)
+ [Aurora Babelfish release 3.5.2, October 7, 2024](#AuroraBabelfish.Updates.352)
+ [Aurora Babelfish release 3.5.1, June 20, 2024](#AuroraBabelfish.Updates.351)
+ [Aurora Babelfish release 3.5.0, April 29, 2024](#AuroraBabelfish.Updates.350)

#### Aurora Babelfish release 3.5.4, July 30, 2025
<a name="AuroraBabelfish.Updates.354"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 3.5.3, February 02, 2025
<a name="AuroraBabelfish.Updates.353"></a>

**High priority stability enhancements**
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 3.5.2, October 7, 2024
<a name="AuroraBabelfish.Updates.352"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.5.1, June 20, 2024
<a name="AuroraBabelfish.Updates.351"></a>

**High priority stability enhancements**
+ Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 3.5.0, April 29, 2024
<a name="AuroraBabelfish.Updates.350"></a>

**New features**
+ Babelfish introduces support for two spatial data types Geometry and Geography to store and manipulate spatial data under a limited scope. For more information, see [Babelfish supports Geospatial data types](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html).
+ Allowing `SELECT FOR JSON AUTO` support in Babelfish.
+ Support the ability to perform vector similarity search using the `pgvector` extension through Babelfish. The ability to use `HNSW` and `IVFLAT` indexes is also supported. For more information, see [Using pgvector in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html#babelfish-postgres-aws-extensions-using-pgvector).
+ Support the ability to access Amazon Machine Learning services such as Amazon Comprehend, Amazon Sagemaker and Amazon Bedrock through `aws_ml` extension. For more information, see [Using Amazon Aurora machine learning with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html#babelfish-postgres-aws-extensions-using-ml).
+ Support T-SQL procedure `sp_procedure_params_100_managed`.
+ Support creating Instead of Triggers (DML) on SQL Server Views.

**Critical stability enhancements**
+ Fixed an issue in Object Explorer Database enumeration with SSMS version 19.2.
+ Fixed an issue that caused error during Selecting data from variable `NVARCHAR(MAX)`, `VARCHAR(MAX)`, `VARBINARY(MAX)` with large length strings.
+ Fixed blank space padding related issue in char datatype for multibyte characters.
+ Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
+ Fixed default column collation to match server collation handled through `babelfishpg_tsql.server_collation_name` for some system views. List of fixed system views are `sys.check_constraints`, `sys.data_spaces`, `sys.default_constraints`, `sys.dm_exec_connections`, `sys.foreign_keys`, `sys.key_constraints`, `sys.stats`, `sys.syscolumns`, `sys.sysforeignkeys`, `sys.sysprocesses`, `sys.system_objects`, `sys.table_types`, `sys.tables`, `sys.types`, `sys.views` and `sys.xml_indexes`.
+ Restrict creation of functions/procedures with the same name in Babelfish.

**High priority stability enhancements**
+ Improved performance for system procedure `sp_tablecollations_100`.
+ Fixed an issue with major version upgrades where views contains cast from string literal to binary type.
+ Fixed a bug where parallel worker was unable to fetch the logical database name.
+ Fixed the performance issue of comparing `date` to `datetime`.

**Additional improvements and enhancements**
+ Fixed an issue on duplicate `object_id` in `sys.all_objects` after major version upgrade.
+ Fixed an issue in `CAST` functions for `Binary` to `Varchar` and `Rowversion` to `Varchar`.
+ Fixed an issue with insert into statement execution with table variable when table variable did not exist.
+ Fixed an issue where input hex string being converted to type binary did not have the correct data length.
+ Fixed an issue with mixed casing error in `sp_columns_100`.
+ Fixed a crash in Table Variable lookup after `TVP` execution via `TDS RPC SPExecuteSQL`.
+ Support embedded whitespace in multi-character comparison operators.
+ Support operators adjacent to `@@variables` without separating whitespace.
+ Fixed a crash with procedure execution if procedure deletes itself or rolls back the transaction which created the procedure.
+ Support for the `AS` keyword in `CREATE` function for all cases.
+ Support expressions in `SELECT...OFFSET...FETCH` clauses.
+ Support `SET TRANSACTION ISOLATION LEVEL` syntax.
+ Support floating-point notation without exponent.
+ Support comparison operators `!<` and `!>`.
+ Support for `DROP INDEX schema.table.index` and `DROP INDEX index ON schema.table` syntax.
+ Fixed issue in functions `parsename`, `session_context` and `sp_set_session_context` when using with non-default server collation.

### Babelfish for Aurora PostgreSQL 3.4
<a name="AuroraBabelfish.Updates.34X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.5. For more information about the improvements in Aurora PostgreSQL 15.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.4.4, August 4, 2025](#AuroraBabelfish.Updates.344)
+ [Aurora Babelfish release 3.4.3, February 5, 2025](#AuroraBabelfish.Updates.343)
+ [Aurora Babelfish release 3.4.2, September 17, 2024](#AuroraBabelfish.Updates.342)
+ [Aurora Babelfish release 3.4.1, June 24, 2024](#AuroraBabelfish.Updates.341)
+ [Aurora Babelfish release 3.4.0, December 21, 2023](#AuroraBabelfish.Updates.340)

#### Aurora Babelfish release 3.4.4, August 4, 2025
<a name="AuroraBabelfish.Updates.344"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 3.4.3, February 5, 2025
<a name="AuroraBabelfish.Updates.343"></a>

**High priority stability enhancements**
+ Fixed an issue for date functions to allow them to take into account the local/session timezone setting.

#### Aurora Babelfish release 3.4.2, September 17, 2024
<a name="AuroraBabelfish.Updates.342"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.4.1, June 24, 2024
<a name="AuroraBabelfish.Updates.341"></a>

**High priority stability enhancements**
+ Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 3.4.0, December 21, 2023
<a name="AuroraBabelfish.Updates.340"></a>

**New features**
+ Added support for TSQL Isolation Level SERIALIZABLE and REPEATABLE READ with PostgreSQL semantics. For more information, see [Transaction Isolation Levels in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-transaction.html).
+ Added support for enable or disable triggers.
+ Added support for TSQL functions DATETRUNC(), DATE\_BUCKET(), SWITCHOFFSET(), TODATETIMEOFFSET(), and AT TIME ZONE clause.
+ Added support for TSQL functions TYPE\_ID(), TYPE\_NAME(), COL\_LENGTH(), COL\_NAME().
+ Added support for DEFAULT keyword in calls to stored procedures and functions.
+ Added support for casting DATETIME to numeric types.
+ Added support for DBCC CHECKIDENT for ability to reset IDENTITY columns.
+ Added support for PRIMARY KEY NOT NULL IDENTITY clause in CREATE/ALTER TABLE.
+ Added support for double-quoted strings containing single-quote, embedded double quotes in a double-quoted string, and unquoted string parameters.
+ Added support for ALTER AUTHORIZATION syntax to change database owner.
+ Added support for TSQL KILL command.
+ Added support for TSQL Information\_schema.key\_column\_usage view.
+ Added support of variable as input for SET ROWCOUNT and SET DATEFIRST.
+ Added support for sys.server\_role members and sys.database\_permissions catalog views.
+ Added support for IDENTITY() function in a SELECT-INTO statement. In Babelfish, a column specified as IDENTITY will always be the last column in the new table. Due to this slight difference compared with SQL server, this feature needs to be used with an escape hatch babelfishpg\_tsql.escape\_hatch\_identity\_function. User-defined datatypes for IDENTITY() function are not currently supported.
+ Added support for ALTER USER...WITH LOGIN syntax.
+ Added support for change in transaction isolation from inside transaction block with well defined behavior.
+ Added support for casting datetime and smalldatetime to numeric types.
+ Added support for PIVOT in limited scope (not supported when used in a view definition, a common table expression, or a join).
+ Stored procedure sp\_changedbowner is supported.

**Security enhancements**
+ Fixed permission issue for view sys.server\_principals.

**Critical stability enhancements**
+ Fixed an issue where ISNULL function may return incorrect data type.
+ Fixed an issue where condition may be evaluated incorrectly for conditional statement like IF.
+ Fixed an error "database ... does not exist" that may be observed when parallel query is enforced.
+ Fixed handling of table variable or temp table when parallel worker is enforced.
+ Fixed unexpected error "lost connection to parallel worker" occurring when parallel worker is enforced.
+ Fixed an issue with multiple parentheses in SELECT columns.
+ Fixed an issue with handling of column name alias which may cause client to hang if column name alias contains string of length more than 64 bytes, for example, select col as '您对“数据一览“中的车型，颜色，内饰，选装, '.
+ Fixed datatype of information\_schema\_tsql.tables.TABLE\_TYPE column.
+ Fixed the error - “column ... does not exist” when using table.column with alias defined for table or schema\_name.table.column in set clause of update queries.
+ Fixed issue of incorrect schema resolution for multiple functions in query statement.
+ Fixed an issue for a few variants of DELETE with OUTPUT clause combined with table alias returns an error.
+ Fixed performance issue while expanding stored procedures in SSMS Object Explorer.
+ Fixed a crash when UNION with NULL values not cast to fixed-length types.
+ Fixed SESSION\_USER/SYSTEM\_USER in SET/PRINT/DECLARE variable assignment returning wrong result/error.
+ Fixed issue of blocking of UNIQUE constraint/index on nullable column not implemented consistently.
+ Fix a crash with T-SQL OPENQUERY() and four-part object name when T-SQL keywords are used as server name.
+ Fixed the issue of update with TOP, OUTPUT and join failing with error ‘unrecognized node type’.
+ Fixed the issue of VALUES clause with mixed types gives error containing the clause ‘Please use an explicit CAST or CONVERT’.
+ Fixed an issue of different assignments of identity values compared with SQL Server when ORDER BY is used with SELECT INTO statement.
+ Fix incorrect schema resolution where multiple functions are called in a single statement.

**High priority stability enhancements**
+ Fixed type conversion between varchar and binary datatype with use of proper encoding.
+ Fixed an issue where upper/lower case may not be preserved for column name aliases.
+ Fixed crash in queries involving money data-type in parallel query mode.
+ Fixed failure in MVU with non-default server collation name.
+ Fixed the issue of information\_schema vs. sys.objects WHERE type IN ('U', 'V') giving different result in Babelfish.
+ Fixed issue of sp\_columns and sp\_columns\_100 incorrectly show NULL radix for decimal columns.
+ Fixed issue in queries involving sys.format() function in parallel query mode returning error “cannot start subtransactions during a parallel operation”.
+ Fixed unexpected error “could not access file "pg\_hint\_plan": No such file or directory" while using pg\_hint\_plan in parallel query mode.
+ Fixed the issue of getting error ‘duplicate key value violates unique constraint ...' when re-creating the previously dropped view with the same name.

**Additional improvements and enhancements**
+ Improved performance for stored procedure sp\_describe\_undeclared\_parameters.
+ Fixed performance issue for DATEADD(), DATEDIFF().
+ SSMS - Fixed issue of stored procedure takes long time to load in Object Explorer.
+ SSMS - Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
+ Fixed performance issue after create/upgrade of Babelfish extension by running ANALYZE after Babelfish extension creation and upgrade.
+ Fixed the issue of index not used when query has an unnecessary cast to bigint.
+ Fixed an issue when stored procedures starting with (sp\_\*) are invoked with a dbo. or sys. prefix.
+ Fixed the issue with default\_schema\_name column of the catalog sys.babelfish\_authid\_user\_ext in case of "guest" user.
+ Fixed issue of orphan entries in sys.babelfish\_view\_def catalog table.
+ Fixed an issue with UNION and fixed-length types.
+ Fixed performance issue with '\+' operator in concatenation operation.
+ Fixed performance issue by optimizing use of internal function during index creation and usage in queries.
+ Fixed an issue when comparing BIT and VARCHAR types.
+ Performance improvements for create/drop database with large number of databases.
+ Added sort operators for Babelfish datatypes, so that MAX/MIN aggregation on index column can have a query plan candidate of LIMIT 1 and index scan.
+ Fixed nulls order of Babelfish indexes, so that TOP 1 clause on index column can have a query plan candidate of LIMIT 1 and index scan.
+ Fixed a crash with SSMS in Table properties dialog box while clicking on Permissions page.
+ Restricted use of view as a target with OUTPUT INTO clause.

### Babelfish for Aurora PostgreSQL 3.3
<a name="AuroraBabelfish.Updates.33X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.4. For more information about the improvements in Aurora PostgreSQL 15.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.3.1, November 14, 2024](#AuroraBabelfish.Updates.331)
+ [Aurora Babelfish release 3.3.0, October 24, 2023](#AuroraBabelfish.Updates.330)

#### Aurora Babelfish release 3.3.1, November 14, 2024
<a name="AuroraBabelfish.Updates.331"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.3.0, October 24, 2023
<a name="AuroraBabelfish.Updates.330"></a>

**New features**
+ Added support for TSQL functions `HOST_ID()`, `EOMONTH()`, `PARSENAME()` and `SMALLDATETIMEFROMPARTS()` are supported.
+ `sys.extended_properties` system catalog view is supported.
+ Stored procedures `sp_enum_oledb_providers`, `sp_testlinkedserver`, and `sp_who` are supported.
+ Added support for the T-SQL square bracket syntax with the LIKE predicate.
+ Added support for `pg_stat_statements` extension with Babelfish. For more information, see [pg\_stat\_statements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html).
+ Added support for CREATE or ALTER or DROP EXTENSION statements in `sp_execute_postgresql` procedure. For more information, see [sp\_execute\_postgresql](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.Babelfish.Functions.html).
+ Added support for extended properties for object types database, schema, table, view, column, sequence, function, procedure: `sys.extended_properties` system catalog view, stored procedures `sp_addextendedproperty`, `sp_updateextendedproperty`, `sp_dropextendedproperty`, and system function `fn_listextendedproperty()`.

**Critical stability enhancements**
+ T-SQL trigger can't be performed when function, procedure or trigger of PostgreSQL is in execution stack. If you try to do, the following error message will appear: `T-SQL trigger can not be executed from PostgreSQL function, procedure or trigger.`

**High priority stability enhancements**
+ Fixed the issue of GETDATE() incorrectly returning different values in the same query.
+ Fixed the issue of GETUTCDATE() incorrectly returning time of transaction instead of time of query.

**Additional improvements and enhancements**
+ Fixed an issue where SSMS generate script for multiple views, or combining a view with other objects throws an error.
+ Fixed an issue to avoid system crash while formatting `datetime` values in the results of FOR JSON or FOR XML. 
+ Fixed an issue to avoid system crash during table variable cleanup after a runtime error.
+ Fixed an issue to avoid system crash when using certain values in nested function calls.
+ Fixed an invalid memory access issue while freeing `PLTSQL` functions.
+ Fixed a crash in `SqlBulkCopy` when the order of columns is different from the table where it is defined.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed crash in parallel query when `enable_pg_hint` is turned on.
+ Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
+ Fixed issue where `sp_describe_first_result_set` procedure can return incorrect column order, which could cause BCP to work incorrectly.
+ Fixed issue related to loss of decimal digits when converting from REAL to DECIMAL.
+ Fixed error handling during the Babelfish upgrade process. Babelfish throws an error if there is a failure during the upgrade.
+ Fixed an issue with sender of XML data type to handle `NULL` value where it was causing client to hang.
+ Fixed an issue where USE database statement was incorrectly allowed inside the procedure, function or trigger definition.
+ Fixed crash while calling T-SQL procedure from PG port when querying `sys.sysobjects`.
+ Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY() and remote object references with a four-part object names are invoked within the master database.
+ Added support for `connect_timeout` option in `sp_serveroption`.
+ Fixed a recreation issue with indexed temp tables. You can now create indexed temp tables in Babelfish.
+ Fixed an issue with identity columns in procedures.
+ Fixed an issue where some catalog entries were not being cleared after use with temp tables, causing occasional error messages. 
+ Fixed an issue with Babelfish TOP clause that accept number without parenthesis. 
+ Fixed performance problem for create index or scan index.
+ Fixed an issue when using like expression in join on condition failed with nondeterministic error.

### Babelfish for Aurora PostgreSQL 3.2
<a name="AuroraBabelfish.Updates.32X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.3. For more information about the improvements in Aurora PostgreSQL 15.3, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.2.2, November 12, 2024](#AuroraBabelfish.Updates.322)
+ [Aurora Babelfish release 3.2.1, October 4, 2023](#AuroraBabelfish.Updates.321)
+ [Aurora Babelfish release 3.2.0, July 13, 2023](#AuroraBabelfish.Updates.320)

#### Aurora Babelfish release 3.2.2, November 12, 2024
<a name="AuroraBabelfish.Updates.322"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.2.1, October 4, 2023
<a name="AuroraBabelfish.Updates.321"></a>

**High priority stability enhancements**
+ Fixed an issue causing crash when cursor referencing a table variable is already dropped.
+ Fixed an issue where queries with UNION ALL, ORDER BY, and multiple joins could cause unavailability.
+ Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.
+ Fixed an invalid memory access while freeing `PLTSQL` functions.

**Additional improvements and enhancements**
+ Fixed an issue to avoid crash by properly handling formatting of datetime values in the results of FOR JSON or FOR XML.
+ Fixed a crash in `SqlBulkCopy` when the order of columns is different compared to table defining.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
+ Fixed a crash when dropping temp table or table variables during cleanup.
+ Fixed an issue with sender of XML data type to handle NULL value where it was causing client to hang.
+ Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY() and remote object referenced with a four-part object names are invoked within the master database.
+ Fixed an issue to avoid failure error message 2600 while attempting to create a temp table.
+ Fixed a bug to prevent temp table index recreation issue.

#### Aurora Babelfish release 3.2.0, July 13, 2023
<a name="AuroraBabelfish.Updates.320"></a>

**New features**
+ Supports TIMEFROMPARTS(), DATETIME2FROMPARTS(), ROWCOUNT\_BIG(), DATABASE\_PRINCIPAL\_ID() and CONTEXT\_INFO() T-SQL functions.
+ Supports STDEV(), STDEVP(), VAR(), VARP() statistical T-SQL aggregates.
+ Supports sp\_rename for COLUMN , TRIGGER, TABLE TYPE and USER DEFINED DATATYPE objects.
+ Supports Babelfish instance as a linked server from SQL server instance. For more information, see [Babelfish supports linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-linkedservers.html).
+ Supports 4 parts object name references for remote objects for select queries. For more information, see [Babelfish supports linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-linkedservers.html).
+ Supports TOP clause for INSERT SELECT statement.
+ Supports SET rowcount and SET CONTEXT\_INFO T-SQL syntax.

**Security enhancements**
+ Fixed an issue that non-sysadmin logins could DROP or ALTER logins.

**Critical stability enhancements**
+ Fixed an issue when table variables may cause orphaned metadata entries.
+ Fixed the issue that CTE top order handles null first behavior incorrectly.

**High priority stability enhancements**
+ Fixed intermittent issue with concurrent SSL connections to Babelfish server.
+ Fixed an issue in column name resolution of ORDER BY clause over UNION ALL query.
+ Fixed the Unrecognized object issue when dropping database.
+ Fixed the crash issue when adding non string unique key.
+ User defined scalar functions were created as VOLATILE by default. This fix changes the behavior such that user defined scalar functions which do not perform any DML or DDL are created as STABLE by default.
+ Fixed issues in column name resolution logic for UPDATE and DELETE statements with TOP clause.

**Additional improvements and enhancements**
+ Fixed an issue with sp\_helpdb where NULL is shown for compatbility\_level.
+ Fixed a memory management issue with update\_DropRoleStmt.
+ Fixed table variables to make it immune to transaction rollback.
+ The fix corrects the behavior of ‘select convert(nvarchar(10),Getdate(),105)’ for nvarchar datatype.
+ Fixed an issue to allow UPDATE and DELETE for Table Variables inside functions.
+ Made enhancement to improve the performance and avoid catalog bloat while using table variables.
+ Fixed an issue in @@NEXTLEVEL which returned 1 unit larger than expected.
+ Fixed an issue in sp\_helpdb where input parameter’s case sensitivity is not handled properly.
+ Fixed an issue that COMMIT, ROLLBACK,EXECUTE, PRINT, SAVE and RAISERROR could be used in CREATE FUNCTION statement.
+ Supports query timeout in sp\_serveroption for OPENQUERY. For more information, see [Babelfish supports linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-linkedservers.html).
+ Fixed the case sensitivity issue in the CREATE USER for windows login.
+ Fixed an issue with detecting invalid login name in CREATE LOGIN WITH WINDOWS statement.
+ Fixed an issue to support INT values in JSON\_MODIFY() function.
+ Fixed an issue in JSON\_MODIFY() function to support new value parameters as JSON\_QUERY, SELECT FOR JSON, or JSON MODIFY.
+ Fixed an issue in babelfishpg\_tds.product\_version.
+ Fixed an issue in datetimeoffset operations.
+ Fixed an issue for datetimeoffset default values.
+ Supports numeric expressions representing datetime values.
+ Fixed an issue in sys.database\_principals view where the users sys and information\_schema, as well as the database role public are not shown.
+ Old-style T-SQL catalogs, with names starting with 'sys' (like sysprocesses) were available only in the 'sys' schema, but are now also available in the 'dbo' schema.
+ Fixed an issue where a T-SQL view could be created on top of a temporary table.
+ Fixed an issue that DATETIME2 doesn’t accept 7 as scale argument.

### Babelfish for Aurora PostgreSQL 3.1 (Deprecated)
<a name="AuroraBabelfish.Updates.31X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.2. For more information about the improvements in Aurora PostgreSQL 15.2, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 3.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 3.1.4, November 6, 2024](#AuroraBabelfish.Updates.314)
+ [Aurora Babelfish release 3.1.3, October 4, 2023](#AuroraBabelfish.Updates.313)
+ [Aurora Babelfish release 3.1.2, July 24, 2023](#AuroraBabelfish.Updates.312)
+ [Aurora Babelfish release 3.1.1, May 10, 2023](#AuroraBabelfish.Updates.311)
+ [Aurora Babelfish release 3.1.0, April 5, 2023](#AuroraBabelfish.Updates.310)

#### Aurora Babelfish release 3.1.4, November 6, 2024
<a name="AuroraBabelfish.Updates.314"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.1.3, October 4, 2023
<a name="AuroraBabelfish.Updates.313"></a>

**Additional improvements and enhancements**
+ Fixed a memory management issue with `update_DropRoleStmt`.
+ Fixed a crash in `SqlBulkCopy` with heap\_compute\_data\_size function in stacktrace when the order of columns is different compared to table defining.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY() and remote object referenced with a four-part object names are invoked within the master database.
+ Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.

#### Aurora Babelfish release 3.1.2, July 24, 2023
<a name="AuroraBabelfish.Updates.312"></a>

**Additional improvements and enhancements**
+ Fixed intermittent SSL connectivity issue during concurrent connections towards Babelfish instance.
+ Fixed login name case sensitivity issue with CREATE USER for windows login syntax.

#### Aurora Babelfish release 3.1.1, May 10, 2023
<a name="AuroraBabelfish.Updates.311"></a>

**Additional improvements and enhancements**
+ Fixed an issue to prevent error when sequences are created in a database other than 'master'.
+ Fixed a crash during bulk load operation in a specific scenario.
+ Fixed an issue to prevent Babelfish instance from crashing when alter table and alter column is called with drop default where the column has no definition.

#### Aurora Babelfish release 3.1.0, April 5, 2023
<a name="AuroraBabelfish.Updates.310"></a>

**New features**
+ Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 14.6 and 14.7 to Aurora PostgreSQL 15.2. For more information on the major version upgrade, see [Upgrading your Babelfish cluster to a new version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading.html#babelfish-information-upgrading-major).
+ Support for the following functions: STR, APP\_NAME, OBJECT\_DEFINITION, OBJECT\_SCHEMA\_NAME, ATN2, DATEDIFF\_BIG functions.
+ Support for the following INFORMATION\_SCHEMA views: sequences, routines and schemata.
+ Support sp\_rename for TABLE, VIEW, PROCEDURE, FUNCTION, SEQUENCE.
+ Support sys.systypes system compatibility view.
+ Support for a new GUC parameter called babelfishpg\_tds.product\_version that allows you to set SQL Server product version number that is returned as an output by Babelfish. For more information, see [Using Babelfish product version GUC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-guc-version). 
+ Added support to generate data definition scripts for various objects present in a Babelfish for Aurora PostgreSQL database. For more information, see [DDL exports supported by Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-query-database.html#babelfish-ddl-exports).
+ Babelfish now supports Aurora PostgreSQL database authentication with Kerberos using AWS Directory Service for Microsoft Managed Active Directory. With this feature, for authentication you can use Microsoft Windows Authentication when you connect to your Babelfish database. For more information, see [Database authentication with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-db-authentication.html).
+ Babelfish now supports linked servers from your Aurora PostgreSQL database by using the tds\_fdw (TDS Foreign Data Wrapper) APG extension. Only the OPENQUERY function that executes the specified pass-through query on the specified linked server is currently supported. For more information, see [Babelfish supports linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-linkedservers.html).

**Security enhancements**
+ Fixed buffer overflow due to out of bound array access.

**High priority stability enhancements**
+ Improved the performance through benefiting interactive queries, ODBC-based applications and tools such as SQL Server Management Studio. Following enhancements has been made for the same:
  + Fixed performance issues in several system functions including OBJECT\_ID(), OBJECT\_NAME(), SCHEMA\_ID().
  + Fixed performance issues in system stored procedures sp\_sproc\_columns and sp\_fkeys.
  + Fixed performance issues in system catalog views sys.all\_views, sys.objects and sys.types.
  + Improved the performance of bulk load, parsing of T-SQL and prepared statements.
+ Added a new system stored procedure sp\_babelfish\_volatility that you can use to set the volatility of user-defined functions to improve index use when the functions are used as part of query predicates.
+ Fixed an issue where the UPDATE FROM or DELETE FROM statement that references the correlation name of the updated table raised an error.
+ Fixed an issue where scope\_identity function returns wrong result after exiting one scope.
+ Fixed an issue where name resolution doesn't work as expected when commands are invoked from the .NET client framework.
+ Fixed an issue where any index defined on column having binary/varbinary data types are not considered by the query optimizer for equality predicates.

**Additional improvements and enhancements**
+ Fixed an issue where the statement timeout parameter for a session was not working as expected.
+  Supports sequence creations using user-defined data types. 
+ Fixed an issue where unicode in column names, aliases or comments causes parsing errors.
+ Fixed an issue where scope\_identity function requires higher permission than actually needed.
+ Support for the following stored procedures for working with linked servers: sp\_addlinkedserver, sp\_dropserver, sp\_linkedservers, sp\_addlinkedsrvlogin, sp\_droplinkedsrvlogin, sp\_helplinkedsrvlogin.
+ Support for NEXT VALUE FOR function that gets the next value of a sequence. Note that this function cannot be used in some control-of-flow statements. OVER clause is also not supported.
+ Fixed a crash when handling certain errors with sp\_describe\_undeclared\_parameters.
+ Fixed a rare error during Babelfish extension creation.
+ Fixed an issue which was throwing an error "typename is NULL" while using TVP in sp\_executesql.
+ Fixed SELECT FOR XML/JSON behavior to not raise error when using SELECT with correlation name in subquery using FOR XML PATH clause.
+ Fixed an issue with the SELECT FOR JSON or a SELECT FOR XML query which didn't return correct results for an empty table.
+ Fixed an issue where the guest user can create objects in the wrong schema.
+ Fixed schema name resolution for user defined types for param types in system stored procedures.
+ Fixed an issue where applications issuing queries with more than 100 bind parameters for prepared statements were failing. This limit is now increased to 2100 to match the limits used by SQL Server.
+ Fixed an issue with case handling of variable names in the sp\_executesql call.
+ sp\_fkeys stored procedure now also returns 'deferrability' column in the result set.
+ Fixed an issue in AVG aggregates which led to the termination of the connection for some integer datatypes.
+ The index\_id and indid column for respective views now returns the same value for indexes belonging to same object and the index\_id is unique only within the object.
+ Fixed an issue to not throw an error when OpenJson is called in stored procedures using nvarchar or join.
+ Fixed an issue to not throw an error while using try\_convert and try\_cast for prohibited conversions involving some integer literals.
+ Fixed an issue to allow OPENJSON WITH clause to accept a table alias.
+ Support Degrees, Radians and Power functions returning the proper type.
+ Fixed an issue where membership handling for sysadmin is not handled correctly.
+ Fixed the default output style when converting DATE/TIME types to VARCHAR type using CONVERT function.
+ Support EXECUTE AS CALLER clause in CREATE PROC/FUNCTION/TRIGGER.
+ Fixed an issue where configurations are not reverted after existing sp\_executesql scope.
+ Fixed issues with handling cross-database access for the sys.has\_perms\_by\_name function.
+ Support the ProductLevel and ProductUpdateLevel properties for the SERVERPROPERTY function. ProductUpdateLevel always returns NULL and ProductLevel tracks the Babelfish version number closely with the T-SQL definition.
+ Fixed an issue where the table variable when used as a bind parameter from client application resulted in an error.

## Babelfish for Aurora PostgreSQL 2.x versions (includes some deprecated versions)
<a name="aurorababelfish-versions-version2x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 2.17](#AuroraBabelfish.Updates.217X)
+ [Babelfish for Aurora PostgreSQL 2.16](#AuroraBabelfish.Updates.216X)
+ [Babelfish for Aurora PostgreSQL 2.14](#AuroraBabelfish.Updates.214X)
+ [Babelfish for Aurora PostgreSQL 2.13](#AuroraBabelfish.Updates.213X)
+ [Babelfish for Aurora PostgreSQL 2.12](#AuroraBabelfish.Updates.212X)
+ [Babelfish for Aurora PostgreSQL 2.11](#AuroraBabelfish.Updates.211X)
+ [Babelfish for Aurora PostgreSQL 2.10](#AuroraBabelfish.Updates.210X)
+ [Babelfish for Aurora PostgreSQL 2.9](#AuroraBabelfish.Updates.29X)
+ [Babelfish for Aurora PostgreSQL 2.8](#AuroraBabelfish.Updates.28X)
+ [Babelfish for Aurora PostgreSQL 2.7 (Deprecated)](#AuroraBabelfish.Updates.27X)
+ [Babelfish for Aurora PostgreSQL 2.6](#AuroraBabelfish.Updates.26X)
+ [Babelfish for Aurora PostgreSQL 2.5 (Deprecated)](#AuroraBabelfish.Updates.25X)
+ [Babelfish for Aurora PostgreSQL 2.4 (Deprecated)](#AuroraBabelfish.Updates.24X)
+ [Babelfish for Aurora PostgreSQL 2.3 (Deprecated)](#AuroraBabelfish.Updates.23X)
+ [Babelfish for Aurora PostgreSQL 2.2](#AuroraBabelfish.Updates.22X)
+ [Babelfish for Aurora PostgreSQL 2.1](#AuroraBabelfish.Updates.21X)

### Babelfish for Aurora PostgreSQL 2.17
<a name="AuroraBabelfish.Updates.217X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.23. For more information about the improvements in Aurora PostgreSQL 14.23, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.17 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 2.17.0, August 21, 2026
<a name="AuroraBabelfish.Updates.2170"></a>

**Critical enhancements**
+ Fixed an issue that could cause crash in SPI\_finish after Out Of Memory error.

### Babelfish for Aurora PostgreSQL 2.16
<a name="AuroraBabelfish.Updates.216X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.22. For more information about the improvements in Aurora PostgreSQL 14.22, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

#### Aurora Babelfish release 2.16.0, April 6, 2026
<a name="AuroraBabelfish.Updates.2160"></a>

**Critical enhancements**
+ Fixed an issue where update with output clause may skip rows during concurrent updates.

### Babelfish for Aurora PostgreSQL 2.14
<a name="AuroraBabelfish.Updates.214X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.19. For more information about the improvements in Aurora PostgreSQL 14.19, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.14 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.14.0, November 25, 2025](#AuroraBabelfish.Updates.2140)

#### Aurora Babelfish release 2.14.0, November 25, 2025
<a name="AuroraBabelfish.Updates.2140"></a>

**Critical enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations

**Additional improvements and enhancements**
+ Fixed an issue while adding a column with default value which resulted in an error

### Babelfish for Aurora PostgreSQL 2.13
<a name="AuroraBabelfish.Updates.213X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.18. For more information about the improvements in Aurora PostgreSQL 14.18, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.13 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.13.1, August 08, 2025](#AuroraBabelfish.Updates.2131)

#### Aurora Babelfish release 2.13.1, August 08, 2025
<a name="AuroraBabelfish.Updates.2131"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

### Babelfish for Aurora PostgreSQL 2.12
<a name="AuroraBabelfish.Updates.212X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.17. For more information about the improvements in Aurora PostgreSQL 14.17, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.12 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.12.2, October 09, 2025](#AuroraBabelfish.Updates.2122)
+ [**Aurora Babelfish release 2.12.1, June 03, 2025**](#AuroraBabelfish.Updates.2121)
+ [Aurora Babelfish release 2.12, April 08, 2025](#AuroraBabelfish.Updates.212)

#### Aurora Babelfish release 2.12.2, October 09, 2025
<a name="AuroraBabelfish.Updates.2122"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

#### **Aurora Babelfish release 2.12.1, June 03, 2025**
<a name="AuroraBabelfish.Updates.2121"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.12, April 08, 2025
<a name="AuroraBabelfish.Updates.212"></a>

**Critical enhancements**
+ Added Cleanup of stale parameters and configs in case of connection pooling.
+ Added comprehensive cursor state cleanup to avoid stale data in case of connection pooling.
+ Fixed a issue with `IDENTITY` columns not being recognized during `DML` statements using `OUTPUT` and `WHERE`.

**High priority stability enhancements**
+ Fix behavior of queries which use `sys.Db_id()` function which returned empty rows in enforced parallel mode.

### Babelfish for Aurora PostgreSQL 2.11
<a name="AuroraBabelfish.Updates.211X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.15. For more information about the improvements in Aurora PostgreSQL 14.15, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.11 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.11.3, November 13, 2025](#AuroraBabelfish.Updates.2113)
+ [Aurora Babelfish release 2.11.2, June 24, 2025](#AuroraBabelfish.Updates.2112)
+ [Aurora Babelfish release 2.11.1, January 20, 2025](#AuroraBabelfish.Updates.2111)
+ [Aurora Babelfish release 2.11.0, December 27, 2024](#AuroraBabelfish.Updates.2110)

#### Aurora Babelfish release 2.11.3, November 13, 2025
<a name="AuroraBabelfish.Updates.2113"></a>

**Critical stability enhancements**
+ Fixed an issue during TDS Reset Connection in certain situations.

#### Aurora Babelfish release 2.11.2, June 24, 2025
<a name="AuroraBabelfish.Updates.2112"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.11.1, January 20, 2025
<a name="AuroraBabelfish.Updates.2111"></a>

**High priority stability enhancements**.
+ Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 2.11.0, December 27, 2024
<a name="AuroraBabelfish.Updates.2110"></a>

***New features***
+ Enabled support of `sys.sp_reset_connection stored` proc to reset connection.

***Additional improvements and enhancements***
+ Fixed an issue with `ISNUMERIC` function to return correct result for nvarchar/varchar parameters.
+ Fixed an issue to rethrow correct TSQL error code.

### Babelfish for Aurora PostgreSQL 2.10
<a name="AuroraBabelfish.Updates.210X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.13. For more information about the improvements in Aurora PostgreSQL 14.13, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.10 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.10.2, July 11, 2025](#AuroraBabelfish.Updates.2102)
+ [Aurora Babelfish release 2.10.0, September 30, 2024](#AuroraBabelfish.Updates.2100)

#### Aurora Babelfish release 2.10.2, July 11, 2025
<a name="AuroraBabelfish.Updates.2102"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.10.0, September 30, 2024
<a name="AuroraBabelfish.Updates.2100"></a>

**Security enhancements**
+ Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
+ Fixed an issue with `sys.database_principals` view where it was showing metadata related to all the users irrespective of privileges of server principal.

**High Priority stability enhancements**
+ Fixed an issue with `information_schema.tables` returning incorrect table\_name.
+ Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is installed.

**Additional improvements and enhancements**
+ Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
+ Fixed an issue when comment comes with the column name.

### Babelfish for Aurora PostgreSQL 2.9
<a name="AuroraBabelfish.Updates.29X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.12. For more information about the improvements in Aurora PostgreSQL 14.12, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.9 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.9.3, July 17, 2025](#AuroraBabelfish.Updates.293)
+ [Aurora Babelfish release 2.9.1, September 27, 2024](#AuroraBabelfish.Updates.291)
+ [Aurora Babelfish release 2.9.0, August 8, 2024](#AuroraBabelfish.Updates.290)

#### Aurora Babelfish release 2.9.3, July 17, 2025
<a name="AuroraBabelfish.Updates.293"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.9.1, September 27, 2024
<a name="AuroraBabelfish.Updates.291"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.9.0, August 8, 2024
<a name="AuroraBabelfish.Updates.290"></a>

**Critical stability enhancements**
+ Fixed issue producing syntax error with delimited column alias without preceding whitespace.
+ Creating a user for a login is blocked when its login is already a member of sysadmin.
+ Fixed the column type of the T-SQL views to use nvarchar(max).
+ Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.

**High priority stability enhancements**
+ Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
+ Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
+ Fixed issue of crash under certain conditions while executing bulk copy.
+ Crash in `handle_where_clause_restargets_right()`.
+ Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
+ Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
+ Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
+ Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
+ Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases. 
+ Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
+ Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
+ Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
+ Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.

**Additional improvements and enhancements**
+ Fixed memory leak in decimal (numeric) conversion for BCP import.
+ Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
+ Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
+ Added restriction on dropping of Babelfish extensions for all users except admin role.
+ Prevent partial upgrades of Babelfish extensions.
+ sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
+ DDL scripting of indexes or constraints will now include correct ordering with columns.

### Babelfish for Aurora PostgreSQL 2.8
<a name="AuroraBabelfish.Updates.28X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.11. For more information about the improvements in Aurora PostgreSQL 14.11, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.8 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.8.4, July 30, 2025](#AuroraBabelfish.Updates.284)
+ [Aurora Babelfish release 2.8.2, October 7, 2024](#AuroraBabelfish.Updates.282)
+ [Aurora Babelfish release 2.8.0, April 29, 2024](#AuroraBabelfish.Updates.280)

#### Aurora Babelfish release 2.8.4, July 30, 2025
<a name="AuroraBabelfish.Updates.284"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.8.2, October 7, 2024
<a name="AuroraBabelfish.Updates.282"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.8.0, April 29, 2024
<a name="AuroraBabelfish.Updates.280"></a>

**Critical stability enhancements**
+ Fixed an issue in Object Explorer Database enumeration with SSMS version 19.2.
+ Fixed an issue that caused error during Selecting data from variable `NVARCHAR(MAX)`, `VARCHAR(MAX)`, `VARBINARY(MAX)` with large length strings.
+ Fixed blank space padding related issue in char datatype for multibyte characters.
+ Fixed performance issue of enumerating tables and views in SSMS Object Explorer.

**High priority stability enhancements**
+ Improved performance for system procedure `sp_tablecollations_100`.
+ Fixed an issue with major version upgrades where views contains cast from string literal to binary type.
+ Fixed a bug where parallel worker was unable to fetch the logical database name.
+ Fixed the performance issue of comparing `date` to `datetime`.

**Additional improvements and enhancements**
+ Fixed an issue on duplicate `object_id` in `sys.all_objects` after major version upgrade.
+ Fixed an issue in `CAST` functions for `Binary` to `Varchar` and `Rowversion` to `Varchar`.
+ Fixed an issue with insert into statement execution with table variable when table variable did not exist.
+ Fixed an issue where input hex string being converted to type binary did not have the correct data length.
+ Fixed an issue with mixed casing error in `sp_columns_100`.
+ Fixed a crash in Table Variable lookup after `TVP` execution via `TDS RPC SPExecuteSQL`.
+ Fixed Babelfish view definition table index to have correct collation when upgrading from 14.5 to 14.11.

### Babelfish for Aurora PostgreSQL 2.7 (Deprecated)
<a name="AuroraBabelfish.Updates.27X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.10. For more information about the improvements in Aurora PostgreSQL 14.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.7 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.7.4, August 4, 2025](#AuroraBabelfish.Updates.274)
+ [Aurora Babelfish release 2.7.2, September 17, 2024](#AuroraBabelfish.Updates.272)
+ [Aurora Babelfish release 2.7.0, December 21, 2023](#AuroraBabelfish.Updates.270)

#### Aurora Babelfish release 2.7.4, August 4, 2025
<a name="AuroraBabelfish.Updates.274"></a>

**Security enhancements**
+ Fixed an issue with permission check in parallel worker where non-privileged user may get read access to data in some scenarios.

#### Aurora Babelfish release 2.7.2, September 17, 2024
<a name="AuroraBabelfish.Updates.272"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.7.0, December 21, 2023
<a name="AuroraBabelfish.Updates.270"></a>

**Security enhancements**
+ Fixed permission issue for view sys.server\_principals.

**Critical stability enhancements**
+ Fixed an issue where ISNULL function may return incorrect data type.
+ Fixed an issue where condition may be evaluated incorrectly for conditional statement like IF.
+ Fixed an error "database ... does not exist" that may be observed when parallel query is enforced.
+ Fixed handling of table variable or temp table when Parallel worker is enforced.
+ Fixed unexpected error "lost connection to parallel worker" occurring when parallel worker is enforced.
+ Fixed an issue with multiple parentheses in SELECT columns.
+ Fixed an issue with handling of column name alias which may cause client to hang if column name alias contains string of length more than 64 bytes, for example, select col as '您对“数据一览“中的车型，颜色，内饰，选装, '.
+ Fixed datatype of information\_schema\_tsql.tables.TABLE\_TYPE column.
+ Fixed the error - “column ... does not exist” when using table.column with alias defined for table or schema\_name.table.column in set clause of update queries.
+ Fixed issue of incorrect schema resolution for multiple functions in query statement.

**High priority stability enhancements**
+ Fixed type conversion between varchar and binary datatype with use of proper encoding.
+ Fixed an issue where upper/lower case may not be preserved for column name aliases.
+ Fixed crash in queries involving money data-type in parallel query mode.
+ Fixed failure in MVU with non-default server collation name.
+ Fixed the issue of information\_schema vs. sys.objects WHERE type IN ('U', 'V') giving different result in Babelfish.
+ Fixed issue of sp\_columns and sp\_columns\_100 incorrectly show NULL radix for decimal columns.
+ Fixed issue in queries involving sys.format() function in parallel query mode returning error “cannot start subtransactions during a parallel operation”.
+ Fixed unexpected error “could not access file "pg\_hint\_plan": No such file or directory" while using pg\_hint\_plan in parallel query mode.
+ Fixed the issue of getting error ‘duplicate key value violates unique constraint ...' when re-creating a previously dropped view with the same name.

**Additional improvements and enhancements**
+ Improved performance for stored procedure sp\_describe\_undeclared\_parameters.
+ Fixed performance issue for DATEADD(), DATEDIFF().
+ SSMS - Fixed issue of stored procedure takes long time to load in Object Explorer.
+ SSMS - Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
+ Fixed performance issue after create/upgrade of Babelfish extension by running ANALYZE after Babelfish extension creation and upgrade.
+ Fixed the issue of index not used when query has an unnecessary cast to bigint.
+ Fixed an issue when stored procedures starting with (sp\_\*) are invoked with a dbo. or sys. prefix.
+ Fixed the issue with default\_schema\_name column of the catalog sys.babelfish\_authid\_user\_ext in case of "guest" user.
+ Fixed issue of orphan entries in sys.babelfish\_view\_def catalog table.

### Babelfish for Aurora PostgreSQL 2.6
<a name="AuroraBabelfish.Updates.26X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.9. For more information about the improvements in Aurora PostgreSQL 14.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.6.1, November 14, 2024](#AuroraBabelfish.Updates.261)
+ [Aurora Babelfish release 2.6.0, October 24, 2023](#AuroraBabelfish.Updates.260)

#### Aurora Babelfish release 2.6.1, November 14, 2024
<a name="AuroraBabelfish.Updates.261"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.6.0, October 24, 2023
<a name="AuroraBabelfish.Updates.260"></a>

**New features**
+ Added support for TSQL function SMALLDATETIMEFROMPARTS().

**Critical stability enhancements**
+ T-SQL trigger can't be executed when function, procedure or trigger of PostgreSQL is in execution stack.

**High priority stability enhancements**
+ Fixed the issue of GETDATE() incorrectly returning different values in the same query.
+ Fixed the issue of GETUTCDATE() incorrectly returning time of transaction instead of time of query.

**Additional improvements and enhancements**
+ Fixed an issue where SSMS generate script for multiple views, or combining a view with other objects throws an error.
+ Fixed an issue to avoid system crash while formatting `datetime` values in the results of FOR JSON or FOR XML. 
+ Fixed an issue to avoid system crash during table variable cleanup after a runtime error.
+ Fixed an issue to avoid system crash when using certain values in nested function calls.
+ Fixed an invalid memory access issue while freeing `PLTSQL` functions.
+ Fixed a crash in `SqlBulkCopy` when the order of columns is different from the table where it is defined.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed crash in parallel query when `enable_pg_hint` is turned on.
+ Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
+ Fixed issue where `sp_describe_first_result_set` procedure can return incorrect column order, which could cause BCP to work incorrectly.
+ Fixed issue related to loss of decimal digits when converting from REAL to DECIMAL.
+ Fixed error handling during the Babelfish upgrade process. Babelfish throws an error if there is a failure during the upgrade.
+ Fixed an issue with sender of XML data type to handle `NULL` value where it was causing client to hang.
+ Fixed an issue where USE database statement was incorrectly allowed inside the procedure, function or trigger definition.
+ Fixed crash while calling T-SQL procedure from PG port when querying `sys.sysobjects`.

### Babelfish for Aurora PostgreSQL 2.5 (Deprecated)
<a name="AuroraBabelfish.Updates.25X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.8. For more information about the improvements in Aurora PostgreSQL 14.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.5.2, November 12, 2024](#AuroraBabelfish.Updates.252)
+ [Aurora Babelfish release 2.5.1, October 4, 2023](#AuroraBabelfish.Updates.251)
+ [Aurora Babelfish release 2.5.0, July 13, 2023](#AuroraBabelfish.Updates.250)

#### Aurora Babelfish release 2.5.2, November 12, 2024
<a name="AuroraBabelfish.Updates.252"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.5.1, October 4, 2023
<a name="AuroraBabelfish.Updates.251"></a>

**High priority stability enhancements**
+ Fixed an issue causing crash when cursor referencing a table variable is already dropped.
+ Fixed an issue where queries with UNION ALL, ORDER BY, and multiple joins could cause unavailability.
+ Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.
+ Fixed an invalid memory access while freeing `PLTSQL` functions.

**Additional improvements and enhancements**
+ Fixed an issue to avoid crash by properly handling formatting of datetime values in the results of FOR JSON or FOR XML.
+ Fixed a crash in `SqlBulkCopy` when the order of columns is different compared to table defining.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
+ Fixed a crash when dropping temp table or table variables during cleanup.
+ Fixed an issue with sender of XML data type to handle NULL value where it was causing client to hang.

#### Aurora Babelfish release 2.5.0, July 13, 2023
<a name="AuroraBabelfish.Updates.250"></a>

**Security enhancements**
+ Fixed an issue that non-sysadmin logins could DROP or ALTER logins.

**Critical stability enhancements**
+ Fixed an issue when table variables may cause orphaned metadata entries.
+ Fixed the issue where CTE top order handles null first behavior incorrectly.

**High priority stability enhancements**
+ Fixed intermittent issue with concurrent SSL connections to Babelfish server.
+ Fixed an issue in column name resolution of ORDER BY clause over UNION ALL query.
+ Fixed the Unrecognized object issue when dropping database.
+ Fixed the crash issue when adding non string unique key.

**Additional improvements and enhancements**
+ Fixed an issue with sp\_helpdb where NULL is shown for compatbility\_level.
+ Fixed a memory management issue with update\_DropRoleStmt.
+ Fixed table variables to make it immune to transaction rollback.
+ The fix corrects the behavior of ‘select convert(nvarchar(10),Getdate(),105)’ for nvarchar datatype.
+ Fixed an issue to allow UPDATE and DELETE for Table Variables inside functions.
+ Made enhancement to improve the performance and avoid catalog bloat while using table variables.
+ Fixed an issue in @@NEXTLEVEL which returned 1 unit larger than expected.
+ Fixed an issue in sp\_helpdb where input parameter’s case sensitivity is not handled properly.

### Babelfish for Aurora PostgreSQL 2.4 (Deprecated)
<a name="AuroraBabelfish.Updates.24X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.7. For more information about the improvements in Aurora PostgreSQL 14.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.4.4, November 6, 2024](#AuroraBabelfish.Updates.244)
+ [Aurora Babelfish release 2.4.3, October 4, 2023](#AuroraBabelfish.Updates.243)
+ [Aurora Babelfish release 2.4.2, July 24, 2023](#AuroraBabelfish.Updates.242)
+ [Aurora Babelfish release 2.4.1, May 10, 2023](#AuroraBabelfish.Updates.241)
+ [Aurora Babelfish release 2.4.0, April 5, 2023](#AuroraBabelfish.Updates.240)

#### Aurora Babelfish release 2.4.4, November 6, 2024
<a name="AuroraBabelfish.Updates.244"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.4.3, October 4, 2023
<a name="AuroraBabelfish.Updates.243"></a>
+ Fixed a memory management issue with `update_DropRoleStmt`.
+ Fixed a crash in `SqlBulkCopy` with heap\_compute\_data\_size function in stacktrace when the order of columns is different compared to table defining.
+ Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
+ Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.

#### Aurora Babelfish release 2.4.2, July 24, 2023
<a name="AuroraBabelfish.Updates.242"></a>

**Additional improvements and enhancements**
+ Fixed intermittent SSL connectivity issue during concurrent connections towards Babelfish instance.

#### Aurora Babelfish release 2.4.1, May 10, 2023
<a name="AuroraBabelfish.Updates.241"></a>

**Additional improvements and enhancements**
+ Fixed an issue to prevent error when sequences are created in a database other than 'master'.
+ Fixed a crash during bulk load operation in a specific scenario.

#### Aurora Babelfish release 2.4.0, April 5, 2023
<a name="AuroraBabelfish.Updates.240"></a>

**New features**
+ Supports minor version upgrade from Babelfish for Aurora PostgreSQL DB cluster 14.3 onwards to Aurora PostgreSQL 14.7. For more information on the minor version upgrade, see [Upgrading Babelfish to a new minor version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading.html#babelfish-information-upgrading-minor).
+ Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 13.x onwards to Aurora PostgreSQL 14.7. For more information on the major version upgrade, see [Upgrading Babelfish to a new major version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading.html#babelfish-information-upgrading-major).
+ Support for the following functions: STR, APP\_NAME, OBJECT\_DEFINITION, OBJECT\_SCHEMA\_NAME, ATN2, DATEDIFF\_BIG functions.
+ Support for the following INFORMATION\_SCHEMA views: sequences, routines and schemata.
+  Support sp\_rename for TABLE, VIEW, PROCEDURE, FUNCTION, SEQUENCE. 
+ Support sys.systypes system compatibility view.
+ Support for a new GUC parameter called babelfishpg\_tds.product\_version that allows you to set SQL Server product version number that is returned as an output by Babelfish. For more information, see [Using Babelfish product version GUC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-guc-version). 
+ Added support to generate data definition scripts for various objects present in a Babelfish for Aurora PostgreSQL database. For more information, see [DDL exports supported by Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-query-database.html#babelfish-ddl-exports).

**Security enhancements**
+ Fixed buffer overflow due to out of bound array access.

**High priority stability enhancements**
+ Improved the performance through interactive queries, ODBC-based applications and tools such as SQL Server Management Studio. Following enhancements has been made for the same:
  + Fixed performance issues in several system functions including OBJECT\_ID(), OBJECT\_NAME(), SCHEMA\_ID().
  + Fixed performance issues in system stored procedures sp\_sproc\_columns and sp\_fkeys.
  + Fixed performance issues in system catalog views sys.all\_views, sys.objects and sys.types.
  + Improved the performance of bulk load, parsing of T-SQL and prepared statements.
+ Added a new system stored procedure sp\_babelfish\_volatility that you can use to set the volatility of user-defined functions to improve index use when the functions are used as part of query predicates.
+ Fixed an issue where the UPDATE FROM or DELETE FROM statement that references the correlation name of the updated table raised an error.
+ Fixed an issue where scope\_identity function returns wrong result after exiting one scope.
+ Fixed an issue where name resolution doesn't work as expected when commands are invoked from the .NET client framework.

**Additional improvements and enhancements**
+ Fixed an issue where the statement timeout parameter for a session was not working as expected.
+  Support for sequence creations using user-defined data types. 
+ Fixed an issue where unicode in column names, aliases or comments causes parsing errors.
+ Fixed an issue where scope\_identity function requires higher permission than actually needed.
+ Support for NEXT VALUE FOR function that gets the next value of a sequence. Note that this function cannot be used in some control-of-flow statements. OVER clause is also not supported.
+ Fixed a crash when handling certain errors with sp\_describe\_undeclared\_parameters.
+ Fixed a rare error during Babelfish extension creation.
+ Fixed an issue which was throwing an error "typename is NULL" while using TVP in sp\_executesql.
+ Fixed SELECT FOR XML/JSON behavior to not raise error when using SELECT with correlation name in subquery using FOR XML PATH clause.
+ Fixed an issue with the SELECT FOR JSON or a SELECT FOR XML query which didn't return correct results for an empty table.
+ Fixed an issue where the guest user can create objects in the wrong schema.
+ Fixed schema name resolution for user defined types for param types in system stored procedures.
+ Fixed the issue where applications issuing queries with more than 100 bind parameters for prepared statements were failing. This limit is now increased to 2100 to match the limits used by SQL Server.
+ Fixed an issue with case handling of variable names in the sp\_executesql call.
+ sp\_fkeys stored procedure now also returns 'deferrability' column in the result set.
+ Fixed an issue in AVG aggregates which led to the termination of the connection for various integer datatypes.
+ The index\_id and indid column for respective views now returns the same value for indexes belonging to same object and the index\_id is unique only within the object.
+ Fixed an issue to not throw an error when OpenJson is called in stored procedures using nvarchar or join.
+ Fixed an issue to not throw an error while using try\_convert and try\_cast for prohibited conversions involving int literals.
+ Fixed an issue to allow OPENJSON WITH clause to accept a table alias.
+ Support Degrees, Radians and Power functions returning the proper type.
+ Fixed an issue where membership handling for sysadmin is not handled correctly.
+ Fixed the default output style when converting DATE/TIME types to VARCHAR type using CONVERT function.
+ Support EXECUTE AS CALLER clause in CREATE PROC/FUNCTION/TRIGGER.
+ Fixed an issue where configurations are not reverted after existing sp\_executesql scope.
+ Fixed issues with handling cross-database access for the sys.has\_perms\_by\_name function.
+ Support the ProductLevel and ProductUpdateLevel properties for the SERVERPROPERTY function. ProductUpdateLevel always returns NULL and ProductLevel tracks the Babelfish version number closely with the T-SQL definition.
+ Fixed an issue where the table variable when used as a bind parameter from client application resulted in an error.

### Babelfish for Aurora PostgreSQL 2.3 (Deprecated)
<a name="AuroraBabelfish.Updates.23X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.6. For more information about the improvements in Aurora PostgreSQL 14.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.3.4, November 18, 2024](#AuroraBabelfish.Updates.234)
+ [Aurora Babelfish release 2.3.3, September 13, 2023](#AuroraBabelfish.Updates.233)
+ [Aurora Babelfish release 2.3.2, March 3, 2023](#AuroraBabelfish.Updates.232)
+ [Aurora Babelfish release 2.3.0, January 20, 2023](#AuroraBabelfish.Updates.230)

#### Aurora Babelfish release 2.3.4, November 18, 2024
<a name="AuroraBabelfish.Updates.234"></a>

**Security enhancements**
+ Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.3.3, September 13, 2023
<a name="AuroraBabelfish.Updates.233"></a>

**Additional improvements and enhancements**
+ Fixed a rare error during Babelfish extension creation.
+ Fixed a memory management issue with `update_DropRoleStme`.

#### Aurora Babelfish release 2.3.2, March 3, 2023
<a name="AuroraBabelfish.Updates.232"></a>

**Security enhancements**
+ Fixed buffer overflow due to out of bound array access.

#### Aurora Babelfish release 2.3.0, January 20, 2023
<a name="AuroraBabelfish.Updates.230"></a>

**New features**
+ Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 13.6 and later to Aurora PostgreSQL 14.6. For more information on the major version upgrade, see [Upgrading your Babelfish cluster to a new version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information.html#babelfish-information-upgrading).
+ Support for T-SQL hints (join methods, index usage, MAXDOP). For more information on the T-SQL hints supported by Babelfish, see [Using T-SQL query hints to improve Babelfish query performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-tsql-hints).
+ Babelfish now supports Zero-downtime patching (ZDP). For more information, see [Minor release upgrades and zero-downtime patching](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html#USER_UpgradeDBInstance.PostgreSQL.Minor) in the *Amazon Aurora User Guide*.
+ Support for FORMAT() T-SQL function with minor limitations.
+ Support the estimated execution plans for THROW, PRINT, USE, and RAISEERROR statements.
+ Support for JSON\_MODIFY function in Babelfish which updates the value of a property in a JSON string and returns the updated JSON string.
+ Support the VALUES() constructor in FROM clause in a SELECT statement.
+ Support sp\_addrole, sp\_droprole, sp\_addrolemember, sp\_droprolemember procedures to create or alter a role.
+ Support for sys.all\_parameters catalog view.
+ Support guest user in all the user created databases and support GRANT/CONNECT TO/FROM user (including guest).
+ Support sp\_helpdbfixedrole and DATETIMEOFFSETFROMPARTS functions.

**High priority stability enhancements**
+ Improved performance for INSERT statement with IDENTITY\_INSERT=ON.
+ Fixed an issue where "DROP DATABASE" statement fails due to incorrect comparison operator used.
+ Fixed an issue where numeric overflow error was not handled properly for numeric types.
+ Fixed an issue where DB owner is not considered as dbo in its own DB.
+ Fixed issues with SSL handshake failure and added a few other improvements.
+ Fixed the sys.all\_objects view to correctly identify inline table-valued functions (IF) and table-valued functions (TF) which were previously reported as scalar functions (FN). Similar issue is fixed for the IsInlineFunction property of the OBJECTPROPERTY function.
+ Fixed an issue where DBO is assumed member of a DB role incorrectly.
+ Fixed an issue where member of sysadmin could not connect through SSMS.
+ Corrected the schema name resolution for triggers and views so that it selects/modifies the correct object(tables).
+ Fixed the mapping consistency in catalog when creating roles with names in upper/lower case.
+ Fixed an issue where drop database is blocked after access denial to other logins due to in sufficient permission.
+ Fixed the default collation of Babelfish data types except TEXT and NTEXT to be the same as that mentioned in the babelfishpg\_tsql.server\_collation\_name parameter. For more information, see [Default Collation in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-collations.html#babelfish-collations-default).
+ Fixed the cross-DB references to tempdb.sys.objects for correct results.

**Additional improvements and enhancements**
+ Fixed an issue to make trigger names unique for each database.
+ Fixed an issue in sp\_tables when it is invoked from JDBC metadata functions.
+ Fixed an issue when CHECK constraints are used with LIKE condition.
+ Performance improvements with sp\_sproc\_columns when dealing with stored procedures.
+ sp\_sproc\_columns now includes table-valued parameter row for stored procedures that use TVP as a parameter.
+ Fixed the cross-DB references to INFORMATION\_SCHEMA.ROUTINES and tempdb.sys.objects to give the correct results.
+ Fixed issues to support datetime/smalldatetime operation with various numeric and non numeric datatypes.
+ Fixed the return values of SUM aggregates for integer datatypes to return the correct datatypes.
+ Fixed an issue when UPDATE/DELETE is used with table aliases.
+ Support added for sysobjects.crdate (create\_date) for all user defined tables, views, procedures, functions, triggers and table types.
+ Procedure/function call is not allowed when required parameter is missing and an explicit error is raised.
+ Fixed issue to calculate the day difference and the hour difference, without considering timestamp (i.e., hh:mm:ss.msec).
+ Fixed an issue with DATEDIFF() function to return correct results between two input dates regardless of the input parameters.
+ Fixed an issue with DATEADD() function when used with the 'nanosecond' units.
+ Fixed an issue with DATEPART(), DATENAME(), DATEDIFF() and DATEADD() functions when used with 'w' units
+ Fixed an issue with DATEPART() and DATENAME() to allow units 'y'.
+ Fixed issues with DATEPART(), DATENAME(), DATEDIFF() and DATEADD() functions to convert string to datetime and to recognize mi units.
+ Support for TRY\_CONVERT() function.
+ Fixed issue with using strict/lax jsonpath with arrays to avoid OPENJSON error: "syntax error at or near " " of jsonpath input".
+ Support UDF (User Defined Function) as column default in ALTER TABLE statement.
+ Fixed an issue when SUBSTRING() takes NULL arguments.
+ Support for cast operations to SMALLDATETIME from various numeric types.
+ Fixed an issue where dbname parameter is not handled properly for sp\_helpdb.
+ Fixed an issue where DB owner is allowed to create another user for itself.
+ Fixed an issue where trailing spaces are not ignored in sp\_helpsrvrolemember and IS\_ROLEMEMBER/IS\_MEMBER functions.
+ Improved error message for unsupported data types: HIERARCHYID, GEOGRAPHY, GEOMETRY.
+ Fixed issues where cross database procedure calls and sp\_ procedures access from other databases should succeed even without EXECUTE keyword.
+ Fixed an issue where user 'guest' is not dropped in any database, but only disabled.
+ Fixed the column value for SID in the procedure sp\_helpuser when the user is guest.
+ Fixed an issue where overflow/underflow is not getting handled with money datatype.
+ Fixed an issue where error is not getting handled while error processing in tds.
+ Fixed a better error message for CREATE USER WITHOUT LOGIN.
+ Fixed an issue where sp\_helpsrvrolemember is throwing unsupported errors for unsupported server level roles.
+ Fixed an issue where SET BABELFISH\_STATISTICS PROFILE shows planning and execution times.
+ Corrected the schema name resolution for Babelfish objects like views and triggers, so that correct object is selected or modified.
+ Support rowversion/timestamp Datatype for Insert Bulk.
+ In Babelfish, sp\_babelfish\_configure supports enable\_pg\_hint and explain-related configurations by turning them "on/off". Accepting "ignore/strict" option is allowed when there are multiple matches while using sp\_babelfish\_configure.
+ Support to Keep Nulls (-k) bcp option for optimized implementation to insert Bulk.
+ Support multi-byte currency symbols to use with money data type.
+ Fixed issue for dotnet clients (including SSMS) that received invalid precision/scale error for certain arithmetic expressions.
+ Fixed the sys.all\_objects view to correctly identify inline table-valued functions (IF) and table-valued functions (TF) which were previously reported as scalar functions (FN). Fixed similar issue for the IsInlineFunction property of the OBJECTPROPERTY function.
+ Fixed an issue where the is\_member function returns an incorrect result for certain roles.
+ Improvements in FOR JSON PATH clause of SELECT statement which supports ROOT, INCLUDE\_NULL\_VALUES, WITHOUT\_ARRAY\_WRAPPER.
+ Supports a new escape hatch, 'escape\_hatch\_checkpoint' with a default pf 'ignore'. This escape hatch allows the use of CHECKPOINT statement in the procedural code, but the CHECKPOINT statement is currently not implemented.

### Babelfish for Aurora PostgreSQL 2.2
<a name="AuroraBabelfish.Updates.22X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.5. For more information about the improvements in Aurora PostgreSQL 14.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 2.2.3, October 17, 2023](#AuroraBabelfish.Updates.223)
+ [Aurora Babelfish release 2.2.2, March 2, 2023](#AuroraBabelfish.Updates.222)
+ [Aurora Babelfish release 2.2.1, December 13, 2022](#AuroraBabelfish.Updates.221)
+ [Aurora Babelfish release 2.2.0, November 9, 2022](#AuroraBabelfish.Updates.220)

#### Aurora Babelfish release 2.2.3, October 17, 2023
<a name="AuroraBabelfish.Updates.223"></a>

**High priority stability enhancements**
+ Fixed issues with SSL handshake failure and added a few other improvements.

**Additional improvements and enhancements**
+ Fixed a memory management issue with `update_DropRoleStmt`.

#### Aurora Babelfish release 2.2.2, March 2, 2023
<a name="AuroraBabelfish.Updates.222"></a>

**Security enhancements**
+ Fixed buffer overflow due to out of bound array access.

#### Aurora Babelfish release 2.2.1, December 13, 2022
<a name="AuroraBabelfish.Updates.221"></a>
+ Fixed an issue that prevented the use of collations like Chinese\_PRC\_CI\_AS, Japanese\_CI\_AS and so on for babelfishpg\_tsql.server\_collation\_name.

#### Aurora Babelfish release 2.2.0, November 9, 2022
<a name="AuroraBabelfish.Updates.220"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

**High priority stability enhancements**
+ Fixed error handling in sp\_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
+ Fixed error handling in SSL/TLS handshake for some client drivers.
+ Fixed an issue where a login can access the database without creating DB user after the DROP/CREATE of login.
+ Fixed an issue where a login isn't dropped if it is logged in on any session.

**New features**
+ Support for data migration using the BCP client and the bcp utility now supports -E flag (for identity columns) and -b flag (for batching inserts).
+ Support for cross-database stored procedure execution.
+ Support for CROSS APPLY and OUTER APPLY (lateral join).
+ Support for built-in functions SYSTEM\_USER, HOST\_NAME; the Hostname is visible in the sys.sysprocesses T-SQL view; the SID\_BINARY function is supported but always returns NULL in Babelfish.
+ Support for CAST function of numeric expressions to DATETIME.
+ Support for @@LANGUAGE variable with constant value as 'us\_english’.
+ Support for the old-style function calls with '::' preceding the function name.
+ Support for the sp\_helpsrvrolemember stored procedure.
+ Support for the msdb.dbo.fn\_syspolicy\_is\_automation\_enabled system function.
+ Support for more catalogs: assembly\_types, numbered\_procedures, triggers, spatial\_index\_tessellations, plan\_guides, synonyms, events, trigger\_events, fulltext\_indexes, dm\_hadr\_cluster, xml\_indexes, change\_tracking\_tables, key\_constraints, database\_filestream\_options, filetable\_system\_defined\_objects, hash\_indexes, filegroups, master\_files, assembly\_modules, change\_tracking\_databases, database\_recovery\_status, fulltext\_catalogs, fulltext\_stoplists, fulltext\_indexes, fulltext\_index\_columns, fulltext\_languages, selective\_xml\_index\_paths, spatial\_indexes, filetables, registered\_search\_property\_lists, syspolicy\_configuration, syspolicy\_system\_health\_state.
+ Support for new INFORMATION\_SCHEMA catalogs: COLUMN\_DOMAIN\_USAGE, CONSTRAINT\_COLUMN\_USAGE, CHECK\_CONSTRAINTS, ROUTINES, VIEWS.
+ Support for new PG-style query plan: escape hatch 'babelfish\_pgtsql.escape\_hatch\_showplan\_all'.
  + when set to 'ignore', SET SHOWPLAN\_ALL and SET STATISTICS PROFILE behaves as SET BABELFISH\_SHOWPLAN\_ALL and SET BABELFISH\_STATISTICS PROFILE. 
  + when set to 'strict', SET SHOWPLAN\_ALL and SET STATISTICS PROFILE are silently ignored.
+  Support for executing stored procedures with the sp\_ prefix in the master database without using a three-part name. 

**Additional improvements and enhancements**
+ Fixed an issue where a value of 1900-01-01 00:00:00 was stored when a NULL was inserted or updated into a datetime column. A NULL value is inserted now. Column values in tables created in a previous Babelfish release are not affected.
+ TIME datatypes that return 7 digits in SQL Server now returns 7 digits in Babelfish as well, with the 7th digit always being zero. In addition, a rounding issue that sometimes affected the 6th digit has been resolved.
+  Increased parameter lengths for @tsql and @params for sp\_describe\_first\_result\_set from nvarchar(384) to nvarchar(8000). This increases the number of columns the DMS Babelfish target endpoint can support from 25 to 1000. 
+ Improved performance for system stored procedures: sys.sp\_tablecollations\_100, sp\_columns\_managed, and sp\_describe\_undeclared\_parameters. This fix improves the performance of the DMS Babelfish target endpoint, SQL Server Management Studio import and export wizard, and prevents timeouts.
+ Fixed an issue with Bitwise NOT \~ operator and it returns the correct result with BIT data types now. 
+ Fixed an issue with BCP when it is used for tables that have triggers.
+ Fixed an issue of backend failure in INSERT BULK when using Import-Export wizard.
+ Fixed an issue where SQL Server Management Studio (SSMS) returns an error while expanding "Triggers" for a table in the Object Explorer view.
+ Fixed an issue where the name column in the sys.sysobjects view was using case sensitive collation.
+ Fixed an issue to refer SQL objects inside a function and is resolved to the function's schema rather than the default schema of the user.
+ Fixed an issue where a backend crash can occur when using the ISNULL function with CONVERT on computed columns.
+ Fixed an issue with the DATEPART function when the date argument is a string literal.
+ Fixed an issue where a role can be dropped even if it has members.
+ Fixed an issue so that the db user can't add to a role or drop from a role.
+ Fixed an issue to allow BCP to work correctly with collations other than English collations.
+ Fixed an issue to make sp\_helpuser procedure show login name for dbo user.
+ Fixed an issue to handle NULL and mix-cased inputs correctly for the functions SUSER\_SNAME and SUSER\_SID.
+ Fixed an issue with Babelfish returning an invalid TDS protocol stream when there is a numeric overflow error.
+ Fixed an issue where is\_fixed\_role column returns incorrect value in the sys.server\_principals view for the 'sysadmin' role.
+ Fixed the transaction error handling in a batch if the string passed to execute contains a USE `dbname` and fails because the database `dbname` was not found.
+ Fixed the issue with procedures created in master database context with prefix sp\_ that are not accessible from other database context.
+ Fixed the failure to resolve object name inside a procedure when used with schema name.
+ Fixed case-sensitivity issue with arguments to the functions USER\_ID and SUSER\_ID.
+ Fixed an issue where triggers were allowed to be created on Babelfish temporary tables.
+ Fixed several performance issues with Import-Export wizard.
+ Support for multi-byte client encodings other than UTF-16 for VARCHAR(n).
+ Fixed the system compatibility view sys.sysprocesses to show the correct value for hostname provided by the client connection.
+ Fixed case sensitivity issue with Polish\_CI\_AS collation.
+ Fixed the @@DBTS function so that value of @@DBTS correctly returns the current transaction id after each DML statement even when used within a transaction.
+  Improved performance for queries that refer to the functions SCOPE\_IDENTITY and @@IDENTITY. 
+  Support added for collations Japanese\_CS\_AS, Japanese\_CI\_AI and Japanese\_CI\_AS for fn\_helpcollations. 
+ @@SERVERNAME and SERVERPROPERTY('ServerName') now return the name of the Babelfish instance as specified by the user when the instance is created. This value is also returned by the newly supported properties SERVERPROPERTY('MachineName') and SERVERPROPERTY('InstanceName').
+ Function fn\_mapped\_system\_error\_list lists the PG error code mapped to @@ERROR codes, as well as the corresponding error message text. This function also exists in previous Babelfish releases but did not include mapping details.
+  Fixed DATEADD function to now support milliseconds(ms) time units. 
+ SET NO\_BROWSETABLE {ON\|OFF} is now subject to escape hatch escape\_hatch\_session\_settings, so no error is raised when set to ignored.
+ SET PARSEONLY {ON\|OFF} is now supported. Previously this would raise an error unless escape hatch escape\_hatch\_session\_settings is set to ignored.
+ The DATABASE\_DEFAULT AND CATALOG\_DEFAULT collation is now supported; this refers to the server/instance-level collation that was specified when the Babelfish instance was created, as Babelfish doesn't currently support collations on database level.
+ For the functions OBJECTPROPERTY and OBJECTPROPERTYEX, the following properties are now supported: ExecIsAnsiNullsOn, ExecIsQuotedIdentOn, IsDefault, IsDefaultCnst, IsDeterministic, IsIndexed, IsInlineFunction, IsMSShipped, IsPrimaryKey, IsProcedure, IsRule, IsScalarFunction, IsSchemaBound, IsTable, IsTableFunction, IsTrigger, IsUserTable, IsView, OwnerId, TableFulltextPopulateStatus, TableHasVarDecimalStorageFormat.
+ OBJECTPROPERTYEX function supports the BaseType property.
+ INDEXPROPERTY function supports the following properties: IndexFillFactor, IndexID, IsClustered, IsDisabled, IsHypothetical, IsPadIndex, IsPageLockDisallowed, IsRowLockDisallowed, IsUnique.

### Babelfish for Aurora PostgreSQL 2.1
<a name="AuroraBabelfish.Updates.21X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.3 and 14.4. For more information about the improvements in Aurora PostgreSQL 14.3 and 14.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 2.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html).

**Topics**
+ [Babelfish for Aurora PostgreSQL release 2.1.2, October 18, 2022](#AuroraBabelfish.Updates.212)
+ [Babelfish for Aurora PostgreSQL release 2.1.1, July 6, 2022](#AuroraBabelfish.Updates.211)
+ [Babelfish for Aurora PostgreSQL release 2.1.0, June 21, 2022](#AuroraBabelfish.Updates.210)

#### Babelfish for Aurora PostgreSQL release 2.1.2, October 18, 2022
<a name="AuroraBabelfish.Updates.212"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

**High priority stability enhancements**
+ Fixed error handling in sp\_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
+ Fixed error handling in SSL/TLS handshake for some client drivers.

#### Babelfish for Aurora PostgreSQL release 2.1.1, July 6, 2022
<a name="AuroraBabelfish.Updates.211"></a>
+ Fixed the babelfishpg\_tds extension to correctly allocate the shared memory size used by the extension.

#### Babelfish for Aurora PostgreSQL release 2.1.0, June 21, 2022
<a name="AuroraBabelfish.Updates.210"></a>

Babelfish DB clusters running on Aurora PostgreSQL 13.7 or older versions can't be upgraded to Aurora PostgreSQL 14.3 with Babelfish 2.1.0.

**New features**
+ Support for data migration using the bcp client utility, as an experimental feature. Some bcp options (-b, -C, -E, -G, -h, -K, -k, -q, -R, -T, -V) are not currently supported.
+ Support for connecting with the SSMS object explorer connection dialog (rather than only the Query Editor connection dialog), as well as partial support for the SSMS object explorer itself.
+ Improved support for data migration with the SSMS Import/Export Wizard.
+ Support for IS\_MEMBER, IS\_ROLEMEMBER, and HAS\_PERMS\_BY\_NAME functions.
+ Support for syslanguages, sys.indexes, sys.all\_views, sys.database\_files, sys.sql\_modules, sys.system\_sql\_modules, sys.all\_sql\_modules, sys.xml\_schema\_collections, sys.dm\_hadr\_database\_replica\_states, sys.data\_spaces, sys.database\_mirroring, sys.database\_role\_members catalogs.
+ Support for sp\_sproc\_columns, sp\_sproc\_columns\_100, sp\_helprole, sp\_helprolemember system stored procedures.
+ Support for Japanese\_CS\_AS, Japanese\_CI\_AI, Japanese\_CI\_AS collations.
+ Babelfish now supports CHARINDEX substring searches on systems using nondeterministic collations.
+ Babelfish now supports PATINDEX, and supports arguments to STRING\_SPLIT that are collated using a case-insensitive collation.
+ Query plan output is generated following SET BABELFISH\_SHOWPLAN\_ALL ON (and OFF) and SET BABELFISH\_STATISTICS PROFILE ON (OFF). This will generate PostgreSQL-style query plan information for T-SQL queries in Babelfish. Make sure these SET statements are identical to existing T-SQL statements, but with the added BABELFISH\_ prefix.

**Additional improvements and enhancements**
+ Cross–database references outside the current database, with a 3-part object name, for SELECT,SELECT..INTO, INSERT, UPDATE, DELETE.
+ CREATE ROLE (AUTHORIZATION clause not supported), DROP ROLE, ALTER ROLE.
+ Babelfish now maps the error code for @@ERROR=213. For more information on error handling, see [Managing Babelfish error handling.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-strict)
+ Fixed an issue with SUBSTRING(CHARINDEX()) variable assignment that caused Babelfish to become unavailable. 
+ Fixed an issue with INSERT INTO...with OUTPUT clause that resulted in a `Number of given values doesn't match target table definition` error.
+ Fixed an issue that caused DELETE with OUTPUT INTO temporary table statements to return a `WITH query 'nnnnnnnnnnn' doesn't have a RETURNING clause` error.
+ Fixed an issue that caused LEFT OUTER JOIN to fail with a `Sqlcmd: Error: Internal error at ReadAndHandleColumnData (Reason: Error reading column data)` error. This issue was a regression introduced in Babelfish 1.1.0. If your Babelfish for Aurora PostgreSQL DB cluster runs Babelfish version 1.1.0 and you get this error, we recommend that you upgrade to Aurora PostgreSQL 13.7 to obtain this fix.
+ Fixed an invalid syntax error using the GETUTCDATE() and SYSUTCDATETIME() built-in functions.
+ Fixed an issue where numeric overflow conditions using SUM() and AVG() functions caused a TDS error.
+ Fixed an issue with .NET applications calling store procedures for a DataTable object that resulted in a datatype mismatch and disallowed implicit casting error.

## Babelfish for Aurora PostgreSQL 1.x versions (includes some deprecated versions)
<a name="aurorababelfish-versions-version1x"></a>

**Topics**
+ [Babelfish for Aurora PostgreSQL 1.5](#AuroraBabelfish.Updates.15X)
+ [Babelfish for Aurora PostgreSQL 1.4 (Deprecated)](#AuroraBabelfish.Updates.14X)
+ [Babelfish for Aurora PostgreSQL 1.3 (Deprecated)](#AuroraBabelfish.Updates.13X)
+ [Babelfish for Aurora PostgreSQL 1.2 (Deprecated)](#AuroraBabelfish.Updates.12X)
+ [Babelfish for Aurora PostgreSQL 1.1 (Deprecated)](#AuroraBabelfish.Updates.11X)
+ [Babelfish for Aurora PostgreSQL 1.0 (Deprecated)](#AuroraBabelfish.Updates.10X)

### Babelfish for Aurora PostgreSQL 1.5
<a name="AuroraBabelfish.Updates.15X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.9. For more information about the improvements in Aurora PostgreSQL 13.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). Babelfish for Aurora PostgreSQL 1.5 adds a new feature and an enhancement. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 1.5.0, January 20, 2023](#AuroraBabelfish.Updates.150)

#### Aurora Babelfish release 1.5.0, January 20, 2023
<a name="AuroraBabelfish.Updates.150"></a>

**New features**
+ Babelfish now supports Zero-downtime patching (ZDP). For more information, see [Minor release upgrades and zero-downtime patching](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html#USER_UpgradeDBInstance.PostgreSQL.Minor) in the *Amazon Aurora User Guide*.

**High priority stability enhancements**
+ Fixed an issue related to money operator class during minor version upgrade from 13.4 to 13.5 or later due to which the upgrade was failing.

### Babelfish for Aurora PostgreSQL 1.4 (Deprecated)
<a name="AuroraBabelfish.Updates.14X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.8. For more information about the improvements in Aurora PostgreSQL 13.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). The following issues are resolved in Babelfish for Aurora PostgreSQL 1.4 release. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Aurora Babelfish release 1.4.1, December 13, 2022](#AuroraBabelfish.Updates.141)
+ [Aurora Babelfish release 1.4.0, November 9, 2022](#AuroraBabelfish.Updates.140)

#### Aurora Babelfish release 1.4.1, December 13, 2022
<a name="AuroraBabelfish.Updates.141"></a>
+ Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.8.

#### Aurora Babelfish release 1.4.0, November 9, 2022
<a name="AuroraBabelfish.Updates.140"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

**High priority stability enhancements**
+ Fixed error handling in sp\_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
+ Fixed error handling in SSL/TLS handshake for some client drivers.

**Additional improvements**
+ Fixed the babelfishpg\_tds extension to correctly allocate the shared memory size used by the extension.

### Babelfish for Aurora PostgreSQL 1.3 (Deprecated)
<a name="AuroraBabelfish.Updates.13X"></a>

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.7. For more information about the improvements in Aurora PostgreSQL 13.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). The following issues are resolved in Babelfish for Aurora PostgreSQL 1.3 release. For more information about Babelfish for Aurora PostgreSQL, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Babelfish for Aurora PostgreSQL release 1.3.3, December 14, 2022](#AuroraBabelfish.Updates.133)
+ [Babelfish for Aurora PostgreSQL release 1.3.2, October 18, 2022](#AuroraBabelfish.Updates.132)
+ [Babelfish for Aurora PostgreSQL release 1.3.1, July 6, 2022](#AuroraBabelfish.Updates.131)
+ [Babelfish for Aurora PostgreSQL release 1.3.0, June 9, 2022](#AuroraBabelfish.Updates.130)

#### Babelfish for Aurora PostgreSQL release 1.3.3, December 14, 2022
<a name="AuroraBabelfish.Updates.133"></a>
+ Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.7.

#### Babelfish for Aurora PostgreSQL release 1.3.2, October 18, 2022
<a name="AuroraBabelfish.Updates.132"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

**High priority stability enhancements**
+ Fixed error handling in sp\_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
+ Fixed error handling in SSL/TLS handshake for some client drivers.

#### Babelfish for Aurora PostgreSQL release 1.3.1, July 6, 2022
<a name="AuroraBabelfish.Updates.131"></a>
+ Fixed the babelfishpg\_tds extension to correctly allocate the shared memory size used by the extension.

#### Babelfish for Aurora PostgreSQL release 1.3.0, June 9, 2022
<a name="AuroraBabelfish.Updates.130"></a>
+ Fixed an issue with SUBSTRING(CHARINDEX()) variable assignment that caused Babelfish to become unavailable. 
+ Fixed an issue with INSERT INTO...with OUTPUT clause that resulted in a `Number of given values doesn't match target table definition` error.
+ Fixed an issue that caused DELETE with OUTPUT INTO temporary table statements to return a `WITH query 'nnnnnnnnnnn' doesn't have a RETURNING clause` error.
+ Fixed an issue that caused LEFT OUTER JOIN to fail with a `Sqlcmd: Error: Internal error at ReadAndHandleColumnData (Reason: Error reading column data)` error. This issue was a regression introduced in Babelfish 1.1.0. If your Babelfish for Aurora PostgreSQL DB cluster runs Babelfish version 1.1.0 and you get this error, we recommend that you upgrade to Aurora PostgreSQL 13.7 to obtain this fix.

### Babelfish for Aurora PostgreSQL 1.2 (Deprecated)
<a name="AuroraBabelfish.Updates.12X"></a>

This release of Babelfish is provided with Aurora PostgreSQL 13.6. For more information about the improvements in Aurora PostgreSQL 13.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). The following issues are resolved in Babelfish 1.2 release. For more information about Babelfish, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Babelfish for Aurora PostgreSQL release 1.2.4, December 15, 2022](#AuroraBabelfish.Updates.124)
+ [Babelfish for Aurora PostgreSQL release 1.2.3, October 18, 2022](#AuroraBabelfish.Updates.123)
+ [Babelfish for Aurora PostgreSQL release 1.2.2, July 18, 2022](#AuroraBabelfish.Updates.122)
+ [Babelfish for Aurora PostgreSQL release 1.2.1, April 27, 2022](#AuroraBabelfish.Updates.121)
+ [Babelfish for Aurora PostgreSQL release 1.2.0, March 29, 2022](#AuroraBabelfish.Updates.120)

#### Babelfish for Aurora PostgreSQL release 1.2.4, December 15, 2022
<a name="AuroraBabelfish.Updates.124"></a>
+ Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.6.

#### Babelfish for Aurora PostgreSQL release 1.2.3, October 18, 2022
<a name="AuroraBabelfish.Updates.123"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

#### Babelfish for Aurora PostgreSQL release 1.2.2, July 18, 2022
<a name="AuroraBabelfish.Updates.122"></a>
+ Fixed an issue causing outer join queries to sometimes fail with an internal error message. 
+ Fixed the babelfishpg\_tds extension to correctly allocate the shared memory size used by the extension. 

#### Babelfish for Aurora PostgreSQL release 1.2.1, April 27, 2022
<a name="AuroraBabelfish.Updates.121"></a>
+ Fixed an issue that caused Babelfish to become unavailable after working with temporary tables. 
+ Fixed an issue that prevented successful minor version upgrade from a Babelfish for Aurora PostgreSQL 13.4 or 13.5 DB cluster to Aurora PostgreSQL 13.6. 
+ Fixed an issue that prevented transferring data to a table with identity columns using the SQL Server Management Studio import and export wizard. 

#### Babelfish for Aurora PostgreSQL release 1.2.0, March 29, 2022
<a name="AuroraBabelfish.Updates.120"></a>

In addition to the new features and improvements in the following list, Babelfish for Aurora PostgreSQL 1.2.0 adds several features that currently have limited implementations. These features are available for use but don't yet have complete parity with T-SQL syntax or Microsoft SQL Server. For more information, see [Features with limited implementation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.html#babelfish-compatibility.tsql.limited-implementation). 
+ Casing (upper-case, lower-case) of column names as created with T-SQL is now retained. That is, `SELECT * FROM {{table}}` returns the column names using the same casing as used when the table was created at the TDS endpoint.
+ INSTEAD-OF triggers are now supported on tables (tables only, not views). 
+ Support for system-defined global variables @@DBTS, @@LOCK\_TIMEOUT, @@SERVICENAME. 
+ Support for syntax SET LOCK\_TIMEOUT. 
+ Support for datatypes TIMESTAMP and ROWVERSION.
+ Support for built-in functions COLUMNS\_UPDATED, UPDATE, FULLTEXTSERVICEPROPERTY, ISJSON, JSON\_QUERY, JSON\_VALUE, HAS\_DBACCESS, SUSER\_SID, SUSER\_SNAME, IS\_SRVROLEMEMBER.
+ Full support for the CHECKSUM function. This function now supports \* and multiple columns (`CHECKSUM ( * | expression [ ,...n ] )`). 
+ Full support for the SCHEMA\_ID function. This function can now be used without any arguments (`SCHEMA_ID ( [ schema_name ] )`). 
+ Support for DROP IF EXISTS with SCHEMA, DATABASE, and USER objects. 
+ Support for these additional values for CONNECTIONPROPERTY: physical\_net\_transport and client\_net\_address. 
+ Support for the these SERVERPROPERTY values: EditionID, EngineEdition, LicenseType, ProductVersion, ProductMajorVersion, ProductMinorVersion, IsIntegratedSecurityOnly, IsLocalDB, IsAdvancedAnalyticsInstalled, IsBigDataCluster, IsPolyBaseInstalled, IsFullTextInstalled, and IsXTPSupported. 
+ Support for these catalogs: sys.dm\_os\_host\_info, sys.dm\_exec\_sessions, sys.dm\_exec\_connections, sys.endpoints, sys.table\_types, sys.database\_principals, sys.sysprocesses, sys.sysconfigures, sys.syscurconfigs, and sys.configurations. 
+ Support for these INFORMATION\_SCHEMA catalogs: TABLES, COLUMNS, DOMAINS, and TABLE\_CONSTRAINTS.
+ Support for these system stored procedures: sp\_table\_privileges, sp\_column\_privileges, sp\_special\_columns, sp\_fkeys, sp\_pkeys, sp\_stored\_procedures, xp\_qv, sp\_describe\_undeclared\_parameters, and sp\_helpuser. 
+ Limited support for creating, altering, and dropping database principals (USER objects). Limitations for CREATE/ALTER/DROP syntax with USER objects are as follows:
  + For CREATE USER, you can specify the FOR/FROM LOGIN and DEFAULT\_SCHEMA options only.
  + For ALTER USER, you can specify DEFAULT\_SCHEMA option only.
+ Limited support for the SET FMTONLY ON command. Setting this command ON suppresses the execution of SELECT statements only. It doesn't suppress the execution of other statements. 
+ Support for granting and revoking (GRANT/REVOKE) permisions for database principals only (not database roles). Support includes GRANT OPTION and REVOKE..CASCADE options for SELECT, INSERT, UPDATE, DELETE, REFERENCES, EXECUTE, and ALL [PRIVILEGES]. 
+ Support for WITH AUTHORIZATION on CREATE SCHEMA.
+ Support for the following new escape hatches and escape hatch functionality:
  + Restore all default settings for escape hatches for your Babelfish DB instance by passing `default` as the second argument to the `sp_babelfish_configure` stored procedure.
  + A new escape hatch, `escape_hatch_ignore_dup_key` (default=strict) controls the IGNORE\_DUP\_KEY option in CREATE/ALTER TABLE and CREATE INDEX statements. When IGNORE\_DUP\_KEY=ON, an error is raised unless escape\_hatch\_ignore\_dup\_key is set to `'ignore'`. 
  + Added support for the `ignore` option on the `escape_hatch_storage_options` escape hatch. When set to `ignore`, Babelfish ignores errors raised in the following cases:
    + Ignores errors raised in the ON clause in a CREATE DATABASE statement. 
    + Ignores errors raised by CREATE INDEX when used with SORT\_IN\_TEMPDB, DROP\_EXISTING, or ONLINE options. 

  For details, see [Managing Babelfish error handling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-strict.html#babelfish-escape_hatches).
+ The msdb system database is always present, and has dbid=4. For more information, see [Babelfish architecture](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html#babelfish-architecture). 
+ For a list of features supported in each Babelfish release, see [Supported functionality in Babelfish by version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.supported-functionality-table.html). 

### Babelfish for Aurora PostgreSQL 1.1 (Deprecated)
<a name="AuroraBabelfish.Updates.11X"></a>

This release of Babelfish is provided with Aurora PostgreSQL 13.5. For more information about the improvements in Aurora PostgreSQL 13.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). The following issues are resolved in Babelfish 1.1 release. For more information about Babelfish, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Babelfish for Aurora PostgreSQL release 1.1.2, December 16, 2022](#AuroraBabelfish.Updates.112)
+ [Babelfish for Aurora PostgreSQL release 1.1.1, October 18, 2022](#AuroraBabelfish.Updates.111)
+ [Babelfish for Aurora PostgreSQL release 1.1.0, February 25, 2022](#AuroraBabelfish.Updates.110)

#### Babelfish for Aurora PostgreSQL release 1.1.2, December 16, 2022
<a name="AuroraBabelfish.Updates.112"></a>
+ Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.5.

#### Babelfish for Aurora PostgreSQL release 1.1.1, October 18, 2022
<a name="AuroraBabelfish.Updates.111"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

#### Babelfish for Aurora PostgreSQL release 1.1.0, February 25, 2022
<a name="AuroraBabelfish.Updates.110"></a>

Babelfish for Aurora PostgreSQL version 1.1.0 adds support for the following Microsoft SQL Server functionality and T-SQL commands. For more information, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html).
+ Unique indexes or UNIQUE constraints on nullable columns. To use this capability, change the `escape_hatch_unique_constraint` to `'ignore'`. For more information, see [Managing Babelfish error handling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-strict.html#babelfish-escape_hatches)
+ Reference transition tables from triggers with multiple DML actions.
+ Identifiers that have leading dot characters.
+ The COLUMNPROPERTY function (limited to CharMaxLen and AllowsNull properties). 
+ System-defined @@ variables: @@CURSOR\_ROWS, @@LOCK\_TIMEOUT, @@MAX\_CONNECTIONS, @@MICROSOFTVERSION, @@NESTLEVEL, and @@PROCID.
+ Built-in functions: CHOOSE, CONCAT\_WS, CURSOR\_STATUS, DATEFROMPARTS, DATETIMEFROMPARTS, ORIGINAL\_LOGIN, SCHEMA\_NAME (now fully supported), SESSION\_USER, SQUARE, and TRIGGER\_NESTLEVEL supported (but only without arguments). 
+ System stored procedures: sp\_columns, sp\_columns\_100, sp\_columns\_managed, sp\_cursor, sp\_cursor\_list, sp\_cursorclose, sp\_cursorexecute, sp\_cursorfetch, sp\_cursoropen, sp\_cursoroption, sp\_cursorprepare, sp\_cursorprepexec, sp\_cursorunprepare, sp\_databases, sp\_datatype\_info, sp\_datatype\_info\_100, sp\_describe\_cursor, sp\_describe\_first\_result\_set, sp\_describe\_undeclared\_parameters, sp\_oledb\_ro\_usrname, sp\_pkeys, sp\_prepare, sp\_statistics, sp\_statistics\_100, sp\_tablecollations\_100, sp\_tables, and sp\_unprepare. 
+ For a list of features supported in each Babelfish release, see [Supported functionality in Babelfish by version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.supported-functionality-table.html). 

### Babelfish for Aurora PostgreSQL 1.0 (Deprecated)
<a name="AuroraBabelfish.Updates.10X"></a>

This release of Babelfish is provided with Aurora PostgreSQL 13.4. For more information about the improvements in Aurora PostgreSQL 13.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.Updates.md). The following issues are resolved in Babelfish 1.0 release. For more information about Babelfish, see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html). 

**Topics**
+ [Babelfish for Aurora PostgreSQL release 1.0.1, October 18, 2022](#AuroraBabelfish.Updates.101)
+ [Babelfish for Aurora PostgreSQL release 1.0.0, October 28, 2021](#AuroraBabelfish.Updates.100)

#### Babelfish for Aurora PostgreSQL release 1.0.1, October 18, 2022
<a name="AuroraBabelfish.Updates.101"></a>

**Security enhancements**
+ Fixed critical issues in Babelfish due to incorrect handling of user input for some application features. This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj).

#### Babelfish for Aurora PostgreSQL release 1.0.0, October 28, 2021
<a name="AuroraBabelfish.Updates.100"></a>
+ Babelfish for Aurora PostgreSQL version 1.0.0 supports Babelfish 1.0.0 which extends your Amazon Aurora PostgreSQL database with the ability to accept database connections from Microsoft SQL Server clients. For more information, see see [Working with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html).