

# SQL Server to PostgreSQL
<a name="sc-default-rules-sqlserver"></a>

This section describes the default rules that DMS Schema Conversion applies when it converts a Microsoft SQL Server source database to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL.

SQL Server and PostgreSQL differ in how they handle identifier case, qualify objects by database and schema, name parameters and variables, and provide built-in functions. Some SQL Server objects have no direct equivalent in PostgreSQL. DMS Schema Conversion resolves these differences automatically where it can. When an object needs manual work or review, it reports an action item. The following topics describe the default rules for each area of the conversion.

**Topics**
+ [Object type rules](sc-default-rules-object-types-sqlserver.md)
+ [Naming rules](sc-default-rules-naming-sqlserver.md)
+ [Data type rules](sc-default-rules-data-types-sqlserver.md)
+ [Built-in function and system object rules](sc-default-rules-builtins-sqlserver.md)