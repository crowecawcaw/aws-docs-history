# Babelfish for Aurora PostgreSQL updates

Following, you can find information about versions of the Babelfish that have been
released for Aurora PostgreSQL. Babelfish is an option available with Aurora PostgreSQL
version 13.4 and higher releases. Updates to Babelfish become available with certain
new releases of the Aurora PostgreSQL database engine.

For information about Aurora PostgreSQL extensions with Babelfish, see [Using
Aurora PostgreSQL extensions with Babelfish](../AuroraUserGuide/babelfish-postgres-aws-extensions.md "../AuroraUserGuide/babelfish-postgres-aws-extensions.md").

For information about Babelfish version updates, see [Babelfish version
updates](../AuroraUserGuide/babelfish-information.md "../AuroraUserGuide/babelfish-information.md").

For a list of supported and unsupported functionality across different Babelfish
releases, see [Babelfish for Aurora PostgreSQL reference](../AuroraUserGuide/USER_AuroraPostgreSQL_Babelfish_Reference.md "../AuroraUserGuide/USER_AuroraPostgreSQL_Babelfish_Reference.md").

###### Topics

- [Babelfish for Aurora PostgreSQL 5.x versions](#aurorababelfish-versions-version5x "#aurorababelfish-versions-version5x")
- [Babelfish for Aurora PostgreSQL 4.x versions](#aurorababelfish-versions-version4x "#aurorababelfish-versions-version4x")
- [Babelfish for Aurora PostgreSQL 3.x versions (includes some deprecated versions)](#aurorababelfish-versions-version3x "#aurorababelfish-versions-version3x")
- [Babelfish for Aurora PostgreSQL 2.x versions (includes some deprecated versions)](#aurorababelfish-versions-version2x "#aurorababelfish-versions-version2x")
- [Babelfish for Aurora PostgreSQL 1.x versions (includes some deprecated versions)](#aurorababelfish-versions-version1x "#aurorababelfish-versions-version1x")

## Babelfish for Aurora PostgreSQL 5.x versions

###### Version updates

- [Babelfish for Aurora PostgreSQL 5.4](#AuroraBabelfish.Updates.54X "#AuroraBabelfish.Updates.54X")
- [Babelfish for Aurora PostgreSQL 5.3](#AuroraBabelfish.Updates.53X "#AuroraBabelfish.Updates.53X")
- [Babelfish for Aurora PostgreSQL 5.2](#AuroraBabelfish.Updates.52X "#AuroraBabelfish.Updates.52X")
- [Babelfish for Aurora PostgreSQL 5.1](#AuroraBabelfish.Updates.51X "#AuroraBabelfish.Updates.51X")

### Babelfish for Aurora PostgreSQL 5.4

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.7. For more
information about the improvements in Aurora PostgreSQL 17.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
5.4 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 5.4.0, December, 18, 2025

**New Features**

- Enabled support of SELECT TOP N PERCENT clause with few [limitations](../AuroraUserGuide/babelfish-compatibility.tsql.md "../AuroraUserGuide/babelfish-compatibility.tsql.md").
- Enabled support for Linestring instances for [geography/geometry datatypes](../AuroraUserGuide/babelfish-geospatial.md "../AuroraUserGuide/babelfish-geospatial.md").
- Enabled support for system procedures sp_xml_preparedocument, sp_xml_removedocument and [OPENXML](../AuroraUserGuide/babelfish-xml-datatype-methods.md "../AuroraUserGuide/babelfish-xml-datatype-methods.md").
- Enabled support for XML method .VALUE() for XML Data Types.
- Enabled support for ownership chaining for object references inside views and stored procedures/functions. Permission checking on underlying objects is determined by either the user's direct permissions or through ownership chaining.
- Enabled support of sys.time_zone_info view
- Enabled support for Values clause and subquery columns in SELECT list in FOR JSON AUTO functionality

**Critical enhancements**

- Fixed STPointFromText() and Point() to throw error on NULL arguments.
- Fixed issues with Geometry/Geography to (var)char and (var)binary conversions.
- Fixed function definition of STPointFromText(), STPointFromText(), STAsText() and STAsBinary().
- Fixed bytea to Geometry/Geography conversion for Point instance.
- ASCII function returns incorrect results with argument type as Binary and Varbinary.
- Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.
- Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

**High Priority stability enhancements**

- Fixed an issue where user can not be dropped when permissions have been granted to that user.
- Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
- Fixed precision/scale for Round() function.
- Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.
- Fixed an issue where errors in pg_cron job was leading to server reboot.

**Additional improvements and enhancements**

- Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.
- Fixed an issue which resets the escape hatch settings to default with the first temp table creation.
- Fixed Datetime and Varbinary to Binary CAST functions.
- Fixed an issue to match CONVERT and CAST function return values for Binary type.
- Fixed INSERT INTO table DEFAULT VALUES for domain types, by setting appropriate function return type.
- Fixed an issue where running multi-Statement table valued function throws syntax error if the database name contains a symbol for an operator.
- Fixed REVOKE permission execution to correctly handle overlapping schema-level and object-level grants.
- Enabled support for the NULL/NOT NULL syntax in ALTER TABLE ALTER COLUMN statements.
- Add identifier delimiters to handle special characters in login and role names.
- Fixed indexes that were created on top of T-SQL temporary tables to correctly follow transaction semantics.
- Fixed various mathematical functions for Money and smallmoney datatype.
- Fixed an issue to persist column level permissions when modifying views using ALTER VIEW.
- Enabled support to allow alter on functions with dependent weak schemabinding views.
- Fixed issue with Geometry/Geography static methods when using delimited identifiers for data types.
- Fixed return type of SQRT() function to float.
- Fixed issues with assignment of multibyte characters to local variable of type nchar/nvarchar.
- Added empty string handling in ISNUMERIC(), to ensure compatibility with T-SQL behavior.
- Fixed DATALENGTH() to return correct byte length value for various datatypes and their UDTs.
- Fixed DATETIME to VARBINARY CAST function.
- Fixed precision/scale in SELECT INTO while using with GROUP BY clause.
- Fixed an issue of protocol error in TDS stream due to Numeric/Decimal overflow.
- Fixed issues with CTE logic and missing intermediate levels in the output of FOR JSON AUTO clause.
- Fixed an issue related to LIKE operator where ESCAPE character does not work as expected when ESCAPE character comes after wildcard in pattern.
- Fixed an issue which occurs when parameter of type binary(8) passed from .NET driver.

### Babelfish for Aurora PostgreSQL 5.3

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.6. For more
information about the improvements in Aurora PostgreSQL 17.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
5.3 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 5.3.0, November 25, 2025

**New Features**

- Added support for boolean operators and prefix term grammer in T-SQL CONTAINS clause for [Full-Text Search](../AuroraUserGuide/babelfish-postgres-fulltextsearch.md "../AuroraUserGuide/babelfish-postgres-fulltextsearch.md") .
- Added support for Z-M flags for Point Instances and Z, M, HasZ and HasM functions for [GEOMETRY and GEOGRAPHY datatypes](../AuroraUserGuide/babelfish-geospatial.md "../AuroraUserGuide/babelfish-geospatial.md") .
- Added support for sp_helplogins stored procedure.
- Enabled Support for weak binding views with few limitations.

**Critical enhancements**

- Fixed an issue during TDS Reset Connection in certain situations.
- Fixed an issue in GroupAD where login with mapped user should not have access to guest privileges.
- Improved the performance of queries using the ISNUMERIC() function in predicates.
- Added support for queries to choose index scan for queries having predicates comparing numeric and integer data types.

**High Priority stability enhancements**

- Fixed overflow checks in all arithmetic operations with money, smallmoney being a higher precedence operand.
- Fixed the output datatype for all arithmetic operations involving smallmoney and bit.
- Fixed behavior of certain math functions like CEIL, ROUND, POWER and FLOOR for money and smallmoney data types.
- Fixed issue with connection crash during arithmetic operations on smallmoney and int.
- Fixed overflow checks in all arithmetic/numeric operations with smallmoney/money being a operand.
- Fixed an issue with DATENAME() to gives correct value of TZOFFSET part.
- Handling for CHAR()/NCHAR() function to return NULL instead of errors when values are out of range.
- Handling for NCHAR() function to accept inputs that can be converted to integers.
- Fixed PATINDEX() function to correctly finds patterns at the end of text and handles wildcard searches accurately.
- Enabled index usage for Accent Sensitive / Insensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match with following conditions:
  - For Accent Sensitive collation, user needs to create index from TSQL endpoint : CREATE INDEX <index_name> ON <table_name>(<column_name>)
  - For Accent Insensitive collation, user needs to create index from PSQL endpoint: CREATE INDEX <index_name> ON <schema_name>.<table_name>(sys.remove_accents_internal_using_cache(<column_name>))

- Fixed an issue where TRY_CAST and TRY_CONVERT was incorrectly rounding decimal values when casting to integer types, instead of truncating the fractional part.
- Fixed precision and scale for arithmetic operations between money/smallmoney and numeric and for money/smallmoney in union operators.
- Fixed precision and scale handling for case expressions and nested case expressions when with numeric and smallmoney/money branches.
- Fixed precision and scale handling for numeric expressions with sub-expressions as money/smallmoney or fixed length datatypes.
- Fixed an issue with handling of bigint and money/smallmoney multiplication operations.
- Fixed an issue where money/smallmoney multiplications was incorrectly truncating decimal values in result, insetad of rounding the fractional part.
- Fixed precision and scale handling for SUM()/AVG() functions with money/smallmoney and fixed length datatypes.
- Fixed an issue with airthetic operations between numeric variable and fixed length variables.
- Fixed precision and scale handling for aggregate functions with numeric.
- Fixed an issue with babelfish connections restored during ZDP.
- Fixed an issue with RESET ALL command from postgres endpoint.
- Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
- Fixed an issue where parallelism won't be used for pltsql RETURN expression.
- Fixed permission denied issue in cross-db table valued functions.
- Added handling for empty input string handling in date and time datatypes.
- Fixed precision and scale handling for money/smallmoney while creating objects, casts, variables and user defined datatypes using it.
- Fixed an issue to preserve Timezone information during casting from string to datetimeoffset.
- Fixed Function QUOTENAME() to return correct strings.
- Added handling of binary arguments for Len() function.
- Fixed the precision and scale for aggregate function that have \*(all columns) as input.
- Fixed an issue for CaseExpr with numeric computation.
- Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'.
- Fixed rounding off issue during storing datetime datatype. Existing users should run the following query from TSQL endpoint to update their existing data: UPDATE <table_name> SET <datetime_col> = CAST(CAST(<datetime_col> as VARCHAR) AS DATETIME).
- Fixed datetime comparison in Babelfish to match TSQL behavior of treating datetime values within 0.00333 second precision as equal.

**Additional improvements and enhancements**

- Fixed an issue with OBJECT_DEFINITION function where it was trucating the output after 4000 characters.
- Fixed the database_principals view to display the correct SID.
- Handle PostgreSQL reserved keywords in Cursor operations.
- Added support for sys.server_permissions, sys.sql_logins views and sys.fn_varbintohexsubstring system function.
- Fixed an issue while adding a column with default value which resulted in an error.
- Fixed an issue with INSERT ... EXECUTE statements in stored procedures related to nested levels.

### Babelfish for Aurora PostgreSQL 5.2

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.5. For more
information about the improvements in Aurora PostgreSQL 17.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
5.2 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 5.2.0, June 30, 2025

**New Features**

- Added CREATE OR ALTER VIEW / ALTER VIEW syntax support in Babelfish with few limitations.
- Added support of Transact-SQL UNPIVOT operators for Babelfish.
- Added support for `STDimension`, `STDisjoint`,
  `STIntersects`, `STIsClosed`,
  `STIsEmpty`, `STIsValid` Geospatial functions.
- Added support for collation in partition functions and partitioning columns.
- Enabled support for scripting logins in SSMS for Babelfish.
- Added support for column_list in T-SQL CONTAINS clause for Full-Text Search.

**Critical enhancements**

- Added “+” and “-” operator for varbinary.
- Added new GUCs `babelfishpg_tsql.apg_enable_correlated_scalar_transform` and
  `babelfishpg_tsql.apg_enable_subquery_cache` to control subquery optimization
  features in Babelfish. The new GUCs are `ON` by default.
- Added support for larger server hello messages during SSL handshake by segmenting them
  into 4096 byte packets.
- Added support for CAST from VARBINARY to DATETIME in Babelfish.
- Added support for altering user/role in Babelfish GroupAD for fixed database roles’
  member.
- Allow CREATE schema in Babelfish GroupAD via fixed db roles’ membership.
- Fixed an issue with object ownership. Any new object created by a user from TDS endpoint
  will now be owned by schema owner as opposed to previous behaviour where the current user
  always owned the new object.
- Added handling for default schema name for procedure in Group-AD session, when Table
  Valued Parameter is used as an argument of a procedure.

**High Priority stability enhancements**

- Fixed logic to adjust precision and scale in Numeric Multiplication and Division.
- Fixed computation of precision and scale for User defined types.
- Fixed computation of precision and scale for constant with value 0.
- Fixed the issue `wrong varnullingrels` error could be reported incorrectly
  after subquery transformation.
- Fixed the issue that alter table will cause follow up cascade drop command failed to drop the
  database contain this table.
- Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
- Restrict dropping of Babelfish login via PG port, if a BBF login has mapped users in all
  three master, tempdb and msdb databases.
- Fixed permission denied error in Babelfish Group AD while using table variables in some
  scenarios.
- Fixed bug which prevented enable/disable all triggers on tables.
- Fixed incorrect conversion from integers to varbinary datatype.
- Fixed Casting and Conversion from Float to Varchar datatype.
- Fixed suser_sname() function to handle the null inputs.
- Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
- Fixed issue which causes incorrect result in arithmetic operations which results in
  numeric/decimal type.
- Fixed an issue which caused communication link failure with DROP LOGIN/USER/ROLE [public].
- Restricted dropping of system procedures and views from dbo schema.
- Fixed an issue in round() function to ensure return types match input argument types.
- Transfer nullability and identity properties of columns in SELECT INTO statement to new
  table. These properties are only transferred if there is a single table in FROM clause of
  SELECT INTO and the column isn't part of expression in select into statements target
  list.

**Additional improvements and
enhancements**

- Fixed JSON string formatting to prevent improper backslash escaping in “FOR
  JSON” output with json_query function.
- Fixed an issue where guest user could create objects in guest schema.
- Fixed PUBLIC role attributes in system views.
- Fixed sys.objects catalog to correctly populate unique constraints metadata.
- Fixed issue when max length of a RPC character based parameter is 0.
- Restricted members of fixed database role db_ddladmin from creating schema for database
  principals that it isn't a member of.
- Restricted members of fixed database role db_ddladmin from creating schema for database
  principals that it isn't a member of.
- Added an escape hatch for the INLINE option in CREATE FUNCTION statements, defaulting to
  “strict” mode for proper error handling.
- Fixed the entry in `babelfish_schema_permissions` which was getting
  overridden if there were table and procedure with the same name.
- Fixed an errors while fetching the object definition of tsql objects due to handling of few
  nodes in `sys.tsql_get_expr`.
- Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
- Fixed some cases of object resolution inside stored procedures, functions and trigger.
- Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
- Improved index name handling in Babelfish by preserving the original index name in the
  catalog, making it visible in catalog views like sys.indexes. It also adds support for
  renaming existing indexes using sp_rename to preserve and display their original names.
- Fixed a crash in `resolve_numeric_typmod_from_exp` for aggregate functions using \*(all
  columns).

### Babelfish for Aurora PostgreSQL 5.1

This release of Aurora Babelfish is provided with Aurora PostgreSQL 17.4. For more
information about the improvements in Aurora PostgreSQL 17.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
5.1 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 5.1.1, June 03, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

**Critical stability enhancements**

- Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 5.1.0, May 01,

2025

**New Features**

- Added support for fixed database-level roles `db_securityadmin`,
  `db_accessadmin`, `db_ddladmin`, `db_datareader` and
  `db_datawriter`. T-SQL users can be added to these fixed database roles.
- Added support for fixed server-level roles `securityadmin` and
  `dbcreator`. T-SQL logins can be added to these fixed server roles.
- Added support for adding T-SQL users to `db_owner` fixed database-level
  role. This T-SQL will have privileges similar to the database owner.

For more information about relevant permission management and access control settings for these new features in Babelfish, see [Managing permissions and access control in Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish-permissions.md "../AuroraUserGuide/babelfish-permissions.md").

**Critical enhancements**

- Fixed issues with `Convert` function when converting from
  `string` to `date`, `datetimeoffset`,
  `datetime2`, `datetime`, `smalldatetime` and
  `time`.
- Fixed the issue of parameter declarations containing # characters not being handled
  correctly.
- Supported `SET IDENTITY_INSERT` for three part relation references.
- Fixed an issue with the `HASHBYTES` function to ensure correct behavior
  when processing `NVARCHAR` argument.
- Fixed the issue of `CREATE PARTITION SCHEME` not supporting “PRIMARY”
  syntax.
- Fixed the issue of UPDATE/DELETE of table variable query in a function getting
  incorrectly rejected with multi-table FROM clause.
- Restricted user defined @@function from being mapped to sys function.
- Fixed the issue of comparison with empty double quoted string raised the error about
  “zero-length delimited identifier”.
- Fixed a crash which could occur in rare situations when using temporary tables with
  certain orphaned catalog entries.
- Fixed an issue where trigger gets dropped when dropping a column in a table.
- Improved performance of queries having join between `TABLE_CONSTRAINTS` and
  `KEY_COLUMN_USAGE` view in the INFORMATION_SCHEMA schema.
- Fixed inconsistent formatting issue with `Convert` function when converting
  MONEY datatype with value 0 to string datatypes.
- Fixed formatting issues in `CAST` from `MONEY` to
  `CHAR/VARCHAR`.
- Fixed the issue where `SELECT...INTO` with `MIN` and
  `MAX` aggregations on `MONEY` columns lost type
  information.
- Implement modulo operator for `MONEY` type.
- Added cleanup of stale parameters and configs in case of connection pooling.
- Added comprehensive cursor state cleanup to avoid stale data in case of connection
  pooling.
- Fixed a issue with `IDENTITY` columns not being recognized during
  `DML` statements using `OUTPUT` and `WHERE`
  clause.

**High Priority stability enhancements**

- Fixed an issue where @@function in `UPDATE SET` clause causes syntax
  error.
- Fixed dynamic evaluation of @local_var for `UPDATE ... SET` @local_var and
  `SELECT` command.
- Fixed an issue with `sp_columns_100` where partial data could be returned
  if @fUsePattern = 0 is used.
- Fixed an issue where local variables may not be updated correct when query involves
  manipulation of local variable.
- Improved the general performance of parsing.
- Fixed an issue with system function `OPENJSON`.
- Fixed the incorrect result datatype of `UNION` involving `MONEY`
  type.
- Fixed offset when using “AT TIME ZONE” with DATETIME2 datatype conversion with
  convert() function in non-default local timezone setting.
- Fixed an issue where batches containing cross database queries looks up the objects in
  incorrect database.
- Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions
  for week and quarter `Datepart`.
- Fixed an issue where `sys.column_property` may return incorrect results for
  ordinal property of a column.
- Fixed “`AT TIME ZONE`” issue near DST change time with
  `DATETIME2` datatype conversion.
- Fixed behavior of queries which use `sys.Db_id()`function which returned
  empty rows in enforced parallel mode.

**Additional improvements and enhancements**

- Optimize execution the `plan` extension by removing unnecessary
  `CAST` functions.
- `EXECUTE`() on a double-quoted string no longer raises an error.
- Fixed an error when using functions as column default values on temp tables.
- Fixed an error in `OPENJSON` function call to allow parse on long
  `JSON` string.
- Fixed issue where dropping member from role does not work after restoring
  Babelfish database.
- Fixed the alias issue when if exists co-exists with a “=” alias in select list.
- Restricted declaring the reserved @@function names as common variables.
- Corrected the implementation of procedure `sp_helpuser` for database roles
  where `sp_helpuser` should show roles only when explicitly specified.
- Fixed an issue where smalldatetime type and date type can more flexibly access data
  through index.
- Fixed an issue with system procedure `fn_listextendedproperty`.
- Fixed the use of table-valued parameters as arguments in procedures. Previously, you
  had to specify the type name of the table-valued parameter when calling the procedure, now
  it is optional.
- Fixed precision and scale when common type of `CASE` expression is
  `NUMERIC` / `DECIMAL` .
- Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for
  already terminated connections.
- Fixed an issue where a login with mapped database user still has guest user
  privileges.
- Fixed an issue where transaction count changes after execution of some system
  functions.
- Fixed issue where `Datepart` functions were having different output based
  on the GUC `timezone`.

## Babelfish for Aurora PostgreSQL 4.x versions

###### Version updates

- [Babelfish for Aurora PostgreSQL 4.8](#AuroraBabelfish.Updates.48X "#AuroraBabelfish.Updates.48X")
- [Babelfish for Aurora PostgreSQL 4.7](#AuroraBabelfish.Updates.47X "#AuroraBabelfish.Updates.47X")
- [Babelfish for Aurora PostgreSQL 4.6](#AuroraBabelfish.Updates.46X "#AuroraBabelfish.Updates.46X")
- [Babelfish for Aurora PostgreSQL 4.5](#AuroraBabelfish.Updates.45X "#AuroraBabelfish.Updates.45X")
- [Babelfish for Aurora PostgreSQL 4.4](#AuroraBabelfish.Updates.44X "#AuroraBabelfish.Updates.44X")
- [Babelfish for Aurora PostgreSQL 4.3](#AuroraBabelfish.Updates.43X "#AuroraBabelfish.Updates.43X")
- [Babelfish for Aurora PostgreSQL 4.2](#AuroraBabelfish.Updates.42X "#AuroraBabelfish.Updates.42X")
- [Babelfish for Aurora PostgreSQL 4.1](#AuroraBabelfish.Updates.41X "#AuroraBabelfish.Updates.41X")
- [Babelfish for Aurora PostgreSQL 4.0](#AuroraBabelfish.Updates.40X "#AuroraBabelfish.Updates.40X")

### Babelfish for Aurora PostgreSQL 4.8

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.11. For more
information about the improvements in Aurora PostgreSQL 16.11, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
4.8 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 4.8.0, December 18, 2025

**New Features**

- Enabled support of SELECT TOP N PERCENT clause with few [limitations](../AuroraUserGuide/babelfish-compatibility.tsql.md "../AuroraUserGuide/babelfish-compatibility.tsql.md").
- Enabled support of sys.time_zone_info view.
- Enabled support for Values clause and subquery columns in SELECT list in FOR JSON AUTO functionality.

**Critical enhancements**

- Fixed STPointFromText() and Point() to throw error on NULL arguments.
- Fixed issues with Geometry/Geography to (var)char and (var)binary conversions.
- Fixed function definition of STPointFromText(), STPointFromText(), STAsText() and STAsBinary().
- Fixed bytea to Geometry/Geography conversion for Point instance.
- Fixed handling of STPointFromText, STGeomFromText, STLineFromText for incorrect binary input.
- ASCII function returns incorrect results with argument type as Binary and Varbinary.
- Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.
- Fixed crashes and intermittent errors caused by memory corruption when a parameter is assigned to itself.

**High Priority stability enhancements**

- Fixed an issue where user can not be dropped when permissions have been granted to that user.
- Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
- Fixed precision/scale for Round() function.
- Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.
- Fixed an issue where errors in pg_cron job was leading to server reboot.

**Additional improvements and enhancements**

- Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.
- Fixed an issue which resets the escape hatch settings to default with the first temp table creation.
- Fixed Datetime and Varbinary to Binary CAST functions.
- Fixed an issue to match CONVERT and CAST function return values for Binary type.
- Fixed INSERT INTO table DEFAULT VALUES for domain types, by setting appropriate function return type.
- Fixed an issue where running multi-Statement table valued function throws syntax error if the database name contains a symbol for an operator.
- Fixed REVOKE permission execution to correctly handle overlapping schema-level and object-level grants.
- Enabled support for the NULL/NOT NULL syntax in ALTER TABLE ALTER COLUMN statements.
- Add identifier delimiters to handle special characters in login and role names.
- Fixed indexes that were created on top of T-SQL temporary tables to correctly follow transaction semantics.
- Fixed various mathematical functions for Money and smallmoney datatype.
- Fixed an issue to persist column level permissions when modifying views using ALTER VIEW.
- Enabled support to allow alter on functions with dependent weak schemabinding views.
- Fixed issue with Geometry/Geography static methods when using delimited identifiers for data types.
- Fixed return type of SQRT() function to float.
- Fixed issues with assignment of multibyte characters to local variable of type nchar/nvarchar.
- Added empty string handling in ISNUMERIC(), to ensure compatibility with T-SQL behavior.
- Fixed DATALENGTH() to return correct byte length value for various datatypes and their UDTs.
- Fixed DATETIME to VARBINARY CAST function.
- Fixed precision/scale in SELECT INTO while using with GROUP BY clause.
- Fixed an issue of protocol error in TDS stream due to Numeric/Decimal overflow.
- Fixed issues with CTE logic and missing intermediate levels in the output of FOR JSON AUTO clause.
- Fixed an issue related to LIKE operator where ESCAPE character does not work as expected when ESCAPE character comes after wildcard in pattern.
- Fixed an issue which occurs when parameter of type binary(8) passed from .NET driver.

### Babelfish for Aurora PostgreSQL 4.7

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.10. For more
information about the improvements in Aurora PostgreSQL 16.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
4.7 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.7.0, November 25, 2025](#AuroraBabelfish.Updates.470 "#AuroraBabelfish.Updates.470")

#### Aurora Babelfish release 4.7.0, November 25, 2025

**New Features**

- Added support for Z-M flags for Point Instances and Z, M, HasZ and HasM functions for [GEOMETRY and GEOGRAPHY datatypes.](../AuroraUserGuide/babelfish-geospatial.md "../AuroraUserGuide/babelfish-geospatial.md")
- Added support for sp_helplogins stored procedure.
- Enabled Support for weak binding views with few limitations.

**Critical enhancements**

- Fixed an issue during TDS Reset Connection in certain situations.
- Fixed an issue in GroupAD where login with mapped user should not have access to guest privileges.
- Improved the performance of queries using the ISNUMERIC() function in predicates.
- Added support for queries to choose index scan for queries having predicates comparing numeric and integer data types.

**High Priority stability enhancements**

- Fixed overflow checks in all arithmetic operations with money, smallmoney being a higher precedence operand.
- Fixed the output datatype for all arithmetic operations involving smallmoney and bit.
- Fixed behavior of certain math functions like CEIL, ROUND, POWER and FLOOR for money and smallmoney data types.
- Fixed issue with connection crash during arithmetic operations on smallmoney and int.
- Fixed overflow checks in all arithmetic/numeric operations with smallmoney/money being a operand.
- Fixed an issue with DATENAME() to gives correct value of TZOFFSET part.
- Handling for CHAR()/NCHAR() function to return NULL instead of errors when values are out of range.
- Handling for NCHAR() function to accept inputs that can be converted to integers.
- Fixed PATINDEX() function to correctly finds patterns at the end of text and handles wildcard searches accurately.
- To use Index for Accent Sensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match, user needs to create index from TSQL endpoint : CREATE INDEX <index_name> ON <table_name>(<column_name>). To use Index for Accent Insensitive collation for LIKE operator when the pattern is EXACT or PREFIX or INFIX match, user needs to create index from PSQL endpoint: CREATE INDEX <index_name> ON <schema_name>.<table_name>(sys.remove_accents_internal_using_cache(<column_name>)).
- Fixed an issue where TRY_CAST and TRY_CONVERT was incorrectly rounding decimal values when casting to integer types, instead of truncating the fractional part.
- Fixed precision and scale for arithmetic operations between money/smallmoney and numeric and for money/smallmoney in union operators.
- Fixed precision and scale handling for case expressions and nested case expressions when with numeric and smallmoney/money branches.
- Fixed precision and scale handling for numeric expressions with sub-expressions as money/smallmoney or fixed length datatypes.
- Fixed an issue with handling of bigint and money/smallmoney multiplication operations.
- Fixed an issue where money/smallmoney multiplications was incorrectly truncating decimal values in result, insetad of rounding the fractional part.
- Fixed precision and scale handling for nested case expressions with numeric and money/smallmoney as their branches.
- Fixed precision and scale handling for SUM()/AVG() functions with money/smallmoney and fixed length datatypes.
- Fixed an issue with airthetic operations between numeric variable and fixed length variables.
- Fixed precision and scale handling for aggregate functions with numeric.
- Fixed an issue with babelfish connections restored during ZDP.
- Fixed an issue with RESET ALL command from postgres endpoint.
- Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
- Fixed an issue where parallelism won't be used for pltsql RETURN expression.
- Fixed permission denied issue in cross-db table valued functions.
- Added Handling for empty input string handling in date and time datatypes.
- Fixed precision and scale handling for money/smallmoney while creating objects,casts,variables and user defined datatypes using it.
- Fixed an issue to preserve Timezone information during casting from string to datetimeoffset.
- Fixed Function QUOTENAME() to return correct strings.
- Added handling of binary arguments for Len() function.
- Fixed the precision and scale for aggregate function that have \*(all columns) as input.
- Fixed an issue for CaseExpr with numeric computation.
- Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'.
- Fixed rounding off issue during storing datetime datatype. Existing users should run the following query from TSQL endpoint to update their existing data: UPDATE <table_name> SET <datetime_col> = CAST(CAST(<datetime_col> as VARCHAR) AS DATETIME).
- Fixed datetime comparison in Babelfish to match TSQL behavior of treating datetime values within 0.00333 second precision as equal.

**Additional improvements and enhancements**

- Fixed an issue with OBJECT_DEFINITION function where it was trucating the output after 4000 characters.
- Fixed the database_principals view to display the correct SID.
- Handle PostgreSQL reserved keywords in Cursor operations.
- Add full support for sys.server_permissions, sys.sql_logins views and sys.fn_varbintohexsubstring system function.
- Fixed an issue while adding a column with default value which resulted in an error.
- Fixed an issue with INSERT ... EXECUTE statements in stored procedures related to nested levels.

### Babelfish for Aurora PostgreSQL 4.6

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.9. For more
information about the improvements in Aurora PostgreSQL 16.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
4.6 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.6.0, June 30, 2025](#AuroraBabelfish.Updates.46X "#AuroraBabelfish.Updates.46X")

#### Aurora Babelfish release 4.6.0, June 30, 2025

**New Features**

- Added CREATE OR ALTER VIEW / ALTER VIEW syntax support in Babelfish with few limitations.
- Added support of Transact-SQL UNPIVOT operators for Babelfish.
- Added support for `STDimension`, `STDisjoint`,
  `STIntersects`, `STIsClosed`,
  `STIsEmpty`, `STIsValid` Geospatial functions.
- Added support for collation in partition functions and partitioning columns.
- Enabled support for scripting logins in SSMS for Babelfish.

**Critical enhancements**

- Added “+” and “-” operator for varbinary.
- Added new GUCs `babelfishpg_tsql.apg_enable_correlated_scalar_transform` and
  `babelfishpg_tsql.apg_enable_subquery_cache` to control subquery optimization
  features in Babelfish. The new GUCs are ON by default.
- Added support for larger server hello messages during SSL handshake by segmenting them
  into 4096 byte packets.
- Added support for CAST from VARBINARY to DATETIME in Babelfish.
- Added support for altering user/role in Babelfish GroupAD for fixed database roles’
  member.
- Allow CREATE schema in Babelfish GroupAD via fixed db roles’ membership.
- Fixed an issue with object ownership. Any new object created by a user from TDS endpoint
  will now be owned by schema owner as opposed to previous behaviour where the current user
  always owned the new object.
- Added handling for default schema name for procedure in Group-AD session, when Table
  Valued Parameter is used as an argument of a procedure.

**High Priority stability enhancements**

- Fixed logic to adjust precision and scale in Numeric Multiplication and Division.
- Fixed computation of precision and scale for User defined types.
- Fixed computation of precision and scale for constant with value 0.
- Fixed the issue `wrong varnullingrels` error could be reported incorrectly
  after subquery transformation.
- Fixed the issue that alter table will cause follow up cacade drop cmd failed to drop the
  database contain this table.
- Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
- Restrict dropping of Babelfish login via PG port, if a BBF login has mapped users in all
  three master, tempdb and msdb databases.
- Fixed permission denied error in Babelfish Group AD while using table variables in some
  scenarios.
- Fixed bug which prevented enable/disable all triggers on tables.
- Fixed incorrect conversion from integers to varbinary datatype.
- Fixed Casting and Conversion from Float to Varchar datatype.
- Fixed suser_sname() function to handle the null inputs.
- Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
- Fixed issue which causes incorrect result in arithmetic operations which results in
  numeric/decimal type.
- Fixed an issue which caused communication link failure with DROP LOGIN/USER/ROLE [public].
- Restricted dropping of system procedures and views from dbo schema.
- Fixed an issue in round() function to ensure return types match input argument types.
- Transfer nullability and identity properties of columns in SELECT INTO statement to new
  table. These properties are only transferred if there is a single table in FROM clause of
  SELECT INTO and the column isn't part of expression in select into statements target
  list.

**Additional improvements and
enhancements**

- Fixed JSON string formatting to prevent improper backslash escaping in “FOR
  JSON” output with json_query function.
- Fixed CONVERT function to allow empty string values to be converted to `datetime` format.
- Fixed an issue where guest user could create objects in guest schema.
- Fixed PUBLIC role attributes in system views.
- Fixed sys.objects catalog to correctly populate unique constraints metadata.
- Fixed issue when max length of a RPC character based parameter is 0.
- Restricted members of fixed database role db_ddladmin from creating schema for database
  principals that it isn't a member of.
- Restricted members of fixed database role db_ddladmin from creating schema for database
  principals that it isn't a member of.
- Added an escape hatch for the INLINE option in CREATE FUNCTION statements, defaulting to
  “strict” mode for proper error handling.
- Fixed the entry in `babelfish_schema_permissions` which was getting
  overridden if there were table and procedure with the same name.
- Fixed an errors while fetching the object definition of tsql objects due to handling of few
  nodes in `sys.tsql_get_expr`.
- Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
- Fixed some cases of object resolution inside stored procedures, functions and trigger.
- Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
- Improved index name handling in Babelfish by preserving the original index name in the
  catalog, making it visible in catalog views like sys.indexes. It also adds support for
  renaming existing indexes using sp_rename to preserve and display their original names.
- Fixed a crash in resolve_numeric_typmod_from_exp for aggragate functions using \*(all
  columns).

### Babelfish for Aurora PostgreSQL 4.5

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.8. For more
information about the improvements in Aurora PostgreSQL 16.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
4.5 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.5.1, June 03, 2025](#AuroraBabelfish.Updates.451 "#AuroraBabelfish.Updates.451")
- [Aurora Babelfish release 4.5.0, April 08,
  2025](#AuroraBabelfish.Updates.450 "#AuroraBabelfish.Updates.450")

#### **Aurora Babelfish release 4.5.1, June 03, 2025**

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

**Critical stability enhancements**

- Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 4.5.0, April 08,

2025

**New Features**

- Added support for fixed database-level roles `db_securityadmin`,
  `db_accessadmin`, `db_ddladmin`, `db_datareader` and
  `db_datawriter`. T-SQL users can be added to these fixed database roles.
- Added support for fixed server-level roles `securityadmin` and
  `dbcreator`. T-SQL logins can be added to these fixed server roles.
- Added support for adding T-SQL users to `db_owner` fixed database-level
  role. This T-SQL will have privileges similar to the database owner.

For more information about relevant permission management and access control settings for these new features in Babelfish, see [Managing permissions and access control in Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish-permissions.md "../AuroraUserGuide/babelfish-permissions.md").

**Critical enhancements**

- Fixed the issue of parameter declarations containing # characters not being handled
  correctly.
- Supported `SET IDENTITY_INSERT` for three part relation references.
- Fixed an issue with the `HASHBYTES` function to ensure correct behavior
  when processing `NVARCHAR` argument.
- Fixed the issue of `CREATE PARTITION SCHEME` not supporting “PRIMARY”
  syntax.
- Fixed the issue of UPDATE/DELETE of table variable query in a function getting
  incorrectly rejected with multi-table FROM clause.
- Restricted user defined @@function from being mapped to sys function.
- Fixed the issue of comparison with empty double quoted string raised the error about
  “zero-length delimited identifier”.
- Fixed a crash which could occur in rare situations when using temporary tables with
  certain orphaned catalog entries.
- Fixed an issue where trigger gets dropped when dropping a column in a table.
- Improved performance of queries having join between `TABLE_CONSTRAINTS` and
  `KEY_COLUMN_USAGE` view in the INFORMATION_SCHEMA schema.
- Fixed inconsistent formatting issue with `Convert` function when converting
  MONEY datatype with value 0 to string datatypes.
- Fixed formatting issues in `CAST` from `MONEY` to
  `CHAR/VARCHAR`.
- Fixed the issue where `SELECT...INTO` with `MIN` and
  `MAX` aggregations on `MONEY` columns lost type
  information.
- Implement modulo operator for `MONEY` type.
- Added Cleanup of stale parameters and configs in case of connection pooling.
- Added comprehensive cursor state cleanup to avoid stale data in case of connection
  pooling.
- Fixed a issue with `IDENTITY` columns not being recognized during
  `DML` statements using `OUTPUT` and `WHERE`
  clause.

**High Priority stability enhancements**

- Fixed an issue where @@function in `UPDATE SET` clause causes syntax
  error.
- Fixed dynamic evaluation of @local_var for `UPDATE ... SET` @local_var and
  `SELECT` command.
- Fixed an issue with `sp_columns_100` where partial data could be returned
  if @fUsePattern = 0 is used.
- Fixed an issue where local variables may not be updated correct when query involves
  manipulation of local variable.
- Improved the general performance of antlr parsing.
- Fixed an issue with system function `OPENJSON`.
- Fixed the incorrect result datatype of `UNION` involving `MONEY`
  type.
- Fixed offset when using “`AT TIME ZONE`” with `DATETIME2`
  datatype conversion with convert() function in non-default local timezone setting.
- Improved string functions to handle a wider range of datatypes.
- Fixed an issue where batches containing cross database queries looks up the objects in
  incorrect database.
- Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions
  for week and quarter `Datepart`.
- Fixed an issue where `sys.column_property` may return incorrect results for
  ordinal property of a column.
- Fixed “`AT TIME ZONE`” issue near DST change time with
  `DATETIME2` datatype conversion.
- Fixed behavior of queries which use `sys.Db_id()` function which returned
  empty rows in enforced parallel mode.

**Additional improvements and enhancements**

- Optimize execution the `plan` extension by removing unnecessary
  `CAST` functions.
- `EXECUTE`() on a double-quoted string no longer raises an error.
- Fixed an error when using functions as column default values on temp tables.
- Fixed an error in `OPENJSON` function call to allow parse on long
  `JSON` string.
- Fixed issue where dropping member from role does not work after restoring
  Babelfish database.
- Fixed the alias issue when if exists co-exists with a “=” alias in select list.
- Restricted declaring the reserved @@function names as common variables.
- Corrected the implementation of procedure `sp_helpuser` for database roles
  where `sp_helpuser` should show roles only when explicitly specified.
- Fixed an issue where smalldatetime type and date type can more flexibly access data
  through index.
- Fixed an issue with system procedure `fn_listextendedproperty`.
- Fixed the use of table-valued parameters as arguments in procedures. Previously, you
  had to specify the type name of the table-valued parameter when calling the procedure, now
  it is optional.
- Fixed precision and scale when common type of `CASE` expression is
  `NUMERIC` / `DECIMAL` .
- Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for
  already terminated connections.
- Fixed an issue where a login with mapped database user still has guest user
  privileges.
- Fixed an issue where transaction count changes after execution of some system
  functions.
- Fixed issue where `Datepart` functions were having different output based
  on the GUC `timezone`.

### Babelfish for Aurora PostgreSQL 4.4

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.6. For more information about the improvements in Aurora PostgreSQL 16.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 4.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.4.2,
  June 24, 2025](#AuroraBabelfish.Updates.442 "#AuroraBabelfish.Updates.442")
- [Aurora Babelfish release 4.4.1, January 20,
  2025](#AuroraBabelfish.Updates.441 "#AuroraBabelfish.Updates.441")
- [Aurora Babelfish release 4.4.0, December 27, 2024](#AuroraBabelfish.Updates.440 "#AuroraBabelfish.Updates.440")

#### Aurora Babelfish release 4.4.2,

June 24, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 4.4.1, January 20,

2025

**High priority stability enhancements**

- Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 4.4.0, December 27, 2024

###### _New features_

- Added support for `ALTER FUNCTION` syntax.
- Added support for view usage for `PIVOT` operator .
- Added `pgaudit` extension support with Babelfish.
- Added support of XML method `.EXIST()` for XML Datatypes.
- Enabled support of Geospatial data types in data migration via DMS for Babelfish under
  PostgreSQL endpoint.
- Enabled user to create database with specific collations. For more information, see
  [Collation supported at database level in Babelfish](../AuroraUserGuide/babelfish-collations.md#babelfish-collations.database-level "../AuroraUserGuide/babelfish-collations.md#babelfish-collations.database-level").
- Enabled support of `sys.sp_reset_connection` stored procedure to reset connection.
- Enabled cross-database references of objects (tables/views/functions) in views.
- Enabled support of `sys.dm_os_sys_info` view to provides information about the instance like
  `server_start_time` and `ms_ticks`.
- Enabled support of user connection and network packet size information in
  `sys.configurations` view.
- Enabled support of correlated subquery transformation for more scenarios. For more information, refer to Limitations section in
  [Improving Babelfish query performance using subquery transformation](../AuroraUserGuide/babelfish-correlated-subquery.md#babelfish-corsubquery-transformation "../AuroraUserGuide/babelfish-correlated-subquery.md#babelfish-corsubquery-transformation") .

###### _High priority stability enhancements_

- Fixed date functions to take into account the timezone setting.
- Improved error handling behavior for `relation does not exist` and
  `column does not exist` errors.
- Fixed `sp_tables` stored procedure to correctly handle three-part object names across
  databases to retrieve correct database name during linked servers usage.
- Fixed an issue to enable database owner login to explore database objects in SSMS.
- Fixed `sp_tables` stored procedure to return correct result when @table_name parameter has
  square brackets around underscore (\_).
- Fixed an issue where individual login active directory authentication used to throw error
  of pg_ad_mapping the `plugin` extension pointer not initialized.
- Fixed an issue where index creation could fail if the table is created using SELECT INTO
  syntax.
- Fixed an permission issue with cross-database function calls.
- Enabled Grant on schema to takes effect correctly on future objects created in that schema
  by any of the schema’s authorized users.
- Fixed an issue to pick correct collation for prepared statements.
- Fixed an issue to have foreign key constraint check work correctly when column is created
  using non-default collation.
- Enabled the bcp queries to run with the `pgaudit` extension enabled.
- Fixed an issue to insert correct value in the table having identity column.
- Fixed an issue to have correct identity sequence value when bcp / SqlBulkCopy / insert
  bulk are used with `keep identity values` mode.

###### _Additional improvements and enhancements_

- Fixed the issue with Kill command which still left few sessions running after the command.
- Fixed the issue of `sys.identity_columns` view was wrongly returning more entries than it
  should.
- Fixed the issue of CASE statement and MIN/MAX functions related to error of string size
  not being defined or using explicit cast.
- Fixed an issue with `ISNUMERIC` function to return correct result for nvarchar/varchar
  parameters.
- Fixed the issue of CASE statement not working correctly when branch expression is of
  NVARCHAR type.
- Fixed behavior of CONCAT() and CONCAT_WS() functions for multibyte characters and to work
  with atleast 2 and 3 arguments respectively.
- Fixed an issue to allow ALTER COLUMN with type char for Temp Table.
- Fixed an issue in CONVERT function to make it work consistently with BINARY and VARBINARY
  types in Babelfish.
- Fixed the issue of inconsistent output from select query with FOR XML PATH clause.
- Fixed an issue to rethrow correct TSQL error code.
- Fixed behaviour of STRING_AGG() function for input containing multibyte characters.
- Fixed an issue where wrong overloaded variant of regexp_replace is called during restore.
- Fixed cast from sys.varchar to TIME type.
- Enabled use of nvarchar(max) as output parameter in procedure.
- Fixed an issue of missing brackets while declaring the variables in the definition of
  procedure.

### Babelfish for Aurora PostgreSQL 4.3

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.4. For more information about the improvements in Aurora PostgreSQL 16.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 4.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.3.2,
  July 11, 2025](#AuroraBabelfish.Updates.432 "#AuroraBabelfish.Updates.432")
- [Aurora Babelfish release 4.3.1, January 02,
  2025](#AuroraBabelfish.Updates.431 "#AuroraBabelfish.Updates.431")
- [Aurora Babelfish release 4.3.0, September 30, 2024](#AuroraBabelfish.Updates.430 "#AuroraBabelfish.Updates.430")

#### Aurora Babelfish release 4.3.2,

July 11, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 4.3.1, January 02,

2025

**High priority stability enhancements**

- Fixed an issue where individual login active directory authentication used to throw error
  of `pg_ad_mapping` the `plugin` extension pointer not initialized.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

**Additional improvements and enhancements**

- Fixed an issue where reserved keyword `PRIMARY` caused syntax errors when used as a column
  name or alias in DML and DDL statements.

#### Aurora Babelfish release 4.3.0, September 30, 2024

###### New Features

- Added support for Partitioning in Babelfish. For more information, see
  [Understanding partitioning in Babelfish](../AuroraUserGuide/babelfish-partition.md "../AuroraUserGuide/babelfish-partition.md").
- Support system functions `CHARINDEX()`, `PATINDEX()` and `REPLACE()` for Babelfish non
  deterministic collations.
- Enabling support for `STContains`, `STEquals`, `STArea` the `PostGIS` extension functions for geospatial
  datatypes.

###### Security enhancements

- Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
- Fixed an issue with `sys.database_principals` view where it was showing metadata related to
  all the users irrespective of privileges of server principal.

###### High Priority stability enhancements

- Fixed an issue with information_schema.tables returning incorrect table_name.
- Fixed an issue where less than operator gives incorrect results for binary data types.
- Fixed inconsistency with OIDs of triggers in `OBJECT_ID()` function and `sys.objects` view.
- Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is
  installed.

###### Additional improvements and enhancements

- Fixed behavior of `TRIM()`, `LTRIM()`, `RTRIM()`, `LEFT()`, and `RIGHT()` functions for input
  containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
- Improved performance of like operator with non deterministic collations.
- Fixed an issue where search patch may be incorrect when database name and/or schema name
  contains special characters in quotes.
- Fixed difference in behavior in Babelfish and TSQL for `UPPER()` and `LOWER()` functions with
  multibyte characters and appropriate argument and return types.
- Added Support of `WITH RECOMPILE` for Transact-SQL stored procedures and for ALTER PROCEDURE
  clause.
- The `sp_tables` procedure now allows you to use the `%`
  wildcard character in the `@table_qualifier` parameter. This makes it
  easier to search for tables by matching patterns in the table names.
- Fixed difference in behavior in Babelfish and TSQL for `STUFF()` , `SUBSTRING()` and `TRANSLATE()`
  functions with multibyte characters and appropriate argument and return types.
- Updated error message for `GRANT`, `REVOKE`, `DENY` statements.
- Fixed behavior of `REVERSE()`, `REPLACE()`, and `REPLICATE()` functions for input containing
  multibyte characters, by returning result with appropriate datatype based on argument
  datatype.
- Fixed output of `SPACE()` function for non-positve input argument.
- Improved memory handling when using BCP on a table with indexes.
- Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
- Fixed a data type resolve issue with union clause.
- Fixed an error message for `SUBSTRING()` function when the number of arguments are not
  appropriate.
- Fixed an issue when comment comes with the column name.
- Fixed an issue with `sys.server_principals` view to show `public` role entry.
- Added support for `WITHIN GROUP` clause for `STRING_AGG()` function.
- Fixed DDL export issue for database with SSMS.
- Added support for new vector extensions like `halfvec` and sparsevec which got introduced in
  version 0.7 of pgvector.
- Added support to show windows group membership in T-SQL function `IS_MEMBER()`.

### Babelfish for Aurora PostgreSQL 4.2

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.3. For more information about the improvements in Aurora PostgreSQL 16.3, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 4.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.2.3,
  July 17, 2025](#AuroraBabelfish.Updates.423 "#AuroraBabelfish.Updates.423")
- [Aurora Babelfish release 4.2.2, January 23,
  2025](#AuroraBabelfish.Updates.422 "#AuroraBabelfish.Updates.422")
- [Aurora Babelfish release 4.2.1,
  September 27, 2024](#AuroraBabelfish.Updates.421 "#AuroraBabelfish.Updates.421")
- [Aurora Babelfish release 4.2.0,
  August 8, 2024](#AuroraBabelfish.Updates.420 "#AuroraBabelfish.Updates.420")

#### Aurora Babelfish release 4.2.3,

July 17, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 4.2.2, January 23,

2025

**High priority stability enhancements**

- Fixed an issue where individual login active directory authentication used to throw error
  of pg_ad_mapping the `plugin` extension pointer not initialized.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 4.2.1,

September 27, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.2.0,

August 8, 2024

###### New features

- Introduced support for PostgreSQL native logical replication so that users can replicate and synchronize individual tables from a source to one or more recipients
  using a publisher and subscriber model.
- Added support for Blue/Green deployments with Babelfish. You can now use Amazon RDS Blue/Green Deployments, to make and test database changes before
  implementing them in a production environment. For more information, see
  [Overview of Amazon RDS Blue/Green Deployments for Aurora](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md").
- Added support for GRANT/REVOKE .. ON SCHEMA .. in Babelfish.
  - Following permissions are supported based on the object types.
    - Scalar function permissions – EXECUTE.
    - Table-valued function permissions – EXECUTE.
    - Stored procedure permissions – EXECUTE.
    - Table permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
    - View permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.

  - CASCADE isn't supported with Grant/Revoke on Schema.
  - GRANT/REVOKE OPTION FOR .. on SCHEMA isn't supported in Babelfish.
  - GRANT/REVOKE inside CREATE SCHEMA isn't supported in Babelfish.

- Added support for `sys.login_token` and `sys.user_token` system views.
- Added support for LIKE clause for some AI collations. For more information, see
  [Deterministic and nondeterministic collations in Babelfish](../AuroraUserGuide/babelfish-collations.md#babelfish-collations.deterministic-nondeterministic "../AuroraUserGuide/babelfish-collations.md#babelfish-collations.deterministic-nondeterministic").
- Added support to Group Security based Active Directory authentication. Users can manage their workloads without provisioning individual logins with enhanced security posture. For more information, see
  [Setting up kerberos authentication using Active Directory security groups for Babelfish](../AuroraUserGuide/babelfish-kerberos-securityad.md "../AuroraUserGuide/babelfish-kerberos-securityad.md").
- Added support of CTE and JOIN for PIVOT operator.
- Support ALTER syntax for Proc.
- Support renaming of a SQL Server database.
- Support unique constraints on nullable columns. Escape hatch `babelfishpg_tsql.escape_hatch_unique_constraint` has been deprecated.
- Introduced support to correlated subquery transform and cache for enhancement of query performance by transforming scalar correlated subquery into join query, or caching the
  subquery result set and reduce duplicate subquery re-executions when transformation is not possible. For more information, see
  [Improving Aurora PostgreSQL query performance using subquery transformation](../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation "../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation") .

###### Critical stability enhancements

- Fixed issue producing syntax error with delimited column alias without preceding whitespace.
- Creating a user for a login is blocked when its login is already a member of sysadmin.
- Fixed the column type of the T-SQL views to use nvarchar(max).
- Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.
- Fixed casting issue from geometry to `varbinary` or `byte` datatype when `SRID` is zero.
- Fixed the issue of indexes not being used in case of queries comparing numeric and integer data types.

###### High priority stability enhancements

- Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
- Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
- Fixed issue of crash under certain conditions while executing bulk copy.
- Crash in `handle_where_clause_restargets_right()`.
- Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
- Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
- Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
- Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
- Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases.
- Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
- Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
- Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
- Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.
- Fixed an issue where some queries with ORDER BY clause did not use primary key indexes.
- Fixed an issue with CREATE/ALTER PROCEDURE command that could cause server restart if procedure name contains special white characters.
- Fixed an issue where query may return incorrect result when predicate involves SCOPE_IDENTITY().

###### Additional improvements and enhancements

- Fixed memory leak in decimal (numeric) conversion for BCP import.
- Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
- Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
- Added restriction on dropping of Babelfish extensions for all users except admin role.
- Prevent partial upgrades of Babelfish extensions.
- sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
- DDL scripting of indexes or constraints will now include correct ordering with columns.
- Fixed an error to allow referencing a `#tmp table` in a nested procedure through OBJECT_ID() clause.
- Fixed an issue to avoid error when dropping trigger created on temp table.
- Made an enhancement to allow table variables having a name longer than 63 characters.
- Fixed issue with --schema-only and --data-only options of BabelfishDump utilities.
- Fixed issue with BabelfishDump utility where it wasn't able to dump extended properties.
- Fixed issue of fully qualified column reference doesn't work in PIVOT aggregate function.
- Fixed an error to allow alter procedure from PG endpoint.
- Blocked SET/RESET role statements execution from TDS endpoint.
- Changed the default behavior of the full-text search GUC to have the feature turned `OFF` by default. You can set the GUC to `ignore` to use FTS features.

### Babelfish for Aurora PostgreSQL 4.1

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.2. For more
information about the improvements in Aurora PostgreSQL 16.2, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 4.1 adds several new features, enhancements, and fixes. For more information
about Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.1.4,
  July 30, 2025](#AuroraBabelfish.Updates.414 "#AuroraBabelfish.Updates.414")
- [Aurora Babelfish release 4.1.3,
  February 02, 2025](#AuroraBabelfish.Updates.413 "#AuroraBabelfish.Updates.413")
- [Aurora Babelfish release 4.1.2,
  October 7, 2024](#AuroraBabelfish.Updates.412 "#AuroraBabelfish.Updates.412")
- [Aurora Babelfish release 4.1.1,
  June 20, 2024](#AuroraBabelfish.Updates.411 "#AuroraBabelfish.Updates.411")
- [Aurora Babelfish release 4.1.0,
  April 29, 2024](#AuroraBabelfish.Updates.410 "#AuroraBabelfish.Updates.410")

#### Aurora Babelfish release 4.1.4,

July 30, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 4.1.3,

February 02, 2025

**High priority stability enhancements**.

- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.

#### Aurora Babelfish release 4.1.2,

October 7, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.1.1,

June 20, 2024

###### High priority stability enhancements

- Optimized performance for Create and Drop Databases for
  Babelfish.
- Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 4.1.0,

April 29, 2024

###### New features

- Babelfish introduces support for two spatial data types Geometry and
  Geography to store and manipulate spatial data under a limited scope. For more
  information, see [Babelfish supports Geospatial data types](../AuroraUserGuide/babelfish-geospatial.md "../AuroraUserGuide/babelfish-geospatial.md").
- Allowing `SELECT FOR JSON AUTO` support in Babelfish.
- Support the ability to perform vector similarity search using the
  `pgvector` extension through Babelfish. The ability to use
  `HNSW` and `IVFLAT` indexes is also supported. For
  more information, see [Using pgvector in Babelfish](../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-pgvector "../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-pgvector").
- Support the ability to access Amazon Machine Learning services such as Amazon
  Comprehend, Amazon Sagemaker and Amazon Bedrock through `aws_ml`
  extension. For more information, see [Using Amazon Aurora machine learning with Babelfish](../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-ml "../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-ml").
- Support T-SQL procedure `sp_procedure_params_100_managed`.
- CONTAINS clause used in Full Text Search will also support for special
  characters and single digit in search condition. For more information, see
  [Full Text Search in Babelfish](../AuroraUserGuide/babelfish-postgres-fulltextsearch.md "../AuroraUserGuide/babelfish-postgres-fulltextsearch.md").

###### Critical stability enhancements

- Fixed an issue in Object Explorer Database enumeration with SSMS version
  19.2.
- Fixed an issue that caused error during Selecting data from variable
  `NVARCHAR(MAX)`, `VARCHAR(MAX)`,
  `VARBINARY(MAX)` with large length strings.
- Fixed blank space padding related issue in char datatype for multibyte
  characters.
- Fixed performance issue of enumerating tables and views in SSMS Object
  Explorer.
- Fixed default column collation to match server collation handled through
  `babelfishpg_tsql.server_collation_name` for some system views.
  List of fixed system views are `sys.check_constraints`,
  `sys.data_spaces`, `sys.default_constraints`,
  `sys.dm_exec_connections`, `sys.foreign_keys`,
  `sys.key_constraints`, `sys.stats`,
  `sys.syscolumns`, `sys.sysforeignkeys`,
  `sys.sysprocesses`, `sys.system_objects`,
  `sys.table_types`, `sys.tables`,
  `sys.types`, `sys.views` and
  `sys.xml_indexes`.
- Restrict creation of functions/procedures with the same name in
  Babelfish.

###### High priority stability enhancements

- Improved performance for system procedure
  `sp_tablecollations_100`.
- Fixed an issue with major version upgrades where views contains cast from
  string literal to binary type.
- Fixed a bug where parallel worker was unable to fetch the logical database
  name.
- Fixed the performance issue of comparing `date` to
  `datetime`.

###### Additional improvements and enhancements

- Fixed an issue on duplicate `object_id` in
  `sys.all_objects` after major version upgrade.
- Fixed an issue in `CAST` functions for `Binary` to
  `Varchar` and `Rowversion` to
  `Varchar`.
- Fixed an issue with insert into statement execution with table variable when
  table variable did not exist.
- Fixed an issue where input hex string being converted to type binary did not
  have the correct data length.
- Fixed an issue with mixed casing error in `sp_columns_100`.
- Fixed a crash in Table Variable lookup after `TVP` execution via
  `TDS RPC SPExecuteSQL`.
- Support embedded whitespace in multi-character comparison operators.
- Support operators adjacent to `@@variables` without separating
  whitespace.
- Fixed a crash with procedure execution if procedure deletes itself or rolls
  back the transaction which created the procedure.
- Support for the `AS` keyword in `CREATE` function for
  all cases.
- Support expressions in `SELECT...OFFSET...FETCH` clauses.
- Support `SET TRAN ISOLATION LEVEL` syntax.
- Support floating-point notation without exponent.
- Support comparison operators `!<` and `!>`.
- Support for `DROP INDEX schema.table.index` and `DROP INDEX
index ON schema.table` syntax.

### Babelfish for Aurora PostgreSQL 4.0

This release of Aurora Babelfish is provided with Aurora PostgreSQL 16.1. For more information about the improvements in Aurora PostgreSQL 16.1, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 4.0 (version 4.0 is build on top of version 3.4) adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 4.0.4,
  August 4, 2025](#AuroraBabelfish.Updates.404 "#AuroraBabelfish.Updates.404")
- [Aurora Babelfish release 4.0.3, February 5, 2025](#AuroraBabelfish.Updates.403 "#AuroraBabelfish.Updates.403")
- [Aurora Babelfish release 4.0.2,
  September 17, 2024](#AuroraBabelfish.Updates.402 "#AuroraBabelfish.Updates.402")
- [Aurora Babelfish release 4.0.1,
  June 24, 2024](#AuroraBabelfish.Updates.401 "#AuroraBabelfish.Updates.401")
- [Aurora Babelfish release 4.0.0,
  January 31, 2024](#AuroraBabelfish.Updates.400 "#AuroraBabelfish.Updates.400")

#### Aurora Babelfish release 4.0.4,

August 4, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 4.0.3, February 5, 2025

**High priority stability enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 4.0.2,

September 17, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 4.0.1,

June 24, 2024

###### High priority stability enhancements

- Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
- Optimized performance for Create and Drop Databases for Babelfish.
- Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 4.0.0,

January 31, 2024

###### New features

- Limited support for Full Text Search in Babelfish. For more information, see
  [Full Text Search in Babelfish](../AuroraUserGuide/babelfish-postgres-fulltextsearch.md "../AuroraUserGuide/babelfish-postgres-fulltextsearch.md").
- Added support for creating INSTEAD OF Triggers on Views.
- Changed the default Babelfish migration mode from single database to multiple databases.

###### Security enhancements

- Fixed security issues with handling of TSQL login and users.

###### High priority stability enhancements

- Fixed a regression issue where update-join with inserted table in trigger procedure causes `result relation must be a regular relation` error.
- Fixed the issue where querying `information_schema` for type U and V was earlier giving different results in Babelfish.
- Fixed an issue to avoid blocking of vacuum progress when using temp tables in certain situations.

###### Additional improvements and enhancements

- Fixed an issue with principal name in `pg_stat_gssapi` catalog view.
- Fixed issue in functions `parsename`, `session_context` and `sp_set_session_context` when using with non-default server collation.

###### Recommendations

- We recommend you to upgrade from Aurora PostgreSQL version 14 to 15 and then from version 15 to 16. Currently, direct upgrade from version 14 to 16 isn't supported and it fails with an error.

## Babelfish for Aurora PostgreSQL 3.x versions (includes some deprecated versions)

###### Version updates

- [Babelfish for Aurora PostgreSQL 3.12](#AuroraBabelfish.Updates.312X "#AuroraBabelfish.Updates.312X")
- [Babelfish for Aurora PostgreSQL 3.11](#AuroraBabelfish.Updates.311 "#AuroraBabelfish.Updates.311")
- [Babelfish for Aurora PostgreSQL 3.10](#AuroraBabelfish.Updates.310 "#AuroraBabelfish.Updates.310")
- [Babelfish for Aurora PostgreSQL 3.9](#AuroraBabelfish.Updates.39X "#AuroraBabelfish.Updates.39X")
- [Babelfish for Aurora PostgreSQL 3.8](#AuroraBabelfish.Updates.38X "#AuroraBabelfish.Updates.38X")
- [Babelfish for Aurora PostgreSQL 3.7](#AuroraBabelfish.Updates.37X "#AuroraBabelfish.Updates.37X")
- [Babelfish for Aurora PostgreSQL 3.6](#AuroraBabelfish.Updates.36X "#AuroraBabelfish.Updates.36X")
- [Babelfish for Aurora PostgreSQL 3.5](#AuroraBabelfish.Updates.35X "#AuroraBabelfish.Updates.35X")
- [Babelfish for Aurora PostgreSQL 3.4](#AuroraBabelfish.Updates.34X "#AuroraBabelfish.Updates.34X")
- [Babelfish for Aurora PostgreSQL 3.3](#AuroraBabelfish.Updates.33X "#AuroraBabelfish.Updates.33X")
- [Babelfish for Aurora PostgreSQL 3.2](#AuroraBabelfish.Updates.32X "#AuroraBabelfish.Updates.32X")
- [Babelfish for Aurora PostgreSQL 3.1 (Deprecated)](#AuroraBabelfish.Updates.31X "#AuroraBabelfish.Updates.31X")

### Babelfish for Aurora PostgreSQL 3.12

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.15. For more
information about the improvements in Aurora PostgreSQL 15.15, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
3.12 adds several enhancements and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

#### Aurora Babelfish release 3.12.0, December 18, 2025

**Critical enhancements**

- Active snapshots when system catalogs are being updated while ResetTempTableNamespace in TDS.

**High Priority stability enhancements**

- Added support for the planner to choose index scan for queries having predicates comparing numeric and money/smallmoney data types.
- Fixed an issue where rollback to savepoint in some cases failed to send the correct transaction state token to the client, causing subsequent operations in the transaction to fail.

**Additional improvements and enhancements**

- Fixed an issue to allow concurrent UPDATE operations with OUTPUT clauses.

### Babelfish for Aurora PostgreSQL 3.11

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.14. For more
information about the improvements in Aurora PostgreSQL 15.14, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
3.11 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.11.0, November 25, 2025](#AuroraBabelfish.Updates.3110 "#AuroraBabelfish.Updates.3110")

#### Aurora Babelfish release 3.11.0, November 25, 2025

**Critical enhancements**

- Fixed an issue during TDS Reset Connection in certain situations
- Added support to let index scan used in case of queries having predicates comparing numeric and integer data types

**High Priority stability enhancements**

- Fixed an issue with RESET ALL command from postgres endpoint
- Fixed an issue with response packets when reading large nvarchar(max) data, which could cause ArgumentOutOfRangeException with .NET driver.
- Fixed an issue where parallelism won't be used for pltsql RETURN expression
- Fixed an issue to preserve Timezone information during casting from string to datetimeoffset
- Fixed a crash in queries using 'FOR JSON AUTO' and 'JSON PATH'

**Additional improvements and enhancements**

- Fixed an issue while adding a column with default value which resulted in an error

### Babelfish for Aurora PostgreSQL 3.10

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.13. For more
information about the improvements in Aurora PostgreSQL 15.13, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
3.10 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.10.0, June 30, 2025](#AuroraBabelfish.Updates.3100 "#AuroraBabelfish.Updates.3100")

#### Aurora Babelfish release 3.10.0, June 30, 2025

**Critical enhancements**

- Added support for larger server hello messages during SSL handshake by segmenting them
  into 4096 byte packets.
- Added support for CAST from VARBINARY to DATETIME in Babelfish.
- Added handling for default schema name for procedure in Group-AD session, when Table
  Valued Parameter is used as an argument of a procedure.
- Added “+” and “-” operator for varbinary.

**High Priority stability enhancements**

- Fixed PIVOT operator to gracefully handle NULL entries in pivot column.
- Fixed issue with result having incorrect scale in numeric/decimal addition and subtraction.
- Fixed issue which causes incorrect result in arithmetic operations which results in
  numeric/decimal type.
- Fixed an issue in round() function to ensure return types match input argument types.

**Additional improvements and
enhancements**

- Fixed the entry in `babelfish_schema_permissions` which was getting
  overridden if there were table and procedure with the same name.
- Fixed an errors while fetching the object definition of tsql objects due to handling of few
  nodes in `sys.tsql_get_expr`.
- Fixed the logic for numeric/decimal datatype typmod resolution in outer/inner queries.
- Fixed case expression when one of the branch is NUMERIC and other is of EXACT NUMERIC.
- Fixed a crash in `resolve_numeric_typmod_from_exp` for aggregate functions using \*(all
  columns).

### Babelfish for Aurora PostgreSQL 3.9

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.12. For more
information about the improvements in Aurora PostgreSQL 15.12, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
3.9 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.9.1, June 03, 2025](#AuroraBabelfish.Updates.391 "#AuroraBabelfish.Updates.391")
- [Aurora Babelfish release 3.9.0, April 08,
  2025](#AuroraBabelfish.Updates.390 "#AuroraBabelfish.Updates.390")

#### Aurora Babelfish release 3.9.1, June 03, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

**Critical stability enhancements**

- Added support for larger server hello messages during SSL handshake.

#### Aurora Babelfish release 3.9.0, April 08,

2025

**Critical enhancements**

- Fixed an issue where trigger gets dropped when dropping a column in a table.
- Improved performance of queries having join between `TABLE_CONSTRAINTS` and
  `KEY_COLUMN_USAGE` view in the INFORMATION_SCHEMA schema.
- Fixed inconsistent formatting issue with `Convert` function when converting
  MONEY datatype with value 0 to string datatypes.
- Fixed formatting issues in `CAST` from `MONEY` to
  `CHAR/VARCHAR`.
- Fixed the issue where `SELECT...INTO` with `MIN` and
  `MAX` aggregations on `MONEY` columns lost type
  information.
- Implement modulo operator for `MONEY` type.
- Added Cleanup of stale parameters and configs in case of connection pooling.
- Added comprehensive cursor state cleanup to avoid stale data in case of connection
  pooling.
- Fixed a issue with `IDENTITY` columns not being recognized during
  `DML` statements using `OUTPUT` and `WHERE`
  clause.

**High Priority stability enhancements**

- Fixed an issue with system function `OPENJSON`.
- Fixed the incorrect result datatype of `UNION` involving `MONEY`
  type.
- Fixed offset when using “`AT TIME ZONE`” with `DATETIME2`
  datatype conversion with convert() function in non-default local timezone setting.
- Improved string functions to handle a wider range of datatypes.
- Fixed an issue where batches containing cross database queries looks up the objects in
  incorrect database.
- Fixed behavior of `DATEDIFF`() and `DATEDIFF_BIG`() functions
  for week and quarter `Datepart`.
- Fixed an issue where `sys.column_property` may return incorrect results for
  ordinal property of a column.
- Fixed “`AT TIME ZONE`” issue near DST change time with
  `DATETIME2` datatype conversion.
- Fixed behavior of queries which use `sys.Db_id()` function which returned
  empty rows in enforced parallel mode.

**Additional improvements and enhancements**

- Fixed an issue where smalldatetime type and date type can more flexibly access data
  through index.
- Fixed an issue with system procedure `fn_listextendedproperty`.
- Fixed the use of table-valued parameters as arguments in procedures. Previously, you
  had to specify the type name of the table-valued parameter when calling the procedure, now
  it is optional.
- Fixed precision and scale when common type of `CASE` expression is
  `NUMERIC` / `DECIMAL` .
- Fixed an issue where `sys.dm_exec_sessions` may have abandoned entries for
  already terminated connections.
- Fixed an issue where a login with mapped database user still has guest user
  privileges.
- Fixed an issue where transaction count changes after execution of some system
  functions.
- Fixed issue where `Datepart` functions were having different output based
  on the GUC `timezone`.

### Babelfish for Aurora PostgreSQL 3.8

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.10. For more
information about the improvements in Aurora PostgreSQL 15.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
3.8 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.8.2,
  June 24, 2025](#AuroraBabelfish.Updates.382 "#AuroraBabelfish.Updates.382")
- [Aurora Babelfish release 3.8.1, January 20,
  2025](#AuroraBabelfish.Updates.380 "#AuroraBabelfish.Updates.380")
- [Aurora Babelfish release 3.8.0, December
  27, 2024](#AuroraBabelfish.Updates.380 "#AuroraBabelfish.Updates.380")

#### Aurora Babelfish release 3.8.2,

June 24, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 3.8.1, January 20,

2025

**High priority stability enhancements**

- Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 3.8.0, December

27, 2024

###### _New features_

- Added support for `ALTER FUNCTION` syntax.
- Enabled the `pgaudit` extension support with Babelfish.
- Enabled user to create view on statement with `PIVOT` operator.
- Enabled support of `sys.sp_reset_connection` stored procedure to reset connection.
- Enabled cross-database references of objects (tables/views/functions) in views.

###### _High priority stability enhancements_

- Fixed date functions to take into account the timezone setting.
- Improved error handling behavior for `relation does not exist` and `column does not
exist` errors.
- Fixed `sp_tables` stored procedure to correctly handle three-part object names across
  databases to retrieve correct database name during linked servers usage.
- Fixed an issue to enable database owner login to explore database objects in
  SSMS.
- Fixed `sp_tables` stored procedure to return correct result when @table_name parameter
  has square brackets around underscore (\_).
- Fixed an issue where individual login active directory authentication used to throw
  error of `pg_ad_mapping` the `plugin` extension pointer not initialized.
- Fixed an issue where index creation could fail if the table is created using `SELECT
INTO` syntax.
- Fixed an permission issue with cross-database function calls.
- Enabled Grant on schema to takes effect correctly on future objects created in that
  schema by any of the schema’s authorized users.
- Fixed an issue to insert correct value in the table having identity column.
- Fixed an issue to have correct identity sequence value when bcp or SqlBulkCopy or insert
  bulk are used with `keep identity values` mode.

###### _Additional improvements and enhancements_

- Fixed the issue with Kill command which still left few sessions running after the
  command.
- Fixed the issue of `sys.identity_columns` view was wrongly returning more entries than
  it should.
- Fixed the issue of CASE statement and MIN/MAX functions related to error of string
  size not being defined or using explicit cast.
- Fixed an issue with ISNUMERIC function to return correct result for nvarchar/varchar
  parameters.
- Fixed the issue of CASE statement not working correctly when branch expression is of
  NVARCHAR type.
- Fixed behavior of CONCAT() and CONCAT_WS() functions for multibyte characters and to
  work with atleast 2 and 3 arguments respectively.
- Fixed an issue to allow ALTER COLUMN with type char for Temp Table.
- Fixed an issue in CONVERT function to make it work consistently with BINARY and
  VARBINARY types in Babelfish.
- Fixed the issue of inconsistent output from select query with FOR XML PATH
  clause.
- Fixed an issue to rethrow correct TSQL error code.
- Fixed behaviour of `STRING_AGG()` function for input containing multibyte
  characters.
- Fixed an issue where wrong overloaded variant of `regexp_replace` is called during
  restore.
- Fixed cast from `sys.varchar` to TIME type.

### Babelfish for Aurora PostgreSQL 3.7

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.8. For more information about the improvements in Aurora PostgreSQL 15.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.7 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.7.2,
  July 11, 2025](#AuroraBabelfish.Updates.372 "#AuroraBabelfish.Updates.372")
- [Aurora Babelfish release 3.7.1, January 02,
  2025](#AuroraBabelfish.Updates.371 "#AuroraBabelfish.Updates.371")
- [Aurora Babelfish release 3.7.0, September 30, 2024](#AuroraBabelfish.Updates.370 "#AuroraBabelfish.Updates.370")

#### Aurora Babelfish release 3.7.2,

July 11, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 3.7.1, January 02,

2025

**High priority stability enhancements**

- Fixed an issue where individual login active directory authentication used to throw error
  of pg_ad_mapping the `plugin` extension pointer not initialized.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 3.7.0, September 30, 2024

###### _New Features_

- Enabling support for `STContains`, `STEquals`, `STArea` the `PostGIS` extension functions for geospatial
  datatypes.

###### Security enhancements

- Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
- Fixed an issue with `sys.database_principals` view where it was showing metadata related to
  all the users irrespective of privileges of server principal.

###### High Priority stability enhancements

- Fixed an issue with `information_schema.tables` returning incorrect table_name.
- Fixed an issue where less than operator gives incorrect results for binary data types.
- Fixed inconsistency with OIDs of triggers in `OBJECT_ID()` function and `sys.objects` view.
- Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is
  installed.

###### Additional improvements and enhancements

- Fixed behavior of `TRIM()`, `LTRIM()`, `RTRIM()`, `LEFT()`, and `RIGHT()` functions for input
  containing multibyte characters, by returning result with appropriate datatype based on argument datatype.
- Improved performance of like operator with non deterministic collations.
- Fixed an issue where search patch may be incorrect when database name and/or schema name
  contains special characters in quotes.
- Fixed difference in behavior in Babelfish and TSQL for `UPPER()` and `LOWER()` functions with
  multibyte characters and appropriate argument and return types.
- The `sp_tables` procedure now allows you to use the `%`
  wildcard character in the `@table_qualifier` parameter. This makes it
  easier to search for tables by matching patterns in the table names.
- Fixed difference in behavior in Babelfish and TSQL for `STUFF()` , `SUBSTRING()` and `TRANSLATE()`
  functions with multibyte characters and appropriate argument and return types.
- Updated error message for GRANT/REVOKE/DENY statements.
- Fixed behavior of `REVERSE()`, `REPLACE()`, and `REPLICATE()` functions for input containing
  multibyte characters, by returning result with appropriate datatype based on argument
  datatype.
- Fixed output of `SPACE()` function for non-positve input argument.
- Improved memory handling when using BCP on a table with indexes.
- Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
- Fixed a data type resolve issue with union clause.
- Fixed an error message for `SUBSTRING()` function when the number of arguments are not
  appropriate.
- Fixed an issue when comment comes with the column name.
- Fixed an issue with `sys.server_principals` view to show `public` role entry.
- Fixed DDL export issue for database with SSMS.
- Added support to show windows group membership in T-SQL function `IS_MEMBER()`.

### Babelfish for Aurora PostgreSQL 3.6

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.7. For more information about the improvements in Aurora PostgreSQL 15.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.6.3,
  July 17, 2025](#AuroraBabelfish.Updates.363 "#AuroraBabelfish.Updates.363")
- [Aurora Babelfish release 3.6.2, January 23, 2025](#AuroraBabelfish.Updates.362 "#AuroraBabelfish.Updates.362")
- [Aurora Babelfish release 3.6.1,
  September 27, 2024](#AuroraBabelfish.Updates.361 "#AuroraBabelfish.Updates.361")
- [Aurora Babelfish release 3.6.0,
  August 8, 2024](#AuroraBabelfish.Updates.360 "#AuroraBabelfish.Updates.360")

#### Aurora Babelfish release 3.6.3,

July 17, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 3.6.2, January 23, 2025

**High priority stability enhancements**

- Fixed an issue where individual login active directory authentication used to throw error
  of pg_ad_mapping the `plugin` extension pointer not initialized.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 3.6.1,

September 27, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.6.0,

August 8, 2024

###### New features

- Introduced support for PostgreSQL native logical replication so that users can replicate and synchronize individual tables from a source to one or more recipients
  using a publisher and subscriber model.
- Added support for Blue/Green deployments with Babelfish. You can now use Amazon RDS Blue/Green Deployments, to make and test database changes before
  implementing them in a production environment. For more information, see
  [Overview of Amazon RDS Blue/Green Deployments for Aurora](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md").
- Added support for GRANT/REVOKE .. ON SCHEMA .. in Babelfish.
  - Following permissions are supported based on the object types.
    - Scalar function permissions – EXECUTE.
    - Table-valued function permissions – EXECUTE.
    - Stored procedure permissions – EXECUTE.
    - Table permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.
    - View permissions – DELETE, INSERT, REFERENCES, SELECT, UPDATE.

  - CASCADE isn't supported with Grant/Revoke on Schema.
  - GRANT/REVOKE OPTION FOR .. on SCHEMA isn't supported in Babelfish.
  - GRANT/REVOKE inside CREATE SCHEMA isn't supported in Babelfish.

- Added support for `sys.login_token` and `sys.user_token` system views.
- Added support for LIKE clause for some AI collations. For more information, see
  [Deterministic and nondeterministic collations in Babelfish](../AuroraUserGuide/babelfish-collations.md#babelfish-collations.deterministic-nondeterministic "../AuroraUserGuide/babelfish-collations.md#babelfish-collations.deterministic-nondeterministic").
- Added support to Group Security based Active Directory authentication. Users can manage their workloads without provisioning individual logins with enhanced security posture. For more information, see
  [Setting up kerberos authentication using Active Directory security groups for Babelfish](../AuroraUserGuide/babelfish-kerberos-securityad.md "../AuroraUserGuide/babelfish-kerberos-securityad.md").
- Added support of CTE and JOIN for PIVOT operator.
- Support ALTER syntax for Proc.
- Support renaming of a SQL Server database.
- Support unique constraints on nullable columns. Escape hatch `babelfishpg_tsql.escape_hatch_unique_constraint` has been deprecated.

###### Critical stability enhancements

- Fixed issue producing syntax error with delimited column alias without preceding whitespace.
- Creating a user for a login is blocked when its login is already a member of sysadmin.
- Fixed the column type of the T-SQL views to use nvarchar(max).
- Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.
- Fixed casting issue from geometry to `varbinary` or `byte` datatype when `SRID` is zero.
- Fixed the issue of indexes not being used in case of queries comparing numeric and integer data types.

###### High priority stability enhancements

- Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
- Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
- Fixed issue of crash under certain conditions while executing bulk copy.
- Crash in `handle_where_clause_restargets_right()`.
- Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
- Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
- Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
- Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
- Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases.
- Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
- Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
- Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
- Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.
- Fixed an issue where some queries with ORDER BY clause did not use primary key indexes.
- Fixed an issue with CREATE/ALTER PROCEDURE command that could cause server restart if procedure name contains special white characters.
- Fixed an issue where query may return incorrect result when predicate involves SCOPE_IDENTITY().

###### Additional improvements and enhancements

- Fixed memory leak in decimal (numeric) conversion for BCP import.
- Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
- Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
- Added restriction on dropping of Babelfish extensions for all users except admin role.
- Prevent partial upgrades of Babelfish extensions.
- sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
- DDL scripting of indexes or constraints will now include correct ordering with columns.
- Fixed an error to allow referencing a `#tmp table` in a nested procedure through OBJECT_ID() clause.
- Fixed an issue to avoid error when dropping trigger created on temp table.
- Made an enhancement to allow table variables having a name longer than 63 characters.
- Fixed issue with --schema-only and --data-only options of BabelfishDump utilities.
- Fixed issue with BabelfishDump utility where it wasn't able to dump extended properties.
- Fixed issue of fully qualified column reference doesn't work in PIVOT aggregate function.
- Fixed an error to allow alter procedure from PG endpoint.
- Blocked SET/RESET role statements execution from TDS endpoint.

### Babelfish for Aurora PostgreSQL 3.5

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.6. For more information about the improvements in Aurora PostgreSQL 15.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.5.4,
  July 30, 2025](#AuroraBabelfish.Updates.354 "#AuroraBabelfish.Updates.354")
- [Aurora Babelfish release 3.5.3, February 02,
  2025](#AuroraBabelfish.Updates.353 "#AuroraBabelfish.Updates.353")
- [Aurora Babelfish release 3.5.2,
  October 7, 2024](#AuroraBabelfish.Updates.352 "#AuroraBabelfish.Updates.352")
- [Aurora Babelfish release 3.5.1,
  June 20, 2024](#AuroraBabelfish.Updates.351 "#AuroraBabelfish.Updates.351")
- [Aurora Babelfish release 3.5.0,
  April 29, 2024](#AuroraBabelfish.Updates.350 "#AuroraBabelfish.Updates.350")

#### Aurora Babelfish release 3.5.4,

July 30, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 3.5.3, February 02,

2025

**High priority stability enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 3.5.2,

October 7, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.5.1,

June 20, 2024

###### High priority stability enhancements

- Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 3.5.0,

April 29, 2024

###### New features

- Babelfish introduces support for two spatial data types Geometry and Geography to store and manipulate spatial data under a limited scope.
  For more information, see [Babelfish supports Geospatial data types](../AuroraUserGuide/babelfish-geospatial.md "../AuroraUserGuide/babelfish-geospatial.md").
- Allowing `SELECT FOR JSON AUTO` support in Babelfish.
- Support the ability to perform vector similarity search using the `pgvector` extension through Babelfish.
  The ability to use `HNSW` and `IVFLAT` indexes is also supported. For more information, see
  [Using pgvector in Babelfish](../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-pgvector "../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-pgvector").
- Support the ability to access Amazon Machine Learning services such as Amazon Comprehend, Amazon Sagemaker and Amazon Bedrock through
  `aws_ml` extension. For more information, see
  [Using Amazon Aurora machine learning with Babelfish](../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-ml "../AuroraUserGuide/babelfish-postgres-aws-extensions.md#babelfish-postgres-aws-extensions-using-ml").
- Support T-SQL procedure `sp_procedure_params_100_managed`.
- Support creating Instead of Triggers (DML) on SQL Server Views.

###### Critical stability enhancements

- Fixed an issue in Object Explorer Database enumeration with SSMS version 19.2.
- Fixed an issue that caused error during Selecting data from variable `NVARCHAR(MAX)`, `VARCHAR(MAX)`,
  `VARBINARY(MAX)` with large length strings.
- Fixed blank space padding related issue in char datatype for multibyte characters.
- Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
- Fixed default column collation to match server collation handled through `babelfishpg_tsql.server_collation_name`
  for some system views. List of fixed system views are `sys.check_constraints`, `sys.data_spaces`, `sys.default_constraints`,
  `sys.dm_exec_connections`, `sys.foreign_keys`, `sys.key_constraints`, `sys.stats`, `sys.syscolumns`,
  `sys.sysforeignkeys`, `sys.sysprocesses`, `sys.system_objects`, `sys.table_types`, `sys.tables`,
  `sys.types`, `sys.views` and `sys.xml_indexes`.
- Restrict creation of functions/procedures with the same name in Babelfish.

###### High priority stability enhancements

- Improved performance for system procedure `sp_tablecollations_100`.
- Fixed an issue with major version upgrades where views contains cast from string literal to binary type.
- Fixed a bug where parallel worker was unable to fetch the logical database name.
- Fixed the performance issue of comparing `date` to `datetime`.

###### Additional improvements and enhancements

- Fixed an issue on duplicate `object_id` in `sys.all_objects` after major version upgrade.
- Fixed an issue in `CAST` functions for `Binary` to `Varchar` and `Rowversion` to `Varchar`.
- Fixed an issue with insert into statement execution with table variable when table variable did not exist.
- Fixed an issue where input hex string being converted to type binary did not have the correct data length.
- Fixed an issue with mixed casing error in `sp_columns_100`.
- Fixed a crash in Table Variable lookup after `TVP` execution via `TDS RPC SPExecuteSQL`.
- Support embedded whitespace in multi-character comparison operators.
- Support operators adjacent to `@@variables` without separating whitespace.
- Fixed a crash with procedure execution if procedure deletes itself or rolls back the transaction which created the procedure.
- Support for the `AS` keyword in `CREATE` function for all cases.
- Support expressions in `SELECT...OFFSET...FETCH` clauses.
- Support `SET TRANSACTION ISOLATION LEVEL` syntax.
- Support floating-point notation without exponent.
- Support comparison operators `!<` and `!>`.
- Support for `DROP INDEX schema.table.index` and `DROP INDEX index ON schema.table` syntax.
- Fixed issue in functions `parsename`, `session_context` and `sp_set_session_context` when using
  with non-default server collation.

### Babelfish for Aurora PostgreSQL 3.4

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.5. For more information about the improvements in Aurora PostgreSQL 15.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.4.4,
  August 4, 2025](#AuroraBabelfish.Updates.344 "#AuroraBabelfish.Updates.344")
- [Aurora Babelfish release 3.4.3, February 5, 2025](#AuroraBabelfish.Updates.343 "#AuroraBabelfish.Updates.343")
- [Aurora Babelfish release 3.4.2,
  September 17, 2024](#AuroraBabelfish.Updates.342 "#AuroraBabelfish.Updates.342")
- [Aurora Babelfish release 3.4.1,
  June 24, 2024](#AuroraBabelfish.Updates.341 "#AuroraBabelfish.Updates.341")
- [Aurora Babelfish release 3.4.0,
  December 21, 2023](#AuroraBabelfish.Updates.340 "#AuroraBabelfish.Updates.340")

#### Aurora Babelfish release 3.4.4,

August 4, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 3.4.3, February 5, 2025

**High priority stability enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.

#### Aurora Babelfish release 3.4.2,

September 17, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.4.1,

June 24, 2024

###### High priority stability enhancements

- Fixed a crash with execution of pltsql user defined functions.

#### Aurora Babelfish release 3.4.0,

December 21, 2023

###### New features

- Added support for TSQL Isolation Level SERIALIZABLE and REPEATABLE READ with PostgreSQL semantics. For more information, see
  [Transaction Isolation Levels in Babelfish](../AuroraUserGuide/babelfish-transaction.md "../AuroraUserGuide/babelfish-transaction.md").
- Added support for enable or disable triggers.
- Added support for TSQL functions DATETRUNC(), DATE_BUCKET(), SWITCHOFFSET(), TODATETIMEOFFSET(), and AT TIME ZONE clause.
- Added support for TSQL functions TYPE_ID(), TYPE_NAME(), COL_LENGTH(), COL_NAME().
- Added support for DEFAULT keyword in calls to stored procedures and functions.
- Added support for casting DATETIME to numeric types.
- Added support for DBCC CHECKIDENT for ability to reset IDENTITY columns.
- Added support for PRIMARY KEY NOT NULL IDENTITY clause in CREATE/ALTER TABLE.
- Added support for double-quoted strings containing single-quote, embedded double quotes in a double-quoted string, and unquoted string parameters.
- Added support for ALTER AUTHORIZATION syntax to change database owner.
- Added support for TSQL KILL command.
- Added support for TSQL Information_schema.key_column_usage view.
- Added support of variable as input for SET ROWCOUNT and SET DATEFIRST.
- Added support for sys.server_role members and sys.database_permissions catalog views.
- Added support for IDENTITY() function in a SELECT-INTO statement. In Babelfish, a column specified as IDENTITY will always be the last column in the
  new table. Due to this slight difference compared with SQL server, this feature needs to be used with an escape hatch babelfishpg_tsql.escape_hatch_identity_function. User-defined datatypes for IDENTITY() function are not currently supported.
- Added support for ALTER USER...WITH LOGIN syntax.
- Added support for change in transaction isolation from inside transaction block with well defined behavior.
- Added support for casting datetime and smalldatetime to numeric types.
- Added support for PIVOT in limited scope (not supported when used in a view definition, a common table expression, or a join).
- Stored procedure sp_changedbowner is supported.

###### Security enhancements

- Fixed permission issue for view sys.server_principals.

###### Critical stability enhancements

- Fixed an issue where ISNULL function may return incorrect data type.
- Fixed an issue where condition may be evaluated incorrectly for conditional statement like IF.
- Fixed an error "database ... does not exist" that may be observed when parallel query is enforced.
- Fixed handling of table variable or temp table when parallel worker is enforced.
- Fixed unexpected error "lost connection to parallel worker" occurring when parallel worker is enforced.
- Fixed an issue with multiple parentheses in SELECT columns.
- Fixed an issue with handling of column name alias which may cause client to hang if column name alias contains string of length more than 64 bytes, for example, select col as '您对“数据一览“中的车型，颜色，内饰，选装, '.
- Fixed datatype of information_schema_tsql.tables.TABLE_TYPE column.
- Fixed the error - “column ... does not exist” when using table.column with alias defined for table or schema_name.table.column in set clause of update queries.
- Fixed issue of incorrect schema resolution for multiple functions in query statement.
- Fixed an issue for a few variants of DELETE with OUTPUT clause combined with table alias returns an error.
- Fixed performance issue while expanding stored procedures in SSMS Object Explorer.
- Fixed a crash when UNION with NULL values not cast to fixed-length types.
- Fixed SESSION_USER/SYSTEM_USER in SET/PRINT/DECLARE variable assignment returning wrong result/error.
- Fixed issue of blocking of UNIQUE constraint/index on nullable column not implemented consistently.
- Fix a crash with T-SQL OPENQUERY() and four-part object name when T-SQL keywords are used as server name.
- Fixed the issue of update with TOP, OUTPUT and join failing with error ‘unrecognized node type’.
- Fixed the issue of VALUES clause with mixed types gives error containing the clause ‘Please use an explicit CAST or CONVERT’.
- Fixed an issue of different assignments of identity values compared with SQL Server when ORDER BY is used with SELECT INTO statement.
- Fix incorrect schema resolution where multiple functions are called in a single statement.

###### High priority stability enhancements

- Fixed type conversion between varchar and binary datatype with use of proper encoding.
- Fixed an issue where upper/lower case may not be preserved for column name aliases.
- Fixed crash in queries involving money data-type in parallel query mode.
- Fixed failure in MVU with non-default server collation name.
- Fixed the issue of information_schema vs. sys.objects WHERE type IN ('U', 'V') giving different result in Babelfish.
- Fixed issue of sp_columns and sp_columns_100 incorrectly show NULL radix for decimal columns.
- Fixed issue in queries involving sys.format() function in parallel query mode returning error “cannot start subtransactions during a parallel operation”.
- Fixed unexpected error “could not access file "pg_hint_plan": No such file or directory" while using pg_hint_plan in parallel query mode.
- Fixed the issue of getting error ‘duplicate key value violates unique constraint ...' when re-creating the previously dropped view with the same name.

###### Additional improvements and enhancements

- Improved performance for stored procedure sp_describe_undeclared_parameters.
- Fixed performance issue for DATEADD(), DATEDIFF().
- SSMS - Fixed issue of stored procedure takes long time to load in Object Explorer.
- SSMS - Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
- Fixed performance issue after create/upgrade of Babelfish extension by running ANALYZE after Babelfish extension creation and upgrade.
- Fixed the issue of index not used when query has an unnecessary cast to bigint.
- Fixed an issue when stored procedures starting with (sp\_\*) are invoked with a dbo. or sys. prefix.
- Fixed the issue with default_schema_name column of the catalog sys.babelfish_authid_user_ext in case of "guest" user.
- Fixed issue of orphan entries in sys.babelfish_view_def catalog table.
- Fixed an issue with UNION and fixed-length types.
- Fixed performance issue with '+' operator in concatenation operation.
- Fixed performance issue by optimizing use of internal function during index creation and usage in queries.
- Fixed an issue when comparing BIT and VARCHAR types.
- Performance improvements for create/drop database with large number of databases.
- Added sort operators for Babelfish datatypes, so that MAX/MIN aggregation on index column can have a query plan candidate of LIMIT 1 and index scan.
- Fixed nulls order of Babelfish indexes, so that TOP 1 clause on index column can have a query plan candidate of LIMIT 1 and index scan.
- Fixed a crash with SSMS in Table properties dialog box while clicking on Permissions page.
- Restricted use of view as a target with OUTPUT INTO clause.

### Babelfish for Aurora PostgreSQL 3.3

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.4. For more information about the improvements in Aurora PostgreSQL 15.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.3.1,
  November 14, 2024](#AuroraBabelfish.Updates.331 "#AuroraBabelfish.Updates.331")
- [Aurora Babelfish release 3.3.0,
  October 24, 2023](#AuroraBabelfish.Updates.330 "#AuroraBabelfish.Updates.330")

#### Aurora Babelfish release 3.3.1,

November 14, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.3.0,

October 24, 2023

###### New features

- Added support for TSQL functions `HOST_ID()`, `EOMONTH()`, `PARSENAME()` and `SMALLDATETIMEFROMPARTS()` are supported.
- `sys.extended_properties` system catalog view is supported.
- Stored procedures `sp_enum_oledb_providers`, `sp_testlinkedserver`, and `sp_who` are supported.
- Added support for the T-SQL square bracket syntax with the LIKE predicate.
- Added support for `pg_stat_statements` extension with Babelfish. For more information, see
  [pg_stat_statements](../AuroraUserGuide/babelfish-postgres-aws-extensions.md "../AuroraUserGuide/babelfish-postgres-aws-extensions.md").
- Added support for CREATE or ALTER or DROP EXTENSION statements in `sp_execute_postgresql` procedure. For more information, see
  [sp_execute_postgresql](../AuroraUserGuide/Appendix.Babelfish.md "../AuroraUserGuide/Appendix.Babelfish.md").
- Added support for extended properties for object types database, schema, table, view, column, sequence, function, procedure:
  `sys.extended_properties` system catalog view, stored procedures `sp_addextendedproperty`, `sp_updateextendedproperty`, `sp_dropextendedproperty`, and system function `fn_listextendedproperty()`.

###### Critical stability enhancements

- T-SQL trigger can't be performed when function, procedure or trigger of PostgreSQL is in execution stack. If you try to do, the following error message will
  appear: `T-SQL trigger can not be executed from PostgreSQL function, procedure or trigger.`

###### High priority stability enhancements

- Fixed the issue of GETDATE() incorrectly returning different values in the same query.
- Fixed the issue of GETUTCDATE() incorrectly returning time of transaction instead of time of query.

###### Additional improvements and enhancements

- Fixed an issue where SSMS generate script for multiple views, or combining a view with other objects throws an error.
- Fixed an issue to avoid system crash while formatting `datetime` values in the results of FOR JSON or FOR XML.
- Fixed an issue to avoid system crash during table variable cleanup after a runtime error.
- Fixed an issue to avoid system crash when using certain values in nested function calls.
- Fixed an invalid memory access issue while freeing `PLTSQL` functions.
- Fixed a crash in `SqlBulkCopy` when the order of columns is different from the table where it is defined.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed crash in parallel query when `enable_pg_hint` is turned on.
- Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
- Fixed issue where `sp_describe_first_result_set` procedure can return incorrect column order, which could cause BCP to work incorrectly.
- Fixed issue related to loss of decimal digits when converting from REAL to DECIMAL.
- Fixed error handling during the Babelfish upgrade process. Babelfish throws an error if there is a failure during the upgrade.
- Fixed an issue with sender of XML data type to handle `NULL` value where it was causing client to hang.
- Fixed an issue where USE database statement was incorrectly allowed inside the procedure, function or trigger definition.
- Fixed crash while calling T-SQL procedure from PG port when querying `sys.sysobjects`.
- Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY() and remote object
  references with a four-part object names are invoked within the master database.
- Added support for `connect_timeout` option in `sp_serveroption`.
- Fixed a recreation issue with indexed temp tables. You can now create indexed temp tables in Babelfish.
- Fixed an issue with identity columns in procedures.
- Fixed an issue where some catalog entries were not being cleared after use with temp tables, causing occasional error messages.
- Fixed an issue with Babelfish TOP clause that accept number without parenthesis.
- Fixed performance problem for create index or scan index.
- Fixed an issue when using like expression in join on condition failed with nondeterministic error.

### Babelfish for Aurora PostgreSQL 3.2

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.3. For more information about the improvements in Aurora PostgreSQL 15.3, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.2.2,
  November 12, 2024](#AuroraBabelfish.Updates.322 "#AuroraBabelfish.Updates.322")
- [Aurora Babelfish release 3.2.1,
  October 4, 2023](#AuroraBabelfish.Updates.321 "#AuroraBabelfish.Updates.321")
- [Aurora Babelfish release 3.2.0,
  July 13, 2023](#AuroraBabelfish.Updates.320 "#AuroraBabelfish.Updates.320")

#### Aurora Babelfish release 3.2.2,

November 12, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.2.1,

October 4, 2023

###### High priority stability enhancements

- Fixed an issue causing crash when cursor referencing a table variable is already dropped.
- Fixed an issue where queries with UNION ALL, ORDER BY, and multiple joins could cause unavailability.
- Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.
- Fixed an invalid memory access while freeing `PLTSQL` functions.

###### Additional improvements and enhancements

- Fixed an issue to avoid crash by properly handling formatting of datetime values in the results of FOR JSON or FOR XML.
- Fixed a crash in `SqlBulkCopy` when the order of columns is different compared to table defining.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
- Fixed a crash when dropping temp table or table variables during cleanup.
- Fixed an issue with sender of XML data type to handle NULL value where it was causing client to hang.
- Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY()
  and remote object referenced with a four-part object names are invoked within the master database.
- Fixed an issue to avoid failure error message 2600 while attempting to create a temp table.
- Fixed a bug to prevent temp table index recreation issue.

#### Aurora Babelfish release 3.2.0,

July 13, 2023

###### New features

- Supports TIMEFROMPARTS(), DATETIME2FROMPARTS(), ROWCOUNT_BIG(), DATABASE_PRINCIPAL_ID() and CONTEXT_INFO()
  T-SQL functions.
- Supports STDEV(), STDEVP(), VAR(), VARP() statistical T-SQL
  aggregates.
- Supports sp_rename for COLUMN , TRIGGER, TABLE TYPE and USER DEFINED
  DATATYPE objects.
- Supports Babelfish instance as a linked server from SQL server
  instance. For more information,
  see [Babelfish supports linked servers](../AuroraUserGuide/babelfish-postgres-linkedservers.md "../AuroraUserGuide/babelfish-postgres-linkedservers.md").
- Supports 4 parts object name references for remote objects for select
  queries. For more information,
  see [Babelfish supports linked servers](../AuroraUserGuide/babelfish-postgres-linkedservers.md "../AuroraUserGuide/babelfish-postgres-linkedservers.md").
- Supports TOP clause for INSERT SELECT statement.
- Supports SET rowcount and SET CONTEXT_INFO T-SQL syntax.

###### Security enhancements

- Fixed an issue that non-sysadmin logins could DROP or ALTER logins.

###### Critical stability enhancements

- Fixed an issue when table variables may cause orphaned metadata entries.
- Fixed the issue that CTE top order handles null first behavior
  incorrectly.

###### High priority stability enhancements

- Fixed intermittent issue with concurrent SSL connections to Babelfish server.
- Fixed an issue in column name resolution of ORDER BY clause over UNION ALL query.
- Fixed the Unrecognized object issue when dropping database.
- Fixed the crash issue when adding non string unique key.
- User defined scalar functions were created as VOLATILE by default. This fix changes the behavior such that user defined scalar functions which do not perform any DML or DDL are created as STABLE by default.
- Fixed issues in column name resolution logic for UPDATE and DELETE statements with TOP clause.

###### Additional improvements and enhancements

- Fixed an issue with sp_helpdb where NULL is shown for compatbility_level.
- Fixed a memory management issue with update_DropRoleStmt.
- Fixed table variables to make it immune to transaction rollback.
- The fix corrects the behavior of ‘select convert(nvarchar(10),Getdate(),105)’ for nvarchar datatype.
- Fixed an issue to allow UPDATE and DELETE for Table Variables inside functions.
- Made enhancement to improve the performance and avoid catalog bloat while using table variables.
- Fixed an issue in @@NEXTLEVEL which returned 1 unit larger than expected.
- Fixed an issue in sp_helpdb where input parameter’s case sensitivity is not handled properly.
- Fixed an issue that COMMIT, ROLLBACK,EXECUTE, PRINT, SAVE and RAISERROR could be used in CREATE FUNCTION statement.
- Supports query timeout in sp_serveroption for OPENQUERY. For more information,
  see [Babelfish supports linked servers](../AuroraUserGuide/babelfish-postgres-linkedservers.md "../AuroraUserGuide/babelfish-postgres-linkedservers.md").
- Fixed the case sensitivity issue in the CREATE USER for windows login.
- Fixed an issue with detecting invalid login name in CREATE LOGIN WITH WINDOWS statement.
- Fixed an issue to support INT values in JSON_MODIFY() function.
- Fixed an issue in JSON_MODIFY() function to support new value parameters as JSON_QUERY, SELECT FOR JSON, or JSON MODIFY.
- Fixed an issue in babelfishpg_tds.product_version.
- Fixed an issue in datetimeoffset operations.
- Fixed an issue for datetimeoffset default values.
- Supports numeric expressions representing datetime values.
- Fixed an issue in sys.database_principals view where the users sys and information_schema, as well as the database role public are not shown.
- Old-style T-SQL catalogs, with names starting with 'sys' (like sysprocesses) were available only in the 'sys' schema, but are now also available in the 'dbo' schema.
- Fixed an issue where a T-SQL view could be created on top of a temporary table.
- Fixed an issue that DATETIME2 doesn’t accept 7 as scale argument.

### Babelfish for Aurora PostgreSQL 3.1 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 15.2. For more information about the improvements in Aurora PostgreSQL 15.2, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 3.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 3.1.4,
  November 6, 2024](#AuroraBabelfish.Updates.314 "#AuroraBabelfish.Updates.314")
- [Aurora Babelfish release 3.1.3,
  October 4, 2023](#AuroraBabelfish.Updates.313 "#AuroraBabelfish.Updates.313")
- [Aurora Babelfish release 3.1.2,
  July 24, 2023](#AuroraBabelfish.Updates.312 "#AuroraBabelfish.Updates.312")
- [Aurora Babelfish release 3.1.1,
  May 10, 2023](#AuroraBabelfish.Updates.311 "#AuroraBabelfish.Updates.311")
- [Aurora Babelfish release 3.1.0,
  April 5, 2023](#AuroraBabelfish.Updates.310 "#AuroraBabelfish.Updates.310")

#### Aurora Babelfish release 3.1.4,

November 6, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 3.1.3,

October 4, 2023

###### Additional improvements and enhancements

- Fixed a memory management issue with `update_DropRoleStmt`.
- Fixed a crash in `SqlBulkCopy` with heap_compute_data_size function in stacktrace when the order of columns is different compared to table defining.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed issue when user mapping that is created as part of `sp_addlinkedsrvlogin` works only when OPENQUERY() and
  remote object referenced with a four-part object names are invoked within the master database.
- Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.

#### Aurora Babelfish release 3.1.2,

July 24, 2023

###### Additional improvements and enhancements

- Fixed intermittent SSL connectivity issue during concurrent connections towards Babelfish instance.
- Fixed login name case sensitivity issue with CREATE USER for windows login syntax.

#### Aurora Babelfish release 3.1.1,

May 10, 2023

###### Additional improvements and enhancements

- Fixed an issue to prevent error when sequences are created in a database other than 'master'.
- Fixed a crash during bulk load operation in a specific scenario.
- Fixed an issue to prevent Babelfish instance from crashing when alter table and alter column is called with drop default where the column has no definition.

#### Aurora Babelfish release 3.1.0,

April 5, 2023

###### New features

- Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 14.6 and 14.7 to Aurora PostgreSQL 15.2.
  For more information on the major version upgrade, see
  [Upgrading your Babelfish cluster to a new version](../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-major "../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-major").
- Support for the following functions: STR, APP_NAME, OBJECT_DEFINITION, OBJECT_SCHEMA_NAME, ATN2, DATEDIFF_BIG functions.
- Support for the following INFORMATION_SCHEMA views: sequences, routines and schemata.
- Support sp_rename for TABLE, VIEW, PROCEDURE, FUNCTION, SEQUENCE.
- Support sys.systypes system compatibility view.
- Support for a new GUC parameter called babelfishpg_tds.product_version that allows you to set SQL Server product version number that is returned as an output by Babelfish. For more information,
  see [Using Babelfish product version GUC](../AuroraUserGuide/babelfish-guc-version.md "../AuroraUserGuide/babelfish-guc-version.md").
- Added support to generate data definition scripts for various objects present in a Babelfish for Aurora PostgreSQL database. For more information,
  see [DDL exports supported by Babelfish](../AuroraUserGuide/babelfish-query-database.md#babelfish-ddl-exports "../AuroraUserGuide/babelfish-query-database.md#babelfish-ddl-exports").
- Babelfish now supports Aurora PostgreSQL database authentication with Kerberos using AWS Directory Service for Microsoft Managed Active Directory. With this feature, for authentication you can use Microsoft Windows
  Authentication when you connect to your Babelfish database. For more information,
  see [Database authentication with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish-db-authentication.md "../AuroraUserGuide/babelfish-db-authentication.md").
- Babelfish now supports linked servers from your Aurora PostgreSQL database by using the tds_fdw (TDS Foreign Data Wrapper) APG extension. Only the OPENQUERY function that executes the specified pass-through query
  on the specified linked server is currently supported. For more information,
  see [Babelfish supports linked servers](../AuroraUserGuide/babelfish-postgres-linkedservers.md "../AuroraUserGuide/babelfish-postgres-linkedservers.md").

###### Security enhancements

- Fixed buffer overflow due to out of bound array access.

###### High priority stability enhancements

- Improved the performance through benefiting interactive queries, ODBC-based applications and tools such as SQL Server Management Studio.
  Following enhancements has been made for the same:
  - Fixed performance issues in several system functions including OBJECT_ID(), OBJECT_NAME(), SCHEMA_ID().
  - Fixed performance issues in system stored procedures sp_sproc_columns and sp_fkeys.
  - Fixed performance issues in system catalog views sys.all_views, sys.objects and sys.types.
  - Improved the performance of bulk load, parsing of T-SQL and prepared statements.

- Added a new system stored procedure sp_babelfish_volatility that you can use to set the volatility of user-defined
  functions to improve index use when the functions are used as part of query predicates.
- Fixed an issue where the UPDATE FROM or DELETE FROM statement that references the correlation name of the updated table raised an error.
- Fixed an issue where scope_identity function returns wrong result after exiting one scope.
- Fixed an issue where name resolution doesn't work as expected when commands are invoked from the .NET client framework.
- Fixed an issue where any index defined on column having binary/varbinary data types are not considered by the query optimizer for equality predicates.

###### Additional improvements and enhancements

- Fixed an issue where the statement timeout parameter for a session was not working as expected.
- Supports sequence creations using user-defined data types.
- Fixed an issue where unicode in column names, aliases or comments causes parsing errors.
- Fixed an issue where scope_identity function requires higher permission than actually needed.
- Support for the following stored procedures for working with linked servers: sp_addlinkedserver, sp_dropserver, sp_linkedservers,
  sp_addlinkedsrvlogin, sp_droplinkedsrvlogin, sp_helplinkedsrvlogin.
- Support for NEXT VALUE FOR function that gets the next value of a sequence. Note that this function cannot be used in some
  control-of-flow statements. OVER clause is also not supported.
- Fixed a crash when handling certain errors with sp_describe_undeclared_parameters.
- Fixed a rare error during Babelfish extension creation.
- Fixed an issue which was throwing an error "typename is NULL" while using TVP in sp_executesql.
- Fixed SELECT FOR XML/JSON behavior to not raise error when using SELECT with correlation name in subquery using FOR XML PATH clause.
- Fixed an issue with the SELECT FOR JSON or a SELECT FOR XML query which didn't return correct results for an empty table.
- Fixed an issue where the guest user can create objects in the wrong schema.
- Fixed schema name resolution for user defined types for param types in system stored procedures.
- Fixed an issue where applications issuing queries with more than 100 bind parameters for prepared statements were failing.
  This limit is now increased to 2100 to match the limits used by SQL Server.
- Fixed an issue with case handling of variable names in the sp_executesql call.
- sp_fkeys stored procedure now also returns 'deferrability' column in the result set.
- Fixed an issue in AVG aggregates which led to the termination of the connection for some integer datatypes.
- The index_id and indid column for respective views now returns the same value for indexes belonging to same object and the index_id is unique only within the object.
- Fixed an issue to not throw an error when OpenJson is called in stored procedures using nvarchar or join.
- Fixed an issue to not throw an error while using try_convert and try_cast for prohibited conversions involving some integer literals.
- Fixed an issue to allow OPENJSON WITH clause to accept a table alias.
- Support Degrees, Radians and Power functions returning the proper type.
- Fixed an issue where membership handling for sysadmin is not handled correctly.
- Fixed the default output style when converting DATE/TIME types to VARCHAR type using CONVERT function.
- Support EXECUTE AS CALLER clause in CREATE PROC/FUNCTION/TRIGGER.
- Fixed an issue where configurations are not reverted after existing sp_executesql scope.
- Fixed issues with handling cross-database access for the sys.has_perms_by_name function.
- Support the ProductLevel and ProductUpdateLevel properties for the SERVERPROPERTY function.
  ProductUpdateLevel always returns NULL and ProductLevel tracks the Babelfish version number closely with the T-SQL definition.
- Fixed an issue where the table variable when used as a bind parameter from client application resulted in an error.

## Babelfish for Aurora PostgreSQL 2.x versions (includes some deprecated versions)

###### Version updates

- [Babelfish for Aurora PostgreSQL 2.14](#AuroraBabelfish.Updates.214X "#AuroraBabelfish.Updates.214X")
- [Babelfish for Aurora PostgreSQL 2.12](#AuroraBabelfish.Updates.212X "#AuroraBabelfish.Updates.212X")
- [Babelfish for Aurora PostgreSQL 2.11](#AuroraBabelfish.Updates.211X "#AuroraBabelfish.Updates.211X")
- [Babelfish for Aurora PostgreSQL 2.10](#AuroraBabelfish.Updates.210X "#AuroraBabelfish.Updates.210X")
- [Babelfish for Aurora PostgreSQL 2.9](#AuroraBabelfish.Updates.29X "#AuroraBabelfish.Updates.29X")
- [Babelfish for Aurora PostgreSQL 2.8](#AuroraBabelfish.Updates.28X "#AuroraBabelfish.Updates.28X")
- [Babelfish for Aurora PostgreSQL 2.7 (Deprecated)](#AuroraBabelfish.Updates.27X "#AuroraBabelfish.Updates.27X")
- [Babelfish for Aurora PostgreSQL 2.6](#AuroraBabelfish.Updates.26X "#AuroraBabelfish.Updates.26X")
- [Babelfish for Aurora PostgreSQL 2.5 (Deprecated)](#AuroraBabelfish.Updates.25X "#AuroraBabelfish.Updates.25X")
- [Babelfish for Aurora PostgreSQL 2.4 (Deprecated)](#AuroraBabelfish.Updates.24X "#AuroraBabelfish.Updates.24X")
- [Babelfish for Aurora PostgreSQL 2.3 (Deprecated)](#AuroraBabelfish.Updates.23X "#AuroraBabelfish.Updates.23X")
- [Babelfish for Aurora PostgreSQL 2.2](#AuroraBabelfish.Updates.22X "#AuroraBabelfish.Updates.22X")
- [Babelfish for Aurora PostgreSQL 2.1](#AuroraBabelfish.Updates.21X "#AuroraBabelfish.Updates.21X")

### Babelfish for Aurora PostgreSQL 2.14

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.19. For more
information about the improvements in Aurora PostgreSQL 14.19, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
2.14 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.14.0, November 25, 2025](#AuroraBabelfish.Updates.2140 "#AuroraBabelfish.Updates.2140")

#### Aurora Babelfish release 2.14.0, November 25, 2025

**Critical enhancements**

- Fixed an issue during TDS Reset Connection in certain situations

**Additional improvements and enhancements**

- Fixed an issue while adding a column with default value which resulted in an error

### Babelfish for Aurora PostgreSQL 2.12

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.17. For more
information about the improvements in Aurora PostgreSQL 14.17, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
2.12 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.12.1, June 03, 2025](#AuroraBabelfish.Updates.2121 "#AuroraBabelfish.Updates.2121")
- [Aurora Babelfish release 2.12, April 08,
  2025](#AuroraBabelfish.Updates.212 "#AuroraBabelfish.Updates.212")

#### **Aurora Babelfish release 2.12.1, June 03, 2025**

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.12, April 08,

2025

**Critical enhancements**

- Added Cleanup of stale parameters and configs in case of connection pooling.
- Added comprehensive cursor state cleanup to avoid stale data in case of connection
  pooling.
- Fixed a issue with `IDENTITY` columns not being recognized during
  `DML` statements using `OUTPUT` and `WHERE`.

**High priority stability enhancements**

- Fix behavior of queries which use `sys.Db_id()` function which returned empty rows in enforced parallel mode.

### Babelfish for Aurora PostgreSQL 2.11

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.15. For more
information about the improvements in Aurora PostgreSQL 14.15, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md"). Babelfish for Aurora PostgreSQL
2.11 adds several new features, enhancements, and fixes. For more information about
Babelfish for Aurora PostgreSQL, see [Working with
Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.11.2,
  June 24, 2025](#AuroraBabelfish.Updates.2112 "#AuroraBabelfish.Updates.2112")
- [Aurora Babelfish release 2.11.1, January 20,
  2025](#AuroraBabelfish.Updates.2111 "#AuroraBabelfish.Updates.2111")
- [Aurora Babelfish release 2.11.0, December
  27, 2024](#AuroraBabelfish.Updates.2110 "#AuroraBabelfish.Updates.2110")

#### Aurora Babelfish release 2.11.2,

June 24, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.11.1, January 20,

2025

**High priority stability enhancements**.

- Fixed an issue where transactional commands may terminate the connection in some cases.

#### Aurora Babelfish release 2.11.0, December

27, 2024

###### _New features_

- Enabled support of `sys.sp_reset_connection stored` proc to reset connection.

###### _Additional improvements and enhancements_

- Fixed an issue with `ISNUMERIC` function to return correct result for nvarchar/varchar
  parameters.
- Fixed an issue to rethrow correct TSQL error code.

### Babelfish for Aurora PostgreSQL 2.10

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.13. For more information about the improvements in Aurora PostgreSQL 14.13, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.10 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.10.2,
  July 11, 2025](#AuroraBabelfish.Updates.2102 "#AuroraBabelfish.Updates.2102")
- [Aurora Babelfish release 2.10.0, September 30, 2024](#AuroraBabelfish.Updates.2100 "#AuroraBabelfish.Updates.2100")

#### Aurora Babelfish release 2.10.2,

July 11, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.10.0, September 30, 2024

###### Security enhancements

- Fixed an issue that potentially allowed non-privileged users to drop other users and roles in some scenarios.
- Fixed an issue with `sys.database_principals` view where it was showing metadata related to
  all the users irrespective of privileges of server principal.

###### High Priority stability enhancements

- Fixed an issue with `information_schema.tables` returning incorrect table_name.
- Fixed an issue for the `plpgsql` extension function. The function’s local settings for run-time configuration variables may not be reset at the end of function execution when Babelfish is
  installed.

###### Additional improvements and enhancements

- Fixed an issue where DML with `OUTPUT INTO` clause fired a trigger and may result in error.
- Fixed an issue when comment comes with the column name.

### Babelfish for Aurora PostgreSQL 2.9

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.12. For more information about the improvements in Aurora PostgreSQL 14.12, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.9 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.9.3,
  July 17, 2025](#AuroraBabelfish.Updates.293 "#AuroraBabelfish.Updates.293")
- [Aurora Babelfish release 2.9.1,
  September 27, 2024](#AuroraBabelfish.Updates.291 "#AuroraBabelfish.Updates.291")
- [Aurora Babelfish release 2.9.0,
  August 8, 2024](#AuroraBabelfish.Updates.290 "#AuroraBabelfish.Updates.290")

#### Aurora Babelfish release 2.9.3,

July 17, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.9.1,

September 27, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.9.0,

August 8, 2024

###### Critical stability enhancements

- Fixed issue producing syntax error with delimited column alias without preceding whitespace.
- Creating a user for a login is blocked when its login is already a member of sysadmin.
- Fixed the column type of the T-SQL views to use nvarchar(max).
- Fixed the `definition` column of the TSQL view `sys.sql_modules` which should have the datatype `nvarchar(max)`.

###### High priority stability enhancements

- Fixed an issue where Babelfish unexpectedly throws an error when connected with `pyodbc` or `sqlalchemy`.
- Fixed an issue with INSTEAD OF TRIGGER clause when same table has AFTER TRIGGER set on it.
- Fixed issue of crash under certain conditions while executing bulk copy.
- Crash in `handle_where_clause_restargets_right()`.
- Fixed a bug that could cause server restart while executing `comment on trigger` statement on Babelfish for Aurora PostgreSQL instance endpoint.
- Fixed issue with CONVERT() to return date in correct dateformat when converted to `char` and `nchar`.
- Fixed issue with insertion of datetime string with dateformat 13 into column of type `datetime`.
- Fixed several columns in `sys.index_columns` system catalog. Also fixed issue with DDL export of tables with indexes.
- Fixed an issue with ALTER TABLE ... DROP CONSTRAINT where it wasn't able to drop constraint in some cases.
- Fixed the issue of getting unexpected error `not all Parameters have names` when `SP_EXECSQL` contain TVP.
- Fixed an issue in handling of update or delete statements in `sp_describe_undeclared_parameters`.
- Fixed behavioral differences while CAST of string literals to `datetime`, `datetime2` and `datetimeoffset`.
- Fixed behavioral differences in COALESCE function while being called with the combination of variables and constants.

###### Additional improvements and enhancements

- Fixed memory leak in decimal (numeric) conversion for BCP import.
- Fixed the issue of `with tablock` hint resulting in an error for insert bulk statements.
- Added support for double-escaping and unbalanced quotes in `sp_tables table_type`.
- Added restriction on dropping of Babelfish extensions for all users except admin role.
- Prevent partial upgrades of Babelfish extensions.
- sys procedure columnproperty now support additional properties `iscomputed`, `columnid`, `ordinal`, `isidentity`.
- DDL scripting of indexes or constraints will now include correct ordering with columns.

### Babelfish for Aurora PostgreSQL 2.8

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.11. For more information about the improvements in Aurora PostgreSQL 14.11, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.8 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.8.4,
  July 30, 2025](#AuroraBabelfish.Updates.284 "#AuroraBabelfish.Updates.284")
- [Aurora Babelfish release 2.8.2,
  October 7, 2024](#AuroraBabelfish.Updates.282 "#AuroraBabelfish.Updates.282")
- [Aurora Babelfish release 2.8.0,
  April 29, 2024](#AuroraBabelfish.Updates.280 "#AuroraBabelfish.Updates.280")

#### Aurora Babelfish release 2.8.4,

July 30, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.8.2,

October 7, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.8.0,

April 29, 2024

###### Critical stability enhancements

- Fixed an issue in Object Explorer Database enumeration with SSMS version 19.2.
- Fixed an issue that caused error during Selecting data from variable `NVARCHAR(MAX)`, `VARCHAR(MAX)`,
  `VARBINARY(MAX)` with large length strings.
- Fixed blank space padding related issue in char datatype for multibyte characters.
- Fixed performance issue of enumerating tables and views in SSMS Object Explorer.

###### High priority stability enhancements

- Improved performance for system procedure `sp_tablecollations_100`.
- Fixed an issue with major version upgrades where views contains cast from string literal to binary type.
- Fixed a bug where parallel worker was unable to fetch the logical database name.
- Fixed the performance issue of comparing `date` to `datetime`.

###### Additional improvements and enhancements

- Fixed an issue on duplicate `object_id` in `sys.all_objects` after major version upgrade.
- Fixed an issue in `CAST` functions for `Binary` to `Varchar` and `Rowversion` to `Varchar`.
- Fixed an issue with insert into statement execution with table variable when table variable did not exist.
- Fixed an issue where input hex string being converted to type binary did not have the correct data length.
- Fixed an issue with mixed casing error in `sp_columns_100`.
- Fixed a crash in Table Variable lookup after `TVP` execution via `TDS RPC SPExecuteSQL`.
- Fixed Babelfish view definition table index to have correct collation when upgrading from 14.5 to 14.11.

### Babelfish for Aurora PostgreSQL 2.7 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.10. For more information about the improvements in Aurora PostgreSQL 14.10, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.7 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.7.4,
  August 4, 2025](#AuroraBabelfish.Updates.274 "#AuroraBabelfish.Updates.274")
- [Aurora Babelfish release 2.7.2,
  September 17, 2024](#AuroraBabelfish.Updates.272 "#AuroraBabelfish.Updates.272")
- [Aurora Babelfish release 2.7.0,
  December 21, 2023](#AuroraBabelfish.Updates.270 "#AuroraBabelfish.Updates.270")

#### Aurora Babelfish release 2.7.4,

August 4, 2025

**Security enhancements**

- Fixed an issue with permission check in parallel worker where non-privileged user may get
  read access to data in some scenarios.

#### Aurora Babelfish release 2.7.2,

September 17, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.7.0,

December 21, 2023

###### Security enhancements

- Fixed permission issue for view sys.server_principals.

###### Critical stability enhancements

- Fixed an issue where ISNULL function may return incorrect data type.
- Fixed an issue where condition may be evaluated incorrectly for conditional statement like IF.
- Fixed an error "database ... does not exist" that may be observed when parallel query is enforced.
- Fixed handling of table variable or temp table when Parallel worker is enforced.
- Fixed unexpected error "lost connection to parallel worker" occurring when parallel worker is enforced.
- Fixed an issue with multiple parentheses in SELECT columns.
- Fixed an issue with handling of column name alias which may cause client to hang if column name alias contains string of length more than 64 bytes, for example, select col as '您对“数据一览“中的车型，颜色，内饰，选装, '.
- Fixed datatype of information_schema_tsql.tables.TABLE_TYPE column.
- Fixed the error - “column ... does not exist” when using table.column with alias defined for table or schema_name.table.column in set clause of update queries.
- Fixed issue of incorrect schema resolution for multiple functions in query statement.

###### High priority stability enhancements

- Fixed type conversion between varchar and binary datatype with use of proper encoding.
- Fixed an issue where upper/lower case may not be preserved for column name aliases.
- Fixed crash in queries involving money data-type in parallel query mode.
- Fixed failure in MVU with non-default server collation name.
- Fixed the issue of information_schema vs. sys.objects WHERE type IN ('U', 'V') giving different result in Babelfish.
- Fixed issue of sp_columns and sp_columns_100 incorrectly show NULL radix for decimal columns.
- Fixed issue in queries involving sys.format() function in parallel query mode returning error “cannot start subtransactions during a parallel operation”.
- Fixed unexpected error “could not access file "pg_hint_plan": No such file or directory" while using pg_hint_plan in parallel query mode.
- Fixed the issue of getting error ‘duplicate key value violates unique constraint ...' when re-creating a previously dropped view with the same name.

###### Additional improvements and enhancements

- Improved performance for stored procedure sp_describe_undeclared_parameters.
- Fixed performance issue for DATEADD(), DATEDIFF().
- SSMS - Fixed issue of stored procedure takes long time to load in Object Explorer.
- SSMS - Fixed performance issue of enumerating tables and views in SSMS Object Explorer.
- Fixed performance issue after create/upgrade of Babelfish extension by running ANALYZE after Babelfish extension creation and upgrade.
- Fixed the issue of index not used when query has an unnecessary cast to bigint.
- Fixed an issue when stored procedures starting with (sp\_\*) are invoked with a dbo. or sys. prefix.
- Fixed the issue with default_schema_name column of the catalog sys.babelfish_authid_user_ext in case of "guest" user.
- Fixed issue of orphan entries in sys.babelfish_view_def catalog table.

### Babelfish for Aurora PostgreSQL 2.6

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.9. For more information about the improvements in Aurora PostgreSQL 14.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.6 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.6.1,
  November 14, 2024](#AuroraBabelfish.Updates.261 "#AuroraBabelfish.Updates.261")
- [Aurora Babelfish release 2.6.0,
  October 24, 2023](#AuroraBabelfish.Updates.260 "#AuroraBabelfish.Updates.260")

#### Aurora Babelfish release 2.6.1,

November 14, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.6.0,

October 24, 2023

###### New features

- Added support for TSQL function SMALLDATETIMEFROMPARTS().

###### Critical stability enhancements

- T-SQL trigger can't be executed when function, procedure or trigger of PostgreSQL is in execution stack.

###### High priority stability enhancements

- Fixed the issue of GETDATE() incorrectly returning different values in the same query.
- Fixed the issue of GETUTCDATE() incorrectly returning time of transaction instead of time of query.

###### Additional improvements and enhancements

- Fixed an issue where SSMS generate script for multiple views, or combining a view with other objects throws an error.
- Fixed an issue to avoid system crash while formatting `datetime` values in the results of FOR JSON or FOR XML.
- Fixed an issue to avoid system crash during table variable cleanup after a runtime error.
- Fixed an issue to avoid system crash when using certain values in nested function calls.
- Fixed an invalid memory access issue while freeing `PLTSQL` functions.
- Fixed a crash in `SqlBulkCopy` when the order of columns is different from the table where it is defined.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed crash in parallel query when `enable_pg_hint` is turned on.
- Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
- Fixed issue where `sp_describe_first_result_set` procedure can return incorrect column order, which could cause BCP to work incorrectly.
- Fixed issue related to loss of decimal digits when converting from REAL to DECIMAL.
- Fixed error handling during the Babelfish upgrade process. Babelfish throws an error if there is a failure during the upgrade.
- Fixed an issue with sender of XML data type to handle `NULL` value where it was causing client to hang.
- Fixed an issue where USE database statement was incorrectly allowed inside the procedure, function or trigger definition.
- Fixed crash while calling T-SQL procedure from PG port when querying `sys.sysobjects`.

### Babelfish for Aurora PostgreSQL 2.5 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.8. For more information about the improvements in Aurora PostgreSQL 14.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.5 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.5.2,
  November 12, 2024](#AuroraBabelfish.Updates.252 "#AuroraBabelfish.Updates.252")
- [Aurora Babelfish release 2.5.1,
  October 4, 2023](#AuroraBabelfish.Updates.251 "#AuroraBabelfish.Updates.251")
- [Aurora Babelfish release 2.5.0,
  July 13, 2023](#AuroraBabelfish.Updates.250 "#AuroraBabelfish.Updates.250")

#### Aurora Babelfish release 2.5.2,

November 12, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.5.1,

October 4, 2023

###### High priority stability enhancements

- Fixed an issue causing crash when cursor referencing a table variable is already dropped.
- Fixed an issue where queries with UNION ALL, ORDER BY, and multiple joins could cause unavailability.
- Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.
- Fixed an invalid memory access while freeing `PLTSQL` functions.

###### Additional improvements and enhancements

- Fixed an issue to avoid crash by properly handling formatting of datetime values in the results of FOR JSON or FOR XML.
- Fixed a crash in `SqlBulkCopy` when the order of columns is different compared to table defining.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed incorrect value in procedure output parameter when procedure is called by name and is in different parameter order.
- Fixed a crash when dropping temp table or table variables during cleanup.
- Fixed an issue with sender of XML data type to handle NULL value where it was causing client to hang.

#### Aurora Babelfish release 2.5.0,

July 13, 2023

###### Security enhancements

- Fixed an issue that non-sysadmin logins could DROP or ALTER logins.

###### Critical stability enhancements

- Fixed an issue when table variables may cause orphaned metadata entries.
- Fixed the issue where CTE top order handles null first behavior
  incorrectly.

###### High priority stability enhancements

- Fixed intermittent issue with concurrent SSL connections to Babelfish server.
- Fixed an issue in column name resolution of ORDER BY clause over UNION ALL query.
- Fixed the Unrecognized object issue when dropping database.
- Fixed the crash issue when adding non string unique key.

###### Additional improvements and enhancements

- Fixed an issue with sp_helpdb where NULL is shown for compatbility_level.
- Fixed a memory management issue with update_DropRoleStmt.
- Fixed table variables to make it immune to transaction rollback.
- The fix corrects the behavior of ‘select convert(nvarchar(10),Getdate(),105)’ for nvarchar datatype.
- Fixed an issue to allow UPDATE and DELETE for Table Variables inside functions.
- Made enhancement to improve the performance and avoid catalog bloat while using table variables.
- Fixed an issue in @@NEXTLEVEL which returned 1 unit larger than expected.
- Fixed an issue in sp_helpdb where input parameter’s case sensitivity is not handled properly.

### Babelfish for Aurora PostgreSQL 2.4 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.7. For more information about the improvements in Aurora PostgreSQL 14.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.4 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.4.4,
  November 6, 2024](#AuroraBabelfish.Updates.244 "#AuroraBabelfish.Updates.244")
- [Aurora Babelfish release 2.4.3,
  October 4, 2023](#AuroraBabelfish.Updates.243 "#AuroraBabelfish.Updates.243")
- [Aurora Babelfish release 2.4.2,
  July 24, 2023](#AuroraBabelfish.Updates.242 "#AuroraBabelfish.Updates.242")
- [Aurora Babelfish release 2.4.1,
  May 10, 2023](#AuroraBabelfish.Updates.241 "#AuroraBabelfish.Updates.241")
- [Aurora Babelfish release 2.4.0,
  April 5, 2023](#AuroraBabelfish.Updates.240 "#AuroraBabelfish.Updates.240")

#### Aurora Babelfish release 2.4.4,

November 6, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.4.3,

October 4, 2023

######

- Fixed a memory management issue with `update_DropRoleStmt`.
- Fixed a crash in `SqlBulkCopy` with heap_compute_data_size function in stacktrace when the order of columns is different compared to table defining.
- Fixed an issue that `bcp in` results in server crash when the table has large number of columns.
- Fixed a crash in parallel query execution when `enable_pg_hint` is set to `on`.

#### Aurora Babelfish release 2.4.2,

July 24, 2023

###### Additional improvements and enhancements

- Fixed intermittent SSL connectivity issue during concurrent connections towards Babelfish instance.

#### Aurora Babelfish release 2.4.1,

May 10, 2023

###### Additional improvements and enhancements

- Fixed an issue to prevent error when sequences are created in a database other than 'master'.
- Fixed a crash during bulk load operation in a specific scenario.

#### Aurora Babelfish release 2.4.0,

April 5, 2023

###### New features

- Supports minor version upgrade from Babelfish for Aurora PostgreSQL DB cluster 14.3 onwards to Aurora PostgreSQL 14.7.
  For more information on the minor version upgrade, see
  [Upgrading Babelfish to a new minor version](../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-minor "../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-minor").
- Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 13.x onwards to Aurora PostgreSQL 14.7.
  For more information on the major version upgrade, see
  [Upgrading Babelfish to a new major version](../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-major "../AuroraUserGuide/babelfish-information-upgrading.md#babelfish-information-upgrading-major").
- Support for the following functions: STR, APP_NAME, OBJECT_DEFINITION, OBJECT_SCHEMA_NAME, ATN2, DATEDIFF_BIG functions.
- Support for the following INFORMATION_SCHEMA views: sequences, routines and schemata.
- Support sp_rename for TABLE, VIEW, PROCEDURE, FUNCTION, SEQUENCE.
- Support sys.systypes system compatibility view.
- Support for a new GUC parameter called babelfishpg_tds.product_version that allows you to set SQL Server product version number that is returned as an output by Babelfish. For more information,
  see [Using Babelfish product version GUC](../AuroraUserGuide/babelfish-guc-version.md "../AuroraUserGuide/babelfish-guc-version.md").
- Added support to generate data definition scripts for various objects present in a Babelfish for Aurora PostgreSQL database. For more information,
  see [DDL exports supported by Babelfish](../AuroraUserGuide/babelfish-query-database.md#babelfish-ddl-exports "../AuroraUserGuide/babelfish-query-database.md#babelfish-ddl-exports").

###### Security enhancements

- Fixed buffer overflow due to out of bound array access.

###### High priority stability enhancements

- Improved the performance through interactive queries, ODBC-based applications and tools such as SQL Server Management Studio.
  Following enhancements has been made for the same:
  - Fixed performance issues in several system functions including OBJECT_ID(), OBJECT_NAME(), SCHEMA_ID().
  - Fixed performance issues in system stored procedures sp_sproc_columns and sp_fkeys.
  - Fixed performance issues in system catalog views sys.all_views, sys.objects and sys.types.
  - Improved the performance of bulk load, parsing of T-SQL and prepared statements.

- Added a new system stored procedure sp_babelfish_volatility that you can use to set the volatility of user-defined
  functions to improve index use when the functions are used as part of query predicates.
- Fixed an issue where the UPDATE FROM or DELETE FROM statement that references the correlation name of the updated table raised an error.
- Fixed an issue where scope_identity function returns wrong result after exiting one scope.
- Fixed an issue where name resolution doesn't work as expected when commands are invoked from the .NET client framework.

###### Additional improvements and enhancements

- Fixed an issue where the statement timeout parameter for a session was not working as expected.
- Support for sequence creations using user-defined data types.
- Fixed an issue where unicode in column names, aliases or comments causes parsing errors.
- Fixed an issue where scope_identity function requires higher permission than actually needed.
- Support for NEXT VALUE FOR function that gets the next value of a sequence. Note that this function cannot be used in some
  control-of-flow statements. OVER clause is also not supported.
- Fixed a crash when handling certain errors with sp_describe_undeclared_parameters.
- Fixed a rare error during Babelfish extension creation.
- Fixed an issue which was throwing an error "typename is NULL" while using TVP in sp_executesql.
- Fixed SELECT FOR XML/JSON behavior to not raise error when using SELECT with correlation name in subquery using FOR XML PATH clause.
- Fixed an issue with the SELECT FOR JSON or a SELECT FOR XML query which didn't return correct results for an empty table.
- Fixed an issue where the guest user can create objects in the wrong schema.
- Fixed schema name resolution for user defined types for param types in system stored procedures.
- Fixed the issue where applications issuing queries with more than 100 bind parameters for prepared statements were failing.
  This limit is now increased to 2100 to match the limits used by SQL Server.
- Fixed an issue with case handling of variable names in the sp_executesql call.
- sp_fkeys stored procedure now also returns 'deferrability' column in the result set.
- Fixed an issue in AVG aggregates which led to the termination of the connection for various integer datatypes.
- The index_id and indid column for respective views now returns the same value for indexes belonging to same object and the index_id is unique only within the object.
- Fixed an issue to not throw an error when OpenJson is called in stored procedures using nvarchar or join.
- Fixed an issue to not throw an error while using try_convert and try_cast for prohibited conversions involving int literals.
- Fixed an issue to allow OPENJSON WITH clause to accept a table alias.
- Support Degrees, Radians and Power functions returning the proper type.
- Fixed an issue where membership handling for sysadmin is not handled correctly.
- Fixed the default output style when converting DATE/TIME types to VARCHAR type using CONVERT function.
- Support EXECUTE AS CALLER clause in CREATE PROC/FUNCTION/TRIGGER.
- Fixed an issue where configurations are not reverted after existing sp_executesql scope.
- Fixed issues with handling cross-database access for the sys.has_perms_by_name function.
- Support the ProductLevel and ProductUpdateLevel properties for the SERVERPROPERTY function.
  ProductUpdateLevel always returns NULL and ProductLevel tracks the Babelfish version number closely with the T-SQL definition.
- Fixed an issue where the table variable when used as a bind parameter from client application resulted in an error.

### Babelfish for Aurora PostgreSQL 2.3 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.6. For more information about the improvements in Aurora PostgreSQL 14.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.3 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.3.4,
  November 18, 2024](#AuroraBabelfish.Updates.234 "#AuroraBabelfish.Updates.234")
- [Aurora Babelfish release 2.3.3,
  September 13, 2023](#AuroraBabelfish.Updates.233 "#AuroraBabelfish.Updates.233")
- [Aurora Babelfish release 2.3.2,

March 3, 2023](#AuroraBabelfish.Updates.232 "#AuroraBabelfish.Updates.232")

- [Aurora Babelfish release 2.3.0,
  January 20, 2023](#AuroraBabelfish.Updates.230 "#AuroraBabelfish.Updates.230")

#### Aurora Babelfish release 2.3.4,

November 18, 2024

###### Security enhancements

- Fixed an issue with dropping users and roles by non-privileged user.

#### Aurora Babelfish release 2.3.3,

September 13, 2023

###### Additional improvements and enhancements

- Fixed a rare error during Babelfish extension creation.
- Fixed a memory management issue with `update_DropRoleStme`.

#### Aurora Babelfish release 2.3.2,

March 3, 2023

###### Security enhancements

- Fixed buffer overflow due to out of bound array access.

#### Aurora Babelfish release 2.3.0,

January 20, 2023

###### New features

- Supports major version upgrade from Babelfish for Aurora PostgreSQL DB cluster 13.6 and later to Aurora PostgreSQL 14.6.
  For more information on the major version upgrade, see
  [Upgrading your Babelfish cluster to a new version](../AuroraUserGuide/babelfish-information.md#babelfish-information-upgrading "../AuroraUserGuide/babelfish-information.md#babelfish-information-upgrading").
- Support for T-SQL hints (join methods, index usage, MAXDOP). For more information on the T-SQL hints supported by Babelfish,
  see [Using T-SQL query hints to improve Babelfish query performance](../AuroraUserGuide/babelfish-tsql-hints.md "../AuroraUserGuide/babelfish-tsql-hints.md").
- Babelfish now supports Zero-downtime patching (ZDP). For more information, see
  [Minor
  release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor")
  in the _Amazon Aurora User Guide_.
- Support for FORMAT() T-SQL function with minor limitations.
- Support the estimated execution plans for THROW, PRINT, USE, and RAISEERROR statements.
- Support for JSON_MODIFY function in Babelfish which updates the value of a property in a JSON string and returns the updated JSON string.
- Support the VALUES() constructor in FROM clause in a SELECT statement.
- Support sp_addrole, sp_droprole, sp_addrolemember, sp_droprolemember procedures to create or alter a role.
- Support for sys.all_parameters catalog view.
- Support guest user in all the user created databases and support GRANT/CONNECT TO/FROM user (including guest).
- Support sp_helpdbfixedrole and DATETIMEOFFSETFROMPARTS functions.

###### High priority stability enhancements

- Improved performance for INSERT statement with IDENTITY_INSERT=ON.
- Fixed an issue where "DROP DATABASE" statement fails due to incorrect comparison operator used.
- Fixed an issue where numeric overflow error was not handled properly for numeric types.
- Fixed an issue where DB owner is not considered as dbo in its own DB.
- Fixed issues with SSL handshake failure and added a few other improvements.
- Fixed the sys.all_objects view to correctly identify inline table-valued functions (IF) and table-valued functions (TF)
  which were previously reported as scalar functions (FN). Similar issue is fixed for the IsInlineFunction property of the OBJECTPROPERTY function.
- Fixed an issue where DBO is assumed member of a DB role incorrectly.
- Fixed an issue where member of sysadmin could not connect through SSMS.
- Corrected the schema name resolution for triggers and views so that it selects/modifies the correct object(tables).
- Fixed the mapping consistency in catalog when creating roles with names in upper/lower case.
- Fixed an issue where drop database is blocked after access denial to other logins due to in sufficient permission.
- Fixed the default collation of Babelfish data types except TEXT and NTEXT to be the same as that mentioned in the babelfishpg_tsql.server_collation_name parameter.
  For more information, see [Default Collation in Babelfish](../AuroraUserGuide/babelfish-collations.md#babelfish-collations-default "../AuroraUserGuide/babelfish-collations.md#babelfish-collations-default").
- Fixed the cross-DB references to tempdb.sys.objects for correct results.

###### Additional improvements and enhancements

- Fixed an issue to make trigger names unique for each database.
- Fixed an issue in sp_tables when it is invoked from JDBC metadata functions.
- Fixed an issue when CHECK constraints are used with LIKE condition.
- Performance improvements with sp_sproc_columns when dealing with stored procedures.
- sp_sproc_columns now includes table-valued parameter row for stored procedures that use TVP as a parameter.
- Fixed the cross-DB references to INFORMATION_SCHEMA.ROUTINES and tempdb.sys.objects to give the correct results.
- Fixed issues to support datetime/smalldatetime operation with various numeric and non numeric datatypes.
- Fixed the return values of SUM aggregates for integer datatypes to return the correct datatypes.
- Fixed an issue when UPDATE/DELETE is used with table aliases.
- Support added for sysobjects.crdate (create_date) for all user defined tables, views, procedures, functions, triggers and table types.
- Procedure/function call is not allowed when required parameter is missing and an explicit error is raised.
- Fixed issue to calculate the day difference and the hour difference, without considering timestamp (i.e., hh:mm:ss.msec).
- Fixed an issue with DATEDIFF() function to return correct results between two input dates regardless of the input parameters.
- Fixed an issue with DATEADD() function when used with the 'nanosecond' units.
- Fixed an issue with DATEPART(), DATENAME(), DATEDIFF() and DATEADD() functions when used with 'w' units
- Fixed an issue with DATEPART() and DATENAME() to allow units 'y'.
- Fixed issues with DATEPART(), DATENAME(), DATEDIFF() and DATEADD() functions to convert string to datetime and to recognize mi units.
- Support for TRY_CONVERT() function.
- Fixed issue with using strict/lax jsonpath with arrays to avoid OPENJSON error: "syntax error at or near " " of jsonpath input".
- Support UDF (User Defined Function) as column default in ALTER TABLE statement.
- Fixed an issue when SUBSTRING() takes NULL arguments.
- Support for cast operations to SMALLDATETIME from various numeric types.
- Fixed an issue where dbname parameter is not handled properly for sp_helpdb.
- Fixed an issue where DB owner is allowed to create another user for itself.
- Fixed an issue where trailing spaces are not ignored in sp_helpsrvrolemember and IS_ROLEMEMBER/IS_MEMBER functions.
- Improved error message for unsupported data types: HIERARCHYID, GEOGRAPHY, GEOMETRY.
- Fixed issues where cross database procedure calls and sp\_ procedures access from other databases should succeed even without EXECUTE keyword.
- Fixed an issue where user 'guest' is not dropped in any database, but only disabled.
- Fixed the column value for SID in the procedure sp_helpuser when the user is guest.
- Fixed an issue where overflow/underflow is not getting handled with money datatype.
- Fixed an issue where error is not getting handled while error processing in tds.
- Fixed a better error message for CREATE USER WITHOUT LOGIN.
- Fixed an issue where sp_helpsrvrolemember is throwing unsupported errors for unsupported server level roles.
- Fixed an issue where SET BABELFISH_STATISTICS PROFILE shows planning and execution times.
- Corrected the schema name resolution for Babelfish objects like views and triggers, so that correct object is selected or modified.
- Support rowversion/timestamp Datatype for Insert Bulk.
- In Babelfish, sp_babelfish_configure supports enable_pg_hint and explain-related configurations by turning them "on/off". Accepting "ignore/strict" option is allowed when there are multiple matches while using sp_babelfish_configure.
- Support to Keep Nulls (-k) bcp option for optimized implementation to insert Bulk.
- Support multi-byte currency symbols to use with money data type.
- Fixed issue for dotnet clients (including SSMS) that received invalid precision/scale error for certain arithmetic expressions.
- Fixed the sys.all_objects view to correctly identify inline table-valued functions (IF) and table-valued functions (TF) which were previously reported as scalar functions (FN).
  Fixed similar issue for the IsInlineFunction property of the OBJECTPROPERTY function.
- Fixed an issue where the is_member function returns an incorrect result for certain roles.
- Improvements in FOR JSON PATH clause of SELECT statement which supports ROOT, INCLUDE_NULL_VALUES, WITHOUT_ARRAY_WRAPPER.
- Supports a new escape hatch, 'escape_hatch_checkpoint' with a default pf 'ignore'. This escape hatch allows the use of CHECKPOINT statement in the procedural code, but the CHECKPOINT statement is currently not implemented.

### Babelfish for Aurora PostgreSQL 2.2

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.5. For more information about the improvements in Aurora PostgreSQL 14.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.2 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 2.2.3,
  October 17, 2023](#AuroraBabelfish.Updates.223 "#AuroraBabelfish.Updates.223")
- [Aurora Babelfish release 2.2.2,
  March 2, 2023](#AuroraBabelfish.Updates.222 "#AuroraBabelfish.Updates.222")
- [Aurora Babelfish release 2.2.1, December 13, 2022](#AuroraBabelfish.Updates.221 "#AuroraBabelfish.Updates.221")
- [Aurora Babelfish release 2.2.0,
  November 9, 2022](#AuroraBabelfish.Updates.220 "#AuroraBabelfish.Updates.220")

#### Aurora Babelfish release 2.2.3,

October 17, 2023

###### High priority stability enhancements

- Fixed issues with SSL handshake failure and added a few other improvements.

###### Additional improvements and enhancements

- Fixed a memory management issue with `update_DropRoleStmt`.

#### Aurora Babelfish release 2.2.2,

March 2, 2023

###### Security enhancements

- Fixed buffer overflow due to out of bound array access.

#### Aurora Babelfish release 2.2.1, December 13, 2022

- Fixed an issue that prevented the use of collations like Chinese_PRC_CI_AS, Japanese_CI_AS and so on for babelfishpg_tsql.server_collation_name.

#### Aurora Babelfish release 2.2.0,

November 9, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

###### High priority stability enhancements

- Fixed error handling in sp_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
- Fixed error handling in SSL/TLS handshake for some client drivers.
- Fixed an issue where a login can access the database without creating DB user after the DROP/CREATE of login.
- Fixed an issue where a login isn't dropped if it is logged in on any session.

###### New features

- Support for data migration using the BCP client and the bcp utility now supports -E flag (for identity columns) and -b flag (for batching inserts).
- Support for cross-database stored procedure execution.
- Support for CROSS APPLY and OUTER APPLY (lateral join).
- Support for built-in functions SYSTEM_USER, HOST_NAME; the Hostname is visible in the sys.sysprocesses T-SQL view; the SID_BINARY
  function is supported but always returns NULL in Babelfish.
- Support for CAST function of numeric expressions to DATETIME.
- Support for @@LANGUAGE variable with constant value as 'us_english’.
- Support for the old-style function calls with '::' preceding the function name.
- Support for the sp_helpsrvrolemember stored procedure.
- Support for the msdb.dbo.fn_syspolicy_is_automation_enabled system
  function.
- Support for more catalogs: assembly_types, numbered_procedures, triggers,
  spatial_index_tessellations, plan_guides, synonyms, events, trigger_events,
  fulltext_indexes, dm_hadr_cluster, xml_indexes, change_tracking_tables,
  key_constraints, database_filestream_options,
  filetable_system_defined_objects, hash_indexes, filegroups, master_files,
  assembly_modules, change_tracking_databases, database_recovery_status,
  fulltext_catalogs, fulltext_stoplists, fulltext_indexes,
  fulltext_index_columns, fulltext_languages, selective_xml_index_paths,
  spatial_indexes, filetables, registered_search_property_lists,
  syspolicy_configuration, syspolicy_system_health_state.
- Support for new INFORMATION_SCHEMA catalogs: COLUMN_DOMAIN_USAGE,
  CONSTRAINT_COLUMN_USAGE, CHECK_CONSTRAINTS, ROUTINES, VIEWS.
- Support for new PG-style query plan: escape hatch 'babelfish_pgtsql.escape_hatch_showplan_all'.
  - when set to 'ignore', SET SHOWPLAN_ALL and SET STATISTICS
    PROFILE behaves as SET BABELFISH_SHOWPLAN_ALL and SET
    BABELFISH_STATISTICS PROFILE.
  - when set to 'strict', SET SHOWPLAN_ALL and SET
    STATISTICS PROFILE are silently ignored.

- Support for executing stored procedures with the sp\_ prefix in the master database without using a three-part name.

###### Additional improvements and enhancements

- Fixed an issue where a value of 1900-01-01 00:00:00 was stored when a NULL was inserted or updated into a datetime column. A NULL value is inserted now. Column values in tables created in a previous Babelfish release are not affected.
- TIME datatypes that return 7 digits in SQL Server now returns 7 digits in Babelfish as well, with the 7th digit always being zero. In addition, a rounding issue that sometimes affected the 6th digit has been resolved.
- Increased parameter lengths for @tsql and @params for sp_describe_first_result_set from nvarchar(384) to nvarchar(8000). This increases the number of columns the DMS Babelfish target endpoint can support from 25 to 1000.
- Improved performance for system stored procedures: sys.sp_tablecollations_100, sp_columns_managed, and sp_describe_undeclared_parameters. This fix improves the performance of the DMS Babelfish
  target endpoint, SQL Server Management Studio import and export wizard, and prevents timeouts.
- Fixed an issue with Bitwise NOT ~ operator and it returns the correct result with BIT data types now.
- Fixed an issue with BCP when it is used for tables that have triggers.
- Fixed an issue of backend failure in INSERT BULK when using Import-Export wizard.
- Fixed an issue where SQL Server Management Studio (SSMS) returns an error while expanding "Triggers" for a table in the Object Explorer view.
- Fixed an issue where the name column in the sys.sysobjects view was using case sensitive collation.
- Fixed an issue to refer SQL objects inside a function and is resolved to the function's schema rather than the default schema of the user.
- Fixed an issue where a backend crash can occur when using the ISNULL function with CONVERT on computed columns.
- Fixed an issue with the DATEPART function when the date argument is a string literal.
- Fixed an issue where a role can be dropped even if it has members.
- Fixed an issue so that the db user can't add to a role or drop from a role.
- Fixed an issue to allow BCP to work correctly with collations other than English collations.
- Fixed an issue to make sp_helpuser procedure show login name for dbo user.
- Fixed an issue to handle NULL and mix-cased inputs correctly for the functions SUSER_SNAME and SUSER_SID.
- Fixed an issue with Babelfish returning an invalid TDS protocol stream when there is a numeric overflow error.
- Fixed an issue where is_fixed_role column returns incorrect value in the sys.server_principals view for the 'sysadmin' role.
- Fixed the transaction error handling in a batch if the string passed to execute contains a USE `dbname` and fails because the database `dbname` was not found.
- Fixed the issue with procedures created in master database context with prefix sp\_ that are not accessible from other database context.
- Fixed the failure to resolve object name inside a procedure when used with schema name.
- Fixed case-sensitivity issue with arguments to the functions USER_ID and SUSER_ID.
- Fixed an issue where triggers were allowed to be created on Babelfish temporary tables.
- Fixed several performance issues with Import-Export wizard.
- Support for multi-byte client encodings other than UTF-16 for VARCHAR(n).
- Fixed the system compatibility view sys.sysprocesses to show the correct value for hostname provided by the client connection.
- Fixed case sensitivity issue with Polish_CI_AS collation.
- Fixed the @@DBTS function so that value of @@DBTS correctly returns the current transaction id after each DML statement even when used within a transaction.
- Improved performance for queries that refer to the functions SCOPE_IDENTITY and @@IDENTITY.
- Support added for collations Japanese_CS_AS, Japanese_CI_AI and Japanese_CI_AS for fn_helpcollations.
- @@SERVERNAME and SERVERPROPERTY('ServerName') now return the name of the
  Babelfish instance as specified by the user when the instance is created.
  This value is also returned by the newly supported properties
  SERVERPROPERTY('MachineName') and SERVERPROPERTY('InstanceName').
- Function fn_mapped_system_error_list lists the PG error code mapped to
  @@ERROR codes, as well as the corresponding error message text. This
  function also exists in previous Babelfish releases but did not include mapping
  details.
- Fixed DATEADD function to now support milliseconds(ms) time units.
- SET NO_BROWSETABLE {ON|OFF} is now subject to escape hatch escape_hatch_session_settings, so no error is raised when set to ignored.
- SET PARSEONLY {ON|OFF} is now supported. Previously this would raise an error unless escape hatch escape_hatch_session_settings is set to ignored.
- The DATABASE_DEFAULT AND CATALOG_DEFAULT collation is now supported; this refers to the server/instance-level collation that was specified when the Babelfish
  instance was created, as Babelfish doesn't currently support collations on database level.
- For the functions OBJECTPROPERTY and OBJECTPROPERTYEX, the following properties are
  now supported: ExecIsAnsiNullsOn, ExecIsQuotedIdentOn, IsDefault,
  IsDefaultCnst, IsDeterministic, IsIndexed, IsInlineFunction, IsMSShipped,
  IsPrimaryKey, IsProcedure, IsRule, IsScalarFunction, IsSchemaBound, IsTable,
  IsTableFunction, IsTrigger, IsUserTable, IsView, OwnerId,
  TableFulltextPopulateStatus, TableHasVarDecimalStorageFormat.
- OBJECTPROPERTYEX function supports the BaseType property.
- INDEXPROPERTY function supports the following properties: IndexFillFactor,
  IndexID, IsClustered, IsDisabled, IsHypothetical, IsPadIndex,
  IsPageLockDisallowed, IsRowLockDisallowed, IsUnique.

### Babelfish for Aurora PostgreSQL 2.1

This release of Aurora Babelfish is provided with Aurora PostgreSQL 14.3 and 14.4. For more information about the improvements in Aurora PostgreSQL 14.3 and 14.4, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 2.1 adds several new features, enhancements, and fixes. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Babelfish for Aurora PostgreSQL release 2.1.2, October 18, 2022](#AuroraBabelfish.Updates.212 "#AuroraBabelfish.Updates.212")
- [Babelfish for Aurora PostgreSQL release 2.1.1, July 6, 2022](#AuroraBabelfish.Updates.211 "#AuroraBabelfish.Updates.211")
- [Babelfish for Aurora PostgreSQL release 2.1.0, June 21, 2022](#AuroraBabelfish.Updates.210 "#AuroraBabelfish.Updates.210")

####

Babelfish for Aurora PostgreSQL release 2.1.2, October 18, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

###### High priority stability enhancements

- Fixed error handling in sp_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
- Fixed error handling in SSL/TLS handshake for some client drivers.

####

Babelfish for Aurora PostgreSQL release 2.1.1, July 6, 2022

- Fixed the babelfishpg_tds extension to correctly allocate the shared memory size used by the extension.

####

Babelfish for Aurora PostgreSQL release 2.1.0, June 21, 2022

Babelfish DB clusters running on Aurora PostgreSQL 13.7 or older versions can't be upgraded to Aurora PostgreSQL 14.3 with Babelfish 2.1.0.

###### New features

- Support for data migration using the bcp client utility, as an experimental feature. Some bcp options (-b, -C, -E, -G, -h, -K, -k, -q, -R, -T, -V) are not currently supported.
- Support for connecting with the SSMS object explorer connection dialog (rather than only the Query Editor connection dialog), as well as partial support for the SSMS object explorer itself.
- Improved support for data migration with the SSMS Import/Export Wizard.
- Support for IS_MEMBER, IS_ROLEMEMBER, and HAS_PERMS_BY_NAME functions.
- Support for syslanguages, sys.indexes, sys.all_views, sys.database_files, sys.sql_modules, sys.system_sql_modules, sys.all_sql_modules, sys.xml_schema_collections, sys.dm_hadr_database_replica_states, sys.data_spaces, sys.database_mirroring, sys.database_role_members catalogs.
- Support for sp_sproc_columns, sp_sproc_columns_100, sp_helprole, sp_helprolemember system stored procedures.
- Support for Japanese_CS_AS, Japanese_CI_AI, Japanese_CI_AS collations.
- Babelfish now supports CHARINDEX substring searches on systems using nondeterministic collations.
- Babelfish now supports PATINDEX, and supports arguments to STRING_SPLIT that are collated using a case-insensitive collation.
- Query plan output is generated following SET BABELFISH_SHOWPLAN_ALL ON (and OFF) and SET BABELFISH_STATISTICS PROFILE ON (OFF). This will generate PostgreSQL-style query plan information for T-SQL queries in Babelfish. Make sure these SET statements are identical to existing T-SQL statements, but with the added BABELFISH\_ prefix.

###### Additional improvements and enhancements

- Cross–database references outside the current database, with a 3-part object name, for SELECT,SELECT..INTO, INSERT, UPDATE, DELETE.
- CREATE ROLE (AUTHORIZATION clause not supported), DROP ROLE, ALTER ROLE.
- Babelfish now maps the error code for @@ERROR=213. For more information on error handling, see [Managing Babelfish error handling.](../AuroraUserGuide/babelfish-strict.md "../AuroraUserGuide/babelfish-strict.md")
- Fixed an issue with SUBSTRING(CHARINDEX()) variable assignment that caused Babelfish to become unavailable.
- Fixed an issue with INSERT INTO...with OUTPUT clause that resulted in a `Number of given values doesn't match target table definition` error.
- Fixed an issue that caused DELETE with OUTPUT INTO temporary table statements to return a `WITH query 'nnnnnnnnnnn' doesn't have a RETURNING clause` error.
- Fixed an issue that caused LEFT OUTER JOIN to fail with a `Sqlcmd:
Error: Internal error at ReadAndHandleColumnData (Reason: Error reading
column data)` error. This issue was a regression introduced in
  Babelfish 1.1.0. If your Babelfish for Aurora PostgreSQL DB cluster runs
  Babelfish version 1.1.0 and you get this error, we recommend that you
  upgrade to Aurora PostgreSQL 13.7 to obtain this fix.
- Fixed an invalid syntax error using the GETUTCDATE() and SYSUTCDATETIME() built-in functions.
- Fixed an issue where numeric overflow conditions using SUM() and AVG() functions caused a TDS error.
- Fixed an issue with .NET applications calling store procedures for a DataTable object that resulted in a datatype mismatch and disallowed implicit casting error.

## Babelfish for Aurora PostgreSQL 1.x versions (includes some deprecated versions)

###### Version updates

- [Babelfish for Aurora PostgreSQL 1.5](#AuroraBabelfish.Updates.15X "#AuroraBabelfish.Updates.15X")
- [Babelfish for Aurora PostgreSQL 1.4 (Deprecated)](#AuroraBabelfish.Updates.14X "#AuroraBabelfish.Updates.14X")
- [Babelfish for Aurora PostgreSQL 1.3 (Deprecated)](#AuroraBabelfish.Updates.13X "#AuroraBabelfish.Updates.13X")
- [Babelfish for Aurora PostgreSQL 1.2 (Deprecated)](#AuroraBabelfish.Updates.12X "#AuroraBabelfish.Updates.12X")
- [Babelfish for Aurora PostgreSQL 1.1 (Deprecated)](#AuroraBabelfish.Updates.11X "#AuroraBabelfish.Updates.11X")
- [Babelfish for Aurora PostgreSQL 1.0 (Deprecated)](#AuroraBabelfish.Updates.10X "#AuroraBabelfish.Updates.10X")

### Babelfish for Aurora PostgreSQL 1.5

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.9. For more information about the improvements in Aurora PostgreSQL 13.9, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
Babelfish for Aurora PostgreSQL 1.5 adds a new feature and an enhancement. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 1.5.0,
  January 20, 2023](#AuroraBabelfish.Updates.150 "#AuroraBabelfish.Updates.150")

#### Aurora Babelfish release 1.5.0,

January 20, 2023

###### New features

- Babelfish now supports Zero-downtime patching (ZDP). For more information, see
  [Minor
  release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor")
  in the _Amazon Aurora User Guide_.

###### High priority stability enhancements

- Fixed an issue related to money operator class during minor version upgrade from 13.4 to 13.5 or later due to which the upgrade was failing.

### Babelfish for Aurora PostgreSQL 1.4 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.8. For more information about the improvements in Aurora PostgreSQL 13.8, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
The following issues are resolved in Babelfish for Aurora PostgreSQL 1.4 release. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Aurora Babelfish release 1.4.1, December 13, 2022](#AuroraBabelfish.Updates.141 "#AuroraBabelfish.Updates.141")
- [Aurora Babelfish release 1.4.0, November 9, 2022](#AuroraBabelfish.Updates.140 "#AuroraBabelfish.Updates.140")

#### Aurora Babelfish release 1.4.1, December 13, 2022

- Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.8.

####

Aurora Babelfish release 1.4.0, November 9, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

###### High priority stability enhancements

- Fixed error handling in sp_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
- Fixed error handling in SSL/TLS handshake for some client drivers.

###### Additional improvements

- Fixed the babelfishpg_tds extension to correctly allocate the shared memory size used by the extension.

### Babelfish for Aurora PostgreSQL 1.3 (Deprecated)

This release of Aurora Babelfish is provided with Aurora PostgreSQL 13.7. For more information about the improvements in Aurora PostgreSQL 13.7, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
The following issues are resolved in Babelfish for Aurora PostgreSQL 1.3 release. For more information about Babelfish for Aurora PostgreSQL,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Babelfish for Aurora PostgreSQL release 1.3.3, December 14, 2022](#AuroraBabelfish.Updates.133 "#AuroraBabelfish.Updates.133")
- [Babelfish for Aurora PostgreSQL release 1.3.2, October 18, 2022](#AuroraBabelfish.Updates.132 "#AuroraBabelfish.Updates.132")
- [Babelfish for Aurora PostgreSQL release 1.3.1, July 6, 2022](#AuroraBabelfish.Updates.131 "#AuroraBabelfish.Updates.131")
- [Babelfish for Aurora PostgreSQL release 1.3.0, June 9, 2022](#AuroraBabelfish.Updates.130 "#AuroraBabelfish.Updates.130")

####

Babelfish for Aurora PostgreSQL release 1.3.3, December 14, 2022

- Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.7.

####

Babelfish for Aurora PostgreSQL release 1.3.2, October 18, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

###### High priority stability enhancements

- Fixed error handling in sp_prepare calls which can cause a server crash when a large number of parameters are sent by the application. Babelfish currently supports a maximum of 100 parameters for a procedure or function.
- Fixed error handling in SSL/TLS handshake for some client drivers.

####

Babelfish for Aurora PostgreSQL release 1.3.1, July 6, 2022

- Fixed the babelfishpg_tds extension to correctly allocate the shared memory size used by the extension.

####

Babelfish for Aurora PostgreSQL release 1.3.0, June 9, 2022

- Fixed an issue with SUBSTRING(CHARINDEX()) variable assignment that caused Babelfish to become unavailable.
- Fixed an issue with INSERT INTO...with OUTPUT clause that resulted in a `Number of given values doesn't match target table definition` error.
- Fixed an issue that caused DELETE with OUTPUT INTO temporary table statements to return a `WITH query 'nnnnnnnnnnn' doesn't have a RETURNING clause` error.
- Fixed an issue that caused LEFT OUTER JOIN to fail with a `Sqlcmd:
Error: Internal error at ReadAndHandleColumnData (Reason: Error reading
column data)` error. This issue was a regression introduced in
  Babelfish 1.1.0. If your Babelfish for Aurora PostgreSQL DB cluster runs
  Babelfish version 1.1.0 and you get this error, we recommend that you
  upgrade to Aurora PostgreSQL 13.7 to obtain this fix.

### Babelfish for Aurora PostgreSQL 1.2 (Deprecated)

This release of Babelfish is provided with Aurora PostgreSQL 13.6. For more information about the improvements in Aurora PostgreSQL 13.6, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
The following issues are resolved in Babelfish 1.2 release. For more information about Babelfish,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Babelfish for Aurora PostgreSQL release 1.2.4, December 15, 2022](#AuroraBabelfish.Updates.124 "#AuroraBabelfish.Updates.124")
- [Babelfish for Aurora PostgreSQL release 1.2.3, October 18, 2022](#AuroraBabelfish.Updates.123 "#AuroraBabelfish.Updates.123")
- [Babelfish for Aurora PostgreSQL release 1.2.2, July 18, 2022](#AuroraBabelfish.Updates.122 "#AuroraBabelfish.Updates.122")
- [Babelfish for Aurora PostgreSQL release 1.2.1, April 27, 2022](#AuroraBabelfish.Updates.121 "#AuroraBabelfish.Updates.121")
- [Babelfish for Aurora PostgreSQL release 1.2.0, March 29, 2022](#AuroraBabelfish.Updates.120 "#AuroraBabelfish.Updates.120")

####

Babelfish for Aurora PostgreSQL release 1.2.4, December 15, 2022

- Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.6.

####

Babelfish for Aurora PostgreSQL release 1.2.3, October 18, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

####

Babelfish for Aurora PostgreSQL release 1.2.2, July 18, 2022

- Fixed an issue causing outer join queries to sometimes fail with an internal error message.
- Fixed the babelfishpg_tds extension to correctly allocate the shared memory size used by the extension.

####

Babelfish for Aurora PostgreSQL release 1.2.1, April 27, 2022

- Fixed an issue that caused Babelfish to become unavailable after working with temporary tables.
- Fixed an issue that prevented successful minor version upgrade from a Babelfish for Aurora PostgreSQL 13.4 or 13.5 DB cluster to Aurora PostgreSQL 13.6.
- Fixed an issue that prevented transferring data to a table with identity columns using the SQL Server
  Management Studio import and export wizard.

####

Babelfish for Aurora PostgreSQL release 1.2.0, March 29, 2022

In addition to the new features and improvements in the following list, Babelfish for Aurora PostgreSQL 1.2.0 adds several features that currently have limited implementations. These
features are available for use but don't yet have complete parity with T-SQL syntax or Microsoft SQL Server.
For more information, see [Features
with limited implementation](../AuroraUserGuide/babelfish-compatibility.md#babelfish-compatibility.tsql.limited-implementation "../AuroraUserGuide/babelfish-compatibility.md#babelfish-compatibility.tsql.limited-implementation").

- Casing (upper-case, lower-case) of column names as created with T-SQL is now retained. That
  is, `SELECT * FROM `table`` returns the
  column names using the same casing as used when the table was created at the TDS
  endpoint.
- INSTEAD-OF triggers are now supported on tables (tables only, not views).
- Support for system-defined global variables @@DBTS, @@LOCK_TIMEOUT, @@SERVICENAME.
- Support for syntax SET LOCK_TIMEOUT.
- Support for datatypes TIMESTAMP and ROWVERSION.
- Support for built-in functions COLUMNS_UPDATED, UPDATE, FULLTEXTSERVICEPROPERTY,
  ISJSON, JSON_QUERY, JSON_VALUE, HAS_DBACCESS, SUSER_SID, SUSER_SNAME, IS_SRVROLEMEMBER.
- Full support for the CHECKSUM function. This function now
  supports \* and multiple columns (`CHECKSUM ( * | expression [ ,...n ] )`).
- Full support for the SCHEMA_ID function. This function
  can now be used without any arguments (`SCHEMA_ID ( [ schema_name ] )`).
- Support for DROP IF EXISTS with SCHEMA,
  DATABASE, and USER objects.
- Support for these additional values for CONNECTIONPROPERTY:
  physical_net_transport and client_net_address.
- Support for the these SERVERPROPERTY values:
  EditionID, EngineEdition, LicenseType, ProductVersion, ProductMajorVersion,
  ProductMinorVersion, IsIntegratedSecurityOnly, IsLocalDB,
  IsAdvancedAnalyticsInstalled, IsBigDataCluster, IsPolyBaseInstalled,
  IsFullTextInstalled, and IsXTPSupported.
- Support for these catalogs:
  sys.dm_os_host_info, sys.dm_exec_sessions, sys.dm_exec_connections,
  sys.endpoints, sys.table_types, sys.database_principals,
  sys.sysprocesses, sys.sysconfigures, sys.syscurconfigs, and
  sys.configurations.
- Support for these INFORMATION_SCHEMA catalogs: TABLES,
  COLUMNS, DOMAINS, and TABLE_CONSTRAINTS.
- Support for these system stored procedures:
  sp_table_privileges, sp_column_privileges, sp_special_columns,
  sp_fkeys, sp_pkeys, sp_stored_procedures, xp_qv,
  sp_describe_undeclared_parameters, and sp_helpuser.
- Limited support for creating, altering, and
  dropping database principals (USER objects). Limitations for
  CREATE/ALTER/DROP syntax with USER objects are as follows:
  - For CREATE USER, you can specify the
    FOR/FROM LOGIN and DEFAULT_SCHEMA options only.
  - For ALTER USER, you can specify DEFAULT_SCHEMA
    option only.

- Limited support for the SET FMTONLY ON command. Setting this command ON suppresses the execution of SELECT statements only. It doesn't suppress the execution of other statements.
- Support for granting and revoking (GRANT/REVOKE) permisions for
  database principals only (not database roles). Support
  includes GRANT OPTION and REVOKE..CASCADE options for SELECT, INSERT,
  UPDATE, DELETE, REFERENCES, EXECUTE, and ALL [PRIVILEGES].
- Support for WITH AUTHORIZATION on CREATE SCHEMA.
- Support for the following new escape hatches and escape hatch functionality:

      + Restore all default settings for escape hatches for your
       Babelfish DB instance by passing
       `default` as the second argument to the `sp_babelfish_configure`
       stored procedure.
      + A new escape hatch, `escape_hatch_ignore_dup_key` (default=strict)
       controls the IGNORE\_DUP\_KEY option in CREATE/ALTER TABLE and CREATE INDEX statements.
       When IGNORE\_DUP\_KEY=ON, an error is raised unless escape\_hatch\_ignore\_dup\_key is set to `'ignore'`.
      + Added support for the `ignore` option on the `escape_hatch_storage_options`
       escape hatch. When set to `ignore`, Babelfish ignores
       errors raised in the following cases:




      	- Ignores errors raised in the ON clause in a
      	 CREATE DATABASE statement.
      	- Ignores errors raised by CREATE INDEX when used
      	 with SORT\_IN\_TEMPDB, DROP\_EXISTING, or ONLINE options.

  For details, see
  [Managing Babelfish error handling](../AuroraUserGuide/babelfish-strict.md#babelfish-escape_hatches "../AuroraUserGuide/babelfish-strict.md#babelfish-escape_hatches").

- The msdb system database is always present, and has dbid=4. For more information,
  see [Babelfish architecture](../AuroraUserGuide/babelfish.md#babelfish-architecture "../AuroraUserGuide/babelfish.md#babelfish-architecture").
- For a list of features supported in each Babelfish release, see
  [Supported
  functionality in Babelfish by version](../AuroraUserGuide/babelfish-compatibility.md "../AuroraUserGuide/babelfish-compatibility.md").

### Babelfish for Aurora PostgreSQL 1.1 (Deprecated)

This release of Babelfish is provided with Aurora PostgreSQL 13.5. For more information about the improvements in Aurora PostgreSQL 13.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
The following issues are resolved in Babelfish 1.1 release. For more information about Babelfish,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Babelfish for Aurora PostgreSQL release 1.1.2, December 16, 2022](#AuroraBabelfish.Updates.112 "#AuroraBabelfish.Updates.112")
- [Babelfish for Aurora PostgreSQL release 1.1.1, October 18, 2022](#AuroraBabelfish.Updates.111 "#AuroraBabelfish.Updates.111")
- [Babelfish for Aurora PostgreSQL release 1.1.0, February 25, 2022](#AuroraBabelfish.Updates.110 "#AuroraBabelfish.Updates.110")

####

Babelfish for Aurora PostgreSQL release 1.1.2, December 16, 2022

- Fixed an issue that prevented successful minor version upgrade from Babelfish for Aurora PostgreSQL 13.4 DB cluster to Aurora PostgreSQL 13.5.

####

Babelfish for Aurora PostgreSQL release 1.1.1, October 18, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

####

Babelfish for Aurora PostgreSQL release 1.1.0, February 25, 2022

Babelfish for Aurora PostgreSQL version 1.1.0 adds support for the following Microsoft SQL Server functionality and T-SQL commands.
For more information, see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

- Unique indexes or UNIQUE constraints on nullable columns. To use this
  capability, change the `escape_hatch_unique_constraint` to
  `'ignore'`. For more information, see [Managing
  Babelfish error handling](../AuroraUserGuide/babelfish-strict.md#babelfish-escape_hatches "../AuroraUserGuide/babelfish-strict.md#babelfish-escape_hatches")
- Reference transition tables from triggers with multiple DML actions.
- Identifiers that have leading dot characters.
- The COLUMNPROPERTY function (limited to CharMaxLen and AllowsNull properties).
- System-defined @@ variables: @@CURSOR_ROWS, @@LOCK_TIMEOUT, @@MAX_CONNECTIONS, @@MICROSOFTVERSION, @@NESTLEVEL, and @@PROCID.
- Built-in functions: CHOOSE, CONCAT_WS, CURSOR_STATUS, DATEFROMPARTS, DATETIMEFROMPARTS,
  ORIGINAL_LOGIN, SCHEMA_NAME (now fully supported), SESSION_USER, SQUARE, and
  TRIGGER_NESTLEVEL supported (but only without arguments).
- System stored procedures: sp_columns, sp_columns_100, sp_columns_managed, sp_cursor,
  sp_cursor_list, sp_cursorclose, sp_cursorexecute, sp_cursorfetch,
  sp_cursoropen, sp_cursoroption, sp_cursorprepare, sp_cursorprepexec,
  sp_cursorunprepare, sp_databases, sp_datatype_info, sp_datatype_info_100,
  sp_describe_cursor, sp_describe_first_result_set,
  sp_describe_undeclared_parameters, sp_oledb_ro_usrname,
  sp_pkeys, sp_prepare, sp_statistics, sp_statistics_100,
  sp_tablecollations_100, sp_tables, and
  sp_unprepare.
- For a list of features supported in each Babelfish release, see
  [Supported
  functionality in Babelfish by version](../AuroraUserGuide/babelfish-compatibility.md "../AuroraUserGuide/babelfish-compatibility.md").

### Babelfish for Aurora PostgreSQL 1.0 (Deprecated)

This release of Babelfish is provided with Aurora PostgreSQL 13.4. For more information about the improvements in Aurora PostgreSQL 13.5, see [Amazon Aurora PostgreSQL updates](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
The following issues are resolved in Babelfish 1.0 release. For more information about Babelfish,
see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Releases

- [Babelfish for Aurora PostgreSQL release 1.0.1, October 18, 2022](#AuroraBabelfish.Updates.101 "#AuroraBabelfish.Updates.101")
- [Babelfish for Aurora PostgreSQL release 1.0.0, October 28, 2021](#AuroraBabelfish.Updates.100 "#AuroraBabelfish.Updates.100")

####

Babelfish for Aurora PostgreSQL release 1.0.1, October 18, 2022

###### Security enhancements

- Fixed critical issues in Babelfish due to incorrect handling of user input for some application features.
  This is tracked in [https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj](https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj "https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-m399-rrc8-j6fj").

####

Babelfish for Aurora PostgreSQL release 1.0.0, October 28, 2021

- Babelfish for Aurora PostgreSQL version 1.0.0 supports Babelfish 1.0.0 which extends your Amazon Aurora PostgreSQL database with
  the ability to accept database connections from Microsoft SQL Server clients. For more information, see
  see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").
