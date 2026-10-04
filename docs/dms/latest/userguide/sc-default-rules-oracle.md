

# Oracle to PostgreSQL
<a name="sc-default-rules-oracle"></a>

This section describes the default rules that DMS Schema Conversion applies when it converts an Oracle source database to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL.

Oracle and PostgreSQL differ in how they handle identifier case, organize code into packages, provide built-in functions, and define data types. Some Oracle objects have no direct equivalent in PostgreSQL. DMS Schema Conversion resolves these differences automatically where it can. When an object needs manual work or review, it reports an action item. The following topics describe the default rules for each area of the conversion.

**Topics**
+ [Object type rules](sc-default-rules-object-types-oracle.md)
+ [Naming rules](sc-default-rules-naming-oracle.md)
+ [Data type rules](sc-default-rules-data-types-oracle.md)
+ [Built-in function and system object rules](sc-default-rules-builtins-oracle.md)