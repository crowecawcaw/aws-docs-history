

# Default conversion rules
<a name="sc-default-conversion-rules"></a>

DMS Schema Conversion applies a set of *default conversion rules* in every migration project. The following sections list those defaults for each supported source and target pair. Use them to predict the code that DMS Schema Conversion produces, and to decide where to change the result with conversion settings or transformation rules.

These rules cover Oracle and Microsoft SQL Server sources that you convert to Amazon Aurora PostgreSQL or Amazon RDS for PostgreSQL targets.

## How the default rules are organized
<a name="sc-default-rules-organization"></a>

DMS Schema Conversion groups its default rules into the following kinds. Each kind decides a different part of the conversion, and each has its own way to override the default.


| Rule kind | What it decides | Override | 
| --- | --- | --- | 
| Object type rules | Which kinds of database object are converted at all, and what they become | Conversion settings | 
| Naming rules | Target schema, table, and column names — case folding, schema merging, and length limits | Conversion settings; transformation rules | 
| Data type rules | The target data type for every source data type, per usage context | Conversion settings; transformation rules | 
| Built-in function and system object rules | How the built-in functions, packages, procedures, and system objects of your source database are converted | Conversion settings | 

## Overriding the defaults
<a name="sc-default-rules-overriding"></a>

You can override the default conversion rules in two ways.
+ **Conversion settings** change behavior for the whole project — data type mappings, whether object names are lowercased, and how source database and schema names combine into the target schema name. For more information, see [Specifying schema conversion settings for migration projects](schema-conversion-settings.md).
+ **Transformation rules** change behavior for selected objects — renaming, adding prefixes or suffixes, and changing case for specific schemas, tables, or columns. For more information, see [Transformation rules in DMS Schema Conversion](sc-transformation-rules.md).